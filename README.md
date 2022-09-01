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

  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][10]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][22]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][43]
  * [`15.0.8-15.42.15`, `15-latest` (*15-latest/Dockerfile)*][50]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][66]
  * [`13.0.12-13.50.15`, `13-latest` (*13-latest/Dockerfile)*][69]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][88]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][92]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][119]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][122]
  * [`8u345-8.64.0.19`, `8-latest` (*8-latest/Dockerfile)*][127]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][176]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][214]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [18-jre-headless-latest][18],
  [18.0.1-18.30.11-jre-headless][19],
  [18.0.2-18.32.11-jre-headless][20],
  [18.0.2.1-18.32.13-jre-headless][21],
  
  * [17-jre-headless-latest][36],
  [17.0.0-17.28.13-jre-headless][37],
  [17.0.1-17.30.15-jre-headless][38],
  [17.0.2-17.32.13-jre-headless][39],
  [17.0.3-17.34.19-jre-headless][40],
  [17.0.4-17.36.13-jre-headless][41],
  [17.0.4.1-17.36.17-jre-headless][42],
  
  * [15-jre-headless-latest][63],
  [15.0.7-15.40.19-jre-headless][64],
  [15.0.8-15.42.15-jre-headless][65],
  
  * [13-jre-headless-latest][85],
  [13.0.11-13.48.19-jre-headless][86],
  [13.0.12-13.50.15-jre-headless][87],
  
  * [11-jre-headless-latest][114],
  [11.0.15-11.56.19-jre-headless][116],
  [11.0.16-11.58.15-jre-headless][117],
  [11.0.16.1-11.58.23-jre-headless][118],
  
  * [8-jre-headless-latest][172],
  [8u332-8.62.0.19-jre-headless][173],
  [8u342-8.64.0.15-jre-headless][174],
  [8u345-8.64.0.19-jre-headless][175],
  
  * [18-jre-latest][11],
  [18.0.1-18.30.11-jre][15],
  [18.0.2-18.32.11-jre][16],
  [18.0.2.1-18.32.13-jre][17],
  
  * [17-jre-latest][23],
  [17.0.0-17.28.13-jre][30],
  [17.0.1-17.30.15-jre][31],
  [17.0.2-17.32.13-jre][32],
  [17.0.3-17.34.19-jre][33],
  [17.0.4-17.36.13-jre][34],
  [17.0.4.1-17.36.17-jre][35],
  
  * [16-jre-latest][44],
  [16.0.0-16.28.11-jre][47],
  [16.0.1-16.30.15-jre][48],
  [16.0.2-16.32.15-jre][49],
  
  * [15-jre-latest][51],
  [15.0.7-15.40.19-jre][61],
  [15.0.8-15.42.15-jre][62],
  
  * [13-jre-latest][72],
  [13.0.11-13.48.19-jre][83],
  [13.0.12-13.50.15-jre][84],
  
  * [11-jre-latest][99],
  [11.0.15-11.56.19-jre][112],
  [11.0.16-11.58.15-jre][113],
  [11.0.16.1-11.58.23-jre][115],
  
  * [8-jre-latest][128],
  [8u332-8.62.0.19-jre][169],
  [8u342-8.64.0.15-jre][170],
  [8u345-8.64.0.19-jre][171],
  
  * [18-latest][10],
  [18.0.1-18.30.11][12],
  [18.0.2-18.32.11][13],
  [18.0.2.1-18.32.13][14],
  
  * [17-latest][22],
  [17.0.0-17.28.13][24],
  [17.0.1-17.30.15][25],
  [17.0.2-17.32.13][26],
  [17.0.3-17.34.19][27],
  [17.0.4-17.36.13][28],
  [17.0.4.1-17.36.17][29],
  
  * [16-latest][43],
  [16.0.0-16.28.11][45],
  [16.0.2-16.32.15][46],
  
  * [15-latest][50],
  [15.0.1-15.28.13][52],
  [15.0.1-15.28.51][53],
  [15.0.2-15.29.15][54],
  [15.0.3-15.32.15][55],
  [15.0.4-15.34.17][56],
  [15.0.5-15.36.13][57],
  [15.0.6-15.38.17][58],
  [15.0.7-15.40.19][59],
  [15.0.8-15.42.15][60],
  
  * [14-latest][66],
  [14.0.1-14.28.21][67],
  [14.0.2-14.29.23][68],
  
  * [13-latest][69],
  [13.0.1-13.28][70],
  [13.0.2-13.29][71],
  [13.0.3-13.31.11][73],
  [13.0.4-13.33.25][74],
  [13.0.5-13.35.17][75],
  [13.0.6-13.37.21][76],
  [13.0.7-13.40.15][77],
  [13.0.8-13.42.17][78],
  [13.0.9-13.44.13][79],
  [13.0.10-13.46.15][80],
  [13.0.11-13.48.19][81],
  [13.0.12-13.50.15][82],
  
  * [12-12.1][88],
  [12-latest][89],
  [12.0.1-12.2][90],
  [12.0.2-12.3][91],
  
  * [11-latest][92],
  [11.0.1-11.2][93],
  [11.0.2-11.29][94],
  [11.0.3-11.31][95],
  [11.0.4-11.33][96],
  [11.0.5-11.35][97],
  [11.0.6-11.37][98],
  [11.0.7-11.39.15][100],
  [11.0.8-11.41.23][101],
  [11.0.9-11.43.21][102],
  [11.0.10-11.45.27][103],
  [11.0.11-11.48.21][104],
  [11.0.12-11.50.19][105],
  [11.0.13-11.52.13][106],
  [11.0.14-11.54.23][107],
  [11.0.15-11.56.19][108],
  [11.0.16-11.58.15][109],
  [11.0.14.1-11.54.25][110],
  [11.0.16.1-11.58.23][111],
  
  * [10-latest][119],
  [10u01-10.2][120],
  [10u02-10.3][121],
  
  * [9-ea][122],
  [9-latest][123],
  [9u01-9.0.1.3][124],
  [9u04-9.0.4.1][125],
  [9u07-9.0.7.1][126],
  
  * [8-latest][127],
  [8u05-8.1.0.6][129],
  [8u11-8.2.0.1][130],
  [8u20-8.3.0.1][131],
  [8u25-8.4.0.1][132],
  [8u31-8.5.0.1][133],
  [8u40-8.6.0.1][134],
  [8u45-8.7.0.5][135],
  [8u51-8.8.0.3][136],
  [8u60-8.9.0.4][137],
  [8u65-8.10.0.1][138],
  [8u66-8.11.0.1][139],
  [8u72-8.13.0.5][140],
  [8u92-8.15.0.1][141],
  [8u102-8.17.0.3][142],
  [8u112-8.19.0.1][143],
  [8u121-8.20.0.5][144],
  [8u131-8.21.0.1][145],
  [8u144-8.23.0.3][146],
  [8u152-8.25.0.1][147],
  [8u162-8.27.0.7][148],
  [8u172-8.30.0.1][149],
  [8u181-8.31.0.1][150],
  [8u192-8.33.0.1][151],
  [8u202-8.36.0.1][152],
  [8u212-8.38.0.13][153],
  [8u222-8.40.0.25][154],
  [8u232-8.42.0.21][155],
  [8u232-8.42.0.23][156],
  [8u242-8.44.0.11][157],
  [8u252-8.46.0.19][158],
  [8u262-8.48.0.51][159],
  [8u272-8.50.0.21][160],
  [8u275-8.50.0.53][161],
  [8u282-8.52.0.23][162],
  [8u302-8.56.0.21][163],
  [8u312-8.58.0.13][164],
  [8u322-8.60.0.21][165],
  [8u332-8.62.0.19][166],
  [8u342-8.64.0.15][167],
  [8u345-8.64.0.19][168],
  
  * [7-latest][176],
  [7u55-7.4.0.5][177],
  [7u60-7.5.0.1][178],
  [7u65-7.6.0.1][179],
  [7u72-7.7.0.1][180],
  [7u76-7.8.0.3][181],
  [7u79-7.9.0.2][182],
  [7u80-7.10.0.1][183],
  [7u85-7.11.0.3][184],
  [7u91-7.12.0.3][185],
  [7u95-7.13.0.1][186],
  [7u101-7.14.0.5][187],
  [7u111-7.15.0.1][188],
  [7u121-7.16.0.1][189],
  [7u131-7.17.0.5][190],
  [7u141-7.18.0.3][191],
  [7u154-7.20.0.3][192],
  [7u161-7.21.0.3][193],
  [7u171-7.22.0.3][194],
  [7u181-7.23.0.1][195],
  [7u191-7.24.0.1][196],
  [7u201-7.25.0.5][197],
  [7u211-7.27.0.1][198],
  [7u222-7.29.0.5][199],
  [7u232-7.31.0.5][200],
  [7u242-7.34.0.5][201],
  [7u252-7.36.0.5][202],
  [7u262-7.38.0.11][203],
  [7u272-7.40.0.15][204],
  [7u282-7.42.0.13][205],
  [7u285-7.42.0.51][206],
  [7u292-7.44.0.11][207],
  [7u302-7.46.0.11][208],
  [7u312-7.48.0.11][209],
  [7u322-7.50.0.11][210],
  [7u332-7.52.0.11][211],
  [7u342-7.54.0.13][212],
  [7u352-7.56.0.11][213],
  
  * [6-latest][214],
  [6u49-6.4.0.6][215],
  [6u53-6.5.0.2][216],
  [6u56-6.6.0.1][217],
  [6u59-6.7.0.2][218],
  [6u63-6.8.0.1][219],
  [6u69-6.9.0.3][220],
  [6u73-6.10.0.3][221],
  [6u77-6.11.0.2][222],
  [6u79-6.12.0.2][223],
  [6u83-6.13.0.3][224],
  [6u87-6.14.0.1][225],
  [6u89-6.15.0.1][226],
  [6u93-6.16.0.1][227],
  [6u97-6.17.0.1][228],
  [6u99-6.18.0.3][229],
  [6u103-6.19.0.1][230],
  [6u107-6.20.0.1][231],
  [6u113-6.21.0.3][232],
  [6u119-6.22.0.3][233],
  

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


  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-headless-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre-headless/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre-headless/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre-headless/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-headless-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre-headless/Dockerfile
  
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-headless-latest/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre-headless/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre-headless/Dockerfile
  
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-headless-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre-headless/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre-headless/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-headless-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre-headless/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre-headless/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre/Dockerfile
  
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre/Dockerfile
  
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-latest/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-latest/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15/Dockerfile
  
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15/Dockerfile
  
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14.1-11.54.25/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23/Dockerfile
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19/Dockerfile
  
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u342-7.54.0.13/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u352-7.56.0.11/Dockerfile
  
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  