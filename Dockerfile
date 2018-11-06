
FROM nikozero01/flask

MAINTAINER Diego A Carabali

RUN apt-get update && apt-get install build-essential python3-pip python3-dev -y

RUN pip3 install pandas numpy
