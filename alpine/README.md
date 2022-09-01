Alpine-Native Azul Zulu Images
=================================
The `zulu-openjdk-alpine` image includes Alpine-native Azul Zulu builds of OpenJDK, which use the built-in musl libc functionality and do not add glibc on top of the Alpine distribution.


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
  * [`17.0.4.1-17.36.19`, `17-latest` (*17-latest/Dockerfile)*][22]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][49]
  * [`15.0.8-15.42.15`, `15-latest` (*15-latest/Dockerfile)*][57]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][75]
  * [`13.0.12-13.50.15`, `13-latest` (*13-latest/Dockerfile)*][78]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][113]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][117]
  * [`8u345-8.64.0.19`, `8-latest` (*8-latest/Dockerfile)*][167]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][225]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][248]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu:


  * [18-jre-headless-latest][18],
  [18.0.1-18.30.11-jre-headless][19],
  [18.0.2-18.32.11-jre-headless][20],
  [18.0.2.1-18.32.13-jre-headless][21],
  
  * [17-jre-headless-latest][40],
  [17.0.0-17.28.13-jre-headless][41],
  [17.0.1-17.30.15-jre-headless][42],
  [17.0.2-17.32.13-jre-headless][43],
  [17.0.3-17.34.19-jre-headless][44],
  [17.0.4-17.36.13-jre-headless][45],
  [17.0.4-17.36.15-jre-headless][46],
  [17.0.4.1-17.36.17-jre-headless][47],
  [17.0.4.1-17.36.19-jre-headless][48],
  
  * [15-jre-headless-latest][72],
  [15.0.7-15.40.19-jre-headless][73],
  [15.0.8-15.42.15-jre-headless][74],
  
  * [13-jre-headless-latest][102],
  [13.0.3-13.31.11-jre-headless][103],
  [13.0.4-13.33.25-jre-headless][104],
  [13.0.5-13.35.17-jre-headless][105],
  [13.0.6-13.37.21-jre-headless][106],
  [13.0.7-13.40.15-jre-headless][107],
  [13.0.8-13.42.17-jre-headless][108],
  [13.0.9-13.44.13-jre-headless][109],
  [13.0.10-13.46.15-jre-headless][110],
  [13.0.11-13.48.19-jre-headless][111],
  [13.0.12-13.50.15-jre-headless][112],
  
  * [11-jre-headless-latest][151],
  [11.0.5-11.35-jre-headless][154],
  [11.0.6-11.37-jre-headless][155],
  [11.0.7-11.39.15-jre-headless][156],
  [11.0.8-11.41.23-jre-headless][157],
  [11.0.9-11.43.21-jre-headless][158],
  [11.0.10-11.45.27-jre-headless][159],
  [11.0.12-11.50.19-jre-headless][160],
  [11.0.13-11.52.13-jre-headless][161],
  [11.0.14-11.54.23-jre-headless][162],
  [11.0.15-11.56.19-jre-headless][163],
  [11.0.16-11.58.15-jre-headless][164],
  [11.0.14.1-11.54.25-jre-headless][165],
  [11.0.16.1-11.58.23-jre-headless][166],
  
  * [8-jre-headless-latest][211],
  [8u232-8.42.0.23-jre-headless][212],
  [8u242-8.44.0.11-jre-headless][213],
  [8u252-8.46.0.19-jre-headless][214],
  [8u262-8.48.0.51-jre-headless][215],
  [8u272-8.50.0.21-jre-headless][216],
  [8u275-8.50.0.51-jre-headless][217],
  [8u282-8.52.0.23-jre-headless][218],
  [8u302-8.56.0.21-jre-headless][219],
  [8u312-8.58.0.13-jre-headless][220],
  [8u322-8.60.0.21-jre-headless][221],
  [8u332-8.62.0.19-jre-headless][222],
  [8u342-8.64.0.15-jre-headless][223],
  [8u345-8.64.0.19-jre-headless][224],
  
  * [18-jre-latest][11],
  [18.0.1-18.30.11-jre][15],
  [18.0.2-18.32.11-jre][16],
  [18.0.2.1-18.32.13-jre][17],
  
  * [17-jre-latest][23],
  [17.0.0-17.28.13-jre][32],
  [17.0.1-17.30.15-jre][33],
  [17.0.2-17.32.13-jre][34],
  [17.0.3-17.34.19-jre][35],
  [17.0.4-17.36.13-jre][36],
  [17.0.4-17.36.15-jre][37],
  [17.0.4.1-17.36.17-jre][38],
  [17.0.4.1-17.36.19-jre][39],
  
  * [16-jre-latest][50],
  [16.0.0-16.28.11-jre][54],
  [16.0.1-16.30.15-jre][55],
  [16.0.2-16.32.15-jre][56],
  
  * [15-jre-latest][58],
  [15.0.0-15.27.17-jre][69],
  [15.0.7-15.40.19-jre][70],
  [15.0.8-15.42.15-jre][71],
  
  * [13-jre-latest][81],
  [13.0.3-13.31.11-jre][92],
  [13.0.4-13.33.25-jre][93],
  [13.0.5-13.35.17-jre][94],
  [13.0.6-13.37.21-jre][95],
  [13.0.7-13.40.15-jre][96],
  [13.0.8-13.42.17-jre][97],
  [13.0.9-13.44.13-jre][98],
  [13.0.10-13.46.15-jre][99],
  [13.0.11-13.48.19-jre][100],
  [13.0.12-13.50.15-jre][101],
  
  * [11-jre-latest][124],
  [11.0.3-11.31-jre][135],
  [11.0.4-11.33-jre][136],
  [11.0.5-11.35-jre][137],
  [11.0.6-11.37-jre][138],
  [11.0.7-11.39.15-jre][141],
  [11.0.8-11.41.23-jre][142],
  [11.0.9-11.43.21-jre][143],
  [11.0.10-11.45.27-jre][144],
  [11.0.11-11.48.21-jre][145],
  [11.0.12-11.50.19-jre][146],
  [11.0.13-11.52.13-jre][147],
  [11.0.14-11.54.23-jre][148],
  [11.0.15-11.56.19-jre][149],
  [11.0.16-11.58.15-jre][150],
  [11.0.14.1-11.54.25-jre][152],
  [11.0.16.1-11.58.23-jre][153],
  
  * [8-jre-latest][168],
  [8u212-8.38.0.13-jre][194],
  [8u222-8.40.0.25-jre][195],
  [8u232-8.42.0.21-jre][196],
  [8u232-8.42.0.23-jre][197],
  [8u242-8.44.0.11-jre][198],
  [8u252-8.46.0.19-jre][199],
  [8u262-8.48.0.51-jre][200],
  [8u272-8.50.0.21-jre][201],
  [8u275-8.50.0.51-jre][202],
  [8u282-8.52.0.23-jre][203],
  [8u292-8.54.0.21-jre][204],
  [8u302-8.56.0.21-jre][205],
  [8u312-8.58.0.13-jre][206],
  [8u322-8.60.0.21-jre][207],
  [8u332-8.62.0.19-jre][208],
  [8u342-8.64.0.15-jre][209],
  [8u345-8.64.0.19-jre][210],
  
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
  [17.0.4-17.36.15][29],
  [17.0.4.1-17.36.17][30],
  [17.0.4.1-17.36.19][31],
  
  * [16-latest][49],
  [16.0.0-16.28.11][51],
  [16.0.1-16.30.15][52],
  [16.0.2-16.32.15][53],
  
  * [15-latest][57],
  [15.0.0-15.27.17][59],
  [15.0.1-15.28.13][60],
  [15.0.1-15.28.51][61],
  [15.0.2-15.29.15][62],
  [15.0.3-15.32.15][63],
  [15.0.4-15.34.17][64],
  [15.0.5-15.36.13][65],
  [15.0.6-15.38.17][66],
  [15.0.7-15.40.19][67],
  [15.0.8-15.42.15][68],
  
  * [14-latest][75],
  [14.0.1-14.28.21][76],
  [14.0.2-14.29.23][77],
  
  * [13-latest][78],
  [13.0.1-13.28][79],
  [13.0.2-13.29][80],
  [13.0.3-13.31.11][82],
  [13.0.4-13.33.25][83],
  [13.0.5-13.35.17][84],
  [13.0.6-13.37.21][85],
  [13.0.7-13.40.15][86],
  [13.0.8-13.42.17][87],
  [13.0.9-13.44.13][88],
  [13.0.10-13.46.15][89],
  [13.0.11-13.48.19][90],
  [13.0.12-13.50.15][91],
  
  * [12-latest][113],
  [12.0.0-12.1][114],
  [12.0.1-12.2][115],
  [12.0.2-12.3][116],
  
  * [11-latest][117],
  [11.0.1-11.2][118],
  [11.0.2-11.29][119],
  [11.0.3-11.31][120],
  [11.0.4-11.33][121],
  [11.0.5-11.35][122],
  [11.0.6-11.37][123],
  [11.0.7-11.39.15][125],
  [11.0.8-11.41.23][126],
  [11.0.9-11.43.21][127],
  [11.0.10-11.45.27][128],
  [11.0.11-11.48.21][129],
  [11.0.12-11.50.19][130],
  [11.0.13-11.52.13][131],
  [11.0.14-11.54.23][132],
  [11.0.15-11.56.19][133],
  [11.0.16-11.58.15][134],
  [11.0.14.1-11.54.25][139],
  [11.0.16.1-11.58.23][140],
  
  * [8-latest][167],
  [8u131-8.21.0.1][169],
  [8u144-8.23.0.3][170],
  [8u152-8.25.0.1][171],
  [8u162-8.27.0.7][172],
  [8u172-8.30.0.1][173],
  [8u181-8.31.0.1][174],
  [8u192-8.33.0.1][175],
  [8u202-8.36.0.3][176],
  [8u212-8.38.0.13][177],
  [8u222-8.40.0.25][178],
  [8u232-8.42.0.21][179],
  [8u232-8.42.0.23][180],
  [8u242-8.44.0.11][181],
  [8u252-8.46.0.19][182],
  [8u262-8.48.0.51][183],
  [8u272-8.50.0.21][184],
  [8u275-8.50.0.51][185],
  [8u282-8.52.0.23][186],
  [8u292-8.54.0.21][187],
  [8u302-8.56.0.21][188],
  [8u312-8.58.0.13][189],
  [8u322-8.60.0.21][190],
  [8u332-8.62.0.19][191],
  [8u342-8.64.0.15][192],
  [8u345-8.64.0.19][193],
  
  * [7-latest][225],
  [7u141-7.18.0.3][226],
  [7u154-7.20.0.3][227],
  [7u161-7.21.0.3][228],
  [7u171-7.22.0.3][229],
  [7u181-7.23.0.1][230],
  [7u191-7.24.0.1][231],
  [7u201-7.25.0.5][232],
  [7u211-7.27.0.1][233],
  [7u222-7.29.0.5][234],
  [7u232-7.31.0.5][235],
  [7u242-7.34.0.5][236],
  [7u252-7.36.0.5][237],
  [7u262-7.38.0.11][238],
  [7u272-7.40.0.15][239],
  [7u282-7.42.0.13][240],
  [7u285-7.42.0.51][241],
  [7u292-7.44.0.11][242],
  [7u302-7.46.0.11][243],
  [7u312-7.48.0.11][244],
  [7u332-7.52.0.11][245],
  [7u342-7.54.0.13][246],
  [7u352-7.56.0.11][247],
  
  * [6-latest][248],
  [6u93-6.16.0.1][249],
  [6u97-6.17.0.1][250],
  [6u99-6.18.0.3][251],
  [6u103-6.19.0.1][252],
  [6u107-6.20.0.1][253],
  [6u113-6.21.0.3][254],
  [6u119-6.22.0.3][255],
  

