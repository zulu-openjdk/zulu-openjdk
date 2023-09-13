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


  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][11]
  * [`19.0.2-19.32.13`, `19-latest` (*19-latest/Dockerfile)*][23]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][35]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][47]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][83]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][91]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][115]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][118]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][159]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][163]
  * [`8u382-8.72.0.17`, `8-latest` (*8-latest/Dockerfile)*][228]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][301]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][324]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [20-jre-headless-latest][19],
  [20.0.0-20.28.85-jre-headless][20],
  [20.0.1-20.30.11-jre-headless][21],
  [20.0.2-20.32.11-jre-headless][22],
  
  * [19-jre-headless-latest][31],
  [19.0.0-19.28.81-jre-headless][32],
  [19.0.1-19.30.11-jre-headless][33],
  [19.0.2-19.32.13-jre-headless][34],
  
  * [18-jre-headless-latest][43],
  [18.0.1-18.30.11-jre-headless][44],
  [18.0.2-18.32.11-jre-headless][45],
  [18.0.2.1-18.32.13-jre-headless][46],
  
  * [17-jre-headless-latest][71],
  [17.0.0-17.28.13-jre-headless][72],
  [17.0.1-17.30.15-jre-headless][73],
  [17.0.2-17.32.13-jre-headless][74],
  [17.0.3-17.34.19-jre-headless][75],
  [17.0.4-17.36.13-jre-headless][76],
  [17.0.5-17.38.21-jre-headless][77],
  [17.0.6-17.40.19-jre-headless][78],
  [17.0.7-17.42.19-jre-headless][79],
  [17.0.8-17.44.15-jre-headless][80],
  [17.0.4.1-17.36.17-jre-headless][81],
  [17.0.8.1-17.44.53-jre-headless][82],
  
  * [15-jre-headless-latest][110],
  [15.0.7-15.40.19-jre-headless][111],
  [15.0.8-15.42.15-jre-headless][112],
  [15.0.9-15.44.13-jre-headless][113],
  [15.0.10-15.46.17-jre-headless][114],
  
  * [13-jre-headless-latest][146],
  [13.0.3-13.31.11-jre-headless][147],
  [13.0.4-13.33.25-jre-headless][148],
  [13.0.5-13.35.17-jre-headless][149],
  [13.0.6-13.37.21-jre-headless][150],
  [13.0.7-13.40.15-jre-headless][151],
  [13.0.8-13.42.17-jre-headless][152],
  [13.0.9-13.44.13-jre-headless][153],
  [13.0.10-13.46.15-jre-headless][154],
  [13.0.11-13.48.19-jre-headless][155],
  [13.0.12-13.50.15-jre-headless][156],
  [13.0.13-13.52.15-jre-headless][157],
  [13.0.14-13.54.17-jre-headless][158],
  
  * [11-jre-headless-latest][206],
  [11.0.5-11.35-jre-headless][210],
  [11.0.6-11.37-jre-headless][211],
  [11.0.7-11.39.15-jre-headless][212],
  [11.0.8-11.41.23-jre-headless][213],
  [11.0.9-11.43.21-jre-headless][214],
  [11.0.10-11.45.27-jre-headless][215],
  [11.0.12-11.50.19-jre-headless][216],
  [11.0.13-11.52.13-jre-headless][217],
  [11.0.14-11.54.23-jre-headless][218],
  [11.0.15-11.56.19-jre-headless][219],
  [11.0.16-11.58.15-jre-headless][220],
  [11.0.17-11.60.19-jre-headless][221],
  [11.0.18-11.62.17-jre-headless][222],
  [11.0.19-11.64.19-jre-headless][223],
  [11.0.20-11.66.15-jre-headless][224],
  [11.0.14.1-11.54.25-jre-headless][225],
  [11.0.16.1-11.58.23-jre-headless][226],
  [11.0.20.1-11.66.19-jre-headless][227],
  
  * [8-jre-headless-latest][282],
  [8u232-8.42.0.23-jre-headless][283],
  [8u242-8.44.0.11-jre-headless][284],
  [8u252-8.46.0.19-jre-headless][285],
  [8u262-8.48.0.51-jre-headless][286],
  [8u272-8.50.0.21-jre-headless][287],
  [8u275-8.50.0.51-jre-headless][288],
  [8u282-8.52.0.23-jre-headless][289],
  [8u302-8.56.0.21-jre-headless][290],
  [8u312-8.58.0.13-jre-headless][291],
  [8u322-8.60.0.21-jre-headless][292],
  [8u332-8.62.0.19-jre-headless][293],
  [8u342-8.64.0.15-jre-headless][294],
  [8u345-8.64.0.19-jre-headless][295],
  [8u352-8.66.0.15-jre-headless][296],
  [8u362-8.68.0.19-jre-headless][297],
  [8u362-8.68.0.21-jre-headless][298],
  [8u372-8.70.0.23-jre-headless][299],
  [8u382-8.72.0.17-jre-headless][300],
  
  * [20-jre-latest][12],
  [20.0.0-20.28.85-jre][16],
  [20.0.1-20.30.11-jre][17],
  [20.0.2-20.32.11-jre][18],
  
  * [19-jre-latest][24],
  [19.0.0-19.28.81-jre][28],
  [19.0.1-19.30.11-jre][29],
  [19.0.2-19.32.13-jre][30],
  
  * [18-jre-latest][36],
  [18.0.1-18.30.11-jre][40],
  [18.0.2-18.32.11-jre][41],
  [18.0.2.1-18.32.13-jre][42],
  
  * [17-jre-latest][48],
  [17.0.0-17.28.13-jre][60],
  [17.0.1-17.30.15-jre][61],
  [17.0.2-17.32.13-jre][62],
  [17.0.3-17.34.19-jre][63],
  [17.0.4-17.36.13-jre][64],
  [17.0.5-17.38.21-jre][65],
  [17.0.6-17.40.19-jre][66],
  [17.0.7-17.42.19-jre][67],
  [17.0.8-17.44.15-jre][68],
  [17.0.4.1-17.36.17-jre][69],
  [17.0.8.1-17.44.53-jre][70],
  
  * [16-jre-latest][84],
  [16.0.0-16.28.11-jre][88],
  [16.0.1-16.30.15-jre][89],
  [16.0.2-16.32.15-jre][90],
  
  * [15-jre-latest][92],
  [15.0.0-15.27.17-jre][105],
  [15.0.7-15.40.19-jre][106],
  [15.0.8-15.42.15-jre][107],
  [15.0.9-15.44.13-jre][108],
  [15.0.10-15.46.17-jre][109],
  
  * [13-jre-latest][121],
  [13.0.3-13.31.11-jre][134],
  [13.0.4-13.33.25-jre][135],
  [13.0.5-13.35.17-jre][136],
  [13.0.6-13.37.21-jre][137],
  [13.0.7-13.40.15-jre][138],
  [13.0.8-13.42.17-jre][139],
  [13.0.9-13.44.13-jre][140],
  [13.0.10-13.46.15-jre][141],
  [13.0.11-13.48.19-jre][142],
  [13.0.12-13.50.15-jre][143],
  [13.0.13-13.52.15-jre][144],
  [13.0.14-13.54.17-jre][145],
  
  * [11-jre-latest][170],
  [11.0.3-11.31-jre][185],
  [11.0.4-11.33-jre][186],
  [11.0.5-11.35-jre][187],
  [11.0.6-11.37-jre][188],
  [11.0.7-11.39.15-jre][192],
  [11.0.8-11.41.23-jre][193],
  [11.0.9-11.43.21-jre][194],
  [11.0.10-11.45.27-jre][195],
  [11.0.11-11.48.21-jre][196],
  [11.0.12-11.50.19-jre][197],
  [11.0.13-11.52.13-jre][198],
  [11.0.14-11.54.23-jre][199],
  [11.0.15-11.56.19-jre][200],
  [11.0.16-11.58.15-jre][201],
  [11.0.17-11.60.19-jre][202],
  [11.0.18-11.62.17-jre][203],
  [11.0.19-11.64.19-jre][204],
  [11.0.20-11.66.15-jre][205],
  [11.0.14.1-11.54.25-jre][207],
  [11.0.16.1-11.58.23-jre][208],
  [11.0.20.1-11.66.19-jre][209],
  
  * [8-jre-latest][229],
  [8u212-8.38.0.13-jre][260],
  [8u222-8.40.0.25-jre][261],
  [8u232-8.42.0.21-jre][262],
  [8u232-8.42.0.23-jre][263],
  [8u242-8.44.0.11-jre][264],
  [8u252-8.46.0.19-jre][265],
  [8u262-8.48.0.51-jre][266],
  [8u272-8.50.0.21-jre][267],
  [8u275-8.50.0.51-jre][268],
  [8u282-8.52.0.23-jre][269],
  [8u292-8.54.0.21-jre][270],
  [8u302-8.56.0.21-jre][271],
  [8u312-8.58.0.13-jre][272],
  [8u322-8.60.0.21-jre][273],
  [8u332-8.62.0.19-jre][274],
  [8u342-8.64.0.15-jre][275],
  [8u345-8.64.0.19-jre][276],
  [8u352-8.66.0.15-jre][277],
  [8u362-8.68.0.19-jre][278],
  [8u362-8.68.0.21-jre][279],
  [8u372-8.70.0.23-jre][280],
  [8u382-8.72.0.17-jre][281],
  
  * [20-latest][11],
  [20.0.0-20.28.85][13],
  [20.0.1-20.30.11][14],
  [20.0.2-20.32.11][15],
  
  * [19-latest][23],
  [19.0.0-19.28.81][25],
  [19.0.1-19.30.11][26],
  [19.0.2-19.32.13][27],
  
  * [18-latest][35],
  [18.0.1-18.30.11][37],
  [18.0.2-18.32.11][38],
  [18.0.2.1-18.32.13][39],
  
  * [17-latest][47],
  [17.0.0-17.28.13][49],
  [17.0.1-17.30.15][50],
  [17.0.2-17.32.13][51],
  [17.0.3-17.34.19][52],
  [17.0.4-17.36.13][53],
  [17.0.5-17.38.21][54],
  [17.0.6-17.40.19][55],
  [17.0.7-17.42.19][56],
  [17.0.8-17.44.15][57],
  [17.0.4.1-17.36.17][58],
  [17.0.8.1-17.44.53][59],
  
  * [16-latest][83],
  [16.0.0-16.28.11][85],
  [16.0.1-16.30.15][86],
  [16.0.2-16.32.15][87],
  
  * [15-latest][91],
  [15.0.0-15.27.17][93],
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
  
  * [14-latest][115],
  [14.0.1-14.28.21][116],
  [14.0.2-14.29.23][117],
  
  * [13-latest][118],
  [13.0.1-13.28][119],
  [13.0.2-13.29][120],
  [13.0.3-13.31.11][122],
  [13.0.4-13.33.25][123],
  [13.0.5-13.35.17][124],
  [13.0.6-13.37.21][125],
  [13.0.7-13.40.15][126],
  [13.0.8-13.42.17][127],
  [13.0.9-13.44.13][128],
  [13.0.10-13.46.15][129],
  [13.0.11-13.48.19][130],
  [13.0.12-13.50.15][131],
  [13.0.13-13.52.15][132],
  [13.0.14-13.54.17][133],
  
  * [12-latest][159],
  [12.0.0-12.1][160],
  [12.0.1-12.2][161],
  [12.0.2-12.3][162],
  
  * [11-latest][163],
  [11.0.1-11.2][164],
  [11.0.2-11.29][165],
  [11.0.3-11.31][166],
  [11.0.4-11.33][167],
  [11.0.5-11.35][168],
  [11.0.6-11.37][169],
  [11.0.7-11.39.15][171],
  [11.0.8-11.41.23][172],
  [11.0.9-11.43.21][173],
  [11.0.10-11.45.27][174],
  [11.0.11-11.48.21][175],
  [11.0.12-11.50.19][176],
  [11.0.13-11.52.13][177],
  [11.0.14-11.54.23][178],
  [11.0.15-11.56.19][179],
  [11.0.16-11.58.15][180],
  [11.0.17-11.60.19][181],
  [11.0.18-11.62.17][182],
  [11.0.19-11.64.19][183],
  [11.0.20-11.66.15][184],
  [11.0.14.1-11.54.25][189],
  [11.0.16.1-11.58.23][190],
  [11.0.20.1-11.66.19][191],
  
  * [8-latest][228],
  [8u131-8.21.0.1][230],
  [8u144-8.23.0.3][231],
  [8u152-8.25.0.1][232],
  [8u162-8.27.0.7][233],
  [8u172-8.30.0.1][234],
  [8u181-8.31.0.1][235],
  [8u192-8.33.0.1][236],
  [8u202-8.36.0.3][237],
  [8u212-8.38.0.13][238],
  [8u222-8.40.0.25][239],
  [8u232-8.42.0.21][240],
  [8u232-8.42.0.23][241],
  [8u242-8.44.0.11][242],
  [8u252-8.46.0.19][243],
  [8u262-8.48.0.51][244],
  [8u272-8.50.0.21][245],
  [8u275-8.50.0.51][246],
  [8u282-8.52.0.23][247],
  [8u292-8.54.0.21][248],
  [8u302-8.56.0.21][249],
  [8u312-8.58.0.13][250],
  [8u322-8.60.0.21][251],
  [8u332-8.62.0.19][252],
  [8u342-8.64.0.15][253],
  [8u345-8.64.0.19][254],
  [8u352-8.66.0.15][255],
  [8u362-8.68.0.19][256],
  [8u362-8.68.0.21][257],
  [8u372-8.70.0.23][258],
  [8u382-8.72.0.17][259],
  
  * [7-latest][301],
  [7u141-7.18.0.3][302],
  [7u154-7.20.0.3][303],
  [7u161-7.21.0.3][304],
  [7u171-7.22.0.3][305],
  [7u181-7.23.0.1][306],
  [7u191-7.24.0.1][307],
  [7u201-7.25.0.5][308],
  [7u211-7.27.0.1][309],
  [7u222-7.29.0.5][310],
  [7u232-7.31.0.5][311],
  [7u242-7.34.0.5][312],
  [7u252-7.36.0.5][313],
  [7u262-7.38.0.11][314],
  [7u272-7.40.0.15][315],
  [7u282-7.42.0.13][316],
  [7u285-7.42.0.51][317],
  [7u292-7.44.0.11][318],
  [7u302-7.46.0.11][319],
  [7u312-7.48.0.11][320],
  [7u332-7.52.0.11][321],
  [7u342-7.54.0.13][322],
  [7u352-7.56.0.11][323],
  
  * [6-latest][324],
  [6u93-6.16.0.1][325],
  [6u97-6.17.0.1][326],
  [6u99-6.18.0.3][327],
  [6u103-6.19.0.1][328],
  [6u107-6.20.0.1][329],
  [6u113-6.21.0.3][330],
  [6u119-6.22.0.3][331],
  

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


  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-headless-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre-headless/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-headless-latest/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre-headless/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre-headless/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre-headless/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre-headless/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre-headless/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre-headless/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre-headless/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre-headless/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre-headless/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15-jre-headless/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre-headless/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53-jre-headless/Dockerfile
  
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre-headless/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre-headless/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre-headless/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre-headless/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre-headless/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre-headless/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre-headless/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre-headless/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre-headless/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre-headless/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre-headless/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15-jre-headless/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre-headless/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19-jre-headless/Dockerfile
  
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre-headless/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre-headless/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre-headless/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre-headless/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre-headless/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre-headless/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre-headless/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre/Dockerfile
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre/Dockerfile
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15-jre/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53-jre/Dockerfile
  
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17-jre/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre/Dockerfile
  
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre/Dockerfile
  
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15-jre/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19-jre/Dockerfile
  
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17-jre/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-latest/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13/Dockerfile
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8-17.44.15/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.8.1-17.44.53/Dockerfile
  
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17/Dockerfile
  
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17/Dockerfile
  
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20-11.66.15/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.20.1-11.66.19/Dockerfile
  
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u382-8.72.0.17/Dockerfile
  
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u342-7.54.0.13/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u352-7.56.0.11/Dockerfile
  
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  