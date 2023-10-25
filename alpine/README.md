Azul Zulu Alpine
================

The `zulu-openjdk-alpine` image includes Alpine-native Azul Zulu Builds of OpenJDK, which use the built-in musl libc functionality
and do not add glibc on top of the Alpine distribution.

Azul Zulu Builds of OpenJDK are available for free unlimited use and commercially supported by [Azul][1] as a part of the Azul Platform Core bundle.
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
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][20]
  * [`19.0.2-19.32.13`, `19-latest` (*19-latest/Dockerfile)*][32]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][44]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][56]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][95]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][103]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][127]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][130]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][171]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][175]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][243]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][319]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][342]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [21-jre-headless-latest][17],
  [21.0.0-21.28.85-jre-headless][18],
  [21.0.1-21.30.15-jre-headless][19],
  
  * [20-jre-headless-latest][28],
  [20.0.0-20.28.85-jre-headless][29],
  [20.0.1-20.30.11-jre-headless][30],
  [20.0.2-20.32.11-jre-headless][31],
  
  * [19-jre-headless-latest][40],
  [19.0.0-19.28.81-jre-headless][41],
  [19.0.1-19.30.11-jre-headless][42],
  [19.0.2-19.32.13-jre-headless][43],
  
  * [18-jre-headless-latest][52],
  [18.0.1-18.30.11-jre-headless][53],
  [18.0.2-18.32.11-jre-headless][54],
  [18.0.2.1-18.32.13-jre-headless][55],
  
  * [17-jre-headless-latest][82],
  [17.0.0-17.28.13-jre-headless][83],
  [17.0.1-17.30.15-jre-headless][84],
  [17.0.2-17.32.13-jre-headless][85],
  [17.0.3-17.34.19-jre-headless][86],
  [17.0.4-17.36.13-jre-headless][87],
  [17.0.5-17.38.21-jre-headless][88],
  [17.0.6-17.40.19-jre-headless][89],
  [17.0.7-17.42.19-jre-headless][90],
  [17.0.8-17.44.15-jre-headless][91],
  [17.0.9-17.46.19-jre-headless][92],
  [17.0.4.1-17.36.17-jre-headless][93],
  [17.0.8.1-17.44.53-jre-headless][94],
  
  * [15-jre-headless-latest][122],
  [15.0.7-15.40.19-jre-headless][123],
  [15.0.8-15.42.15-jre-headless][124],
  [15.0.9-15.44.13-jre-headless][125],
  [15.0.10-15.46.17-jre-headless][126],
  
  * [13-jre-headless-latest][158],
  [13.0.3-13.31.11-jre-headless][159],
  [13.0.4-13.33.25-jre-headless][160],
  [13.0.5-13.35.17-jre-headless][161],
  [13.0.6-13.37.21-jre-headless][162],
  [13.0.7-13.40.15-jre-headless][163],
  [13.0.8-13.42.17-jre-headless][164],
  [13.0.9-13.44.13-jre-headless][165],
  [13.0.10-13.46.15-jre-headless][166],
  [13.0.11-13.48.19-jre-headless][167],
  [13.0.12-13.50.15-jre-headless][168],
  [13.0.13-13.52.15-jre-headless][169],
  [13.0.14-13.54.17-jre-headless][170],
  
  * [11-jre-headless-latest][220],
  [11.0.5-11.35-jre-headless][224],
  [11.0.6-11.37-jre-headless][225],
  [11.0.7-11.39.15-jre-headless][226],
  [11.0.8-11.41.23-jre-headless][227],
  [11.0.9-11.43.21-jre-headless][228],
  [11.0.10-11.45.27-jre-headless][229],
  [11.0.12-11.50.19-jre-headless][230],
  [11.0.13-11.52.13-jre-headless][231],
  [11.0.14-11.54.23-jre-headless][232],
  [11.0.15-11.56.19-jre-headless][233],
  [11.0.16-11.58.15-jre-headless][234],
  [11.0.17-11.60.19-jre-headless][235],
  [11.0.18-11.62.17-jre-headless][236],
  [11.0.19-11.64.19-jre-headless][237],
  [11.0.20-11.66.15-jre-headless][238],
  [11.0.21-11.68.17-jre-headless][239],
  [11.0.14.1-11.54.25-jre-headless][240],
  [11.0.16.1-11.58.23-jre-headless][241],
  [11.0.20.1-11.66.19-jre-headless][242],
  
  * [8-jre-headless-latest][299],
  [8u232-8.42.0.23-jre-headless][300],
  [8u242-8.44.0.11-jre-headless][301],
  [8u252-8.46.0.19-jre-headless][302],
  [8u262-8.48.0.51-jre-headless][303],
  [8u272-8.50.0.21-jre-headless][304],
  [8u275-8.50.0.51-jre-headless][305],
  [8u282-8.52.0.23-jre-headless][306],
  [8u302-8.56.0.21-jre-headless][307],
  [8u312-8.58.0.13-jre-headless][308],
  [8u322-8.60.0.21-jre-headless][309],
  [8u332-8.62.0.19-jre-headless][310],
  [8u342-8.64.0.15-jre-headless][311],
  [8u345-8.64.0.19-jre-headless][312],
  [8u352-8.66.0.15-jre-headless][313],
  [8u362-8.68.0.19-jre-headless][314],
  [8u362-8.68.0.21-jre-headless][315],
  [8u372-8.70.0.23-jre-headless][316],
  [8u382-8.72.0.17-jre-headless][317],
  [8u392-8.74.0.17-jre-headless][318],
  
  * [21-jre-latest][12],
  [21.0.0-21.28.85-jre][15],
  [21.0.1-21.30.15-jre][16],
  
  * [20-jre-latest][21],
  [20.0.0-20.28.85-jre][25],
  [20.0.1-20.30.11-jre][26],
  [20.0.2-20.32.11-jre][27],
  
  * [19-jre-latest][33],
  [19.0.0-19.28.81-jre][37],
  [19.0.1-19.30.11-jre][38],
  [19.0.2-19.32.13-jre][39],
  
  * [18-jre-latest][45],
  [18.0.1-18.30.11-jre][49],
  [18.0.2-18.32.11-jre][50],
  [18.0.2.1-18.32.13-jre][51],
  
  * [17-jre-latest][57],
  [17.0.0-17.28.13-jre][70],
  [17.0.1-17.30.15-jre][71],
  [17.0.2-17.32.13-jre][72],
  [17.0.3-17.34.19-jre][73],
  [17.0.4-17.36.13-jre][74],
  [17.0.5-17.38.21-jre][75],
  [17.0.6-17.40.19-jre][76],
  [17.0.7-17.42.19-jre][77],
  [17.0.8-17.44.15-jre][78],
  [17.0.9-17.46.19-jre][79],
  [17.0.4.1-17.36.17-jre][80],
  [17.0.8.1-17.44.53-jre][81],
  
  * [16-jre-latest][96],
  [16.0.0-16.28.11-jre][100],
  [16.0.1-16.30.15-jre][101],
  [16.0.2-16.32.15-jre][102],
  
  * [15-jre-latest][104],
  [15.0.0-15.27.17-jre][117],
  [15.0.7-15.40.19-jre][118],
  [15.0.8-15.42.15-jre][119],
  [15.0.9-15.44.13-jre][120],
  [15.0.10-15.46.17-jre][121],
  
  * [13-jre-latest][133],
  [13.0.3-13.31.11-jre][146],
  [13.0.4-13.33.25-jre][147],
  [13.0.5-13.35.17-jre][148],
  [13.0.6-13.37.21-jre][149],
  [13.0.7-13.40.15-jre][150],
  [13.0.8-13.42.17-jre][151],
  [13.0.9-13.44.13-jre][152],
  [13.0.10-13.46.15-jre][153],
  [13.0.11-13.48.19-jre][154],
  [13.0.12-13.50.15-jre][155],
  [13.0.13-13.52.15-jre][156],
  [13.0.14-13.54.17-jre][157],
  
  * [11-jre-latest][182],
  [11.0.3-11.31-jre][198],
  [11.0.4-11.33-jre][199],
  [11.0.5-11.35-jre][200],
  [11.0.6-11.37-jre][201],
  [11.0.7-11.39.15-jre][205],
  [11.0.8-11.41.23-jre][206],
  [11.0.9-11.43.21-jre][207],
  [11.0.10-11.45.27-jre][208],
  [11.0.11-11.48.21-jre][209],
  [11.0.12-11.50.19-jre][210],
  [11.0.13-11.52.13-jre][211],
  [11.0.14-11.54.23-jre][212],
  [11.0.15-11.56.19-jre][213],
  [11.0.16-11.58.15-jre][214],
  [11.0.17-11.60.19-jre][215],
  [11.0.18-11.62.17-jre][216],
  [11.0.19-11.64.19-jre][217],
  [11.0.20-11.66.15-jre][218],
  [11.0.21-11.68.17-jre][219],
  [11.0.14.1-11.54.25-jre][221],
  [11.0.16.1-11.58.23-jre][222],
  [11.0.20.1-11.66.19-jre][223],
  
  * [8-jre-latest][244],
  [8u212-8.38.0.13-jre][276],
  [8u222-8.40.0.25-jre][277],
  [8u232-8.42.0.21-jre][278],
  [8u232-8.42.0.23-jre][279],
  [8u242-8.44.0.11-jre][280],
  [8u252-8.46.0.19-jre][281],
  [8u262-8.48.0.51-jre][282],
  [8u272-8.50.0.21-jre][283],
  [8u275-8.50.0.51-jre][284],
  [8u282-8.52.0.23-jre][285],
  [8u292-8.54.0.21-jre][286],
  [8u302-8.56.0.21-jre][287],
  [8u312-8.58.0.13-jre][288],
  [8u322-8.60.0.21-jre][289],
  [8u332-8.62.0.19-jre][290],
  [8u342-8.64.0.15-jre][291],
  [8u345-8.64.0.19-jre][292],
  [8u352-8.66.0.15-jre][293],
  [8u362-8.68.0.19-jre][294],
  [8u362-8.68.0.21-jre][295],
  [8u372-8.70.0.23-jre][296],
  [8u382-8.72.0.17-jre][297],
  [8u392-8.74.0.17-jre][298],
  
  * [21-latest][11],
  [21.0.0-21.28.85][13],
  [21.0.1-21.30.15][14],
  
  * [20-latest][20],
  [20.0.0-20.28.85][22],
  [20.0.1-20.30.11][23],
  [20.0.2-20.32.11][24],
  
  * [19-latest][32],
  [19.0.0-19.28.81][34],
  [19.0.1-19.30.11][35],
  [19.0.2-19.32.13][36],
  
  * [18-latest][44],
  [18.0.1-18.30.11][46],
  [18.0.2-18.32.11][47],
  [18.0.2.1-18.32.13][48],
  
  * [17-latest][56],
  [17.0.0-17.28.13][58],
  [17.0.1-17.30.15][59],
  [17.0.2-17.32.13][60],
  [17.0.3-17.34.19][61],
  [17.0.4-17.36.13][62],
  [17.0.5-17.38.21][63],
  [17.0.6-17.40.19][64],
  [17.0.7-17.42.19][65],
  [17.0.8-17.44.15][66],
  [17.0.9-17.46.19][67],
  [17.0.4.1-17.36.17][68],
  [17.0.8.1-17.44.53][69],
  
  * [16-latest][95],
  [16.0.0-16.28.11][97],
  [16.0.1-16.30.15][98],
  [16.0.2-16.32.15][99],
  
  * [15-latest][103],
  [15.0.0-15.27.17][105],
  [15.0.1-15.28.13][106],
  [15.0.1-15.28.51][107],
  [15.0.2-15.29.15][108],
  [15.0.3-15.32.15][109],
  [15.0.4-15.34.17][110],
  [15.0.5-15.36.13][111],
  [15.0.6-15.38.17][112],
  [15.0.7-15.40.19][113],
  [15.0.8-15.42.15][114],
  [15.0.9-15.44.13][115],
  [15.0.10-15.46.17][116],
  
  * [14-latest][127],
  [14.0.1-14.28.21][128],
  [14.0.2-14.29.23][129],
  
  * [13-latest][130],
  [13.0.1-13.28][131],
  [13.0.2-13.29][132],
  [13.0.3-13.31.11][134],
  [13.0.4-13.33.25][135],
  [13.0.5-13.35.17][136],
  [13.0.6-13.37.21][137],
  [13.0.7-13.40.15][138],
  [13.0.8-13.42.17][139],
  [13.0.9-13.44.13][140],
  [13.0.10-13.46.15][141],
  [13.0.11-13.48.19][142],
  [13.0.12-13.50.15][143],
  [13.0.13-13.52.15][144],
  [13.0.14-13.54.17][145],
  
  * [12-latest][171],
  [12.0.0-12.1][172],
  [12.0.1-12.2][173],
  [12.0.2-12.3][174],
  
  * [11-latest][175],
  [11.0.1-11.2][176],
  [11.0.2-11.29][177],
  [11.0.3-11.31][178],
  [11.0.4-11.33][179],
  [11.0.5-11.35][180],
  [11.0.6-11.37][181],
  [11.0.7-11.39.15][183],
  [11.0.8-11.41.23][184],
  [11.0.9-11.43.21][185],
  [11.0.10-11.45.27][186],
  [11.0.11-11.48.21][187],
  [11.0.12-11.50.19][188],
  [11.0.13-11.52.13][189],
  [11.0.14-11.54.23][190],
  [11.0.15-11.56.19][191],
  [11.0.16-11.58.15][192],
  [11.0.17-11.60.19][193],
  [11.0.18-11.62.17][194],
  [11.0.19-11.64.19][195],
  [11.0.20-11.66.15][196],
  [11.0.21-11.68.17][197],
  [11.0.14.1-11.54.25][202],
  [11.0.16.1-11.58.23][203],
  [11.0.20.1-11.66.19][204],
  
  * [8-latest][243],
  [8u131-8.21.0.1][245],
  [8u144-8.23.0.3][246],
  [8u152-8.25.0.1][247],
  [8u162-8.27.0.7][248],
  [8u172-8.30.0.1][249],
  [8u181-8.31.0.1][250],
  [8u192-8.33.0.1][251],
  [8u202-8.36.0.3][252],
  [8u212-8.38.0.13][253],
  [8u222-8.40.0.25][254],
  [8u232-8.42.0.21][255],
  [8u232-8.42.0.23][256],
  [8u242-8.44.0.11][257],
  [8u252-8.46.0.19][258],
  [8u262-8.48.0.51][259],
  [8u272-8.50.0.21][260],
  [8u275-8.50.0.51][261],
  [8u282-8.52.0.23][262],
  [8u292-8.54.0.21][263],
  [8u302-8.56.0.21][264],
  [8u312-8.58.0.13][265],
  [8u322-8.60.0.21][266],
  [8u332-8.62.0.19][267],
  [8u342-8.64.0.15][268],
  [8u345-8.64.0.19][269],
  [8u352-8.66.0.15][270],
  [8u362-8.68.0.19][271],
  [8u362-8.68.0.21][272],
  [8u372-8.70.0.23][273],
  [8u382-8.72.0.17][274],
  [8u392-8.74.0.17][275],
  
  * [7-latest][319],
  [7u141-7.18.0.3][320],
  [7u154-7.20.0.3][321],
  [7u161-7.21.0.3][322],
  [7u171-7.22.0.3][323],
  [7u181-7.23.0.1][324],
  [7u191-7.24.0.1][325],
  [7u201-7.25.0.5][326],
  [7u211-7.27.0.1][327],
  [7u222-7.29.0.5][328],
  [7u232-7.31.0.5][329],
  [7u242-7.34.0.5][330],
  [7u252-7.36.0.5][331],
  [7u262-7.38.0.11][332],
  [7u272-7.40.0.15][333],
  [7u282-7.42.0.13][334],
  [7u285-7.42.0.51][335],
  [7u292-7.44.0.11][336],
  [7u302-7.46.0.11][337],
  [7u312-7.48.0.11][338],
  [7u332-7.52.0.11][339],
  [7u342-7.54.0.13][340],
  [7u352-7.56.0.11][341],
  
  * [6-latest][342],
  [6u93-6.16.0.1][343],
  [6u97-6.17.0.1][344],
  [6u99-6.18.0.3][345],
  [6u103-6.19.0.1][346],
  [6u107-6.20.0.1][347],
  [6u113-6.21.0.3][348],
  [6u119-6.22.0.3][349],
  

