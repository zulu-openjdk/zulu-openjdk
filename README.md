What are Azul Zulu Builds of OpenJDK?
=====================================

Azul Zulu Builds of OpenJDK are fully tested, and TCK compliant builds of OpenJDK for Linux, Windows, and macOS operating systems.

Azul Zulu Builds of OpenJDK are available for free unlimited use and are commercially supported by [Azul][1] as a part of the Azul Platform Core bundle.
Check out [Azul Platform Core][2] for more information. The technical documentation can be found on [docs.azul.com/core][3].

Docker images of Azul Zulu are available in the following repositories, depending on the base system:

  * [azul/zulu-openjdk-ubuntu][4]
  * [azul/zulu-openjdk-alpine][5]
  * [azul/zulu-openjdk-centos][6]
  * [azul/zulu-openjdk-debian][7]
  * [azul/zulu-openjdk-distroless][8]

Usage
=====

To run a container of your choice, use the commands below as an example.

For Azul Zulu 17, run:

    docker run -it --rm azul/zulu-openjdk-ubuntu:17 java -version

For Distroless image, run:

    docker run -it azul/zulu-openjdk-distroless:17-distroless-latest --version

as the entrypoint used [ "/usr/lib/jvm/zulu17/bin/java" ]

Tags and `Dockerfile` links
===========================
  * [20-latest (20-latest/Dockerfile)][24]
  * [19-latest (19-latest/Dockerfile)][23]
  * [18-latest (18-latest/Dockerfile)][22]
  * [17-latest (17-latest/Dockerfile)][21]
  * [16-latest (16-latest/Dockerfile)][20]
  * [15-latest (15-latest/Dockerfile)][19]
  * [14-latest (14-latest/Dockerfile)][18]
  * [13-latest (13-latest/Dockerfile)][17]
  * [12-latest (12-latest/Dockerfile)][16]
  * [11-latest (11-latest/Dockerfile)][15]
  * [10-latest (10-latest/Dockerfile)][14]
  * [9-latest (9-latest/Dockerfile)][13]
  * [8-latest (8-latest/Dockerfile)][12]
  * [7-latest (7-latest/Dockerfile)][11]
  * [6-latest (6-latest/Dockerfile)][10]



  [1]: https://www.azul.com/
  [2]: https://www.azul.com/products/core/
  [3]: https://docs.azul.com/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [7]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [8]: https://hub.docker.com/r/azul/zulu-openjdk-distroless

  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile



