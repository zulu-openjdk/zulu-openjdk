FROM centos:7

#
# UTF-8 by default
#
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JAVA_HOME=/usr/lib/jvm/zulu-7

#
# Pull Zulu OpenJDK binaries from official repository:
#
RUN rpm --import http://repos.azulsystems.com/RPM-GPG-KEY-azulsystems && \
    curl -o /etc/yum.repos.d/zulu.repo http://repos.azulsystems.com/rhel/zulu.repo && \
    yum -q -y update && \
    yum -q -y install zulu-7-7.36.0.5-1 && \
    $JAVA_HOME/bin/java -version
