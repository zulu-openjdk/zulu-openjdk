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

Tags and `Dockerfile` links
===========================

Most Recent
-----------

  * [`17.0.0-17.28.13`, `17-latest` (*17-latest/Dockerfile)*][10]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][16]
  * [`15.0.5-15.36.13`, `15-latest` (*15-latest/Dockerfile)*][23]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][30]
  * [`13.0.9-13.44.13`, `13-latest` (*13-latest/Dockerfile)*][33]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][43]
  * [`11.0.13-11.52.13`, `11-latest` (*11-latest/Dockerfile)*][47]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][61]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][64]
  * [`8u312-8.58.0.13`, `8-latest` (*8-latest/Dockerfile)*][69]
  * [`7u322-7.50.0.11`, `7-latest` (*7-latest/Dockerfile)*][106]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][141]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [17-jre-headless-latest][14],
  [17.0.0-17.28.13-jre-headless][15],
  
  * [17-jre-latest][11],
  [17.0.0-17.28.13-jre][13],
  
  * [16-jre-latest][17],
  [16.0.0-16.28.11-jre][20],
  [16.0.1-16.30.15-jre][21],
  [16.0.2-16.32.15-jre][22],
  
  * [17-latest][10],
  [17.0.0-17.28.13][12],
  
  * [16-latest][16],
  [16.0.0-16.28.11][18],
  [16.0.2-16.32.15][19],
  
  * [15-latest][23],
  [15.0.1-15.28.13][24],
  [15.0.1-15.28.51][25],
  [15.0.2-15.29.15][26],
  [15.0.3-15.32.15][27],
  [15.0.4-15.34.17][28],
  [15.0.5-15.36.13][29],
  
  * [14-latest][30],
  [14.0.1-14.28.21][31],
  [14.0.2-14.29.23][32],
  
  * [13-latest][33],
  [13.0.1-13.28][34],
  [13.0.2-13.29][35],
  [13.0.3-13.31.11][36],
  [13.0.4-13.33.25][37],
  [13.0.5-13.35.17][38],
  [13.0.6-13.37.21][39],
  [13.0.7-13.40.15][40],
  [13.0.8-13.42.17][41],
  [13.0.9-13.44.13][42],
  
  * [12-12.1][43],
  [12-latest][44],
  [12.0.1-12.2][45],
  [12.0.2-12.3][46],
  
  * [11-latest][47],
  [11.0.1-11.2][48],
  [11.0.2-11.29][49],
  [11.0.3-11.31][50],
  [11.0.4-11.33][51],
  [11.0.5-11.35][52],
  [11.0.6-11.37][53],
  [11.0.7-11.39.15][54],
  [11.0.8-11.41.23][55],
  [11.0.9-11.43.21][56],
  [11.0.10-11.45.27][57],
  [11.0.11-11.48.21][58],
  [11.0.12-11.50.19][59],
  [11.0.13-11.52.13][60],
  
  * [10-latest][61],
  [10u01-10.2][62],
  [10u02-10.3][63],
  
  * [9-ea][64],
  [9-latest][65],
  [9u01-9.0.1.3][66],
  [9u04-9.0.4.1][67],
  [9u07-9.0.7.1][68],
  
  * [8-latest][69],
  [8u05-8.1.0.6][70],
  [8u11-8.2.0.1][71],
  [8u20-8.3.0.1][72],
  [8u25-8.4.0.1][73],
  [8u31-8.5.0.1][74],
  [8u40-8.6.0.1][75],
  [8u45-8.7.0.5][76],
  [8u51-8.8.0.3][77],
  [8u60-8.9.0.4][78],
  [8u65-8.10.0.1][79],
  [8u66-8.11.0.1][80],
  [8u72-8.13.0.5][81],
  [8u92-8.15.0.1][82],
  [8u102-8.17.0.3][83],
  [8u112-8.19.0.1][84],
  [8u121-8.20.0.5][85],
  [8u131-8.21.0.1][86],
  [8u144-8.23.0.3][87],
  [8u152-8.25.0.1][88],
  [8u162-8.27.0.7][89],
  [8u172-8.30.0.1][90],
  [8u181-8.31.0.1][91],
  [8u192-8.33.0.1][92],
  [8u202-8.36.0.1][93],
  [8u212-8.38.0.13][94],
  [8u222-8.40.0.25][95],
  [8u232-8.42.0.21][96],
  [8u232-8.42.0.23][97],
  [8u242-8.44.0.11][98],
  [8u252-8.46.0.19][99],
  [8u262-8.48.0.51][100],
  [8u272-8.50.0.21][101],
  [8u275-8.50.0.53][102],
  [8u282-8.52.0.23][103],
  [8u302-8.56.0.21][104],
  [8u312-8.58.0.13][105],
  
  * [7-latest][106],
  [7u55-7.4.0.5][107],
  [7u60-7.5.0.1][108],
  [7u65-7.6.0.1][109],
  [7u72-7.7.0.1][110],
  [7u76-7.8.0.3][111],
  [7u79-7.9.0.2][112],
  [7u80-7.10.0.1][113],
  [7u85-7.11.0.3][114],
  [7u91-7.12.0.3][115],
  [7u95-7.13.0.1][116],
  [7u101-7.14.0.5][117],
  [7u111-7.15.0.1][118],
  [7u121-7.16.0.1][119],
  [7u131-7.17.0.5][120],
  [7u141-7.18.0.3][121],
  [7u154-7.20.0.3][122],
  [7u161-7.21.0.3][123],
  [7u171-7.22.0.3][124],
  [7u181-7.23.0.1][125],
  [7u191-7.24.0.1][126],
  [7u201-7.25.0.5][127],
  [7u211-7.27.0.1][128],
  [7u222-7.29.0.5][129],
  [7u232-7.31.0.5][130],
  [7u242-7.34.0.5][131],
  [7u252-7.36.0.5][132],
  [7u262-7.38.0.11][133],
  [7u272-7.40.0.15][134],
  [7u282-7.42.0.13][135],
  [7u285-7.42.0.51][136],
  [7u292-7.44.0.11][137],
  [7u302-7.46.0.11][138],
  [7u312-7.48.0.11][139],
  [7u322-7.50.0.11][140],
  
  * [6-latest][141],
  [6u49-6.4.0.6][142],
  [6u53-6.5.0.2][143],
  [6u56-6.6.0.1][144],
  [6u59-6.7.0.2][145],
  [6u63-6.8.0.1][146],
  [6u69-6.9.0.3][147],
  [6u73-6.10.0.3][148],
  [6u77-6.11.0.2][149],
  [6u79-6.12.0.2][150],
  [6u83-6.13.0.3][151],
  [6u87-6.14.0.1][152],
  [6u89-6.15.0.1][153],
  [6u93-6.16.0.1][154],
  [6u97-6.17.0.1][155],
  [6u99-6.18.0.3][156],
  [6u103-6.19.0.1][157],
  [6u107-6.20.0.1][158],
  [6u113-6.21.0.3][159],
  [6u119-6.22.0.3][160],
  

Usage
=====

This repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 7-17 of Zulu are compliant with Java SE 7-17 respectively.

To run a container of your choice, use the commands below as an example.

For Azul Zulu 11, run:

    docker run -it --rm azul/zulu-openjdk:11 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: https://www.azul.com/
  [3]: https://www.azul.com/products/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk


  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  