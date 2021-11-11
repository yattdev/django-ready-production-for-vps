# ready-start-django-api
A ready to start django rest api with User 

# How to setup:
**1** create a file named ```whatever.env``` and define your variables environment inside like so:
```
ENV=DEVELOPPEMENT
POSTGRES_DB=your_db_name
POSTGRES_USER=user_define_in_dockerfile
POSTGRES_PASSWORD=yourpassword ()
SECRET_KEY='yoursupersecretkey'
DEBUG=True
POSTGRES_HOST=
```
**2** Declare your whatever.env file inside docker-compose 
```
services:
    web:
    ...
        env_file:
            - whatever.env # <----- Your env file here
    db:
    ...
        env_file:
            - whatever.env # <----- Your env file here

```

**3**: Build image and Start container with 
``` docker-compose up --build ```

~~ Enjoy it ! ~~
