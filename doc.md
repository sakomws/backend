Login to Postgre db:
```
sudo -u postgres psql
```
List databases:
```
\l
```
Switch database:
```\c
```
Display tables:
```\dt
```

Reinstall Postgres:

First, I deleted config and database

$ sudo pg_dropcluster --stop 9.6 main
Then removed postgresql

$ sudo apt-get remove --purge postgresql postgresql-9.6

Reinstall:

$ sudo apt-get install postgresql postgresql-9.6

$ sudo pg_createcluster 9.6 main

$ sudo chown root.postgres /var/log/postgresql
$ sudo chmod g+wx /var/log/postgresql
