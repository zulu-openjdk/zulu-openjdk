Azul Zulu CentOS
================

These Docker images of Azul Zulu Build of OpenJDK are based on CentOS.

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
   * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][26]
   * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][38]
   * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][51]
   * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][63]
   * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][108]
   * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][116]
   * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][139]
   * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][142]
   * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][167]
   * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][171]
   * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][222]
   * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][225]
   * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][230]
   * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][303]
   * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][338]

Previous
--------

Earlier CentOS Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [21-jre-headless-latest][21],
  [21.0.1-21.30-jre-headless][22],
  [21.0.2-21.32-jre-headless][23],
  [21.0.0-21.28.85-jre-headless][24],
  [21.0.1-21.30.15-jre-headless][25],
  
  * [20-jre-headless-latest][34],
  [20.0.0-20.28.85-jre-headless][35],
  [20.0.1-20.30.11-jre-headless][36],
  [20.0.2-20.32.11-jre-headless][37],
  
  * [19-jre-headless-latest][47],
  [19.0.0-19.28.81-jre-headless][48],
  [19.0.1-19.30.11-jre-headless][49],
  [19.0.2-19.32.13-jre-headless][50],
  
  * [18-jre-headless-latest][59],
  [18.0.1-18.30.11-jre-headless][60],
  [18.0.2-18.32.11-jre-headless][61],
  [18.0.2.1-18.32.13-jre-headless][62],
  
  * [17-jre-headless-latest][93],
  [17.0.9-17.46-jre-headless][94],
  [17.0.10-17.48-jre-headless][95],
  [17.0.0-17.28.13-jre-headless][96],
  [17.0.1-17.30.15-jre-headless][97],
  [17.0.2-17.32.13-jre-headless][98],
  [17.0.3-17.34.19-jre-headless][99],
  [17.0.4-17.36.13-jre-headless][100],
  [17.0.5-17.38.21-jre-headless][101],
  [17.0.6-17.40.19-jre-headless][102],
  [17.0.7-17.42.19-jre-headless][103],
  [17.0.8-17.44.15-jre-headless][104],
  [17.0.9-17.46.19-jre-headless][105],
  [17.0.4.1-17.36.17-jre-headless][106],
  [17.0.8.1-17.44.53-jre-headless][107],
  
  * [15-jre-headless-latest][134],
  [15.0.7-15.40.19-jre-headless][135],
  [15.0.8-15.42.15-jre-headless][136],
  [15.0.9-15.44.13-jre-headless][137],
  [15.0.10-15.46.17-jre-headless][138],
  
  * [13-jre-headless-latest][162],
  [13.0.11-13.48.19-jre-headless][163],
  [13.0.12-13.50.15-jre-headless][164],
  [13.0.13-13.52.15-jre-headless][165],
  [13.0.14-13.54.17-jre-headless][166],
  
  * [11-jre-headless-latest][208],
  [11.0.21-11.68-jre-headless][211],
  [11.0.22-11.70-jre-headless][212],
  [11.0.15-11.56.19-jre-headless][213],
  [11.0.16-11.58.15-jre-headless][214],
  [11.0.17-11.60.19-jre-headless][215],
  [11.0.18-11.62.17-jre-headless][216],
  [11.0.19-11.64.19-jre-headless][217],
  [11.0.20-11.66.15-jre-headless][218],
  [11.0.21-11.68.17-jre-headless][219],
  [11.0.16.1-11.58.23-jre-headless][220],
  [11.0.20.1-11.66.19-jre-headless][221],
  
  * [8-jre-headless-latest][291],
  [8u392-8.74-jre-headless][292],
  [8u402-8.76-jre-headless][293],
  [8u332-8.62.0.19-jre-headless][294],
  [8u342-8.64.0.15-jre-headless][295],
  [8u345-8.64.0.19-jre-headless][296],
  [8u352-8.66.0.15-jre-headless][297],
  [8u362-8.68.0.19-jre-headless][298],
  [8u362-8.68.0.21-jre-headless][299],
  [8u372-8.70.0.23-jre-headless][300],
  [8u382-8.72.0.17-jre-headless][301],
  [8u392-8.74.0.17-jre-headless][302],
  
  * [21-jre-latest][14],
  [21.0.1-21.30-jre][17],
  [21.0.2-21.32-jre][18],
  [21.0.0-21.28.85-jre][19],
  [21.0.1-21.30.15-jre][20],
  
  * [20-jre-latest][27],
  [20.0.0-20.28.85-jre][31],
  [20.0.1-20.30.11-jre][32],
  [20.0.2-20.32.11-jre][33],
  
  * [19-jre-latest][39],
  [19.0.0-19.28.81-jre][44],
  [19.0.1-19.30.11-jre][45],
  [19.0.2-19.32.13-jre][46],
  
  * [18-jre-latest][52],
  [18.0.1-18.30.11-jre][56],
  [18.0.2-18.32.11-jre][57],
  [18.0.2.1-18.32.13-jre][58],
  
  * [17-jre-latest][65],
  [17.0.9-17.46-jre][77],
  [17.0.10-17.48-jre][78],
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
  
  * [16-jre-latest][109],
  [16.0.0-16.28.11-jre][113],
  [16.0.1-16.30.15-jre][114],
  [16.0.2-16.32.15-jre][115],
  
  * [15-jre-latest][117],
  [15.0.7-15.40.19-jre][130],
  [15.0.8-15.42.15-jre][131],
  [15.0.9-15.44.13-jre][132],
  [15.0.10-15.46.17-jre][133],
  
  * [13-jre-latest][145],
  [13.0.11-13.48.19-jre][158],
  [13.0.12-13.50.15-jre][159],
  [13.0.13-13.52.15-jre][160],
  [13.0.14-13.54.17-jre][161],
  
  * [11-jre-latest][178],
  [11.0.21-11.68-jre][196],
  [11.0.22-11.70-jre][197],
  [11.0.15-11.56.19-jre][201],
  [11.0.16-11.58.15-jre][202],
  [11.0.17-11.60.19-jre][203],
  [11.0.18-11.62.17-jre][204],
  [11.0.19-11.64.19-jre][205],
  [11.0.20-11.66.15-jre][206],
  [11.0.21-11.68.17-jre][207],
  [11.0.16.1-11.58.23-jre][209],
  [11.0.20.1-11.66.19-jre][210],
  
  * [8-jre-latest][233],
  [8u392-8.74-jre][257],
  [8u402-8.76-jre][258],
  [8u332-8.62.0.19-jre][282],
  [8u342-8.64.0.15-jre][283],
  [8u345-8.64.0.19-jre][284],
  [8u352-8.66.0.15-jre][285],
  [8u362-8.68.0.19-jre][286],
  [8u362-8.68.0.21-jre][287],
  [8u372-8.70.0.23-jre][288],
  [8u382-8.72.0.17-jre][289],
  [8u392-8.74.0.17-jre][290],
  
  * [21-latest][11],
  [21.0.1-21.30][12],
  [21.0.2-21.32][13],
  [21.0.0-21.28.85][15],
  [21.0.1-21.30.15][16],
  
  * [20-latest][26],
  [20.0.0-20.28.85][28],
  [20.0.1-20.30.11][29],
  [20.0.2-20.32.11][30],
  
  * [19-latest][38],
  [19.0.0-19.28.81][40],
  [19.0.1-19.30.11][41],
  [19.0.2-19.32.13][42],
  [19.0.2-19.32.15][43],
  
  * [18-latest][51],
  [18.0.1-18.30.11][53],
  [18.0.2-18.32.11][54],
  [18.0.2.1-18.32.13][55],
  
  * [17-latest][63],
  [17.0.9-17.46][64],
  [17.0.10-17.48][66],
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
  [17.0.4.1-17.36.17][79],
  [17.0.8.1-17.44.53][80],
  
  * [16-latest][108],
  [16.0.0-16.28.11][110],
  [16.0.1-16.30.15][111],
  [16.0.2-16.32.15][112],
  
  * [15-latest][116],
  [15.0.0-15.27.17][118],
  [15.0.1-15.28.13][119],
  [15.0.1-15.28.51][120],
  [15.0.2-15.29.15][121],
  [15.0.3-15.32.15][122],
  [15.0.4-15.34.17][123],
  [15.0.5-15.36.13][124],
  [15.0.6-15.38.17][125],
  [15.0.7-15.40.19][126],
  [15.0.8-15.42.15][127],
  [15.0.9-15.44.13][128],
  [15.0.10-15.46.17][129],
  
  * [14-latest][139],
  [14.0.1-14.28.21][140],
  [14.0.2-14.29.23][141],
  
  * [13-latest][142],
  [13.0.1-13.28][143],
  [13.0.2-13.29][144],
  [13.0.3-13.31.11][146],
  [13.0.4-13.33.25][147],
  [13.0.5-13.35.17][148],
  [13.0.6-13.37.21][149],
  [13.0.7-13.40.15][150],
  [13.0.8-13.42.17][151],
  [13.0.9-13.44.13][152],
  [13.0.10-13.46.15][153],
  [13.0.11-13.48.19][154],
  [13.0.12-13.50.15][155],
  [13.0.13-13.52.15][156],
  [13.0.14-13.54.17][157],
  
  * [12-12.1][167],
  [12-latest][168],
  [12.0.1-12.2][169],
  [12.0.2-12.3][170],
  
  * [11-latest][171],
  [11.0.1-11.2][172],
  [11.0.2-11.29][173],
  [11.0.3-11.31][174],
  [11.0.4-11.33][175],
  [11.0.5-11.35][176],
  [11.0.6-11.37][177],
  [11.0.21-11.68][179],
  [11.0.22-11.70][180],
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
  [11.0.14.1-11.54.25][198],
  [11.0.16.1-11.58.23][199],
  [11.0.20.1-11.66.19][200],
  
  * [10-latest][222],
  [10u01-10.2][223],
  [10u02-10.3][224],
  
  * [9-ea][225],
  [9-latest][226],
  [9u01-9.0.1.3][227],
  [9u04-9.0.4.1][228],
  [9u07-9.0.7.1][229],
  
  * [8-latest][230],
  [8u392-8.74][231],
  [8u402-8.76][232],
  [8u11-8.2.0.1][234],
  [8u20-8.3.0.1][235],
  [8u25-8.4.0.1][236],
  [8u31-8.5.0.1][237],
  [8u40-8.6.0.1][238],
  [8u45-8.7.0.5][239],
  [8u51-8.8.0.3][240],
  [8u60-8.9.0.4][241],
  [8u65-8.10.0.1][242],
  [8u66-8.11.0.1][243],
  [8u72-8.13.0.5][244],
  [8u92-8.15.0.1][245],
  [8u102-8.17.0.7][246],
  [8u112-8.19.0.1][247],
  [8u121-8.20.0.5][248],
  [8u131-8.21.0.1][249],
  [8u144-8.23.0.3][250],
  [8u152-8.25.0.1][251],
  [8u162-8.27.0.7][252],
  [8u172-8.30.0.1][253],
  [8u181-8.31.0.1][254],
  [8u192-8.33.0.1][255],
  [8u202-8.36.0.1][256],
  [8u212-8.38.0.13][259],
  [8u222-8.40.0.25][260],
  [8u232-8.42.0.21][261],
  [8u232-8.42.0.23][262],
  [8u242-8.44.0.11][263],
  [8u252-8.46.0.19][264],
  [8u262-8.48.0.51][265],
  [8u272-8.50.0.21][266],
  [8u275-8.50.0.53][267],
  [8u282-8.52.0.23][268],
  [8u292-8.54.0.21][269],
  [8u302-8.56.0.21][270],
  [8u312-8.58.0.13][271],
  [8u322-8.60.0.21][272],
  [8u332-8.62.0.19][273],
  [8u342-8.64.0.15][274],
  [8u345-8.64.0.19][275],
  [8u352-8.66.0.15][276],
  [8u362-8.68.0.19][277],
  [8u362-8.68.0.21][278],
  [8u372-8.70.0.23][279],
  [8u382-8.72.0.17][280],
  [8u392-8.74.0.17][281],
  
  * [7-latest][303],
  [7u65-7.6.0.1][304],
  [7u72-7.7.0.1][305],
  [7u76-7.8.0.3][306],
  [7u79-7.9.0.2][307],
  [7u80-7.10.0.1][308],
  [7u85-7.11.0.3][309],
  [7u91-7.12.0.3][310],
  [7u95-7.13.0.1][311],
  [7u101-7.14.0.5][312],
  [7u111-7.15.0.5][313],
  [7u121-7.16.0.1][314],
  [7u131-7.17.0.5][315],
  [7u141-7.18.0.3][316],
  [7u154-7.20.0.3][317],
  [7u161-7.21.0.3][318],
  [7u171-7.22.0.3][319],
  [7u181-7.23.0.1][320],
  [7u191-7.24.0.1][321],
  [7u201-7.25.0.5][322],
  [7u211-7.27.0.1][323],
  [7u222-7.29.0.5][324],
  [7u232-7.31.0.5][325],
  [7u242-7.34.0.5][326],
  [7u252-7.36.0.5][327],
  [7u262-7.38.0.11][328],
  [7u272-7.40.0.15][329],
  [7u282-7.42.0.13][330],
  [7u285-7.42.0.51][331],
  [7u292-7.44.0.11][332],
  [7u302-7.46.0.11][333],
  [7u312-7.48.0.11][334],
  [7u332-7.52.0.11][335],
  [7u342-7.54.0.13][336],
  [7u352-7.56.0.11][337],
  
  * [6-latest][338],
  [6u53-6.5.0.2][339],
  [6u56-6.6.0.1][340],
  [6u59-6.7.0.2][341],
  [6u63-6.8.0.1][342],
  [6u69-6.9.0.3][343],
  [6u73-6.10.0.3][344],
  [6u77-6.11.0.2][345],
  [6u79-6.12.0.2][346],
  [6u83-6.13.0.7][347],
  [6u87-6.14.0.1][348],
  [6u89-6.15.0.1][349],
  [6u93-6.16.0.1][350],
  [6u97-6.17.0.1][351],
  [6u99-6.18.0.3][352],
  [6u103-6.19.0.1][353],
  [6u107-6.20.0.1][354],
  [6u113-6.21.0.3][355],
  [6u119-6.22.0.3][356],
  

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


  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-headless-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre-headless/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32-jre-headless/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre-headless/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15-jre-headless/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-headless-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre-headless/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre-headless/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-headless-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre-headless/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-headless-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre-headless/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-headless-latest/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre-headless/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48-jre-headless/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre-headless/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre-headless/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13-jre-headless/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19-jre-headless/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13-jre-headless/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19-jre-headless/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-headless-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre-headless/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre-headless/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre-headless/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-headless-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre-headless/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre-headless/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre-headless/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-headless-latest/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre-headless/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.22-11.70-jre-headless/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre-headless/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15-jre-headless/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19-jre-headless/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17-jre-headless/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-headless-latest/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre-headless/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76-jre-headless/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre-headless/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre-headless/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19-jre-headless/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15-jre-headless/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19-jre-headless/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21-jre-headless/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23-jre-headless/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17-jre-headless/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17-jre-headless/Dockerfile
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32-jre/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15-jre/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-latest/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre/Dockerfile
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19-jre/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13-jre/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19-jre/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19-jre/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15-jre/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17-jre/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53-jre/Dockerfile
  
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-jre-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11-jre/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15-jre/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15-jre/Dockerfile
  
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-latest/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17-jre/Dockerfile
  
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-latest/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17-jre/Dockerfile
  
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-latest/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.22-11.70-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15-jre/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19-jre/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15-jre/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17-jre/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19-jre/Dockerfile
  
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-latest/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76-jre/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19-jre/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15-jre/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19-jre/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21-jre/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23-jre/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17-jre/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11/Dockerfile
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.15/Dockerfile
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53/Dockerfile
  
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-latest/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15/Dockerfile
  
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-latest/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.0-15.27.17/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.13/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.51/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.2-15.29.15/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.3-15.32.15/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.4-15.34.17/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.5-15.36.13/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.6-15.38.17/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17/Dockerfile
  
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14-latest/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.1-14.28.21/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.2-14.29.23/Dockerfile
  
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-latest/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.1-13.28/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.2-13.29/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.3-13.31.11/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.4-13.33.25/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.5-13.35.17/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.6-13.37.21/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.7-13.40.15/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.8-13.42.17/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.9-13.44.13/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.10-13.46.15/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17/Dockerfile
  
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-12.1/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-latest/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.1-12.2/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.2-12.3/Dockerfile
  
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-latest/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.1-11.2/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.2-11.29/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.3-11.31/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.4-11.33/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.5-11.35/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.6-11.37/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.22-11.70/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.7-11.39.15/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.8-11.41.23/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.9-11.43.21/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.10-11.45.27/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.11-11.48.21/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.12-11.50.19/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.13-11.52.13/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.14-11.54.23/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.14.1-11.54.25/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19/Dockerfile
  
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10-latest/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u01-10.2/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u02-10.3/Dockerfile
  
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-ea/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-latest/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u01-9.0.1.3/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u04-9.0.4.1/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u07-9.0.7.1/Dockerfile
  
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-latest/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u11-8.2.0.1/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u20-8.3.0.1/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u25-8.4.0.1/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u31-8.5.0.1/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u40-8.6.0.1/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u45-8.7.0.5/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u51-8.8.0.3/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u60-8.9.0.4/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u65-8.10.0.1/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u66-8.11.0.1/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u72-8.13.0.5/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u92-8.15.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u102-8.17.0.7/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u112-8.19.0.1/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u121-8.20.0.5/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u131-8.21.0.1/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u144-8.23.0.3/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u152-8.25.0.1/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u162-8.27.0.7/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u172-8.30.0.1/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u181-8.31.0.1/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u192-8.33.0.1/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u202-8.36.0.1/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u212-8.38.0.13/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u222-8.40.0.25/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u232-8.42.0.21/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u232-8.42.0.23/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u242-8.44.0.11/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u252-8.46.0.19/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u262-8.48.0.51/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u272-8.50.0.21/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u275-8.50.0.53/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u282-8.52.0.23/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u292-8.54.0.21/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u302-8.56.0.21/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u312-8.58.0.13/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u322-8.60.0.21/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17/Dockerfile
  
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7-latest/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u79-7.9.0.2/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u80-7.10.0.1/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u85-7.11.0.3/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u91-7.12.0.3/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u95-7.13.0.1/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u101-7.14.0.5/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u111-7.15.0.5/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u121-7.16.0.1/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u131-7.17.0.5/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u141-7.18.0.3/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u154-7.20.0.3/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u161-7.21.0.3/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u171-7.22.0.3/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u181-7.23.0.1/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u191-7.24.0.1/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u201-7.25.0.5/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u211-7.27.0.1/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u222-7.29.0.5/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u232-7.31.0.5/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u242-7.34.0.5/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u252-7.36.0.5/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u262-7.38.0.11/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u272-7.40.0.15/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u282-7.42.0.13/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u285-7.42.0.51/Dockerfile
  [332]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u292-7.44.0.11/Dockerfile
  [333]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u302-7.46.0.11/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u312-7.48.0.11/Dockerfile
  [335]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u332-7.52.0.11/Dockerfile
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u342-7.54.0.13/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u352-7.56.0.11/Dockerfile
  
  [338]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6-latest/Dockerfile
  [339]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [341]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  [342]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u63-6.8.0.1/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u69-6.9.0.3/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u73-6.10.0.3/Dockerfile
  [345]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u77-6.11.0.2/Dockerfile
  [346]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u79-6.12.0.2/Dockerfile
  [347]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u83-6.13.0.7/Dockerfile
  [348]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u87-6.14.0.1/Dockerfile
  [349]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u89-6.15.0.1/Dockerfile
  [350]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u93-6.16.0.1/Dockerfile
  [351]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u97-6.17.0.1/Dockerfile
  [352]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u99-6.18.0.3/Dockerfile
  [353]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u103-6.19.0.1/Dockerfile
  [354]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u107-6.20.0.1/Dockerfile
  [355]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u113-6.21.0.3/Dockerfile
  [356]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u119-6.22.0.3/Dockerfile
  