#  A shell script to test a given django test file
echo $1 | sed 's/.py//' | sed 's/\//./g' | xargs -I {} python manage.py test {}
