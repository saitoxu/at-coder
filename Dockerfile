FROM python:3.4-alpine
# RUN pip install --upgrade pip
RUN apk --update-cache \
  add musl \
  linux-headers \
  gcc \
  g++ \
  make \
  gfortran \
  openblas-dev
RUN pip install numpy beautifulsoup4
