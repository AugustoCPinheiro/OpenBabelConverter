FROM python

WORKDIR /home/python

COPY ./requirements.txt .

COPY . .

RUN apt-get update && apt-get install -y openbabel python-chemfp python-openbabel libopenbabel-dev libchemistry-openbabel-perl

RUN pip install --upgrade pip && pip install -r requirements.txt


ENTRYPOINT [ "bash" ] 