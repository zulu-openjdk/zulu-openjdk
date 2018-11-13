FROM alpine
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN ZULU_ARCH=zulu8.33.0.1-jdk8.0.192-linux_musl_x64.tar.gz && \
    INSTALL_DIR=/usr/lib/jvm && \
	BIN_DIR=/usr/bin && \
	MAN_DIR=/usr/share/man/man1 && \
	ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) && \
	wget -q https://cdn.azul.com/zulu/bin/${ZULU_ARCH} && \
	mkdir -p ${INSTALL_DIR} && \
	tar -xf ./${ZULU_ARCH} -C ${INSTALL_DIR} && rm -f ${ZULU_ARCH} && \
	cd ${BIN_DIR} && find ${INSTALL_DIR}/${ZULU_DIR}/bin -type f -perm -a=x -exec ln -s {} . \; && \
	mkdir -p ${MAN_DIR} && \
	cd ${MAN_DIR} && find ${INSTALL_DIR}/${ZULU_DIR}/man/man1 -type f -name "*.1" -exec ln -s {} . \;
