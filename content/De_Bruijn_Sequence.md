---
title: De Bruijn Sequence
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * De Bruijn Sequence**

In [combinatorial mathematics](https://en.wikipedia.org/wiki/Combinatorics), a **k**-ary **De Bruijn Sequence** B(k, n) of order **n**, named after the Dutch mathematician [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn"), is a cyclic sequence of a given alphabet **A** with size **k** for which every possible subsequence of length **n** in **A** appears as a sequence of consecutive characters exactly once <a id="cite-note-1" href="#cite-ref-1">[1]</a>. In chess programming there are applications of de Bruijn sequences with the Binary alphabet, in [hashing](Hash_Table "Hash Table") sets like [Piece-Sets](Piece-Sets "Piece-Sets") or Square-sets, also called [Bitboards](Bitboards "Bitboards"), most notably in [Bit scanning](BitScan#DeBruijnMultiplation "BitScan") <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

## Binary alphabet

According to De Bruijn himself <a id="cite-note-3" href="#cite-ref-3">[3]</a> , the existence of De Bruijn sequences were first proved, for the case of alphabets with two elements, by **Camille Flye Sainte-Marie** in 1894, whereas the generalization to larger alphabets is originally due to [Tanja van Ardenne-Ehrenfest](Mathematician#Ehrenfest "Mathematician") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and himself.

Binary digits or [bits](Bit "Bit") inside a computer word are B(2, n) de Bruijn sequences, with **2n** bits length and equal number of ones and zeros, with **2n** overlapping unique **n**-bit subsequences. Since the sequences are cyclic and **n-1** subsequences need to wrap, we restrict them to at least **n-1** leading zeros, to make them overlap the hidden trailing "zeros".

Odd sequences have **n** leading zeros. The even ones with **n-1** leading zeros are rotated (shifted) left by one. Due to **n** leading zeros of these odd sequences we further consider, the first subsequence\[**0**\] is zero. Due to the overlapping, each subsequence\[**i**+1\] is dependent from subsequence\[**i**\]. The doubled value incremented by either zero or one. Since subsequence\[**0**\] is zero, a second zero subsequence with six consecutive binary zeros is further prohibited, and subsequence\[**1**\] must be one. Subsequence index **i** is counted from most significant bit left to right, and therefor reversed from usual bit-index. A modulo **2n** restricts all subsequences to **n** bits:

```C++s[i+1] = (2s[i] + (0|1)) mod (2n)

```

The [Cardinality](https://en.wikipedia.org/wiki/Cardinality) of all distinct B(2, n) de Bruijn sequences is:

```C++|B(2, n)| = 2(2n-1 - n)

```

|  n
|  2n-1 - n
| B(2, n)|
|
| --- | --- | --- |
|  1
|  0
|  1
|
|  2
|  0
|  1
|
|  3
|  1
|  2
|
|  4
|  4
|  16
|
|  5
|  11
|  2,048
|
|  6
|  26
|  67,108,864
|
|  7
|  57
|  144,115,188,075,855,872
|
|  8
|  120
|  ~1.329e+36
|

## B(2, 1)

```C++The two one-bit subsequences obviously do not overlap:

```

```C++
i  01  s[i]
0  0    0
1   1   1

```

## B(2, 2)

B(2, 2) implies 22 or 4-bit sequences. There is one odd four-bit de Bruijn sequence with four overlapping unique two-bit subsequences, 0x3.

```C++
i  0011|0  s[i]
0  00 . . . 0
1   01      1
2  . 11 . . 3
3     1|0   2

```

## B(2, 3)

B(2, 3) implies 23 or 8-bit sequences. There are two odd eight-bit sequences with eight overlapping unique three-bit subsequences, 0x17 and 0x1d. Note that the five relevant bits are reversed.

```C++
i  00010111|00 s[i]    i  00011101|00 s[i]
0  000 . . . .  0      0  000 . . . .  0
1   001         1      1   001         1
2  . 010 . . .  2      2  . 011 . . .  3
3     101       5      3     111       7
4  . . 011 . .  3      4  . . 110 . .  6
5       111     7      5       101     5
6  . . . 11|0   6      6  . . . 01|0   2
7         1|00  4      7         1|00  4

```

## B(2, 4)

B(2, 4) implies 24 or 16 bit sequences. There are 16 odd 16-bit sequences with 16 overlapping unique four-bit subsequences:

```C++
0x09af  0000100110101111
0x09eb  0000100111101011
0x0a6f  0000101001101111
0x0a7b  0000101001111011
0x0b3d  0000101100111101
0x0b4f  0000101101001111
0x0bcd  0000101111001101
0x0bd3  0000101111010011
0x0cbd  0000110010111101
0x0d2f  0000110100101111
0x0d79  0000110101111001
0x0de5  0000110111100101
0x0f2d  0000111100101101
0x0f4b  0000111101001011
0x0f59  0000111101011001
0x0f65  0000111101100101

```

for instance 0x0d2f:

```C++
i  0000110100101111|000 s[i]
 0  0000 . . . . . . . .  0
 1   0001                 1
 2  . 0011 . . . . . . .  3
 3     0110               6
 4  . . 1101 . . . . . . 13
 5       1010            10
 6  . . . 0100 . . . . .  4
 7         1001           9
 8  . . . . 0010 . . . .  2
 9           0101         5
10  . . . . . 1011 . . . 11
11             0111       7
12  . . . . . . 1111 . . 15
13               111|0   14
14  . . . . . . . 11|00  12
15                 1|000  8

```

## B(2, 5)

B(2, 5) implies 25 or 32 bit sequences. There are 2^11 or 2,048 odd 32-bit sequences with 32 overlapping unique five-bit subsequences, for instance 0x076be629

```C++
 i  00000111011010111110011000101001|0000 s[i]
 0  00000 . . . . . . . . . . . . . . . .  0
 1   00001                                 1
 2  . 00011 . . . . . . . . . . . . . . .  3
 3     00111                               7
 4  . . 01110 . . . . . . . . . . . . . . 14
 5       11101                            29
 6  . . . 11011 . . . . . . . . . . . . . 27
 7         10110                          22
 8  . . . . 01101 . . . . . . . . . . . . 13
 9           11010                        26
10  . . . . . 10101 . . . . . . . . . . . 21
11             01011                      11
12  . . . . . . 10111 . . . . . . . . . . 23
13               01111                    15
14  . . . . . . . 11111 . . . . . . . . . 31
15                 11110                  30
16  . . . . . . . . 11100 . . . . . . . . 28
17                   11001                25
18  . . . . . . . . . 10011 . . . . . . . 19
19                     00110               6
20  . . . . . . . . . . 01100 . . . . . . 12
21                       11000            24
22  . . . . . . . . . . . 10001 . . . . . 17
23                         00010           2
24  . . . . . . . . . . . . 00101 . . . .  5
25                           01010        10
26  . . . . . . . . . . . . . 10100 . . . 20
27                             01001       9
28  . . . . . . . . . . . . . . 1001|0. . 18
29                               001|00    4
30  . . . . . . . . . . . . . . . 01|000   8
31                                 1|0000 16

```

## B(2, 6)

B(2, 6) implies 26 or 64 bit sequences. There are 2^26 or 67,108,864 odd 64-bit sequences with 64 overlapping unique six-bit subsequences, for instance 0x022fdd63cc95386d

```C++
 i  0000001000101111110111010110001111001100100101010011100001101101|00000 s[i]
 0  000000 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  0
 1   000001                                                                 1
 2  . 000010 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
 3     000100                                                               4
 4  . . 001000 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
 5       010001                                                            17
 6  . . . 100010 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
 7         000101                                                           5
 8  . . . . 001011 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
 9           010111                                                        23
10  . . . . . 101111 . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
11             011111                                                      31
12  . . . . . . 111111 . . . . . . . . . . . . . . . . . . . . . . . . . . 63
13               111110                                                    62
14  . . . . . . . 111101 . . . . . . . . . . . . . . . . . . . . . . . . . 61
15                 111011                                                  59
16  . . . . . . . . 110111 . . . . . . . . . . . . . . . . . . . . . . . . 55
17                   101110                                                46
18  . . . . . . . . . 011101 . . . . . . . . . . . . . . . . . . . . . . . 29
19                     111010                                              58
20  . . . . . . . . . . 110101 . . . . . . . . . . . . . . . . . . . . . . 53
21                       101011                                            43
22  . . . . . . . . . . . 010110 . . . . . . . . . . . . . . . . . . . . . 22
23                         101100                                          44
24  . . . . . . . . . . . . 011000 . . . . . . . . . . . . . . . . . . . . 24
25                           110001                                        49
26  . . . . . . . . . . . . . 100011 . . . . . . . . . . . . . . . . . . . 35
27                             000111                                       7
28  . . . . . . . . . . . . . . 001111 . . . . . . . . . . . . . . . . . . 15
29                               011110                                    30
30  . . . . . . . . . . . . . . . 111100 . . . . . . . . . . . . . . . . . 60
31                                 111001                                  57
32  . . . . . . . . . . . . . . . . 110011 . . . . . . . . . . . . . . . . 51
33                                   100110                                38
34  . . . . . . . . . . . . . . . . . 001100 . . . . . . . . . . . . . . . 12
35                                     011001                              25
36  . . . . . . . . . . . . . . . . . . 110010 . . . . . . . . . . . . . . 50
37                                       100100                            36
38  . . . . . . . . . . . . . . . . . . . 001001 . . . . . . . . . . . . .  9
39                                         010010                          18
40  . . . . . . . . . . . . . . . . . . . . 100101 . . . . . . . . . . . . 37
41                                           001010                        10
42  . . . . . . . . . . . . . . . . . . . . . 010101 . . . . . . . . . . . 21
43                                             101010                      42
44  . . . . . . . . . . . . . . . . . . . . . . 010100 . . . . . . . . . . 20
45                                               101001                    41
46  . . . . . . . . . . . . . . . . . . . . . . . 010011 . . . . . . . . . 19
47                                                 100111                  39
48  . . . . . . . . . . . . . . . . . . . . . . . . 001110 . . . . . . . . 14
49                                                   011100                28
50  . . . . . . . . . . . . . . . . . . . . . . . . . 111000 . . . . . . . 56
51                                                     110000              48
52  . . . . . . . . . . . . . . . . . . . . . . . . . . 100001 . . . . . . 33
53                                                       000011             3
54  . . . . . . . . . . . . . . . . . . . . . . . . . . . 000110 . . . . .  6
55                                                         001101          13
56  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 011011 . . . . 27
57                                                           110110        54
58  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101101 . . . 45
59                                                             01101|0     26
60  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1101|00  . 52
61                                                               101|000   40
62  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 01|0000  16
63                                                                 1|00000 32

```

## De Bruijn Graphs

A De Bruijn graph is a directed graph representing overlaps between sequences of symbols <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

- Each vertex has exactly m incoming and m outgoing edges
- Each n-dimensional de Bruijn graph is the [line digraph](https://en.wikipedia.org/wiki/Line_graph) of the (n-1)-dimensional de Bruijn graph
- Each de Bruijn graph is [Eulerian](https://en.wikipedia.org/wiki/Euler_cycle) and [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_graph). The Euler cycles and Hamiltonian cycles of these graphs are de Bruijn sequences.

\[
The graph construction of the three smallest binary de Bruijn graphs

## B(2, 4) Graph

\[
A De Bruijn graph. Every four-digit sequence occurs exactly once if one
traverses every edge exactly once and returns to one's starting point.

## De Bruijn Graph on a Chess Board

A directed De Bruijn Graph of B(2, 6) sequences with [Little-Endian Rank-File Mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") board coordinates (a1 = 0, b1 = 1, h8 = 63). For topology reasons, almost each node (except a1 and h8) of the graph is deconcentrated and appears twice in the form of two reversed binary trees. The leaf outputs join the respective reversed tree. Between c6 and f3 is a direct cycle, since 42 is 2\*21 and 21 is (2\*42 + 1) % 64, with both six-bit pattern reversed - 010101 (21) versus 101010 (42). The challenge is to traverse the graph in any way to visit each of the 64 nodes aka squares exactly once.

```C++
+----------------->---------------a1--------------<-----------------+
|                                 |                                 |
|                                 b1                                |
|                 +--------------/  \-------------+                 |
|                c1                               d1                |
^         +-----/  \-----+                 +-----/  \-----+         |
|        e1              f1               g1              h1        |
|     +-/  \-+        +-/  \-+         +-/  \-+        +-/  \-+     |
|    a2      b2      c2      d2       e2      f2      g2      h2    |
|  a3  b3  c3  d3  e3 |f3| g3  h3   a4  b4  c4  d4  e4  f4  g4  h4  |
+-a5b5c5d5e5f5g5h5a6b6c6d6e6f6g6h6 a7b7c7d7e7f7g7h7a8b8c8d8e8f8  |  |
     ^ ^ ^ ^ ^ ^ ^ ^ ^   ^ ^ ^ ^ ^  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  |  |
                                                                 |  |
+----------------->---------------h8--------------<--------------+  ^
|                                  |                                |
|                                 g8                                |
|                 +--------------/  \-------------+                 |
|                f8                               e8                |
^         +-----/  \-----+                 +-----/  \-----+         |
|        d8              c8               b8              a8        |
|     +-/  \-+        +-/  \-+         +-/  \-+        +-/  \-+     |
|    h7      g7      f7      e7       d7      c7      b7      a7    |
|  h6  g6  f6  e6  d6 |c6| b6  a6   h5  g5  f5  e5  d5  c5  b5  a5--+
+-h4g4f4e4d4c4b4a4h3g3f3e3d3c3b3a3 h2g2f2e2d2c2b2a2h1g1f1e1d1c1
     ^ ^ ^ ^ ^ ^ ^ ^ ^   ^ ^ ^ ^ ^  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

```

## De Bruijn Networks

So called De Bruijn Networks with the topology of De Bruijn Graphs have interesting properties in processor and computer networks, for instance as described by [Feldmann et al.](Rainer_Feldmann "Rainer Feldmann") to connect [Transputer](Transputer "Transputer") networks <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> .

## See also

- [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn")
- [De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") from [BitScan](BitScan "BitScan")
- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Prouhet–Thue–Morse Sequence](Max_Euwe#ProuhetThueMorseSequence "Max Euwe")
- [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")

## Selected Publications

## 1894

- Camille Flye Sainte-Marie (**1894**). *Solution to question nr. 48*, L'Intermédiaire des Mathématiciens 1, reproduced in [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn") (**1975**). *Acknowledgement of priority to C. Flye Sainte-Marie on the counting of circular arrangements of 2n zeros and ones that show each n-letter word exactly once*. Technical Report, Technische Hogeschool Eindhoven, [pdf](http://alexandria.tue.nl/repository/books/252901.pdf)

## 1946

- [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn") (**1946**). *A Combinatorial Problem*. Koninklijke Nederlandse Akademie v. Wetenschappen 49: 758–764.
- [Jack Good](Jack_Good "Jack Good") (**1946**). *[Normal Recurring Decimals](http://jlms.oxfordjournals.org/cgi/content/citation/s1-21/3/167)*. [Journal of the London Mathematical Society](http://www.lms.ac.uk/publications/jlms) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## 1950 ...

- [Lester Randolph Ford, Jr.](Mathematician#LRFord "Mathematician") (**1957**). *A Cyclic Arrangement of M-Tuples*. Report No. P-1071. [Rand Corporation](https://en.wikipedia.org/wiki/RAND_Corporation)
- [Solomon W. Golomb](Mathematician#SMGolomb "Mathematician") (**1967, 1982**). *[Shift Register Sequences](https://catalog.hathitrust.org/Record/000466600)*. Holden-Day Inc., revised 2nd edition, [Aegean Park Press](https://en.wikipedia.org/wiki/Aegean_Park_Press)
- [Harold M. Fredricksen](Mathematician#HMFredricksen "Mathematician") (**1968**). *Disjoint Cycles from the de Bruijn Graph*. Ph.D. thesis, [University of Southern California](University_of_Southern_California "University of Southern California"), advisor [Solomon Wolf Golomb](Mathematician#SMGolomb "Mathematician")

## 1970 ...

- [Harold M. Fredricksen](Mathematician#HMFredricksen "Mathematician") (**1970**). *The lexicographically least de Bruijn cycle*. [Journal of Combinatorial Theory](https://en.wikipedia.org/wiki/Journal_of_Combinatorial_Theory), Vol. 9, No. 1
- [Abraham Lempel](Mathematician#ALempel "Mathematician") (**1970**). *On a Homomorphism of the De Bruijn Graph and Its Applications to the Design of Feedback Shift Registers*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. 19, No. 12
- [Harold M. Fredricksen](Mathematician#HMFredricksen "Mathematician") (**1972**). *Generation of the Ford Sequence of Length 2n, n Large.* JPL Technical Report 32-1526, Vol. IV, [pdf](http://tmo.jpl.nasa.gov/progress_report2/IV/IVM.PDF)

## 1990 ...

- [Yuejiang Huang](http://dblp.uni-trier.de/pers/hd/h/Huang:Yuejiang) (**1990**). *[A new algorithm for the generation of binary de Bruijn sequences](http://www.sciencedirect.com/science/article/pii/019667749090028D)*. [Journal of Algorithms, Vol. 11, No. 1](<ftp://ftp.math.utah.edu/pub/tex/bib/toc/jalg.html#11(1):March:1990>)
- [Chris J. Mitchell](Mathematician#CJMitchell "Mathematician"), [Tuvi Etzion](Mathematician#TEtzion "Mathematician"), [Kenneth G. Paterson](Mathematician#KGPaterson "Mathematician") (**1996**). *A method for constructing decodable de Bruijn Sequences*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=B603C5EDF04C7DF00B0D604AB96E3226?doi=10.1.1.14.674&rep=rep1&type=pdf) via [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.14.674)
- [Fred S. Annexstein](http://www.ece.uc.edu/~annexste/UC_Pages/Dr._Fred_Annexsteins_Computer_Science_Department_Homepage_____.html) (**1997**). *Generating De Bruijn Sequences: An Efficient Implementation.* [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. 46, No. 2, [pdf](http://www.ece.uc.edu/~annexste/Papers/Annexstein-GeneratingDB.pdf), [Supplement: C-code implementation](http://www.ece.uc.edu/~annexste/Papers/fastdb.c)
- [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*. [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf)

## 2000 ...

- [Vladimir Raphael Rosenfeld](http://research.haifa.ac.il/%7Eevolut/) (**2002**). *Enumerating De Bruijn Sequences*. [Institute of Evolution](http://evolution.haifa.ac.il/), [University of Haifa](https://en.wikipedia.org/wiki/University_of_Haifa), [pdf](http://www.stefangeens.com/br13.pdf)
- [Vladimir Raphael Rosenfeld](http://research.haifa.ac.il/%7Eevolut/) (**2002**). *Enumerating Kautz Sequences*. [Institute of Evolution](http://evolution.haifa.ac.il/), [University of Haifa](https://en.wikipedia.org/wiki/University_of_Haifa), [pdf](http://elib.mi.sanu.ac.rs/files/journals/kjm/24/d003download.pdf)
- [Anwitaman Datta](Mathematician#ADatta "Mathematician"), [Sarunas Girdzijauskas](Mathematician#SGirdzijauskas "Mathematician"), [Karl Aberer](Mathematician#KAberer "Mathematician") (**2004**). *On de Bruijn routing in distributed hash tables: There and back again*. P2P2004, The 4th IEEE International Conference on Peer-to-Peer Computing, [pdf](http://www.ida.liu.se/conferences/p2p/p2p2004/papers/datta.pdf)
- [Pierre Fraigniaud](Mathematician#PFraigniaud "Mathematician"), [Philippe Gauron](Mathematician#PGauron "Mathematician") (**2005**). *D2B: a de Bruijn Based Content-Addressable Network*. [pdf](http://www.liafa.jussieu.fr/%7Epierref/POSTSCRIPTS/D2B.pdf)
- [Drew Armstrong](http://www.math.umn.edu/%7Earmstron/) (**2006**). *De Bruijn Sequences*. [pdf](http://www.math.umn.edu/%7Earmstron/5707/DeBruijn.pdf)
- [Jean Berstel](Mathematician#JBerstel "Mathematician"), [Dominique Perrin](Mathematician#DPerrin "Mathematician") (**2007**). *The origins of combinatorics on words*. [European Journal of Combinatorics 28](http://www.informatik.uni-trier.de/~ley/db/journals/ejc/ejc28.html), [pdf](http://www-igm.univ-mlv.fr/~berstel/Articles/2007Origins.pdf)

## 2010 ...

- [Yaw-Ling Lin](http://www.cs.pu.edu.tw/~yawlin/), [Charles B. Ward](https://sites.google.com/site/charlesbward/), [Bharat Jain](http://dblp.uni-trier.de/pers/hd/j/Jain:Bharat), [Steven Skiena](Steven_Skiena "Steven Skiena") (**2011**). *[Constructing Orthogonal de Bruijn Sequences](http://link.springer.com/chapter/10.1007%2F978-3-642-22300-6_50)*. [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 6844, [WADS 2011](http://dblp.uni-trier.de/db/conf/wads/wads2011.html#LinWJS11)
- [Zuling Chang](https://www.researchgate.net/profile/Zuling_Chang), [Martianus Frederic Ezerman](Mathematician#MFEzerman "Mathematician"), [San Ling](Mathematician#SanLing "Mathematician"), [Huaxiong Wang](Mathematician#HuaxiongWang "Mathematician") (**2016**). *On Binary de Bruijn Sequences from LFSRs with Arbitrary Characteristic Polynomials*. [arXiv:1611.10088](https://arxiv.org/abs/1611.10088) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Zuling Chang](https://www.researchgate.net/profile/Zuling_Chang), [Martianus Frederic Ezerman](Mathematician#MFEzerman "Mathematician"), [Adamas Aqsa Fahreza](https://www.linkedin.com/in/adamas-aqsa-fahreza-08927995/), [San Ling](Mathematician#SanLing "Mathematician"), [Huaxiong Wang](Mathematician#HuaxiongWang "Mathematician") (**2017**). *Large Order Binary de Bruijn Sequences via Zech's Logarithms*. [arXiv:1705.03150](https://arxiv.org/abs/1705.03150) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Joe Sawada](Mathematician#JSawada "Mathematician"), [Aaron Williams](Mathematician#AWilliams "Mathematician") (**2017**). *[Practical Algorithms to Rank Necklaces, Lyndon Words, and de Bruijn Sequences](https://dl.acm.org/citation.cfm?id=3085499)*. [Journal of Discrete Algorithms](https://www.journals.elsevier.com/journal-of-discrete-algorithms/), Vol. 43, No. C, [pdf](http://www.socs.uoguelph.ca/~sawada/papers/ranking.pdf)

## External Links

- [De Bruijn sequence from Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn_sequence)
- [De Bruijn graph from Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn_graph)
- [Kautz graph from Wikipedia](https://en.wikipedia.org/wiki/Kautz_graph)
- [Koorde from Wikipedia](https://en.wikipedia.org/wiki/Koorde)
- [A166315 - OEIS](https://oeis.org/A166315)
- [Lyndon word from Wikipedia](https://en.wikipedia.org/wiki/Lyndon_word)
- [If](Category:If "Category:If") - [Forgotten Roads](https://en.wikipedia.org/wiki/If_3), [Beat-Club](https://en.wikipedia.org/wiki/Beat-Club) [#71](https://www.youtube.com/watch?v=V1BcLk19hVw), September 25, 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [De Bruijn sequence from Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn_sequence)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*. [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn") (**1975**). *Acknowledgement of priority to C. Flye Sainte-Marie on the counting of circular arrangements of 2n zeros and ones that show each n-letter word exactly once*. Technical Report, Technische Hogeschool Eindhoven, [pdf](http://alexandria.tue.nl/repository/books/252901.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn") (**1985**). *In Memoriam T. van Ardenne-Ehrenfest*. [pdf](http://alexandria.tue.nl/repository/freearticles/597575.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [De Bruijn graph from Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn_graph)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems* Phd-Thesis, [pdf](http://wwwcs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Recurring decimal from Wikipedia](https://en.wikipedia.org/wiki/Recurring_decimal)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [LFSR from Wikipedia](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Zech's logarithm from Wikipedia](https://en.wikipedia.org/wiki/Zech%27s_logarithm)

**[Up one Level](Data "Data")**

