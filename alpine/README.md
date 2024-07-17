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


  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][32]
  * [`21.0.4-21.36`, `21-latest` (*21-latest/Dockerfile)*][44]
  * [`17.0.12-17.52`, `17-latest` (*17-latest/Dockerfile)*][101]
  * [`11.0.24-11.74`, `11-latest` (*11-latest/Dockerfile)*][232]
  * [`8u422-8.80`, `8-latest` (*8-latest/Dockerfile)*][312]

Previous
--------

Earlier Alpine Docker image tags (the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[22-jre-headless-latest][11],
  [22-jre-headless-latest][34],
  [22.0.0-22.28-jre-headless][35],
  [22.0.1-22.30-jre-headless][39],
  
  
  *[21-jre-headless-latest][12],
  [21-jre-headless-latest][46],
  [21.0.0-21.28.85-jre-headless][47],
  [21.0.1-21.30-jre-headless][51],
  
  
  
  
  
  *[20-jre-headless-latest][13],
  [20-jre-headless-latest][67],
  [20.0.0-20.28.85-jre-headless][70],
  [20.0.1-20.30.11-jre-headless][72],
  
  
  *[19-jre-headless-latest][14],
  [19-jre-headless-latest][78],
  [19.0.0-19.28.81-jre-headless][80],
  [19.0.1-19.30.11-jre-headless][84],
  
  
  *[18-jre-headless-latest][15],
  [18-jre-headless-latest][91],
  [18.0.1-18.30.11-jre-headless][92],
  [18.0.2.1-18.32.13-jre-headless][96],
  
  
  *[17-jre-headless-latest][16],
  [17-jre-headless-latest][103],
  [17.0.0-17.28.13-jre-headless][104],
  [17.0.1-17.30.15-jre-headless][109],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][17],
  [15-jre-headless-latest][162],
  [15.0.7-15.40.19-jre-headless][173],
  [15.0.8-15.42.15-jre-headless][177],
  
  
  
  *[13-jre-headless-latest][18],
  [13-jre-headless-latest][189],
  [13.0.3-13.31.11-jre-headless][192],
  [13.0.4-13.33.25-jre-headless][197],
  
  
  
  
  
  
  
  
  
  
  
  *[11-jre-headless-latest][19],
  [11-jre-headless-latest][234],
  [11.0.5-11.35-jre-headless][241],
  [11.0.6-11.37-jre-headless][246],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][20],
  [8-jre-headless-latest][314],
  [8u232-8.42.0.23-jre-headless][331],
  [8u242-8.44.0.11-jre-headless][334],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[22-jre-latest][21],
  [22-jre-latest][33],
  [22.0.0-22.28-jre][37],
  [22.0.1-22.30-jre][38],
  
  
  *[21-jre-latest][22],
  [21-jre-latest][45],
  [21.0.0-21.28.85-jre][49],
  [21.0.1-21.30-jre][50],
  
  
  
  
  
  *[20-jre-latest][23],
  [20-jre-latest][66],
  [20.0.0-20.28.85-jre][69],
  [20.0.1-20.30.11-jre][73],
  
  
  *[19-jre-latest][24],
  [19-jre-latest][79],
  [19.0.0-19.28.81-jre][82],
  [19.0.1-19.30.11-jre][83],
  
  
  *[18-jre-latest][25],
  [18-jre-latest][90],
  [18.0.1-18.30.11-jre][94],
  [18.0.2.1-18.32.13-jre][95],
  
  
  *[17-jre-latest][26],
  [17-jre-latest][102],
  [17.0.0-17.28.13-jre][106],
  [17.0.1-17.30.15-jre][107],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][27],
  [16-jre-latest][153],
  [16.0.0-16.28.11-jre][155],
  [16.0.1-16.30.15-jre][156],
  
  
  *[15-jre-latest][28],
  [15-jre-latest][161],
  [15.0.0-15.27.17-jre][163],
  [15.0.7-15.40.19-jre][172],
  
  
  
  
  *[13-jre-latest][29],
  [13-jre-latest][188],
  [13.0.3-13.31.11-jre][194],
  [13.0.4-13.33.25-jre][196],
  
  
  
  
  
  
  
  
  
  
  
  *[11-jre-latest][30],
  [11-jre-latest][233],
  [11.0.3-11.31-jre][237],
  [11.0.4-11.33-jre][240],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][31],
  [8-jre-latest][313],
  [8u212-8.38.0.13-jre][324],
  [8u222-8.40.0.25-jre][325],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[22-latest][32],
  [22.0.0-22.28][36],
  [22.0.1-22.30][40],
  [22.0.2-22.32][41],
  
  *[21-latest][44],
  [21.0.0-21.28.85][48],
  [21.0.1-21.30][52],
  [21.0.1-21.30.15][54],
  
  
  
  
  *[20-latest][65],
  [20.0.0-20.28.85][68],
  [20.0.1-20.30.11][71],
  [20.0.2-20.32.11][74],
  
  *[19-latest][77],
  [19.0.0-19.28.81][81],
  [19.0.1-19.30.11][85],
  [19.0.2-19.32.13][87],
  
  *[18-latest][89],
  [18.0.1-18.30.11][93],
  [18.0.2.1-18.32.13][97],
  [18.0.2-18.32.11][100],
  
  *[17-latest][101],
  [17.0.0-17.28.13][105],
  [17.0.1-17.30.15][108],
  [17.0.2-17.32.13][110],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][152],
  [16.0.0-16.28.11][154],
  [16.0.1-16.30.15][157],
  [16.0.2-16.32.15][158],
  
  *[15-latest][160],
  [15.0.0-15.27.17][164],
  [15.0.1-15.28.13][165],
  [15.0.1-15.28.51][166],
  
  
  
  
  
  
  
  
  
  
  *[14-latest][184],
  [14.0.1-14.28.21][185],
  [14.0.2-14.29.23][186],
  
  *[13-latest][187],
  [13.0.1-13.28][190],
  [13.0.2-13.29][191],
  [13.0.3-13.31.11][193],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][228],
  [12.0.0-12.1][229],
  [12.0.1-12.2][230],
  [12.0.2-12.3][231],
  
  *[11-latest][232],
  [11.0.1-11.2][235],
  [11.0.2-11.29][236],
  [11.0.3-11.31][238],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-latest][312],
  [8u131-8.21.0.1][315],
  [8u144-8.23.0.3][316],
  [8u152-8.25.0.1][317],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][400],
  [7u141-7.18.0.3][401],
  [7u154-7.20.0.3][402],
  [7u161-7.21.0.3][403],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][423],
  [6u93-6.16.0.1][424],
  [6u97-6.17.0.1][425],
  [6u99-6.18.0.3][426],
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22-jre-headless-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22-jre-headless-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.0-22.28-jre-headless/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.1-22.30-jre-headless/Dockerfile
  
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-headless-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-headless-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30-jre-headless/Dockerfile
  
  
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-headless-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-headless-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre-headless/Dockerfile
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-headless-latest/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-headless-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre-headless/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre-headless/Dockerfile
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre-headless/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre-headless/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre-headless/Dockerfile
  
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22-jre-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22-jre-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.0-22.28-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.1-22.30-jre/Dockerfile
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-jre-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30-jre/Dockerfile
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre/Dockerfile
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-latest/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-latest/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre/Dockerfile
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre/Dockerfile
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17-jre/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre/Dockerfile
  
  
  
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.0-22.28/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.1-22.30/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/22.0.2-22.32/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.0-21.28.85/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/21.0.1-21.30.15/Dockerfile
  
  
  
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.2-20.32.11/Dockerfile
  
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-latest/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13/Dockerfile
  
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11/Dockerfile
  
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [400]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [401]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [402]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [403]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [423]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [424]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [425]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [426]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  
  
  
  
  