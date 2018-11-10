
FROM nikozero01/flask

MAINTAINER Diego A Carabali

RUN apt-get update && apt-get install build-essential python3-pip python3-dev -y

RUN pip3 install pandas numpy

RUN pip3 install matplotlib

#COPY app.py /myapp/app.py

#COPY gapminder.tsv /myapp/gapminder.tsv

#COPY /templates/test.html /myapp/templates/test.html

#ENTRYPOINT [ "python3" ]

#CMD [ "/myapp/app.py" ]
