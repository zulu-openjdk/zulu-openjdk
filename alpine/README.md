Azul Zulu Alpine
================

The `zulu-openjdk-alpine` image includes Alpine-native Azul Zulu Builds of OpenJDK, which use the built-in musl libc functionality
and do not add glibc on top of the Alpine distribution.

[Azul Zulu Builds of OpenJDK][1] are fully tested, and TCK compliant builds of OpenJDK for Linux, Windows, and macOS operating systems.
For more information about Azul Zulu and how to use these Docker images, check:

  * [Azul documentation][2]
  * [azul/zulu-openjdk-alpine][3]


Tags and `Dockerfile` links
===========================

Most Recent
-----------


  * [`19.0.2-19.32.13`, `19-latest` (*19-latest/Dockerfile)*][10]
  * [`18.0.2.1-18.32.13`, `18-latest` (*18-latest/Dockerfile)*][22]
  * [`17.0.4.1-17.36.17`, `17-latest` (*17-latest/Dockerfile)*][34]
  * [`16.0.2-16.32.15`, `16-latest` (*16-latest/Dockerfile)*][61]
  * [`15.0.10-15.46.17`, `15-latest` (*15-latest/Dockerfile)*][69]
  * [`14.0.2-14.29.23`, `14-latest` (*14-latest/Dockerfile)*][93]
  * [`13.0.14-13.54.17`, `13-latest` (*13-latest/Dockerfile)*][96]
  * [`12.0.2-12.3`, `12-latest` (*12-latest/Dockerfile)*][137]
  * [`11.0.16.1-11.58.23`, `11-latest` (*11-latest/Dockerfile)*][141]
  * [`8u362-8.68.0.21`, `8-latest` (*8-latest/Dockerfile)*][197]
  * [`7u352-7.56.0.11`, `7-latest` (*7-latest/Dockerfile)*][264]
  * [`6u119-6.22.0.3`, `6-latest` (*6-latest/Dockerfile)*][287]

Previous
--------

