# topsis-priyajot-102003293
Topsis stands for 'Technique for Order of Preference by Similarity to Ideal Solution'.
TopsisPy is a Python Package implementing [Topsis](https://en.wikipedia.org/wiki/TOPSIS) method used for multi-criteria decision analysis.

## Installation
Install the Package using the command - 
```s
$ pip install topsis-priyajot-102003293
```


## Example

Attempt|Fund Name|    P1  |  P2 |  P3 |   P4  |   P5|
0        M1  0.84  0.71  6.7  42.1  12.59
1        M2  0.91  0.83  7.0  31.7  10.11
2        M3  0.79  0.62  4.8  46.7  13.23
3        M4  0.78  0.61  6.4  42.4  12.55
4        M5  0.94  0.88  3.6  62.2  16.91
5        M6  0.88  0.77  6.5  51.5  14.91
6        M7  0.66  0.44  5.3  48.9  13.83
7        M8  0.93  0.86  3.4  37.0  10.55

Output saved to Final.csv

   Fund Name    P1    P2   P3    P4     P5  Performance Score  Rank
0        M1  0.84  0.71  6.7  42.1  12.59           0.644719     2
1        M2  0.91  0.83  7.0  31.7  10.11           0.680361     1
2        M3  0.79  0.62  4.8  46.7  13.23           0.443785     7
3        M4  0.78  0.61  6.4  42.4  12.55           0.563500     4
4        M5  0.94  0.88  3.6  62.2  16.91           0.489617     6
5        M6  0.88  0.77  6.5  51.5  14.91           0.639262     3
6        M7  0.66  0.44  5.3  48.9  13.83           0.376340     8
7        M8  0.93  0.86  3.4  37.0  10.55           0.514142     5

### License

MIT

### This repository is licensed under the MIT license. See LICENSE for details.
