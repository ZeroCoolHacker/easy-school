# Easy School

This is a school management system that uses
[Django Admin](https://www.google.com/search?client=opera&q=django+admin&sourceid=opera&ie=UTF-8&oe=UTF-8) to 
do most of the work of managing students, fee submissions, teacher records etc..

Setting up Easy School is very easy.
## Want to Use?
You can clone this branch and use it right now using any of the methods mentioned below

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
## Building with Docker
First run `docker-compose` to build the container:

```bash
docker-compose build
```

Then, run the following command to create the superuser:

```bash
docker-compose run web python manage.py createsuperuser
```

Finally, the Docker container can be launched with the following command:

```bash
docker-compose up
```

The server should be responding at 127.0.0.1:8000


## Contributing

Just follow the steps above to setup your environment.
Read the [Contribution Guide](CONTRIBUTION.md)
If you have any more questions you can join the gitter room [![Gitter](https://badges.gitter.im/ZeroCoolHacker/community.svg)](https://gitter.im/ZeroCoolHacker/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
## To do

- [x] Manage Students Record in admin
- [x] Submit fees in admin
- [x] Show last submitted fee along with students
- [x] Link Students to different Courses
- [x] Search the record by various fields
- [x] Minimize the number of queries for each view
- [x] Add Teachers Record to admin
- [x] Add Teachers Salary Record to admin
- [x] Export Data in csv format from admin
- [ ] Add graph comparing teacher salaries given vs student's fee collected


## Licensing
This Project is Licensed under [GLWTPL](LICENSE)

## Hall of fame
Everyone who contributes to easy-school gets a spot here.
* [@ZeroCoolHacker](https://github.com/ZeroCoolHacker)
* [@Argetan](https://github.com/Argetan)
* [@ismailuddin](https://github.com/ismailuddin)
* [@davidkarabas](https://github.com/davidkarabas)
* [@mmoomocow](https://github.com/mmoomocow)
* [@MohanChhabaria](https://github.com/MohanChhabaria)
* [@mrunderline](https://github.com/mrunderline)
