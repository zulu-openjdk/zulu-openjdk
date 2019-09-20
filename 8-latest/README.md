What is Zulu? ![Zulu Duke in a Box][1]
======================================

Zulu is a binary distribution of the open-source OpenJDK project for Linux, Windows, and MacOS operating systems.

Zulu distributions are fully tested and verified for compatibility builds of the latest versions of OpenJDK 12, 11, 8, and 7.

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

The Zulu azul/zulu-openjdk repository provides various Ubuntu Docker image tags. The most recent Zulu versions of OpenJDK 12, 11, 8, and 7 are listed below:

 * [`12.0.2`, `12` (*12.0.2/Dockerfile*)][88]

 * [`11.0.4`, `11` (*11.0.4/Dockerfile*)][84]

 * [`8u222`, `8`, `latest` (*8u222/Dockerfile*)][53]

 * [`7u232`, `7` (*7u232/Dockerfile*)][29]

Previous
--------

Earlier created Ubuntu Docker image tags of Zulu for previous releases of OpenJDK 12, 11, 10, 9, 8, 7, and 6 are as follows:

* [12.0.1][89]

* [11.0.1][85], [11.0.2][86], [11.0.3][87]

* [10u01][82], [10u02][83]

* [9u01][79], [9u04][80], [9u07][81]

* [8u05][54], [8u11][55], [8u20][56], [8u25][57], [8u31][58], [8u40][59], [8u45][60], [8u51][61], [8u60][62], [8u65][63], [8u66][64], [8u72][65], [8u92][66], [8u102][67], [8u112][68], [8u121][69], [8u131][70], [8u144][71], [8u152][72], [8u162][73], [8u172][74], [8u181][75], [8u192][76], [8u202][77], [8u212][78]

* [7u55][30], [7u60][31], [7u65][32], [7u72][33], [7u76][34], [7u79][35], [7u80][36], [7u85][37], [7u91][38], [7u95][39], [7u101][40], [7u111][41], [7u121][42], [7u131][43], [7u141][44], [7u154][45], [7u161][46], [7u171][47], [7u181][48], [7u191][49], [7u201][50], [7u211][51], [7u222][52]

* [6u49][10], [6u53][11], [6u56][12], [6u59][13], [6u63][14], [6u69][15], [6u73][16], [6u77][17], [6u79][18], [6u83][19], [6u87][20], [6u89][21], [6u93][22], [6u97][23], [6u99][24], [6u103][25], [6u107][26], [6u113][27], [6u119][28]

Usage
=====

This Zulu repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 12, 11, 8, and 7 of Zulu are compliant with Java SE 12, 11, 8, and 7 respectively.

To run a container of your choice, use commands below as an example.

For a Zulu OpenJDK 12 container, enter:

    docker run -it --rm azul/zulu-openjdk:12 java -version

For a Zulu OpenJDK 11 container, enter:

    docker run -it --rm azul/zulu-openjdk:11 java -version

For a Zulu OpenJDK 8 container, enter:

    docker run -it --rm azul/zulu-openjdk:8 java -version

For a Zulu OpenJDK 7 container, enter:

    docker run -it --rm azul/zulu-openjdk:7 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: http://www.azul.com/zulu
  [3]: https://www.azul.com/products/zulu-enterprise
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk

  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
