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

  * [`17.0.2-17.32.13`, `17-latest` (*17-latest/Dockerfile)*][10]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][22]
  * [`15.0.6-15.38.17`, `15-latest` (*15-latest/Dockerfile)*][30]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][40]
  * [`13.0.10-13.46.15`, `13-latest` (*13-latest/Dockerfile)*][43]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][72]
  * [`11.0.14-11.54.23`, `11-latest` (*11-latest/Dockerfile)*][76]
  * [`8u322-8.60.0.21`, `8-latest` (*8-latest/Dockerfile)*][114]
  * [`7u332-7.52.0.11`, `7-latest` (*7-latest/Dockerfile)*][163]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][185]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu:


  * [17-jre-headless-latest][18],
  [17.0.0-17.28.13-jre-headless][19],
  [17.0.1-17.30.15-jre-headless][20],
  [17.0.2-17.32.13-jre-headless][21],
  
  * [13-jre-headless-latest][63],
  [13.0.3-13.31.11-jre-headless][64],
  [13.0.4-13.33.25-jre-headless][65],
  [13.0.5-13.35.17-jre-headless][66],
  [13.0.6-13.37.21-jre-headless][67],
  [13.0.7-13.40.15-jre-headless][68],
  [13.0.8-13.42.17-jre-headless][69],
  [13.0.9-13.44.13-jre-headless][70],
  [13.0.10-13.46.15-jre-headless][71],
  
  * [11-jre-headless-latest][104],
  [11.0.5-11.35-jre-headless][105],
  [11.0.6-11.37-jre-headless][106],
  [11.0.7-11.39.15-jre-headless][107],
  [11.0.8-11.41.23-jre-headless][108],
  [11.0.9-11.43.21-jre-headless][109],
  [11.0.10-11.45.27-jre-headless][110],
  [11.0.12-11.50.19-jre-headless][111],
  [11.0.13-11.52.13-jre-headless][112],
  [11.0.14-11.54.23-jre-headless][113],
  
  * [8-jre-headless-latest][152],
  [8u232-8.42.0.23-jre-headless][153],
  [8u242-8.44.0.11-jre-headless][154],
  [8u252-8.46.0.19-jre-headless][155],
  [8u262-8.48.0.51-jre-headless][156],
  [8u272-8.50.0.21-jre-headless][157],
  [8u275-8.50.0.51-jre-headless][158],
  [8u282-8.52.0.23-jre-headless][159],
  [8u302-8.56.0.21-jre-headless][160],
  [8u312-8.58.0.13-jre-headless][161],
  [8u322-8.60.0.21-jre-headless][162],
  
  * [17-jre-latest][11],
  [17.0.0-17.28.13-jre][15],
  [17.0.1-17.30.15-jre][16],
  [17.0.2-17.32.13-jre][17],
  
  * [16-jre-latest][23],
  [16.0.0-16.28.11-jre][27],
  [16.0.1-16.30.15-jre][28],
  [16.0.2-16.32.15-jre][29],
  
  * [13-jre-latest][46],
  [13.0.3-13.31.11-jre][55],
  [13.0.4-13.33.25-jre][56],
  [13.0.5-13.35.17-jre][57],
  [13.0.6-13.37.21-jre][58],
  [13.0.7-13.40.15-jre][59],
  [13.0.8-13.42.17-jre][60],
  [13.0.9-13.44.13-jre][61],
  [13.0.10-13.46.15-jre][62],
  
  * [11-jre-latest][83],
  [11.0.3-11.31-jre][92],
  [11.0.4-11.33-jre][93],
  [11.0.5-11.35-jre][94],
  [11.0.6-11.37-jre][95],
  [11.0.7-11.39.15-jre][96],
  [11.0.8-11.41.23-jre][97],
  [11.0.9-11.43.21-jre][98],
  [11.0.10-11.45.27-jre][99],
  [11.0.11-11.48.21-jre][100],
  [11.0.12-11.50.19-jre][101],
  [11.0.13-11.52.13-jre][102],
  [11.0.14-11.54.23-jre][103],
  
  * [8-jre-latest][115],
  [8u212-8.38.0.13-jre][138],
  [8u222-8.40.0.25-jre][139],
  [8u232-8.42.0.21-jre][140],
  [8u232-8.42.0.23-jre][141],
  [8u242-8.44.0.11-jre][142],
  [8u252-8.46.0.19-jre][143],
  [8u262-8.48.0.51-jre][144],
  [8u272-8.50.0.21-jre][145],
  [8u275-8.50.0.51-jre][146],
  [8u282-8.52.0.23-jre][147],
  [8u292-8.54.0.21-jre][148],
  [8u302-8.56.0.21-jre][149],
  [8u312-8.58.0.13-jre][150],
  [8u322-8.60.0.21-jre][151],
  
  * [17-latest][10],
  [17.0.0-17.28.13][12],
  [17.0.1-17.30.15][13],
  [17.0.2-17.32.13][14],
  
  * [16-latest][22],
  [16.0.0-16.28.11][24],
  [16.0.1-16.30.15][25],
  [16.0.2-16.32.15][26],
  
  * [15-latest][30],
  [15.0.0-15.27.17][31],
  [15.0.1-15.28.13][32],
  [15.0.1-15.28.51][33],
  [15.0.2-15.29.15][34],
  [15.0.3-15.32.15][35],
  [15.0.4-15.34.17][36],
  [15.0.5-15.36.13][37],
  [15.0.6-15.38.17][38],
  
  * [14-latest][40],
  [14.0.1-14.28.21][41],
  [14.0.2-14.29.23][42],
  
  * [13-latest][43],
  [13.0.1-13.28][44],
  [13.0.2-13.29][45],
  [13.0.3-13.31.11][47],
  [13.0.4-13.33.25][48],
  [13.0.5-13.35.17][49],
  [13.0.6-13.37.21][50],
  [13.0.7-13.40.15][51],
  [13.0.8-13.42.17][52],
  [13.0.9-13.44.13][53],
  [13.0.10-13.46.15][54],
  
  * [12-latest][72],
  [12.0.0-12.1][73],
  [12.0.1-12.2][74],
  [12.0.2-12.3][75],
  
  * [11-latest][76],
  [11.0.1-11.2][77],
  [11.0.2-11.29][78],
  [11.0.3-11.31][79],
  [11.0.4-11.33][80],
  [11.0.5-11.35][81],
  [11.0.6-11.37][82],
  [11.0.7-11.39.15][84],
  [11.0.8-11.41.23][85],
  [11.0.9-11.43.21][86],
  [11.0.10-11.45.27][87],
  [11.0.11-11.48.21][88],
  [11.0.12-11.50.19][89],
  [11.0.13-11.52.13][90],
  [11.0.14-11.54.23][91],
  
  * [8-latest][114],
  [8u131-8.21.0.1][116],
  [8u144-8.23.0.3][117],
  [8u152-8.25.0.1][118],
  [8u162-8.27.0.7][119],
  [8u172-8.30.0.1][120],
  [8u181-8.31.0.1][121],
  [8u192-8.33.0.1][122],
  [8u202-8.36.0.3][123],
  [8u212-8.38.0.13][124],
  [8u222-8.40.0.25][125],
  [8u232-8.42.0.21][126],
  [8u232-8.42.0.23][127],
  [8u242-8.44.0.11][128],
  [8u252-8.46.0.19][129],
  [8u262-8.48.0.51][130],
  [8u272-8.50.0.21][131],
  [8u275-8.50.0.51][132],
  [8u282-8.52.0.23][133],
  [8u292-8.54.0.21][134],
  [8u302-8.56.0.21][135],
  [8u312-8.58.0.13][136],
  [8u322-8.60.0.21][137],
  
  * [7-latest][163],
  [7u141-7.18.0.3][164],
  [7u154-7.20.0.3][165],
  [7u161-7.21.0.3][166],
  [7u171-7.22.0.3][167],
  [7u181-7.23.0.1][168],
  [7u191-7.24.0.1][169],
  [7u201-7.25.0.5][170],
  [7u211-7.27.0.1][171],
  [7u222-7.29.0.5][172],
  [7u232-7.31.0.5][173],
  [7u242-7.34.0.5][174],
  [7u252-7.36.0.5][175],
  [7u262-7.38.0.11][176],
  [7u272-7.40.0.15][177],
  [7u282-7.42.0.13][178],
  [7u285-7.42.0.51][179],
  [7u292-7.44.0.11][180],
  [7u302-7.46.0.11][181],
  [7u312-7.48.0.11][182],
  [7u322-7.50.0.11][183],
  [7u332-7.52.0.11][184],
  
  * [6-latest][185],
  [6u93-6.16.0.1][186],
  [6u97-6.17.0.1][187],
  [6u99-6.18.0.3][188],
  [6u103-6.19.0.1][189],
  [6u107-6.20.0.1][190],
  [6u113-6.21.0.3][191],
  [6u119-6.22.0.3][192],
  

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


  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u322-7.50.0.11/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  