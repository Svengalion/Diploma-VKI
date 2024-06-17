FROM python

RUN apt-get update && apt-get install -y postgresql-client

RUN mkdir /Back

WORKDIR ./Back

COPY . .

RUN pip install --no-cache-dir -r app/requirements.txt

RUN chmod a+x app/docker/*.sh