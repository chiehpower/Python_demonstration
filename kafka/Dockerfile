FROM python:3.11

RUN apt update && apt install -y bsdmainutils curl git mercurial make binutils bison gcc build-essential
RUN pip3 install kafka-python
RUN bash -c 'curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer | bash'

ENV GVM_ROOT /root/.gvm
RUN ["/bin/bash", "-c", "source $GVM_ROOT/scripts/gvm && gvm install go1.18 -B && gvm use go1.18 --default"]

