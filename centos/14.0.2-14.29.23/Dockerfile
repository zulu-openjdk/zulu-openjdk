FROM centos:7

#
# UTF-8 by default
#
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

#
# Pull Zulu OpenJDK binaries from official repository:
#

RUN rpm --import http://repos.azulsystems.com/RPM-GPG-KEY-azulsystems && \
    curl -o /etc/yum.repos.d/zulu.repo http://repos.azulsystems.com/rhel/zulu.repo && \
    yum -q -y update && \
    yum -q -y upgrade && \
    yum -q -y install zulu-14-14.29+23 && \
    yum clean all && \
    rm -rf /var/cache/yum

ENV JAVA_HOME=/usr/lib/jvm/zulu-14