Earlier Alpine Docker image tags of Azul Zulu for previous update releases of OpenJDK are as follows:


  * [19-jre-headless-latest][18],
  [19.0.0-19.28.81-jre-headless][19],
  [19.0.1-19.30.11-jre-headless][20],
  [19.0.2-19.32.13-jre-headless][21],
  
  * [18-jre-headless-latest][30],
  [18.0.1-18.30.11-jre-headless][31],
  [18.0.2-18.32.11-jre-headless][32],
  [18.0.2.1-18.32.13-jre-headless][33],
  
  * [17-jre-headless-latest][52],
  [17.0.0-17.28.13-jre-headless][53],
  [17.0.1-17.30.15-jre-headless][54],
  [17.0.2-17.32.13-jre-headless][55],
  [17.0.3-17.34.19-jre-headless][56],
  [17.0.4-17.36.13-jre-headless][57],
  [17.0.5-17.38.21-jre-headless][58],
  [17.0.6-17.40.19-jre-headless][59],
  [17.0.4.1-17.36.17-jre-headless][60],
  
  * [15-jre-headless-latest][88],
  [15.0.7-15.40.19-jre-headless][89],
  [15.0.8-15.42.15-jre-headless][90],
  [15.0.9-15.44.13-jre-headless][91],
  [15.0.10-15.46.17-jre-headless][92],
  
  * [13-jre-headless-latest][124],
  [13.0.3-13.31.11-jre-headless][125],
  [13.0.4-13.33.25-jre-headless][126],
  [13.0.5-13.35.17-jre-headless][127],
  [13.0.6-13.37.21-jre-headless][128],
  [13.0.7-13.40.15-jre-headless][129],
  [13.0.8-13.42.17-jre-headless][130],
  [13.0.9-13.44.13-jre-headless][131],
  [13.0.10-13.46.15-jre-headless][132],
  [13.0.11-13.48.19-jre-headless][133],
  [13.0.12-13.50.15-jre-headless][134],
  [13.0.13-13.52.15-jre-headless][135],
  [13.0.14-13.54.17-jre-headless][136],
  
  * [11-jre-headless-latest][179],
  [11.0.5-11.35-jre-headless][182],
  [11.0.6-11.37-jre-headless][183],
  [11.0.7-11.39.15-jre-headless][184],
  [11.0.8-11.41.23-jre-headless][185],
  [11.0.9-11.43.21-jre-headless][186],
  [11.0.10-11.45.27-jre-headless][187],
  [11.0.12-11.50.19-jre-headless][188],
  [11.0.13-11.52.13-jre-headless][189],
  [11.0.14-11.54.23-jre-headless][190],
  [11.0.15-11.56.19-jre-headless][191],
  [11.0.16-11.58.15-jre-headless][192],
  [11.0.17-11.60.19-jre-headless][193],
  [11.0.18-11.62.17-jre-headless][194],
  [11.0.14.1-11.54.25-jre-headless][195],
  [11.0.16.1-11.58.23-jre-headless][196],
  
  * [8-jre-headless-latest][247],
  [8u232-8.42.0.23-jre-headless][248],
  [8u242-8.44.0.11-jre-headless][249],
  [8u252-8.46.0.19-jre-headless][250],
  [8u262-8.48.0.51-jre-headless][251],
  [8u272-8.50.0.21-jre-headless][252],
  [8u275-8.50.0.51-jre-headless][253],
  [8u282-8.52.0.23-jre-headless][254],
  [8u302-8.56.0.21-jre-headless][255],
  [8u312-8.58.0.13-jre-headless][256],
  [8u322-8.60.0.21-jre-headless][257],
  [8u332-8.62.0.19-jre-headless][258],
  [8u342-8.64.0.15-jre-headless][259],
  [8u345-8.64.0.19-jre-headless][260],
  [8u352-8.66.0.15-jre-headless][261],
  [8u362-8.68.0.19-jre-headless][262],
  [8u362-8.68.0.21-jre-headless][263],
  
  * [19-jre-latest][11],
  [19.0.0-19.28.81-jre][15],
  [19.0.1-19.30.11-jre][16],
  [19.0.2-19.32.13-jre][17],
  
  * [18-jre-latest][23],
  [18.0.1-18.30.11-jre][27],
  [18.0.2-18.32.11-jre][28],
  [18.0.2.1-18.32.13-jre][29],
  
  * [17-jre-latest][35],
  [17.0.0-17.28.13-jre][44],
  [17.0.1-17.30.15-jre][45],
  [17.0.2-17.32.13-jre][46],
  [17.0.3-17.34.19-jre][47],
  [17.0.4-17.36.13-jre][48],
  [17.0.5-17.38.21-jre][49],
  [17.0.6-17.40.19-jre][50],
  [17.0.4.1-17.36.17-jre][51],
  
  * [16-jre-latest][62],
  [16.0.0-16.28.11-jre][66],
  [16.0.1-16.30.15-jre][67],
  [16.0.2-16.32.15-jre][68],
  
  * [15-jre-latest][70],
  [15.0.0-15.27.17-jre][83],
  [15.0.7-15.40.19-jre][84],
  [15.0.8-15.42.15-jre][85],
  [15.0.9-15.44.13-jre][86],
  [15.0.10-15.46.17-jre][87],
  
  * [13-jre-latest][99],
  [13.0.3-13.31.11-jre][112],
  [13.0.4-13.33.25-jre][113],
  [13.0.5-13.35.17-jre][114],
  [13.0.6-13.37.21-jre][115],
  [13.0.7-13.40.15-jre][116],
  [13.0.8-13.42.17-jre][117],
  [13.0.9-13.44.13-jre][118],
  [13.0.10-13.46.15-jre][119],
  [13.0.11-13.48.19-jre][120],
  [13.0.12-13.50.15-jre][121],
  [13.0.13-13.52.15-jre][122],
  [13.0.14-13.54.17-jre][123],
  
  * [11-jre-latest][148],
  [11.0.3-11.31-jre][161],
  [11.0.4-11.33-jre][162],
  [11.0.5-11.35-jre][163],
  [11.0.6-11.37-jre][164],
  [11.0.7-11.39.15-jre][167],
  [11.0.8-11.41.23-jre][168],
  [11.0.9-11.43.21-jre][169],
  [11.0.10-11.45.27-jre][170],
  [11.0.11-11.48.21-jre][171],
  [11.0.12-11.50.19-jre][172],
  [11.0.13-11.52.13-jre][173],
  [11.0.14-11.54.23-jre][174],
  [11.0.15-11.56.19-jre][175],
  [11.0.16-11.58.15-jre][176],
  [11.0.17-11.60.19-jre][177],
  [11.0.18-11.62.17-jre][178],
  [11.0.14.1-11.54.25-jre][180],
  [11.0.16.1-11.58.23-jre][181],
  
  * [8-jre-latest][198],
  [8u212-8.38.0.13-jre][227],
  [8u222-8.40.0.25-jre][228],
  [8u232-8.42.0.21-jre][229],
  [8u232-8.42.0.23-jre][230],
  [8u242-8.44.0.11-jre][231],
  [8u252-8.46.0.19-jre][232],
  [8u262-8.48.0.51-jre][233],
  [8u272-8.50.0.21-jre][234],
  [8u275-8.50.0.51-jre][235],
  [8u282-8.52.0.23-jre][236],
  [8u292-8.54.0.21-jre][237],
  [8u302-8.56.0.21-jre][238],
  [8u312-8.58.0.13-jre][239],
  [8u322-8.60.0.21-jre][240],
  [8u332-8.62.0.19-jre][241],
  [8u342-8.64.0.15-jre][242],
  [8u345-8.64.0.19-jre][243],
  [8u352-8.66.0.15-jre][244],
  [8u362-8.68.0.19-jre][245],
  [8u362-8.68.0.21-jre][246],
  
  * [19-latest][10],
  [19.0.0-19.28.81][12],
  [19.0.1-19.30.11][13],
  [19.0.2-19.32.13][14],
  
  * [18-latest][22],
  [18.0.1-18.30.11][24],
  [18.0.2-18.32.11][25],
  [18.0.2.1-18.32.13][26],
  
  * [17-latest][34],
  [17.0.0-17.28.13][36],
  [17.0.1-17.30.15][37],
  [17.0.2-17.32.13][38],
  [17.0.3-17.34.19][39],
  [17.0.4-17.36.13][40],
  [17.0.5-17.38.21][41],
  [17.0.6-17.40.19][42],
  [17.0.4.1-17.36.17][43],
  
  * [16-latest][61],
  [16.0.0-16.28.11][63],
  [16.0.1-16.30.15][64],
  [16.0.2-16.32.15][65],
  
  * [15-latest][69],
  [15.0.0-15.27.17][71],
  [15.0.1-15.28.13][72],
  [15.0.1-15.28.51][73],
  [15.0.2-15.29.15][74],
  [15.0.3-15.32.15][75],
  [15.0.4-15.34.17][76],
  [15.0.5-15.36.13][77],
  [15.0.6-15.38.17][78],
  [15.0.7-15.40.19][79],
  [15.0.8-15.42.15][80],
  [15.0.9-15.44.13][81],
  [15.0.10-15.46.17][82],
  
  * [14-latest][93],
  [14.0.1-14.28.21][94],
  [14.0.2-14.29.23][95],
  
  * [13-latest][96],
  [13.0.1-13.28][97],
  [13.0.2-13.29][98],
  [13.0.3-13.31.11][100],
  [13.0.4-13.33.25][101],
  [13.0.5-13.35.17][102],
  [13.0.6-13.37.21][103],
  [13.0.7-13.40.15][104],
  [13.0.8-13.42.17][105],
  [13.0.9-13.44.13][106],
  [13.0.10-13.46.15][107],
  [13.0.11-13.48.19][108],
  [13.0.12-13.50.15][109],
  [13.0.13-13.52.15][110],
  [13.0.14-13.54.17][111],
  
  * [12-latest][137],
  [12.0.0-12.1][138],
  [12.0.1-12.2][139],
  [12.0.2-12.3][140],
  
  * [11-latest][141],
  [11.0.1-11.2][142],
  [11.0.2-11.29][143],
  [11.0.3-11.31][144],
  [11.0.4-11.33][145],
  [11.0.5-11.35][146],
  [11.0.6-11.37][147],
  [11.0.7-11.39.15][149],
  [11.0.8-11.41.23][150],
  [11.0.9-11.43.21][151],
  [11.0.10-11.45.27][152],
  [11.0.11-11.48.21][153],
  [11.0.12-11.50.19][154],
  [11.0.13-11.52.13][155],
  [11.0.14-11.54.23][156],
  [11.0.15-11.56.19][157],
  [11.0.16-11.58.15][158],
  [11.0.17-11.60.19][159],
  [11.0.18-11.62.17][160],
  [11.0.14.1-11.54.25][165],
  [11.0.16.1-11.58.23][166],
  
  * [8-latest][197],
  [8u131-8.21.0.1][199],
  [8u144-8.23.0.3][200],
  [8u152-8.25.0.1][201],
  [8u162-8.27.0.7][202],
  [8u172-8.30.0.1][203],
  [8u181-8.31.0.1][204],
  [8u192-8.33.0.1][205],
  [8u202-8.36.0.3][206],
  [8u212-8.38.0.13][207],
  [8u222-8.40.0.25][208],
  [8u232-8.42.0.21][209],
  [8u232-8.42.0.23][210],
  [8u242-8.44.0.11][211],
  [8u252-8.46.0.19][212],
  [8u262-8.48.0.51][213],
  [8u272-8.50.0.21][214],
  [8u275-8.50.0.51][215],
  [8u282-8.52.0.23][216],
  [8u292-8.54.0.21][217],
  [8u302-8.56.0.21][218],
  [8u312-8.58.0.13][219],
  [8u322-8.60.0.21][220],
  [8u332-8.62.0.19][221],
  [8u342-8.64.0.15][222],
  [8u345-8.64.0.19][223],
  [8u352-8.66.0.15][224],
  [8u362-8.68.0.19][225],
  [8u362-8.68.0.21][226],
  
  * [7-latest][264],
  [7u141-7.18.0.3][265],
  [7u154-7.20.0.3][266],
  [7u161-7.21.0.3][267],
  [7u171-7.22.0.3][268],
  [7u181-7.23.0.1][269],
  [7u191-7.24.0.1][270],
  [7u201-7.25.0.5][271],
  [7u211-7.27.0.1][272],
  [7u222-7.29.0.5][273],
  [7u232-7.31.0.5][274],
  [7u242-7.34.0.5][275],
  [7u252-7.36.0.5][276],
  [7u262-7.38.0.11][277],
  [7u272-7.40.0.15][278],
  [7u282-7.42.0.13][279],
  [7u285-7.42.0.51][280],
  [7u292-7.44.0.11][281],
  [7u302-7.46.0.11][282],
  [7u312-7.48.0.11][283],
  [7u332-7.52.0.11][284],
  [7u342-7.54.0.13][285],
  [7u352-7.56.0.11][286],
  
  * [6-latest][287],
  [6u93-6.16.0.1][288],
  [6u97-6.17.0.1][289],
  [6u99-6.18.0.3][290],
  [6u103-6.19.0.1][291],
  [6u107-6.20.0.1][292],
  [6u113-6.21.0.3][293],
  [6u119-6.22.0.3][294],
  

