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

Remove Postgres:

Delete config and database:

```sudo pg_dropcluster --stop 9.6 main```

Delete postgresql:

```sudo apt-get remove --purge postgresql postgresql-9.6```

Reinstall Postgres:
```
sudo apt-get install postgresql postgresql-9.6
sudo pg_createcluster 9.6 main
sudo chown root.postgres /var/log/postgresql
sudo chmod g+wx /var/log/postgresql
```

Check postgres status:
```
/etc/init.d/postgresql status/start/stop```
or:```
sudo service postgresql status```

Check which port listens:```
sudo netstat -nl | grep postgres```

Kill all postgres:```
sudo pkill -u postgres```





