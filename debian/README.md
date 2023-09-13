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


  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][11]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][23]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][36]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][48]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][84]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][92]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][114]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][117]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][142]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][146]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][188]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][191]
  * [`8u382-8.72.0.17`, `8-latest` (*8-latest/Dockerfile)*][196]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][261]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][299]

Previous
--------

Earlier Debian Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [20-jre-headless-latest][19],
  [20.0.0-20.28.85-jre-headless][20],
  [20.0.1-20.30.11-jre-headless][21],
  [20.0.2-20.32.11-jre-headless][22],
  
  * [19-jre-headless-latest][32],
  [19.0.0-19.28.81-jre-headless][33],
  [19.0.1-19.30.11-jre-headless][34],
  [19.0.2-19.32.13-jre-headless][35],
  
  * [18-jre-headless-latest][44],
  [18.0.1-18.30.11-jre-headless][45],
  [18.0.2-18.32.11-jre-headless][46],
  [18.0.2.1-18.32.13-jre-headless][47],
  
  * [17-jre-headless-latest][72],
  [17.0.0-17.28.13-jre-headless][73],
  [17.0.1-17.30.15-jre-headless][74],
  [17.0.2-17.32.13-jre-headless][75],
  [17.0.3-17.34.19-jre-headless][76],
  [17.0.4-17.36.13-jre-headless][77],
  [17.0.5-17.38.21-jre-headless][78],
  [17.0.6-17.40.19-jre-headless][79],
  [17.0.7-17.42.19-jre-headless][80],
  [17.0.8-17.44.15-jre-headless][81],
  [17.0.4.1-17.36.17-jre-headless][82],
  [17.0.8.1-17.44.53-jre-headless][83],
  
  * [15-jre-headless-latest][109],
  [15.0.7-15.40.19-jre-headless][110],
  [15.0.8-15.42.15-jre-headless][111],
  [15.0.9-15.44.13-jre-headless][112],
  [15.0.10-15.46.17-jre-headless][113],
  
  * [13-jre-headless-latest][137],
  [13.0.11-13.48.19-jre-headless][138],
  [13.0.12-13.50.15-jre-headless][139],
  [13.0.13-13.52.15-jre-headless][140],
  [13.0.14-13.54.17-jre-headless][141],
  
  * [11-jre-headless-latest][177],
  [11.0.15-11.56.19-jre-headless][180],
  [11.0.16-11.58.15-jre-headless][181],
  [11.0.17-11.60.19-jre-headless][182],
  [11.0.18-11.62.17-jre-headless][183],
  [11.0.19-11.64.19-jre-headless][184],
  [11.0.20-11.66.15-jre-headless][185],
  [11.0.16.1-11.58.23-jre-headless][186],
  [11.0.20.1-11.66.19-jre-headless][187],
  
  * [8-jre-headless-latest][252],
  [8u332-8.62.0.19-jre-headless][253],
  [8u342-8.64.0.15-jre-headless][254],
  [8u345-8.64.0.19-jre-headless][255],
  [8u352-8.66.0.15-jre-headless][256],
  [8u362-8.68.0.19-jre-headless][257],
  [8u362-8.68.0.21-jre-headless][258],
  [8u372-8.70.0.23-jre-headless][259],
  [8u382-8.72.0.17-jre-headless][260],
  
  * [20-jre-latest][12],
  [20.0.0-20.28.85-jre][16],
  [20.0.1-20.30.11-jre][17],
  [20.0.2-20.32.11-jre][18],
  
  * [19-jre-latest][24],
  [19.0.0-19.28.81-jre][29],
  [19.0.1-19.30.11-jre][30],
  [19.0.2-19.32.13-jre][31],
  
  * [18-jre-latest][37],
  [18.0.1-18.30.11-jre][41],
  [18.0.2-18.32.11-jre][42],
  [18.0.2.1-18.32.13-jre][43],
  
  * [17-jre-latest][49],
  [17.0.0-17.28.13-jre][61],
  [17.0.1-17.30.15-jre][62],
  [17.0.2-17.32.13-jre][63],
  [17.0.3-17.34.19-jre][64],
  [17.0.4-17.36.13-jre][65],
  [17.0.5-17.38.21-jre][66],
  [17.0.6-17.40.19-jre][67],
  [17.0.7-17.42.19-jre][68],
  [17.0.8-17.44.15-jre][69],
  [17.0.4.1-17.36.17-jre][70],
  [17.0.8.1-17.44.53-jre][71],
  
  * [16-jre-latest][85],
  [16.0.0-16.28.11-jre][89],
  [16.0.1-16.30.15-jre][90],
  [16.0.2-16.32.15-jre][91],
  
  * [15-jre-latest][93],
  [15.0.7-15.40.19-jre][105],
  [15.0.8-15.42.15-jre][106],
  [15.0.9-15.44.13-jre][107],
  [15.0.10-15.46.17-jre][108],
  
  * [13-jre-latest][120],
  [13.0.11-13.48.19-jre][133],
  [13.0.12-13.50.15-jre][134],
  [13.0.13-13.52.15-jre][135],
  [13.0.14-13.54.17-jre][136],
  
  * [11-jre-latest][153],
  [11.0.15-11.56.19-jre][171],
  [11.0.16-11.58.15-jre][172],
  [11.0.17-11.60.19-jre][173],
  [11.0.18-11.62.17-jre][174],
  [11.0.19-11.64.19-jre][175],
  [11.0.20-11.66.15-jre][176],
  [11.0.16.1-11.58.23-jre][178],
  [11.0.20.1-11.66.19-jre][179],
  
  * [8-jre-latest][197],
  [8u332-8.62.0.19-jre][244],
  [8u342-8.64.0.15-jre][245],
  [8u345-8.64.0.19-jre][246],
  [8u352-8.66.0.15-jre][247],
  [8u362-8.68.0.19-jre][248],
  [8u362-8.68.0.21-jre][249],
  [8u372-8.70.0.23-jre][250],
  [8u382-8.72.0.17-jre][251],
  
  * [20-latest][11],
  [20.0.0-20.28.85][13],
  [20.0.1-20.30.11][14],
  [20.0.2-20.32.11][15],
  
  * [19-latest][23],
  [19.0.0-19.28.81][25],
  [19.0.1-19.30.11][26],
  [19.0.2-19.32.13][27],
  [19.0.2-19.32.15][28],
  
  * [18-latest][36],
  [18.0.1-18.30.11][38],
  [18.0.2-18.32.11][39],
  [18.0.2.1-18.32.13][40],
  
  * [17-latest][48],
  [17.0.0-17.28.13][50],
  [17.0.1-17.30.15][51],
  [17.0.2-17.32.13][52],
  [17.0.3-17.34.19][53],
  [17.0.4-17.36.13][54],
  [17.0.5-17.38.21][55],
  [17.0.6-17.40.19][56],
  [17.0.7-17.42.19][57],
  [17.0.8-17.44.15][58],
  [17.0.4.1-17.36.17][59],
  [17.0.8.1-17.44.53][60],
  
  * [16-latest][84],
  [16.0.0-16.28.11][86],
  [16.0.1-16.30.15][87],
  [16.0.2-16.32.15][88],
  
  * [15-latest][92],
  [15.0.1-15.28.13][94],
  [15.0.1-15.28.51][95],
  [15.0.2-15.29.15][96],
  [15.0.3-15.32.15][97],
  [15.0.4-15.34.17][98],
  [15.0.5-15.36.13][99],
  [15.0.6-15.38.17][100],
  [15.0.7-15.40.19][101],
  [15.0.8-15.42.15][102],
  [15.0.9-15.44.13][103],
  [15.0.10-15.46.17][104],
  
  * [14-latest][114],
  [14.0.1-14.28.21][115],
  [14.0.2-14.29.23][116],
  
  * [13-latest][117],
  [13.0.1-13.28][118],
  [13.0.2-13.29][119],
  [13.0.3-13.31.11][121],
  [13.0.4-13.33.25][122],
  [13.0.5-13.35.17][123],
  [13.0.6-13.37.21][124],
  [13.0.7-13.40.15][125],
  [13.0.8-13.42.17][126],
  [13.0.9-13.44.13][127],
  [13.0.10-13.46.15][128],
  [13.0.11-13.48.19][129],
  [13.0.12-13.50.15][130],
  [13.0.13-13.52.15][131],
  [13.0.14-13.54.17][132],
  
  * [12-12.1][142],
  [12-latest][143],
  [12.0.1-12.2][144],
  [12.0.2-12.3][145],
  
  * [11-latest][146],
  [11.0.1-11.2][147],
  [11.0.2-11.29][148],
  [11.0.3-11.31][149],
  [11.0.4-11.33][150],
  [11.0.5-11.35][151],
  [11.0.6-11.37][152],
  [11.0.7-11.39.15][154],
  [11.0.8-11.41.23][155],
  [11.0.9-11.43.21][156],
  [11.0.10-11.45.27][157],
  [11.0.11-11.48.21][158],
  [11.0.12-11.50.19][159],
  [11.0.13-11.52.13][160],
  [11.0.14-11.54.23][161],
  [11.0.15-11.56.19][162],
  [11.0.16-11.58.15][163],
  [11.0.17-11.60.19][164],
  [11.0.18-11.62.17][165],
  [11.0.19-11.64.19][166],
  [11.0.20-11.66.15][167],
  [11.0.14.1-11.54.25][168],
  [11.0.16.1-11.58.23][169],
  [11.0.20.1-11.66.19][170],
  
  * [10-latest][188],
  [10u01-10.2][189],
  [10u02-10.3][190],
  
  * [9-ea][191],
  [9-latest][192],
  [9u01-9.0.1.3][193],
  [9u04-9.0.4.1][194],
  [9u07-9.0.7.1][195],
  
  * [8-latest][196],
  [8u05-8.1.0.6][198],
  [8u11-8.2.0.1][199],
  [8u20-8.3.0.1][200],
  [8u25-8.4.0.1][201],
  [8u31-8.5.0.1][202],
  [8u40-8.6.0.1][203],
  [8u45-8.7.0.5][204],
  [8u51-8.8.0.3][205],
  [8u60-8.9.0.4][206],
  [8u65-8.10.0.1][207],
  [8u66-8.11.0.1][208],
  [8u72-8.13.0.5][209],
  [8u92-8.15.0.1][210],
  [8u102-8.17.0.3][211],
  [8u112-8.19.0.1][212],
  [8u121-8.20.0.5][213],
  [8u131-8.21.0.1][214],
  [8u144-8.23.0.3][215],
  [8u152-8.25.0.1][216],
  [8u162-8.27.0.7][217],
  [8u172-8.30.0.1][218],
  [8u181-8.31.0.1][219],
  [8u192-8.33.0.1][220],
  [8u202-8.36.0.1][221],
  [8u212-8.38.0.13][222],
  [8u222-8.40.0.25][223],
  [8u232-8.42.0.21][224],
  [8u232-8.42.0.23][225],
  [8u242-8.44.0.11][226],
  [8u252-8.46.0.19][227],
  [8u262-8.48.0.51][228],
  [8u272-8.50.0.21][229],
  [8u275-8.50.0.53][230],
  [8u282-8.52.0.23][231],
  [8u292-8.54.0.21][232],
  [8u302-8.56.0.21][233],
  [8u312-8.58.0.13][234],
  [8u322-8.60.0.21][235],
  [8u332-8.62.0.19][236],
  [8u342-8.64.0.15][237],
  [8u345-8.64.0.19][238],
  [8u352-8.66.0.15][239],
  [8u362-8.68.0.19][240],
  [8u362-8.68.0.21][241],
  [8u372-8.70.0.23][242],
  [8u382-8.72.0.17][243],
  
  * [7-latest][261],
  [7u55-7.4.0.5][262],
  [7u60-7.5.0.1][263],
  [7u65-7.6.0.1][264],
  [7u72-7.7.0.1][265],
  [7u76-7.8.0.3][266],
  [7u79-7.9.0.2][267],
  [7u80-7.10.0.1][268],
  [7u85-7.11.0.3][269],
  [7u91-7.12.0.3][270],
  [7u95-7.13.0.1][271],
  [7u101-7.14.0.5][272],
  [7u111-7.15.0.1][273],
  [7u121-7.16.0.1][274],
  [7u131-7.17.0.5][275],
  [7u141-7.18.0.3][276],
  [7u154-7.20.0.3][277],
  [7u161-7.21.0.3][278],
  [7u171-7.22.0.3][279],
  [7u181-7.23.0.1][280],
  [7u191-7.24.0.1][281],
  [7u201-7.25.0.5][282],
  [7u211-7.27.0.1][283],
  [7u222-7.29.0.5][284],
  [7u232-7.31.0.5][285],
  [7u242-7.34.0.5][286],
  [7u252-7.36.0.5][287],
  [7u262-7.38.0.11][288],
  [7u272-7.40.0.15][289],
  [7u282-7.42.0.13][290],
  [7u285-7.42.0.51][291],
  [7u292-7.44.0.11][292],
  [7u302-7.46.0.11][293],
  [7u312-7.48.0.11][294],
  [7u322-7.50.0.11][295],
  [7u332-7.52.0.11][296],
  [7u342-7.54.0.13][297],
  [7u352-7.56.0.11][298],
  
  * [6-latest][299],
  [6u49-6.4.0.6][300],
  [6u53-6.5.0.2][301],
  [6u56-6.6.0.1][302],
  [6u59-6.7.0.2][303],
  [6u63-6.8.0.1][304],
  [6u69-6.9.0.3][305],
  [6u73-6.10.0.3][306],
  [6u77-6.11.0.2][307],
  [6u79-6.12.0.2][308],
  [6u83-6.13.0.3][309],
  [6u87-6.14.0.1][310],
  [6u89-6.15.0.1][311],
  [6u93-6.16.0.1][312],
  [6u97-6.17.0.1][313],
  [6u99-6.18.0.3][314],
  [6u103-6.19.0.1][315],
  [6u107-6.20.0.1][316],
  [6u113-6.21.0.3][317],
  [6u119-6.22.0.3][318],
  

