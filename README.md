# django_drf_postgres_auth_tasksapp

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

run the command:

`python manage.py migrate`

finally the project run with: 

`$ python manage.py runserver`

open your browser in: 

`localhost:8000/signup`\
`localhost:8000/signin`\ 
`localhost:8000/task`\
`localhost:8000/task/new`\
`localhost:8000/task/<int:id>`\
`localhost:8000/task/done/<int:id>`\
`localhost:8000/task/edit/<int:id>`\
`localhost:8000/task/delete/<int:id>`\
`localhost:8000/users`\
`localhost:8000/users/done`

