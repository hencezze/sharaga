FROM python:3.11.2-buster
WORKDIR /opt/server/
COPY server.py /opt/server/server.py
COPY index.html /opt/server/index.html
EXPOSE 8080
CMD ["python3", "server.py"]
