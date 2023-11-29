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
   * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][23]
   * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][35]
   * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][48]
   * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][60]
   * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][102]
   * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][110]
   * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][133]
   * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][136]
   * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][161]
   * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][165]
   * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][213]
   * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][216]
   * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][221]
   * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][291]
   * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][326]

Previous
--------

Earlier CentOS Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [21-jre-headless-latest][19],
  [21.0.1-21.30-jre-headless][20],
  [21.0.0-21.28.85-jre-headless][21],
  [21.0.1-21.30.15-jre-headless][22],
  
  * [20-jre-headless-latest][31],
  [20.0.0-20.28.85-jre-headless][32],
  [20.0.1-20.30.11-jre-headless][33],
  [20.0.2-20.32.11-jre-headless][34],
  
  * [19-jre-headless-latest][44],
  [19.0.0-19.28.81-jre-headless][45],
  [19.0.1-19.30.11-jre-headless][46],
  [19.0.2-19.32.13-jre-headless][47],
  
  * [18-jre-headless-latest][56],
  [18.0.1-18.30.11-jre-headless][57],
  [18.0.2-18.32.11-jre-headless][58],
  [18.0.2.1-18.32.13-jre-headless][59],
  
  * [17-jre-headless-latest][88],
  [17.0.9-17.46-jre-headless][89],
  [17.0.0-17.28.13-jre-headless][90],
  [17.0.1-17.30.15-jre-headless][91],
  [17.0.2-17.32.13-jre-headless][92],
  [17.0.3-17.34.19-jre-headless][93],
  [17.0.4-17.36.13-jre-headless][94],
  [17.0.5-17.38.21-jre-headless][95],
  [17.0.6-17.40.19-jre-headless][96],
  [17.0.7-17.42.19-jre-headless][97],
  [17.0.8-17.44.15-jre-headless][98],
  [17.0.9-17.46.19-jre-headless][99],
  [17.0.4.1-17.36.17-jre-headless][100],
  [17.0.8.1-17.44.53-jre-headless][101],
  
  * [15-jre-headless-latest][128],
  [15.0.7-15.40.19-jre-headless][129],
  [15.0.8-15.42.15-jre-headless][130],
  [15.0.9-15.44.13-jre-headless][131],
  [15.0.10-15.46.17-jre-headless][132],
  
  * [13-jre-headless-latest][156],
  [13.0.11-13.48.19-jre-headless][157],
  [13.0.12-13.50.15-jre-headless][158],
  [13.0.13-13.52.15-jre-headless][159],
  [13.0.14-13.54.17-jre-headless][160],
  
  * [11-jre-headless-latest][200],
  [11.0.21-11.68-jre-headless][203],
  [11.0.15-11.56.19-jre-headless][204],
  [11.0.16-11.58.15-jre-headless][205],
  [11.0.17-11.60.19-jre-headless][206],
  [11.0.18-11.62.17-jre-headless][207],
  [11.0.19-11.64.19-jre-headless][208],
  [11.0.20-11.66.15-jre-headless][209],
  [11.0.21-11.68.17-jre-headless][210],
  [11.0.16.1-11.58.23-jre-headless][211],
  [11.0.20.1-11.66.19-jre-headless][212],
  
  * [8-jre-headless-latest][280],
  [8u392-8.74-jre-headless][281],
  [8u332-8.62.0.19-jre-headless][282],
  [8u342-8.64.0.15-jre-headless][283],
  [8u345-8.64.0.19-jre-headless][284],
  [8u352-8.66.0.15-jre-headless][285],
  [8u362-8.68.0.19-jre-headless][286],
  [8u362-8.68.0.21-jre-headless][287],
  [8u372-8.70.0.23-jre-headless][288],
  [8u382-8.72.0.17-jre-headless][289],
  [8u392-8.74.0.17-jre-headless][290],
  
  * [21-jre-latest][13],
  [21.0.1-21.30-jre][16],
  [21.0.0-21.28.85-jre][17],
  [21.0.1-21.30.15-jre][18],
  
  * [20-jre-latest][24],
  [20.0.0-20.28.85-jre][28],
  [20.0.1-20.30.11-jre][29],
  [20.0.2-20.32.11-jre][30],
  
  * [19-jre-latest][36],
  [19.0.0-19.28.81-jre][41],
  [19.0.1-19.30.11-jre][42],
  [19.0.2-19.32.13-jre][43],
  
  * [18-jre-latest][49],
  [18.0.1-18.30.11-jre][53],
  [18.0.2-18.32.11-jre][54],
  [18.0.2.1-18.32.13-jre][55],
  
  * [17-jre-latest][62],
  [17.0.9-17.46-jre][73],
  [17.0.0-17.28.13-jre][76],
  [17.0.1-17.30.15-jre][77],
  [17.0.2-17.32.13-jre][78],
  [17.0.3-17.34.19-jre][79],
  [17.0.4-17.36.13-jre][80],
  [17.0.5-17.38.21-jre][81],
  [17.0.6-17.40.19-jre][82],
  [17.0.7-17.42.19-jre][83],
  [17.0.8-17.44.15-jre][84],
  [17.0.9-17.46.19-jre][85],
  [17.0.4.1-17.36.17-jre][86],
  [17.0.8.1-17.44.53-jre][87],
  
  * [16-jre-latest][103],
  [16.0.0-16.28.11-jre][107],
  [16.0.1-16.30.15-jre][108],
  [16.0.2-16.32.15-jre][109],
  
  * [15-jre-latest][111],
  [15.0.7-15.40.19-jre][124],
  [15.0.8-15.42.15-jre][125],
  [15.0.9-15.44.13-jre][126],
  [15.0.10-15.46.17-jre][127],
  
  * [13-jre-latest][139],
  [13.0.11-13.48.19-jre][152],
  [13.0.12-13.50.15-jre][153],
  [13.0.13-13.52.15-jre][154],
  [13.0.14-13.54.17-jre][155],
  
  * [11-jre-latest][172],
  [11.0.21-11.68-jre][189],
  [11.0.15-11.56.19-jre][193],
  [11.0.16-11.58.15-jre][194],
  [11.0.17-11.60.19-jre][195],
  [11.0.18-11.62.17-jre][196],
  [11.0.19-11.64.19-jre][197],
  [11.0.20-11.66.15-jre][198],
  [11.0.21-11.68.17-jre][199],
  [11.0.16.1-11.58.23-jre][201],
  [11.0.20.1-11.66.19-jre][202],
  
  * [8-jre-latest][223],
  [8u392-8.74-jre][247],
  [8u332-8.62.0.19-jre][271],
  [8u342-8.64.0.15-jre][272],
  [8u345-8.64.0.19-jre][273],
  [8u352-8.66.0.15-jre][274],
  [8u362-8.68.0.19-jre][275],
  [8u362-8.68.0.21-jre][276],
  [8u372-8.70.0.23-jre][277],
  [8u382-8.72.0.17-jre][278],
  [8u392-8.74.0.17-jre][279],
  
  * [21-latest][11],
  [21.0.1-21.30][12],
  [21.0.0-21.28.85][14],
  [21.0.1-21.30.15][15],
  
  * [20-latest][23],
  [20.0.0-20.28.85][25],
  [20.0.1-20.30.11][26],
  [20.0.2-20.32.11][27],
  
  * [19-latest][35],
  [19.0.0-19.28.81][37],
  [19.0.1-19.30.11][38],
  [19.0.2-19.32.13][39],
  [19.0.2-19.32.15][40],
  
  * [18-latest][48],
  [18.0.1-18.30.11][50],
  [18.0.2-18.32.11][51],
  [18.0.2.1-18.32.13][52],
  
  * [17-latest][60],
  [17.0.9-17.46][61],
  [17.0.0-17.28.13][63],
  [17.0.1-17.30.15][64],
  [17.0.2-17.32.13][65],
  [17.0.3-17.34.19][66],
  [17.0.4-17.36.13][67],
  [17.0.5-17.38.21][68],
  [17.0.6-17.40.19][69],
  [17.0.7-17.42.19][70],
  [17.0.8-17.44.15][71],
  [17.0.9-17.46.19][72],
  [17.0.4.1-17.36.17][74],
  [17.0.8.1-17.44.53][75],
  
  * [16-latest][102],
  [16.0.0-16.28.11][104],
  [16.0.1-16.30.15][105],
  [16.0.2-16.32.15][106],
  
  * [15-latest][110],
  [15.0.0-15.27.17][112],
  [15.0.1-15.28.13][113],
  [15.0.1-15.28.51][114],
  [15.0.2-15.29.15][115],
  [15.0.3-15.32.15][116],
  [15.0.4-15.34.17][117],
  [15.0.5-15.36.13][118],
  [15.0.6-15.38.17][119],
  [15.0.7-15.40.19][120],
  [15.0.8-15.42.15][121],
  [15.0.9-15.44.13][122],
  [15.0.10-15.46.17][123],
  
  * [14-latest][133],
  [14.0.1-14.28.21][134],
  [14.0.2-14.29.23][135],
  
  * [13-latest][136],
  [13.0.1-13.28][137],
  [13.0.2-13.29][138],
  [13.0.3-13.31.11][140],
  [13.0.4-13.33.25][141],
  [13.0.5-13.35.17][142],
  [13.0.6-13.37.21][143],
  [13.0.7-13.40.15][144],
  [13.0.8-13.42.17][145],
  [13.0.9-13.44.13][146],
  [13.0.10-13.46.15][147],
  [13.0.11-13.48.19][148],
  [13.0.12-13.50.15][149],
  [13.0.13-13.52.15][150],
  [13.0.14-13.54.17][151],
  
  * [12-12.1][161],
  [12-latest][162],
  [12.0.1-12.2][163],
  [12.0.2-12.3][164],
  
  * [11-latest][165],
  [11.0.1-11.2][166],
  [11.0.2-11.29][167],
  [11.0.3-11.31][168],
  [11.0.4-11.33][169],
  [11.0.5-11.35][170],
  [11.0.6-11.37][171],
  [11.0.21-11.68][173],
  [11.0.7-11.39.15][174],
  [11.0.8-11.41.23][175],
  [11.0.9-11.43.21][176],
  [11.0.10-11.45.27][177],
  [11.0.11-11.48.21][178],
  [11.0.12-11.50.19][179],
  [11.0.13-11.52.13][180],
  [11.0.14-11.54.23][181],
  [11.0.15-11.56.19][182],
  [11.0.16-11.58.15][183],
  [11.0.17-11.60.19][184],
  [11.0.18-11.62.17][185],
  [11.0.19-11.64.19][186],
  [11.0.20-11.66.15][187],
  [11.0.21-11.68.17][188],
  [11.0.14.1-11.54.25][190],
  [11.0.16.1-11.58.23][191],
  [11.0.20.1-11.66.19][192],
  
  * [10-latest][213],
  [10u01-10.2][214],
  [10u02-10.3][215],
  
  * [9-ea][216],
  [9-latest][217],
  [9u01-9.0.1.3][218],
  [9u04-9.0.4.1][219],
  [9u07-9.0.7.1][220],
  
  * [8-latest][221],
  [8u392-8.74][222],
  [8u11-8.2.0.1][224],
  [8u20-8.3.0.1][225],
  [8u25-8.4.0.1][226],
  [8u31-8.5.0.1][227],
  [8u40-8.6.0.1][228],
  [8u45-8.7.0.5][229],
  [8u51-8.8.0.3][230],
  [8u60-8.9.0.4][231],
  [8u65-8.10.0.1][232],
  [8u66-8.11.0.1][233],
  [8u72-8.13.0.5][234],
  [8u92-8.15.0.1][235],
  [8u102-8.17.0.7][236],
  [8u112-8.19.0.1][237],
  [8u121-8.20.0.5][238],
  [8u131-8.21.0.1][239],
  [8u144-8.23.0.3][240],
  [8u152-8.25.0.1][241],
  [8u162-8.27.0.7][242],
  [8u172-8.30.0.1][243],
  [8u181-8.31.0.1][244],
  [8u192-8.33.0.1][245],
  [8u202-8.36.0.1][246],
  [8u212-8.38.0.13][248],
  [8u222-8.40.0.25][249],
  [8u232-8.42.0.21][250],
  [8u232-8.42.0.23][251],
  [8u242-8.44.0.11][252],
  [8u252-8.46.0.19][253],
  [8u262-8.48.0.51][254],
  [8u272-8.50.0.21][255],
  [8u275-8.50.0.53][256],
  [8u282-8.52.0.23][257],
  [8u292-8.54.0.21][258],
  [8u302-8.56.0.21][259],
  [8u312-8.58.0.13][260],
  [8u322-8.60.0.21][261],
  [8u332-8.62.0.19][262],
  [8u342-8.64.0.15][263],
  [8u345-8.64.0.19][264],
  [8u352-8.66.0.15][265],
  [8u362-8.68.0.19][266],
  [8u362-8.68.0.21][267],
  [8u372-8.70.0.23][268],
  [8u382-8.72.0.17][269],
  [8u392-8.74.0.17][270],
  
  * [7-latest][291],
  [7u65-7.6.0.1][292],
  [7u72-7.7.0.1][293],
  [7u76-7.8.0.3][294],
  [7u79-7.9.0.2][295],
  [7u80-7.10.0.1][296],
  [7u85-7.11.0.3][297],
  [7u91-7.12.0.3][298],
  [7u95-7.13.0.1][299],
  [7u101-7.14.0.5][300],
  [7u111-7.15.0.5][301],
  [7u121-7.16.0.1][302],
  [7u131-7.17.0.5][303],
  [7u141-7.18.0.3][304],
  [7u154-7.20.0.3][305],
  [7u161-7.21.0.3][306],
  [7u171-7.22.0.3][307],
  [7u181-7.23.0.1][308],
  [7u191-7.24.0.1][309],
  [7u201-7.25.0.5][310],
  [7u211-7.27.0.1][311],
  [7u222-7.29.0.5][312],
  [7u232-7.31.0.5][313],
  [7u242-7.34.0.5][314],
  [7u252-7.36.0.5][315],
  [7u262-7.38.0.11][316],
  [7u272-7.40.0.15][317],
  [7u282-7.42.0.13][318],
  [7u285-7.42.0.51][319],
  [7u292-7.44.0.11][320],
  [7u302-7.46.0.11][321],
  [7u312-7.48.0.11][322],
  [7u332-7.52.0.11][323],
  [7u342-7.54.0.13][324],
  [7u352-7.56.0.11][325],
  
  * [6-latest][326],
  [6u53-6.5.0.2][327],
  [6u56-6.6.0.1][328],
  [6u59-6.7.0.2][329],
  [6u63-6.8.0.1][330],
  [6u69-6.9.0.3][331],
  [6u73-6.10.0.3][332],
  [6u77-6.11.0.2][333],
  [6u79-6.12.0.2][334],
  [6u83-6.13.0.7][335],
  [6u87-6.14.0.1][336],
  [6u89-6.15.0.1][337],
  [6u93-6.16.0.1][338],
  [6u97-6.17.0.1][339],
  [6u99-6.18.0.3][340],
  [6u103-6.19.0.1][341],
  [6u107-6.20.0.1][342],
  [6u113-6.21.0.3][343],
  [6u119-6.22.0.3][344],
  

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


  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-headless-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre-headless/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15-jre-headless/Dockerfile
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-headless-latest/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre-headless/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre-headless/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-headless-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre-headless/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre-headless/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-headless-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre-headless/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre-headless/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-headless-latest/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre-headless/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre-headless/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre-headless/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13-jre-headless/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19-jre-headless/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13-jre-headless/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21-jre-headless/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19-jre-headless/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19-jre-headless/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15-jre-headless/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19-jre-headless/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-headless-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre-headless/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre-headless/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre-headless/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-headless-latest/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre-headless/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre-headless/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre-headless/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-headless-latest/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre-headless/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre-headless/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15-jre-headless/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19-jre-headless/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17-jre-headless/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19-jre-headless/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15-jre-headless/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17-jre-headless/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-headless-latest/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre-headless/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre-headless/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre-headless/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19-jre-headless/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15-jre-headless/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19-jre-headless/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21-jre-headless/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23-jre-headless/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17-jre-headless/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17-jre-headless/Dockerfile
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre/Dockerfile
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre/Dockerfile
  
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre/Dockerfile
  
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13-jre/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19-jre/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21-jre/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15-jre/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19-jre/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53-jre/Dockerfile
  
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-jre-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15-jre/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15-jre/Dockerfile
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17-jre/Dockerfile
  
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17-jre/Dockerfile
  
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-latest/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19-jre/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17-jre/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19-jre/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15-jre/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19-jre/Dockerfile
  
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-latest/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19-jre/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15-jre/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19-jre/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21-jre/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23-jre/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17-jre/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11/Dockerfile
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.15/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13/Dockerfile
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.3-17.34.19/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4-17.36.13/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.5-17.38.21/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.6-17.40.19/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.7-17.42.19/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8-17.44.15/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46.19/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.4.1-17.36.17/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.8.1-17.44.53/Dockerfile
  
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15/Dockerfile
  
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-latest/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.0-15.27.17/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.13/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.51/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.2-15.29.15/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.3-15.32.15/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.4-15.34.17/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.5-15.36.13/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.6-15.38.17/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.10-15.46.17/Dockerfile
  
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14-latest/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.1-14.28.21/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.2-14.29.23/Dockerfile
  
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-latest/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.1-13.28/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.2-13.29/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.3-13.31.11/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.4-13.33.25/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.5-13.35.17/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.6-13.37.21/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.7-13.40.15/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.8-13.42.17/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.9-13.44.13/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.10-13.46.15/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.14-13.54.17/Dockerfile
  
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-12.1/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.1-12.2/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.2-12.3/Dockerfile
  
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-latest/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.1-11.2/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.2-11.29/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.3-11.31/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.4-11.33/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.5-11.35/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.6-11.37/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.7-11.39.15/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.8-11.41.23/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.9-11.43.21/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.10-11.45.27/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.11-11.48.21/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.12-11.50.19/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.13-11.52.13/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.14-11.54.23/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16-11.58.15/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.17-11.60.19/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.18-11.62.17/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.19-11.64.19/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20-11.66.15/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68.17/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.14.1-11.54.25/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.20.1-11.66.19/Dockerfile
  
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10-latest/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u01-10.2/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u02-10.3/Dockerfile
  
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-ea/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-latest/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u01-9.0.1.3/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u04-9.0.4.1/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u07-9.0.7.1/Dockerfile
  
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-latest/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u11-8.2.0.1/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u20-8.3.0.1/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u25-8.4.0.1/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u31-8.5.0.1/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u40-8.6.0.1/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u45-8.7.0.5/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u51-8.8.0.3/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u60-8.9.0.4/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u65-8.10.0.1/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u66-8.11.0.1/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u72-8.13.0.5/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u92-8.15.0.1/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u102-8.17.0.7/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u112-8.19.0.1/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u121-8.20.0.5/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u131-8.21.0.1/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u144-8.23.0.3/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u152-8.25.0.1/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u162-8.27.0.7/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u172-8.30.0.1/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u181-8.31.0.1/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u192-8.33.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u202-8.36.0.1/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u212-8.38.0.13/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u222-8.40.0.25/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u232-8.42.0.21/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u232-8.42.0.23/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u242-8.44.0.11/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u252-8.46.0.19/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u262-8.48.0.51/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u272-8.50.0.21/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u275-8.50.0.53/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u282-8.52.0.23/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u292-8.54.0.21/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u302-8.56.0.21/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u312-8.58.0.13/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u322-8.60.0.21/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u345-8.64.0.19/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u352-8.66.0.15/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.19/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u362-8.68.0.21/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u372-8.70.0.23/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u382-8.72.0.17/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74.0.17/Dockerfile
  
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7-latest/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u79-7.9.0.2/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u80-7.10.0.1/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u85-7.11.0.3/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u91-7.12.0.3/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u95-7.13.0.1/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u101-7.14.0.5/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u111-7.15.0.5/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u121-7.16.0.1/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u131-7.17.0.5/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u141-7.18.0.3/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u154-7.20.0.3/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u161-7.21.0.3/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u171-7.22.0.3/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u181-7.23.0.1/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u191-7.24.0.1/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u201-7.25.0.5/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u211-7.27.0.1/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u222-7.29.0.5/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u232-7.31.0.5/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u242-7.34.0.5/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u252-7.36.0.5/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u262-7.38.0.11/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u272-7.40.0.15/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u282-7.42.0.13/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u285-7.42.0.51/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u292-7.44.0.11/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u302-7.46.0.11/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u312-7.48.0.11/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u332-7.52.0.11/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u342-7.54.0.13/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u352-7.56.0.11/Dockerfile
  
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6-latest/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u63-6.8.0.1/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u69-6.9.0.3/Dockerfile
  [332]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u73-6.10.0.3/Dockerfile
  [333]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u77-6.11.0.2/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u79-6.12.0.2/Dockerfile
  [335]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u83-6.13.0.7/Dockerfile
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u87-6.14.0.1/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u89-6.15.0.1/Dockerfile
  [338]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u93-6.16.0.1/Dockerfile
  [339]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u97-6.17.0.1/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u99-6.18.0.3/Dockerfile
  [341]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u103-6.19.0.1/Dockerfile
  [342]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u107-6.20.0.1/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u113-6.21.0.3/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u119-6.22.0.3/Dockerfile
  