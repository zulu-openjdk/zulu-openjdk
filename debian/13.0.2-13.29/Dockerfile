FROM debian:9

ENV JAVA_HOME=/usr/lib/jvm/zulu-13-amd64/
#
# Pull Zulu OpenJDK binaries from official repository
#
RUN apt-get -qq update && \
    apt-get -y install gnupg && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9 && \
    echo "deb http://repos.azulsystems.com/debian stable  main" >> /etc/apt/sources.list.d/zulu.list && \
    apt-get -qq update && \
    apt-get remove -y gnupg
   
RUN apt-get -y install zulu-13=13.29+9 && \
    $JAVA_HOME/bin/java -version && \
    apt-get autoremove -y && \
    apt-get clean
