What is Azul Zulu? ![Zulu Duke in a Box][1]
======================================

Azul Zulu builds of OpenJDK are fully tested and TCK compliant builds of OpenJDK for Linux, Windows, and macOS operating systems.

Azul Zulu comes in two flavours: Azul Zulu Community Edition, a completely free version, and commercially supported Azul Zulu builds of OpenJDK.

Check out [Azul Zulu Overview][3] for more information.

Alpine, Centos, Debian, and Ubuntu Docker official images of Zulu are available in the following repositories:

  * [azul/zulu-openjdk-alpine][4]
  * [azul/zulu-openjdk-centos][5]
  * [azul/zulu-openjdk-debian][6]
  * [azul/zulu-openjdk][7]

Tags and `Dockerfile` links
===========================

Most Recent
-----------

 * [`16.0.0`, `16` (*16.0.0/Dockerfile*)][120]

 * [`16.0.0-jre`, `16-jre` (*16.0.0-jre/Dockerfile*)][121]

 * [`15.0.2`, `15` (*15.0.2/Dockerfile*)][119]

 * [`14.0.2`, `14` (*14.0.2/Dockerfile*)][117]

 * [`13.0.6`, `13` (*13.0.6/Dockerfile*)][115]

 * [`11.0.10`, `11` (*11.0.10/Dockerfile*)][107]

 * [`8u282`, `8`, `latest` (*8u282/Dockerfile*)][92]

 * [`7u292`, `7` (*7u292/Dockerfile*)][59]

Previous
--------

Earlier Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-15 are as follows:
* [15.0.1][118]

* [14.0.1][116]

* [13.0.1][110], [13.0.2][111], [13.0.3][112], [13.0.4][113], [13.0.5][114]

* [12.0.1][108], [12.0.2][109]

* [11.0.1][98], [11.0.2][99], [11.0.3][100], [11.0.4][101], [11.0.5][102], [11.0.6][103], [11.0.7][104], [11.0.8][105], [11.0.9][106]

* [9u01][93], [9u04][94], [9u07][95]

* [8u05][60], [8u11][61], [8u20][62], [8u25][63], [8u31][64], [8u40][65], [8u45][66], [8u51][67], [8u60][68], [8u65][69], [8u66][70], [8u72][71], [8u92][72], [8u102][73], [8u112][74], [8u121][75], [8u131][76], [8u144][77], [8u152][78], [8u162][79], [8u172][80], [8u181][81], [8u192][82], [8u202][83], [8u212][84], [8u222][85], [8u232][86], [8u242][87], [8u252][88], [8u262][89], [8u272][90], [8u275][91]

* [7u55][29], [7u60][30], [7u65][31], [7u72][32], [7u76][33], [7u79][34], [7u80][35], [7u85][36], [7u91][37], [7u95][38], [7u101][39], [7u111][40], [7u121][41], [7u131][42], [7u141][43], [7u154][44], [7u161][45], [7u171][46], [7u181][47], [7u191][48], [7u201][49], [7u211][50], [7u222][51], [7u232][52], [7u242][53], [7u252][54], [7u262][55], [7u272][56], [7u275][57], [7u282][58]

* [6u49][10], [6u53][11], [6u56][12], [6u59][13], [6u63][14], [6u69][15], [6u73][16], [6u77][17], [6u79][18], [6u83][19], [6u87][20], [6u89][21], [6u93][22], [6u97][23], [6u99][24], [6u103][25], [6u107][26], [6u113][27], [6u119][28]

Usage
=====

This Azul Zulu repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 7-16 of Azul Zulu are compliant with Java SE 7-16 respectively.

To run a container of your choice, use commands below as an example.

To run Azul Zulu OpenJDK 11 in a container, enter:

    docker run -it --rm azul/zulu-openjdk:11 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: https://www.azul.com/
  [3]: https://www.azul.com/products/zulu-community/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk

  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/centos/6u49-6.4.0.6/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u59-6.7.0.2/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u63-6.8.0.1/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u69-6.9.0.3/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u73-6.10.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u77-6.11.0.2/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u79-6.12.0.2/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u83-6.13.0.3/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u87-6.14.0.1/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u89-6.15.0.1/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u93-6.16.0.1/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u97-6.17.0.1/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u99-6.18.0.3/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u103-6.19.0.1/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u107-6.20.0.1/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u113-6.21.0.3/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u119-6.22.0.3/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u72-7.7.0.1/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u76-7.8.0.3/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u79-7.9.0.2/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u80-7.10.0.1/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u85-7.11.0.3/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u91-7.12.0.3/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u95-7.13.0.1/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u101-7.14.0.5/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u111-7.15.0.1/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u121-7.16.0.1/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u131-7.17.0.5/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u141-7.18.0.3/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u154-7.20.0.3/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u161-7.21.0.3/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u171-7.22.0.3/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u181-7.23.0.1/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u191-7.24.0.1/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u201-7.25.0.5/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u211-7.27.0.1/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u222-7.29.0.5/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u232-7.31.0.5/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u242-7.34.0.5/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u252-7.36.0.5/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u262-7.38.0.11/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u272-7.40.0.15/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u282-7.42.0.13/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u285-7.42.0.51/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u292-7.44.0.11/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u25-8.4.0.1/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u31-8.5.0.1/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u40-8.6.0.1/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u45-8.7.0.5/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u51-8.8.0.3/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u60-8.9.0.4/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u65-8.10.0.1/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u66-8.11.0.1/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u72-8.13.0.5/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u92-8.15.0.1/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u102-8.17.0.3/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u112-8.19.0.1/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u121-8.20.0.5/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u131-8.21.0.1/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u144-8.23.0.3/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u152-8.25.0.1/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u162-8.27.0.7/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u172-8.30.0.1/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u181-8.31.0.1/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u192-8.33.0.1/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u202-8.36.0.1/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u212-8.38.0.13/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u222-8.40.0.25/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u232-8.42.0.23/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u242-8.44.0.11/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u252-8.46.0.19/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u262-8.48.0.51/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u272-8.50.0.21/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u275-8.50.0.53/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u282-8.52.0.23/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u07-9.0.7.1/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.4-11.33/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.5-11.35/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.6-11.37/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.7-11.39.15/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.8-11.41.23/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.9-11.43.21/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.10-11.45.27/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.4-13.33.25/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.5-13.35.17/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.6-13.37.21/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile