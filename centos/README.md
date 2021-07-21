What is Azul Zulu? 
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

  * [`6u119`, `6` (*6-latest/Dockerfile)*][10]
  * [`7u312`, `7` (*7-latest/Dockerfile)*][29]
  * [`8u302`, `8` (*8-latest/Dockerfile)*][61]
  * [`9u07`, `9` (*9-ea/Dockerfile)*][96]
  * [`10u02`, `10` (*10-latest/Dockerfile)*][100]
  * [`11.0.12`, `11` (*11-latest/Dockerfile)*][103]
  * [`12.0.2`, `12` (*12-12.1/Dockerfile)*][116]
  * [`13.0.8`, `13` (*13-latest/Dockerfile)*][119]
  * [`14.0.2`, `14` (*14-latest/Dockerfile)*][128]
  * [`15.0.4`, `15` (*15-latest/Dockerfile)*][131]
  * [`16.0.1`, `16` (*16-latest/Dockerfile)*][137]

Previous
--------

Earlier Ubuntu Docker image tags of Azul Zulu:

  * [6][10],
  [6u53][11],
  [6u56][12],
  [6u59][13],
  [6u63][14],
  [6u69][15],
  [6u73][16],
  [6u77][17],
  [6u79][18],
  [6u83][19],
  [6u87][20],
  [6u89][21],
  [6u93][22],
  [6u97][23],
  [6u99][24],
  [6u103][25],
  [6u107][26],
  [6u113][27],
  [6u119][28],
  
  * [7][29],
  [7u65][30],
  [7u72][31],
  [7u76][32],
  [7u79][33],
  [7u80][34],
  [7u85][35],
  [7u91][36],
  [7u95][37],
  [7u101][38],
  [7u111][39],
  [7u121][40],
  [7u131][41],
  [7u141][42],
  [7u154][43],
  [7u161][44],
  [7u171][45],
  [7u181][46],
  [7u191][47],
  [7u201][48],
  [7u211][49],
  [7u222][50],
  [7u232][51],
  [7u242][52],
  [7u252][53],
  [7u262][54],
  [7u272][55],
  [7u282][56],
  [7u285][57],
  [7u292][58],
  [7u302][59],
  [7u312][60],
  
  * [8][61],
  [8u11][62],
  [8u20][63],
  [8u25][64],
  [8u31][65],
  [8u40][66],
  [8u45][67],
  [8u51][68],
  [8u60][69],
  [8u65][70],
  [8u66][71],
  [8u72][72],
  [8u92][73],
  [8u102][74],
  [8u112][75],
  [8u121][76],
  [8u131][77],
  [8u144][78],
  [8u152][79],
  [8u162][80],
  [8u172][81],
  [8u181][82],
  [8u192][83],
  [8u202][84],
  [8u212][85],
  [8u222][86],
  [8u232][87],
  [8u242][88],
  [8u252][89],
  [8u262][90],
  [8u272][91],
  [8u275][92],
  [8u282][93],
  [8u292][94],
  [8u302][95],
  
  * [9][96],
  [9u01][97],
  [9u04][98],
  [9u07][99],
  
  * [10][100],
  [10u01][101],
  [10u02][102],
  
  * [11][103],
  [11.0.1][104],
  [11.0.2][105],
  [11.0.3][106],
  [11.0.4][107],
  [11.0.5][108],
  [11.0.6][109],
  [11.0.7][110],
  [11.0.8][111],
  [11.0.9][112],
  [11.0.10][113],
  [11.0.11][114],
  [11.0.12][115],
  
  * [12][116],
  [12.0.1][117],
  [12.0.2][118],
  
  * [13][119],
  [13.0.1][120],
  [13.0.2][121],
  [13.0.3][122],
  [13.0.4][123],
  [13.0.5][124],
  [13.0.6][125],
  [13.0.7][126],
  [13.0.8][127],
  
  * [14][128],
  [14.0.1][129],
  [14.0.2][130],
  
  * [15][131],
  [15.0.0][132],
  [15.0.1][133],
  [15.0.2][134],
  [15.0.3][135],
  [15.0.4][136],
  
  * [16][137],
  [16.0.0][138],
  [16.0.1][139],
  

