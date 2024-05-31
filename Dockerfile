FROM python

RUN mkdir /Back

WORKDIR ./Back

COPY . .

RUN pip install -r app/requirements.txt

RUN chmod a+x app/docker/*.sh