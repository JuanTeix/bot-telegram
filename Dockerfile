FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

COPY . .

CMD python3 ./app.py echo "Se esta ejecutando el bot"

