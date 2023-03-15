FROM azul/zulu-openjdk:17-jre-headless-latest AS builder

RUN mkdir /emptydir

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

COPY --from=builder /emptydir /tmp

ENV PATH="${PATH}:/usr/lib/jvm/zulu17/bin/"

ENTRYPOINT [ "/usr/lib/jvm/zulu17/bin/java" ]
