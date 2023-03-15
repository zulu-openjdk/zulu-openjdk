What is Azul Zulu?
======================================

Azul Zulu builds of OpenJDK are fully tested, and TCK compliant builds of OpenJDK for Linux, Windows, and macOS operating systems.

Azul Zulu Builds of OpenJDK are available for free unlimited use and are commercially supported by Azul as a part of the Azul Platform Core bundle.
Check out [Azul Platform Core][3] for more information.

Alpine, Centos, Debian, and Ubuntu Docker official images of Azul Zulu are available in the following repositories:

  * [azul/zulu-openjdk-alpine][4]
  * [azul/zulu-openjdk-centos][5]
  * [azul/zulu-openjdk-debian][6]
  * [azul/zulu-openjdk][7]
  * [azul/zulu-openjdk-distroless][8]

Usage
=====

To run a container of your choice, use the commands below as an example.

For Azul Zulu 17, run:

    docker run -it --rm azul/zulu-openjdk:17 java -version

For Distroless image, run: 

    docker run -it azul/zulu-openjdk:17-distroless-latest --version

as the entrypoint used [ "/usr/lib/jvm/zulu17/bin/java" ]

Tags and `Dockerfile` links
===========================

Most Recent
-----------

  * [`17.0.6-17.40.19-distroless`, `17-latest` (*17-latest/Dockerfile)*][10]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * 
  * [17-latest][10],
  [17.0.6-17.40.19][11],
  [17-distroless-latest][12],
  [17.0.5-17.38.21-distroless][13],
  [17.0.6-17.40.19-distroless][14],
  

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: https://www.azul.com/
  [3]: https://www.azul.com/products/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk
  [8]: https://hub.docker.com/r/azul/zulu-openjdk-distroless


  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17-latest/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.6-17.40.19/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17-distroless-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.5-17.38.21-distroless/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.6-17.40.19-distroless/Dockerfile
  