**Note**: Some of these may use glibc and predate the move to musl libc.

  [1]: https://www.azul.com/products/core/
  [2]: https://docs.azul.com/core/
  [3]: https://hub.docker.com/r/azul/zulu-openjdk-alpine


  [18]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19-jre-headless-latest/Dockerfile
  [19]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.0-19.28.81-jre-headless/Dockerfile
  [20]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.1-19.30.11-jre-headless/Dockerfile
  [21]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.2-19.32.13-jre-headless/Dockerfile
  
  [30]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18-jre-headless-latest/Dockerfile
  [31]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.1-18.30.11-jre-headless/Dockerfile
  [32]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2-18.32.11-jre-headless/Dockerfile
  [33]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2.1-18.32.13-jre-headless/Dockerfile
  
  [52]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17-jre-headless-latest/Dockerfile
  [53]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.0-17.28.13-jre-headless/Dockerfile
  [54]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.1-17.30.15-jre-headless/Dockerfile
  [55]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.2-17.32.13-jre-headless/Dockerfile
  [56]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.3-17.34.19-jre-headless/Dockerfile
  [57]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4-17.36.13-jre-headless/Dockerfile
  [58]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.5-17.38.21-jre-headless/Dockerfile
  [59]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.6-17.40.19-jre-headless/Dockerfile
  [60]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4.1-17.36.17-jre-headless/Dockerfile
  
  [88]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15-jre-headless-latest/Dockerfile
  [89]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.7-15.40.19-jre-headless/Dockerfile
  [90]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.8-15.42.15-jre-headless/Dockerfile
  [91]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.9-15.44.13-jre-headless/Dockerfile
  [92]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.10-15.46.17-jre-headless/Dockerfile
  
  [124]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13-jre-headless-latest/Dockerfile
  [125]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.3-13.31.11-jre-headless/Dockerfile
  [126]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.4-13.33.25-jre-headless/Dockerfile
  [127]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.5-13.35.17-jre-headless/Dockerfile
  [128]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.6-13.37.21-jre-headless/Dockerfile
  [129]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.7-13.40.15-jre-headless/Dockerfile
  [130]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.8-13.42.17-jre-headless/Dockerfile
  [131]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.9-13.44.13-jre-headless/Dockerfile
  [132]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.10-13.46.15-jre-headless/Dockerfile
  [133]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.11-13.48.19-jre-headless/Dockerfile
  [134]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.12-13.50.15-jre-headless/Dockerfile
  [135]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.13-13.52.15-jre-headless/Dockerfile
  [136]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.14-13.54.17-jre-headless/Dockerfile
  
  [179]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11-jre-headless-latest/Dockerfile
  [182]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.5-11.35-jre-headless/Dockerfile
  [183]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.6-11.37-jre-headless/Dockerfile
  [184]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.7-11.39.15-jre-headless/Dockerfile
  [185]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.8-11.41.23-jre-headless/Dockerfile
  [186]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.9-11.43.21-jre-headless/Dockerfile
  [187]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.10-11.45.27-jre-headless/Dockerfile
  [188]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.12-11.50.19-jre-headless/Dockerfile
  [189]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.13-11.52.13-jre-headless/Dockerfile
  [190]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14-11.54.23-jre-headless/Dockerfile
  [191]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.15-11.56.19-jre-headless/Dockerfile
  [192]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16-11.58.15-jre-headless/Dockerfile
  [193]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.17-11.60.19-jre-headless/Dockerfile
  [194]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.18-11.62.17-jre-headless/Dockerfile
  [195]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14.1-11.54.25-jre-headless/Dockerfile
  [196]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16.1-11.58.23-jre-headless/Dockerfile
  
  [247]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8-jre-headless-latest/Dockerfile
  [248]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u232-8.42.0.23-jre-headless/Dockerfile
  [249]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u242-8.44.0.11-jre-headless/Dockerfile
  [250]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u252-8.46.0.19-jre-headless/Dockerfile
  [251]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u262-8.48.0.51-jre-headless/Dockerfile
  [252]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u272-8.50.0.21-jre-headless/Dockerfile
  [253]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u275-8.50.0.51-jre-headless/Dockerfile
  [254]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u282-8.52.0.23-jre-headless/Dockerfile
  [255]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u302-8.56.0.21-jre-headless/Dockerfile
  [256]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u312-8.58.0.13-jre-headless/Dockerfile
  [257]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u322-8.60.0.21-jre-headless/Dockerfile
  [258]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u332-8.62.0.19-jre-headless/Dockerfile
  [259]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u342-8.64.0.15-jre-headless/Dockerfile
  [260]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u345-8.64.0.19-jre-headless/Dockerfile
  [261]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u352-8.66.0.15-jre-headless/Dockerfile
  [262]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.19-jre-headless/Dockerfile
  [263]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.21-jre-headless/Dockerfile
  
  [11]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19-jre-latest/Dockerfile
  [15]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.0-19.28.81-jre/Dockerfile
  [16]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.1-19.30.11-jre/Dockerfile
  [17]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.2-19.32.13-jre/Dockerfile
  
  [23]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18-jre-latest/Dockerfile
  [27]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.1-18.30.11-jre/Dockerfile
  [28]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2-18.32.11-jre/Dockerfile
  [29]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2.1-18.32.13-jre/Dockerfile
  
  [35]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17-jre-latest/Dockerfile
  [44]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.0-17.28.13-jre/Dockerfile
  [45]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.1-17.30.15-jre/Dockerfile
  [46]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.2-17.32.13-jre/Dockerfile
  [47]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.3-17.34.19-jre/Dockerfile
  [48]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4-17.36.13-jre/Dockerfile
  [49]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.5-17.38.21-jre/Dockerfile
  [50]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.6-17.40.19-jre/Dockerfile
  [51]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4.1-17.36.17-jre/Dockerfile
  
  [62]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16-jre-latest/Dockerfile
  [66]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.0-16.28.11-jre/Dockerfile
  [67]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.1-16.30.15-jre/Dockerfile
  [68]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.2-16.32.15-jre/Dockerfile
  
  [70]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15-jre-latest/Dockerfile
  [83]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.0-15.27.17-jre/Dockerfile
  [84]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.7-15.40.19-jre/Dockerfile
  [85]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.8-15.42.15-jre/Dockerfile
  [86]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.9-15.44.13-jre/Dockerfile
  [87]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.10-15.46.17-jre/Dockerfile
  
  [99]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13-jre-latest/Dockerfile
  [112]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.3-13.31.11-jre/Dockerfile
  [113]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.4-13.33.25-jre/Dockerfile
  [114]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.5-13.35.17-jre/Dockerfile
  [115]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.6-13.37.21-jre/Dockerfile
  [116]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.7-13.40.15-jre/Dockerfile
  [117]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.8-13.42.17-jre/Dockerfile
  [118]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.9-13.44.13-jre/Dockerfile
  [119]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.10-13.46.15-jre/Dockerfile
  [120]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.11-13.48.19-jre/Dockerfile
  [121]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.12-13.50.15-jre/Dockerfile
  [122]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.13-13.52.15-jre/Dockerfile
  [123]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.14-13.54.17-jre/Dockerfile
  
  [148]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11-jre-latest/Dockerfile
  [161]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.3-11.31-jre/Dockerfile
  [162]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.4-11.33-jre/Dockerfile
  [163]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.5-11.35-jre/Dockerfile
  [164]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.6-11.37-jre/Dockerfile
  [167]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.7-11.39.15-jre/Dockerfile
  [168]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.8-11.41.23-jre/Dockerfile
  [169]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.9-11.43.21-jre/Dockerfile
  [170]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.10-11.45.27-jre/Dockerfile
  [171]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.11-11.48.21-jre/Dockerfile
  [172]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.12-11.50.19-jre/Dockerfile
  [173]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.13-11.52.13-jre/Dockerfile
  [174]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14-11.54.23-jre/Dockerfile
  [175]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.15-11.56.19-jre/Dockerfile
  [176]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16-11.58.15-jre/Dockerfile
  [177]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.17-11.60.19-jre/Dockerfile
  [178]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.18-11.62.17-jre/Dockerfile
  [180]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14.1-11.54.25-jre/Dockerfile
  [181]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16.1-11.58.23-jre/Dockerfile
  
  [198]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8-jre-latest/Dockerfile
  [227]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u212-8.38.0.13-jre/Dockerfile
  [228]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u222-8.40.0.25-jre/Dockerfile
  [229]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u232-8.42.0.21-jre/Dockerfile
  [230]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u232-8.42.0.23-jre/Dockerfile
  [231]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u242-8.44.0.11-jre/Dockerfile
  [232]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u252-8.46.0.19-jre/Dockerfile
  [233]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u262-8.48.0.51-jre/Dockerfile
  [234]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u272-8.50.0.21-jre/Dockerfile
  [235]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u275-8.50.0.51-jre/Dockerfile
  [236]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u282-8.52.0.23-jre/Dockerfile
  [237]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u292-8.54.0.21-jre/Dockerfile
  [238]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u302-8.56.0.21-jre/Dockerfile
  [239]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u312-8.58.0.13-jre/Dockerfile
  [240]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u322-8.60.0.21-jre/Dockerfile
  [241]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u332-8.62.0.19-jre/Dockerfile
  [242]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u342-8.64.0.15-jre/Dockerfile
  [243]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u345-8.64.0.19-jre/Dockerfile
  [244]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u352-8.66.0.15-jre/Dockerfile
  [245]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.19-jre/Dockerfile
  [246]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.21-jre/Dockerfile
  
  [10]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19-latest/Dockerfile
  [12]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.0-19.28.81/Dockerfile
  [13]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.1-19.30.11/Dockerfile
  [14]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//19.0.2-19.32.13/Dockerfile
  
  [22]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18-latest/Dockerfile
  [24]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.1-18.30.11/Dockerfile
  [25]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2-18.32.11/Dockerfile
  [26]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//18.0.2.1-18.32.13/Dockerfile
  
  [34]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17-latest/Dockerfile
  [36]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.0-17.28.13/Dockerfile
  [37]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.1-17.30.15/Dockerfile
  [38]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.2-17.32.13/Dockerfile
  [39]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.3-17.34.19/Dockerfile
  [40]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4-17.36.13/Dockerfile
  [41]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.5-17.38.21/Dockerfile
  [42]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.6-17.40.19/Dockerfile
  [43]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//17.0.4.1-17.36.17/Dockerfile
  
  [61]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16-latest/Dockerfile
  [63]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.0-16.28.11/Dockerfile
  [64]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.1-16.30.15/Dockerfile
  [65]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//16.0.2-16.32.15/Dockerfile
  
  [69]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15-latest/Dockerfile
  [71]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.0-15.27.17/Dockerfile
  [72]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.1-15.28.13/Dockerfile
  [73]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.1-15.28.51/Dockerfile
  [74]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.2-15.29.15/Dockerfile
  [75]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.3-15.32.15/Dockerfile
  [76]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.4-15.34.17/Dockerfile
  [77]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.5-15.36.13/Dockerfile
  [78]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.6-15.38.17/Dockerfile
  [79]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.7-15.40.19/Dockerfile
  [80]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.8-15.42.15/Dockerfile
  [81]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.9-15.44.13/Dockerfile
  [82]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//15.0.10-15.46.17/Dockerfile
  
  [93]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//14-latest/Dockerfile
  [94]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//14.0.1-14.28.21/Dockerfile
  [95]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//14.0.2-14.29.23/Dockerfile
  
  [96]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13-latest/Dockerfile
  [97]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.1-13.28/Dockerfile
  [98]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.2-13.29/Dockerfile
  [100]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.3-13.31.11/Dockerfile
  [101]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.4-13.33.25/Dockerfile
  [102]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.5-13.35.17/Dockerfile
  [103]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.6-13.37.21/Dockerfile
  [104]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.7-13.40.15/Dockerfile
  [105]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.8-13.42.17/Dockerfile
  [106]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.9-13.44.13/Dockerfile
  [107]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.10-13.46.15/Dockerfile
  [108]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.11-13.48.19/Dockerfile
  [109]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.12-13.50.15/Dockerfile
  [110]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.13-13.52.15/Dockerfile
  [111]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//13.0.14-13.54.17/Dockerfile
  
  [137]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//12-latest/Dockerfile
  [138]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//12.0.0-12.1/Dockerfile
  [139]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//12.0.1-12.2/Dockerfile
  [140]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//12.0.2-12.3/Dockerfile
  
  [141]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11-latest/Dockerfile
  [142]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.1-11.2/Dockerfile
  [143]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.2-11.29/Dockerfile
  [144]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.3-11.31/Dockerfile
  [145]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.4-11.33/Dockerfile
  [146]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.5-11.35/Dockerfile
  [147]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.6-11.37/Dockerfile
  [149]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.7-11.39.15/Dockerfile
  [150]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.8-11.41.23/Dockerfile
  [151]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.9-11.43.21/Dockerfile
  [152]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.10-11.45.27/Dockerfile
  [153]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.11-11.48.21/Dockerfile
  [154]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.12-11.50.19/Dockerfile
  [155]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.13-11.52.13/Dockerfile
  [156]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14-11.54.23/Dockerfile
  [157]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.15-11.56.19/Dockerfile
  [158]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16-11.58.15/Dockerfile
  [159]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.17-11.60.19/Dockerfile
  [160]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.18-11.62.17/Dockerfile
  [165]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.14.1-11.54.25/Dockerfile
  [166]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//11.0.16.1-11.58.23/Dockerfile
  
  [197]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8-latest/Dockerfile
  [199]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u131-8.21.0.1/Dockerfile
  [200]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u144-8.23.0.3/Dockerfile
  [201]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u152-8.25.0.1/Dockerfile
  [202]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u162-8.27.0.7/Dockerfile
  [203]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u172-8.30.0.1/Dockerfile
  [204]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u181-8.31.0.1/Dockerfile
  [205]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u192-8.33.0.1/Dockerfile
  [206]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u202-8.36.0.3/Dockerfile
  [207]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u212-8.38.0.13/Dockerfile
  [208]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u222-8.40.0.25/Dockerfile
  [209]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u232-8.42.0.21/Dockerfile
  [210]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u232-8.42.0.23/Dockerfile
  [211]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u242-8.44.0.11/Dockerfile
  [212]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u252-8.46.0.19/Dockerfile
  [213]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u262-8.48.0.51/Dockerfile
  [214]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u272-8.50.0.21/Dockerfile
  [215]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u275-8.50.0.51/Dockerfile
  [216]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u282-8.52.0.23/Dockerfile
  [217]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u292-8.54.0.21/Dockerfile
  [218]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u302-8.56.0.21/Dockerfile
  [219]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u312-8.58.0.13/Dockerfile
  [220]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u322-8.60.0.21/Dockerfile
  [221]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u332-8.62.0.19/Dockerfile
  [222]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u342-8.64.0.15/Dockerfile
  [223]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u345-8.64.0.19/Dockerfile
  [224]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u352-8.66.0.15/Dockerfile
  [225]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.19/Dockerfile
  [226]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//8u362-8.68.0.21/Dockerfile
  
  [264]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7-latest/Dockerfile
  [265]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u141-7.18.0.3/Dockerfile
  [266]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u154-7.20.0.3/Dockerfile
  [267]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u161-7.21.0.3/Dockerfile
  [268]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u171-7.22.0.3/Dockerfile
  [269]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u181-7.23.0.1/Dockerfile
  [270]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u191-7.24.0.1/Dockerfile
  [271]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u201-7.25.0.5/Dockerfile
  [272]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u211-7.27.0.1/Dockerfile
  [273]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u222-7.29.0.5/Dockerfile
  [274]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u232-7.31.0.5/Dockerfile
  [275]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u242-7.34.0.5/Dockerfile
  [276]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u252-7.36.0.5/Dockerfile
  [277]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u262-7.38.0.11/Dockerfile
  [278]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u272-7.40.0.15/Dockerfile
  [279]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u282-7.42.0.13/Dockerfile
  [280]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u285-7.42.0.51/Dockerfile
  [281]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u292-7.44.0.11/Dockerfile
  [282]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u302-7.46.0.11/Dockerfile
  [283]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u312-7.48.0.11/Dockerfile
  [284]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u332-7.52.0.11/Dockerfile
  [285]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u342-7.54.0.13/Dockerfile
  [286]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//7u352-7.56.0.11/Dockerfile
  
  [287]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6-latest/Dockerfile
  [288]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u93-6.16.0.1/Dockerfile
  [289]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u97-6.17.0.1/Dockerfile
  [290]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u99-6.18.0.3/Dockerfile
  [291]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u103-6.19.0.1/Dockerfile
  [292]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u107-6.20.0.1/Dockerfile
  [293]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u113-6.21.0.3/Dockerfile
  [294]: https://github.com/zulu-openjdk/zulu-openjdk/blob/master/alpine//6u119-6.22.0.3/Dockerfile
  