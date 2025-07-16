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


  * [`24.0.2-24.32`, `24-latest` (*24-latest/Dockerfile)*][36]
  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][56]
  * [`21.0.8-21.44`, `21-latest` (*21-latest/Dockerfile)*][66]
  * [`17.0.16-17.60`, `17-latest` (*17-latest/Dockerfile)*][128]
  * [`11.0.28-11.82`, `11-latest` (*11-latest/Dockerfile)*][246]
  * [`8u462-8.88`, `8-latest` (*8-latest/Dockerfile)*][321]

Previous
--------

Earlier Debian Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[24-jre-headless-latest][11],
  [24.0.0-24.28-jre-headless][39],
  [24.0.1-24.30-jre-headless][41],
  [24.0.2-24.32-jre-headless][43],
  
  *[23-jre-headless-latest][12],
  [23.0.0-23.28-jre-headless][49],
  [23.0.1-23.30-jre-headless][51],
  [23.0.2-23.32-jre-headless][55],
  
  *[22-jre-headless-latest][13],
  [22.0.0-22.28-jre-headless][57],
  [22.0.1-22.30-jre-headless][61],
  [22.0.2-22.32-jre-headless][65],
  
  *[21-jre-headless-latest][14],
  [21.0.0-21.28.85-jre-headless][67],
  [21.0.1-21.30-jre-headless][71],
  [21.0.1-21.30.15-jre-headless][73],
  
  
  
  
  
  
  
  
  *[20-jre-headless-latest][15],
  [20.0.0-20.28.85-jre-headless][100],
  [20.0.1-20.30.11-jre-headless][102],
  [20.0.2-20.32.11-jre-headless][106],
  
  *[19-jre-headless-latest][16],
  [19.0.0-19.28.81-jre-headless][108],
  [19.0.1-19.30.11-jre-headless][112],
  [19.0.2-19.32.13-jre-headless][116],
  
  *[18-jre-headless-latest][17],
  [18.0.1-18.30.11-jre-headless][119],
  [18.0.2.1-18.32.13-jre-headless][123],
  [18.0.2-18.32.11-jre-headless][125],
  
  *[17-jre-headless-latest][18],
  [17.0.0-17.28.13-jre-headless][129],
  [17.0.1-17.30.15-jre-headless][134],
  [17.0.2-17.32.13-jre-headless][137],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][19],
  [15.0.7-15.40.19-jre-headless][205],
  [15.0.8-15.42.15-jre-headless][209],
  [15.0.9-15.44.13-jre-headless][211],
  
  
  *[13-jre-headless-latest][20],
  [13.0.11-13.48.19-jre-headless][231],
  [13.0.12-13.50.15-jre-headless][235],
  [13.0.13-13.52.15-jre-headless][236],
  
  
  *[11-jre-headless-latest][21],
  [11.0.15-11.56.19-jre-headless][263],
  [11.0.16.1-11.58.23-jre-headless][265],
  [11.0.16-11.58.15-jre-headless][269],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][22],
  [8u332-8.62.0.19-jre-headless][360],
  [8u342-8.64.0.15-jre-headless][364],
  [8u345-8.64.0.19-jre-headless][367],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[24-jre-latest][23],
  [24.0.0-24.28-jre][38],
  [24.0.1-24.30-jre][40],
  [24.0.2-24.32-jre][44],
  
  *[23-jre-latest][24],
  [23.0.0-23.28-jre][47],
  [23.0.1-23.30-jre][52],
  [23.0.2-23.32-jre][54],
  
  *[22-jre-latest][25],
  [22.0.0-22.28-jre][59],
  [22.0.1-22.30-jre][60],
  [22.0.2-22.32-jre][64],
  
  *[21-jre-latest][26],
  [21.0.0-21.28.85-jre][69],
  [21.0.1-21.30-jre][70],
  [21.0.1-21.30.15-jre][75],
  
  
  
  
  
  
  
  
  *[20-jre-latest][27],
  [20.0.0-20.28.85-jre][99],
  [20.0.1-20.30.11-jre][103],
  [20.0.2-20.32.11-jre][105],
  
  *[19-jre-latest][28],
  [19.0.0-19.28.81-jre][110],
  [19.0.1-19.30.11-jre][111],
  [19.0.2-19.32.13-jre][114],
  
  *[18-jre-latest][29],
  [18.0.1-18.30.11-jre][121],
  [18.0.2.1-18.32.13-jre][122],
  [18.0.2-18.32.11-jre][126],
  
  *[17-jre-latest][30],
  [17.0.0-17.28.13-jre][131],
  [17.0.1-17.30.15-jre][132],
  [17.0.2-17.32.13-jre][136],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][31],
  [16.0.0-16.28.11-jre][191],
  [16.0.1-16.30.15-jre][192],
  [16.0.2-16.32.15-jre][195],
  
  *[15-jre-latest][32],
  [15.0.7-15.40.19-jre][204],
  [15.0.8-15.42.15-jre][208],
  [15.0.9-15.44.13-jre][210],
  
  
  *[13-jre-latest][33],
  [13.0.11-13.48.19-jre][232],
  [13.0.12-13.50.15-jre][233],
  [13.0.13-13.52.15-jre][238],
  
  
  *[11-jre-latest][34],
  [11.0.15-11.56.19-jre][262],
  [11.0.16.1-11.58.23-jre][267],
  [11.0.16-11.58.15-jre][270],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][35],
  [8u332-8.62.0.19-jre][361],
  [8u342-8.64.0.15-jre][365],
  [8u345-8.64.0.19-jre][368],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[24-latest][36],
  [24.0.0-24.28][37],
  [24.0.1-24.30][42],
  [24.0.2-24.32][45],
  
  *[23-latest][46],
  [23.0.0-23.28][48],
  [23.0.1-23.30][50],
  [23.0.2-23.32][53],
  
  *[22-latest][56],
  [22.0.0-22.28][58],
  [22.0.1-22.30][62],
  [22.0.2-22.32][63],
  
  *[21-latest][66],
  [21.0.0-21.28.85][68],
  [21.0.1-21.30][72],
  [21.0.1-21.30.15][74],
  
  
  
  
  
  
  
  
  *[20-latest][97],
  [20.0.0-20.28.85][98],
  [20.0.1-20.30.11][101],
  [20.0.2-20.32.11][104],
  
  *[19-latest][107],
  [19.0.0-19.28.81][109],
  [19.0.1-19.30.11][113],
  [19.0.2-19.32.13][115],
  
  
  *[18-latest][118],
  [18.0.1-18.30.11][120],
  [18.0.2.1-18.32.13][124],
  [18.0.2-18.32.11][127],
  
  *[17-latest][128],
  [17.0.0-17.28.13][130],
  [17.0.1-17.30.15][133],
  [17.0.2-17.32.13][135],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][189],
  [16.0.0-16.28.11][190],
  [16.0.1-16.30.15][193],
  [16.0.2-16.32.15][194],
  
  *[15-latest][196],
  [15.0.1-15.28.13][197],
  [15.0.1-15.28.51][198],
  [15.0.2-15.29.15][199],
  
  
  
  
  
  
  
  
  
  *[14-latest][216],
  [14.0.1-14.28.21][217],
  [14.0.2-14.29.23][218],
  
  *[13-latest][219],
  [13.0.1-13.28][220],
  [13.0.2-13.29][221],
  [13.0.3-13.31.11][222],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][242],
  [12.0.1-12.2][243],
  [12.0.2-12.3][244],
  [12-12.1][245],
  
  *[11-latest][246],
  [11.0.1-11.2][247],
  [11.0.2-11.29][248],
  [11.0.3-11.31][249],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][313],
  [10u01-10.2][314],
  [10u02-10.3][315],
  
  *[9-latest][316],
  [9-ea][317],
  [9u01-9.0.1.3][318],
  [9u04-9.0.4.1][319],
  
  
  *[8-latest][321],
  [8u05-8.1.0.6][322],
  [8u11-8.2.0.1][323],
  [8u20-8.3.0.1][324],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][411],
  [7u55-7.4.0.5][412],
  [7u60-7.5.0.1][413],
  [7u65-7.6.0.1][414],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][449],
  [6u49-6.4.0.6][450],
  [6u53-6.5.0.2][451],
  [6u56-6.6.0.1][452],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30-jre-headless/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-headless-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre-headless/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre-headless/Dockerfile
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-headless-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre-headless/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre-headless/Dockerfile
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-headless-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre-headless/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre-headless/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre-headless/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [360]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  [364]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre-headless/Dockerfile
  [367]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-jre-latest/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28-jre/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30-jre/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre/Dockerfile
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre/Dockerfile
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [361]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  [365]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre/Dockerfile
  [368]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-latest/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32/Dockerfile
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32/Dockerfile
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32/Dockerfile
  
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15/Dockerfile
  
  
  
  
  
  
  
  
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11/Dockerfile
  
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  
  
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  
  
  [321]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [411]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [412]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [413]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [414]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [449]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [450]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [451]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [452]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  