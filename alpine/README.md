Azul Zulu Alpine
================

The `zulu-openjdk-alpine` image includes Alpine-native Azul Zulu Builds of OpenJDK, which use the built-in musl libc functionality
and do not add glibc on top of the Alpine distribution.

[Azul Zulu Builds of OpenJDK][1] are fully tested, and TCK compliant builds of OpenJDK for Linux, Windows, and macOS operating systems.
For more information about Azul Zulu and how to use these Docker images, check:

  * [Azul Zulu Docker documentation on docs.azul.com][2]]
  * [Other Azul Zulu Docker images on hub.docker.com/azul/zulu-openjdk][3]


Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`20.0.1-20.30.11`, `20-latest` (*20-latest/Dockerfile)*][10]
  * [`19.0.2-19.32.13`, `19-latest` (*19-latest/Dockerfile)*][19]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][31]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][43]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][73]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][81]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][105]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][108]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][149]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][153]
  * [`8u372-8.70.0.23`, `8-latest` (*8-latest/Dockerfile)*][212]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][282]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][305]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [20-jre-headless-latest][16],
  [20.0.0-20.28.85-jre-headless][17],
  [20.0.1-20.30.11-jre-headless][18],
  
  * [19-jre-headless-latest][27],
  [19.0.0-19.28.81-jre-headless][28],
  [19.0.1-19.30.11-jre-headless][29],
  [19.0.2-19.32.13-jre-headless][30],
  
  * [18-jre-headless-latest][39],
  [18.0.1-18.30.11-jre-headless][40],
  [18.0.2-18.32.11-jre-headless][41],
  [18.0.2.1-18.32.13-jre-headless][42],
  
  * [17-jre-headless-latest][63],
  [17.0.0-17.28.13-jre-headless][64],
  [17.0.1-17.30.15-jre-headless][65],
  [17.0.2-17.32.13-jre-headless][66],
  [17.0.3-17.34.19-jre-headless][67],
  [17.0.4-17.36.13-jre-headless][68],
  [17.0.5-17.38.21-jre-headless][69],
  [17.0.6-17.40.19-jre-headless][70],
  [17.0.7-17.42.19-jre-headless][71],
  [17.0.4.1-17.36.17-jre-headless][72],
  
  * [15-jre-headless-latest][100],
  [15.0.7-15.40.19-jre-headless][101],
  [15.0.8-15.42.15-jre-headless][102],
  [15.0.9-15.44.13-jre-headless][103],
  [15.0.10-15.46.17-jre-headless][104],
  
  * [13-jre-headless-latest][136],
  [13.0.3-13.31.11-jre-headless][137],
  [13.0.4-13.33.25-jre-headless][138],
  [13.0.5-13.35.17-jre-headless][139],
  [13.0.6-13.37.21-jre-headless][140],
  [13.0.7-13.40.15-jre-headless][141],
  [13.0.8-13.42.17-jre-headless][142],
  [13.0.9-13.44.13-jre-headless][143],
  [13.0.10-13.46.15-jre-headless][144],
  [13.0.11-13.48.19-jre-headless][145],
  [13.0.12-13.50.15-jre-headless][146],
  [13.0.13-13.52.15-jre-headless][147],
  [13.0.14-13.54.17-jre-headless][148],
  
  * [11-jre-headless-latest][193],
  [11.0.5-11.35-jre-headless][196],
  [11.0.6-11.37-jre-headless][197],
  [11.0.7-11.39.15-jre-headless][198],
  [11.0.8-11.41.23-jre-headless][199],
  [11.0.9-11.43.21-jre-headless][200],
  [11.0.10-11.45.27-jre-headless][201],
  [11.0.12-11.50.19-jre-headless][202],
  [11.0.13-11.52.13-jre-headless][203],
  [11.0.14-11.54.23-jre-headless][204],
  [11.0.15-11.56.19-jre-headless][205],
  [11.0.16-11.58.15-jre-headless][206],
  [11.0.17-11.60.19-jre-headless][207],
  [11.0.18-11.62.17-jre-headless][208],
  [11.0.19-11.64.19-jre-headless][209],
  [11.0.14.1-11.54.25-jre-headless][210],
  [11.0.16.1-11.58.23-jre-headless][211],
  
  * [8-jre-headless-latest][264],
  [8u232-8.42.0.23-jre-headless][265],
  [8u242-8.44.0.11-jre-headless][266],
  [8u252-8.46.0.19-jre-headless][267],
  [8u262-8.48.0.51-jre-headless][268],
  [8u272-8.50.0.21-jre-headless][269],
  [8u275-8.50.0.51-jre-headless][270],
  [8u282-8.52.0.23-jre-headless][271],
  [8u302-8.56.0.21-jre-headless][272],
  [8u312-8.58.0.13-jre-headless][273],
  [8u322-8.60.0.21-jre-headless][274],
  [8u332-8.62.0.19-jre-headless][275],
  [8u342-8.64.0.15-jre-headless][276],
  [8u345-8.64.0.19-jre-headless][277],
  [8u352-8.66.0.15-jre-headless][278],
  [8u362-8.68.0.19-jre-headless][279],
  [8u362-8.68.0.21-jre-headless][280],
  [8u372-8.70.0.23-jre-headless][281],
  
  * [20-jre-latest][11],
  [20.0.0-20.28.85-jre][14],
  [20.0.1-20.30.11-jre][15],
  
  * [19-jre-latest][20],
  [19.0.0-19.28.81-jre][24],
  [19.0.1-19.30.11-jre][25],
  [19.0.2-19.32.13-jre][26],
  
  * [18-jre-latest][32],
  [18.0.1-18.30.11-jre][36],
  [18.0.2-18.32.11-jre][37],
  [18.0.2.1-18.32.13-jre][38],
  
  * [17-jre-latest][44],
  [17.0.0-17.28.13-jre][54],
  [17.0.1-17.30.15-jre][55],
  [17.0.2-17.32.13-jre][56],
  [17.0.3-17.34.19-jre][57],
  [17.0.4-17.36.13-jre][58],
  [17.0.5-17.38.21-jre][59],
  [17.0.6-17.40.19-jre][60],
  [17.0.7-17.42.19-jre][61],
  [17.0.4.1-17.36.17-jre][62],
  
  * [16-jre-latest][74],
  [16.0.0-16.28.11-jre][78],
  [16.0.1-16.30.15-jre][79],
  [16.0.2-16.32.15-jre][80],
  
  * [15-jre-latest][82],
  [15.0.0-15.27.17-jre][95],
  [15.0.7-15.40.19-jre][96],
  [15.0.8-15.42.15-jre][97],
  [15.0.9-15.44.13-jre][98],
  [15.0.10-15.46.17-jre][99],
  
  * [13-jre-latest][111],
  [13.0.3-13.31.11-jre][124],
  [13.0.4-13.33.25-jre][125],
  [13.0.5-13.35.17-jre][126],
  [13.0.6-13.37.21-jre][127],
  [13.0.7-13.40.15-jre][128],
  [13.0.8-13.42.17-jre][129],
  [13.0.9-13.44.13-jre][130],
  [13.0.10-13.46.15-jre][131],
  [13.0.11-13.48.19-jre][132],
  [13.0.12-13.50.15-jre][133],
  [13.0.13-13.52.15-jre][134],
  [13.0.14-13.54.17-jre][135],
  
  * [11-jre-latest][160],
  [11.0.3-11.31-jre][174],
  [11.0.4-11.33-jre][175],
  [11.0.5-11.35-jre][176],
  [11.0.6-11.37-jre][177],
  [11.0.7-11.39.15-jre][180],
  [11.0.8-11.41.23-jre][181],
  [11.0.9-11.43.21-jre][182],
  [11.0.10-11.45.27-jre][183],
  [11.0.11-11.48.21-jre][184],
  [11.0.12-11.50.19-jre][185],
  [11.0.13-11.52.13-jre][186],
  [11.0.14-11.54.23-jre][187],
  [11.0.15-11.56.19-jre][188],
  [11.0.16-11.58.15-jre][189],
  [11.0.17-11.60.19-jre][190],
  [11.0.18-11.62.17-jre][191],
  [11.0.19-11.64.19-jre][192],
  [11.0.14.1-11.54.25-jre][194],
  [11.0.16.1-11.58.23-jre][195],
  
  * [8-jre-latest][213],
  [8u212-8.38.0.13-jre][243],
  [8u222-8.40.0.25-jre][244],
  [8u232-8.42.0.21-jre][245],
  [8u232-8.42.0.23-jre][246],
  [8u242-8.44.0.11-jre][247],
  [8u252-8.46.0.19-jre][248],
  [8u262-8.48.0.51-jre][249],
  [8u272-8.50.0.21-jre][250],
  [8u275-8.50.0.51-jre][251],
  [8u282-8.52.0.23-jre][252],
  [8u292-8.54.0.21-jre][253],
  [8u302-8.56.0.21-jre][254],
  [8u312-8.58.0.13-jre][255],
  [8u322-8.60.0.21-jre][256],
  [8u332-8.62.0.19-jre][257],
  [8u342-8.64.0.15-jre][258],
  [8u345-8.64.0.19-jre][259],
  [8u352-8.66.0.15-jre][260],
  [8u362-8.68.0.19-jre][261],
  [8u362-8.68.0.21-jre][262],
  [8u372-8.70.0.23-jre][263],
  
  * [20-latest][10],
  [20.0.0-20.28.85][12],
  [20.0.1-20.30.11][13],
  
  * [19-latest][19],
  [19.0.0-19.28.81][21],
  [19.0.1-19.30.11][22],
  [19.0.2-19.32.13][23],
  
  * [18-latest][31],
  [18.0.1-18.30.11][33],
  [18.0.2-18.32.11][34],
  [18.0.2.1-18.32.13][35],
  
  * [17-latest][43],
  [17.0.0-17.28.13][45],
  [17.0.1-17.30.15][46],
  [17.0.2-17.32.13][47],
  [17.0.3-17.34.19][48],
  [17.0.4-17.36.13][49],
  [17.0.5-17.38.21][50],
  [17.0.6-17.40.19][51],
  [17.0.7-17.42.19][52],
  [17.0.4.1-17.36.17][53],
  
  * [16-latest][73],
  [16.0.0-16.28.11][75],
  [16.0.1-16.30.15][76],
  [16.0.2-16.32.15][77],
  
  * [15-latest][81],
  [15.0.0-15.27.17][83],
  [15.0.1-15.28.13][84],
  [15.0.1-15.28.51][85],
  [15.0.2-15.29.15][86],
  [15.0.3-15.32.15][87],
  [15.0.4-15.34.17][88],
  [15.0.5-15.36.13][89],
  [15.0.6-15.38.17][90],
  [15.0.7-15.40.19][91],
  [15.0.8-15.42.15][92],
  [15.0.9-15.44.13][93],
  [15.0.10-15.46.17][94],
  
  * [14-latest][105],
  [14.0.1-14.28.21][106],
  [14.0.2-14.29.23][107],
  
  * [13-latest][108],
  [13.0.1-13.28][109],
  [13.0.2-13.29][110],
  [13.0.3-13.31.11][112],
  [13.0.4-13.33.25][113],
  [13.0.5-13.35.17][114],
  [13.0.6-13.37.21][115],
  [13.0.7-13.40.15][116],
  [13.0.8-13.42.17][117],
  [13.0.9-13.44.13][118],
  [13.0.10-13.46.15][119],
  [13.0.11-13.48.19][120],
  [13.0.12-13.50.15][121],
  [13.0.13-13.52.15][122],
  [13.0.14-13.54.17][123],
  
  * [12-latest][149],
  [12.0.0-12.1][150],
  [12.0.1-12.2][151],
  [12.0.2-12.3][152],
  
  * [11-latest][153],
  [11.0.1-11.2][154],
  [11.0.2-11.29][155],
  [11.0.3-11.31][156],
  [11.0.4-11.33][157],
  [11.0.5-11.35][158],
  [11.0.6-11.37][159],
  [11.0.7-11.39.15][161],
  [11.0.8-11.41.23][162],
  [11.0.9-11.43.21][163],
  [11.0.10-11.45.27][164],
  [11.0.11-11.48.21][165],
  [11.0.12-11.50.19][166],
  [11.0.13-11.52.13][167],
  [11.0.14-11.54.23][168],
  [11.0.15-11.56.19][169],
  [11.0.16-11.58.15][170],
  [11.0.17-11.60.19][171],
  [11.0.18-11.62.17][172],
  [11.0.19-11.64.19][173],
  [11.0.14.1-11.54.25][178],
  [11.0.16.1-11.58.23][179],
  
  * [8-latest][212],
  [8u131-8.21.0.1][214],
  [8u144-8.23.0.3][215],
  [8u152-8.25.0.1][216],
  [8u162-8.27.0.7][217],
  [8u172-8.30.0.1][218],
  [8u181-8.31.0.1][219],
  [8u192-8.33.0.1][220],
  [8u202-8.36.0.3][221],
  [8u212-8.38.0.13][222],
  [8u222-8.40.0.25][223],
  [8u232-8.42.0.21][224],
  [8u232-8.42.0.23][225],
  [8u242-8.44.0.11][226],
  [8u252-8.46.0.19][227],
  [8u262-8.48.0.51][228],
  [8u272-8.50.0.21][229],
  [8u275-8.50.0.51][230],
  [8u282-8.52.0.23][231],
  [8u292-8.54.0.21][232],
  [8u302-8.56.0.21][233],
  [8u312-8.58.0.13][234],
  [8u322-8.60.0.21][235],
  [8u332-8.62.0.19][236],
  [8u342-8.64.0.15][237],
  [8u345-8.64.0.19][238],
  [8u352-8.66.0.15][239],
  [8u362-8.68.0.19][240],
  [8u362-8.68.0.21][241],
  [8u372-8.70.0.23][242],
  
  * [7-latest][282],
  [7u141-7.18.0.3][283],
  [7u154-7.20.0.3][284],
  [7u161-7.21.0.3][285],
  [7u171-7.22.0.3][286],
  [7u181-7.23.0.1][287],
  [7u191-7.24.0.1][288],
  [7u201-7.25.0.5][289],
  [7u211-7.27.0.1][290],
  [7u222-7.29.0.5][291],
  [7u232-7.31.0.5][292],
  [7u242-7.34.0.5][293],
  [7u252-7.36.0.5][294],
  [7u262-7.38.0.11][295],
  [7u272-7.40.0.15][296],
  [7u282-7.42.0.13][297],
  [7u285-7.42.0.51][298],
  [7u292-7.44.0.11][299],
  [7u302-7.46.0.11][300],
  [7u312-7.48.0.11][301],
  [7u332-7.52.0.11][302],
  [7u342-7.54.0.13][303],
  [7u352-7.56.0.11][304],
  
  * [6-latest][305],
  [6u93-6.16.0.1][306],
  [6u97-6.17.0.1][307],
  [6u99-6.18.0.3][308],
  [6u103-6.19.0.1][309],
  [6u107-6.20.0.1][310],
  [6u113-6.21.0.3][311],
  [6u119-6.22.0.3][312],
  

