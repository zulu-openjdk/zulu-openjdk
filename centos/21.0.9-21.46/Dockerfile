FROM centos:7

ENV LANG='en_US.UTF-8'

ARG ZULU_REPO_SHA256=2724b8be277ec16196b8e9357ed5e506eb791f88f966965a4f4a8bd5c4acdcfe
ARG ZULU_REPO_VER=1.0.0-1

RUN set -ex && \
    rpm --import https://repos.azulsystems.com/RPM-GPG-KEY-azulsystems && \
    curl -sLO https://cdn.azul.com/zulu/bin/zulu-repo-${ZULU_REPO_VER}.noarch.rpm && \
    echo "${ZULU_REPO_SHA256}  zulu-repo-${ZULU_REPO_VER}.noarch.rpm" | sha256sum --strict --check - && \
    rpm -ivh zulu-repo-${ZULU_REPO_VER}.noarch.rpm && \
    sed -i 's/^mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
    sed -i 's|# *baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
    yum -q -y install yum-plugin-versionlock tzdata fontconfig && \
    yum versionlock zulu21-*-21.0.9-* && \
    yum -q -y install zulu21-jdk && \
    yum clean all && \
    rm -rf /var/cache/yum zulu-repo_${ZULU_REPO_VER}.noarch.rpm
ENV JAVA_HOME=/usr/lib/jvm/zulu21