**Note**: Some of these may use glibc and predate the move to musl libc.

Usage
=====

This Azul Zulu repository supports numerous versions of OpenJDK-based Java SE JDKs. Versions 7-17 of Azul Zulu are compliant with Java 7-17 respectively.

To run a container of your choice, use the command below as an example.

To start Azul Zulu 11 in a container, enter:

    docker run -it --rm azul/zulu-openjdk-alpine:11 java -version

  [1]: https://www.azul.com/files/ZuluDocker60.gif
  [2]: https://www.azul.com/
  [3]: https://www.azul.com/products/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [7]: https://hub.docker.com/r/azul/zulu-openjdk


  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre-headless/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre-headless/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre-headless/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.15-jre-headless/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.19-jre-headless/Dockerfile
  
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre-headless/Dockerfile
  
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre-headless/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre-headless/Dockerfile
  
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre-headless/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre-headless/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre-headless/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre-headless/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre-headless/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.15-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.19-jre/Dockerfile
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre/Dockerfile
  
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre/Dockerfile
  
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre/Dockerfile
  
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.15/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.19/Dockerfile
  
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15/Dockerfile
  
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15/Dockerfile
  
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23/Dockerfile
  
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19/Dockerfile
  
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u342-7.54.0.13/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u352-7.56.0.11/Dockerfile
  
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  