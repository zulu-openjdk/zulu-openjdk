FROM alpine:3.20

ENV LANG en_US.UTF-8
ARG ZULU_KEY_SHA256=6c6393d4755818a15cf055a5216cffa599f038cd508433faed2226925956509a
RUN set -ex && \
    apk update && apk upgrade --no-cache && \
    wget --quiet https://cdn.azul.com/public_keys/alpine-signing@azul.com-5d5dc44c.rsa.pub -P /etc/apk/keys/ && \
    echo "${ZULU_KEY_SHA256}  /etc/apk/keys/alpine-signing@azul.com-5d5dc44c.rsa.pub" | sha256sum -c - && \
    apk --repository https://repos.azul.com/zulu/alpine --no-cache add zulu11-jre-headless~=11.0.29 tzdata

ENV JAVA_HOME=/usr/lib/jvm/zulu11
