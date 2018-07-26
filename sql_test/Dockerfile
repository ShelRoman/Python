FROM ubuntu:latest
ENV pqver=10
WORKDIR /sql_task
ADD . /sql_task
RUN apt-get update && apt install -yq postgresql-$pqver postgresql-client-$pqver postgresql-contrib-$pqver
RUN /etc/init.d/postgresql start
