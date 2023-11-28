Azul Zulu Ubuntu
================

These Docker images of Azul Zulu Build of OpenJDK are based on Ubuntu.

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


  * [`21.0.1-21.30.15`, `21-latest` (*21-latest/Dockerfile)*][11]
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][27]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][39]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][52]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][64]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][111]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][118]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][140]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][143]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][168]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][172]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][220]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][223]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][228]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][298]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][336]

Previous
--------

Earlier Ubuntu Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [21-jre-headless-latest][21],
  [21.0.1-21.30-jre-headless][24],
  [21.0.0-21.28.85-jre-headless][25],
  [21.0.1-21.30.15-jre-headless][26],
  
  * [20-jre-headless-latest][35],
  [20.0.0-20.28.85-jre-headless][36],
  [20.0.1-20.30.11-jre-headless][37],
  [20.0.2-20.32.11-jre-headless][38],
  
  * [19-jre-headless-latest][48],
  [19.0.0-19.28.81-jre-headless][49],
  [19.0.1-19.30.11-jre-headless][50],
  [19.0.2-19.32.13-jre-headless][51],
  
  * [18-jre-headless-latest][60],
  [18.0.1-18.30.11-jre-headless][61],
  [18.0.2-18.32.11-jre-headless][62],
  [18.0.2.1-18.32.13-jre-headless][63],
  
  * [17-jre-headless-latest][94],
  [17.0.9-17.46-jre-headless][97],
  [17.0.0-17.28.13-jre-headless][99],
  [17.0.1-17.30.15-jre-headless][100],
  [17.0.2-17.32.13-jre-headless][101],
  [17.0.3-17.34.19-jre-headless][102],
  [17.0.4-17.36.13-jre-headless][103],
  [17.0.5-17.38.21-jre-headless][104],
  [17.0.6-17.40.19-jre-headless][105],
  [17.0.7-17.42.19-jre-headless][106],
  [17.0.8-17.44.15-jre-headless][107],
  [17.0.9-17.46.19-jre-headless][108],
  [17.0.4.1-17.36.17-jre-headless][109],
  [17.0.8.1-17.44.53-jre-headless][110],
  
  * [15-jre-headless-latest][135],
  [15.0.7-15.40.19-jre-headless][136],
  [15.0.8-15.42.15-jre-headless][137],
  [15.0.9-15.44.13-jre-headless][138],
  [15.0.10-15.46.17-jre-headless][139],
  
  * [13-jre-headless-latest][163],
  [13.0.11-13.48.19-jre-headless][164],
  [13.0.12-13.50.15-jre-headless][165],
  [13.0.13-13.52.15-jre-headless][166],
  [13.0.14-13.54.17-jre-headless][167],
  
  * [11-jre-headless-latest][207],
  [11.0.21-11.68-jre-headless][210],
  [11.0.15-11.56.19-jre-headless][211],
  [11.0.16-11.58.15-jre-headless][212],
  [11.0.17-11.60.19-jre-headless][213],
  [11.0.18-11.62.17-jre-headless][214],
  [11.0.19-11.64.19-jre-headless][215],
  [11.0.20-11.66.15-jre-headless][216],
  [11.0.21-11.68.17-jre-headless][217],
  [11.0.16.1-11.58.23-jre-headless][218],
  [11.0.20.1-11.66.19-jre-headless][219],
  
  * [8-jre-headless-latest][287],
  [8u392-8.74-jre-headless][288],
  [8u332-8.62.0.19-jre-headless][289],
  [8u342-8.64.0.15-jre-headless][290],
  [8u345-8.64.0.19-jre-headless][291],
  [8u352-8.66.0.15-jre-headless][292],
  [8u362-8.68.0.19-jre-headless][293],
  [8u362-8.68.0.21-jre-headless][294],
  [8u372-8.70.0.23-jre-headless][295],
  [8u382-8.72.0.17-jre-headless][296],
  [8u392-8.74.0.17-jre-headless][297],
  
  * [21-jdk-crac-latest][17],
  [21.0.1-21.30-jdk-crac][20],
  [21.0.0-21.28.89-jdk-crac][22],
  [21.0.1-21.30.19-jdk-crac][23],
  
  * [17-jdk-crac-latest][80],
  [17.0.9-17.46-jdk-crac][93],
  [17.0.8-17.44.17-jdk-crac][95],
  [17.0.9-17.46.27-jdk-crac][96],
  [17.0.8.1-17.44.55-jdk-crac][98],
  
  * [21-jre-latest][13],
  [21.0.1-21.30-jre][16],
  [21.0.0-21.28.85-jre][18],
  [21.0.1-21.30.15-jre][19],
  
  * [20-jre-latest][28],
  [20.0.0-20.28.85-jre][32],
  [20.0.1-20.30.11-jre][33],
  [20.0.2-20.32.11-jre][34],
  
  * [19-jre-latest][40],
  [19.0.0-19.28.81-jre][45],
  [19.0.1-19.30.11-jre][46],
  [19.0.2-19.32.13-jre][47],
  
  * [18-jre-latest][53],
  [18.0.1-18.30.11-jre][57],
  [18.0.2-18.32.11-jre][58],
  [18.0.2.1-18.32.13-jre][59],
  
  * [17-jre-latest][66],
  [17.0.9-17.46-jre][77],
  [17.0.0-17.28.13-jre][81],
  [17.0.1-17.30.15-jre][82],
  [17.0.2-17.32.13-jre][83],
  [17.0.3-17.34.19-jre][84],
  [17.0.4-17.36.13-jre][85],
  [17.0.5-17.38.21-jre][86],
  [17.0.6-17.40.19-jre][87],
  [17.0.7-17.42.19-jre][88],
  [17.0.8-17.44.15-jre][89],
  [17.0.9-17.46.19-jre][90],
  [17.0.4.1-17.36.17-jre][91],
  [17.0.8.1-17.44.53-jre][92],
  
  * [16-jre-latest][112],
  [16.0.0-16.28.11-jre][115],
  [16.0.1-16.30.15-jre][116],
  [16.0.2-16.32.15-jre][117],
  
  * [15-jre-latest][119],
  [15.0.7-15.40.19-jre][131],
  [15.0.8-15.42.15-jre][132],
  [15.0.9-15.44.13-jre][133],
  [15.0.10-15.46.17-jre][134],
  
  * [13-jre-latest][146],
  [13.0.11-13.48.19-jre][159],
  [13.0.12-13.50.15-jre][160],
  [13.0.13-13.52.15-jre][161],
  [13.0.14-13.54.17-jre][162],
  
  * [11-jre-latest][179],
  [11.0.21-11.68-jre][196],
  [11.0.15-11.56.19-jre][200],
  [11.0.16-11.58.15-jre][201],
  [11.0.17-11.60.19-jre][202],
  [11.0.18-11.62.17-jre][203],
  [11.0.19-11.64.19-jre][204],
  [11.0.20-11.66.15-jre][205],
  [11.0.21-11.68.17-jre][206],
  [11.0.16.1-11.58.23-jre][208],
  [11.0.20.1-11.66.19-jre][209],
  
  * [8-jre-latest][230],
  [8u392-8.74-jre][255],
  [8u332-8.62.0.19-jre][278],
  [8u342-8.64.0.15-jre][279],
  [8u345-8.64.0.19-jre][280],
  [8u352-8.66.0.15-jre][281],
  [8u362-8.68.0.19-jre][282],
  [8u362-8.68.0.21-jre][283],
  [8u372-8.70.0.23-jre][284],
  [8u382-8.72.0.17-jre][285],
  [8u392-8.74.0.17-jre][286],
  
  * [21-latest][11],
  [21.0.1-21.30][12],
  [21.0.0-21.28.85][14],
  [21.0.1-21.30.15][15],
  
  * [20-latest][27],
  [20.0.0-20.28.85][29],
  [20.0.1-20.30.11][30],
  [20.0.2-20.32.11][31],
  
  * [19-latest][39],
  [19.0.0-19.28.81][41],
  [19.0.1-19.30.11][42],
  [19.0.2-19.32.13][43],
  [19.0.2-19.32.15][44],
  
  * [18-latest][52],
  [18.0.1-18.30.11][54],
  [18.0.2-18.32.11][55],
  [18.0.2.1-18.32.13][56],
  
  * [17-latest][64],
  [17.0.9-17.46][65],
  [17.0.0-17.28.13][67],
  [17.0.1-17.30.15][68],
  [17.0.2-17.32.13][69],
  [17.0.3-17.34.19][70],
  [17.0.4-17.36.13][71],
  [17.0.5-17.38.21][72],
  [17.0.6-17.40.19][73],
  [17.0.7-17.42.19][74],
  [17.0.8-17.44.15][75],
  [17.0.9-17.46.19][76],
  [17.0.4.1-17.36.17][78],
  [17.0.8.1-17.44.53][79],
  
  * [16-latest][111],
  [16.0.0-16.28.11][113],
  [16.0.2-16.32.15][114],
  
  * [15-latest][118],
  [15.0.1-15.28.13][120],
  [15.0.1-15.28.51][121],
  [15.0.2-15.29.15][122],
  [15.0.3-15.32.15][123],
  [15.0.4-15.34.17][124],
  [15.0.5-15.36.13][125],
  [15.0.6-15.38.17][126],
  [15.0.7-15.40.19][127],
  [15.0.8-15.42.15][128],
  [15.0.9-15.44.13][129],
  [15.0.10-15.46.17][130],
  
  * [14-latest][140],
  [14.0.1-14.28.21][141],
  [14.0.2-14.29.23][142],
  
  * [13-latest][143],
  [13.0.1-13.28][144],
  [13.0.2-13.29][145],
  [13.0.3-13.31.11][147],
  [13.0.4-13.33.25][148],
  [13.0.5-13.35.17][149],
  [13.0.6-13.37.21][150],
  [13.0.7-13.40.15][151],
  [13.0.8-13.42.17][152],
  [13.0.9-13.44.13][153],
  [13.0.10-13.46.15][154],
  [13.0.11-13.48.19][155],
  [13.0.12-13.50.15][156],
  [13.0.13-13.52.15][157],
  [13.0.14-13.54.17][158],
  
  * [12-12.1][168],
  [12-latest][169],
  [12.0.1-12.2][170],
  [12.0.2-12.3][171],
  
  * [11-latest][172],
  [11.0.1-11.2][173],
  [11.0.2-11.29][174],
  [11.0.3-11.31][175],
  [11.0.4-11.33][176],
  [11.0.5-11.35][177],
  [11.0.6-11.37][178],
  [11.0.21-11.68][180],
  [11.0.7-11.39.15][181],
  [11.0.8-11.41.23][182],
  [11.0.9-11.43.21][183],
  [11.0.10-11.45.27][184],
  [11.0.11-11.48.21][185],
  [11.0.12-11.50.19][186],
  [11.0.13-11.52.13][187],
  [11.0.14-11.54.23][188],
  [11.0.15-11.56.19][189],
  [11.0.16-11.58.15][190],
  [11.0.17-11.60.19][191],
  [11.0.18-11.62.17][192],
  [11.0.19-11.64.19][193],
  [11.0.20-11.66.15][194],
  [11.0.21-11.68.17][195],
  [11.0.14.1-11.54.25][197],
  [11.0.16.1-11.58.23][198],
  [11.0.20.1-11.66.19][199],
  
  * [10-latest][220],
  [10u01-10.2][221],
  [10u02-10.3][222],
  
  * [9-ea][223],
  [9-latest][224],
  [9u01-9.0.1.3][225],
  [9u04-9.0.4.1][226],
  [9u07-9.0.7.1][227],
  
  * [8-latest][228],
  [8u392-8.74][229],
  [8u05-8.1.0.6][231],
  [8u11-8.2.0.1][232],
  [8u20-8.3.0.1][233],
  [8u25-8.4.0.1][234],
  [8u31-8.5.0.1][235],
  [8u40-8.6.0.1][236],
  [8u45-8.7.0.5][237],
  [8u51-8.8.0.3][238],
  [8u60-8.9.0.4][239],
  [8u65-8.10.0.1][240],
  [8u66-8.11.0.1][241],
  [8u72-8.13.0.5][242],
  [8u92-8.15.0.1][243],
  [8u102-8.17.0.3][244],
  [8u112-8.19.0.1][245],
  [8u121-8.20.0.5][246],
  [8u131-8.21.0.1][247],
  [8u144-8.23.0.3][248],
  [8u152-8.25.0.1][249],
  [8u162-8.27.0.7][250],
  [8u172-8.30.0.1][251],
  [8u181-8.31.0.1][252],
  [8u192-8.33.0.1][253],
  [8u202-8.36.0.1][254],
  [8u212-8.38.0.13][256],
  [8u222-8.40.0.25][257],
  [8u232-8.42.0.21][258],
  [8u232-8.42.0.23][259],
  [8u242-8.44.0.11][260],
  [8u252-8.46.0.19][261],
  [8u262-8.48.0.51][262],
  [8u272-8.50.0.21][263],
  [8u275-8.50.0.53][264],
  [8u282-8.52.0.23][265],
  [8u302-8.56.0.21][266],
  [8u312-8.58.0.13][267],
  [8u322-8.60.0.21][268],
  [8u332-8.62.0.19][269],
  [8u342-8.64.0.15][270],
  [8u345-8.64.0.19][271],
  [8u352-8.66.0.15][272],
  [8u362-8.68.0.19][273],
  [8u362-8.68.0.21][274],
  [8u372-8.70.0.23][275],
  [8u382-8.72.0.17][276],
  [8u392-8.74.0.17][277],
  
  * [7-latest][298],
  [7u55-7.4.0.5][299],
  [7u60-7.5.0.1][300],
  [7u65-7.6.0.1][301],
  [7u72-7.7.0.1][302],
  [7u76-7.8.0.3][303],
  [7u79-7.9.0.2][304],
  [7u80-7.10.0.1][305],
  [7u85-7.11.0.3][306],
  [7u91-7.12.0.3][307],
  [7u95-7.13.0.1][308],
  [7u101-7.14.0.5][309],
  [7u111-7.15.0.1][310],
  [7u121-7.16.0.1][311],
  [7u131-7.17.0.5][312],
  [7u141-7.18.0.3][313],
  [7u154-7.20.0.3][314],
  [7u161-7.21.0.3][315],
  [7u171-7.22.0.3][316],
  [7u181-7.23.0.1][317],
  [7u191-7.24.0.1][318],
  [7u201-7.25.0.5][319],
  [7u211-7.27.0.1][320],
  [7u222-7.29.0.5][321],
  [7u232-7.31.0.5][322],
  [7u242-7.34.0.5][323],
  [7u252-7.36.0.5][324],
  [7u262-7.38.0.11][325],
  [7u272-7.40.0.15][326],
  [7u282-7.42.0.13][327],
  [7u285-7.42.0.51][328],
  [7u292-7.44.0.11][329],
  [7u302-7.46.0.11][330],
  [7u312-7.48.0.11][331],
  [7u322-7.50.0.11][332],
  [7u332-7.52.0.11][333],
  [7u342-7.54.0.13][334],
  [7u352-7.56.0.11][335],
  
  * [6-latest][336],
  [6u49-6.4.0.6][337],
  [6u53-6.5.0.2][338],
  [6u56-6.6.0.1][339],
  [6u59-6.7.0.2][340],
  [6u63-6.8.0.1][341],
  [6u69-6.9.0.3][342],
  [6u73-6.10.0.3][343],
  [6u77-6.11.0.2][344],
  [6u79-6.12.0.2][345],
  [6u83-6.13.0.3][346],
  [6u87-6.14.0.1][347],
  [6u89-6.15.0.1][348],
  [6u93-6.16.0.1][349],
  [6u97-6.17.0.1][350],
  [6u99-6.18.0.3][351],
  [6u103-6.19.0.1][352],
  [6u107-6.20.0.1][353],
  [6u113-6.21.0.3][354],
  [6u119-6.22.0.3][355],
  


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


  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.15-jre-headless/Dockerfile
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre-headless/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre-headless/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre-headless/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.2-17.32.13-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.3-17.34.19-jre-headless/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4-17.36.13-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.5-17.38.21-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.6-17.40.19-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.7-17.42.19-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.15-jre-headless/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46.19-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre-headless/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre-headless/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16-11.58.15-jre-headless/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.17-11.60.19-jre-headless/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.18-11.62.17-jre-headless/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.19-11.64.19-jre-headless/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20-11.66.15-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68.17-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre-headless/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre-headless/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u345-8.64.0.19-jre-headless/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u352-8.66.0.15-jre-headless/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.19-jre-headless/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.21-jre-headless/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u372-8.70.0.23-jre-headless/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u382-8.72.0.17-jre-headless/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74.0.17-jre-headless/Dockerfile
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jdk-crac/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.89-jdk-crac/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.19-jdk-crac/Dockerfile
  
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jdk-crac/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.17-jdk-crac/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46.27-jdk-crac/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8.1-17.44.55-jdk-crac/Dockerfile
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.15-jre/Dockerfile
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre/Dockerfile
  
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.2-17.32.13-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.3-17.34.19-jre/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4-17.36.13-jre/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.5-17.38.21-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.6-17.40.19-jre/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.7-17.42.19-jre/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.15-jre/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46.19-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4.1-17.36.17-jre/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8.1-17.44.53-jre/Dockerfile
  
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15-jre/Dockerfile
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.10-15.46.17-jre/Dockerfile
  
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.14-13.54.17-jre/Dockerfile
  
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16-11.58.15-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.17-11.60.19-jre/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.18-11.62.17-jre/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.19-11.64.19-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20-11.66.15-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68.17-jre/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20.1-11.66.19-jre/Dockerfile
  
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u345-8.64.0.19-jre/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u352-8.66.0.15-jre/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.19-jre/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.21-jre/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u372-8.70.0.23-jre/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u382-8.72.0.17-jre/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.15/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11/Dockerfile
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.15/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.2-17.32.13/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.3-17.34.19/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4-17.36.13/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.5-17.38.21/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.6-17.40.19/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.7-17.42.19/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.15/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46.19/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.4.1-17.36.17/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8.1-17.44.53/Dockerfile
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.2-15.29.15/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.3-15.32.15/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.4-15.34.17/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.5-15.36.13/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.6-15.38.17/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.10-15.46.17/Dockerfile
  
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.3-13.31.11/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.4-13.33.25/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.5-13.35.17/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.6-13.37.21/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.7-13.40.15/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.8-13.42.17/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.9-13.44.13/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.10-13.46.15/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.14-13.54.17/Dockerfile
  
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-12.1/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.3-11.31/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.4-11.33/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.5-11.35/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.6-11.37/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.7-11.39.15/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.8-11.41.23/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.9-11.43.21/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.10-11.45.27/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.11-11.48.21/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.12-11.50.19/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.13-11.52.13/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.14-11.54.23/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16-11.58.15/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.17-11.60.19/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.18-11.62.17/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.19-11.64.19/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20-11.66.15/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68.17/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.14.1-11.54.25/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.20.1-11.66.19/Dockerfile
  
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u04-9.0.4.1/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u07-9.0.7.1/Dockerfile
  
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u11-8.2.0.1/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u20-8.3.0.1/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u25-8.4.0.1/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u31-8.5.0.1/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u40-8.6.0.1/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u45-8.7.0.5/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u51-8.8.0.3/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u60-8.9.0.4/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u65-8.10.0.1/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u66-8.11.0.1/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u72-8.13.0.5/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u92-8.15.0.1/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u102-8.17.0.3/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u112-8.19.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u121-8.20.0.5/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u131-8.21.0.1/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u144-8.23.0.3/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u152-8.25.0.1/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u162-8.27.0.7/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u172-8.30.0.1/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u181-8.31.0.1/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u192-8.33.0.1/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u202-8.36.0.1/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u212-8.38.0.13/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u222-8.40.0.25/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u232-8.42.0.21/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u232-8.42.0.23/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u242-8.44.0.11/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u252-8.46.0.19/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u262-8.48.0.51/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u272-8.50.0.21/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u275-8.50.0.53/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u282-8.52.0.23/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u302-8.56.0.21/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u312-8.58.0.13/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u322-8.60.0.21/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u345-8.64.0.19/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u352-8.66.0.15/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.19/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u362-8.68.0.21/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u372-8.70.0.23/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u382-8.72.0.17/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74.0.17/Dockerfile
  
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u65-7.6.0.1/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u72-7.7.0.1/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u76-7.8.0.3/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u79-7.9.0.2/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u80-7.10.0.1/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u85-7.11.0.3/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u91-7.12.0.3/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u95-7.13.0.1/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u101-7.14.0.5/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u111-7.15.0.1/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u121-7.16.0.1/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u131-7.17.0.5/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u141-7.18.0.3/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u154-7.20.0.3/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u161-7.21.0.3/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u171-7.22.0.3/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u181-7.23.0.1/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u191-7.24.0.1/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u201-7.25.0.5/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u211-7.27.0.1/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u222-7.29.0.5/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u232-7.31.0.5/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u242-7.34.0.5/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u252-7.36.0.5/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u262-7.38.0.11/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u272-7.40.0.15/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u282-7.42.0.13/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u285-7.42.0.51/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u292-7.44.0.11/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u302-7.46.0.11/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u312-7.48.0.11/Dockerfile
  [332]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u322-7.50.0.11/Dockerfile
  [333]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u332-7.52.0.11/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u342-7.54.0.13/Dockerfile
  [335]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u352-7.56.0.11/Dockerfile
  
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [338]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  [339]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u56-6.6.0.1/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u59-6.7.0.2/Dockerfile
  [341]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u63-6.8.0.1/Dockerfile
  [342]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u69-6.9.0.3/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u73-6.10.0.3/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u77-6.11.0.2/Dockerfile
  [345]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u79-6.12.0.2/Dockerfile
  [346]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u83-6.13.0.3/Dockerfile
  [347]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u87-6.14.0.1/Dockerfile
  [348]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u89-6.15.0.1/Dockerfile
  [349]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u93-6.16.0.1/Dockerfile
  [350]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u97-6.17.0.1/Dockerfile
  [351]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u99-6.18.0.3/Dockerfile
  [352]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u103-6.19.0.1/Dockerfile
  [353]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u107-6.20.0.1/Dockerfile
  [354]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u113-6.21.0.3/Dockerfile
  [355]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u119-6.22.0.3/Dockerfile
  