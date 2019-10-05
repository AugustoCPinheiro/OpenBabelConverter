FROM python

WORKDIR /home/python

RUN apt-get update && apt-get install -y openbabel python-chemfp python-openbabel libopenbabel-dev libchemistry-openbabel-perl

RUN pip install --upgrade pip

RUN pip install django && pip install requests && pip install Pillow && pip install numpy

COPY . .

ENTRYPOINT [ "bash" ] 