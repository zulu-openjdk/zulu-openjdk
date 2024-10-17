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


  * [`23.0.1-23.30`, `23-latest` (*23-latest/Dockerfile)*][42]
  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][55]
  * [`21.0.5-21.38`, `21-latest` (*21-latest/Dockerfile)*][73]
  * [`17.0.13-17.54`, `17-latest` (*17-latest/Dockerfile)*][143]
  * [`11.0.25-11.76`, `11-latest` (*11-latest/Dockerfile)*][268]
  * [`8u432-8.82`, `8-latest` (*8-latest/Dockerfile)*][336]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 3 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[23-jre-headless-latest][11],
  [23-jre-headless-latest][44],
  [23.0.0-23.28-jre-headless][51],
  
  
  *[22-jre-headless-latest][12],
  [22-jre-headless-latest][58],
  [22.0.0-22.28-jre-headless][60],
  
  
  
  *[21-jre-headless-latest][13],
  [21-jre-headless-latest][77],
  [21.0.0-21.28.85-jre-headless][78],
  
  
  
  
  
  
  
  *[20-jre-headless-latest][14],
  [20-jre-headless-latest][108],
  [20.0.0-20.28.85-jre-headless][111],
  
  
  
  *[19-jre-headless-latest][15],
  [19-jre-headless-latest][119],
  [19.0.0-19.28.81-jre-headless][121],
  
  
  
  *[18-jre-headless-latest][16],
  [18-jre-headless-latest][133],
  [18.0.1-18.30.11-jre-headless][134],
  
  
  
  *[17-jre-headless-latest][17],
  [17-jre-headless-latest][147],
  [17.0.0-17.28.13-jre-headless][148],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][18],
  [15-jre-headless-latest][216],
  [15.0.7-15.40.19-jre-headless][225],
  
  
  
  
  *[13-jre-headless-latest][19],
  [13-jre-headless-latest][241],
  [13.0.11-13.48.19-jre-headless][253],
  
  
  
  
  *[11-jre-headless-latest][20],
  [11-jre-headless-latest][270],
  [11.0.15-11.56.19-jre-headless][287],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][21],
  [8-jre-headless-latest][338],
  [8u332-8.62.0.19-jre-headless][376],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[23-jre-crac-latest][22],
  [23-jdk-crac-latest][23],
  [23-jre-crac-latest][43],
  
  
  
  
  *[23-jre-crac-latest][22],
  [23-jdk-crac-latest][23],
  [23-jre-crac-latest][43],
  
  
  
  
  *[22-jre-crac-latest][24],
  [22-jdk-crac-latest][25],
  [22-jre-crac-latest][56],
  
  
  
  
  
  
  *[22-jre-crac-latest][24],
  [22-jdk-crac-latest][25],
  [22-jre-crac-latest][56],
  
  
  
  
  
  
  *[21-jre-crac-latest][26],
  [21-jdk-crac-latest][27],
  [21-jre-crac-latest][74],
  
  
  
  
  
  
  
  
  
  *[21-jre-crac-latest][26],
  [21-jdk-crac-latest][27],
  [21-jre-crac-latest][74],
  
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][28],
  [17-jdk-crac-latest][29],
  [17-jre-crac-latest][144],
  
  
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][28],
  [17-jdk-crac-latest][29],
  [17-jre-crac-latest][144],
  
  
  
  
  
  
  
  
  
  
  *[23-jre-latest][30],
  [23-jre-latest][46],
  [23.0.0-23.28-jre][47],
  
  
  *[22-jre-latest][31],
  [22-jre-latest][57],
  [22.0.0-22.28-jre][63],
  
  
  
  *[21-jre-latest][32],
  [21-jre-latest][75],
  [21.0.0-21.28.85-jre][80],
  
  
  
  
  
  
  
  *[20-jre-latest][33],
  [20-jre-latest][107],
  [20.0.0-20.28.85-jre][110],
  
  
  
  *[19-jre-latest][34],
  [19-jre-latest][120],
  [19.0.0-19.28.81-jre][123],
  
  
  
  *[18-jre-latest][35],
  [18-jre-latest][132],
  [18.0.1-18.30.11-jre][136],
  
  
  
  *[17-jre-latest][36],
  [17-jre-latest][145],
  [17.0.0-17.28.13-jre][150],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][37],
  [16-jre-latest][208],
  [16.0.0-16.28.11-jre][210],
  
  
  
  *[15-jre-latest][38],
  [15-jre-latest][215],
  [15.0.7-15.40.19-jre][224],
  
  
  
  
  *[13-jre-latest][39],
  [13-jre-latest][240],
  [13.0.11-13.48.19-jre][254],
  
  
  
  
  *[11-jre-latest][40],
  [11-jre-latest][269],
  [11.0.15-11.56.19-jre][286],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][41],
  [8-jre-latest][337],
  [8u332-8.62.0.19-jre][377],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[23-latest][42],
  [23.0.0-23.28][49],
  [23.0.1-23.30][52],
  
  *[22-latest][55],
  [22.0.0-22.28][61],
  [22.0.1-22.30][67],
  
  
  *[21-latest][73],
  [21.0.0-21.28.85][79],
  [21.0.1-21.30][85],
  
  
  
  
  
  
  *[20-latest][106],
  [20.0.0-20.28.85][109],
  [20.0.1-20.30.11][112],
  
  
  *[19-latest][118],
  [19.0.0-19.28.81][122],
  [19.0.1-19.30.11][126],
  
  
  
  *[18-latest][131],
  [18.0.1-18.30.11][135],
  [18.0.2.1-18.32.13][139],
  
  
  *[17-latest][143],
  [17.0.0-17.28.13][149],
  [17.0.1-17.30.15][152],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][207],
  [16.0.0-16.28.11][209],
  [16.0.2-16.32.15][212],
  
  *[15-latest][214],
  [15.0.1-15.28.13][217],
  [15.0.1-15.28.51][218],
  
  
  
  
  
  
  
  
  
  
  *[14-latest][236],
  [14.0.1-14.28.21][237],
  [14.0.2-14.29.23][238],
  
  *[13-latest][239],
  [13.0.1-13.28][242],
  [13.0.2-13.29][243],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][264],
  [12.0.1-12.2][265],
  [12.0.2-12.3][266],
  
  
  *[11-latest][268],
  [11.0.1-11.2][271],
  [11.0.2-11.29][272],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][328],
  [10u01-10.2][329],
  [10u02-10.3][330],
  
  *[9-latest][331],
  [9-ea][332],
  [9u01-9.0.1.3][333],
  
  
  
  *[8-latest][336],
  [8u05-8.1.0.6][339],
  [8u11-8.2.0.1][340],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][418],
  [7u55-7.4.0.5][419],
  [7u60-7.5.0.1][420],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][456],
  [6u49-6.4.0.6][457],
  [6u53-6.5.0.2][458],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-headless-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-headless-latest/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre-headless/Dockerfile
  
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre-headless/Dockerfile
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  
  
  
  
  
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [338]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [376]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre/Dockerfile
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre/Dockerfile
  
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  
  
  
  
  
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  
  
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  
  
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  
  
  
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [337]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [377]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30/Dockerfile
  
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30/Dockerfile
  
  
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  
  
  
  
  
  
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  
  
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  
  
  
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  
  
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  
  
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [332]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [333]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  
  
  
  [336]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [339]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  [340]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u11-8.2.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [418]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [419]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [420]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [456]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [457]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [458]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  