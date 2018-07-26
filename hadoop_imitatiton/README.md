# Word count in Python streaming
The goal of this task is to write map-reduce job in Hadoop Streaming using python
( http://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html ), i.e.
the mapper and reducer have to be written in Python

# Dependencies
- Internet connection
- Docker installed on your machine ---> https://docs.docker.com/install/#supported-platforms
- Archive with text downloaded

# How to run
- Download files from git and archive with task and put them into one folder
- Create folder `res` inside that folder
- Run terminal/power-shell
- Get to folder with files (using `cd` command)
- Build container `docker build -t %container_name% .`
- After container is built run it `docker run -it -v ${PWD}/res:/hadoop_task/res %container_name%`
- In the container's terminal run `zcat biographies.list.gz | python3.6 mapper.py | sort -k1,1 | python3.6 reducer.py > res/result.txt`
- Files with result will appear in the `'res'` dir under `'result.txt''` name
