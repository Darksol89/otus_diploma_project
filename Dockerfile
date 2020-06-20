FROM python:3.6.8
LABEL author=ivan_chistov

WORKDIR /tests

COPY . .

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt

CMD pytest -v --alluredir=allure-report --browser_name=remote --url=http://host.docker.internal:8080