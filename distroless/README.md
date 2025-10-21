Azul Zulu Distroless
====================

"Distroless" images contain only your application and its runtime dependencies. They do not contain package managers,
shells or any other programs you would expect to find in a standard Linux distribution.

Azul Zulu Builds of OpenJDK are available for free unlimited use and are commercially supported by [Azul][1] as a part of the Azul Platform Core bundle.
Check out [Azul Platform Core][2] for more information. The technical documentation can be found on [docs.azul.com/core][3].

Docker images of Azul Zulu are available in the following repositories, depending on the base system:

  * [Ubuntu: azul/zulu-openjdk][4]
  * [Alpine: azul/zulu-openjdk-alpine][5]
  * [CentOS: azul/zulu-openjdk-centos][6]
  * [Debian: azul/zulu-openjdk-debian][7]
  * [Distroless: azul/zulu-openjdk-distroless][8]

Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`21.0.9-21.46`, `21-latest` (*21-latest/Dockerfile)*][11]
  * [`17.0.17-17.62`, `17-latest` (*17-latest/Dockerfile)*][20]

Previous
--------

Earlier Distroless Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[21-latest][11],
  [21.0.2-21.32][12],
  [21.0.3-21.34][13],
  [21.0.4-21.36][14],
  
  
  
  
  
  
  *[17-latest][20],
  [17.0.6-17.40.19][21],
  [17.0.7-17.42.19][22],
  [17.0.8.1-17.44.53][23],
  
  
  
  
  
  
  
  
  
  
  
  License
=======

Azul Zulu incorporates third-party licensed software packages. Some of these have distribution restrictions, and some have only reporting requirements. Please see [docs.azul.com/core/tpl][9] for the links to the documents with licenses for third-party software included in the latest version of Azul Platform Core.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc., from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

[BSD 3-Clause Clear License][10]


  [1]: https://www.azul.com/
  [2]: https://www.azul.com/products/core/
  [3]: https://docs.azul.com/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [7]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [8]: https://hub.docker.com/r/azul/zulu-openjdk-distroless
  [9]: https://docs.azul.com/core/tpl
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/LICENSE.txt


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/21-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/21.0.2-21.32/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/21.0.3-21.34/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/21.0.4-21.36/Dockerfile
  
  
  
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.6-17.40.19/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.7-17.42.19/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/distroless/17.0.8.1-17.44.53/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  