---
title: Influence Quantity of Pieces
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Pieces](Pieces "Pieces") \* Influence Quantity**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bd0) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Intruder <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
The **influence quantity** of pieces is defined by their number of unique [moves](Moves "Moves") with respect to their [from](Origin_Square "Origin Square")- and [to-square](Target_Square "Target Square") coordinates, the [cardinality](https://en.wikipedia.org/wiki/Cardinality) of the set of all possible moves, or [potential, global](Mobility#TheValueofReachingaSquare "Mobility") [mobility](Mobility "Mobility") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It might be used to enumerate and [encode](Encoding_Moves "Encoding Moves") all those moves, i.e. associating each move, per piece and in total, with a unique number for [minimal perfect hashing](Hash_Table#MinimalPerfectHashing "Hash Table") opposed to intermittent [Butterfly boards](Butterfly_Boards "Butterfly Boards").


For instance a [pawn](Pawn "Pawn") (including [promotions](Promotions "Promotions")) has 48 (8\*6) single pushes and 84 (2\*7\*6) [captures](Captures "Captures"), plus 8 possible double pushes on each [file](Files "Files"), which results in a influence quantity of 140 of either white or black pawns.The influence quantities of all pieces are divisible by four times seven (28), excluding pawn and [king](King "King") even by sixteen times seven (112). While obviously the number of [queen](Queen "Queen") quantities is the sum of [rook](Rook "Rook")- and [bishop](Bishop "Bishop") quantities, it is at the first glance somehow surprising that the rook quantity is the sum of bishop- and [knight](Knight "Knight") quantities. 



### Whole Board Diagrams


Whole board tables cover pawn, knight, king and sliding pieces, and their [file](Files "Files")-, [rank](Ranks "Ranks") and total sums:




```C++
White pawn total                      white pawn a2                         white pawn d2
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |     |   |   |   |   |   |   |   |   |     |   |   |   |   |   |   |   |   |
| 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22  | 2 | 3 | 3 | 3 | 3 | 3 |   |   | 17  | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22
| 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22  | 2 | 3 | 3 | 3 | 3 |   |   |   | 14  | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22
| 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22  | 2 | 3 | 3 | 3 |   |   |   |   | 11  | 2 | 3 | 3 | 3 | 3 | 3 | 3 |   | 20
| 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22  | 2 | 3 | 3 |   |   |   |   |   |  8  |   | 3 | 3 | 3 | 3 | 3 |   |   | 15
| 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 22  | 2 | 3 |   |   |   |   |   |   |  5  |   |   | 3 | 3 | 3 |   |   |   |  9
| 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 30  | 3 |   |   |   |   |   |   |   |  3  |   |   |   | 4 |   |   |   |   |  4
|   |   |   |   |   |   |   |   |     |   |   |   |   |   |   |   |   |     |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+
 13  19  19  19  19  19  19  13  140   13  15  12   9   6   3           58    6  12  15  19  15  12   9   4   92

Knight                                                                      King
+---+---+---+---+---+---+---+---+                                           +---+---+---+---+---+---+---+---+
| 2 | 3 | 4 | 4 | 4 | 4 | 3 | 2 | 26                                        | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 36
| 3 | 4 | 6 | 6 | 6 | 6 | 4 | 3 | 38                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 4 | 6 | 8 | 8 | 8 | 8 | 6 | 4 | 52                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 4 | 6 | 8 | 8 | 8 | 8 | 6 | 4 | 52                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 4 | 6 | 8 | 8 | 8 | 8 | 6 | 4 | 52                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 4 | 6 | 8 | 8 | 8 | 8 | 6 | 4 | 52                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 3 | 4 | 6 | 6 | 6 | 6 | 4 | 3 | 38                                        | 5 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 58
| 2 | 3 | 4 | 4 | 4 | 4 | 3 | 2 | 26                                        | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 36
+---+---+---+---+---+---+---+---+                                           +---+---+---+---+---+---+---+---+
 26  38  52  52  52  52  38  26  336                                         36  58  58  58  58  58  58  36  420

Bishop                                Rook                                  Queen
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+
| 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 56  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |21 |21 |21 |21 |21 |21 |21 |168
| 7 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 68  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |23 |23 |23 |23 |23 |21 |180
| 7 | 9 |11 |11 |11 |11 | 9 | 7 | 76  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |25 |25 |25 |25 |23 |21 |188
| 7 | 9 |11 |13 |13 |11 | 9 | 7 | 80  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |25 |27 |27 |25 |23 |21 |192
| 7 | 9 |11 |13 |13 |11 | 9 | 7 | 80  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |25 |27 |27 |25 |23 |21 |192
| 7 | 9 |11 |11 |11 |11 | 9 | 7 | 76  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |25 |25 |25 |25 |23 |21 |188
| 7 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 68  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |23 |23 |23 |23 |23 |23 |21 |180
| 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 56  |14 |14 |14 |14 |14 |14 |14 |14 |112  |21 |21 |21 |21 |21 |21 |21 |21 |168
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+
 56  68  76  80  80  76  68  56  560  112 112 112 112 112 112 112 112  896  168 180 188 192 192 188 180 168 1456

```

### Board Circles


The [concentric](https://en.wikipedia.org/wiki/Concentric) "circles" around the [center](Center "Center") with their respective influence sums of sliding pieces:




```C++
Bishop Circles                        Rook Circles                          Queen Circles
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+
|              196              |     |              392              |     |              588              |
+   +---+---+---+---+---+---+   +     +   +---+---+---+---+---+---+   +     +   +---+---+---+---+---+---+   +
|   |          180          |   |     |   |          280          |   |     |   |          460          |   |
+   +   +---+---+---+---+   +   +     +   +   +---+---+---+---+   +   +     +   +   +---+---+---+---+   +   +
|   |   |      132      |   |   |     |   |   |      168      |   |   |     |   |   |      300      |   |   |
+   +   +   +---+---+   +   +   +     +   +   +   +---+---+   +   +   +     +   +   +   +---+---+   +   +   +
|   |   |   |   52  |   |   |   |     |   |   |   |   56  |   |   |   |     |   |   |   |  108  |   |   |   |
+   +   +   +       +   +   +   +     +   +   +   +       +   +   +   +     +   +   +   +       +   +   +   +
|   |   |   | 4*13  |   |   |   |     |   |   |   | 4*14  |   |   |   |     |   |   |   | 4*27  |   |   |   |
+   +   +   +---+---+   +   +   +     +   +   +   +---+---+   +   +   +     +   +   +   +---+---+   +   +   +
|   |   |    12*11      |   |   |     |   |   |    12*14      |   |   |     |   |   |    12*25      |   |   |
+   +   +---+---+---+---+   +   +     +   +   +---+---+---+---+   +   +     +   +   +---+---+---+---+   +   +
|   |        20* 9          |   |     |   |        20*14          |   |     |   |        20*23          |   |
+   +---+---+---+---+---+---+   +     +   +---+---+---+---+---+---+   +     +   +---+---+---+---+---+---+   +
|            28* 7              |     |            28*14              |     |            28*21              |
+---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+

```





## Quantities and Point Values


The mentioned move quantities of pawns and pieces only roughly correlate with their [point values](Point_Value "Point Value") since the static enumeration of all moves with distinct coordinates does not take into account the reachability of all origin-squares. Only queen and rook can reach any square in at least two moves on the otherwise empty board. Bishop quantities cover all light and dark colored from-squares. While a single bishop is bounded to one square color, its individual influence quantity is therefor divided by two. Also, pawns can only move forward and can not reach each enumerated origin square, which decreases their individual influence accordantly. King and knights can reach every square on the otherwise empty board, but may take more time with respect to [distance](Distance "Distance") and [knight-distance](Knight-Distance "Knight-Distance").



## Divisibility by Seven


All influence quantities are divisible by four times seven, thanks to the double pushes. For a rook it is quite obvious, since each of the 64 from squares covers one rank and file each with seven squares left.





|  Piece
 |  #
 |  div 4
 |  div 7
 |  div 28
 |
| --- | --- | --- | --- | --- |
|  Pawn
 |  140
 |  35
 |  20
 |  5
 |
|  Knight
 |  336
 |  84
 |  48
 |  12
 |
|  King
 |  420
 |  105
 |  60
 |  15
 |
|  Bishops
 |  560
 |  140
 |  80
 |  20
 |
|  Bishop
 |  280
 |  70
 |  40
 |  10
 |
|  Rook
 |  896
 |  224
 |  128
 |  32
 |
|  Queen
 |  1456
 |  364
 |  208
 |  52
 |
|  N
 |  1792
 |  448
 |  256
 |  64
 |






## Fibonacci Spiral


If we only consider pieces with disjoint moves (excluding pawns and king), and the queen as superset of bishop and rook, the influence quantities are even divisible by seven times sixteen, where the remaining quotients from knight to queen are [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) as shown by the Fibonacci spiral <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> .





|  |  |
| --- | --- |
| [Chessfibspirale.jpg](http://www.127jupiter.com/) | [Yupana 1.png](File:Yupana_1.png) |
|  Fibonacci spiral <a id="cite-note-5" href="#cite-ref-5">[5]</a> | [Yupana](https://en.wikipedia.org/wiki/Yupana), counting tool of the [Incas](https://en.wikipedia.org/wiki/Incas) |




|  Piece
 |  covers other pieces
 |  #
 |  ÷ (7x16)
 |
| --- | --- | --- | --- |
| Knight
 |  -
 |  336
 |  3
 |
|  Bishop
 |  queen, king and pawn captures
 |  560
 |  5
 |
| Rook
 |  queen, king and pawn pushes
 |  896
 |  8
 |
|  possible queen move coordinates
 |  1456
 |  13
 |
|  possible from-to move coordinates
 |  1792
 |  16
 |


## Analogy in Astronomy


In his [esoteric](https://en.wikipedia.org/wiki/Esotericism) and [pseudo scientific](https://en.wikipedia.org/wiki/Pseudoscience) touched *Encyclopedia of Chess-Prehistory*, Peter Orantek <a id="cite-note-6" href="#cite-ref-6">[6]</a> mentions a possible connection to [astronomy](https://en.wikipedia.org/wiki/Astronomy), related to the [orbital period](https://en.wikipedia.org/wiki/Orbital_period) of [Earth](https://en.wikipedia.org/wiki/Earth) and [Venus](https://en.wikipedia.org/wiki/Venus). The influence quantity of a queen is equivalent to about 4 years (4 x 364 days), while the influence quantity of a rook is equivalent to 224 days x 4 Venus rotations.





|  |  |  |
| --- | --- | --- |
| [FullMoon2010.jpg](https://en.wikipedia.org/wiki/Moon) | [Venus-real color.jpg](https://en.wikipedia.org/wiki/Venus) | [The Earth seen from Apollo 17.jpg](https://en.wikipedia.org/wiki/Earth) |
| [Moon](https://en.wikipedia.org/wiki/Moon) | [Venus](https://en.wikipedia.org/wiki/Venus) 224
 | [Earth](https://en.wikipedia.org/wiki/Earth) 364
 |


In his German text sample <a id="cite-note-7" href="#cite-ref-7">[7]</a> , Orantek further elaborates that queen quantities of the four [center squares](Center "Center") (four times 27) represent four [earth moon](https://en.wikipedia.org/wiki/Moon) rotations, while the three concentric rings around the center might related to various [synodic periods](https://en.wikipedia.org/wiki/Orbital_period) of the four [terrestrial planets](https://en.wikipedia.org/wiki/Terrestrial_planet). He associates following [prime numbers](https://en.wikipedia.org/wiki/Prime_number) with [planets](https://en.wikipedia.org/wiki/Planet) or objects orbiting the [Sun](https://en.wikipedia.org/wiki/Sun) <a id="cite-note-8" href="#cite-ref-8">[8]</a> :





|  Primenumber
 |  Piece
 |  Engine
 |  Planetor Objects
 |  Symbol
 |  Orbital periodin days
 |  Synodic periodin days
 |
| --- | --- | --- | --- | --- | --- | --- |
| [3](https://en.wikipedia.org/wiki/3_%28number%29) | [Knight](Knight "Knight") | [Black Knight](Black_Knight "Black Knight")[White Knight](White_Knight "White Knight") | [Mercury](https://en.wikipedia.org/wiki/Mercury_%28planet%29) | [Mercury symbol.svg](File:Mercury_symbol.svg) |  87.9691
 |  115.88
 |
| [5](https://en.wikipedia.org/wiki/5_%28number%29) | [Bishop](Bishop "Bishop") | [BlackBishop](BlackBishop "BlackBishop")[The Crazy Bishop](The_Crazy_Bishop "The Crazy Bishop") | [Venus](https://en.wikipedia.org/wiki/Venus) | [Venus symbol.svg](File:Venus_symbol.svg) | **224.70069** |  583.92
(579–589) 
 |
| [13](https://en.wikipedia.org/wiki/13_%28number%29) | [Queen](Queen "Queen") | [Queen](Queen_(engine) "Queen (engine)")[Terra](Terra "Terra") | [Earth](https://en.wikipedia.org/wiki/Earth) | [Earth symbol.svg](File:Earth_symbol.svg) | **365.256366** |  |
| [61](https://en.wikipedia.org/wiki/61_%28number%29) |  |  | [Mars](https://en.wikipedia.org/wiki/Mars) | [Mars symbol.svg](File:Mars_symbol.svg) |  686.971
 |  779.96
(764–811) 
 |
| [89](https://en.wikipedia.org/wiki/89_%28number%29) |  | [Anubis](Anubis "Anubis") | [Asteroids](https://en.wikipedia.org/wiki/Asteroid) |  |  |  |
| [127](https://en.wikipedia.org/wiki/127_%28number%29) |  | [Jupiter](Jupiter "Jupiter") | [Jupiter](https://en.wikipedia.org/wiki/Jupiter) | [Jupiter symbol.svg](File:Jupiter_symbol.svg) |  4,331.572
 |  398.88
 |
| [167](https://en.wikipedia.org/wiki/167_%28number%29) |  |  | [Charon](https://en.wikipedia.org/wiki/Charon_%28moon%29) |  |  |  |
| [181](https://en.wikipedia.org/wiki/181_%28number%29) |  |  | [Saturn](https://en.wikipedia.org/wiki/Saturn) | [Saturn symbol.svg](File:Saturn_symbol.svg) |  10,759.220
 |  378.09
 |
|  307
 |  | [Chiron](Chiron "Chiron") | [Chiron](https://en.wikipedia.org/wiki/2060_Chiron) | [Chiron symbol.svg](File:Chiron_symbol.svg) |  18,539.000
 |  |
|  487
 |  |  | [Uranus](https://en.wikipedia.org/wiki/Uranus) | [Uranus symbol.svg](File:Uranus_symbol.svg) |  30,799.095
 |  369.66
 |
|  499
 |  |  | [Pholus](https://en.wikipedia.org/wiki/5145_Pholus) |  |  33,547.410
 |  |
|  547
 |  | [Neptune](Neptune "Neptune") | [Neptune](https://en.wikipedia.org/wiki/Neptune) | [Neptune symbol.svg](File:Neptune_symbol.svg) |  60,190.000
 |  367.49
 |
|  761
 |  |  | [Pluto](https://en.wikipedia.org/wiki/Pluto) | [Pluto symbol.svg](File:Pluto_symbol.svg) |  90,613.305
 |  366.73
 |
|  1307
 |  |  | [Transpluto](https://en.wikipedia.org/wiki/Planets_beyond_Neptune#Planet_X) |  |  |  |


## See also


* [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
* [Dumb7Fill](Dumb7Fill "Dumb7Fill")
* [Encoding Moves](Encoding_Moves "Encoding Moves")


 [Move Enumeration](Encoding_Moves#Enumeration "Encoding Moves")
* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
* [Material](Material "Material")
* [Mobility](Mobility "Mobility")
* [Point Value](Point_Value "Point Value")
* [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")


## Publications


* H. M. Taylor (**1876**). *[On the Relative Values of the Pieces in Chess](http://www.tandfonline.com/doi/abs/10.1080/14786447608639029#.UfEUGXePZlR)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Series 5, Vol. 1, pp. 221-229
* [H. S. M. Coxeter](Mathematician#Coxeter "Mathematician") (**1940**). *Mathematical Recreations and Essays*. from the [original](http://www.gutenberg.org/ebooks/26839) by [W. W. Rouse Ball](Mathematician#WWRouseBall "Mathematician"), [Macmillan](https://en.wikipedia.org/wiki/Macmillan_Publishers)
* [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
* [Dan Heisman](Dan_Heisman "Dan Heisman") (**1990, 1999, 2010**). *[Elements of Positional Evaluation](https://www.danheisman.com/elements-of-positional-evaluation.html)*. Russell Enterprises
* Peter Orantek (**2008**). *[Encyclopedia of Chess-Prehistory - Programming Language Chess](http://www.127jupiter.com/)*.


## Forum Posts


* [Value of the pieces](https://groups.google.com/d/msg/rec.games.chess/efBhsZU3J1g/fC7rxV5yuycJ) by Joost de Heer, [rgc](Computer_Chess_Forums "Computer Chess Forums"), February 01, 1995
* [Material/Mobility](http://www.open-chess.org/viewtopic.php?f=5&t=171) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 17, 2010


## External Links


* [7 from Wikipedia](https://en.wikipedia.org/wiki/7_%28number%29)
* [Seven-day week from Wikipedia](https://en.wikipedia.org/wiki/Seven-day_week)
* [If](Category:If "Category:If") - [Fibonacci's Number](https://en.wikipedia.org/wiki/If_3) (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") and [The Mothers of Invention](https://en.wikipedia.org/wiki/The_Mothers_of_Invention), [Inca Roads](https://en.wikipedia.org/wiki/Inca_Roads_(song)), 1974, ([A Token of His Extreme](https://en.wikipedia.org/wiki/A_Token_of_His_Extreme_(Soundtrack))), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>


 [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa"), [George Duke](Category:George_Duke "Category:George Duke"), [Napoleon Murphy Brock](https://en.wikipedia.org/wiki/Napoleon_Murphy_Brock), [Chester Thompson](Category:Chester_Thompson "Category:Chester Thompson"), [Tom Fowler](https://en.wikipedia.org/wiki/Tom_Fowler_%28musician%29), [Ruth Underwood](https://en.wikipedia.org/wiki/Ruth_Underwood), [Captain Beefheart](https://en.wikipedia.org/wiki/Captain_Beefheart)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bd0) [Center for Holocaust & Genocide Studies](http://chgs.elevator.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Dan Heisman](Dan_Heisman "Dan Heisman") (**1990, 1999, 2010**). *[Elements of Positional Evaluation](https://www.danheisman.com/elements-of-positional-evaluation.html)*. Russell Enterprises
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [The Fibonacci Series - The Series - Fibonacci Spiral In Action](http://library.thinkquest.org/27890/theSeries6a.html)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> The [relative piece values](Point_Value#TheoreticalAttempt "Point Value") for {N, B, R, Q} of {3, 5, 8, 15} were mentioned by H. M. Taylor (**1876**). *[On the Relative Values of the Pieces in Chess](http://www.tandfonline.com/doi/abs/10.1080/14786447608639029#.UfEUGXePZlR)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Series 5, Vol. 1, pp. 221-229 as reported in [H. S. M. Coxeter](Mathematician#Coxeter "Mathematician") (**1940**). *Mathematical Recreations and Essays*. pp. 162-165, from the [original](http://www.gutenberg.org/ebooks/26839) by [W. W. Rouse Ball](Mathematician#WWRouseBall "Mathematician"), [Macmillan](https://en.wikipedia.org/wiki/Macmillan_Publishers), as reported by [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Peter Orantek: Encyclopedia of Chess-Prehistory](http://www.127jupiter.com/)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Peter Orantek: Encyclopedia of Chess-Prehistory - Programming Language Chess](http://www.127jupiter.com/Honors.pdf)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Peter 0rantek: Encyclopedia of Chess-Prehistory - Decoded prehistorical books of Chess](http://www.127jupiter.com/Example.pdf) (pdf text sample)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Peter 0rantek: Encyclopedia of Chess-Prehistory - Decoded prehistorical books of Chess - Contents](http://www.127jupiter.com/Contents.pdf) (pdf)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Clay animation](https://en.wikipedia.org/wiki/Clay_animation) by [Bruce Bickford](https://en.wikipedia.org/wiki/Bruce_Bickford_(animator))
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Kelly Fisher Lowe](http://adeucefortheskycap.blogspot.com/2007/10/eulogy-for-kelly-lowe-by-michael-king.html) (**2006**). *[The Words and Music of Frank Zappa](http://www.afka.net/Books/lowe.htm)*. Praeger Publishers, pp. 119 *The lyrics to "Inca Roads" are absurdist in the extreme. They veer wildly from spacey - "Did a vehicle / Come from somewhere out there / Just to land in the Andes?," which both [Watson](https://en.wikipedia.org/wiki/Ben_Watson_(music_writer)) and [Courrier](http://www.beefheart.com/tag/kevin-courrier/) claim Zappa's satire on the popular-at-the-time book [Chariots of the Gods?](https://en.wikipedia.org/wiki/Chariots_of_the_Gods%3F)* ...
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Nazca Lines from Wikipedia](https://en.wikipedia.org/wiki/Nazca_lines)

**[Up one Level](Pieces "Pieces")**







 
