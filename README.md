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

  * [`18.0.2-18.32.11`, `18-latest` (*18-latest/Dockerfile)*][10]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][19]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][40]
  * [`15.0.8-15.42.15`, `15-latest` (*15-latest/Dockerfile)*][47]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][63]
  * [`13.0.12-13.50.15`, `13-latest` (*13-latest/Dockerfile)*][66]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][85]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][89]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][116]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][119]
  * [`8u345-8.64.0.19`, `8-latest` (*8-latest/Dockerfile)*][124]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][173]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][211]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [18-jre-headless-latest][16],
  [18.0.1-18.30.11-jre-headless][17],
  [18.0.2-18.32.11-jre-headless][18],
  
  * [17-jre-headless-latest][33],
  [17.0.0-17.28.13-jre-headless][34],
  [17.0.1-17.30.15-jre-headless][35],
  [17.0.2-17.32.13-jre-headless][36],
  [17.0.3-17.34.19-jre-headless][37],
  [17.0.4-17.36.13-jre-headless][38],
  [17.0.4.1-17.36.17-jre-headless][39],
  
  * [15-jre-headless-latest][60],
  [15.0.7-15.40.19-jre-headless][61],
  [15.0.8-15.42.15-jre-headless][62],
  
  * [13-jre-headless-latest][82],
  [13.0.11-13.48.19-jre-headless][83],
  [13.0.12-13.50.15-jre-headless][84],
  
  * [11-jre-headless-latest][111],
  [11.0.15-11.56.19-jre-headless][113],
  [11.0.16-11.58.15-jre-headless][114],
  [11.0.16.1-11.58.23-jre-headless][115],
  
  * [8-jre-headless-latest][169],
  [8u332-8.62.0.19-jre-headless][170],
  [8u342-8.64.0.15-jre-headless][171],
  [8u345-8.64.0.19-jre-headless][172],
  
  * [18-jre-latest][11],
  [18.0.1-18.30.11-jre][14],
  [18.0.2-18.32.11-jre][15],
  
  * [17-jre-latest][20],
  [17.0.0-17.28.13-jre][27],
  [17.0.1-17.30.15-jre][28],
  [17.0.2-17.32.13-jre][29],
  [17.0.3-17.34.19-jre][30],
  [17.0.4-17.36.13-jre][31],
  [17.0.4.1-17.36.17-jre][32],
  
  * [16-jre-latest][41],
  [16.0.0-16.28.11-jre][44],
  [16.0.1-16.30.15-jre][45],
  [16.0.2-16.32.15-jre][46],
  
  * [15-jre-latest][48],
  [15.0.7-15.40.19-jre][58],
  [15.0.8-15.42.15-jre][59],
  
  * [13-jre-latest][69],
  [13.0.11-13.48.19-jre][80],
  [13.0.12-13.50.15-jre][81],
  
  * [11-jre-latest][96],
  [11.0.15-11.56.19-jre][109],
  [11.0.16-11.58.15-jre][110],
  [11.0.16.1-11.58.23-jre][112],
  
  * [8-jre-latest][125],
  [8u332-8.62.0.19-jre][166],
  [8u342-8.64.0.15-jre][167],
  [8u345-8.64.0.19-jre][168],
  
  * [18-latest][10],
  [18.0.1-18.30.11][12],
  [18.0.2-18.32.11][13],
  
  * [17-latest][19],
  [17.0.0-17.28.13][21],
  [17.0.1-17.30.15][22],
  [17.0.2-17.32.13][23],
  [17.0.3-17.34.19][24],
  [17.0.4-17.36.13][25],
  [17.0.4.1-17.36.17][26],
  
  * [16-latest][40],
  [16.0.0-16.28.11][42],
  [16.0.2-16.32.15][43],
  
  * [15-latest][47],
  [15.0.1-15.28.13][49],
  [15.0.1-15.28.51][50],
  [15.0.2-15.29.15][51],
  [15.0.3-15.32.15][52],
  [15.0.4-15.34.17][53],
  [15.0.5-15.36.13][54],
  [15.0.6-15.38.17][55],
  [15.0.7-15.40.19][56],
  [15.0.8-15.42.15][57],
  
  * [14-latest][63],
  [14.0.1-14.28.21][64],
  [14.0.2-14.29.23][65],
  
  * [13-latest][66],
  [13.0.1-13.28][67],
  [13.0.2-13.29][68],
  [13.0.3-13.31.11][70],
  [13.0.4-13.33.25][71],
  [13.0.5-13.35.17][72],
  [13.0.6-13.37.21][73],
  [13.0.7-13.40.15][74],
  [13.0.8-13.42.17][75],
  [13.0.9-13.44.13][76],
  [13.0.10-13.46.15][77],
  [13.0.11-13.48.19][78],
  [13.0.12-13.50.15][79],
  
  * [12-12.1][85],
  [12-latest][86],
  [12.0.1-12.2][87],
  [12.0.2-12.3][88],
  
  * [11-latest][89],
  [11.0.1-11.2][90],
  [11.0.2-11.29][91],
  [11.0.3-11.31][92],
  [11.0.4-11.33][93],
  [11.0.5-11.35][94],
  [11.0.6-11.37][95],
  [11.0.7-11.39.15][97],
  [11.0.8-11.41.23][98],
  [11.0.9-11.43.21][99],
  [11.0.10-11.45.27][100],
  [11.0.11-11.48.21][101],
  [11.0.12-11.50.19][102],
  [11.0.13-11.52.13][103],
  [11.0.14-11.54.23][104],
  [11.0.15-11.56.19][105],
  [11.0.16-11.58.15][106],
  [11.0.14.1-11.54.25][107],
  [11.0.16.1-11.58.23][108],
  
  * [10-latest][116],
  [10u01-10.2][117],
  [10u02-10.3][118],
  
  * [9-ea][119],
  [9-latest][120],
  [9u01-9.0.1.3][121],
  [9u04-9.0.4.1][122],
  [9u07-9.0.7.1][123],
  
  * [8-latest][124],
  [8u05-8.1.0.6][126],
  [8u11-8.2.0.1][127],
  [8u20-8.3.0.1][128],
  [8u25-8.4.0.1][129],
  [8u31-8.5.0.1][130],
  [8u40-8.6.0.1][131],
  [8u45-8.7.0.5][132],
  [8u51-8.8.0.3][133],
  [8u60-8.9.0.4][134],
  [8u65-8.10.0.1][135],
  [8u66-8.11.0.1][136],
  [8u72-8.13.0.5][137],
  [8u92-8.15.0.1][138],
  [8u102-8.17.0.3][139],
  [8u112-8.19.0.1][140],
  [8u121-8.20.0.5][141],
  [8u131-8.21.0.1][142],
  [8u144-8.23.0.3][143],
  [8u152-8.25.0.1][144],
  [8u162-8.27.0.7][145],
  [8u172-8.30.0.1][146],
  [8u181-8.31.0.1][147],
  [8u192-8.33.0.1][148],
  [8u202-8.36.0.1][149],
  [8u212-8.38.0.13][150],
  [8u222-8.40.0.25][151],
  [8u232-8.42.0.21][152],
  [8u232-8.42.0.23][153],
  [8u242-8.44.0.11][154],
  [8u252-8.46.0.19][155],
  [8u262-8.48.0.51][156],
  [8u272-8.50.0.21][157],
  [8u275-8.50.0.53][158],
  [8u282-8.52.0.23][159],
  [8u302-8.56.0.21][160],
  [8u312-8.58.0.13][161],
  [8u322-8.60.0.21][162],
  [8u332-8.62.0.19][163],
  [8u342-8.64.0.15][164],
  [8u345-8.64.0.19][165],
  
  * [7-latest][173],
  [7u55-7.4.0.5][174],
  [7u60-7.5.0.1][175],
  [7u65-7.6.0.1][176],
  [7u72-7.7.0.1][177],
  [7u76-7.8.0.3][178],
  [7u79-7.9.0.2][179],
  [7u80-7.10.0.1][180],
  [7u85-7.11.0.3][181],
  [7u91-7.12.0.3][182],
  [7u95-7.13.0.1][183],
  [7u101-7.14.0.5][184],
  [7u111-7.15.0.1][185],
  [7u121-7.16.0.1][186],
  [7u131-7.17.0.5][187],
  [7u141-7.18.0.3][188],
  [7u154-7.20.0.3][189],
  [7u161-7.21.0.3][190],
  [7u171-7.22.0.3][191],
  [7u181-7.23.0.1][192],
  [7u191-7.24.0.1][193],
  [7u201-7.25.0.5][194],
  [7u211-7.27.0.1][195],
  [7u222-7.29.0.5][196],
  [7u232-7.31.0.5][197],
  [7u242-7.34.0.5][198],
  [7u252-7.36.0.5][199],
  [7u262-7.38.0.11][200],
  [7u272-7.40.0.15][201],
  [7u282-7.42.0.13][202],
  [7u285-7.42.0.51][203],
  [7u292-7.44.0.11][204],
  [7u302-7.46.0.11][205],
  [7u312-7.48.0.11][206],
  [7u322-7.50.0.11][207],
  [7u332-7.52.0.11][208],
  [7u342-7.54.0.13][209],
  [7u352-7.56.0.11][210],
  
  * [6-latest][211],
  [6u49-6.4.0.6][212],
  [6u53-6.5.0.2][213],
  [6u56-6.6.0.1][214],
  [6u59-6.7.0.2][215],
  [6u63-6.8.0.1][216],
  [6u69-6.9.0.3][217],
  [6u73-6.10.0.3][218],
  [6u77-6.11.0.2][219],
  [6u79-6.12.0.2][220],
  [6u83-6.13.0.3][221],
  [6u87-6.14.0.1][222],
  [6u89-6.15.0.1][223],
  [6u93-6.16.0.1][224],
  [6u97-6.17.0.1][225],
  [6u99-6.18.0.3][226],
  [6u103-6.19.0.1][227],
  [6u107-6.20.0.1][228],
  [6u113-6.21.0.3][229],
  [6u119-6.22.0.3][230],
  

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


  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-headless-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre-headless/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre-headless/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre-headless/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre-headless/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre-headless/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-headless-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre-headless/Dockerfile
  
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-headless-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre-headless/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre-headless/Dockerfile
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-headless-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre-headless/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre-headless/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-headless-latest/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre-headless/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre-headless/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre/Dockerfile
  
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre/Dockerfile
  
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre/Dockerfile
  
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-latest/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15/Dockerfile
  
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14.1-11.54.25/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23/Dockerfile
  
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19/Dockerfile
  
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u342-7.54.0.13/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u352-7.56.0.11/Dockerfile
  
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  