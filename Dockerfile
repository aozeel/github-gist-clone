#base image
FROM python:3.8
#setup environment variable
ENV DockerHOME=/usr/src/app

# set work directory
#RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && apt-get install -yyq netcat
# install dependencies
RUN pip install --upgrade pip
#copy whole project to your docker home directory. COPY . $DockerHOME
#run this command to install all dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY entrypoint.sh .

#Copy the project
COPY gistclone .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
# port where the Django app runs
#EXPOSE 8000
#start server
#CMD ["python", "gistclone/manage.py", "runserver", "0.0.0.0:8000"]