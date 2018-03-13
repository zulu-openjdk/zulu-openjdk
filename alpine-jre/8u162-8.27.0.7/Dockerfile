FROM frolvlad/alpine-glibc
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN ZULU_ARCH=zulu8.27.0.7-jdk8.0.162-linux_x64.tar.gz && \
	INSTALL_DIR=/usr/lib/jvm && \
	BIN_DIR=/usr/bin && \
	ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) && \
	apk update && \
	apk add --no-cache ca-certificates wget && \
	update-ca-certificates && \
	wget -q http://cdn.azul.com/zulu/bin/${ZULU_ARCH} && \
	mkdir -p ${INSTALL_DIR} && \
	tar -xf ./${ZULU_ARCH} -C /usr/lib/jvm/ && rm -f ${ZULU_ARCH} && \
	rm -rf ${INSTALL_DIR}/${ZULU_DIR}/bin ${INSTALL_DIR}/${ZULU_DIR}/demo ${INSTALL_DIR}/${ZULU_DIR}/lib && \
	rm -rf ${INSTALL_DIR}/${ZULU_DIR}/src.zip ${INSTALL_DIR}/${ZULU_DIR}/man && \
	cd ${BIN_DIR}; find ${INSTALL_DIR}/${ZULU_DIR}/jre/bin -type f -perm -a=x -exec ln -s {} . \; && \
	java -version 
