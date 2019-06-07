FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ceiphrcom
WORKDIR /ceiphrcom
COPY requirements.txt /ceiphrcom/
RUN pip install -r requirements.txt
COPY . /ceiphrcom/