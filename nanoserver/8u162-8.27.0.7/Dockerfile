FROM microsoft/nanoserver:latest

MAINTAINER Boshi Lian <farmer1992@gmail.com>

ENV JDK_URL https://cdn.azul.com/zulu/bin/zulu8.27.0.7-jdk8.0.162-win_x64.zip
ENV JDK_VERSION 1.8.0_162

RUN powershell -NoProfile -Command \
        Invoke-WebRequest %JDK_URL% -OutFile jdk.zip; \
        Expand-Archive jdk.zip -DestinationPath '%ProgramFiles%'; \
        Move-Item '%ProgramFiles%\zulu*' '%ProgramFiles%\zulujdk'; \
        Remove-Item -Force jdk.zip

RUN setx /M JAVA_HOME "%ProgramFiles%\zulujdk\jre"

RUN setx /M PATH "%PATH%;%ProgramFiles%\zulujdk\bin"
