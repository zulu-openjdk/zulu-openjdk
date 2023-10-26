FROM ubuntu:22.04 as builder

ADD https://cdn.azul.com/zulu/bin/zulu21.28.89-ca-crac-jdk21.0.0-linux_x64.tar.gz /opt/
RUN cd /opt/ && tar -xzf zulu21.28.89-ca-crac-jdk21.0.0-linux_x64.tar.gz && rm -rf zulu21.28.89-ca-crac-jdk21.0.0-linux_x64.tar.gz
FROM ubuntu:22.04
COPY --from=builder /opt/zulu21.28.89-ca-crac-jdk21.0.0-linux_x64 /opt/zulu21.28.89-ca-crac-jdk21.0.0-linux_x64
ENV JAVA_HOME /opt/zulu21.28.89-ca-crac-jdk21.0.0-linux_x64
ENV PATH $JAVA_HOME/bin:$PATH
RUN apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install locales  tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 

