FROM centos:7
RUN yum makecache
RUN yum -y install epel-release
RUN yum -y install -y python python-pip python-devel git gcc libjpeg-turbo-devel libxml2-devel libxslt-devel postgresql-devel
RUN yum -y clean all

COPY ./requirements/ /tmp/requirements/
RUN pip install -r /tmp/requirements/docker.txt

WORKDIR /app
COPY . /app

EXPOSE 80

CMD ["./bin/run-docker.sh"]
