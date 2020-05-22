FROM  docker.io/centos:latest 
COPY ./requirements.txt /
WORKDIR /mysite
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && yum install python-devel -y && yum install mysql-devel -y &&  yum install gcc -y && pip install -r /requirements.txt && yum install pcp-pmda-nginx -y 
