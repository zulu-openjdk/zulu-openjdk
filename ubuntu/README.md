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

Important Notice
=====

This container image repository will be retired by the end of 2026. Please start migrating to the [Docker Official repository with Azul containers][9]. Check the [Running Azul Zulu Community Availability (CA) in a Docker Container][10] in the Azul Documentation for more information.

If you run into any issues or have feature/configuration requests, please open an issue at [AzulSystems/azul-zulu-images issues][11].

Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`26.0.2.1-26.32`, `26-latest` (*26-latest/Dockerfile)*][54]
  * [`25.0.4.1-25.36`, `25-latest` (*25-latest/Dockerfile)*][65]
  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][118]
  * [`21.0.12.1-21.52`, `21-latest` (*21-latest/Dockerfile)*][132]
  * [`17.0.20.1-17.68`, `17-latest` (*17-latest/Dockerfile)*][224]
  * [`11.0.32.1-11.90`, `11-latest` (*11-latest/Dockerfile)*][372]
  * [`8u504-8.96`, `8-latest` (*8-latest/Dockerfile)*][456]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 3 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[26-jre-headless-latest][11],
  [26.0.0-26.28-jre-headless][57],
  [26.0.2.1-26.32-jre-headless][61],
  
  *[25-jre-headless-latest][12],
  [25.0.0-25.28-jre-headless][68],
  [25.0.1-25.30-jre-headless][72],
  
  
  
  *[24-jre-headless-latest][13],
  [24.0.0-24.28-jre-headless][90],
  [24.0.1-24.30-jre-headless][95],
  
  
  *[23-jre-headless-latest][14],
  [23.0.0-23.28-jre-headless][107],
  [23.0.1-23.30-jre-headless][109],
  
  
  *[22-jre-headless-latest][15],
  [22.0.0-22.28-jre-headless][119],
  [22.0.1-22.30-jre-headless][125],
  
  
  *[21-jre-headless-latest][16],
  [21.0.0-21.28.85-jre-headless][133],
  [21.0.1-21.30-jre-headless][139],
  
  
  
  
  
  
  
  
  
  
  
  
  *[20-jre-headless-latest][17],
  [20.0.0-20.28.85-jre-headless][196],
  [20.0.1-20.30.11-jre-headless][198],
  
  
  *[19-jre-headless-latest][18],
  [19.0.0-19.28.81-jre-headless][204],
  [19.0.1-19.30.11-jre-headless][208],
  
  
  *[18-jre-headless-latest][19],
  [18.0.1-18.30.11-jre-headless][215],
  [18.0.2.1-18.32.13-jre-headless][219],
  
  
  *[17-jre-headless-latest][20],
  [17.0.0-17.28.13-jre-headless][225],
  [17.0.1-17.30.15-jre-headless][230],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][21],
  [15.0.7-15.40.19-jre-headless][331],
  [15.0.8-15.42.15-jre-headless][335],
  
  
  
  *[13-jre-headless-latest][22],
  [13.0.11-13.48.19-jre-headless][357],
  [13.0.12-13.50.15-jre-headless][361],
  
  
  
  *[11-jre-headless-latest][23],
  [11.0.15-11.56.19-jre-headless][389],
  [11.0.16.1-11.58.23-jre-headless][391],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][24],
  [8u332-8.62.0.19-jre-headless][494],
  [8u342-8.64.0.15-jre-headless][498],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[26-jre-crac-latest][25],
  [26.0.0-26.28-jre-crac][55],
  [26.0.2.1-26.32-jre-crac][63],
  
  *[26-jdk-crac-latest][26],
  [26.0.0-26.28-jdk-crac][56],
  [26.0.2.1-26.32-jdk-crac][62],
  
  *[25-jre-crac-latest][27],
  [25.0.0-25.28-jre-crac][69],
  [25.0.1-25.30-jre-crac][74],
  
  
  
  *[25-jdk-crac-latest][28],
  [25.0.0-25.28-jdk-crac][70],
  [25.0.1-25.30-jdk-crac][75],
  
  
  
  *[24-jre-crac-latest][29],
  [24.0.0-24.28-jre-crac][88],
  [24.0.1-24.30-jre-crac][93],
  
  
  *[24-jdk-crac-latest][30],
  [24.0.0-24.28-jdk-crac][91],
  [24.0.1-24.30-jdk-crac][94],
  
  
  *[23-jre-crac-latest][31],
  [23.0.0-23.28-jre-crac][104],
  [23.0.1-23.30-jre-crac][110],
  
  
  *[23-jdk-crac-latest][32],
  [23.0.0-23.28-jdk-crac][106],
  [23.0.1-23.30-jdk-crac][112],
  
  
  *[22-jre-crac-latest][33],
  [22.0.2-22.32-jre-crac][127],
  
  *[22-jdk-crac-latest][34],
  [22.0.0-22.28-jdk-crac][121],
  [22.0.1-22.30-jdk-crac][124],
  
  
  *[21-jre-crac-latest][35],
  [21.0.4-21.36-jre-crac][157],
  [21.0.5-21.38-jre-crac][159],
  
  
  
  
  
  
  
  *[21-jdk-crac-latest][36],
  [21.0.0-21.28.89-jdk-crac][136],
  [21.0.1-21.30-jdk-crac][138],
  
  
  
  
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][37],
  [17.0.12-17.52-jre-crac][278],
  [17.0.13-17.54-jre-crac][282],
  
  
  
  
  
  
  
  *[17-jdk-crac-latest][38],
  [17.0.8.1-17.44.55-jdk-crac][255],
  [17.0.8-17.44.17-jdk-crac][259],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[26-jre-latest][39],
  [26.0.0-26.28-jre][59],
  [26.0.2.1-26.32-jre][60],
  
  *[25-jre-latest][40],
  [25.0.0-25.28-jre][66],
  [25.0.1-25.30-jre][73],
  
  
  
  *[24-jre-latest][41],
  [24.0.0-24.28-jre][89],
  [24.0.1-24.30-jre][92],
  
  
  *[23-jre-latest][42],
  [23.0.0-23.28-jre][103],
  [23.0.1-23.30-jre][111],
  
  
  *[22-jre-latest][43],
  [22.0.0-22.28-jre][122],
  [22.0.1-22.30-jre][123],
  
  
  *[21-jre-latest][44],
  [21.0.0-21.28.85-jre][135],
  [21.0.1-21.30-jre][137],
  
  
  
  
  
  
  
  
  
  
  
  
  *[20-jre-latest][45],
  [20.0.0-20.28.85-jre][195],
  [20.0.1-20.30.11-jre][199],
  
  
  *[19-jre-latest][46],
  [19.0.0-19.28.81-jre][206],
  [19.0.1-19.30.11-jre][207],
  
  
  *[18-jre-latest][47],
  [18.0.1-18.30.11-jre][217],
  [18.0.2.1-18.32.13-jre][218],
  
  
  *[17-jre-latest][48],
  [17.0.0-17.28.13-jre][227],
  [17.0.1-17.30.15-jre][228],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][49],
  [16.0.0-16.28.11-jre][318],
  [16.0.1-16.30.15-jre][319],
  
  
  *[15-jre-latest][50],
  [15.0.7-15.40.19-jre][330],
  [15.0.8-15.42.15-jre][334],
  
  
  
  *[13-jre-latest][51],
  [13.0.11-13.48.19-jre][358],
  [13.0.12-13.50.15-jre][359],
  
  
  
  *[11-jre-latest][52],
  [11.0.15-11.56.19-jre][388],
  [11.0.16.1-11.58.23-jre][393],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][53],
  [8u332-8.62.0.19-jre][495],
  [8u342-8.64.0.15-jre][499],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[26-latest][54],
  [26.0.0-26.28][58],
  [26.0.2.1-26.32][64],
  
  *[25-latest][65],
  [25.0.0-25.28][67],
  [25.0.1-25.30][71],
  
  
  
  *[24-latest][86],
  [24.0.0-24.28][87],
  [24.0.1-24.30][96],
  
  
  *[23-latest][102],
  [23.0.0-23.28][105],
  [23.0.1-23.30][108],
  
  
  *[22-latest][118],
  [22.0.0-22.28][120],
  [22.0.1-22.30][126],
  
  
  *[21-latest][132],
  [21.0.0-21.28.85][134],
  [21.0.1-21.30][140],
  
  
  
  
  
  
  
  
  
  
  
  
  *[20-latest][193],
  [20.0.0-20.28.85][194],
  [20.0.1-20.30.11][197],
  
  
  *[19-latest][203],
  [19.0.0-19.28.81][205],
  [19.0.1-19.30.11][209],
  
  
  
  *[18-latest][214],
  [18.0.1-18.30.11][216],
  [18.0.2.1-18.32.13][220],
  
  
  *[17-latest][224],
  [17.0.0-17.28.13][226],
  [17.0.1-17.30.15][229],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][316],
  [16.0.0-16.28.11][317],
  [16.0.2-16.32.15][320],
  
  *[15-latest][322],
  [15.0.1-15.28.13][323],
  [15.0.1-15.28.51][324],
  
  
  
  
  
  
  
  
  
  
  *[14-latest][342],
  [14.0.1-14.28.21][343],
  [14.0.2-14.29.23][344],
  
  *[13-latest][345],
  [13.0.1-13.28][346],
  [13.0.2-13.29][347],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][368],
  [12.0.1-12.2][369],
  [12.0.2-12.3][370],
  
  
  *[11-latest][372],
  [11.0.1-11.2][373],
  [11.0.2-11.29][374],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][448],
  [10u01-10.2][449],
  [10u02-10.3][450],
  
  *[9-latest][451],
  [9-ea][452],
  [9u01-9.0.1.3][453],
  
  
  
  *[8-latest][456],
  [8u05-8.1.0.6][457],
  [8u11-8.2.0.1][458],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][554],
  [7u55-7.4.0.5][555],
  [7u60-7.5.0.1][556],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][592],
  [6u49-6.4.0.6][593],
  [6u53-6.5.0.2][594],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  License
