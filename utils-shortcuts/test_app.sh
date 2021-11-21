#  A shell script to test a given django app directory
realpath --relative-to='.' $1 | sed 's/.py//' | sed 's/\//./g' | xargs -I {} python manage.py test {}
