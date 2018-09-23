# Easy School

This is a school management system that uses
[Django Admin](https://www.google.com/search?client=opera&q=django+admin&sourceid=opera&ie=UTF-8&oe=UTF-8) to 
do most of the work of managing students, fee submissions, teacher records etc..

Setting up Easy School is very easy.

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv venv
$ source venv/bin/activate
$ git clone https://github.com/ZeroCoolHacker/easy-school .
```
Then you navigate to the base directory of the project and install the requirements in your virtual environment

```sh
$ cd easy-school/easy-school
$ pip install -r requirements.txt
```
And finally you make migrations to the database, create a super user, and run the server
``sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):

```sh
$ foreman start
```
## Licensing

This library is BSD-licensed.

