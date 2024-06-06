# Docker images of Azul Zulu Builds of OpenJDK

This project contains the sources used to generate the Docker Hub images and info pages available on:

* Ubuntu: [azul/zulu-openjdk](https://hub.docker.com/r/azul/zulu-openjdk)
* Alpine: [azul/zulu-openjdk-alpine](https://hub.docker.com/r/azul/zulu-openjdk-alpine)
* CentOS: [azul/zulu-openjdk-centos](https://hub.docker.com/r/azul/zulu-openjdk-centos)
* Debian: [azul/zulu-openjdk-debian](https://hub.docker.com/r/azul/zulu-openjdk-debian)
* Distroless: [azul/zulu-openjdk-distroless](https://hub.docker.com/r/azul/zulu-openjdk-distroless)

Usage
=====

To run a container of your choice, use the commands below as an example.

For Ubuntu image with Azul Zulu 17, run:

    docker run -it --rm azul/zulu-openjdk:17-latest java -version

For Distroless image with Azul Zulu 17, run:

    docker run -it azul/zulu-openjdk-distroless:17-latest --version

as the entrypoint used [ "/usr/lib/jvm/zulu17/bin/java" ]

## Project structure

For each base operating system, a directory is created with the following content:

* `README.j2`: template file used by the build system to generate the `README.md` file in the same directory.
* `README.md`: generated file. DO NOT EDIT. It will be overwritten by the build system.
* A directory per version containing a `Dockerfile`.
