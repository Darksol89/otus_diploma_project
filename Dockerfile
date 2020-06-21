FROM python:3.6.8
LABEL author=ivan_chistov

WORKDIR /tests

COPY . .

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt

CMD pytest -v --alluredir=allure-report --browser_name=selenoid-chrome --url=http://172.17.0.1:8080