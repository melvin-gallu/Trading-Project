# Dockerfile, Image, Container
FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 5000
ENV FLASK_APP=/code/app/app.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]