# Sql test
In this task you are required to write an SQL query to find the most recent version of
each app.

# Dependencies
- Internet connection
- Docker installed on your machine ---> https://docs.docker.com/install/#supported-platforms

# How to run
- Download files from git and put them into one folder
- Run terminal/power-shell
- Get to folder with files (using `cd` command)
- Build container `docker build -t %container_name% .`
- After container is built run it `docker run -it %container_name%`
- In the container's terminal run next commands in order below:
    * `/etc/init.d/postgresql start`
    * `su postgres`
    * `cd /sql_task`
    * `psql`
- Postgres terminal will be opened within it run 2 commands:
    * `\i create_table.sql` - which will use script from file to create table
    * `\i get_most_recent_app.sql` - which will return expected result

