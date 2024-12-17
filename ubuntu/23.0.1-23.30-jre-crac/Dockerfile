FROM ubuntu:22.04 as builder

ADD https://cdn.azul.com/zulu/bin/zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64.tar.gz /opt/
RUN cd /opt/ && tar -xzf zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64.tar.gz && rm -rf zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64.tar.gz
FROM ubuntu:22.04
COPY --from=builder /opt/zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64 /opt/zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64
ENV JAVA_HOME /opt/zulu23.30.13-ca-crac-jre23.0.1-linux_aarch64
ENV PATH $JAVA_HOME/bin:$PATH
RUN apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install locales tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
