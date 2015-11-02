What is Zulu? ![Zulu Duke in a Box][1]
======================================

Zulu is a widely available binary distribution of OpenJDK. Zulu distributions are fully tested and compatibility verified builds of the latest versions of the OpenJDK 8, 7, and 6 platforms. Zulu is available free of charge for Linux, Windows, and MacOS platforms, with commercial support available upon request.

Zulu is built, tested, supported and made available by Azul Systems.

[www.azul.com/zulu][2]

Tags and `Dockerfile` links
===========================

The Zulu repository azul/zulu-openjdk provides multiple tagged images. The latest Zulu OpenJDK 8, 7, and 6 versions are:

[`8u66`, `8`, `latest` (*8u66/Dockerfile*)][25]

[`7u91`, `7`, `latest` (*7u91/Dockerfile*)][16]

[`6u69`, `6`, `latest` (*6u69/Dockerfile*)][10]

Earlier Zulu OpenJDK 8, 7, and 6 releases can be found at: 

[8u05][26], [8u11][27], [8u20][28], [8u25][29], [8u31][30], [8u40][31], [8u45][32], [8u51][33], [8u60][34], [8u65][35]

[7u55][17], [7u60][18], [7u65][19], [7u72][20], [7u76][21], [7u79][22], [7u80][23], [7u85][24]

[6u49][11], [6u53][12], [6u56][13], [6u59][14], [6u63][15]


Usage
=====

This Zulu repository supports multiple versions of OpenJDK-based Java SE JDKs. Zulu versions 8, 7, and 6 are compliant with Java SE 8, Java SE 7, and Java SE 6, respectively.

For example, you can run a Zulu OpenJDK 8 container with the following command:

    docker run -it --rm azul/zulu-openjdk:8 java -version

Similarly, you can run a Zulu OpenJDK 7 container with the following command:

    docker run -it --rm azul/zulu-openjdk:7 java -version

And you can run a Zulu OpenJDK 6 container with the following command:

    docker run -it --rm azul/zulu-openjdk:6 java -version


  [1]: http://www.azulsystems.com/sites/default/files//ZuluDocker60.gif
  [2]: http://www.azul.com/zulu
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile

