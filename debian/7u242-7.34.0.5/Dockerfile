FROM debian:9

RUN apt-get -qq update
RUN apt-get -y install gnupg

#
# Pull Zulu OpenJDK binaries from official repository:
#
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9
RUN echo "deb http://repos.azulsystems.com/debian stable  main" >> /etc/apt/sources.list.d/zulu.list
RUN apt-get -qq update
RUN apt-get -y install zulu-7=7.34.0.5

ENV JAVA_HOME=/usr/lib/jvm/zulu-7-amd64/
