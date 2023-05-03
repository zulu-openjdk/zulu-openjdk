Azul Zulu Debian
================

These Docker images of Azul Zulu Build of OpenJDK are based on Debian.

Azul Zulu Builds of OpenJDK are available for free unlimited use and are commercially supported by [Azul][1] as a part of the Azul Platform Core bundle.
Check out [Azul Platform Core][2] for more information. The technical documentation can be found on [docs.azul.com/core][3].

Docker images of Azul Zulu are available in the following repositories, depending on the base system:

  * [Ubuntu: azul/zulu-openjdk][4]
  * [Alpine: azul/zulu-openjdk-alpine][5]
  * [CentOS: azul/zulu-openjdk-centos][6]
  * [Debian: azul/zulu-openjdk-debian][7]
  * [Distroless: azul/zulu-openjdk-distroless][8]

Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`20.0.1-20.30.11`, `20-latest` (*20-latest/Dockerfile)*][11]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][20]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][33]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][45]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][75]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][83]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][105]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][108]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][133]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][137]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][173]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][176]
  * [`8u372-8.70.0.23`, `8-latest` (*8-latest/Dockerfile)*][181]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][243]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][281]

Previous
--------

Earlier Debian Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [20-jre-headless-latest][17],
  [20.0.0-20.28.85-jre-headless][18],
  [20.0.1-20.30.11-jre-headless][19],
  
  * [19-jre-headless-latest][29],
  [19.0.0-19.28.81-jre-headless][30],
  [19.0.1-19.30.11-jre-headless][31],
  [19.0.2-19.32.13-jre-headless][32],
  
  * [18-jre-headless-latest][41],
  [18.0.1-18.30.11-jre-headless][42],
  [18.0.2-18.32.11-jre-headless][43],
  [18.0.2.1-18.32.13-jre-headless][44],
  
  * [17-jre-headless-latest][65],
  [17.0.0-17.28.13-jre-headless][66],
  [17.0.1-17.30.15-jre-headless][67],
  [17.0.2-17.32.13-jre-headless][68],
  [17.0.3-17.34.19-jre-headless][69],
  [17.0.4-17.36.13-jre-headless][70],
  [17.0.5-17.38.21-jre-headless][71],
  [17.0.6-17.40.19-jre-headless][72],
  [17.0.7-17.42.19-jre-headless][73],
  [17.0.4.1-17.36.17-jre-headless][74],
  
  * [15-jre-headless-latest][100],
  [15.0.7-15.40.19-jre-headless][101],
  [15.0.8-15.42.15-jre-headless][102],
  [15.0.9-15.44.13-jre-headless][103],
  [15.0.10-15.46.17-jre-headless][104],
  
  * [13-jre-headless-latest][128],
  [13.0.11-13.48.19-jre-headless][129],
  [13.0.12-13.50.15-jre-headless][130],
  [13.0.13-13.52.15-jre-headless][131],
  [13.0.14-13.54.17-jre-headless][132],
  
  * [11-jre-headless-latest][165],
  [11.0.15-11.56.19-jre-headless][167],
  [11.0.16-11.58.15-jre-headless][168],
  [11.0.17-11.60.19-jre-headless][169],
  [11.0.18-11.62.17-jre-headless][170],
  [11.0.19-11.64.19-jre-headless][171],
  [11.0.16.1-11.58.23-jre-headless][172],
  
  * [8-jre-headless-latest][235],
  [8u332-8.62.0.19-jre-headless][236],
  [8u342-8.64.0.15-jre-headless][237],
  [8u345-8.64.0.19-jre-headless][238],
  [8u352-8.66.0.15-jre-headless][239],
  [8u362-8.68.0.19-jre-headless][240],
  [8u362-8.68.0.21-jre-headless][241],
  [8u372-8.70.0.23-jre-headless][242],
  
  * [20-jre-latest][12],
  [20.0.0-20.28.85-jre][15],
  [20.0.1-20.30.11-jre][16],
  
  * [19-jre-latest][21],
  [19.0.0-19.28.81-jre][26],
  [19.0.1-19.30.11-jre][27],
  [19.0.2-19.32.13-jre][28],
  
  * [18-jre-latest][34],
  [18.0.1-18.30.11-jre][38],
  [18.0.2-18.32.11-jre][39],
  [18.0.2.1-18.32.13-jre][40],
  
  * [17-jre-latest][46],
  [17.0.0-17.28.13-jre][56],
  [17.0.1-17.30.15-jre][57],
  [17.0.2-17.32.13-jre][58],
  [17.0.3-17.34.19-jre][59],
  [17.0.4-17.36.13-jre][60],
  [17.0.5-17.38.21-jre][61],
  [17.0.6-17.40.19-jre][62],
  [17.0.7-17.42.19-jre][63],
  [17.0.4.1-17.36.17-jre][64],
  
  * [16-jre-latest][76],
  [16.0.0-16.28.11-jre][80],
  [16.0.1-16.30.15-jre][81],
  [16.0.2-16.32.15-jre][82],
  
  * [15-jre-latest][84],
  [15.0.7-15.40.19-jre][96],
  [15.0.8-15.42.15-jre][97],
  [15.0.9-15.44.13-jre][98],
  [15.0.10-15.46.17-jre][99],
  
  * [13-jre-latest][111],
  [13.0.11-13.48.19-jre][124],
  [13.0.12-13.50.15-jre][125],
  [13.0.13-13.52.15-jre][126],
  [13.0.14-13.54.17-jre][127],
  
  * [11-jre-latest][144],
  [11.0.15-11.56.19-jre][160],
  [11.0.16-11.58.15-jre][161],
  [11.0.17-11.60.19-jre][162],
  [11.0.18-11.62.17-jre][163],
  [11.0.19-11.64.19-jre][164],
  [11.0.16.1-11.58.23-jre][166],
  
  * [8-jre-latest][182],
  [8u332-8.62.0.19-jre][228],
  [8u342-8.64.0.15-jre][229],
  [8u345-8.64.0.19-jre][230],
  [8u352-8.66.0.15-jre][231],
  [8u362-8.68.0.19-jre][232],
  [8u362-8.68.0.21-jre][233],
  [8u372-8.70.0.23-jre][234],
  
  * [20-latest][11],
  [20.0.0-20.28.85][13],
  [20.0.1-20.30.11][14],
  
  * [19-latest][20],
  [19.0.0-19.28.81][22],
  [19.0.1-19.30.11][23],
  [19.0.2-19.32.13][24],
  [19.0.2-19.32.15][25],
  
  * [18-latest][33],
  [18.0.1-18.30.11][35],
  [18.0.2-18.32.11][36],
  [18.0.2.1-18.32.13][37],
  
  * [17-latest][45],
  [17.0.0-17.28.13][47],
  [17.0.1-17.30.15][48],
  [17.0.2-17.32.13][49],
  [17.0.3-17.34.19][50],
  [17.0.4-17.36.13][51],
  [17.0.5-17.38.21][52],
  [17.0.6-17.40.19][53],
  [17.0.7-17.42.19][54],
  [17.0.4.1-17.36.17][55],
  
  * [16-latest][75],
  [16.0.0-16.28.11][77],
  [16.0.1-16.30.15][78],
  [16.0.2-16.32.15][79],
  
  * [15-latest][83],
  [15.0.1-15.28.13][85],
  [15.0.1-15.28.51][86],
  [15.0.2-15.29.15][87],
  [15.0.3-15.32.15][88],
  [15.0.4-15.34.17][89],
  [15.0.5-15.36.13][90],
  [15.0.6-15.38.17][91],
  [15.0.7-15.40.19][92],
  [15.0.8-15.42.15][93],
  [15.0.9-15.44.13][94],
  [15.0.10-15.46.17][95],
  
  * [14-latest][105],
  [14.0.1-14.28.21][106],
  [14.0.2-14.29.23][107],
  
  * [13-latest][108],
  [13.0.1-13.28][109],
  [13.0.2-13.29][110],
  [13.0.3-13.31.11][112],
  [13.0.4-13.33.25][113],
  [13.0.5-13.35.17][114],
  [13.0.6-13.37.21][115],
  [13.0.7-13.40.15][116],
  [13.0.8-13.42.17][117],
  [13.0.9-13.44.13][118],
  [13.0.10-13.46.15][119],
  [13.0.11-13.48.19][120],
  [13.0.12-13.50.15][121],
  [13.0.13-13.52.15][122],
  [13.0.14-13.54.17][123],
  
  * [12-12.1][133],
  [12-latest][134],
  [12.0.1-12.2][135],
  [12.0.2-12.3][136],
  
  * [11-latest][137],
  [11.0.1-11.2][138],
  [11.0.2-11.29][139],
  [11.0.3-11.31][140],
  [11.0.4-11.33][141],
  [11.0.5-11.35][142],
  [11.0.6-11.37][143],
  [11.0.7-11.39.15][145],
  [11.0.8-11.41.23][146],
  [11.0.9-11.43.21][147],
  [11.0.10-11.45.27][148],
  [11.0.11-11.48.21][149],
  [11.0.12-11.50.19][150],
  [11.0.13-11.52.13][151],
  [11.0.14-11.54.23][152],
  [11.0.15-11.56.19][153],
  [11.0.16-11.58.15][154],
  [11.0.17-11.60.19][155],
  [11.0.18-11.62.17][156],
  [11.0.19-11.64.19][157],
  [11.0.14.1-11.54.25][158],
  [11.0.16.1-11.58.23][159],
  
  * [10-latest][173],
  [10u01-10.2][174],
  [10u02-10.3][175],
  
  * [9-ea][176],
  [9-latest][177],
  [9u01-9.0.1.3][178],
  [9u04-9.0.4.1][179],
  [9u07-9.0.7.1][180],
  
  * [8-latest][181],
  [8u05-8.1.0.6][183],
  [8u11-8.2.0.1][184],
  [8u20-8.3.0.1][185],
  [8u25-8.4.0.1][186],
  [8u31-8.5.0.1][187],
  [8u40-8.6.0.1][188],
  [8u45-8.7.0.5][189],
  [8u51-8.8.0.3][190],
  [8u60-8.9.0.4][191],
  [8u65-8.10.0.1][192],
  [8u66-8.11.0.1][193],
  [8u72-8.13.0.5][194],
  [8u92-8.15.0.1][195],
  [8u102-8.17.0.3][196],
  [8u112-8.19.0.1][197],
  [8u121-8.20.0.5][198],
  [8u131-8.21.0.1][199],
  [8u144-8.23.0.3][200],
  [8u152-8.25.0.1][201],
  [8u162-8.27.0.7][202],
  [8u172-8.30.0.1][203],
  [8u181-8.31.0.1][204],
  [8u192-8.33.0.1][205],
  [8u202-8.36.0.1][206],
  [8u212-8.38.0.13][207],
  [8u222-8.40.0.25][208],
  [8u232-8.42.0.21][209],
  [8u232-8.42.0.23][210],
  [8u242-8.44.0.11][211],
  [8u252-8.46.0.19][212],
  [8u262-8.48.0.51][213],
  [8u272-8.50.0.21][214],
  [8u275-8.50.0.53][215],
  [8u282-8.52.0.23][216],
  [8u292-8.54.0.21][217],
  [8u302-8.56.0.21][218],
  [8u312-8.58.0.13][219],
  [8u322-8.60.0.21][220],
  [8u332-8.62.0.19][221],
  [8u342-8.64.0.15][222],
  [8u345-8.64.0.19][223],
  [8u352-8.66.0.15][224],
  [8u362-8.68.0.19][225],
  [8u362-8.68.0.21][226],
  [8u372-8.70.0.23][227],
  
  * [7-latest][243],
  [7u55-7.4.0.5][244],
  [7u60-7.5.0.1][245],
  [7u65-7.6.0.1][246],
  [7u72-7.7.0.1][247],
  [7u76-7.8.0.3][248],
  [7u79-7.9.0.2][249],
  [7u80-7.10.0.1][250],
  [7u85-7.11.0.3][251],
  [7u91-7.12.0.3][252],
  [7u95-7.13.0.1][253],
  [7u101-7.14.0.5][254],
  [7u111-7.15.0.1][255],
  [7u121-7.16.0.1][256],
  [7u131-7.17.0.5][257],
  [7u141-7.18.0.3][258],
  [7u154-7.20.0.3][259],
  [7u161-7.21.0.3][260],
  [7u171-7.22.0.3][261],
  [7u181-7.23.0.1][262],
  [7u191-7.24.0.1][263],
  [7u201-7.25.0.5][264],
  [7u211-7.27.0.1][265],
  [7u222-7.29.0.5][266],
  [7u232-7.31.0.5][267],
  [7u242-7.34.0.5][268],
  [7u252-7.36.0.5][269],
  [7u262-7.38.0.11][270],
  [7u272-7.40.0.15][271],
  [7u282-7.42.0.13][272],
  [7u285-7.42.0.51][273],
  [7u292-7.44.0.11][274],
  [7u302-7.46.0.11][275],
  [7u312-7.48.0.11][276],
  [7u322-7.50.0.11][277],
  [7u332-7.52.0.11][278],
  [7u342-7.54.0.13][279],
  [7u352-7.56.0.11][280],
  
  * [6-latest][281],
  [6u49-6.4.0.6][282],
  [6u53-6.5.0.2][283],
  [6u56-6.6.0.1][284],
  [6u59-6.7.0.2][285],
  [6u63-6.8.0.1][286],
  [6u69-6.9.0.3][287],
  [6u73-6.10.0.3][288],
  [6u77-6.11.0.2][289],
  [6u79-6.12.0.2][290],
  [6u83-6.13.0.3][291],
  [6u87-6.14.0.1][292],
  [6u89-6.15.0.1][293],
  [6u93-6.16.0.1][294],
  [6u97-6.17.0.1][295],
  [6u99-6.18.0.3][296],
  [6u103-6.19.0.1][297],
  [6u107-6.20.0.1][298],
  [6u113-6.21.0.3][299],
  [6u119-6.22.0.3][300],
  

