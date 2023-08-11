FROM python:3.10

LABEL Maintainer="ak4m410x01"

SHELL [ "/bin/bash", "-c" ]

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "python3 manage.py runserver 0.0.0.0:8000" ]
