FROM microsoft/nanoserver:latest

MAINTAINER Boshi Lian <farmer1992@gmail.com>

ENV JDK_URL http://cdn.azul.com/zulu/bin/zulu8.25.0.1-jdk8.0.152-win_x64.zip
ENV JDK_VERSION 1.8.0_152

RUN powershell -NoProfile -Command \
        Invoke-WebRequest %JDK_URL% -OutFile jdk.zip; \
        Expand-Archive jdk.zip -DestinationPath '%ProgramFiles%'; \
        Move-Item '%ProgramFiles%\zulu*' '%ProgramFiles%\zulujdk'; \
        Remove-Item -Force jdk.zip

RUN setx /M JAVA_HOME "%ProgramFiles%\zulujdk\jre"

RUN setx /M PATH "%PATH%;%ProgramFiles%\zulujdk\bin"
