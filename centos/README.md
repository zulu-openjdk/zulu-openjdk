Azul Zulu CentOS
================

These Docker images of Azul Zulu Build of OpenJDK are based on CentOS.

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


  * [`22.0.1-22.30`, `22-latest` (*22-latest/Dockerfile)*][11]
  * [`21.0.1-21.30.15`, `21-latest` (*21-latest/Dockerfile)*][20]
  * [`20.0.2-20.32.11`, `20-latest` (*20-latest/Dockerfile)*][38]
  * [`19.0.2-19.32.15`, `19-latest` (*19-latest/Dockerfile)*][50]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][63]
  * [`17.0.8.1-17.44.53`, `17-latest` (*17-latest/Dockerfile)*][75]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][123]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][131]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][154]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][157]
  * [`12.0.2-12.3`, `12-12.1` (*12-12.1/Dockerfile)*][182]
  * [`11.0.20.1-11.66.19`, `11-latest` (*11-latest/Dockerfile)*][186]
  * [`10u02-10.3`, `10-latest` (*10-latest/Dockerfile)*][240]
  * [`9u07-9.0.7.1`, `9-ea` (*9-ea/Dockerfile)*][243]
  * [`8u392-8.74.0.17`, `8-latest` (*8-latest/Dockerfile)*][248]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][324]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][359]

Previous
--------

