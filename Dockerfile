FROM gliderlabs/alpine:latest

# Install alpine packages
RUN apk add --update \
    python3 \
    python3-dev \
    build-base \
    nodejs \
    nodejs-npm \
    py-pip \
    jpeg-dev \
    zlib-dev \
  && python3 -m pip install virtualenv \
  && python3 -m pip install --upgrade pip setuptools \
  && rm -rf /var/cache/apk/*

ENV LIBRARY_PATH=/lib:/usr/lib

# Create project directory and copy requirements
RUN mkdir /ceiphrcom
WORKDIR /ceiphrcom
COPY requirements.txt /ceiphrcom/

# Install node modules
RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install -g sass yuglify

# Creating a virtual environment for project dependencies
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python3 packages
RUN python3 -m pip install -U pip
RUN python3 -m pip install -r requirements.txt

# Collect static files
COPY . /ceiphrcom/
RUN python3 /ceiphrcom/ceiphr_proj/manage.py collectstatic --noinput
