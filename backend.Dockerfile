FROM python:3.10

LABEL Maintainer="ak4m410x01"

SHELL [ "/bin/bash", "-c" ]

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt upgrade -y

RUN useradd -r -s /bin/false ak4m410x01
RUN mkdir /home/ak4m410x01
RUN chown ak4m410x01:ak4m410x01 -R /home/ak4m410x01
RUN chown ak4m410x01:ak4m410x01 -R /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "su - ak4m410x01 -s /bin/bash -c 'python3 /app/manage.py runserver 0.0.0.0:8000'" ]