**Note**: Some of these may use glibc and predate the move to musl libc.

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


  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-headless-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85-jre-headless/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30.15-jre-headless/Dockerfile
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-headless-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre-headless/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre-headless/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-headless-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre-headless/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre-headless/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre-headless/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre-headless/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre-headless/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre-headless/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre-headless/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15-jre-headless/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.9-17.46.19-jre-headless/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre-headless/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre-headless/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre-headless/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre-headless/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre-headless/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre-headless/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre-headless/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre-headless/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre-headless/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre-headless/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre-headless/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15-jre-headless/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.21-11.68.17-jre-headless/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre-headless/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre-headless/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre-headless/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre-headless/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre-headless/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre-headless/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre-headless/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre-headless/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17-jre-headless/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u392-8.74.0.17-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30.15-jre/Dockerfile
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11-jre/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre/Dockerfile
  
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre/Dockerfile
  
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15-jre/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.9-17.46.19-jre/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53-jre/Dockerfile
  
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17-jre/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre/Dockerfile
  
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre/Dockerfile
  
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15-jre/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.21-11.68.17-jre/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19-jre/Dockerfile
  
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17-jre/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u392-8.74.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30.15/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13/Dockerfile
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.9-17.46.19/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53/Dockerfile
  
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17/Dockerfile
  
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17/Dockerfile
  
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.21-11.68.17/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19/Dockerfile
  
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u392-8.74.0.17/Dockerfile
  
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [332]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [333]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [335]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [338]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [339]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u342-7.54.0.13/Dockerfile
  [341]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u352-7.56.0.11/Dockerfile
  
  [342]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [345]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [346]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [347]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [348]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [349]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  