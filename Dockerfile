FROM fedora
MAINTAINER https://github.com/wkicior
RUN yum update -y
RUN yum install -y python-pip wget
ADD requirements .
RUN pip install -r requirements

ONBUILD ADD . /app
ONBUILD WORKDIR /app

EXPOSE 80
WORKDIR /app
CMD python server.py

