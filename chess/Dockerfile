FROM alpine:latest

RUN apk add --no-cache python3 socat \
    && rm -rf /tmp/* /var/cache/apk/*

RUN adduser -D chess
WORKDIR /home/chess

ADD ./src /home/chess

RUN chmod 755 /home/chess/chess-challenge.py

USER chess

EXPOSE 8164
ENTRYPOINT ["sh", "/home/chess/entrypoint.sh"]
