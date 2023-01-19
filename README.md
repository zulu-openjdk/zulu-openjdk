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

  * [`19.0.2-19.32.13`, `19-latest` (*19-latest/Dockerfile)*][10]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][22]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][34]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][63]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][70]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][92]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][95]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][120]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][124]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][157]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][160]
  * [`8u362-8.68.0.19`, `8-latest` (*8-latest/Dockerfile)*][165]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][220]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][258]

Previous
--------
Earlier created Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK 6-16 are as follows:

  * [19-jre-headless-latest][18],
  [19.0.0-19.28.81-jre-headless][19],
  [19.0.1-19.30.11-jre-headless][20],
  [19.0.2-19.32.13-jre-headless][21],
  
  * [18-jre-headless-latest][30],
  [18.0.1-18.30.11-jre-headless][31],
  [18.0.2-18.32.11-jre-headless][32],
  [18.0.2.1-18.32.13-jre-headless][33],
  
  * [17-jre-headless-latest][53],
  [17.0.0-17.28.13-jre-headless][55],
  [17.0.1-17.30.15-jre-headless][56],
  [17.0.2-17.32.13-jre-headless][57],
  [17.0.3-17.34.19-jre-headless][58],
  [17.0.4-17.36.13-jre-headless][59],
  [17.0.5-17.38.21-jre-headless][60],
  [17.0.6-17.40.19-jre-headless][61],
  [17.0.4.1-17.36.17-jre-headless][62],
  
  * [15-jre-headless-latest][87],
  [15.0.7-15.40.19-jre-headless][88],
  [15.0.8-15.42.15-jre-headless][89],
  [15.0.9-15.44.13-jre-headless][90],
  [15.0.10-15.46.17-jre-headless][91],
  
  * [13-jre-headless-latest][115],
  [13.0.11-13.48.19-jre-headless][116],
  [13.0.12-13.50.15-jre-headless][117],
  [13.0.13-13.52.15-jre-headless][118],
  [13.0.14-13.54.17-jre-headless][119],
  
  * [11-jre-headless-latest][150],
  [11.0.15-11.56.19-jre-headless][152],
  [11.0.16-11.58.15-jre-headless][153],
  [11.0.17-11.60.19-jre-headless][154],
  [11.0.18-11.62.17-jre-headless][155],
  [11.0.16.1-11.58.23-jre-headless][156],
  
  * [8-jre-headless-latest][214],
  [8u332-8.62.0.19-jre-headless][215],
  [8u342-8.64.0.15-jre-headless][216],
  [8u345-8.64.0.19-jre-headless][217],
  [8u352-8.66.0.15-jre-headless][218],
  [8u362-8.68.0.19-jre-headless][219],
  
  * [17-distroless-latest][51],
  [17.0.5-17.38.21-distroless][54],
  
  * [19-jre-latest][11],
  [19.0.0-19.28.81-jre][15],
  [19.0.1-19.30.11-jre][16],
  [19.0.2-19.32.13-jre][17],
  
  * [18-jre-latest][23],
  [18.0.1-18.30.11-jre][27],
  [18.0.2-18.32.11-jre][28],
  [18.0.2.1-18.32.13-jre][29],
  
  * [17-jre-latest][35],
  [17.0.0-17.28.13-jre][44],
  [17.0.1-17.30.15-jre][45],
  [17.0.2-17.32.13-jre][46],
  [17.0.3-17.34.19-jre][47],
  [17.0.4-17.36.13-jre][48],
  [17.0.5-17.38.21-jre][49],
  [17.0.6-17.40.19-jre][50],
  [17.0.4.1-17.36.17-jre][52],
  
  * [16-jre-latest][64],
  [16.0.0-16.28.11-jre][67],
  [16.0.1-16.30.15-jre][68],
  [16.0.2-16.32.15-jre][69],
  
  * [15-jre-latest][71],
  [15.0.7-15.40.19-jre][83],
  [15.0.8-15.42.15-jre][84],
  [15.0.9-15.44.13-jre][85],
  [15.0.10-15.46.17-jre][86],
  
  * [13-jre-latest][98],
  [13.0.11-13.48.19-jre][111],
  [13.0.12-13.50.15-jre][112],
  [13.0.13-13.52.15-jre][113],
  [13.0.14-13.54.17-jre][114],
  
  * [11-jre-latest][131],
  [11.0.15-11.56.19-jre][146],
  [11.0.16-11.58.15-jre][147],
  [11.0.17-11.60.19-jre][148],
  [11.0.18-11.62.17-jre][149],
  [11.0.16.1-11.58.23-jre][151],
  
  * [8-jre-latest][166],
  [8u332-8.62.0.19-jre][209],
  [8u342-8.64.0.15-jre][210],
  [8u345-8.64.0.19-jre][211],
  [8u352-8.66.0.15-jre][212],
  [8u362-8.68.0.19-jre][213],
  
  * [19-latest][10],
  [19.0.0-19.28.81][12],
  [19.0.1-19.30.11][13],
  [19.0.2-19.32.13][14],
  
  * [18-latest][22],
  [18.0.1-18.30.11][24],
  [18.0.2-18.32.11][25],
  [18.0.2.1-18.32.13][26],
  
  * [17-latest][34],
  [17.0.0-17.28.13][36],
  [17.0.1-17.30.15][37],
  [17.0.2-17.32.13][38],
  [17.0.3-17.34.19][39],
  [17.0.4-17.36.13][40],
  [17.0.5-17.38.21][41],
  [17.0.6-17.40.19][42],
  [17.0.4.1-17.36.17][43],
  
  * [16-latest][63],
  [16.0.0-16.28.11][65],
  [16.0.2-16.32.15][66],
  
  * [15-latest][70],
  [15.0.1-15.28.13][72],
  [15.0.1-15.28.51][73],
  [15.0.2-15.29.15][74],
  [15.0.3-15.32.15][75],
  [15.0.4-15.34.17][76],
  [15.0.5-15.36.13][77],
  [15.0.6-15.38.17][78],
  [15.0.7-15.40.19][79],
  [15.0.8-15.42.15][80],
  [15.0.9-15.44.13][81],
  [15.0.10-15.46.17][82],
  
  * [14-latest][92],
  [14.0.1-14.28.21][93],
  [14.0.2-14.29.23][94],
  
  * [13-latest][95],
  [13.0.1-13.28][96],
  [13.0.2-13.29][97],
  [13.0.3-13.31.11][99],
  [13.0.4-13.33.25][100],
  [13.0.5-13.35.17][101],
  [13.0.6-13.37.21][102],
  [13.0.7-13.40.15][103],
  [13.0.8-13.42.17][104],
  [13.0.9-13.44.13][105],
  [13.0.10-13.46.15][106],
  [13.0.11-13.48.19][107],
  [13.0.12-13.50.15][108],
  [13.0.13-13.52.15][109],
  [13.0.14-13.54.17][110],
  
  * [12-12.1][120],
  [12-latest][121],
  [12.0.1-12.2][122],
  [12.0.2-12.3][123],
  
  * [11-latest][124],
  [11.0.1-11.2][125],
  [11.0.2-11.29][126],
  [11.0.3-11.31][127],
  [11.0.4-11.33][128],
  [11.0.5-11.35][129],
  [11.0.6-11.37][130],
  [11.0.7-11.39.15][132],
  [11.0.8-11.41.23][133],
  [11.0.9-11.43.21][134],
  [11.0.10-11.45.27][135],
  [11.0.11-11.48.21][136],
  [11.0.12-11.50.19][137],
  [11.0.13-11.52.13][138],
  [11.0.14-11.54.23][139],
  [11.0.15-11.56.19][140],
  [11.0.16-11.58.15][141],
  [11.0.17-11.60.19][142],
  [11.0.18-11.62.17][143],
  [11.0.14.1-11.54.25][144],
  [11.0.16.1-11.58.23][145],
  
  * [10-latest][157],
  [10u01-10.2][158],
  [10u02-10.3][159],
  
  * [9-ea][160],
  [9-latest][161],
  [9u01-9.0.1.3][162],
  [9u04-9.0.4.1][163],
  [9u07-9.0.7.1][164],
  
  * [8-latest][165],
  [8u05-8.1.0.6][167],
  [8u11-8.2.0.1][168],
  [8u20-8.3.0.1][169],
  [8u25-8.4.0.1][170],
  [8u31-8.5.0.1][171],
  [8u40-8.6.0.1][172],
  [8u45-8.7.0.5][173],
  [8u51-8.8.0.3][174],
  [8u60-8.9.0.4][175],
  [8u65-8.10.0.1][176],
  [8u66-8.11.0.1][177],
  [8u72-8.13.0.5][178],
  [8u92-8.15.0.1][179],
  [8u102-8.17.0.3][180],
  [8u112-8.19.0.1][181],
  [8u121-8.20.0.5][182],
  [8u131-8.21.0.1][183],
  [8u144-8.23.0.3][184],
  [8u152-8.25.0.1][185],
  [8u162-8.27.0.7][186],
  [8u172-8.30.0.1][187],
  [8u181-8.31.0.1][188],
  [8u192-8.33.0.1][189],
  [8u202-8.36.0.1][190],
  [8u212-8.38.0.13][191],
  [8u222-8.40.0.25][192],
  [8u232-8.42.0.21][193],
  [8u232-8.42.0.23][194],
  [8u242-8.44.0.11][195],
  [8u252-8.46.0.19][196],
  [8u262-8.48.0.51][197],
  [8u272-8.50.0.21][198],
  [8u275-8.50.0.53][199],
  [8u282-8.52.0.23][200],
  [8u302-8.56.0.21][201],
  [8u312-8.58.0.13][202],
  [8u322-8.60.0.21][203],
  [8u332-8.62.0.19][204],
  [8u342-8.64.0.15][205],
  [8u345-8.64.0.19][206],
  [8u352-8.66.0.15][207],
  [8u362-8.68.0.19][208],
  
  * [7-latest][220],
  [7u55-7.4.0.5][221],
  [7u60-7.5.0.1][222],
  [7u65-7.6.0.1][223],
  [7u72-7.7.0.1][224],
  [7u76-7.8.0.3][225],
  [7u79-7.9.0.2][226],
  [7u80-7.10.0.1][227],
  [7u85-7.11.0.3][228],
  [7u91-7.12.0.3][229],
  [7u95-7.13.0.1][230],
  [7u101-7.14.0.5][231],
  [7u111-7.15.0.1][232],
  [7u121-7.16.0.1][233],
  [7u131-7.17.0.5][234],
  [7u141-7.18.0.3][235],
  [7u154-7.20.0.3][236],
  [7u161-7.21.0.3][237],
  [7u171-7.22.0.3][238],
  [7u181-7.23.0.1][239],
  [7u191-7.24.0.1][240],
  [7u201-7.25.0.5][241],
  [7u211-7.27.0.1][242],
  [7u222-7.29.0.5][243],
  [7u232-7.31.0.5][244],
  [7u242-7.34.0.5][245],
  [7u252-7.36.0.5][246],
  [7u262-7.38.0.11][247],
  [7u272-7.40.0.15][248],
  [7u282-7.42.0.13][249],
  [7u285-7.42.0.51][250],
  [7u292-7.44.0.11][251],
  [7u302-7.46.0.11][252],
  [7u312-7.48.0.11][253],
  [7u322-7.50.0.11][254],
  [7u332-7.52.0.11][255],
  [7u342-7.54.0.13][256],
  [7u352-7.56.0.11][257],
  
  * [6-latest][258],
  [6u49-6.4.0.6][259],
  [6u53-6.5.0.2][260],
  [6u56-6.6.0.1][261],
  [6u59-6.7.0.2][262],
  [6u63-6.8.0.1][263],
  [6u69-6.9.0.3][264],
  [6u73-6.10.0.3][265],
  [6u77-6.11.0.2][266],
  [6u79-6.12.0.2][267],
  [6u83-6.13.0.3][268],
  [6u87-6.14.0.1][269],
  [6u89-6.15.0.1][270],
  [6u93-6.16.0.1][271],
  [6u97-6.17.0.1][272],
  [6u99-6.18.0.3][273],
  [6u103-6.19.0.1][274],
  [6u107-6.20.0.1][275],
  [6u113-6.21.0.3][276],
  [6u119-6.22.0.3][277],
  

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


  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-jre-headless-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81-jre-headless/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-headless-latest/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre-headless/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre-headless/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-headless-latest/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre-headless/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre-headless/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre-headless/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre-headless/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre-headless/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-jre-headless/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.6-17.40.19-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-headless-latest/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre-headless/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre-headless/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre-headless/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-headless-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre-headless/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre-headless/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre-headless/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-headless-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre-headless/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre-headless/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre-headless/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.18-11.62.17-jre-headless/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-headless-latest/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre-headless/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u362-8.68.0.19-jre-headless/Dockerfile
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-distroless-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-distroless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.2-19.32.13-jre/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-jre-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13-jre/Dockerfile
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-jre-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13-jre/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19-jre/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13-jre/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.6-17.40.19-jre/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17-jre/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-jre-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.1-16.30.15-jre/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15-jre/Dockerfile
  
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-jre-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15-jre/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13-jre/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.10-15.46.17-jre/Dockerfile
  
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-jre-latest/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19-jre/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15-jre/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15-jre/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.14-13.54.17-jre/Dockerfile
  
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-jre-latest/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15-jre/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19-jre/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.18-11.62.17-jre/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23-jre/Dockerfile
  
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-jre-latest/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15-jre/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19-jre/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15-jre/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u362-8.68.0.19-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.0-19.28.81/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.1-19.30.11/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/19.0.2-19.32.13/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.1-18.30.11/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2-18.32.11/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/18.0.2.1-18.32.13/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.0-17.28.13/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.1-17.30.15/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.2-17.32.13/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.3-17.34.19/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4-17.36.13/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.5-17.38.21/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.6-17.40.19/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/17.0.4.1-17.36.17/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16-latest/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.0-16.28.11/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/16.0.2-16.32.15/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.13/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.1-15.28.51/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.2-15.29.15/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.3-15.32.15/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.4-15.34.17/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.5-15.36.13/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.6-15.38.17/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.7-15.40.19/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.8-15.42.15/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.9-15.44.13/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/15.0.10-15.46.17/Dockerfile
  
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.1-14.28.21/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/14.0.2-14.29.23/Dockerfile
  
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13-latest/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.1-13.28/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.2-13.29/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.3-13.31.11/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.4-13.33.25/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.5-13.35.17/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.6-13.37.21/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.7-13.40.15/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.8-13.42.17/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.9-13.44.13/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.10-13.46.15/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.11-13.48.19/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.12-13.50.15/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.13-13.52.15/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/13.0.14-13.54.17/Dockerfile
  
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-12.1/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12-latest/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.1-12.2/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/12.0.2-12.3/Dockerfile
  
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11-latest/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.1-11.2/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.2-11.29/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.3-11.31/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.4-11.33/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.5-11.35/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.6-11.37/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.7-11.39.15/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.8-11.41.23/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.9-11.43.21/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.10-11.45.27/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.11-11.48.21/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.12-11.50.19/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.13-11.52.13/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14-11.54.23/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.15-11.56.19/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16-11.58.15/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.17-11.60.19/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.18-11.62.17/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.14.1-11.54.25/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/11.0.16.1-11.58.23/Dockerfile
  
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10-latest/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u01-10.2/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/10u02-10.3/Dockerfile
  
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-ea/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9-latest/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u01-9.0.1.3/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u04-9.0.4.1/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/9u07-9.0.7.1/Dockerfile
  
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8-latest/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u05-8.1.0.6/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u11-8.2.0.1/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u20-8.3.0.1/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u25-8.4.0.1/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u31-8.5.0.1/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u40-8.6.0.1/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u45-8.7.0.5/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u51-8.8.0.3/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u60-8.9.0.4/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u65-8.10.0.1/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u66-8.11.0.1/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u72-8.13.0.5/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u92-8.15.0.1/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u102-8.17.0.3/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u112-8.19.0.1/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u121-8.20.0.5/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u131-8.21.0.1/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u144-8.23.0.3/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u152-8.25.0.1/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u162-8.27.0.7/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u172-8.30.0.1/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u181-8.31.0.1/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u192-8.33.0.1/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u202-8.36.0.1/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u212-8.38.0.13/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u222-8.40.0.25/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.21/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u232-8.42.0.23/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u242-8.44.0.11/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u252-8.46.0.19/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u262-8.48.0.51/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u272-8.50.0.21/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u275-8.50.0.53/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u282-8.52.0.23/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u302-8.56.0.21/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u312-8.58.0.13/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u322-8.60.0.21/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u332-8.62.0.19/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u342-8.64.0.15/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u345-8.64.0.19/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u352-8.66.0.15/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/8u362-8.68.0.19/Dockerfile
  
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7-latest/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u55-7.4.0.5/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u60-7.5.0.1/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u65-7.6.0.1/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u72-7.7.0.1/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u76-7.8.0.3/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u79-7.9.0.2/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u80-7.10.0.1/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u85-7.11.0.3/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u91-7.12.0.3/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u95-7.13.0.1/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u101-7.14.0.5/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u111-7.15.0.1/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u121-7.16.0.1/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u131-7.17.0.5/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u141-7.18.0.3/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u154-7.20.0.3/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u161-7.21.0.3/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u171-7.22.0.3/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u181-7.23.0.1/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u191-7.24.0.1/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u201-7.25.0.5/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u211-7.27.0.1/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u222-7.29.0.5/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u232-7.31.0.5/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u242-7.34.0.5/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u252-7.36.0.5/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u262-7.38.0.11/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u272-7.40.0.15/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u282-7.42.0.13/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u285-7.42.0.51/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u292-7.44.0.11/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u302-7.46.0.11/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u312-7.48.0.11/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u322-7.50.0.11/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u332-7.52.0.11/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u342-7.54.0.13/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/7u352-7.56.0.11/Dockerfile
  
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6-latest/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u49-6.4.0.6/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u53-6.5.0.2/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u56-6.6.0.1/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u59-6.7.0.2/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u63-6.8.0.1/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u69-6.9.0.3/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u73-6.10.0.3/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u77-6.11.0.2/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u79-6.12.0.2/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u83-6.13.0.3/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u87-6.14.0.1/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u89-6.15.0.1/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u93-6.16.0.1/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u97-6.17.0.1/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u99-6.18.0.3/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u103-6.19.0.1/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u107-6.20.0.1/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u113-6.21.0.3/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/6u119-6.22.0.3/Dockerfile
  