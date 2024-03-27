FROM ubuntu:22.04 as builder

ADD https://cdn.azul.com/zulu/bin/zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64.tar.gz /opt/
RUN cd /opt/ && tar -xzf zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64.tar.gz && rm -rf zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64.tar.gz
FROM ubuntu:22.04
COPY --from=builder /opt/zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64 /opt/zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64
ENV JAVA_HOME /opt/zulu22.28.93-ca-crac-jdk22.0.0-linux_aarch64
ENV PATH $JAVA_HOME/bin:$PATH
RUN apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install locales tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
