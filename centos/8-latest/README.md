What is Zulu? ![Zulu Duke in a Box][1]
======================================

Zulu is a widely available binary distribution of OpenJDK. Zulu distributions are fully tested and compatibility verified builds of the latest versions of the OpenJDK 8, 7, and 6 platforms. Zulu is available free of charge for Linux, Windows, and MacOS platforms, with commercial support available upon request.

Zulu is built, tested, supported and made available by Azul Systems.

[www.azul.com/zulu][2]

Tags and `Dockerfile` links
===========================

The Zulu repository azul/zulu-openjdk provides multiple tagged images. The latest Zulu OpenJDK 8, 7, and 6 versions are:

[`8u92`, `8`, `latest` (*8u92/Dockerfile*)][27]

[`7u101`, `7`, `latest` (*7u101/Dockerfile*)][18]

[`6u79`, `6`, `latest` (*6u79/Dockerfile*)][10]

Earlier Zulu OpenJDK 8, 7, and 6 releases can be found at: 

[8u11][28], [8u20][29], [8u25][30], [8u31][31], [8u40][32], [8u45][33], [8u51][34], [8u60][35], [8u65][36], [8u66][37], [8u72][38]

[7u65][19], [7u72][20], [7u76][21], [7u79][22], [7u80][23], [7u85][24], [7u91][25], [7u95][26]

[6u53][11], [6u56][12], [6u59][13], [6u63][14], [6u69][15], [6u73][16], [6u77][17]


Usage
=====

This Zulu repository supports multiple versions of OpenJDK-based Java SE JDKs. Zulu versions 8, 7, and 6 are compliant with Java SE 8, Java SE 7, and Java SE 6, respectively.

For example, you can run a Zulu OpenJDK 8 container with the following command:

    docker run -it --rm azul/zulu-openjdk-centos:8 java -version

Similarly, you can run a Zulu OpenJDK 7 container with the following command:

    docker run -it --rm azul/zulu-openjdk-centos:7 java -version

And you can run a Zulu OpenJDK 6 container with the following command:

    docker run -it --rm azul/zulu-openjdk-centos:6 java -version


  [1]: http://www.azulsystems.com/sites/default/files//ZuluDocker60.gif
  [2]: http://www.azul.com/zulu
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u79-6.12.0.2/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u63-6.8.0.1/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u69-6.9.0.3/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u73-6.10.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u77-6.11.0.2/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u101-7.14.0.5/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u79-7.9.0.2/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u80-7.10.0.1/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u85-7.11.0.3/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u91-7.12.0.3/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u95-7.13.0.1/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u92-8.15.0.1/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u11-8.2.0.1/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u20-8.3.0.1/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u25-8.4.0.1/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u31-8.5.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u40-8.6.0.1/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u45-8.7.0.5/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u51-8.8.0.3/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u60-8.9.0.4/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u65-8.10.0.1/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u66-8.11.0.1/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u72-8.13.0.5/Dockerfile
