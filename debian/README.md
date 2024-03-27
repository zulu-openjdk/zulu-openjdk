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


  * [`22.0.0-22.28`, `22-latest` (*22-latest/Dockerfile)*][11]
  * [`21.0.1-21.30.15`, `21-latest` (*21-latest/Dockerfile)*][17]
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][32]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][44]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][57]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][69]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][114]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][122]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][144]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][147]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][172]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][176]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][227]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][230]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][235]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][309]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][347]

Previous
--------

Earlier Debian Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[22-jre-headless-latest][15],
  [22.0.0-22.28-jre-headless][16],
  
  *[21-jre-headless-latest][27],
  [21.0.1-21.30-jre-headless][28],
  [21.0.2-21.32-jre-headless][29],
  [21.0.0-21.28.85-jre-headless][30],
  
  
  *[20-jre-headless-latest][40],
  [20.0.0-20.28.85-jre-headless][41],
  [20.0.1-20.30.11-jre-headless][42],
  [20.0.2-20.32.11-jre-headless][43],
  
  *[19-jre-headless-latest][53],
  [19.0.0-19.28.81-jre-headless][54],
  [19.0.1-19.30.11-jre-headless][55],
  [19.0.2-19.32.13-jre-headless][56],
  
  *[18-jre-headless-latest][65],
  [18.0.1-18.30.11-jre-headless][66],
  [18.0.2-18.32.11-jre-headless][67],
  [18.0.2.1-18.32.13-jre-headless][68],
  
  *[17-jre-headless-latest][99],
  [17.0.9-17.46-jre-headless][100],
  [17.0.10-17.48-jre-headless][101],
  [17.0.0-17.28.13-jre-headless][102],
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][139],
  [15.0.7-15.40.19-jre-headless][140],
  [15.0.8-15.42.15-jre-headless][141],
  [15.0.9-15.44.13-jre-headless][142],
  
  
  *[13-jre-headless-latest][167],
  [13.0.11-13.48.19-jre-headless][168],
  [13.0.12-13.50.15-jre-headless][169],
  [13.0.13-13.52.15-jre-headless][170],
  
  
  *[11-jre-headless-latest][213],
  [11.0.21-11.68-jre-headless][216],
  [11.0.22-11.70-jre-headless][217],
  [11.0.15-11.56.19-jre-headless][218],
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][297],
  [8u392-8.74-jre-headless][298],
  [8u402-8.76-jre-headless][299],
  [8u332-8.62.0.19-jre-headless][300],
  
  
  
  
  
  
  
  
  
  *[22-jre-latest][13],
  [22.0.0-22.28-jre][14],
  
  *[21-jre-latest][20],
  [21.0.1-21.30-jre][23],
  [21.0.2-21.32-jre][24],
  [21.0.0-21.28.85-jre][25],
  
  
  *[20-jre-latest][33],
  [20.0.0-20.28.85-jre][37],
  [20.0.1-20.30.11-jre][38],
  [20.0.2-20.32.11-jre][39],
  
  *[19-jre-latest][45],
  [19.0.0-19.28.81-jre][50],
  [19.0.1-19.30.11-jre][51],
  [19.0.2-19.32.13-jre][52],
  
  *[18-jre-latest][58],
  [18.0.1-18.30.11-jre][62],
  [18.0.2-18.32.11-jre][63],
  [18.0.2.1-18.32.13-jre][64],
  
  *[17-jre-latest][71],
  [17.0.9-17.46-jre][83],
  [17.0.10-17.48-jre][84],
  [17.0.0-17.28.13-jre][87],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][115],
  [16.0.0-16.28.11-jre][119],
  [16.0.1-16.30.15-jre][120],
  [16.0.2-16.32.15-jre][121],
  
  *[15-jre-latest][123],
  [15.0.7-15.40.19-jre][135],
  [15.0.8-15.42.15-jre][136],
  [15.0.9-15.44.13-jre][137],
  
  
  *[13-jre-latest][150],
  [13.0.11-13.48.19-jre][163],
  [13.0.12-13.50.15-jre][164],
  [13.0.13-13.52.15-jre][165],
  
  
  *[11-jre-latest][183],
  [11.0.21-11.68-jre][201],
  [11.0.22-11.70-jre][202],
  [11.0.15-11.56.19-jre][206],
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][238],
  [8u392-8.74-jre][263],
  [8u402-8.76-jre][264],
  [8u332-8.62.0.19-jre][288],
  
  
  
  
  
  
  
  
  
  *[22-latest][11],
  [22.0.0-22.28][12],
  
  *[21-latest][17],
  [21.0.1-21.30][18],
  [21.0.2-21.32][19],
  [21.0.0-21.28.85][21],
  
  
  *[20-latest][32],
  [20.0.0-20.28.85][34],
  [20.0.1-20.30.11][35],
  [20.0.2-20.32.11][36],
  
  *[19-latest][44],
  [19.0.0-19.28.81][46],
  [19.0.1-19.30.11][47],
  [19.0.2-19.32.13][48],
  
  
  *[18-latest][57],
  [18.0.1-18.30.11][59],
  [18.0.2-18.32.11][60],
  [18.0.2.1-18.32.13][61],
  
  *[17-latest][69],
  [17.0.9-17.46][70],
  [17.0.10-17.48][72],
  [17.0.0-17.28.13][73],
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][114],
  [16.0.0-16.28.11][116],
  [16.0.1-16.30.15][117],
  [16.0.2-16.32.15][118],
  
  *[15-latest][122],
  [15.0.1-15.28.13][124],
  [15.0.1-15.28.51][125],
  [15.0.2-15.29.15][126],
  
  
  
  
  
  
  
  
  
  *[14-latest][144],
  [14.0.1-14.28.21][145],
  [14.0.2-14.29.23][146],
  
  *[13-latest][147],
  [13.0.1-13.28][148],
  [13.0.2-13.29][149],
  [13.0.3-13.31.11][151],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-12.1][172],
  [12-latest][173],
  [12.0.1-12.2][174],
  [12.0.2-12.3][175],
  
  *[11-latest][176],
  [11.0.1-11.2][177],
  [11.0.2-11.29][178],
  [11.0.3-11.31][179],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][227],
  [10u01-10.2][228],
  [10u02-10.3][229],
  
  *[9-ea][230],
  [9-latest][231],
  [9u01-9.0.1.3][232],
  [9u04-9.0.4.1][233],
  
  
  *[8-latest][235],
  [8u392-8.74][236],
  [8u402-8.76][237],
  [8u05-8.1.0.6][239],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][309],
  [7u55-7.4.0.5][310],
  [7u60-7.5.0.1][311],
  [7u65-7.6.0.1][312],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][347],
  [6u49-6.4.0.6][348],
  [6u53-6.5.0.2][349],
  [6u56-6.6.0.1][350],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-headless-latest/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre-headless/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-headless-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre-headless/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.2-21.32-jre-headless/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre-headless/Dockerfile
  
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.9-17.46-jre-headless/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.10-17.48-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.21-11.68-jre-headless/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.22-11.70-jre-headless/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u392-8.74-jre-headless/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u402-8.76-jre-headless/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.2-21.32-jre/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre/Dockerfile
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre/Dockerfile
  
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.9-17.46-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.10-17.48-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  
  
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  
  
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.21-11.68-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.22-11.70-jre/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u392-8.74-jre/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u402-8.76-jre/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28/Dockerfile
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.2-21.32/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85/Dockerfile
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  
  
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.9-17.46/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.10-17.48/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  
  
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u392-8.74/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u402-8.76/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [347]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [348]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [349]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [350]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  