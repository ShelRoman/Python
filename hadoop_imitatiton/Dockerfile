FROM ubuntu:latest
WORKDIR /hadoop_task
ADD . /hadoop_task
RUN \
  apt-get update && \
  apt-get install -y python3.6 && \
  rm -rf /var/lib/apt/lists/*
