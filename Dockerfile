FROM alpine:latest

RUN apk add --no-cache --upgrade python3 \
                       py-pip \
    && rm -rf /var/cache/apk/* \
    && pip3 install --upgrade pip requests

COPY script/starships.py /script/starships.py

CMD ["python3", "/script/starships.py"]
