FROM debian:buster


RUN apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install gnupg software-properties-common && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x219BD9C9 && \
    apt-add-repository "deb http://repos.azulsystems.com/debian stable main" && \
    apt-get -qq update && \
    apt-get -qq -y dist-upgrade && \
    apt-get -qq -y --no-install-recommends install zulu-14=14.28+21 && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/zulu-14-amd64
