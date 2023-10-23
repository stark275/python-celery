FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /deamon
RUN apt-get update 
RUN apt-get install nano
RUN pip3 install mysql-connector-python==8.0.26
RUN pip3 install pika==1.3.2
COPY ./ ./
CMD [ "python3", "--version"]

