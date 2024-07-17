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


  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][32]
  * [`21.0.4-21.36`, `21-latest` (*21-latest/Dockerfile)*][44]
  * [`17.0.12-17.52`, `17-latest` (*17-latest/Dockerfile)*][102]
  * [`11.0.24-11.74`, `11-latest` (*11-latest/Dockerfile)*][216]
  * [`8u422-8.80`, `8-latest` (*8-latest/Dockerfile)*][281]

Previous
--------

Earlier CentOS Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


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
  [18-jre-headless-latest][92],
  [18.0.1-18.30.11-jre-headless][93],
  [18.0.2.1-18.32.13-jre-headless][97],
  
  
  *[17-jre-headless-latest][16],
  [17-jre-headless-latest][104],
  [17.0.0-17.28.13-jre-headless][105],
  [17.0.1-17.30.15-jre-headless][110],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][17],
  [15-jre-headless-latest][163],
  [15.0.7-15.40.19-jre-headless][173],
  [15.0.8-15.42.15-jre-headless][177],
  
  
  
  *[13-jre-headless-latest][18],
  [13-jre-headless-latest][189],
  [13.0.11-13.48.19-jre-headless][201],
  [13.0.12-13.50.15-jre-headless][205],
  
  
  
  *[11-jre-headless-latest][19],
  [11-jre-headless-latest][218],
  [11.0.15-11.56.19-jre-headless][235],
  [11.0.16.1-11.58.23-jre-headless][237],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][20],
  [8-jre-headless-latest][283],
  [8u332-8.62.0.19-jre-headless][321],
  [8u342-8.64.0.15-jre-headless][325],
  
  
  
  
  
  
  
  
  
  
  
  
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
  [18-jre-latest][91],
  [18.0.1-18.30.11-jre][95],
  [18.0.2.1-18.32.13-jre][96],
  
  
  *[17-jre-latest][26],
  [17-jre-latest][103],
  [17.0.0-17.28.13-jre][107],
  [17.0.1-17.30.15-jre][108],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][27],
  [16-jre-latest][154],
  [16.0.0-16.28.11-jre][156],
  [16.0.1-16.30.15-jre][157],
  
  
  *[15-jre-latest][28],
  [15-jre-latest][162],
  [15.0.7-15.40.19-jre][172],
  [15.0.8-15.42.15-jre][176],
  
  
  
  *[13-jre-latest][29],
  [13-jre-latest][188],
  [13.0.11-13.48.19-jre][202],
  [13.0.12-13.50.15-jre][203],
  
  
  
  *[11-jre-latest][30],
  [11-jre-latest][217],
  [11.0.15-11.56.19-jre][234],
  [11.0.16.1-11.58.23-jre][239],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][31],
  [8-jre-latest][282],
  [8u332-8.62.0.19-jre][322],
  [8u342-8.64.0.15-jre][326],
  
  
  
  
  
  
  
  
  
  
  
  
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
  
  
  *[18-latest][90],
  [18.0.1-18.30.11][94],
  [18.0.2.1-18.32.13][98],
  [18.0.2-18.32.11][101],
  
  *[17-latest][102],
  [17.0.0-17.28.13][106],
  [17.0.1-17.30.15][109],
  [17.0.2-17.32.13][111],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][153],
  [16.0.0-16.28.11][155],
  [16.0.1-16.30.15][158],
  [16.0.2-16.32.15][159],
  
  *[15-latest][161],
  [15.0.0-15.27.17][164],
  [15.0.1-15.28.13][165],
  [15.0.1-15.28.51][166],
  
  
  
  
  
  
  
  
  
  
  *[14-latest][184],
  [14.0.1-14.28.21][185],
  [14.0.2-14.29.23][186],
  
  *[13-latest][187],
  [13.0.1-13.28][190],
  [13.0.2-13.29][191],
  [13.0.3-13.31.11][192],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][212],
  [12.0.1-12.2][213],
  [12.0.2-12.3][214],
  [12-12.1][215],
  
  *[11-latest][216],
  [11.0.1-11.2][219],
  [11.0.2-11.29][220],
  [11.0.3-11.31][221],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][273],
  [10u01-10.2][274],
  [10u02-10.3][275],
  
  *[9-latest][276],
  [9-ea][277],
  [9u01-9.0.1.3][278],
  [9u04-9.0.4.1][279],
  
  
  *[8-latest][281],
  [8u11-8.2.0.1][284],
  [8u20-8.3.0.1][285],
  [8u25-8.4.0.1][286],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][360],
  [7u65-7.6.0.1][361],
  [7u72-7.7.0.1][362],
  [7u76-7.8.0.3][363],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][395],
  [6u53-6.5.0.2][396],
  [6u56-6.6.0.1][397],
  [6u59-6.7.0.2][398],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-headless-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-headless-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28-jre-headless/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30-jre-headless/Dockerfile
  
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-headless-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-headless-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre-headless/Dockerfile
  
  
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-headless-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-headless-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre-headless/Dockerfile
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-headless-latest/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-headless-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre-headless/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre-headless/Dockerfile
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-headless-latest/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-headless-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre-headless/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-headless-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-headless-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre-headless/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-headless-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-headless-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre-headless/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre-headless/Dockerfile
  
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-headless-latest/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-headless-latest/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre-headless/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre-headless/Dockerfile
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-headless-latest/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-headless-latest/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre-headless/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-headless-latest/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-headless-latest/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre-headless/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30-jre/Dockerfile
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre/Dockerfile
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre/Dockerfile
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-latest/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-latest/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre/Dockerfile
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-latest/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-latest/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre/Dockerfile
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-jre-latest/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-jre-latest/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11-jre/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15-jre/Dockerfile
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-latest/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-latest/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre/Dockerfile
  
  
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-latest/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-latest/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre/Dockerfile
  
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-latest/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-latest/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.15-11.56.19-jre/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.16.1-11.58.23-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-latest/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-latest/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u332-8.62.0.19-jre/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u342-8.64.0.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.2-22.32/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.0-21.28.85/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30.15/Dockerfile
  
  
  
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11/Dockerfile
  
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-latest/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13/Dockerfile
  
  
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-latest/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11/Dockerfile
  
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-latest/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.0-17.28.13/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.1-17.30.15/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-latest/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15/Dockerfile
  
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.0-15.27.17/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.13/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.51/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14-latest/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.1-14.28.21/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.2-14.29.23/Dockerfile
  
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-latest/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.1-13.28/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.2-13.29/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-latest/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.1-12.2/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.2-12.3/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-12.1/Dockerfile
  
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-latest/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.1-11.2/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.2-11.29/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10-latest/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u01-10.2/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u02-10.3/Dockerfile
  
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-latest/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-ea/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u01-9.0.1.3/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u04-9.0.4.1/Dockerfile
  
  
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-latest/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u11-8.2.0.1/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u20-8.3.0.1/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u25-8.4.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [360]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7-latest/Dockerfile
  [361]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [362]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [363]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [395]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6-latest/Dockerfile
  [396]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [397]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [398]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  