Earlier CentOS Docker image tags(the most recent 4 tags) of Azul Zulu for previous update releases of OpenJDK are as follows:


  *[22-jre-headless-latest][17],
  [22.0.0-22.28-jre-headless][18],
  [22.0.1-22.30-jre-headless][19],
  
  *[21-jre-headless-latest][32],
  [21.0.1-21.30-jre-headless][33],
  [21.0.2-21.32-jre-headless][34],
  [21.0.3-21.34-jre-headless][35],
  
  
  
  *[20-jre-headless-latest][46],
  [20.0.0-20.28.85-jre-headless][47],
  [20.0.1-20.30.11-jre-headless][48],
  [20.0.2-20.32.11-jre-headless][49],
  
  *[19-jre-headless-latest][59],
  [19.0.0-19.28.81-jre-headless][60],
  [19.0.1-19.30.11-jre-headless][61],
  [19.0.2-19.32.13-jre-headless][62],
  
  *[18-jre-headless-latest][71],
  [18.0.1-18.30.11-jre-headless][72],
  [18.0.2-18.32.11-jre-headless][73],
  [18.0.2.1-18.32.13-jre-headless][74],
  
  *[17-jre-headless-latest][107],
  [17.0.9-17.46-jre-headless][108],
  [17.0.10-17.48-jre-headless][109],
  [17.0.11-17.50-jre-headless][110],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[15-jre-headless-latest][149],
  [15.0.7-15.40.19-jre-headless][150],
  [15.0.8-15.42.15-jre-headless][151],
  [15.0.9-15.44.13-jre-headless][152],
  
  
  *[13-jre-headless-latest][177],
  [13.0.11-13.48.19-jre-headless][178],
  [13.0.12-13.50.15-jre-headless][179],
  [13.0.13-13.52.15-jre-headless][180],
  
  
  *[11-jre-headless-latest][225],
  [11.0.21-11.68-jre-headless][228],
  [11.0.22-11.70-jre-headless][229],
  [11.0.23-11.72-jre-headless][230],
  
  
  
  
  
  
  
  
  
  
  *[8-jre-headless-latest][311],
  [8u392-8.74-jre-headless][312],
  [8u402-8.76-jre-headless][313],
  [8u412-8.78-jre-headless][314],
  
  
  
  
  
  
  
  
  
  
  *[22-jre-latest][14],
  [22.0.0-22.28-jre][15],
  [22.0.1-22.30-jre][16],
  
  *[21-jre-latest][24],
  [21.0.1-21.30-jre][27],
  [21.0.2-21.32-jre][28],
  [21.0.3-21.34-jre][29],
  
  
  
  *[20-jre-latest][39],
  [20.0.0-20.28.85-jre][43],
  [20.0.1-20.30.11-jre][44],
  [20.0.2-20.32.11-jre][45],
  
  *[19-jre-latest][51],
  [19.0.0-19.28.81-jre][56],
  [19.0.1-19.30.11-jre][57],
  [19.0.2-19.32.13-jre][58],
  
  *[18-jre-latest][64],
  [18.0.1-18.30.11-jre][68],
  [18.0.2-18.32.11-jre][69],
  [18.0.2.1-18.32.13-jre][70],
  
  *[17-jre-latest][77],
  [17.0.9-17.46-jre][90],
  [17.0.10-17.48-jre][91],
  [17.0.11-17.50-jre][92],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-jre-latest][124],
  [16.0.0-16.28.11-jre][128],
  [16.0.1-16.30.15-jre][129],
  [16.0.2-16.32.15-jre][130],
  
  *[15-jre-latest][132],
  [15.0.7-15.40.19-jre][145],
  [15.0.8-15.42.15-jre][146],
  [15.0.9-15.44.13-jre][147],
  
  
  *[13-jre-latest][160],
  [13.0.11-13.48.19-jre][173],
  [13.0.12-13.50.15-jre][174],
  [13.0.13-13.52.15-jre][175],
  
  
  *[11-jre-latest][193],
  [11.0.21-11.68-jre][212],
  [11.0.22-11.70-jre][213],
  [11.0.23-11.72-jre][214],
  
  
  
  
  
  
  
  
  
  
  *[8-jre-latest][252],
  [8u392-8.74-jre][276],
  [8u402-8.76-jre][277],
  [8u412-8.78-jre][278],
  
  
  
  
  
  
  
  
  
  
  *[22-latest][11],
  [22.0.0-22.28][12],
  [22.0.1-22.30][13],
  
  *[21-latest][20],
  [21.0.1-21.30][21],
  [21.0.2-21.32][22],
  [21.0.3-21.34][23],
  
  
  
  *[20-latest][38],
  [20.0.0-20.28.85][40],
  [20.0.1-20.30.11][41],
  [20.0.2-20.32.11][42],
  
  *[19-latest][50],
  [19.0.0-19.28.81][52],
  [19.0.1-19.30.11][53],
  [19.0.2-19.32.13][54],
  
  
  *[18-latest][63],
  [18.0.1-18.30.11][65],
  [18.0.2-18.32.11][66],
  [18.0.2.1-18.32.13][67],
  
  *[17-latest][75],
  [17.0.9-17.46][76],
  [17.0.10-17.48][78],
  [17.0.11-17.50][79],
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[16-latest][123],
  [16.0.0-16.28.11][125],
  [16.0.1-16.30.15][126],
  [16.0.2-16.32.15][127],
  
  *[15-latest][131],
  [15.0.0-15.27.17][133],
  [15.0.1-15.28.13][134],
  [15.0.1-15.28.51][135],
  
  
  
  
  
  
  
  
  
  
  *[14-latest][154],
  [14.0.1-14.28.21][155],
  [14.0.2-14.29.23][156],
  
  *[13-latest][157],
  [13.0.1-13.28][158],
  [13.0.2-13.29][159],
  [13.0.3-13.31.11][161],
  
  
  
  
  
  
  
  
  
  
  
  
  *[12-12.1][182],
  [12-latest][183],
  [12.0.1-12.2][184],
  [12.0.2-12.3][185],
  
  *[11-latest][186],
  [11.0.1-11.2][187],
  [11.0.2-11.29][188],
  [11.0.3-11.31][189],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[10-latest][240],
  [10u01-10.2][241],
  [10u02-10.3][242],
  
  *[9-ea][243],
  [9-latest][244],
  [9u01-9.0.1.3][245],
  [9u04-9.0.4.1][246],
  
  
  *[8-latest][248],
  [8u392-8.74][249],
  [8u402-8.76][250],
  [8u412-8.78][251],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[7-latest][324],
  [7u65-7.6.0.1][325],
  [7u72-7.7.0.1][326],
  [7u76-7.8.0.3][327],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  *[6-latest][359],
  [6u53-6.5.0.2][360],
  [6u56-6.6.0.1][361],
  [6u59-6.7.0.2][362],
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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


  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-headless-latest/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28-jre-headless/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30-jre-headless/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-headless-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre-headless/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32-jre-headless/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.3-21.34-jre-headless/Dockerfile
  
  
  
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-headless-latest/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre-headless/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre-headless/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre-headless/Dockerfile
  
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-headless-latest/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre-headless/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre-headless/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-headless-latest/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre-headless/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre-headless/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-headless-latest/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre-headless/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48-jre-headless/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.11-17.50-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-headless-latest/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre-headless/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre-headless/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre-headless/Dockerfile
  
  
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-headless-latest/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre-headless/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre-headless/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre-headless/Dockerfile
  
  
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-headless-latest/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre-headless/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.22-11.70-jre-headless/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.23-11.72-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-headless-latest/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre-headless/Dockerfile
  [313]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76-jre-headless/Dockerfile
  [314]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u412-8.78-jre-headless/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30-jre/Dockerfile
  
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-jre-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.3-21.34-jre/Dockerfile
  
  
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-jre-latest/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85-jre/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11-jre/Dockerfile
  
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-jre-latest/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81-jre/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13-jre/Dockerfile
  
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-jre-latest/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11-jre/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11-jre/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13-jre/Dockerfile
  
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-jre-latest/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46-jre/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48-jre/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.11-17.50-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-jre-latest/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11-jre/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15-jre/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15-jre/Dockerfile
  
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-jre-latest/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.7-15.40.19-jre/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.8-15.42.15-jre/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.9-15.44.13-jre/Dockerfile
  
  
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-jre-latest/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.11-13.48.19-jre/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.12-13.50.15-jre/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.13-13.52.15-jre/Dockerfile
  
  
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-jre-latest/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.21-11.68-jre/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.22-11.70-jre/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.23-11.72-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-jre-latest/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74-jre/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76-jre/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u412-8.78-jre/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.0-22.28/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/22.0.1-22.30/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.1-21.30/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.2-21.32/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/21.0.3-21.34/Dockerfile
  
  
  
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.0-20.28.85/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.1-20.30.11/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/20.0.2-20.32.11/Dockerfile
  
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19-latest/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.0-19.28.81/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.1-19.30.11/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/19.0.2-19.32.13/Dockerfile
  
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18-latest/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.1-18.30.11/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2-18.32.11/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/18.0.2.1-18.32.13/Dockerfile
  
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17-latest/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.9-17.46/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.10-17.48/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/17.0.11-17.50/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16-latest/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.0-16.28.11/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.1-16.30.15/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/16.0.2-16.32.15/Dockerfile
  
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15-latest/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.0-15.27.17/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.13/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/15.0.1-15.28.51/Dockerfile
  
  
  
  
  
  
  
  
  
  
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14-latest/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.1-14.28.21/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/14.0.2-14.29.23/Dockerfile
  
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13-latest/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.1-13.28/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.2-13.29/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/13.0.3-13.31.11/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-12.1/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12-latest/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.1-12.2/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/12.0.2-12.3/Dockerfile
  
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11-latest/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.1-11.2/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.2-11.29/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/11.0.3-11.31/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10-latest/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u01-10.2/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/10u02-10.3/Dockerfile
  
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-ea/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9-latest/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u01-9.0.1.3/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/9u04-9.0.4.1/Dockerfile
  
  
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8-latest/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u392-8.74/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u402-8.76/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/8u412-8.78/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [324]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7-latest/Dockerfile
  [325]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u65-7.6.0.1/Dockerfile
  [326]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u72-7.7.0.1/Dockerfile
  [327]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/7u76-7.8.0.3/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  [359]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6-latest/Dockerfile
  [360]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u53-6.5.0.2/Dockerfile
  [361]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u56-6.6.0.1/Dockerfile
  [362]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/centos/6u59-6.7.0.2/Dockerfile
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  