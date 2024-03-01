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
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][31]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][43]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][56]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][68]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][119]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][126]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][148]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][151]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][176]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][180]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][231]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][234]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][239]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][312]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][350]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[21-jre-headless-latest][24],
  [21.0.1-21.30-jre-headless][27],
  [21.0.2-21.32-jre-headless][28],
  [21.0.0-21.28.85-jre-headless][29],
  
  
  *[20-jre-headless-latest][39],
  [20.0.0-20.28.85-jre-headless][40],
  [20.0.1-20.30.11-jre-headless][41],
  [20.0.2-20.32.11-jre-headless][42],
  
  *[19-jre-headless-latest][52],
  [19.0.0-19.28.81-jre-headless][53],
  [19.0.1-19.30.11-jre-headless][54],
  [19.0.2-19.32.13-jre-headless][55],
  
  *[18-jre-headless-latest][64],
  [18.0.1-18.30.11-jre-headless][65],
  [18.0.2-18.32.11-jre-headless][66],
  [18.0.2.1-18.32.13-jre-headless][67],
  
  *[17-jre-headless-latest][100],
  [17.0.9-17.46-jre-headless][104],
  [17.0.10-17.48-jre-headless][105],
  [17.0.0-17.28.13-jre-headless][107],
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][143],
  [15.0.7-15.40.19-jre-headless][144],
  [15.0.8-15.42.15-jre-headless][145],
  [15.0.9-15.44.13-jre-headless][146],
  
  
  *[13-jre-headless-latest][171],
  [13.0.11-13.48.19-jre-headless][172],
  [13.0.12-13.50.15-jre-headless][173],
  [13.0.13-13.52.15-jre-headless][174],
  
  
  *[11-jre-headless-latest][217],
  [11.0.21-11.68-jre-headless][220],
  [11.0.22-11.70-jre-headless][221],
  [11.0.15-11.56.19-jre-headless][222],
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][300],
  [8u392-8.74-jre-headless][301],
  [8u402-8.76-jre-headless][302],
  [8u332-8.62.0.19-jre-headless][303],
  
  
  
  
  
  
  
  
  
  *[21-jdk-crac-latest][19],
  [21.0.1-21.30-jdk-crac][22],
  [21.0.2-21.32-jdk-crac][23],
  [21.0.0-21.28.89-jdk-crac][25],
  
  
  *[17-jdk-crac-latest][86],
  [17.0.9-17.46-jdk-crac][99],
  [17.0.10-17.48-jdk-crac][101],
  [17.0.8-17.44.17-jdk-crac][102],
  
  
  
  *[21-jre-latest][14],
  [21.0.1-21.30-jre][17],
  [21.0.2-21.32-jre][18],
  [21.0.0-21.28.85-jre][20],
  
  
  *[20-jre-latest][32],
  [20.0.0-20.28.85-jre][36],
  [20.0.1-20.30.11-jre][37],
  [20.0.2-20.32.11-jre][38],
  
  *[19-jre-latest][44],
  [19.0.0-19.28.81-jre][49],
  [19.0.1-19.30.11-jre][50],
  [19.0.2-19.32.13-jre][51],
  
  *[18-jre-latest][57],
  [18.0.1-18.30.11-jre][61],
  [18.0.2-18.32.11-jre][62],
  [18.0.2.1-18.32.13-jre][63],
  
  *[17-jre-latest][70],
  [17.0.9-17.46-jre][82],
  [17.0.10-17.48-jre][83],
  [17.0.0-17.28.13-jre][87],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][120],
  [16.0.0-16.28.11-jre][123],
  [16.0.1-16.30.15-jre][124],
  [16.0.2-16.32.15-jre][125],
  
  *[15-jre-latest][127],
  [15.0.7-15.40.19-jre][139],
  [15.0.8-15.42.15-jre][140],
  [15.0.9-15.44.13-jre][141],
  
  
  *[13-jre-latest][154],
  [13.0.11-13.48.19-jre][167],
  [13.0.12-13.50.15-jre][168],
  [13.0.13-13.52.15-jre][169],
  
  
  *[11-jre-latest][187],
  [11.0.21-11.68-jre][205],
  [11.0.22-11.70-jre][206],
  [11.0.15-11.56.19-jre][210],
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][242],
  [8u392-8.74-jre][267],
  [8u402-8.76-jre][268],
  [8u332-8.62.0.19-jre][291],
  
  
  
  
  
  
  
  
  
  *[21-latest][11],
  [21.0.1-21.30][12],
  [21.0.2-21.32][13],
  [21.0.0-21.28.85][15],
  
  
  *[20-latest][31],
  [20.0.0-20.28.85][33],
  [20.0.1-20.30.11][34],
  [20.0.2-20.32.11][35],
  
  *[19-latest][43],
  [19.0.0-19.28.81][45],
  [19.0.1-19.30.11][46],
  [19.0.2-19.32.13][47],
  
  
  *[18-latest][56],
  [18.0.1-18.30.11][58],
  [18.0.2-18.32.11][59],
  [18.0.2.1-18.32.13][60],
  
  *[17-latest][68],
  [17.0.9-17.46][69],
  [17.0.10-17.48][71],
  [17.0.0-17.28.13][72],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][119],
  [16.0.0-16.28.11][121],
  [16.0.2-16.32.15][122],
  
  *[15-latest][126],
  [15.0.1-15.28.13][128],
  [15.0.1-15.28.51][129],
  [15.0.2-15.29.15][130],
  
  
  
  
  
  
  
  
  
  *[14-latest][148],
  [14.0.1-14.28.21][149],
  [14.0.2-14.29.23][150],
  
  *[13-latest][151],
  [13.0.1-13.28][152],
  [13.0.2-13.29][153],
  [13.0.3-13.31.11][155],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-12.1][176],
  [12-latest][177],
  [12.0.1-12.2][178],
  [12.0.2-12.3][179],
  
  *[11-latest][180],
  [11.0.1-11.2][181],
  [11.0.2-11.29][182],
  [11.0.3-11.31][183],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][231],
  [10u01-10.2][232],
  [10u02-10.3][233],
  
  *[9-ea][234],
  [9-latest][235],
  [9u01-9.0.1.3][236],
  [9u04-9.0.4.1][237],
  
  
  *[8-latest][239],
  [8u392-8.74][240],
  [8u402-8.76][241],
  [8u05-8.1.0.6][243],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][312],
  [7u55-7.4.0.5][313],
  [7u60-7.5.0.1][314],
  [7u65-7.6.0.1][315],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][350],
  [6u49-6.4.0.6][351],
  [6u53-6.5.0.2][352],
  [6u56-6.6.0.1][353],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jre-headless/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre-headless/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.22-11.70-jre-headless/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre-headless/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76-jre-headless/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jdk-crac/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jdk-crac/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.89-jdk-crac/Dockerfile
  
  
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jdk-crac/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jdk-crac/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.17-jdk-crac/Dockerfile
  
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32-jre/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11-jre/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13-jre/Dockerfile
  
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46-jre/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15-jre/Dockerfile
  
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.9-15.44.13-jre/Dockerfile
  
  
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.13-13.52.15-jre/Dockerfile
  
  
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.21-11.68-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.22-11.70-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74-jre/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76-jre/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.2-21.32/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13/Dockerfile
  
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.9-17.46/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.10-17.48/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-12.1/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u04-9.0.4.1/Dockerfile
  
  
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u392-8.74/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u402-8.76/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [350]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [351]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [352]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  [353]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  