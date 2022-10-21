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
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][55]
  * [`15.0.9-15.44.13`, `15-latest` (*15-latest/Dockerfile)*][62]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][81]
  * [`13.0.13-13.52.15`, `13-latest` (*13-latest/Dockerfile)*][84]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][106]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][110]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][140]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][143]
  * [`8u352-8.66.0.15`, `8-latest` (*8-latest/Dockerfile)*][148]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][200]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][238]

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
  
  * [17-jre-headless-latest][47],
  [17.0.0-17.28.13-jre-headless][48],
  [17.0.1-17.30.15-jre-headless][49],
  [17.0.2-17.32.13-jre-headless][50],
  [17.0.3-17.34.19-jre-headless][51],
  [17.0.4-17.36.13-jre-headless][52],
  [17.0.5-17.38.21-jre-headless][53],
  [17.0.4.1-17.36.17-jre-headless][54],
  
  * [15-jre-headless-latest][77],
  [15.0.7-15.40.19-jre-headless][78],
  [15.0.8-15.42.15-jre-headless][79],
  [15.0.9-15.44.13-jre-headless][80],
  
  * [13-jre-headless-latest][102],
  [13.0.11-13.48.19-jre-headless][103],
  [13.0.12-13.50.15-jre-headless][104],
  [13.0.13-13.52.15-jre-headless][105],
  
  * [11-jre-headless-latest][134],
  [11.0.15-11.56.19-jre-headless][136],
  [11.0.16-11.58.15-jre-headless][137],
  [11.0.17-11.60.19-jre-headless][138],
  [11.0.16.1-11.58.23-jre-headless][139],
  
  * [8-jre-headless-latest][195],
  [8u332-8.62.0.19-jre-headless][196],
  [8u342-8.64.0.15-jre-headless][197],
  [8u345-8.64.0.19-jre-headless][198],
  [8u352-8.66.0.15-jre-headless][199],
  
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
  [17.0.4.1-17.36.17-jre][46],
  
  * [16-jre-latest][56],
  [16.0.0-16.28.11-jre][59],
  [16.0.1-16.30.15-jre][60],
  [16.0.2-16.32.15-jre][61],
  
  * [15-jre-latest][63],
  [15.0.7-15.40.19-jre][74],
  [15.0.8-15.42.15-jre][75],
  [15.0.9-15.44.13-jre][76],
  
  * [13-jre-latest][87],
  [13.0.11-13.48.19-jre][99],
  [13.0.12-13.50.15-jre][100],
  [13.0.13-13.52.15-jre][101],
  
  * [11-jre-latest][117],
  [11.0.15-11.56.19-jre][131],
  [11.0.16-11.58.15-jre][132],
  [11.0.17-11.60.19-jre][133],
  [11.0.16.1-11.58.23-jre][135],
  
  * [8-jre-latest][149],
  [8u332-8.62.0.19-jre][191],
  [8u342-8.64.0.15-jre][192],
  [8u345-8.64.0.19-jre][193],
  [8u352-8.66.0.15-jre][194],
  
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
  
  * [16-latest][55],
  [16.0.0-16.28.11][57],
  [16.0.2-16.32.15][58],
  
  * [15-latest][62],
  [15.0.1-15.28.13][64],
  [15.0.1-15.28.51][65],
  [15.0.2-15.29.15][66],
  [15.0.3-15.32.15][67],
  [15.0.4-15.34.17][68],
  [15.0.5-15.36.13][69],
  [15.0.6-15.38.17][70],
  [15.0.7-15.40.19][71],
  [15.0.8-15.42.15][72],
  [15.0.9-15.44.13][73],
  
  * [14-latest][81],
  [14.0.1-14.28.21][82],
  [14.0.2-14.29.23][83],
  
  * [13-latest][84],
  [13.0.1-13.28][85],
  [13.0.2-13.29][86],
  [13.0.3-13.31.11][88],
  [13.0.4-13.33.25][89],
  [13.0.5-13.35.17][90],
  [13.0.6-13.37.21][91],
  [13.0.7-13.40.15][92],
  [13.0.8-13.42.17][93],
  [13.0.9-13.44.13][94],
  [13.0.10-13.46.15][95],
  [13.0.11-13.48.19][96],
  [13.0.12-13.50.15][97],
  [13.0.13-13.52.15][98],
  
  * [12-12.1][106],
  [12-latest][107],
  [12.0.1-12.2][108],
  [12.0.2-12.3][109],
  
  * [11-latest][110],
  [11.0.1-11.2][111],
  [11.0.2-11.29][112],
  [11.0.3-11.31][113],
  [11.0.4-11.33][114],
  [11.0.5-11.35][115],
  [11.0.6-11.37][116],
  [11.0.7-11.39.15][118],
  [11.0.8-11.41.23][119],
  [11.0.9-11.43.21][120],
  [11.0.10-11.45.27][121],
  [11.0.11-11.48.21][122],
  [11.0.12-11.50.19][123],
  [11.0.13-11.52.13][124],
  [11.0.14-11.54.23][125],
  [11.0.15-11.56.19][126],
  [11.0.16-11.58.15][127],
  [11.0.17-11.60.19][128],
  [11.0.14.1-11.54.25][129],
  [11.0.16.1-11.58.23][130],
  
  * [10-latest][140],
  [10u01-10.2][141],
  [10u02-10.3][142],
  
  * [9-ea][143],
  [9-latest][144],
  [9u01-9.0.1.3][145],
  [9u04-9.0.4.1][146],
  [9u07-9.0.7.1][147],
  
  * [8-latest][148],
  [8u05-8.1.0.6][150],
  [8u11-8.2.0.1][151],
  [8u20-8.3.0.1][152],
  [8u25-8.4.0.1][153],
  [8u31-8.5.0.1][154],
  [8u40-8.6.0.1][155],
  [8u45-8.7.0.5][156],
  [8u51-8.8.0.3][157],
  [8u60-8.9.0.4][158],
  [8u65-8.10.0.1][159],
  [8u66-8.11.0.1][160],
  [8u72-8.13.0.5][161],
  [8u92-8.15.0.1][162],
  [8u102-8.17.0.3][163],
  [8u112-8.19.0.1][164],
  [8u121-8.20.0.5][165],
  [8u131-8.21.0.1][166],
  [8u144-8.23.0.3][167],
  [8u152-8.25.0.1][168],
  [8u162-8.27.0.7][169],
  [8u172-8.30.0.1][170],
  [8u181-8.31.0.1][171],
  [8u192-8.33.0.1][172],
  [8u202-8.36.0.1][173],
  [8u212-8.38.0.13][174],
  [8u222-8.40.0.25][175],
  [8u232-8.42.0.21][176],
  [8u232-8.42.0.23][177],
  [8u242-8.44.0.11][178],
  [8u252-8.46.0.19][179],
  [8u262-8.48.0.51][180],
  [8u272-8.50.0.21][181],
  [8u275-8.50.0.53][182],
  [8u282-8.52.0.23][183],
  [8u302-8.56.0.21][184],
  [8u312-8.58.0.13][185],
  [8u322-8.60.0.21][186],
  [8u332-8.62.0.19][187],
  [8u342-8.64.0.15][188],
  [8u345-8.64.0.19][189],
  [8u352-8.66.0.15][190],
  
  * [7-latest][200],
  [7u55-7.4.0.5][201],
  [7u60-7.5.0.1][202],
  [7u65-7.6.0.1][203],
  [7u72-7.7.0.1][204],
  [7u76-7.8.0.3][205],
  [7u79-7.9.0.2][206],
  [7u80-7.10.0.1][207],
  [7u85-7.11.0.3][208],
  [7u91-7.12.0.3][209],
  [7u95-7.13.0.1][210],
  [7u101-7.14.0.5][211],
  [7u111-7.15.0.1][212],
  [7u121-7.16.0.1][213],
  [7u131-7.17.0.5][214],
  [7u141-7.18.0.3][215],
  [7u154-7.20.0.3][216],
  [7u161-7.21.0.3][217],
  [7u171-7.22.0.3][218],
  [7u181-7.23.0.1][219],
  [7u191-7.24.0.1][220],
  [7u201-7.25.0.5][221],
  [7u211-7.27.0.1][222],
  [7u222-7.29.0.5][223],
  [7u232-7.31.0.5][224],
  [7u242-7.34.0.5][225],
  [7u252-7.36.0.5][226],
  [7u262-7.38.0.11][227],
  [7u272-7.40.0.15][228],
  [7u282-7.42.0.13][229],
  [7u285-7.42.0.51][230],
  [7u292-7.44.0.11][231],
  [7u302-7.46.0.11][232],
  [7u312-7.48.0.11][233],
  [7u322-7.50.0.11][234],
  [7u332-7.52.0.11][235],
  [7u342-7.54.0.13][236],
  [7u352-7.56.0.11][237],
  
  * [6-latest][238],
  [6u49-6.4.0.6][239],
  [6u53-6.5.0.2][240],
  [6u56-6.6.0.1][241],
  [6u59-6.7.0.2][242],
  [6u63-6.8.0.1][243],
  [6u69-6.9.0.3][244],
  [6u73-6.10.0.3][245],
  [6u77-6.11.0.2][246],
  [6u79-6.12.0.2][247],
  [6u83-6.13.0.3][248],
  [6u87-6.14.0.1][249],
  [6u89-6.15.0.1][250],
  [6u93-6.16.0.1][251],
  [6u97-6.17.0.1][252],
  [6u99-6.18.0.3][253],
  [6u103-6.19.0.1][254],
  [6u107-6.20.0.1][255],
  [6u113-6.21.0.3][256],
  [6u119-6.22.0.3][257],
  

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
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre-headless/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre-headless/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-jre-headless/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-headless-latest/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre-headless/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre-headless/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre-headless/Dockerfile
  
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-headless-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre-headless/Dockerfile
  
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-headless-latest/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre-headless/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre-headless/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-headless-latest/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre-headless/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre-headless/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre-headless/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre-headless/Dockerfile
  
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
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre/Dockerfile
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-latest/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre/Dockerfile
  
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-latest/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre/Dockerfile
  
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre/Dockerfile
  
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-latest/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre/Dockerfile
  
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
  
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13/Dockerfile
  
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15/Dockerfile
  
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14.1-11.54.25/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23/Dockerfile
  
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15/Dockerfile
  
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u342-7.54.0.13/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u352-7.56.0.11/Dockerfile
  
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  