FROM debian:bookworm-slim

ENV LANG='en_US.UTF-8'
RUN set -ex && \
    apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install gnupg ca-certificates locales curl tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    curl -s https://repos.azul.com/azul-repo.key | gpg --dearmor -o /usr/share/keyrings/azul.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb stable main" > /etc/apt/sources.list.d/zulu.list && \
    apt-get -qq update && \
    echo "Package: zulu24-*\nPin: version 24.0.2-*\nPin-Priority: 1001" > /etc/apt/preferences && \
    apt-get -qq -y --no-install-recommends install zulu24-jre-headless=24.0.2-* && \
    apt-get -qq -y purge --auto-remove gnupg curl && \
    apt-get -qq -y dist-upgrade && \
    apt-get -qq -y autoremove && \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/zulu24
