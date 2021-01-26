FROM alpine:3.12

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ARG ZULU_DIR=zulu7.42.0.51-ca-jdk7.0.285-linux_x64

RUN ZULU_PACK=${ZULU_DIR}.tar.gz && \
    INSTALL_DIR=/usr/lib/jvm && \
    BIN_DIR=/usr/bin && \
    MAN_DIR=/usr/share/man/man1 && \
    apk --no-cache add binutils ca-certificates wget zstd tar xz && \
    apk update && \
    apk upgrade && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk && \
    apk add glibc-2.28-r0.apk && rm glibc-2.28-r0.apk && \
    wget -O gcc-libs.tar.zst https://www.archlinux.org/packages/core/x86_64/gcc-libs/download/ && \
    wget -O zlib.tar.xz https://www.archlinux.org/packages/core/x86_64/zlib/download/ && \
    tar -I zstd -xf gcc-libs.tar.zst -C /tmp && \
    tar -xJf zlib.tar.xz -C /tmp && \
    mv /tmp/usr/lib/libgcc_s.so* /tmp/usr/lib/libstdc++.so* /tmp/usr/lib/libz.so* /usr/glibc-compat/lib/ && \
    strip /usr/glibc-compat/lib/libgcc_s.so.* /usr/glibc-compat/lib/libstdc++.so.* && \
    rm -rf gcc-libs.tar.xz zlib.tar.xz /tmp/usr && \
    wget -q https://cdn.azul.com/zulu/bin/zulu7.42.0.51-ca-jdk7.0.285-linux_x64.tar.gz && rm /root/.wget-hsts && \
    mkdir -p ${INSTALL_DIR} && \
    tar -xf ./${ZULU_PACK} -C ${INSTALL_DIR} && rm -f ${ZULU_PACK} && \
    cd ${BIN_DIR} && \
    find ${INSTALL_DIR}/${ZULU_DIR}/bin -type f -perm -a=x -exec ln -s {} . \; && \
    mkdir -p ${MAN_DIR} && \
    cd ${MAN_DIR} && \
    find ${INSTALL_DIR}/${ZULU_DIR}/man/man1 -type f -name "*.1" -exec ln -s {} . \;


ENV JAVA_HOME=/usr/lib/jvm/${ZULU_DIR}

