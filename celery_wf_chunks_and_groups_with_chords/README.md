# Celery-Chunks-and-Groups-with-Chords
An example which executes a Celery task using Celery Groups and Celery chunks and monitors memory usage

You can change number of tasks, chunk size and loop limit in `constants.py`

# Steps

## 1- Install Redis-Server

### Install redis on OSX
`brew install redis`

`brew upgrade redis`

### Install Redis on Ubuntu
`sudo apt-get install redis-server`

### Start Redis Server
`sudo service redis-server start`

## 2- Create a virtualenv and install requirements.txt

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## 3- Run Celery worker

RUN file run_celery.py or command -> `celery -A tasks worker -n chords --loglevel=info`

## 4- Run `monitor_usage.py`

`python monitor_usage.py`

## 5- Monitor Celery Flower
RUN file run_flower.py or command `celery -A tasks flower --port=5511 --loglevel=info`