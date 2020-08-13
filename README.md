# Django Task

**NOTE:**

1. Please install `python3.7` or `above` on your system before starting.

2. Suggested `Docker version 19.03.10`

### Installation:

`git clone https://github.com/krishna-mathuria/DjangoTask.git`


##### 1) First we need to setup a database:

Run the following docker command:

```
docker run --name=postgres_db -d -e POSTGRES_USER='postgres' -e POSTGRES_PASSWORD=postgres -e POSTGRES_DBNAME=postgres -p 5434:5432 postgres
```

##### 2) Setting up local python env:

You are free to use your own python development environment, with which you are comfortable. Just in case if you want to follow along.

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip3 install -r requirements.txt`

##### 3) Run the local dev server and migrate DB

Run the following commands before running the server or creating any `superuser`.

1. `python3 manage.py migrate`
2. `python3 manage.py creategroups`

And Finally run:

`python3 manage.py runserver`

**NOTE:**

Please ensure your database is running after you setup. To start the database run
`docker start postgres_db`
