FROM python:3.10.4-slim-buster

ADD tp3_data_publisher.py /

RUN pip install numpy paho-mqtt

CMD [ "python", "./tp3_data_publisher.py" ]