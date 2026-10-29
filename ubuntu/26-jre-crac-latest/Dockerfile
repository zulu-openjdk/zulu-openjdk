FROM ubuntu:22.04 as builder

ADD https://cdn.azul.com/zulu/bin/zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64.tar.gz /opt/
RUN cd /opt/ && tar -xzf zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64.tar.gz && rm -rf zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64.tar.gz
FROM ubuntu:22.04
COPY --from=builder /opt/zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64 /opt/zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64
ENV JAVA_HOME /opt/zulu26.32.203-ca-crac-jre26.0.2.1-linux_aarch64
ENV PATH $JAVA_HOME/bin:$PATH
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    set -ex && \
    apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install locales tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    apt-get -qq -y dist-upgrade && \
    apt-get -qq -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
