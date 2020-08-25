FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

HEALTHCHECK CMD curl -fsSL "http://$(hostname --ip-address):9200/_cat/health?h=status" | grep -E '^green'

ENTRYPOINT [ "python" ]
CMD [ "indexer.py" ]