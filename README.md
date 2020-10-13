# Easy School
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/mrunderline"><img src="https://avatars2.githubusercontent.com/u/23085360?v=4" width="100px;" alt=""/><br /><sub><b>ali madihi bidgoli</b></sub></a><br /><a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=mrunderline" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mmoomocow"><img src="https://avatars1.githubusercontent.com/u/44288823?v=4" width="100px;" alt=""/><br /><sub><b>mmoomocow</b></sub></a><br /><a href="https://github.com/ZeroCoolHacker/easy-school/issues?q=author%3Ammoomocow" title="Bug reports">🐛</a> <a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=mmoomocow" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/davidkarabas"><img src="https://avatars0.githubusercontent.com/u/56340850?v=4" width="100px;" alt=""/><br /><sub><b>davidkarabas</b></sub></a><br /><a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=davidkarabas" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/adamzavacky"><img src="https://avatars3.githubusercontent.com/u/44172077?v=4" width="100px;" alt=""/><br /><sub><b>adamzavacky</b></sub></a><br /><a href="#design-adamzavacky" title="Design">🎨</a> <a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=adamzavacky" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jvdoorn"><img src="https://avatars1.githubusercontent.com/u/19390615?v=4" width="100px;" alt=""/><br /><sub><b>Julian van Doorn</b></sub></a><br /><a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=jvdoorn" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/MohanChhabaria"><img src="https://avatars2.githubusercontent.com/u/63086398?v=4" width="100px;" alt=""/><br /><sub><b>Mohan Chhabaria</b></sub></a><br /><a href="#design-MohanChhabaria" title="Design">🎨</a> <a href="https://github.com/ZeroCoolHacker/easy-school/commits?author=MohanChhabaria" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