License
=======

Azul Zulu incorporates third-party licensed software packages. Some of these have distribution restrictions, and some have only reporting requirements. Please see [docs.azul.com/core/tpl][9] for the links to the documents with licenses for third-party software included in the latest version of Azul Platform Core.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc., from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

[BSD 3-Clause Clear License][10]

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


  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre-headless/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre-headless/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19-jre-headless/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13-jre-headless/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21-jre-headless/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19-jre-headless/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19-jre-headless/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8-17.44.15-jre-headless/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre-headless/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19-jre-headless/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17-jre-headless/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19-jre-headless/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20-11.66.15-jre-headless/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre-headless/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre-headless/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15-jre-headless/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19-jre-headless/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21-jre-headless/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23-jre-headless/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u382-8.72.0.17-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19-jre/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13-jre/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21-jre/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19-jre/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8-17.44.15-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17-jre/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8.1-17.44.53-jre/Dockerfile
  
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17-jre/Dockerfile
  
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17-jre/Dockerfile
  
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19-jre/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17-jre/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19-jre/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20-11.66.15-jre/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20.1-11.66.19-jre/Dockerfile
  
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15-jre/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19-jre/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21-jre/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23-jre/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u382-8.72.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.15/Dockerfile
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.3-17.34.19/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4-17.36.13/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.5-17.38.21/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.6-17.40.19/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.7-17.42.19/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8-17.44.15/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.4.1-17.36.17/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.8.1-17.44.53/Dockerfile
  
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.3-15.32.15/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.4-15.34.17/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.5-15.36.13/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.6-15.38.17/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.10-15.46.17/Dockerfile
  
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.4-13.33.25/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.5-13.35.17/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.6-13.37.21/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.7-13.40.15/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.8-13.42.17/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.9-13.44.13/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.10-13.46.15/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.14-13.54.17/Dockerfile
  
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.4-11.33/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.5-11.35/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.6-11.37/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.7-11.39.15/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.8-11.41.23/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.9-11.43.21/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.10-11.45.27/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.11-11.48.21/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.12-11.50.19/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.13-11.52.13/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.14-11.54.23/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.17-11.60.19/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.18-11.62.17/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.19-11.64.19/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20-11.66.15/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.14.1-11.54.25/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.20.1-11.66.19/Dockerfile
  
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u07-9.0.7.1/Dockerfile
  
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u25-8.4.0.1/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u31-8.5.0.1/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u40-8.6.0.1/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u45-8.7.0.5/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u51-8.8.0.3/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u60-8.9.0.4/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u65-8.10.0.1/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u66-8.11.0.1/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u72-8.13.0.5/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u92-8.15.0.1/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u102-8.17.0.3/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u112-8.19.0.1/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u121-8.20.0.5/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u131-8.21.0.1/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u144-8.23.0.3/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u152-8.25.0.1/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u162-8.27.0.7/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u172-8.30.0.1/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u181-8.31.0.1/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u192-8.33.0.1/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u202-8.36.0.1/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u212-8.38.0.13/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u222-8.40.0.25/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u232-8.42.0.21/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u232-8.42.0.23/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u242-8.44.0.11/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u252-8.46.0.19/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u262-8.48.0.51/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u272-8.50.0.21/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u275-8.50.0.53/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u282-8.52.0.23/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u292-8.54.0.21/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u302-8.56.0.21/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u312-8.58.0.13/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u322-8.60.0.21/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u352-8.66.0.15/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.19/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u362-8.68.0.21/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u372-8.70.0.23/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u382-8.72.0.17/Dockerfile
  
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u72-7.7.0.1/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u76-7.8.0.3/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u79-7.9.0.2/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u80-7.10.0.1/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u85-7.11.0.3/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u91-7.12.0.3/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u95-7.13.0.1/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u101-7.14.0.5/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u111-7.15.0.1/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u121-7.16.0.1/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u131-7.17.0.5/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u141-7.18.0.3/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u154-7.20.0.3/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u161-7.21.0.3/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u171-7.22.0.3/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u181-7.23.0.1/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u191-7.24.0.1/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u201-7.25.0.5/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u211-7.27.0.1/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u222-7.29.0.5/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u232-7.31.0.5/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u242-7.34.0.5/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u252-7.36.0.5/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u262-7.38.0.11/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u272-7.40.0.15/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u282-7.42.0.13/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u285-7.42.0.51/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u292-7.44.0.11/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u302-7.46.0.11/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u312-7.48.0.11/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u322-7.50.0.11/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u332-7.52.0.11/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u342-7.54.0.13/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u352-7.56.0.11/Dockerfile
  
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u59-6.7.0.2/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u63-6.8.0.1/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u69-6.9.0.3/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u73-6.10.0.3/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u77-6.11.0.2/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u79-6.12.0.2/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u83-6.13.0.3/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u87-6.14.0.1/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u89-6.15.0.1/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u93-6.16.0.1/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u97-6.17.0.1/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u99-6.18.0.3/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u103-6.19.0.1/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u107-6.20.0.1/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u113-6.21.0.3/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u119-6.22.0.3/Dockerfile
  