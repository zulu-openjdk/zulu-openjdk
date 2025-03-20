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


  * [`24.0.0-24.28`, `24-latest` (*24-latest/Dockerfile)*][36]
  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][50]
  * [`21.0.6-21.40`, `21-latest` (*21-latest/Dockerfile)*][60]
  * [`17.0.14-17.56`, `17-latest` (*17-latest/Dockerfile)*][116]
  * [`11.0.26-11.78`, `11-latest` (*11-latest/Dockerfile)*][228]
  * [`8u442-8.84`, `8-latest` (*8-latest/Dockerfile)*][297]

Previous
--------

Earlier Debian Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[24-jre-headless-latest][11],
  [24.0.0-24.28-jre-headless][39],
  
  *[23-jre-headless-latest][12],
  [23.0.0-23.28-jre-headless][43],
  [23.0.1-23.30-jre-headless][45],
  [23.0.2-23.32-jre-headless][49],
  
  *[22-jre-headless-latest][13],
  [22.0.0-22.28-jre-headless][51],
  [22.0.1-22.30-jre-headless][55],
  [22.0.2-22.32-jre-headless][59],
  
  *[21-jre-headless-latest][14],
  [21.0.0-21.28.85-jre-headless][61],
  [21.0.1-21.30-jre-headless][65],
  [21.0.1-21.30.15-jre-headless][67],
  
  
  
  
  
  
  *[20-jre-headless-latest][15],
  [20.0.0-20.28.85-jre-headless][88],
  [20.0.1-20.30.11-jre-headless][90],
  [20.0.2-20.32.11-jre-headless][94],
  
  *[19-jre-headless-latest][16],
  [19.0.0-19.28.81-jre-headless][96],
  [19.0.1-19.30.11-jre-headless][100],
  [19.0.2-19.32.13-jre-headless][104],
  
  *[18-jre-headless-latest][17],
  [18.0.1-18.30.11-jre-headless][107],
  [18.0.2.1-18.32.13-jre-headless][111],
  [18.0.2-18.32.11-jre-headless][113],
  
  *[17-jre-headless-latest][18],
  [17.0.0-17.28.13-jre-headless][117],
  [17.0.1-17.30.15-jre-headless][122],
  [17.0.2-17.32.13-jre-headless][125],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][19],
  [15.0.7-15.40.19-jre-headless][187],
  [15.0.8-15.42.15-jre-headless][191],
  [15.0.9-15.44.13-jre-headless][193],
  
  
  *[13-jre-headless-latest][20],
  [13.0.11-13.48.19-jre-headless][213],
  [13.0.12-13.50.15-jre-headless][217],
  [13.0.13-13.52.15-jre-headless][218],
  
  
  *[11-jre-headless-latest][21],
  [11.0.15-11.56.19-jre-headless][245],
  [11.0.16.1-11.58.23-jre-headless][247],
  [11.0.16-11.58.15-jre-headless][251],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][22],
  [8u332-8.62.0.19-jre-headless][336],
  [8u342-8.64.0.15-jre-headless][340],
  [8u345-8.64.0.19-jre-headless][343],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[24-jre-latest][23],
  [24.0.0-24.28-jre][38],
  
  *[23-jre-latest][24],
  [23.0.0-23.28-jre][41],
  [23.0.1-23.30-jre][46],
  [23.0.2-23.32-jre][48],
  
  *[22-jre-latest][25],
  [22.0.0-22.28-jre][53],
  [22.0.1-22.30-jre][54],
  [22.0.2-22.32-jre][58],
  
  *[21-jre-latest][26],
  [21.0.0-21.28.85-jre][63],
  [21.0.1-21.30-jre][64],
  [21.0.1-21.30.15-jre][69],
  
  
  
  
  
  
  *[20-jre-latest][27],
  [20.0.0-20.28.85-jre][87],
  [20.0.1-20.30.11-jre][91],
  [20.0.2-20.32.11-jre][93],
  
  *[19-jre-latest][28],
  [19.0.0-19.28.81-jre][98],
  [19.0.1-19.30.11-jre][99],
  [19.0.2-19.32.13-jre][102],
  
  *[18-jre-latest][29],
  [18.0.1-18.30.11-jre][109],
  [18.0.2.1-18.32.13-jre][110],
  [18.0.2-18.32.11-jre][114],
  
  *[17-jre-latest][30],
  [17.0.0-17.28.13-jre][119],
  [17.0.1-17.30.15-jre][120],
  [17.0.2-17.32.13-jre][124],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][31],
  [16.0.0-16.28.11-jre][173],
  [16.0.1-16.30.15-jre][174],
  [16.0.2-16.32.15-jre][177],
  
  *[15-jre-latest][32],
  [15.0.7-15.40.19-jre][186],
  [15.0.8-15.42.15-jre][190],
  [15.0.9-15.44.13-jre][192],
  
  
  *[13-jre-latest][33],
  [13.0.11-13.48.19-jre][214],
  [13.0.12-13.50.15-jre][215],
  [13.0.13-13.52.15-jre][220],
  
  
  *[11-jre-latest][34],
  [11.0.15-11.56.19-jre][244],
  [11.0.16.1-11.58.23-jre][249],
  [11.0.16-11.58.15-jre][252],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][35],
  [8u332-8.62.0.19-jre][337],
  [8u342-8.64.0.15-jre][341],
  [8u345-8.64.0.19-jre][344],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[24-latest][36],
  [24.0.0-24.28][37],
  
  *[23-latest][40],
  [23.0.0-23.28][42],
  [23.0.1-23.30][44],
  [23.0.2-23.32][47],
  
  *[22-latest][50],
  [22.0.0-22.28][52],
  [22.0.1-22.30][56],
  [22.0.2-22.32][57],
  
  *[21-latest][60],
  [21.0.0-21.28.85][62],
  [21.0.1-21.30][66],
  [21.0.1-21.30.15][68],
  
  
  
  
  
  
  *[20-latest][85],
  [20.0.0-20.28.85][86],
  [20.0.1-20.30.11][89],
  [20.0.2-20.32.11][92],
  
  *[19-latest][95],
  [19.0.0-19.28.81][97],
  [19.0.1-19.30.11][101],
  [19.0.2-19.32.13][103],
  
  
  *[18-latest][106],
  [18.0.1-18.30.11][108],
  [18.0.2.1-18.32.13][112],
  [18.0.2-18.32.11][115],
  
  *[17-latest][116],
  [17.0.0-17.28.13][118],
  [17.0.1-17.30.15][121],
  [17.0.2-17.32.13][123],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][171],
  [16.0.0-16.28.11][172],
  [16.0.1-16.30.15][175],
  [16.0.2-16.32.15][176],
  
  *[15-latest][178],
  [15.0.1-15.28.13][179],
  [15.0.1-15.28.51][180],
  [15.0.2-15.29.15][181],
  
  
  
  
  
  
  
  
  
  *[14-latest][198],
  [14.0.1-14.28.21][199],
  [14.0.2-14.29.23][200],
  
  *[13-latest][201],
  [13.0.1-13.28][202],
  [13.0.2-13.29][203],
  [13.0.3-13.31.11][204],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][224],
  [12.0.1-12.2][225],
  [12.0.2-12.3][226],
  [12-12.1][227],
  
  *[11-latest][228],
  [11.0.1-11.2][229],
  [11.0.2-11.29][230],
  [11.0.3-11.31][231],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][289],
  [10u01-10.2][290],
  [10u02-10.3][291],
  
  *[9-latest][292],
  [9-ea][293],
  [9u01-9.0.1.3][294],
  [9u04-9.0.4.1][295],
  
  
  *[8-latest][297],
  [8u05-8.1.0.6][298],
  [8u11-8.2.0.1][299],
  [8u20-8.3.0.1][300],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][381],
  [7u55-7.4.0.5][382],
  [7u60-7.5.0.1][383],
  [7u65-7.6.0.1][384],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][419],
  [6u49-6.4.0.6][420],
  [6u53-6.5.0.2][421],
  [6u56-6.6.0.1][422],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-jre-headless-latest/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-headless-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre-headless/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre-headless/Dockerfile
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-headless-latest/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre-headless/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre-headless/Dockerfile
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-headless-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre-headless/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre-headless/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-jre-latest/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre/Dockerfile
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-latest/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre/Dockerfile
  
  
  
  
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre/Dockerfile
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  [341]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32/Dockerfile
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-latest/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32/Dockerfile
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15/Dockerfile
  
  
  
  
  
  
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11/Dockerfile
  
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  
  
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  
  
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [381]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [382]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [383]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [384]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [419]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [420]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [421]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [422]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  