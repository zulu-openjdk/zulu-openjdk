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


  * [`23.0.0-23.28`, `23-latest` (*23-latest/Dockerfile)*][42]
  * [`21.0.4-21.36`, `21-latest` (*21-latest/Dockerfile)*][70]
  * [`17.0.12-17.52`, `17-latest` (*17-latest/Dockerfile)*][137]
  * [`11.0.24-11.74`, `11-latest` (*11-latest/Dockerfile)*][259]
  * [`8u422-8.80`, `8-latest` (*8-latest/Dockerfile)*][324]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[23-jre-headless-latest][11],
  [23-jre-headless-latest][44],
  [23.0.0-23.28-jre-headless][51],
  
  *[22-jre-headless-latest][12],
  [22-jre-headless-latest][55],
  [22.0.0-22.28-jre-headless][57],
  [22.0.1-22.30-jre-headless][63],
  
  
  *[21-jre-headless-latest][13],
  [21-jre-headless-latest][74],
  [21.0.0-21.28.85-jre-headless][75],
  [21.0.1-21.30-jre-headless][81],
  
  
  
  
  
  *[20-jre-headless-latest][14],
  [20-jre-headless-latest][102],
  [20.0.0-20.28.85-jre-headless][105],
  [20.0.1-20.30.11-jre-headless][107],
  
  
  *[19-jre-headless-latest][15],
  [19-jre-headless-latest][113],
  [19.0.0-19.28.81-jre-headless][115],
  [19.0.1-19.30.11-jre-headless][119],
  
  
  *[18-jre-headless-latest][16],
  [18-jre-headless-latest][127],
  [18.0.1-18.30.11-jre-headless][128],
  [18.0.2.1-18.32.13-jre-headless][132],
  
  
  *[17-jre-headless-latest][17],
  [17-jre-headless-latest][141],
  [17.0.0-17.28.13-jre-headless][142],
  [17.0.1-17.30.15-jre-headless][147],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][18],
  [15-jre-headless-latest][207],
  [15.0.7-15.40.19-jre-headless][216],
  [15.0.8-15.42.15-jre-headless][220],
  
  
  
  *[13-jre-headless-latest][19],
  [13-jre-headless-latest][232],
  [13.0.11-13.48.19-jre-headless][244],
  [13.0.12-13.50.15-jre-headless][248],
  
  
  
  *[11-jre-headless-latest][20],
  [11-jre-headless-latest][261],
  [11.0.15-11.56.19-jre-headless][278],
  [11.0.16.1-11.58.23-jre-headless][280],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][21],
  [8-jre-headless-latest][326],
  [8u332-8.62.0.19-jre-headless][364],
  [8u342-8.64.0.15-jre-headless][368],
  
  
  
  
  
  
  
  
  
  
  
  
  *[23-jre-crac-latest][22],
  [23-jdk-crac-latest][23],
  [23-jre-crac-latest][43],
  [23-jdk-crac-latest][45],
  
  
  
  *[23-jre-crac-latest][22],
  [23-jdk-crac-latest][23],
  [23-jre-crac-latest][43],
  [23-jdk-crac-latest][45],
  
  
  
  *[22-jre-crac-latest][24],
  [22-jdk-crac-latest][25],
  [22-jre-crac-latest][53],
  [22-jdk-crac-latest][56],
  
  
  
  
  
  *[22-jre-crac-latest][24],
  [22-jdk-crac-latest][25],
  [22-jre-crac-latest][53],
  [22-jdk-crac-latest][56],
  
  
  
  
  
  *[21-jre-crac-latest][26],
  [21-jdk-crac-latest][27],
  [21-jre-crac-latest][71],
  [21-jdk-crac-latest][73],
  
  
  
  
  
  
  
  
  *[21-jre-crac-latest][26],
  [21-jdk-crac-latest][27],
  [21-jre-crac-latest][71],
  [21-jdk-crac-latest][73],
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][28],
  [17-jdk-crac-latest][29],
  [17-jre-crac-latest][138],
  [17-jdk-crac-latest][140],
  
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][28],
  [17-jdk-crac-latest][29],
  [17-jre-crac-latest][138],
  [17-jdk-crac-latest][140],
  
  
  
  
  
  
  
  
  
  *[23-jre-latest][30],
  [23-jre-latest][46],
  [23.0.0-23.28-jre][47],
  
  *[22-jre-latest][31],
  [22-jre-latest][54],
  [22.0.0-22.28-jre][60],
  [22.0.1-22.30-jre][61],
  
  
  *[21-jre-latest][32],
  [21-jre-latest][72],
  [21.0.0-21.28.85-jre][77],
  [21.0.1-21.30-jre][79],
  
  
  
  
  
  *[20-jre-latest][33],
  [20-jre-latest][101],
  [20.0.0-20.28.85-jre][104],
  [20.0.1-20.30.11-jre][108],
  
  
  *[19-jre-latest][34],
  [19-jre-latest][114],
  [19.0.0-19.28.81-jre][117],
  [19.0.1-19.30.11-jre][118],
  
  
  *[18-jre-latest][35],
  [18-jre-latest][126],
  [18.0.1-18.30.11-jre][130],
  [18.0.2.1-18.32.13-jre][131],
  
  
  *[17-jre-latest][36],
  [17-jre-latest][139],
  [17.0.0-17.28.13-jre][144],
  [17.0.1-17.30.15-jre][145],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][37],
  [16-jre-latest][199],
  [16.0.0-16.28.11-jre][201],
  [16.0.1-16.30.15-jre][202],
  
  
  *[15-jre-latest][38],
  [15-jre-latest][206],
  [15.0.7-15.40.19-jre][215],
  [15.0.8-15.42.15-jre][219],
  
  
  
  *[13-jre-latest][39],
  [13-jre-latest][231],
  [13.0.11-13.48.19-jre][245],
  [13.0.12-13.50.15-jre][246],
  
  
  
  *[11-jre-latest][40],
  [11-jre-latest][260],
  [11.0.15-11.56.19-jre][277],
  [11.0.16.1-11.58.23-jre][282],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][41],
  [8-jre-latest][325],
  [8u332-8.62.0.19-jre][365],
  [8u342-8.64.0.15-jre][369],
  
  
  
  
  
  
  
  
  
  
  
  
  *[23-latest][42],
  [23.0.0-23.28][49],
  
  *[22-latest][52],
  [22.0.0-22.28][58],
  [22.0.1-22.30][64],
  [22.0.2-22.32][66],
  
  *[21-latest][70],
  [21.0.0-21.28.85][76],
  [21.0.1-21.30][82],
  [21.0.1-21.30.15][84],
  
  
  
  
  *[20-latest][100],
  [20.0.0-20.28.85][103],
  [20.0.1-20.30.11][106],
  [20.0.2-20.32.11][109],
  
  *[19-latest][112],
  [19.0.0-19.28.81][116],
  [19.0.1-19.30.11][120],
  [19.0.2-19.32.13][122],
  
  
  *[18-latest][125],
  [18.0.1-18.30.11][129],
  [18.0.2.1-18.32.13][133],
  [18.0.2-18.32.11][136],
  
  *[17-latest][137],
  [17.0.0-17.28.13][143],
  [17.0.1-17.30.15][146],
  [17.0.2-17.32.13][148],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][198],
  [16.0.0-16.28.11][200],
  [16.0.2-16.32.15][203],
  
  *[15-latest][205],
  [15.0.1-15.28.13][208],
  [15.0.1-15.28.51][209],
  [15.0.2-15.29.15][210],
  
  
  
  
  
  
  
  
  
  *[14-latest][227],
  [14.0.1-14.28.21][228],
  [14.0.2-14.29.23][229],
  
  *[13-latest][230],
  [13.0.1-13.28][233],
  [13.0.2-13.29][234],
  [13.0.3-13.31.11][235],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][255],
  [12.0.1-12.2][256],
  [12.0.2-12.3][257],
  [12-12.1][258],
  
  *[11-latest][259],
  [11.0.1-11.2][262],
  [11.0.2-11.29][263],
  [11.0.3-11.31][264],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][316],
  [10u01-10.2][317],
  [10u02-10.3][318],
  
  *[9-latest][319],
  [9-ea][320],
  [9u01-9.0.1.3][321],
  [9u04-9.0.4.1][322],
  
  
  *[8-latest][324],
  [8u05-8.1.0.6][327],
  [8u11-8.2.0.1][328],
  [8u20-8.3.0.1][329],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][403],
  [7u55-7.4.0.5][404],
  [7u60-7.5.0.1][405],
  [7u65-7.6.0.1][406],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][441],
  [6u49-6.4.0.6][442],
  [6u53-6.5.0.2][443],
  [6u56-6.6.0.1][444],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre-headless/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre-headless/Dockerfile
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  
  
  
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [364]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  [368]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  
  
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  
  
  
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre/Dockerfile
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre/Dockerfile
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  
  
  
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  
  
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [365]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  [369]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.2-22.32/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.15/Dockerfile
  
  
  
  
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11/Dockerfile
  
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13/Dockerfile
  
  
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11/Dockerfile
  
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-12.1/Dockerfile
  
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u04-9.0.4.1/Dockerfile
  
  
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  [328]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u11-8.2.0.1/Dockerfile
  [329]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u20-8.3.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [403]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [404]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [405]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  [406]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [441]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [442]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [443]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  [444]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  