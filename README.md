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

  * [`17.0.1-17.30.15`, `17-latest` (*17-latest/Dockerfile)*][10]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][19]
  * [`15.0.6-15.38.17`, `15-latest` (*15-latest/Dockerfile)*][26]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][34]
  * [`13.0.10-13.46.15`, `13-latest` (*13-latest/Dockerfile)*][37]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][48]
  * [`11.0.14-11.54.23`, `11-latest` (*11-latest/Dockerfile)*][52]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][67]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][70]
  * [`8u322-8.60.0.21`, `8-latest` (*8-latest/Dockerfile)*][75]
  * [`7u332-7.52.0.11`, `7-latest` (*7-latest/Dockerfile)*][113]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][149]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [17-jre-headless-latest][16],
  [17.0.0-17.28.13-jre-headless][17],
  [17.0.1-17.30.15-jre-headless][18],
  
  * [17-jre-latest][11],
  [17.0.0-17.28.13-jre][14],
  [17.0.1-17.30.15-jre][15],
  
  * [16-jre-latest][20],
  [16.0.0-16.28.11-jre][23],
  [16.0.1-16.30.15-jre][24],
  [16.0.2-16.32.15-jre][25],
  
  * [17-latest][10],
  [17.0.0-17.28.13][12],
  [17.0.1-17.30.15][13],
  
  * [16-latest][19],
  [16.0.0-16.28.11][21],
  [16.0.2-16.32.15][22],
  
  * [15-latest][26],
  [15.0.1-15.28.13][27],
  [15.0.1-15.28.51][28],
  [15.0.2-15.29.15][29],
  [15.0.3-15.32.15][30],
  [15.0.4-15.34.17][31],
  [15.0.5-15.36.13][32],
  [15.0.6-15.38.17][33],
  
  * [14-latest][34],
  [14.0.1-14.28.21][35],
  [14.0.2-14.29.23][36],
  
  * [13-latest][37],
  [13.0.1-13.28][38],
  [13.0.2-13.29][39],
  [13.0.3-13.31.11][40],
  [13.0.4-13.33.25][41],
  [13.0.5-13.35.17][42],
  [13.0.6-13.37.21][43],
  [13.0.7-13.40.15][44],
  [13.0.8-13.42.17][45],
  [13.0.9-13.44.13][46],
  [13.0.10-13.46.15][47],
  
  * [12-12.1][48],
  [12-latest][49],
  [12.0.1-12.2][50],
  [12.0.2-12.3][51],
  
  * [11-latest][52],
  [11.0.1-11.2][53],
  [11.0.2-11.29][54],
  [11.0.3-11.31][55],
  [11.0.4-11.33][56],
  [11.0.5-11.35][57],
  [11.0.6-11.37][58],
  [11.0.7-11.39.15][59],
  [11.0.8-11.41.23][60],
  [11.0.9-11.43.21][61],
  [11.0.10-11.45.27][62],
  [11.0.11-11.48.21][63],
  [11.0.12-11.50.19][64],
  [11.0.13-11.52.13][65],
  [11.0.14-11.54.23][66],
  
  * [10-latest][67],
  [10u01-10.2][68],
  [10u02-10.3][69],
  
  * [9-ea][70],
  [9-latest][71],
  [9u01-9.0.1.3][72],
  [9u04-9.0.4.1][73],
  [9u07-9.0.7.1][74],
  
  * [8-latest][75],
  [8u05-8.1.0.6][76],
  [8u11-8.2.0.1][77],
  [8u20-8.3.0.1][78],
  [8u25-8.4.0.1][79],
  [8u31-8.5.0.1][80],
  [8u40-8.6.0.1][81],
  [8u45-8.7.0.5][82],
  [8u51-8.8.0.3][83],
  [8u60-8.9.0.4][84],
  [8u65-8.10.0.1][85],
  [8u66-8.11.0.1][86],
  [8u72-8.13.0.5][87],
  [8u92-8.15.0.1][88],
  [8u102-8.17.0.3][89],
  [8u112-8.19.0.1][90],
  [8u121-8.20.0.5][91],
  [8u131-8.21.0.1][92],
  [8u144-8.23.0.3][93],
  [8u152-8.25.0.1][94],
  [8u162-8.27.0.7][95],
  [8u172-8.30.0.1][96],
  [8u181-8.31.0.1][97],
  [8u192-8.33.0.1][98],
  [8u202-8.36.0.1][99],
  [8u212-8.38.0.13][100],
  [8u222-8.40.0.25][101],
  [8u232-8.42.0.21][102],
  [8u232-8.42.0.23][103],
  [8u242-8.44.0.11][104],
  [8u252-8.46.0.19][105],
  [8u262-8.48.0.51][106],
  [8u272-8.50.0.21][107],
  [8u275-8.50.0.53][108],
  [8u282-8.52.0.23][109],
  [8u302-8.56.0.21][110],
  [8u312-8.58.0.13][111],
  [8u322-8.60.0.21][112],
  
  * [7-latest][113],
  [7u55-7.4.0.5][114],
  [7u60-7.5.0.1][115],
  [7u65-7.6.0.1][116],
  [7u72-7.7.0.1][117],
  [7u76-7.8.0.3][118],
  [7u79-7.9.0.2][119],
  [7u80-7.10.0.1][120],
  [7u85-7.11.0.3][121],
  [7u91-7.12.0.3][122],
  [7u95-7.13.0.1][123],
  [7u101-7.14.0.5][124],
  [7u111-7.15.0.1][125],
  [7u121-7.16.0.1][126],
  [7u131-7.17.0.5][127],
  [7u141-7.18.0.3][128],
  [7u154-7.20.0.3][129],
  [7u161-7.21.0.3][130],
  [7u171-7.22.0.3][131],
  [7u181-7.23.0.1][132],
  [7u191-7.24.0.1][133],
  [7u201-7.25.0.5][134],
  [7u211-7.27.0.1][135],
  [7u222-7.29.0.5][136],
  [7u232-7.31.0.5][137],
  [7u242-7.34.0.5][138],
  [7u252-7.36.0.5][139],
  [7u262-7.38.0.11][140],
  [7u272-7.40.0.15][141],
  [7u282-7.42.0.13][142],
  [7u285-7.42.0.51][143],
  [7u292-7.44.0.11][144],
  [7u302-7.46.0.11][145],
  [7u312-7.48.0.11][146],
  [7u322-7.50.0.11][147],
  [7u332-7.52.0.11][148],
  
  * [6-latest][149],
  [6u49-6.4.0.6][150],
  [6u53-6.5.0.2][151],
  [6u56-6.6.0.1][152],
  [6u59-6.7.0.2][153],
  [6u63-6.8.0.1][154],
  [6u69-6.9.0.3][155],
  [6u73-6.10.0.3][156],
  [6u77-6.11.0.2][157],
  [6u79-6.12.0.2][158],
  [6u83-6.13.0.3][159],
  [6u87-6.14.0.1][160],
  [6u89-6.15.0.1][161],
  [6u93-6.16.0.1][162],
  [6u97-6.17.0.1][163],
  [6u99-6.18.0.3][164],
  [6u103-6.19.0.1][165],
  [6u107-6.20.0.1][166],
  [6u113-6.21.0.3][167],
  [6u119-6.22.0.3][168],
  

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


  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  