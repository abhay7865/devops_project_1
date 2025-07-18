FROM redhat/ubi8

RUN yum install -y python3 python3-pip
RUN pip3 install flask

COPY devops.pro.py /devops.pro.py

ENTRYPOINT [ "python3", "/devops.pro.py" ]
