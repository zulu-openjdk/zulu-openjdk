FROM alpine:3.7

ENV LANG=C.UTF-8

# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.

RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" && \
	ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0" && \
	ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
	ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
	ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
	apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
	wget \
		"https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub" \
		-O "/etc/apk/keys/sgerrand.rsa.pub" && \
	wget \
		"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
	apk add --no-cache \
		"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
	\
	rm "/etc/apk/keys/sgerrand.rsa.pub" && \
	/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 "$LANG" || true && \
	echo "export LANG=$LANG" > /etc/profile.d/locale.sh && \
	\
	apk del glibc-i18n && \
	\
	rm "/root/.wget-hsts" && \
	apk del .build-dependencies && \
	rm \
		"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
		"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"

RUN cd /tmp && \
	wget -O gcc-libs.tar.xz https://www.archlinux.org/packages/core/x86_64/gcc-libs/download/ && \
	wget -O zlib.tar.xz https://www.archlinux.org/packages/core/x86_64/zlib/download/ && \
	tar Jxf gcc-libs.tar.xz usr/lib && \
	tar Jxf zlib.tar.xz usr/lib && \
	mv /tmp/usr/lib/libgcc_s.so* /tmp/usr/lib/libstdc++.so* /tmp/usr/lib/libz.so* /usr/glibc-compat/lib/ && \
	rm -rf /tmp/usr

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN ZULU_ARCH=zulu10.2+3-jdk10.0.1-linux_x64.tar.gz && \
	INSTALL_DIR=/usr/lib/jvm && \
	BIN_DIR=/usr/bin && \
	MAN_DIR=/usr/share/man/man1 && \
	ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) && \
	apk update && \
	apk add --no-cache ca-certificates wget && \
	update-ca-certificates && \
	wget -q http://172.17.0.1:8000/${ZULU_ARCH} && \
	mkdir -p ${INSTALL_DIR} && \
	tar -xf ./${ZULU_ARCH} -C /usr/lib/jvm/ && rm -f ${ZULU_ARCH} && \
	cd ${BIN_DIR}; find ${INSTALL_DIR}/${ZULU_DIR}/bin -type f -perm -a=x -exec ln -s {} . \; && \
	mkdir -p ${MAN_DIR} && \
	cd ${MAN_DIR}; find ${INSTALL_DIR}/${ZULU_DIR}/man/man1 -type f -name "*.1" -exec ln -s {} . \; && \
	java -version 
