# Easy School

This is a school management system that uses
[Django Admin](https://www.google.com/search?client=opera&q=django+admin&sourceid=opera&ie=UTF-8&oe=UTF-8) to 
do most of the work of managing students, fee submissions, teacher records etc..

Setting up Easy School is very easy.

## Building

It is best to use the python `virtualenv` tool to build locally:

```bash
> virtualenv venv
> source venv/bin/activate
> git clone https://github.com/ZeroCoolHacker/easy-school .
```
Then you navigate to the base directory of the project and install the requirements in your virtual environment

```bash
> cd easy-school/easy-school
> pip install -r requirements.txt
```
And finally you make migrations to the database, create a super user, and run the server
```bash
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally

```bash
> foreman start
```

# Contributing

Just follow the steps above to setup your environment.
Read the [Contribution Guide](CONTRIBUTION.md)
# To do

- [x] Manage Students Record in admin
- [x] Submit fees in admin
- [x] Show last submitted fee along with students
- [x] Link Students to different Courses
- [x] Search the record by various fields
- [x] Minimize the number of queries for each view
- [x] Add Teachers Record to admin
- [ ] Create Signup and Login view for teachers
- [ ] Attendence Management
- [ ] Result management for different Exams
## Licensing
This Project is Licensed under [GLWTPL](LICENSE)

## Hall of fame
Everyone who contributes to EpPos gets a spot here.
* [@ZeroCoolHacker](https://github.com/ZeroCoolHacker)
* [@Argetan](https://github.com/Argetan)
