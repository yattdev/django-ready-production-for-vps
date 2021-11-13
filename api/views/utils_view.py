from django.middleware import csrf
from django.http import JsonResponse


#  Return CSRF token
def get_csrf_token(request):
    token = csrf.get_token(request)

    return JsonResponse({'csrf_token': token})
