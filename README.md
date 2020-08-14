# Django Task

**NOTE:**

Please install `Docker version 19.03.10` or `above` on your system before starting.

### Installation:

`git clone https://github.com/krishna-mathuria/DjangoTask.git`

`docker-compose up`


### To create a superuser:

`sudo docker-compose run web python3 manage.py createsuperuser`

### Some Important URLs:


To create a user:

`/users/`  

Request: `POST`

Required Fields: `username`, `email`, `password`


To receive email with reset password link:  

`/users/reset_password/`

Request: `GET`

Required Fields: `email`


To Login/generate JWT:                      

`/jwt/create/`

Request: `POST`

Required Fields: `username`, `password`


To add the user to the specified group:

`/addgroup/`

Request: `POST`

Required Fields: `group`



To get a list of all students for the teachers:

`/students`

Request: `GET`


To get a ist of all the users for Super-admins:

`/allusers`

Request: `GET`
