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

Important Notice
=====

This container image repository will be retired by the end of 2026. Please start migrating to the [Docker Official repository with Azul containers][9]. Check the [Running Azul Zulu Community Availability (CA) in a Docker Container][10] in the Azul Documentation for more information.

If you run into any issues or have feature/configuration requests, please open an issue at [AzulSystems/azul-zulu-images issues][11].

Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`26.0.2.1-26.32`, `26-latest` (*26-latest/Dockerfile)*][40]
  * [`25.0.4.1-25.36`, `25-latest` (*25-latest/Dockerfile)*][47]
  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][80]
  * [`21.0.12.1-21.52`, `21-latest` (*21-latest/Dockerfile)*][90]
  * [`17.0.20.1-17.68`, `17-latest` (*17-latest/Dockerfile)*][161]
  * [`11.0.32.1-11.90`, `11-latest` (*11-latest/Dockerfile)*][288]
  * [`8u504-8.96`, `8-latest` (*8-latest/Dockerfile)*][372]

Previous
--------

Earlier Debian Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[26-jre-headless-latest][11],
  [26.0.0-26.28-jre-headless][41],
  [26.0.2.1-26.32-jre-headless][45],
  
  *[25-jre-headless-latest][12],
  [25.0.0-25.28-jre-headless][50],
  [25.0.1-25.30-jre-headless][52],
  [25.0.2-25.32-jre-headless][55],
  
  
  *[24-jre-headless-latest][13],
  [24.0.0-24.28-jre-headless][63],
  [24.0.1-24.30-jre-headless][65],
  [24.0.2-24.32-jre-headless][67],
  
  *[23-jre-headless-latest][14],
  [23.0.0-23.28-jre-headless][73],
  [23.0.1-23.30-jre-headless][75],
  [23.0.2-23.32-jre-headless][79],
  
  *[22-jre-headless-latest][15],
  [22.0.0-22.28-jre-headless][81],
  [22.0.1-22.30-jre-headless][85],
  [22.0.2-22.32-jre-headless][89],
  
  *[21-jre-headless-latest][16],
  [21.0.0-21.28.85-jre-headless][91],
  [21.0.1-21.30-jre-headless][95],
  [21.0.1-21.30.15-jre-headless][97],
  
  
  
  
  
  
  
  
  
  
  
  *[20-jre-headless-latest][17],
  [20.0.0-20.28.85-jre-headless][133],
  [20.0.1-20.30.11-jre-headless][135],
  [20.0.2-20.32.11-jre-headless][139],
  
  *[19-jre-headless-latest][18],
  [19.0.0-19.28.81-jre-headless][141],
  [19.0.1-19.30.11-jre-headless][145],
  [19.0.2-19.32.13-jre-headless][149],
  
  *[18-jre-headless-latest][19],
  [18.0.1-18.30.11-jre-headless][152],
  [18.0.2.1-18.32.13-jre-headless][156],
  [18.0.2-18.32.11-jre-headless][158],
  
  *[17-jre-headless-latest][20],
  [17.0.0-17.28.13-jre-headless][162],
  [17.0.1-17.30.15-jre-headless][167],
  [17.0.2-17.32.13-jre-headless][170],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][21],
  [15.0.7-15.40.19-jre-headless][247],
  [15.0.8-15.42.15-jre-headless][251],
  [15.0.9-15.44.13-jre-headless][253],
  
  
  *[13-jre-headless-latest][22],
  [13.0.11-13.48.19-jre-headless][273],
  [13.0.12-13.50.15-jre-headless][277],
  [13.0.13-13.52.15-jre-headless][278],
  
  
  *[11-jre-headless-latest][23],
  [11.0.15-11.56.19-jre-headless][305],
  [11.0.16.1-11.58.23-jre-headless][307],
  [11.0.16-11.58.15-jre-headless][311],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][24],
  [8u332-8.62.0.19-jre-headless][411],
  [8u342-8.64.0.15-jre-headless][415],
  [8u345-8.64.0.19-jre-headless][418],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[26-jre-latest][25],
  [26.0.0-26.28-jre][43],
  [26.0.2.1-26.32-jre][44],
  
  *[25-jre-latest][26],
  [25.0.0-25.28-jre][48],
  [25.0.1-25.30-jre][53],
  [25.0.2-25.32-jre][56],
  
  
  *[24-jre-latest][27],
  [24.0.0-24.28-jre][62],
  [24.0.1-24.30-jre][64],
  [24.0.2-24.32-jre][68],
  
  *[23-jre-latest][28],
  [23.0.0-23.28-jre][71],
  [23.0.1-23.30-jre][76],
  [23.0.2-23.32-jre][78],
  
  *[22-jre-latest][29],
  [22.0.0-22.28-jre][83],
  [22.0.1-22.30-jre][84],
  [22.0.2-22.32-jre][88],
  
  *[21-jre-latest][30],
  [21.0.0-21.28.85-jre][93],
  [21.0.1-21.30-jre][94],
  [21.0.1-21.30.15-jre][99],
  
  
  
  
  
  
  
  
  
  
  
  *[20-jre-latest][31],
  [20.0.0-20.28.85-jre][132],
  [20.0.1-20.30.11-jre][136],
  [20.0.2-20.32.11-jre][138],
  
  *[19-jre-latest][32],
  [19.0.0-19.28.81-jre][143],
  [19.0.1-19.30.11-jre][144],
  [19.0.2-19.32.13-jre][147],
  
  *[18-jre-latest][33],
  [18.0.1-18.30.11-jre][154],
  [18.0.2.1-18.32.13-jre][155],
  [18.0.2-18.32.11-jre][159],
  
  *[17-jre-latest][34],
  [17.0.0-17.28.13-jre][164],
  [17.0.1-17.30.15-jre][165],
  [17.0.2-17.32.13-jre][169],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][35],
  [16.0.0-16.28.11-jre][233],
  [16.0.1-16.30.15-jre][234],
  [16.0.2-16.32.15-jre][237],
  
  *[15-jre-latest][36],
  [15.0.7-15.40.19-jre][246],
  [15.0.8-15.42.15-jre][250],
  [15.0.9-15.44.13-jre][252],
  
  
  *[13-jre-latest][37],
  [13.0.11-13.48.19-jre][274],
  [13.0.12-13.50.15-jre][275],
  [13.0.13-13.52.15-jre][280],
  
  
  *[11-jre-latest][38],
  [11.0.15-11.56.19-jre][304],
  [11.0.16.1-11.58.23-jre][309],
  [11.0.16-11.58.15-jre][312],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][39],
  [8u332-8.62.0.19-jre][412],
  [8u342-8.64.0.15-jre][416],
  [8u345-8.64.0.19-jre][419],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[26-latest][40],
  [26.0.0-26.28][42],
  [26.0.2.1-26.32][46],
  
  *[25-latest][47],
  [25.0.0-25.28][49],
  [25.0.1-25.30][51],
  [25.0.2-25.32][54],
  
  
  *[24-latest][60],
  [24.0.0-24.28][61],
  [24.0.1-24.30][66],
  [24.0.2-24.32][69],
  
  *[23-latest][70],
  [23.0.0-23.28][72],
  [23.0.1-23.30][74],
  [23.0.2-23.32][77],
  
  *[22-latest][80],
  [22.0.0-22.28][82],
  [22.0.1-22.30][86],
  [22.0.2-22.32][87],
  
  *[21-latest][90],
  [21.0.0-21.28.85][92],
  [21.0.1-21.30][96],
  [21.0.1-21.30.15][98],
  
  
  
  
  
  
  
  
  
  
  
  *[20-latest][130],
  [20.0.0-20.28.85][131],
  [20.0.1-20.30.11][134],
  [20.0.2-20.32.11][137],
  
  *[19-latest][140],
  [19.0.0-19.28.81][142],
  [19.0.1-19.30.11][146],
  [19.0.2-19.32.13][148],
  
  
  *[18-latest][151],
  [18.0.1-18.30.11][153],
  [18.0.2.1-18.32.13][157],
  [18.0.2-18.32.11][160],
  
  *[17-latest][161],
  [17.0.0-17.28.13][163],
  [17.0.1-17.30.15][166],
  [17.0.2-17.32.13][168],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][231],
  [16.0.0-16.28.11][232],
  [16.0.1-16.30.15][235],
  [16.0.2-16.32.15][236],
  
  *[15-latest][238],
  [15.0.1-15.28.13][239],
  [15.0.1-15.28.51][240],
  [15.0.2-15.29.15][241],
  
  
  
  
  
  
  
  
  
  *[14-latest][258],
  [14.0.1-14.28.21][259],
  [14.0.2-14.29.23][260],
  
  *[13-latest][261],
  [13.0.1-13.28][262],
  [13.0.2-13.29][263],
  [13.0.3-13.31.11][264],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][284],
  [12.0.1-12.2][285],
  [12.0.2-12.3][286],
  [12-12.1][287],
  
  *[11-latest][288],
  [11.0.1-11.2][289],
  [11.0.2-11.29][290],
  [11.0.3-11.31][291],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][364],
  [10u01-10.2][365],
  [10u02-10.3][366],
  
  *[9-latest][367],
  [9-ea][368],
  [9u01-9.0.1.3][369],
  [9u04-9.0.4.1][370],
  
  
  *[8-latest][372],
  [8u05-8.1.0.6][373],
  [8u11-8.2.0.1][374],
  [8u20-8.3.0.1][375],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][471],
  [7u55-7.4.0.5][472],
  [7u60-7.5.0.1][473],
  [7u65-7.6.0.1][474],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][509],
  [6u49-6.4.0.6][510],
  [6u53-6.5.0.2][511],
  [6u56-6.6.0.1][512],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26-jre-headless-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.0-26.28-jre-headless/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.2.1-26.32-jre-headless/Dockerfile
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25-jre-headless-latest/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.0-25.28-jre-headless/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.1-25.30-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.2-25.32-jre-headless/Dockerfile
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-jre-headless-latest/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32-jre-headless/Dockerfile
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-headless-latest/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre-headless/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre-headless/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre-headless/Dockerfile
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-headless-latest/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre-headless/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre-headless/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre-headless/Dockerfile
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-headless-latest/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre-headless/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre-headless/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-headless-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre-headless/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-headless-latest/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre-headless/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre-headless/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-headless-latest/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre-headless/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre-headless/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre-headless/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-headless-latest/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre-headless/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre-headless/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-headless-latest/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre-headless/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre-headless/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-headless-latest/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre-headless/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre-headless/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-headless-latest/Dockerfile
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre-headless/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre-headless/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-headless-latest/Dockerfile
  [411]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre-headless/Dockerfile
  [415]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre-headless/Dockerfile
  [418]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26-jre-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.0-26.28-jre/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.2.1-26.32-jre/Dockerfile
  
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25-jre-latest/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.0-25.28-jre/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.1-25.30-jre/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.2-25.32-jre/Dockerfile
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-jre-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28-jre/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32-jre/Dockerfile
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-jre-latest/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28-jre/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30-jre/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32-jre/Dockerfile
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-jre-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30-jre/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32-jre/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-jre-latest/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85-jre/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-jre-latest/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85-jre/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11-jre/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11-jre/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-jre-latest/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81-jre/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13-jre/Dockerfile
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-jre-latest/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11-jre/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13-jre/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11-jre/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-jre-latest/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13-jre/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15-jre/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-jre-latest/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11-jre/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15-jre/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15-jre/Dockerfile
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-jre-latest/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.7-15.40.19-jre/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.8-15.42.15-jre/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.9-15.44.13-jre/Dockerfile
  
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-jre-latest/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.11-13.48.19-jre/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.12-13.50.15-jre/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.13-13.52.15-jre/Dockerfile
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-jre-latest/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.15-11.56.19-jre/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16.1-11.58.23-jre/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.16-11.58.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-jre-latest/Dockerfile
  [412]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u332-8.62.0.19-jre/Dockerfile
  [416]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u342-8.64.0.15-jre/Dockerfile
  [419]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u345-8.64.0.19-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.0-26.28/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/26.0.2.1-26.32/Dockerfile
  
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25-latest/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.0-25.28/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.1-25.30/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/25.0.2-25.32/Dockerfile
  
  
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.0-24.28/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.1-24.30/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/24.0.2-24.32/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.0-23.28/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.1-23.30/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/23.0.2-23.32/Dockerfile
  
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22-latest/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.0-22.28/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.1-22.30/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/22.0.2-22.32/Dockerfile
  
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21-latest/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.0-21.28.85/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/21.0.1-21.30.15/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20-latest/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.0-20.28.85/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.1-20.30.11/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/20.0.2-20.32.11/Dockerfile
  
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19-latest/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.0-19.28.81/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.1-19.30.11/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/19.0.2-19.32.13/Dockerfile
  
  
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18-latest/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.1-18.30.11/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2.1-18.32.13/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/18.0.2-18.32.11/Dockerfile
  
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17-latest/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.0-17.28.13/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.1-17.30.15/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16-latest/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.0-16.28.11/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.1-16.30.15/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/16.0.2-16.32.15/Dockerfile
  
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15-latest/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.13/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.1-15.28.51/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14-latest/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.1-14.28.21/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/14.0.2-14.29.23/Dockerfile
  
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13-latest/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.1-13.28/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.2-13.29/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-latest/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.1-12.2/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12.0.2-12.3/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/12-12.1/Dockerfile
  
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11-latest/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.1-11.2/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.2-11.29/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [364]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10-latest/Dockerfile
  [365]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u01-10.2/Dockerfile
  [366]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/10u02-10.3/Dockerfile
  
  [367]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-latest/Dockerfile
  [368]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9-ea/Dockerfile
  [369]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u01-9.0.1.3/Dockerfile
  [370]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/9u04-9.0.4.1/Dockerfile
  
  
  [372]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8-latest/Dockerfile
  [373]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u05-8.1.0.6/Dockerfile
  [374]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u11-8.2.0.1/Dockerfile
  [375]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/8u20-8.3.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [471]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7-latest/Dockerfile
  [472]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u55-7.4.0.5/Dockerfile
  [473]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u60-7.5.0.1/Dockerfile
  [474]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [509]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6-latest/Dockerfile
  [510]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u49-6.4.0.6/Dockerfile
  [511]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u53-6.5.0.2/Dockerfile
  [512]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/debian/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  