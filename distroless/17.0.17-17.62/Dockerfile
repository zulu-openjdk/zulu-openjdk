FROM ubuntu:jammy AS builder
ENV LANG='en_US.UTF-8'

RUN set -ex && \
    apt-get -qq update && \
    apt-get -qq -y --no-install-recommends install gnupg ca-certificates locales curl tzdata && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    curl -s https://repos.azul.com/azul-repo.key | gpg --dearmor -o /usr/share/keyrings/azul.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb stable main" > /etc/apt/sources.list.d/zulu.list && \
    apt-get -qq update && \
    echo "Package: zulu17-*\nPin: version 17.0.17-*\nPin-Priority: 1001" > /etc/apt/preferences && \
    apt-get -qq -y --no-install-recommends install zulu17-jdk=17.0.17-* && \
    apt-get -qq -y purge --auto-remove gnupg curl && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/zulu17

RUN mkdir -p rootfs/tmp && chmod -R 777 rootfs/tmp

FROM scratch

COPY --from=builder \
		/usr/lib/x86_64-linux-gnu/libresolv.so* \
		/usr/lib/x86_64-linux-gnu/libc.so* \
		/usr/lib/x86_64-linux-gnu/libdl.so* \
		/usr/lib/x86_64-linux-gnu/libm.so* \
		/usr/lib/x86_64-linux-gnu/librt.so* \
		/usr/lib/x86_64-linux-gnu/libpthread.so* \
		/usr/lib/x86_64-linux-gnu/libnet.so* \
	        /usr/lib/x86_64-linux-gnu/libnss_file*.so* \
		/usr/lib/x86_64-linux-gnu/libnss_dns*.so* \
		/usr/lib/x86_64-linux-gnu/libz.so* \
		/lib/x86_64-linux-gnu/

COPY --from=builder \
		/usr/lib64/ld-linux-x86-64.so.2 \
		/lib64/

COPY --from=builder /usr/lib/jvm/zulu17-ca-amd64 /usr/lib/jvm/zulu17

COPY --from=builder rootfs/ /

ENV PATH="${PATH}:/usr/lib/jvm/zulu17/bin/"

ENTRYPOINT [ "/usr/lib/jvm/zulu17/bin/java" ]
