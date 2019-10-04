FROM python:3.7-alpine

LABEL maintainer="contact@ceiphr.com"

# Labels (DEPRECATED but used for Microbadger)
# http://label-schema.org/rc1/
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="ceiphr/ceiphr.com"
LABEL org.label-schema.description="The portfolio and blog of Ari Birnbaum. Built with Django and Bulma."
LABEL org.label-schema.url="https://ceiphr.com/"
LABEL org.label-schema.vcs-url="https://github.com/ceiphr/ceiphr.com"
LABEL org.label-schema.vcs-ref=$VCS_REF

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV LIBRARY_PATH=/lib:/usr/lib

# Install node modules
RUN apk add --no-cache --update \
    nodejs \
    nodejs-npm \
  && npm config set user 0 \
  && npm config set unsafe-perm true \
  && npm install -g sass yuglify babel-cli \
  && apk del nodejs-npm

# Create project directory and copy requirements
WORKDIR /usr/src/app
COPY requirements/requirements.txt /usr/src/app/requirements.txt

# Install project dependencies
RUN apk add --no-cache --update build-base \
    postgresql-dev \
    jpeg-dev \
    zlib-dev\
  && python3 -m pip install --no-cache --upgrade pip setuptools \
  && python3 -m pip install --no-cache -r requirements.txt \
  && apk del build-base

# Collect static files
COPY ceiphr_proj/ /usr/src/app/

# Entrypoint
RUN chmod 777 /usr/src/app/entrypoint.sh \
    && ln -s /usr/src/app/entrypoint.sh /
CMD ["sh", "/usr/src/app/entrypoint.sh"]