=======

Azul Zulu incorporates third-party licensed software packages. Some of these have distribution restrictions, and some have only reporting requirements. Please see [docs.azul.com/core/tpl][12] for the links to the documents with licenses for third-party software included in the latest version of Azul Platform Core.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc., from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

[BSD 3-Clause Clear License][13]

  [1]: https://www.azul.com/
  [2]: https://www.azul.com/products/core/
  [3]: https://docs.azul.com/core/
  [4]: https://hub.docker.com/r/azul/zulu-openjdk
  [5]: https://hub.docker.com/r/azul/zulu-openjdk-alpine
  [6]: https://hub.docker.com/r/azul/zulu-openjdk-centos
  [7]: https://hub.docker.com/r/azul/zulu-openjdk-debian
  [8]: https://hub.docker.com/r/azul/zulu-openjdk-distroless
  [9]: https://hub.docker.com/_/azul-zulu
  [10]: https://docs.azul.com/core/install/linux-ca-docker
  [11]: https://github.com/AzulSystems/azul-zulu-images/issues
  [12]: https://docs.azul.com/core/tpl
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/LICENSE.txt


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26-jre-headless-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.0-26.28-jre-headless/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.2.1-26.32-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25-jre-headless-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.0-25.28-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.1-25.30-jre-headless/Dockerfile
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24-jre-headless-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.0-24.28-jre-headless/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.1-24.30-jre-headless/Dockerfile
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-headless-latest/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30-jre-headless/Dockerfile
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre-headless/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre-headless/Dockerfile
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [331]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [335]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [357]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [361]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [389]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  [391]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [494]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  [498]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26-jre-crac-latest/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.0-26.28-jre-crac/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.2.1-26.32-jre-crac/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26-jdk-crac-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.0-26.28-jdk-crac/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.2.1-26.32-jdk-crac/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25-jre-crac-latest/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.0-25.28-jre-crac/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.1-25.30-jre-crac/Dockerfile
  
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25-jdk-crac-latest/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.0-25.28-jdk-crac/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.1-25.30-jdk-crac/Dockerfile
  
  
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24-jre-crac-latest/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.0-24.28-jre-crac/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.1-24.30-jre-crac/Dockerfile
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24-jdk-crac-latest/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.0-24.28-jdk-crac/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.1-24.30-jdk-crac/Dockerfile
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-crac-latest/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre-crac/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30-jre-crac/Dockerfile
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jdk-crac-latest/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jdk-crac/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30-jdk-crac/Dockerfile
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.2-22.32-jre-crac/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jdk-crac/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jdk-crac/Dockerfile
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.4-21.36-jre-crac/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.5-21.38-jre-crac/Dockerfile
  
  
  
  
  
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.89-jdk-crac/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jdk-crac/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.12-17.52-jre-crac/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.13-17.54-jre-crac/Dockerfile
  
  
  
  
  
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8.1-17.44.55-jdk-crac/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.8-17.44.17-jdk-crac/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26-jre-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.0-26.28-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.2.1-26.32-jre/Dockerfile
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25-jre-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.0-25.28-jre/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.1-25.30-jre/Dockerfile
  
  
  
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24-jre-latest/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.0-24.28-jre/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.1-24.30-jre/Dockerfile
  
  
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-jre-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28-jre/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30-jre/Dockerfile
  
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre/Dockerfile
  
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [318]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [319]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [330]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [334]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  
  
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [358]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [359]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  
  
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [388]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  [393]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [495]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  [499]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.0-26.28/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/26.0.2.1-26.32/Dockerfile
  
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25-latest/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.0-25.28/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/25.0.1-25.30/Dockerfile
  
  
  
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24-latest/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.0-24.28/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/24.0.1-24.30/Dockerfile
  
  
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23-latest/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.0-23.28/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/23.0.1-23.30/Dockerfile
  
  
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-latest/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30/Dockerfile
  
  
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  
  
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  
  
  
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  
  
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [316]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [317]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [320]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [322]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [323]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [342]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [343]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [344]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [345]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [346]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [347]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [368]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [369]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [370]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  
  
  [372]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [373]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [374]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [448]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [449]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [450]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [451]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [452]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [453]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  
  
  
  [456]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [457]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  [458]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u11-8.2.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [554]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [555]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [556]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [592]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [593]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [594]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  