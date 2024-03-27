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


  * [`22.0.0-22.28`, `22-latest` (*22-latest/Dockerfile)*][11]
  * [`21.0.1-21.30.15`, `21-latest` (*21-latest/Dockerfile)*][19]
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][39]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][51]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][64]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][76]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][127]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][134]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][156]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][159]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][184]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][188]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][239]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][242]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][247]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][320]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][358]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[22-jre-headless-latest][17],
  [22.0.0-22.28-jre-headless][18],
  
  *[21-jre-headless-latest][32],
  [21.0.1-21.30-jre-headless][35],
  [21.0.2-21.32-jre-headless][36],
  [21.0.0-21.28.85-jre-headless][37],
  
  
  *[20-jre-headless-latest][47],
  [20.0.0-20.28.85-jre-headless][48],
  [20.0.1-20.30.11-jre-headless][49],
  [20.0.2-20.32.11-jre-headless][50],
  
  *[19-jre-headless-latest][60],
  [19.0.0-19.28.81-jre-headless][61],
  [19.0.1-19.30.11-jre-headless][62],
  [19.0.2-19.32.13-jre-headless][63],
  
  *[18-jre-headless-latest][72],
  [18.0.1-18.30.11-jre-headless][73],
  [18.0.2-18.32.11-jre-headless][74],
  [18.0.2.1-18.32.13-jre-headless][75],
  
  *[17-jre-headless-latest][108],
  [17.0.9-17.46-jre-headless][112],
  [17.0.10-17.48-jre-headless][113],
  [17.0.0-17.28.13-jre-headless][115],
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][151],
  [15.0.7-15.40.19-jre-headless][152],
  [15.0.8-15.42.15-jre-headless][153],
  [15.0.9-15.44.13-jre-headless][154],
  
  
  *[13-jre-headless-latest][179],
  [13.0.11-13.48.19-jre-headless][180],
  [13.0.12-13.50.15-jre-headless][181],
  [13.0.13-13.52.15-jre-headless][182],
  
  
  *[11-jre-headless-latest][225],
  [11.0.21-11.68-jre-headless][228],
  [11.0.22-11.70-jre-headless][229],
  [11.0.15-11.56.19-jre-headless][230],
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][308],
  [8u392-8.74-jre-headless][309],
  [8u402-8.76-jre-headless][310],
  [8u332-8.62.0.19-jre-headless][311],
  
  
  
  
  
  
  
  
  
  *[22-jdk-crac-latest][15],
  [22.0.0-22.28-jdk-crac][16],
  
  *[21-jdk-crac-latest][27],
  [21.0.1-21.30-jdk-crac][30],
  [21.0.2-21.32-jdk-crac][31],
  [21.0.0-21.28.89-jdk-crac][33],
  
  
  *[17-jdk-crac-latest][94],
  [17.0.9-17.46-jdk-crac][107],
  [17.0.10-17.48-jdk-crac][109],
  [17.0.8-17.44.17-jdk-crac][110],
  
  
  
  *[22-jre-latest][13],
  [22.0.0-22.28-jre][14],
  
  *[21-jre-latest][22],
  [21.0.1-21.30-jre][25],
  [21.0.2-21.32-jre][26],
  [21.0.0-21.28.85-jre][28],
  
  
  *[20-jre-latest][40],
  [20.0.0-20.28.85-jre][44],
  [20.0.1-20.30.11-jre][45],
  [20.0.2-20.32.11-jre][46],
  
  *[19-jre-latest][52],
  [19.0.0-19.28.81-jre][57],
  [19.0.1-19.30.11-jre][58],
  [19.0.2-19.32.13-jre][59],
  
  *[18-jre-latest][65],
  [18.0.1-18.30.11-jre][69],
  [18.0.2-18.32.11-jre][70],
  [18.0.2.1-18.32.13-jre][71],
  
  *[17-jre-latest][78],
  [17.0.9-17.46-jre][90],
  [17.0.10-17.48-jre][91],
  [17.0.0-17.28.13-jre][95],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][128],
  [16.0.0-16.28.11-jre][131],
  [16.0.1-16.30.15-jre][132],
  [16.0.2-16.32.15-jre][133],
  
  *[15-jre-latest][135],
  [15.0.7-15.40.19-jre][147],
  [15.0.8-15.42.15-jre][148],
  [15.0.9-15.44.13-jre][149],
  
  
  *[13-jre-latest][162],
  [13.0.11-13.48.19-jre][175],
  [13.0.12-13.50.15-jre][176],
  [13.0.13-13.52.15-jre][177],
  
  
  *[11-jre-latest][195],
  [11.0.21-11.68-jre][213],
  [11.0.22-11.70-jre][214],
  [11.0.15-11.56.19-jre][218],
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][250],
  [8u392-8.74-jre][275],
  [8u402-8.76-jre][276],
  [8u332-8.62.0.19-jre][299],
  
  
  
  
  
  
  
  
  
  *[22-latest][11],
  [22.0.0-22.28][12],
  
  *[21-latest][19],
  [21.0.1-21.30][20],
  [21.0.2-21.32][21],
  [21.0.0-21.28.85][23],
  
  
  *[20-latest][39],
  [20.0.0-20.28.85][41],
  [20.0.1-20.30.11][42],
  [20.0.2-20.32.11][43],
  
  *[19-latest][51],
  [19.0.0-19.28.81][53],
  [19.0.1-19.30.11][54],
  [19.0.2-19.32.13][55],
  
  
  *[18-latest][64],
  [18.0.1-18.30.11][66],
  [18.0.2-18.32.11][67],
  [18.0.2.1-18.32.13][68],
  
  *[17-latest][76],
  [17.0.9-17.46][77],
  [17.0.10-17.48][79],
  [17.0.0-17.28.13][80],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][127],
  [16.0.0-16.28.11][129],
  [16.0.2-16.32.15][130],
  
  *[15-latest][134],
  [15.0.1-15.28.13][136],
  [15.0.1-15.28.51][137],
  [15.0.2-15.29.15][138],
  
  
  
  
  
  
  
  
  
  *[14-latest][156],
  [14.0.1-14.28.21][157],
  [14.0.2-14.29.23][158],
  
  *[13-latest][159],
  [13.0.1-13.28][160],
  [13.0.2-13.29][161],
  [13.0.3-13.31.11][163],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-12.1][184],
  [12-latest][185],
  [12.0.1-12.2][186],
  [12.0.2-12.3][187],
  
  *[11-latest][188],
  [11.0.1-11.2][189],
  [11.0.2-11.29][190],
  [11.0.3-11.31][191],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][239],
  [10u01-10.2][240],
  [10u02-10.3][241],
  
  *[9-ea][242],
  [9-latest][243],
  [9u01-9.0.1.3][244],
  [9u04-9.0.4.1][245],
  
  
  *[8-latest][247],
  [8u392-8.74][248],
  [8u402-8.76][249],
  [8u05-8.1.0.6][251],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][320],
  [7u55-7.4.0.5][321],
  [7u60-7.5.0.1][322],
  [7u65-7.6.0.1][323],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][358],
  [6u49-6.4.0.6][359],
  [6u53-6.5.0.2][360],
  [6u56-6.6.0.1][361],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre-headless/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jre-headless/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre-headless/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre-headless/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jre-headless/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre-headless/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.22-11.70-jre-headless/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre-headless/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76-jre-headless/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jdk-crac/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jdk-crac/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jdk-crac/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.89-jdk-crac/Dockerfile
  
  
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jdk-crac/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jdk-crac/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.17-jdk-crac/Dockerfile
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jre/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15-jre/Dockerfile
  
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre/Dockerfile
  
  
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre/Dockerfile
  
  
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.22-11.70-jre/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76-jre/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11/Dockerfile
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13/Dockerfile
  
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-12.1/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u04-9.0.4.1/Dockerfile
  
  
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [358]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [359]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [360]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  [361]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  