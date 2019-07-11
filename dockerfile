FROM python

WORKDIR /home/python

RUN apt-get update && apt-get install -y openbabel python-chemfp python-openbabel libopenbabel-dev libchemistry-openbabel-perl

RUN pip install django

COPY . .

ENTRYPOINT [ "bash" ] 