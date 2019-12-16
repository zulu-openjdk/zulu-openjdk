Alpine-Native Zulu OpenJDK Images
=================================
Images of zulu-openjdk-alpine include Alpine-native Zulu binary distributions of OpenJDK, which use the built-in musl libc functionality in Alpine Linux, and do not add glibc on top of Alpine distribution.

What is Zulu? ![Zulu Duke in a Box][1]
======================================

Zulu is a binary distribution of the open-source OpenJDK project for Linux, Windows, and MacOS operating systems.

Zulu distributions are fully tested and verified for compatibility builds of the latest versions of OpenJDK 13, 11, 8, and 7.

Zulu comes in two flavours: Zulu Community Edition, a completely free version, and Zulu Enterprise Edition that is backed by full commercial support.

Zulu is built, tested, supported, and delivered by [Azul Systems][2].

Check out [Zulu Overview][3] for more information.

Alpine, Centos, Debian, and Ubuntu Docker official images of Zulu are available in the following repositories:

  * [azul/zulu-openjdk-alpine][4]
  * [azul/zulu-openjdk-centos][5]
  * [azul/zulu-openjdk-debian][6]
  * [azul/zulu-openjdk][7]

Tags and `Dockerfile` links
===========================

Most Recent
-----------

The Zulu azul/zulu-openjdk-alpine repository provides various Alpine Docker image tags. The most recent Zulu versions of OpenJDK 13, 11 and 8 are listed below:

 * [`13`, `13` (*13-latest/Dockerfile*)][45]

 * [`11.0.4`, `11` (*11.0.4/Dockerfile*)][39]

 * [`11.0.4-jre`, `11-jre` (*11.0.4-jre/Dockerfile*)][40]

 * [`8u222`, `8`, `latest` (*8u222/Dockerfile*)][27]

 * [`8u222-jre`, `8-jre`, `latest-jre` (*8u222-jre/Dockerfile*)][28]

Previous
--------

Earlier created Alpine Docker image tags of Zulu for previous releases of OpenJDK 13, 12, 11, 8, 7, and 6 are as follows:

 * [12.0.2][46]

 * [11.0.1][41], [11.0.2][42], [11.0.3][43], [11.0.3-jre][44]

 * [8u131][29], [8u144][30], [8u152][31], [8u162][32], [8u172][33], [8u181][34], [8u192][35], [8u202][36], [8u212][37], [8u212-jre][38]

 * [7u141][17], [7u154][18], [7u161][19], [7u171][20], [7u181][21], [7u191][22], [7u201][23], [7u211][24], [7u222][25], [7u232][26]

 * [6u93][10], [6u97][11], [6u99][12], [6u103][13], [6u107][14], [6u113][15], [6u119][16]

**Note**: Some of these may be using glibc and predate the move to musl libc.

Usage
=====

This Zulu repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 13, 12, 11, 10, 9, 8, and 7 of Zulu are compliant with Java SE 13, 12, 11, 10, 9, 8, and 7 respectively.

To run a container of your choice, use commands below as an example.

For a Zulu OpenJDK 13 container, enter:

    docker run -it --rm azul/zulu-openjdk-alpine:13 java -version

For a Zulu OpenJDK 11 container, enter:

    docker run -it --rm azul/zulu-openjdk-alpine:11 java -version

For a Zulu OpenJDK 8 container, enter:

    docker run -it --rm azul/zulu-openjdk-alpine:8 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: http://www.azul.com
  [3]: https://www.azul.com/products/zulu-enterprise
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
