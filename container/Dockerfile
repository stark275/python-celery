FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /django

RUN apt-get update 

# Install necessary package for django runtime
RUN apt-get install -y default-libmysqlclient-dev \
        pkg-config \
        libpango-1.0-0  \ 
        libharfbuzz0b \
        libpangoft2-1.0-0 \
        libpangocairo-1.0-0 \
        libxml2-dev \ 
        libxslt-dev \
        libffi-dev \
        libcairo2-dev \
        libpango1.0-dev --fix-missing

# Install gcc
RUN apt-get install -y build-essential

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install mysqlclient==2.2.0
# RUN pip3 install mysql-connector-python==8.0.26
RUN pip3 install django-dump-die==0.1.7
RUN apt-get install nano
RUN pip3 install pika
RUN pip3 install Redis

RUN adduser --disabled-password --gecos '' django
RUN echo $(id -u django) > /uid.txt
# USER django

RUN pip3 install gunicorn
RUN pip3 install uvicorn==0.23.1
RUN pip3 install asgiref==3.7.2
RUN pip3 install channels==4.0.0
RUN pip3 install channels-redis==3.3.1
RUN pip3 install 'uvicorn[standard]'


COPY ./ ./
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8003" ]
EXPOSE 8003
