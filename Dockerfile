FROM python:3.9-alpine
ADD . /data
WORKDIR /data
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]
