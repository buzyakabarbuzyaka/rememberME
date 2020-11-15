FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

WORKDIR /app
ADD . /app

CMD python main.py