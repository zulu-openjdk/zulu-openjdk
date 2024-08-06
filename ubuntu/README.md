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


  * [`22.0.2-22.32`, `22-latest` (*22-latest/Dockerfile)*][38]
  * [`21.0.4-21.36`, `21-latest` (*21-latest/Dockerfile)*][56]
  * [`17.0.12-17.52`, `17-latest` (*17-latest/Dockerfile)*][123]
  * [`11.0.24-11.74`, `11-latest` (*11-latest/Dockerfile)*][245]
  * [`8u422-8.80`, `8-latest` (*8-latest/Dockerfile)*][310]

Previous
--------

Earlier Ubuntu Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[22-jre-headless-latest][11],
  [22-jre-headless-latest][41],
  [22.0.0-22.28-jre-headless][43],
  [22.0.1-22.30-jre-headless][49],
  
  
  *[21-jre-headless-latest][12],
  [21-jre-headless-latest][60],
  [21.0.0-21.28.85-jre-headless][61],
  [21.0.1-21.30-jre-headless][67],
  
  
  
  
  
  *[20-jre-headless-latest][13],
  [20-jre-headless-latest][88],
  [20.0.0-20.28.85-jre-headless][91],
  [20.0.1-20.30.11-jre-headless][93],
  
  
  *[19-jre-headless-latest][14],
  [19-jre-headless-latest][99],
  [19.0.0-19.28.81-jre-headless][101],
  [19.0.1-19.30.11-jre-headless][105],
  
  
  *[18-jre-headless-latest][15],
  [18-jre-headless-latest][113],
  [18.0.1-18.30.11-jre-headless][114],
  [18.0.2.1-18.32.13-jre-headless][118],
  
  
  *[17-jre-headless-latest][16],
  [17-jre-headless-latest][127],
  [17.0.0-17.28.13-jre-headless][128],
  [17.0.1-17.30.15-jre-headless][133],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][17],
  [15-jre-headless-latest][193],
  [15.0.7-15.40.19-jre-headless][202],
  [15.0.8-15.42.15-jre-headless][206],
  
  
  
  *[13-jre-headless-latest][18],
  [13-jre-headless-latest][218],
  [13.0.11-13.48.19-jre-headless][230],
  [13.0.12-13.50.15-jre-headless][234],
  
  
  
  *[11-jre-headless-latest][19],
  [11-jre-headless-latest][247],
  [11.0.15-11.56.19-jre-headless][264],
  [11.0.16.1-11.58.23-jre-headless][266],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][20],
  [8-jre-headless-latest][312],
  [8u332-8.62.0.19-jre-headless][350],
  [8u342-8.64.0.15-jre-headless][354],
  
  
  
  
  
  
  
  
  
  
  
  
  *[22-jre-crac-latest][21],
  [22-jdk-crac-latest][22],
  [22-jre-crac-latest][39],
  [22-jdk-crac-latest][42],
  
  
  
  
  
  *[22-jre-crac-latest][21],
  [22-jdk-crac-latest][22],
  [22-jre-crac-latest][39],
  [22-jdk-crac-latest][42],
  
  
  
  
  
  *[21-jre-crac-latest][23],
  [21-jdk-crac-latest][24],
  [21-jre-crac-latest][57],
  [21-jdk-crac-latest][59],
  
  
  
  
  
  
  
  
  *[21-jre-crac-latest][23],
  [21-jdk-crac-latest][24],
  [21-jre-crac-latest][57],
  [21-jdk-crac-latest][59],
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][25],
  [17-jdk-crac-latest][26],
  [17-jre-crac-latest][124],
  [17-jdk-crac-latest][126],
  
  
  
  
  
  
  
  
  
  *[17-jre-crac-latest][25],
  [17-jdk-crac-latest][26],
  [17-jre-crac-latest][124],
  [17-jdk-crac-latest][126],
  
  
  
  
  
  
  
  
  
  *[22-jre-latest][27],
  [22-jre-latest][40],
  [22.0.0-22.28-jre][46],
  [22.0.1-22.30-jre][47],
  
  
  *[21-jre-latest][28],
  [21-jre-latest][58],
  [21.0.0-21.28.85-jre][63],
  [21.0.1-21.30-jre][65],
  
  
  
  
  
  *[20-jre-latest][29],
  [20-jre-latest][87],
  [20.0.0-20.28.85-jre][90],
  [20.0.1-20.30.11-jre][94],
  
  
  *[19-jre-latest][30],
  [19-jre-latest][100],
  [19.0.0-19.28.81-jre][103],
  [19.0.1-19.30.11-jre][104],
  
  
  *[18-jre-latest][31],
  [18-jre-latest][112],
  [18.0.1-18.30.11-jre][116],
  [18.0.2.1-18.32.13-jre][117],
  
  
  *[17-jre-latest][32],
  [17-jre-latest][125],
  [17.0.0-17.28.13-jre][130],
  [17.0.1-17.30.15-jre][131],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][33],
  [16-jre-latest][185],
  [16.0.0-16.28.11-jre][187],
  [16.0.1-16.30.15-jre][188],
  
  
  *[15-jre-latest][34],
  [15-jre-latest][192],
  [15.0.7-15.40.19-jre][201],
  [15.0.8-15.42.15-jre][205],
  
  
  
  *[13-jre-latest][35],
  [13-jre-latest][217],
  [13.0.11-13.48.19-jre][231],
  [13.0.12-13.50.15-jre][232],
  
  
  
  *[11-jre-latest][36],
  [11-jre-latest][246],
  [11.0.15-11.56.19-jre][263],
  [11.0.16.1-11.58.23-jre][268],
  
  
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][37],
  [8-jre-latest][311],
  [8u332-8.62.0.19-jre][351],
  [8u342-8.64.0.15-jre][355],
  
  
  
  
  
  
  
  
  
  
  
  
  *[22-latest][38],
  [22.0.0-22.28][44],
  [22.0.1-22.30][50],
  [22.0.2-22.32][52],
  
  *[21-latest][56],
  [21.0.0-21.28.85][62],
  [21.0.1-21.30][68],
  [21.0.1-21.30.15][70],
  
  
  
  
  *[20-latest][86],
  [20.0.0-20.28.85][89],
  [20.0.1-20.30.11][92],
  [20.0.2-20.32.11][95],
  
  *[19-latest][98],
  [19.0.0-19.28.81][102],
  [19.0.1-19.30.11][106],
  [19.0.2-19.32.13][108],
  
  
  *[18-latest][111],
  [18.0.1-18.30.11][115],
  [18.0.2.1-18.32.13][119],
  [18.0.2-18.32.11][122],
  
  *[17-latest][123],
  [17.0.0-17.28.13][129],
  [17.0.1-17.30.15][132],
  [17.0.2-17.32.13][134],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][184],
  [16.0.0-16.28.11][186],
  [16.0.2-16.32.15][189],
  
  *[15-latest][191],
  [15.0.1-15.28.13][194],
  [15.0.1-15.28.51][195],
  [15.0.2-15.29.15][196],
  
  
  
  
  
  
  
  
  
  *[14-latest][213],
  [14.0.1-14.28.21][214],
  [14.0.2-14.29.23][215],
  
  *[13-latest][216],
  [13.0.1-13.28][219],
  [13.0.2-13.29][220],
  [13.0.3-13.31.11][221],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-latest][241],
  [12.0.1-12.2][242],
  [12.0.2-12.3][243],
  [12-12.1][244],
  
  *[11-latest][245],
  [11.0.1-11.2][248],
  [11.0.2-11.29][249],
  [11.0.3-11.31][250],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][302],
  [10u01-10.2][303],
  [10u02-10.3][304],
  
  *[9-latest][305],
  [9-ea][306],
  [9u01-9.0.1.3][307],
  [9u04-9.0.4.1][308],
  
  
  *[8-latest][310],
  [8u05-8.1.0.6][313],
  [8u11-8.2.0.1][314],
  [8u20-8.3.0.1][315],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][389],
  [7u55-7.4.0.5][390],
  [7u60-7.5.0.1][391],
  [7u65-7.6.0.1][392],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][427],
  [6u49-6.4.0.6][428],
  [6u53-6.5.0.2][429],
  [6u56-6.6.0.1][430],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-headless-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre-headless/Dockerfile
  
  
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-headless-latest/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre-headless/Dockerfile
  
  
  
  
  
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-headless-latest/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre-headless/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre-headless/Dockerfile
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-headless-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre-headless/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre-headless/Dockerfile
  
  
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-headless-latest/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre-headless/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-headless-latest/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre-headless/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-headless-latest/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre-headless/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre-headless/Dockerfile
  
  
  
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-headless-latest/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre-headless/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre-headless/Dockerfile
  
  
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-headless-latest/Dockerfile
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre-headless/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-headless-latest/Dockerfile
  [350]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre-headless/Dockerfile
  [354]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  
  
  
  
  
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-crac-latest/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jdk-crac-latest/Dockerfile
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-crac-latest/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-crac-latest/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jdk-crac-latest/Dockerfile
  
  
  
  
  
  
  
  
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-jre-latest/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28-jre/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30-jre/Dockerfile
  
  
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-jre-latest/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85-jre/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30-jre/Dockerfile
  
  
  
  
  
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-jre-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85-jre/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11-jre/Dockerfile
  
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-jre-latest/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81-jre/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11-jre/Dockerfile
  
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-jre-latest/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11-jre/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13-jre/Dockerfile
  
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-jre-latest/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13-jre/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-jre-latest/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11-jre/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.1-16.30.15-jre/Dockerfile
  
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-jre-latest/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.7-15.40.19-jre/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.8-15.42.15-jre/Dockerfile
  
  
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-jre-latest/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.11-13.48.19-jre/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.12-13.50.15-jre/Dockerfile
  
  
  
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-jre-latest/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.15-11.56.19-jre/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.16.1-11.58.23-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-jre-latest/Dockerfile
  [351]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u332-8.62.0.19-jre/Dockerfile
  [355]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u342-8.64.0.15-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.0-22.28/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.1-22.30/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/22.0.2-22.32/Dockerfile
  
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21-latest/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.0-21.28.85/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/21.0.1-21.30.15/Dockerfile
  
  
  
  
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20-latest/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.0-20.28.85/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.1-20.30.11/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/20.0.2-20.32.11/Dockerfile
  
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19-latest/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.0-19.28.81/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.1-19.30.11/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/19.0.2-19.32.13/Dockerfile
  
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18-latest/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.1-18.30.11/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2.1-18.32.13/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/18.0.2-18.32.11/Dockerfile
  
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17-latest/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.0-17.28.13/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.1-17.30.15/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/17.0.2-17.32.13/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16-latest/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.0-16.28.11/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/16.0.2-16.32.15/Dockerfile
  
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15-latest/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.13/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.1-15.28.51/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/15.0.2-15.29.15/Dockerfile
  
  
  
  
  
  
  
  
  
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14-latest/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.1-14.28.21/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/14.0.2-14.29.23/Dockerfile
  
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13-latest/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.1-13.28/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.2-13.29/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-latest/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.1-12.2/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12.0.2-12.3/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/12-12.1/Dockerfile
  
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11-latest/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.1-11.2/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.2-11.29/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10-latest/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u01-10.2/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/10u02-10.3/Dockerfile
  
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-latest/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9-ea/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u01-9.0.1.3/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/9u04-9.0.4.1/Dockerfile
  
  
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8-latest/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u05-8.1.0.6/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u11-8.2.0.1/Dockerfile
  [315]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/8u20-8.3.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [389]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7-latest/Dockerfile
  [390]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u55-7.4.0.5/Dockerfile
  [391]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u60-7.5.0.1/Dockerfile
  [392]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/7u65-7.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [427]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6-latest/Dockerfile
  [428]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u49-6.4.0.6/Dockerfile
  [429]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u53-6.5.0.2/Dockerfile
  [430]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/ubuntu/6u56-6.6.0.1/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  