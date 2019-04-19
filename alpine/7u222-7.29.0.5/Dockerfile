FROM frolvlad/alpine-glibc
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JAVA_HOME=/usr/lib/jvm/zulu-7
RUN ZULU_ARCH=zulu7.29.0.5-ca-jdk7.0.222-linux_x64.tar.gz && \
    INSTALL_DIR=$( dirname $JAVA_HOME ) && \
    BIN_DIR=/usr/bin && \
    MAN_DIR=/usr/share/man/man1 && \
    ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) && \
    apk update && \
    apk add --no-cache ca-certificates wget && \
    update-ca-certificates && \
    wget -q http://cdn.azul.com/zulu/bin/${ZULU_ARCH} && \
    mkdir -p ${INSTALL_DIR} && \
    tar -xf ./${ZULU_ARCH} -C /usr/lib/jvm/ && rm -f ${ZULU_ARCH} && \
    mv ${INSTALL_DIR}/${ZULU_DIR} ${JAVA_HOME} && \
    cd ${BIN_DIR}; find ${JAVA_HOME}/bin -type f -perm -a=x -exec ln -s {} . \; && \
    mkdir -p ${MAN_DIR} && \
    cd ${MAN_DIR}; find ${JAVA_HOME}/man/man1 -type f -name "*.1" -exec ln -s {} . \; && \
    apk del ca-certificates wget
