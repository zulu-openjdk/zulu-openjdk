FROM debian:jessie

#
# Pull Zulu OpenJDK binaries from official repository:
#
RUN apt-key adv --keyserver hkp://keyserver.debian.com:80 --recv-keys 0x219BD9C9
RUN echo "deb http://repos.azulsystems.com/debian `lsb_release -cs` main" >> /etc/apt/sources.list.d/zulu.list
RUN apt-get -qq update
RUN apt-get -qqy install zulu-7=7.4.0.5