FROM python:3.6

ENV FLASK_APP run.py

COPY manage.py gunicorn-cfg.py requirements.txt .env ./
COPY app app
COPY authentication authentication
COPY core core
COPY customers customers
COPY Departamentos Departamentos

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
