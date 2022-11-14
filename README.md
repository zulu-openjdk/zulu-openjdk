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

  * [`19.0.1-19.30.11`, `19-latest` (*19-latest/Dockerfile)*][10]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][19]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][31]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][57]
  * [`15.0.9-15.44.13`, `15-latest` (*15-latest/Dockerfile)*][64]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][83]
  * [`13.0.13-13.52.15`, `13-latest` (*13-latest/Dockerfile)*][86]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][108]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][112]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][142]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][145]
  * [`8u352-8.66.0.15`, `8-latest` (*8-latest/Dockerfile)*][150]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][202]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][240]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [19-jre-headless-latest][16],
  [19.0.0-19.28.81-jre-headless][17],
  [19.0.1-19.30.11-jre-headless][18],
  
  * [18-jre-headless-latest][27],
  [18.0.1-18.30.11-jre-headless][28],
  [18.0.2-18.32.11-jre-headless][29],
  [18.0.2.1-18.32.13-jre-headless][30],
  
  * [17-jre-headless-latest][48],
  [17.0.0-17.28.13-jre-headless][50],
  [17.0.1-17.30.15-jre-headless][51],
  [17.0.2-17.32.13-jre-headless][52],
  [17.0.3-17.34.19-jre-headless][53],
  [17.0.4-17.36.13-jre-headless][54],
  [17.0.5-17.38.21-jre-headless][55],
  [17.0.4.1-17.36.17-jre-headless][56],
  
  * [15-jre-headless-latest][79],
  [15.0.7-15.40.19-jre-headless][80],
  [15.0.8-15.42.15-jre-headless][81],
  [15.0.9-15.44.13-jre-headless][82],
  
  * [13-jre-headless-latest][104],
  [13.0.11-13.48.19-jre-headless][105],
  [13.0.12-13.50.15-jre-headless][106],
  [13.0.13-13.52.15-jre-headless][107],
  
  * [11-jre-headless-latest][136],
  [11.0.15-11.56.19-jre-headless][138],
  [11.0.16-11.58.15-jre-headless][139],
  [11.0.17-11.60.19-jre-headless][140],
  [11.0.16.1-11.58.23-jre-headless][141],
  
  * [8-jre-headless-latest][197],
  [8u332-8.62.0.19-jre-headless][198],
  [8u342-8.64.0.15-jre-headless][199],
  [8u345-8.64.0.19-jre-headless][200],
  [8u352-8.66.0.15-jre-headless][201],
  
  * [17-distroless-latest][46],
  [17.0.5-17.38.21-distroless][49],
  
  * [19-jre-latest][11],
  [19.0.0-19.28.81-jre][14],
  [19.0.1-19.30.11-jre][15],
  
  * [18-jre-latest][20],
  [18.0.1-18.30.11-jre][24],
  [18.0.2-18.32.11-jre][25],
  [18.0.2.1-18.32.13-jre][26],
  
  * [17-jre-latest][32],
  [17.0.0-17.28.13-jre][40],
  [17.0.1-17.30.15-jre][41],
  [17.0.2-17.32.13-jre][42],
  [17.0.3-17.34.19-jre][43],
  [17.0.4-17.36.13-jre][44],
  [17.0.5-17.38.21-jre][45],
  [17.0.4.1-17.36.17-jre][47],
  
  * [16-jre-latest][58],
  [16.0.0-16.28.11-jre][61],
  [16.0.1-16.30.15-jre][62],
  [16.0.2-16.32.15-jre][63],
  
  * [15-jre-latest][65],
  [15.0.7-15.40.19-jre][76],
  [15.0.8-15.42.15-jre][77],
  [15.0.9-15.44.13-jre][78],
  
  * [13-jre-latest][89],
  [13.0.11-13.48.19-jre][101],
  [13.0.12-13.50.15-jre][102],
  [13.0.13-13.52.15-jre][103],
  
  * [11-jre-latest][119],
  [11.0.15-11.56.19-jre][133],
  [11.0.16-11.58.15-jre][134],
  [11.0.17-11.60.19-jre][135],
  [11.0.16.1-11.58.23-jre][137],
  
  * [8-jre-latest][151],
  [8u332-8.62.0.19-jre][193],
  [8u342-8.64.0.15-jre][194],
  [8u345-8.64.0.19-jre][195],
  [8u352-8.66.0.15-jre][196],
  
  * [19-latest][10],
  [19.0.0-19.28.81][12],
  [19.0.1-19.30.11][13],
  
  * [18-latest][19],
  [18.0.1-18.30.11][21],
  [18.0.2-18.32.11][22],
  [18.0.2.1-18.32.13][23],
  
  * [17-latest][31],
  [17.0.0-17.28.13][33],
  [17.0.1-17.30.15][34],
  [17.0.2-17.32.13][35],
  [17.0.3-17.34.19][36],
  [17.0.4-17.36.13][37],
  [17.0.5-17.38.21][38],
  [17.0.4.1-17.36.17][39],
  
  * [16-latest][57],
  [16.0.0-16.28.11][59],
  [16.0.2-16.32.15][60],
  
  * [15-latest][64],
  [15.0.1-15.28.13][66],
  [15.0.1-15.28.51][67],
  [15.0.2-15.29.15][68],
  [15.0.3-15.32.15][69],
  [15.0.4-15.34.17][70],
  [15.0.5-15.36.13][71],
  [15.0.6-15.38.17][72],
  [15.0.7-15.40.19][73],
  [15.0.8-15.42.15][74],
  [15.0.9-15.44.13][75],
  
  * [14-latest][83],
  [14.0.1-14.28.21][84],
  [14.0.2-14.29.23][85],
  
  * [13-latest][86],
  [13.0.1-13.28][87],
  [13.0.2-13.29][88],
  [13.0.3-13.31.11][90],
  [13.0.4-13.33.25][91],
  [13.0.5-13.35.17][92],
  [13.0.6-13.37.21][93],
  [13.0.7-13.40.15][94],
  [13.0.8-13.42.17][95],
  [13.0.9-13.44.13][96],
  [13.0.10-13.46.15][97],
  [13.0.11-13.48.19][98],
  [13.0.12-13.50.15][99],
  [13.0.13-13.52.15][100],
  
  * [12-12.1][108],
  [12-latest][109],
  [12.0.1-12.2][110],
  [12.0.2-12.3][111],
  
  * [11-latest][112],
  [11.0.1-11.2][113],
  [11.0.2-11.29][114],
  [11.0.3-11.31][115],
  [11.0.4-11.33][116],
  [11.0.5-11.35][117],
  [11.0.6-11.37][118],
  [11.0.7-11.39.15][120],
  [11.0.8-11.41.23][121],
  [11.0.9-11.43.21][122],
  [11.0.10-11.45.27][123],
  [11.0.11-11.48.21][124],
  [11.0.12-11.50.19][125],
  [11.0.13-11.52.13][126],
  [11.0.14-11.54.23][127],
  [11.0.15-11.56.19][128],
  [11.0.16-11.58.15][129],
  [11.0.17-11.60.19][130],
  [11.0.14.1-11.54.25][131],
  [11.0.16.1-11.58.23][132],
  
  * [10-latest][142],
  [10u01-10.2][143],
  [10u02-10.3][144],
  
  * [9-ea][145],
  [9-latest][146],
  [9u01-9.0.1.3][147],
  [9u04-9.0.4.1][148],
  [9u07-9.0.7.1][149],
  
  * [8-latest][150],
  [8u05-8.1.0.6][152],
  [8u11-8.2.0.1][153],
  [8u20-8.3.0.1][154],
  [8u25-8.4.0.1][155],
  [8u31-8.5.0.1][156],
  [8u40-8.6.0.1][157],
  [8u45-8.7.0.5][158],
  [8u51-8.8.0.3][159],
  [8u60-8.9.0.4][160],
  [8u65-8.10.0.1][161],
  [8u66-8.11.0.1][162],
  [8u72-8.13.0.5][163],
  [8u92-8.15.0.1][164],
  [8u102-8.17.0.3][165],
  [8u112-8.19.0.1][166],
  [8u121-8.20.0.5][167],
  [8u131-8.21.0.1][168],
  [8u144-8.23.0.3][169],
  [8u152-8.25.0.1][170],
  [8u162-8.27.0.7][171],
  [8u172-8.30.0.1][172],
  [8u181-8.31.0.1][173],
  [8u192-8.33.0.1][174],
  [8u202-8.36.0.1][175],
  [8u212-8.38.0.13][176],
  [8u222-8.40.0.25][177],
  [8u232-8.42.0.21][178],
  [8u232-8.42.0.23][179],
  [8u242-8.44.0.11][180],
  [8u252-8.46.0.19][181],
  [8u262-8.48.0.51][182],
  [8u272-8.50.0.21][183],
  [8u275-8.50.0.53][184],
  [8u282-8.52.0.23][185],
  [8u302-8.56.0.21][186],
  [8u312-8.58.0.13][187],
  [8u322-8.60.0.21][188],
  [8u332-8.62.0.19][189],
  [8u342-8.64.0.15][190],
  [8u345-8.64.0.19][191],
  [8u352-8.66.0.15][192],
  
  * [7-latest][202],
  [7u55-7.4.0.5][203],
  [7u60-7.5.0.1][204],
  [7u65-7.6.0.1][205],
  [7u72-7.7.0.1][206],
  [7u76-7.8.0.3][207],
  [7u79-7.9.0.2][208],
  [7u80-7.10.0.1][209],
  [7u85-7.11.0.3][210],
  [7u91-7.12.0.3][211],
  [7u95-7.13.0.1][212],
  [7u101-7.14.0.5][213],
  [7u111-7.15.0.1][214],
  [7u121-7.16.0.1][215],
  [7u131-7.17.0.5][216],
  [7u141-7.18.0.3][217],
  [7u154-7.20.0.3][218],
  [7u161-7.21.0.3][219],
  [7u171-7.22.0.3][220],
  [7u181-7.23.0.1][221],
  [7u191-7.24.0.1][222],
  [7u201-7.25.0.5][223],
  [7u211-7.27.0.1][224],
  [7u222-7.29.0.5][225],
  [7u232-7.31.0.5][226],
  [7u242-7.34.0.5][227],
  [7u252-7.36.0.5][228],
  [7u262-7.38.0.11][229],
  [7u272-7.40.0.15][230],
  [7u282-7.42.0.13][231],
  [7u285-7.42.0.51][232],
  [7u292-7.44.0.11][233],
  [7u302-7.46.0.11][234],
  [7u312-7.48.0.11][235],
  [7u322-7.50.0.11][236],
  [7u332-7.52.0.11][237],
  [7u342-7.54.0.13][238],
  [7u352-7.56.0.11][239],
  
  * [6-latest][240],
  [6u49-6.4.0.6][241],
  [6u53-6.5.0.2][242],
  [6u56-6.6.0.1][243],
  [6u59-6.7.0.2][244],
  [6u63-6.8.0.1][245],
  [6u69-6.9.0.3][246],
  [6u73-6.10.0.3][247],
  [6u77-6.11.0.2][248],
  [6u79-6.12.0.2][249],
  [6u83-6.13.0.3][250],
  [6u87-6.14.0.1][251],
  [6u89-6.15.0.1][252],
  [6u93-6.16.0.1][253],
  [6u97-6.17.0.1][254],
  [6u99-6.18.0.3][255],
  [6u103-6.19.0.1][256],
  [6u107-6.20.0.1][257],
  [6u113-6.21.0.3][258],
  [6u119-6.22.0.3][259],
  

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


  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-jre-headless-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81-jre-headless/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11-jre-headless/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-headless-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre-headless/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre-headless/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre-headless/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre-headless/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-jre-headless/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-headless-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre-headless/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre-headless/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre-headless/Dockerfile
  
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-headless-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre-headless/Dockerfile
  
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-headless-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre-headless/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre-headless/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-headless-latest/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre-headless/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre-headless/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre-headless/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre-headless/Dockerfile
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-distroless-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-distroless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81-jre/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11-jre/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-jre/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre/Dockerfile
  
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-latest/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre/Dockerfile
  
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre/Dockerfile
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre/Dockerfile
  
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-latest/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13/Dockerfile
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17/Dockerfile
  
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13/Dockerfile
  
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15/Dockerfile
  
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14.1-11.54.25/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23/Dockerfile
  
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15/Dockerfile
  
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u342-7.54.0.13/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u352-7.56.0.11/Dockerfile
  
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  