# Core Django imports.
import uuid

from blog.models.category_models import Category
# Blog application imports.
from blog.utils.blog_utils import count_words, read_time
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
# Third party app imports
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

# Get Custom User as User
User = get_user_model()


# A snippet to allow taggableManager to use UUID field
class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items",
    #  on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Article(models.Model):

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    # BLOG MODEL FIELDS
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='articles')
    title = models.CharField(max_length=120, null=False, blank=False)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='articles')
    image = models.ImageField(default='article-default.jpg',
                              upload_to='article_pics')
    image_credit = models.CharField(max_length=250, null=True, blank=True)
    body = RichTextUploadingField(blank=True)
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)
    date_published = models.DateTimeField(null=True,
                                          blank=True,
                                          default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    deleted = models.BooleanField(default=False)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="80" />' %
                         (self.image))

    image_tag.short_description = 'Image'

    class Meta:
        unique_together = ("title", )
        ordering = ('-date_published', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail',
                       kwargs={
                           'username': self.author.username.lower(),
                           'slug': self.slug
                       })

    def clean(self):
        if len(self.title) > 119:
            # Validation for title field
            raise ValidationError(
                f"Error field Title: Max length is {self.title}")

        if len(self.sub_title) > 254:
            # Validation for sub_title field
            raise ValidationError(
                f"Error field Title: Max length is {self.sub_title}")
