FROM python:3.7.13-slim
WORKDIR /usr/src/app
COPY app.py ./
EXPOSE 5000
RUN python3 -m pip install flask
CMD python3 app.py

docker build -t myflaskapp:v1 .
docker images
docker run -itd -p 8080:5000 myflaskapp:v1
docker ps
systemctl status docker
