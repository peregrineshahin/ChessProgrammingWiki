---
title: Mater
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mater**



[ [Astrolabe](https://en.wikipedia.org/wiki/Astrolabe), [Mater](https://en.wikipedia.org/wiki/Astrolabe#Construction) and [Tympan](https://en.wikipedia.org/wiki/Tympan) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Mater**,  

a chess [mating](Checkmate "Checkmate") [combinations](Combination "Combination") program, developed in the mid 60s by [George Baylor](George_Baylor "George Baylor") and [Herbert Simon](Herbert_Simon "Herbert Simon"), which was subject of Baylor's Masters thesis at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It was an early pioneering attempt in finding forced checkmates, employing "[Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence")" rather than "[Brute-Force](Brute-Force "Brute-Force")" <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Only [moves](Moves "Moves") which either put the enemy king in [check](Check "Check") (**Mater I**), or [threaten](Threat_Move "Threat Move") [mate in one](Mate_at_a_Glance "Mate at a Glance") (**Mater II**) were [generated](Move_Generation "Move Generation") for the attacking side, [searching](Mate_Search "Mate Search") those moves first which leave the minimum number of defensive replies, to eventually reduce the defender's [mobility](Mobility "Mobility") to zero. 


  




## History


The original mating combination program, as conceived by Herbert Simon and his son Peter Simon in 1962 <a id="cite-note-5" href="#cite-ref-5">[5]</a>, was a hand simulation setting forth a strategy of search. It discovered mating combinations in 52 of the 129 positions collected in [Fine's](https://en.wikipedia.org/wiki/Reuben_Fine) chapter of the mating attack from *The Middlegame in Chess*. [Newell's](Allen_Newell "Allen Newell") and Prasad's [IPL](https://en.wikipedia.org/wiki/Information_Processing_Language) program <a id="cite-note-6" href="#cite-ref-6">[6]</a>, which could set up a [chessboard](Board_Representation "Board Representation"), recorded positions, generated and [made moves](Make_Move "Make Move") and testing their [legality](index.php?title=Legal_Mov&action=edit&redlink=1 "Legal Mov (page does not exist)"), was base of **Mater I** and in 1964 the revised **Mater II** programs. According to [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), Mater was ported to [Fortran](Fortran "Fortran") and incorporated into [Cooper-Kozdrowicki](Coko "Coko") program by [Dennis Cooper](Dennis_Cooper "Dennis Cooper") and [Ed Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki") <a id="cite-note-7" href="#cite-ref-7">[7]</a>:




```C++
MATER is written by George Baylor and Simon in FORTRAN. It is able to search to great depths for checkmates. MATER is presently part of the Cooper-Kozdrowicki program. While MATER is an interesting program in its own right, the opportunity to checkmate one's opponent plays a relatively small computational part of the game of chess, and its inclusion in the Cooper-Kozdrowicki program does not seem to add measurably to the program's strength. 

```

## Mater I




|  |  |  |  |
| --- | --- | --- | --- |
| 

|  |
| --- |
|                                                                         ♜ ♝♚  ♞♜♟  ♟ ♟♘♟♞  ♗     ♟ ♘♙  ♙      ♙    ♙ ♕  ♙ ♙ ♔   ♛     ♝  |

 |  |  Only check giving moves were generated in **Mater I** for the attacking side and check evasions for the defending side, for each [ply](Ply "Ply") level put into a [try-list](Move_List "Move List"). For the attacker, the list is ordered by the fewest-reply heuristic, highest priority goes to moves with the fewest number of legal replies, while checking moves with more than **four** legal replies are pruned entirely. Ties are broken by giving priority to [double checks](Double_Check "Double Check") and then to checks with no [capturing](Captures "Captures") replies. Search only continues down a particular path so long as the opponent's mobility is on the decline, which implies a maximum [search depth](Depth "Depth") of 9 [plies](Ply "Ply"). The defender's side considers captures in [MVV/LVA](MVV-LVA "MVV-LVA") order first, followed by king moves and interpositions. In *A chess mating combinations program*, the [beta-cutoff](Beta-Cutoff "Beta-Cutoff") was mentioned as "killing reply" <a id="cite-note-8" href="#cite-ref-8">[8]</a>, also with a footnote <a id="cite-note-9" href="#cite-ref-9">[9]</a> on [McCarthy.'s](John_McCarthy "John McCarthy") [killer heuristic](Killer_Heuristic "Killer Heuristic") referring [Alan Kotok's](Alan_Kotok "Alan Kotok") 1962 paper <a id="cite-note-10" href="#cite-ref-10">[10]</a>, covering [alpha-beta](Alpha-Beta "Alpha-Beta"). [Reuben Fine's](https://en.wikipedia.org/wiki/Reuben_Fine) position from *The Middlegame in Chess* served as one example of Mater's ability <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a>.
 |






## Mater II




|  |  |  |  |
| --- | --- | --- | --- |
| 

|  |
| --- |
|                                                                            ♜ ♝  ♛♜♚♟♟   ♟ ♟    ♟♙♟♕                     ♘  ♙    ♙♙♙   ♖  ♔♖ |

 |  |  At its first level of search, **Mater II** also generates moves threatening mate in one. After generation and trying checking moves without success, but triggered after collecting useful informations of "nearly" mate with only one legal reply, Mater II considers none checking moves which put additional pressure to the enemy king's sector, that is moves which directly or indirectly ([x-ray](X-ray "X-ray")) attack squares around the king. In this respect it resembles what [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") has called a "sample variation" <a id="cite-note-13" href="#cite-ref-13">[13]</a>, a kind of trial balloon sent up for the express purpose of gathering information to direct subsequent investigations. A further condition to finally add the move into the try-list is that after the move is internally made followed by a defender's [null move](Null_Move "Null Move"), the resulting position is mate in one. Now, the defender's [move ordering](Move_Ordering "Move Ordering") heuristic needs to prefer moves that defend the mating square. Fine's diagram 97 <a id="cite-note-14" href="#cite-ref-14">[14]</a> was given as example of the abilities of Mater II.
 |


## Board Representation


Mater was written in [IPL V](https://en.wikipedia.org/wiki/Information_Processing_Language) with its primary data structure of a [list](Linked_List "Linked List"), and kept lists with a header (name) and [attribute-value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair) for each [square](Squares "Squares") and [piece](Pieces "Pieces") to [represent the board](Board_Representation "Board Representation"), where values for piece and square attributes are addresses (cells) of lists again, yielding in an extensive network of relations among squares and pieces:





|  Name
 |  Attribut
 |  Value
 |
| --- | --- | --- |
|  H1
 |  Man on square
 |  M8
 |
|  North
 |  H2
 |
|  West
 |  G1
 |
|  WNW
 |  F2
 |
|  NW
 |  G2
 |
|  NNW
 |  G3
 |
|  ...
 |  ...
 |  ...
 |
|  M8
 |  Man on what square
 |  H1
 |
|  Type of man
 |  Rook
 |
|  Color of man
 |  White
 |
|  Move directions
 |  list of directions
 |
|  Capture directions
 |  list of directions
 |
|  ...
 |  ...
 |  ...
 |


## Move Generation


In *A chess mating combinations program*, Baylor and Simon further elaborate on [move generation](Move_Generation "Move Generation"), with two tacks, corresponding to a **one-many** or **many-one** approach. In trying to find all checking moves, one could either radiate out from the enemy king, and for each [square](Squares "Squares"), search for a [piece](Pieces "Pieces") that can get there and [check](Check "Check") (one-many), or converge from the squares along the [move directions](Direction#MoveDirections "Direction") of each attacking piece onto the enemy king's square (many-one). If there are many pieces on the board, the former tends to be more effective, if few, the latter.



## Processing Speed


Mater was written in an [interpretive language](https://en.wikipedia.org/wiki/Interpreted_language) IPL, without any attempts to provide a special [machine-language](https://en.wikipedia.org/wiki/Machine_code) representation for primitive board manipulation. The most difficult mates, requiring the examination of about 100 positions, were achieved in about 3 minutes on an [IBM 7090](IBM_7090 "IBM 7090") <a id="cite-note-15" href="#cite-ref-15">[15]</a>.



## Namesake


* [Mater](index.php?title=Mater_(Albillo)&action=edit&redlink=1 "Mater (Albillo) (page does not exist)") by [Valentin Albillo](index.php?title=Valentin_Albillo&action=edit&redlink=1 "Valentin Albillo (page does not exist)") <a id="cite-note-16" href="#cite-ref-16">[16]</a>


## See also


* [Chest](Chest "Chest")
* [MAPP](MAPP "MAPP")
* [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
* [Mate-in-two](Mate-in-two "Mate-in-two")
* [Mate Search](Mate_Search "Mate Search")
* [NSS](NSS "NSS")
* [Perceiver](Perceiver "Perceiver")


## Publications


* [Herbert A. Simon](Herbert_Simon "Herbert Simon"), [Peter A. Simon](http://www.cs.cmu.edu/simon/kfrank.html) (**1962**). *[Trial and Error Search in Solving Difficult Problems: Evidence from the Game of Chess](http://psycnet.apa.org/index.cfm?fa=search.displayRecord&UID=1963-06169-001)*. Behavioral Science, Vol. 7, No. 4, pp. 425-429
* [George W. Baylor](George_Baylor "George Baylor") (**1965**). *[Report on a Mating Combinations Program](http://www.dtic.mil/docs/citations/AD0619018)*. SDC Paper, No. SP-2150, System Development Corporation, Santa Monica, Calif.
* [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference), reprinted in [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1979**). *[Models of Thought](http://yalepress.yale.edu/yupbooks/book.asp?isbn=9780300024326)*. [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press), pp. 181-200, in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*.
* [George W. Baylor](George_Baylor "George Baylor") (**1966**). *A Computer Model of Checkmating Behaviour in Chess*. in [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot"), [Walter R. Reitman](Walter_R._Reitman "Walter R. Reitman") (eds.) (**1966**). *Heuristic Processes in Thinking*. International Congress of Psychology, [Nauka](https://en.wikipedia.org/wiki/Nauka_%28publisher%29), [Moscow](https://en.wikipedia.org/wiki/Moscow)
* [Herbert Simon](Herbert_Simon "Herbert Simon") (**1973**). *Lessons from Perception for Chess-Playing Programs (and Vice Versa)*. Computer Science Research Review 1972-73, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=33779)
* [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**) *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
* [Max Bramer](Max_Bramer "Max Bramer") (**1982**). *Finding Checkmates*. [Computer & Video Games](https://en.wikipedia.org/wiki/Computer_and_Video_Games), [Spring 1982](http://www.chesscomputeruk.com/html/publication_archive_1982.html), [pdf](http://www.chesscomputeruk.com/Computer___Video_Games_Spring_1982.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")


## External Links


* [mater - Wiktionary](https://en.wiktionary.org/wiki/mater)
* [Mater (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Mater)
* [Alma mater from Wikipedia](https://en.wikipedia.org/wiki/Alma_mater)
* [Alma mater (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Alma_mater_%28disambiguation%29)
* [Stabat Mater from Wikipedia](https://en.wikipedia.org/wiki/Stabat_Mater)
* [Stata Mater from Wikipedia](https://en.wikipedia.org/wiki/Stata_Mater)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> One of four extant brass [astrolabes](https://en.wikipedia.org/wiki/Astrolabe) manufactured by the workshop of [Georg Hartmann](https://en.wikipedia.org/wiki/Georg_Hartmann) in [Nuremberg](https://en.wikipedia.org/wiki/Nuremberg) in 1537. This one part of the Scientific Instruments Collection of [Yale University's](https://en.wikipedia.org/wiki/Yale_University) [Peabody Museum of Natural History](https://en.wikipedia.org/wiki/Peabody_Museum_of_Natural_History), [Yale's Hartmann astrolabe.jpg - Wikimedia Commons](http://commons.wikimedia.org/wiki/File:Yale%27s_Hartmann_astrolabe.jpg)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [George Baylor](George_Baylor "George Baylor") in [All Remembrance of Herbert A. Simon](http://www.cs.cmu.edu/simon/all.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Max Bramer](Max_Bramer "Max Bramer") (**1982**). *Finding Checkmates*. [Computer & Video Games](https://en.wikipedia.org/wiki/Computer_and_Video_Games), [Spring 1982](http://www.chesscomputeruk.com/html/publication_archive_1982.html), [pdf](http://www.chesscomputeruk.com/Computer___Video_Games_Spring_1982.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Herbert A. Simon](Herbert_Simon "Herbert Simon"), [Peter A. Simon](http://www.cs.cmu.edu/simon/kfrank.html) (**1962**). *[Trial and Error Search in Solving Difficult Problems: Evidence from the Game of Chess](http://psycnet.apa.org/index.cfm?fa=search.displayRecord&UID=1963-06169-001)*. Behavioral Science, Vol. 7, No. 4, pp. 425-429
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Allen Newell](Allen_Newell "Allen Newell"), N. S. Prasad (**1963**). *IPL-V Chess Position Program*. Internal Memo No. 63, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. Academic Press, New York, N.Y. p. 26
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> "this ([Move ordering](Move_Ordering "Move Ordering")) is an attempt to clip unnecessary proliferations in the move tree: if there is a "killing" reply to a checking move, further analysis of that checking move would seem futile" from **4.** *The Executive and Heuristics of Search* in [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> "This is the [minimax](Minimax "Minimax") assumption: namely that the opponent will make his strongest reply at every opportunity. [McCarthy.'s](John_McCarthy "John McCarthy") *[killer heuristic](Killer_Heuristic "Killer Heuristic")* (see [Kotok](Alan_Kotok "Alan Kotok"), [1962](Alan_Kotok#1962 "Alan Kotok")) assumes that a killing reply to one checking move may be a killing reply to other checking moves and thus should be looked at first" from **4.** *The Executive and Heuristics of Search* in [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Alan Kotok](Alan_Kotok "Alan Kotok") (**1962**). *[Artificial Intelligence Project - MIT Computation Center: Memo 41 - A Chess Playing Program](http://www.kotok.org/AI_Memo_41.html)*. [pdf](ftp://publications.ai.mit.edu/ai-publications/pdf/AIM-041.pdf)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Reuben Fine](https://en.wikipedia.org/wiki/Reuben_Fine) (**1952**). *The Middlegame in Chess*. McKay
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> r1bk2nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1 w - - 0 1 ; Fine 1952, [chess/BWTC.PGN at master · wspeirs/chess · GitHub](https://github.com/wspeirs/chess/blob/master/src/test/resources/mate/BWTC.PGN)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a>  [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1946**). *Het denken van den Schaker, een experimenteel-psychologische studie.* Ph.D. thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam), advisor [Géza Révész](Mathematician#Revesz "Mathematician"); N.V. Noord-Hollandse Uitgevers Maatschappij, [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam). Translated with the help of [George Baylor](George_Baylor "George Baylor"), with additions, (in **1965**) as *Thought and Choice in Chess*. Mouton Publishers, The Hague. ISBN 90-279-7914-6.
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> r1b2qrk/pp3p1p/4pPpQ/8/8/5N2/P4PPP/3R2KR w - - 0 1 ; Fine 1952, [chess/BWTC.PGN at master · wspeirs/chess · GitHub](https://github.com/wspeirs/chess/blob/master/src/test/resources/mate/BWTC.PGN)
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference) - Processing Speed
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [MATER === A simple Mate Searching Program](https://www.stmintz.com/ccc/index.php?id=151785) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), January 24, 2001

**[Up one Level](Engines "Engines")**







 
