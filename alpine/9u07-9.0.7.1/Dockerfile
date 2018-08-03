FROM alpine
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN ZULU_ARCH=zulu9.0.7.1-jdk9.0.7-linux_x64.tar.gz && \
	ALPINE_GLIBC_PACKAGE_VERSION=2.27-r0 && \
	INSTALL_DIR=/usr/lib/jvm && \
	BIN_DIR=/usr/bin && \
	MAN_DIR=/usr/share/man/man1 && \
	ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) && \
	apk add --no-cache --virtual=.build-dependencies ca-certificates wget binutils && \
	update-ca-certificates && \
	wget https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub -O /etc/apk/keys/sgerrand.rsa.pub && \
	wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${ALPINE_GLIBC_PACKAGE_VERSION}/glibc-${ALPINE_GLIBC_PACKAGE_VERSION}.apk -O glibc.apk && \
	apk add --no-cache glibc.apk && \
	rm glibc.apk /etc/apk/keys/sgerrand.rsa.pub && \
	wget -O gcc-libs.tar.xz https://www.archlinux.org/packages/core/x86_64/gcc-libs/download/ && \
	wget -O zlib.tar.xz https://www.archlinux.org/packages/core/x86_64/zlib/download/ && \
	tar -xJf gcc-libs.tar.xz -C /tmp usr/lib && \
	tar -xJf zlib.tar.xz -C /tmp usr/lib && \
	mv /tmp/usr/lib/libgcc_s.so* /tmp/usr/lib/libstdc++.so* /tmp/usr/lib/libz.so* /usr/glibc-compat/lib/ && \
	strip /usr/glibc-compat/lib/libgcc_s.so.* /usr/glibc-compat/lib/libstdc++.so.* && \
	rm -rf gcc-libs.tar.xz zlib.tar.xz /tmp/usr && \
	wget -q https://cdn.azul.com/zulu/bin/${ZULU_ARCH} && \
	apk del .build-dependencies && \
	rm /root/.wget-hsts && \
	mkdir -p ${INSTALL_DIR} && \
	tar -xf ./${ZULU_ARCH} -C ${INSTALL_DIR} && rm -f ${ZULU_ARCH} && \
	cd ${BIN_DIR} && find ${INSTALL_DIR}/${ZULU_DIR}/bin -type f -perm -a=x -exec ln -s {} . \; && \
	mkdir -p ${MAN_DIR} && \
	cd ${MAN_DIR} && find ${INSTALL_DIR}/${ZULU_DIR}/man/man1 -type f -name "*.1" -exec ln -s {} . \; && \
	java -version 
