FROM debian:9

RUN apt-get -qq update && \
	apt-get -y install gnupg && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9 && \
	echo "deb http://repos.azulsystems.com/debian stable  main" >> /etc/apt/sources.list.d/zulu.list && \
	apt-get -qq update && \
	apt-get -y install zulu-7=7.22.0.3 && \
	rm -rf /var/lib/apt/lists/*