License
=======

Azul Zulu incorporates third-party licensed software packages. Some of these have distribution restrictions, and some have only reporting requirements. Please see [docs.azul.com/core/tpl][9] for the links to the documents with licenses for third-party software included in the latest version of Azul Platform Core.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc., from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

[BSD 3-Clause Clear License][10]

Links
=====

  [1]: https://www.azul.com/
  [2]: https://www.azul.com/products/core/
  [3]: https://docs.azul.com/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [7]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [8]: https://hub.docker.com/r/azul/zulu-openjdk-distroless
  [9]: https://docs.azul.com/core/tpl
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/LICENSE.txt


  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre-headless/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre-headless/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19-jre-headless/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13-jre-headless/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19-jre-headless/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre-headless/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19-jre-headless/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17-jre-headless/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19-jre-headless/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre-headless/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre-headless/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15-jre-headless/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19-jre-headless/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21-jre-headless/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17-jre/Dockerfile
  
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17-jre/Dockerfile
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17-jre/Dockerfile
  
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19-jre/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17-jre/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19-jre/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre/Dockerfile
  
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15-jre/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19-jre/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21-jre/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.15/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17/Dockerfile
  
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.3-15.32.15/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.4-15.34.17/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.5-15.36.13/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.6-15.38.17/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17/Dockerfile
  
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.4-13.33.25/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.5-13.35.17/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.6-13.37.21/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.7-13.40.15/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.8-13.42.17/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.9-13.44.13/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.10-13.46.15/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17/Dockerfile
  
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.4-11.33/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.5-11.35/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.6-11.37/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.7-11.39.15/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.8-11.41.23/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.9-11.43.21/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.10-11.45.27/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.11-11.48.21/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.12-11.50.19/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.13-11.52.13/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.14-11.54.23/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.14.1-11.54.25/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23/Dockerfile
  
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u07-9.0.7.1/Dockerfile
  
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u25-8.4.0.1/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u31-8.5.0.1/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u40-8.6.0.1/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u45-8.7.0.5/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u51-8.8.0.3/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u60-8.9.0.4/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u65-8.10.0.1/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u66-8.11.0.1/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u72-8.13.0.5/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u92-8.15.0.1/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u102-8.17.0.3/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u112-8.19.0.1/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u121-8.20.0.5/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u131-8.21.0.1/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u144-8.23.0.3/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u152-8.25.0.1/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u162-8.27.0.7/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u172-8.30.0.1/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u181-8.31.0.1/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u192-8.33.0.1/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u202-8.36.0.1/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u212-8.38.0.13/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u222-8.40.0.25/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u232-8.42.0.21/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u232-8.42.0.23/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u242-8.44.0.11/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u252-8.46.0.19/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u262-8.48.0.51/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u272-8.50.0.21/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u275-8.50.0.53/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u282-8.52.0.23/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u292-8.54.0.21/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u302-8.56.0.21/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u312-8.58.0.13/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u322-8.60.0.21/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23/Dockerfile
  
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u72-7.7.0.1/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u76-7.8.0.3/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u79-7.9.0.2/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u80-7.10.0.1/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u85-7.11.0.3/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u91-7.12.0.3/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u95-7.13.0.1/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u101-7.14.0.5/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u111-7.15.0.1/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u121-7.16.0.1/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u131-7.17.0.5/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u141-7.18.0.3/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u154-7.20.0.3/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u161-7.21.0.3/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u171-7.22.0.3/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u181-7.23.0.1/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u191-7.24.0.1/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u201-7.25.0.5/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u211-7.27.0.1/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u222-7.29.0.5/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u232-7.31.0.5/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u242-7.34.0.5/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u252-7.36.0.5/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u262-7.38.0.11/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u272-7.40.0.15/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u282-7.42.0.13/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u285-7.42.0.51/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u292-7.44.0.11/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u302-7.46.0.11/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u312-7.48.0.11/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u322-7.50.0.11/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u332-7.52.0.11/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u342-7.54.0.13/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u352-7.56.0.11/Dockerfile
  
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u59-6.7.0.2/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u63-6.8.0.1/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u69-6.9.0.3/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u73-6.10.0.3/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u77-6.11.0.2/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u79-6.12.0.2/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u83-6.13.0.3/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u87-6.14.0.1/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u89-6.15.0.1/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u93-6.16.0.1/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u97-6.17.0.1/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u99-6.18.0.3/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u103-6.19.0.1/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u107-6.20.0.1/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u113-6.21.0.3/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u119-6.22.0.3/Dockerfile
  