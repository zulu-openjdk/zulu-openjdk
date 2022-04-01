FROM alpine:3.13

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN wget --quiet https://cdn.azul.com/public_keys/alpine-signing@azul.com-5d5dc44c.rsa.pub -P /etc/apk/keys/ && \
    apk --repository https://repos.azul.com/zulu/alpine --no-cache add zulu8-jre=8.0.292-r1

ENV JAVA_HOME=/usr/lib/jvm/zulu8-ca
