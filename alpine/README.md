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

  * [`17.0.3-17.34.19`, `17-latest` (*17-latest/Dockerfile)*][10]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][25]
  * [`15.0.7-15.40.19`, `15-latest` (*15-latest/Dockerfile)*][33]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][44]
  * [`13.0.11-13.48.19`, `13-latest` (*13-latest/Dockerfile)*][47]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][79]
  * [`11.0.14.1-11.54.25`, `11-latest` (*11-latest/Dockerfile)*][83]
  * [`8u332-8.62.0.19`, `8-latest` (*8-latest/Dockerfile)*][127]
  * [`7u342-7.54.0.13`, `7-latest` (*7-latest/Dockerfile)*][179]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][201]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu:


  * [17-jre-headless-latest][20],
  [17.0.0-17.28.13-jre-headless][21],
  [17.0.1-17.30.15-jre-headless][22],
  [17.0.2-17.32.13-jre-headless][23],
  [17.0.3-17.34.19-jre-headless][24],
  
  * [13-jre-headless-latest][69],
  [13.0.3-13.31.11-jre-headless][70],
  [13.0.4-13.33.25-jre-headless][71],
  [13.0.5-13.35.17-jre-headless][72],
  [13.0.6-13.37.21-jre-headless][73],
  [13.0.7-13.40.15-jre-headless][74],
  [13.0.8-13.42.17-jre-headless][75],
  [13.0.9-13.44.13-jre-headless][76],
  [13.0.10-13.46.15-jre-headless][77],
  [13.0.11-13.48.19-jre-headless][78],
  
  * [11-jre-headless-latest][114],
  [11.0.5-11.35-jre-headless][116],
  [11.0.6-11.37-jre-headless][117],
  [11.0.7-11.39.15-jre-headless][118],
  [11.0.8-11.41.23-jre-headless][119],
  [11.0.9-11.43.21-jre-headless][120],
  [11.0.10-11.45.27-jre-headless][121],
  [11.0.12-11.50.19-jre-headless][122],
  [11.0.13-11.52.13-jre-headless][123],
  [11.0.14-11.54.23-jre-headless][124],
  [11.0.15-11.56.19-jre-headless][125],
  [11.0.14.1-11.54.25-jre-headless][126],
  
  * [8-jre-headless-latest][167],
  [8u232-8.42.0.23-jre-headless][168],
  [8u242-8.44.0.11-jre-headless][169],
  [8u252-8.46.0.19-jre-headless][170],
  [8u262-8.48.0.51-jre-headless][171],
  [8u272-8.50.0.21-jre-headless][172],
  [8u275-8.50.0.51-jre-headless][173],
  [8u282-8.52.0.23-jre-headless][174],
  [8u302-8.56.0.21-jre-headless][175],
  [8u312-8.58.0.13-jre-headless][176],
  [8u322-8.60.0.21-jre-headless][177],
  [8u332-8.62.0.19-jre-headless][178],
  
  * [17-jre-latest][11],
  [17.0.0-17.28.13-jre][16],
  [17.0.1-17.30.15-jre][17],
  [17.0.2-17.32.13-jre][18],
  [17.0.3-17.34.19-jre][19],
  
  * [16-jre-latest][26],
  [16.0.0-16.28.11-jre][30],
  [16.0.1-16.30.15-jre][31],
  [16.0.2-16.32.15-jre][32],
  
  * [13-jre-latest][50],
  [13.0.3-13.31.11-jre][60],
  [13.0.4-13.33.25-jre][61],
  [13.0.5-13.35.17-jre][62],
  [13.0.6-13.37.21-jre][63],
  [13.0.7-13.40.15-jre][64],
  [13.0.8-13.42.17-jre][65],
  [13.0.9-13.44.13-jre][66],
  [13.0.10-13.46.15-jre][67],
  [13.0.11-13.48.19-jre][68],
  
  * [11-jre-latest][90],
  [11.0.3-11.31-jre][100],
  [11.0.4-11.33-jre][101],
  [11.0.5-11.35-jre][102],
  [11.0.6-11.37-jre][103],
  [11.0.7-11.39.15-jre][105],
  [11.0.8-11.41.23-jre][106],
  [11.0.9-11.43.21-jre][107],
  [11.0.10-11.45.27-jre][108],
  [11.0.11-11.48.21-jre][109],
  [11.0.12-11.50.19-jre][110],
  [11.0.13-11.52.13-jre][111],
  [11.0.14-11.54.23-jre][112],
  [11.0.15-11.56.19-jre][113],
  [11.0.14.1-11.54.25-jre][115],
  
  * [8-jre-latest][128],
  [8u212-8.38.0.13-jre][152],
  [8u222-8.40.0.25-jre][153],
  [8u232-8.42.0.21-jre][154],
  [8u232-8.42.0.23-jre][155],
  [8u242-8.44.0.11-jre][156],
  [8u252-8.46.0.19-jre][157],
  [8u262-8.48.0.51-jre][158],
  [8u272-8.50.0.21-jre][159],
  [8u275-8.50.0.51-jre][160],
  [8u282-8.52.0.23-jre][161],
  [8u292-8.54.0.21-jre][162],
  [8u302-8.56.0.21-jre][163],
  [8u312-8.58.0.13-jre][164],
  [8u322-8.60.0.21-jre][165],
  [8u332-8.62.0.19-jre][166],
  
  * [17-latest][10],
  [17.0.0-17.28.13][12],
  [17.0.1-17.30.15][13],
  [17.0.2-17.32.13][14],
  [17.0.3-17.34.19][15],
  
  * [16-latest][25],
  [16.0.0-16.28.11][27],
  [16.0.1-16.30.15][28],
  [16.0.2-16.32.15][29],
  
  * [15-latest][33],
  [15.0.0-15.27.17][34],
  [15.0.1-15.28.13][35],
  [15.0.1-15.28.51][36],
  [15.0.2-15.29.15][37],
  [15.0.3-15.32.15][38],
  [15.0.4-15.34.17][39],
  [15.0.5-15.36.13][40],
  [15.0.6-15.38.17][41],
  [15.0.7-15.40.19][42],
  
  * [14-latest][44],
  [14.0.1-14.28.21][45],
  [14.0.2-14.29.23][46],
  
  * [13-latest][47],
  [13.0.1-13.28][48],
  [13.0.2-13.29][49],
  [13.0.3-13.31.11][51],
  [13.0.4-13.33.25][52],
  [13.0.5-13.35.17][53],
  [13.0.6-13.37.21][54],
  [13.0.7-13.40.15][55],
  [13.0.8-13.42.17][56],
  [13.0.9-13.44.13][57],
  [13.0.10-13.46.15][58],
  [13.0.11-13.48.19][59],
  
  * [12-latest][79],
  [12.0.0-12.1][80],
  [12.0.1-12.2][81],
  [12.0.2-12.3][82],
  
  * [11-latest][83],
  [11.0.1-11.2][84],
  [11.0.2-11.29][85],
  [11.0.3-11.31][86],
  [11.0.4-11.33][87],
  [11.0.5-11.35][88],
  [11.0.6-11.37][89],
  [11.0.7-11.39.15][91],
  [11.0.8-11.41.23][92],
  [11.0.9-11.43.21][93],
  [11.0.10-11.45.27][94],
  [11.0.11-11.48.21][95],
  [11.0.12-11.50.19][96],
  [11.0.13-11.52.13][97],
  [11.0.14-11.54.23][98],
  [11.0.15-11.56.19][99],
  [11.0.14.1-11.54.25][104],
  
  * [8-latest][127],
  [8u131-8.21.0.1][129],
  [8u144-8.23.0.3][130],
  [8u152-8.25.0.1][131],
  [8u162-8.27.0.7][132],
  [8u172-8.30.0.1][133],
  [8u181-8.31.0.1][134],
  [8u192-8.33.0.1][135],
  [8u202-8.36.0.3][136],
  [8u212-8.38.0.13][137],
  [8u222-8.40.0.25][138],
  [8u232-8.42.0.21][139],
  [8u232-8.42.0.23][140],
  [8u242-8.44.0.11][141],
  [8u252-8.46.0.19][142],
  [8u262-8.48.0.51][143],
  [8u272-8.50.0.21][144],
  [8u275-8.50.0.51][145],
  [8u282-8.52.0.23][146],
  [8u292-8.54.0.21][147],
  [8u302-8.56.0.21][148],
  [8u312-8.58.0.13][149],
  [8u322-8.60.0.21][150],
  [8u332-8.62.0.19][151],
  
  * [7-latest][179],
  [7u141-7.18.0.3][180],
  [7u154-7.20.0.3][181],
  [7u161-7.21.0.3][182],
  [7u171-7.22.0.3][183],
  [7u181-7.23.0.1][184],
  [7u191-7.24.0.1][185],
  [7u201-7.25.0.5][186],
  [7u211-7.27.0.1][187],
  [7u222-7.29.0.5][188],
  [7u232-7.31.0.5][189],
  [7u242-7.34.0.5][190],
  [7u252-7.36.0.5][191],
  [7u262-7.38.0.11][192],
  [7u272-7.40.0.15][193],
  [7u282-7.42.0.13][194],
  [7u285-7.42.0.51][195],
  [7u292-7.44.0.11][196],
  [7u302-7.46.0.11][197],
  [7u312-7.48.0.11][198],
  [7u332-7.52.0.11][199],
  [7u342-7.54.0.13][200],
  
  * [6-latest][201],
  [6u93-6.16.0.1][202],
  [6u97-6.17.0.1][203],
  [6u99-6.18.0.3][204],
  [6u103-6.19.0.1][205],
  [6u107-6.20.0.1][206],
  [6u113-6.21.0.3][207],
  [6u119-6.22.0.3][208],
  

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


  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre-headless/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre-headless/Dockerfile
  
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre-headless/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre-headless/Dockerfile
  
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre/Dockerfile
  
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19/Dockerfile
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19/Dockerfile
  
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25/Dockerfile
  
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19/Dockerfile
  
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u342-7.54.0.13/Dockerfile
  
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  