**Note**: Some of these may use glibc and predate the move to musl libc.

  [1]: https://www.azul.com/products/core/
  [2]: https://docs.azul.com/core/zulu-openjdk/install/docker
  [3]: https://hub.docker.com/r/azul/zulu-openjdk-alpine


  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-headless-latest/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre-headless/Dockerfile
  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre-headless/Dockerfile
  
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-headless-latest/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre-headless/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre-headless/Dockerfile
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre-headless/Dockerfile
  
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-headless-latest/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre-headless/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre-headless/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-headless-latest/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre-headless/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre-headless/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre-headless/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre-headless/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre-headless/Dockerfile
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre-headless/Dockerfile
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre-headless/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre-headless/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-headless-latest/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre-headless/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre-headless/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre-headless/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre-headless/Dockerfile
  
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-headless-latest/Dockerfile
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre-headless/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre-headless/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre-headless/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre-headless/Dockerfile
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre-headless/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre-headless/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre-headless/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre-headless/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre-headless/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre-headless/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre-headless/Dockerfile
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre-headless/Dockerfile
  
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-headless-latest/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre-headless/Dockerfile
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre-headless/Dockerfile
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre-headless/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre-headless/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre-headless/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre-headless/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre-headless/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre-headless/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre-headless/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre-headless/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre-headless/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre-headless/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre-headless/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre-headless/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre-headless/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-headless-latest/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre-headless/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre-headless/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre-headless/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre-headless/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre-headless/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre-headless/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre-headless/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre-headless/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre-headless/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre-headless/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre-headless/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre-headless/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre-headless/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre-headless/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre-headless/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre-headless/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-jre-latest/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85-jre/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11-jre/Dockerfile
  
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-jre-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81-jre/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11-jre/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13-jre/Dockerfile
  
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-jre-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11-jre/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11-jre/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13-jre/Dockerfile
  
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-jre-latest/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13-jre/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15-jre/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13-jre/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19-jre/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13-jre/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21-jre/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19-jre/Dockerfile
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19-jre/Dockerfile
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17-jre/Dockerfile
  
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-jre-latest/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11-jre/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15-jre/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15-jre/Dockerfile
  
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-jre-latest/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17-jre/Dockerfile
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19-jre/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15-jre/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13-jre/Dockerfile
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17-jre/Dockerfile
  
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-jre-latest/Dockerfile
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11-jre/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25-jre/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17-jre/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21-jre/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15-jre/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17-jre/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13-jre/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15-jre/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19-jre/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15-jre/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15-jre/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17-jre/Dockerfile
  
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-jre-latest/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31-jre/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33-jre/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35-jre/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37-jre/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15-jre/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23-jre/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21-jre/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27-jre/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21-jre/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19-jre/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13-jre/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23-jre/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19-jre/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15-jre/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19-jre/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17-jre/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19-jre/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25-jre/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23-jre/Dockerfile
  
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-jre-latest/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13-jre/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25-jre/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21-jre/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23-jre/Dockerfile
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11-jre/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19-jre/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51-jre/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21-jre/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51-jre/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23-jre/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21-jre/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21-jre/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13-jre/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21-jre/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19-jre/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15-jre/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19-jre/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15-jre/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19-jre/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21-jre/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.0-20.28.85/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/20.0.1-20.30.11/Dockerfile
  
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19-latest/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.0-19.28.81/Dockerfile
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.1-19.30.11/Dockerfile
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/19.0.2-19.32.13/Dockerfile
  
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18-latest/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.1-18.30.11/Dockerfile
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2-18.32.11/Dockerfile
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/18.0.2.1-18.32.13/Dockerfile
  
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17-latest/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.0-17.28.13/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.1-17.30.15/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.2-17.32.13/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.3-17.34.19/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4-17.36.13/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.5-17.38.21/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.6-17.40.19/Dockerfile
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.7-17.42.19/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/17.0.4.1-17.36.17/Dockerfile
  
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16-latest/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.0-16.28.11/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.1-16.30.15/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/16.0.2-16.32.15/Dockerfile
  
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.0-15.27.17/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.13/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.1-15.28.51/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.2-15.29.15/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.3-15.32.15/Dockerfile
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.4-15.34.17/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.5-15.36.13/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.6-15.38.17/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.7-15.40.19/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.8-15.42.15/Dockerfile
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.9-15.44.13/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/15.0.10-15.46.17/Dockerfile
  
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14-latest/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.1-14.28.21/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/14.0.2-14.29.23/Dockerfile
  
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13-latest/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.1-13.28/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.2-13.29/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.3-13.31.11/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.4-13.33.25/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.5-13.35.17/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.6-13.37.21/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.7-13.40.15/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.8-13.42.17/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.9-13.44.13/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.10-13.46.15/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.11-13.48.19/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.12-13.50.15/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.13-13.52.15/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/13.0.14-13.54.17/Dockerfile
  
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12-latest/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.0-12.1/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.1-12.2/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/12.0.2-12.3/Dockerfile
  
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11-latest/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.1-11.2/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.2-11.29/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.3-11.31/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.4-11.33/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.5-11.35/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.6-11.37/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.7-11.39.15/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.8-11.41.23/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.9-11.43.21/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.10-11.45.27/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.11-11.48.21/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.12-11.50.19/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.13-11.52.13/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14-11.54.23/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.15-11.56.19/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16-11.58.15/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.17-11.60.19/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.18-11.62.17/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.19-11.64.19/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.14.1-11.54.25/Dockerfile
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/11.0.16.1-11.58.23/Dockerfile
  
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8-latest/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u131-8.21.0.1/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u144-8.23.0.3/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u152-8.25.0.1/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u162-8.27.0.7/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u172-8.30.0.1/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u181-8.31.0.1/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u192-8.33.0.1/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u202-8.36.0.3/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u212-8.38.0.13/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u222-8.40.0.25/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.21/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u232-8.42.0.23/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u242-8.44.0.11/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u252-8.46.0.19/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u262-8.48.0.51/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u272-8.50.0.21/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u275-8.50.0.51/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u282-8.52.0.23/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u292-8.54.0.21/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u302-8.56.0.21/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u312-8.58.0.13/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u322-8.60.0.21/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u332-8.62.0.19/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u342-8.64.0.15/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u345-8.64.0.19/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u352-8.66.0.15/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.19/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u362-8.68.0.21/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/8u372-8.70.0.23/Dockerfile
  
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7-latest/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u141-7.18.0.3/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u154-7.20.0.3/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u161-7.21.0.3/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u171-7.22.0.3/Dockerfile
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u181-7.23.0.1/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u191-7.24.0.1/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u201-7.25.0.5/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u211-7.27.0.1/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u222-7.29.0.5/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u232-7.31.0.5/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u242-7.34.0.5/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u252-7.36.0.5/Dockerfile
  [295]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u262-7.38.0.11/Dockerfile
  [296]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u272-7.40.0.15/Dockerfile
  [297]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u282-7.42.0.13/Dockerfile
  [298]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u285-7.42.0.51/Dockerfile
  [299]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u292-7.44.0.11/Dockerfile
  [300]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u302-7.46.0.11/Dockerfile
  [301]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u312-7.48.0.11/Dockerfile
  [302]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u332-7.52.0.11/Dockerfile
  [303]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u342-7.54.0.13/Dockerfile
  [304]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/7u352-7.56.0.11/Dockerfile
  
  [305]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6-latest/Dockerfile
  [306]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u93-6.16.0.1/Dockerfile
  [307]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u97-6.17.0.1/Dockerfile
  [308]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u99-6.18.0.3/Dockerfile
  [309]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u103-6.19.0.1/Dockerfile
  [310]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u107-6.20.0.1/Dockerfile
  [311]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u113-6.21.0.3/Dockerfile
  [312]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine/6u119-6.22.0.3/Dockerfile
  