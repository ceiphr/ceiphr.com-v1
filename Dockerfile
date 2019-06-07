FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ceiphrcom
WORKDIR /ceiphrcom
COPY requirements.txt /ceiphrcom/
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /ceiphrcom/
RUN python /ceiphrcom/ceiphr_proj/manage.py collectstatic --noinput