Usage
=====

This Azul Zulu repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 7-16 of Azul Zulu are compliant with Java SE 7-16 respectively.

To run a container of your choice, use commands below as an example.

For Azul Zulu OpenJDK 11, run:

    docker run -it --rm azul/zulu-openjdk:11 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: https://www.azul.com/
  [3]: https://www.azul.com/products/zulu-community/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk


  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6-latest/Dockerfile
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u63-6.8.0.1/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u69-6.9.0.3/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u73-6.10.0.3/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u77-6.11.0.2/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u79-6.12.0.2/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u83-6.13.0.7/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u87-6.14.0.1/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u89-6.15.0.1/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u93-6.16.0.1/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u97-6.17.0.1/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u99-6.18.0.3/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u103-6.19.0.1/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u107-6.20.0.1/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u113-6.21.0.3/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u119-6.22.0.3/Dockerfile
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7-latest/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u79-7.9.0.2/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u80-7.10.0.1/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u85-7.11.0.3/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u91-7.12.0.3/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u95-7.13.0.1/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u101-7.14.0.5/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u111-7.15.0.5/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u121-7.16.0.1/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u131-7.17.0.5/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u141-7.18.0.3/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u154-7.20.0.3/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u161-7.21.0.3/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u171-7.22.0.3/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u181-7.23.0.1/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u191-7.24.0.1/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u201-7.25.0.5/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u211-7.27.0.1/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u222-7.29.0.5/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u232-7.31.0.5/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u242-7.34.0.5/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u252-7.36.0.5/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u262-7.38.0.11/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u272-7.40.0.15/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u282-7.42.0.13/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u285-7.42.0.51/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u292-7.44.0.11/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u302-7.46.0.11/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u312-7.48.0.11/Dockerfile
  
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u11-8.2.0.1/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u20-8.3.0.1/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u25-8.4.0.1/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u31-8.5.0.1/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u40-8.6.0.1/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u45-8.7.0.5/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u51-8.8.0.3/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u60-8.9.0.4/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u65-8.10.0.1/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u66-8.11.0.1/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u72-8.13.0.5/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u92-8.15.0.1/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u102-8.17.0.7/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u112-8.19.0.1/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u121-8.20.0.5/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u131-8.21.0.1/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u144-8.23.0.3/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u152-8.25.0.1/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u162-8.27.0.7/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u172-8.30.0.1/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u181-8.31.0.1/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u192-8.33.0.1/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u202-8.36.0.1/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u212-8.38.0.13/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u222-8.40.0.25/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u232-8.42.0.23/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u242-8.44.0.11/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u252-8.46.0.19/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u262-8.48.0.51/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u272-8.50.0.21/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u275-8.50.0.53/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u282-8.52.0.23/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u292-8.54.0.21/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u302-8.56.0.21/Dockerfile
  
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-ea/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u01-9.0.1.3/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u04-9.0.4.1/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u07-9.0.7.1/Dockerfile
  
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u01-10.2/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u02-10.3/Dockerfile
  
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.1-11.2/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.2-11.29/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.3-11.31/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.4-11.33/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.5-11.35/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.6-11.37/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.7-11.39.15/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.8-11.41.23/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.9-11.43.21/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.10-11.45.27/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.11-11.48.21/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.12-11.50.19/Dockerfile
  
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-12.1/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.1-12.2/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.2-12.3/Dockerfile
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.1-13.28/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.2-13.29/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.3-13.31.11/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.4-13.33.25/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.5-13.35.17/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.6-13.37.21/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.7-13.40.15/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.8-13.42.17/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.1-14.28.21/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.2-14.29.23/Dockerfile
  
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-latest/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.0-15.27.17/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.51/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.2-15.29.15/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.3-15.32.15/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.4-15.34.17/Dockerfile
  
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11-jre/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15-jre/Dockerfile
  