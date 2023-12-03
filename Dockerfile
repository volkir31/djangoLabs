FROM python:latest

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]