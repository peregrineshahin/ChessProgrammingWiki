---
title: Sjaak Glebbeek
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sjaak**


**Sjaak**, <a id="cite-note-1" href="#cite-ref-1">[1]</a>  

an [open source engine](Category:Open_Source "Category:Open Source") under the [GNU General Public Licence](Free_Software_Foundation#GPL "Free Software Foundation") by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek") as younger sibling of [Jazz](Jazz "Jazz") written in [C](C "C"), but able to play [chess variants](Chess#Variants "Chess") on various [board](Chessboard "Chessboard") sizes compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). 
Sjaak was first released in January 2011, not to confused with [Ronald de Man's](Ronald_de_Man "Ronald de Man") older private engine with the same name <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



## Variants


* [Amazon Chess](index.php?title=Amazon_Chess&action=edit&redlink=1 "Amazon Chess (page does not exist)"), where the queen moves as an amazon (needs to be played as variant "fairy" in XBoard).
* [Berolina Chess](index.php?title=Berolina_Chess&action=edit&redlink=1 "Berolina Chess (page does not exist)"), where pawns move one square diagonal and capture straight ahead.
* [Burmese Chess](index.php?title=Burmese_Chess&action=edit&redlink=1 "Burmese Chess (page does not exist)"), working but not tested fully.
* [Capablanca Chess](index.php?title=Capablanca_Chess&action=edit&redlink=1 "Capablanca Chess (page does not exist)"), a variant played on a 10x8 board with two extra pieces.
* [Capablanca Random Chess](index.php?title=Capablanca_Random_Chess&action=edit&redlink=1 "Capablanca Random Chess (page does not exist)")
* [Chess960](Chess960 "Chess960") (Fischer Random Chess)
* [Chinese Chess](Chinese_Chess "Chinese Chess")
* [Courier Chess](index.php?title=Courier_Chess&action=edit&redlink=1 "Courier Chess (page does not exist)"), a medieval variant played on a 12x8 board.
* [Crazyhouse](Crazyhouse "Crazyhouse")
* [Gothic Chess](index.php?title=Gothic_Chess&action=edit&redlink=1 "Gothic Chess (page does not exist)"), the same as Capablanca Chess but with a different starting position.
* [Grand Chess](index.php?title=Grand_Chess&action=edit&redlink=1 "Grand Chess (page does not exist)"), on a 10x10 board.


 [Indian Grand Chess](index.php?title=Indian_Grand_Chess&action=edit&redlink=1 "Indian Grand Chess (page does not exist)"), or possibly Turkish Grand Chess. On a 10x10 with four extra pieces.
* [Knightmate](Knightmate_Chess "Knightmate Chess"), where the king moves as a knight and the knights move as a king.
* [Makruk](index.php?title=Makruk&action=edit&redlink=1 "Makruk (page does not exist)"), the Thai version of Chess.
* [Orthodox chess](Chess "Chess")
* [Pocket Knight](index.php?title=Pocket_Knight&action=edit&redlink=1 "Pocket Knight (page does not exist)"), like normal chess, but players have an extra knight they can drop on the board.
* [Seirawan Chess](index.php?title=Seirawan_Chess&action=edit&redlink=1 "Seirawan Chess (page does not exist)")
* [Shatranj](Shatranj "Shatranj"), a historic precursor of modern chess.
* [Shogi](Shogi "Shogi") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Spartan Chess](index.php?title=Spartan_Chess&action=edit&redlink=1 "Spartan Chess (page does not exist)"), where black and white play with different armies and black has two kings
* [The Maharaja and the Sepoys](index.php?title=The_Maharaja_and_the_Sepoys&action=edit&redlink=1 "The Maharaja and the Sepoys (page does not exist)"), where white has only one piece (the Maharaja) (needs to be played as variant "fairy" in [XBoard](XBoard "XBoard")).


## Description


### Board Representation


Despite boards exceeding 64 squares, like 10x8, 12x8, and 10x10, Sjaak is a native [bitboard](Bitboards "Bitboards") engine, utilizing either [GCC's](Free_Software_Foundation#GCC "Free Software Foundation") \_\_int128 <a id="cite-note-5" href="#cite-ref-5">[5]</a> extenstion on 64-bit platforms such as [x86-64](X86-64 "X86-64") or 128 bit vectors of integers on 32-bit platforms, the latter supporting [SSE2](SSE2 "SSE2") if available. Sjaak applies [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### Search


Sjaak uses a [fail-soft](Fail-Soft "Fail-Soft") [alpha-beta](Alpha-Beta "Alpha-Beta") [principal variation search](Principal_Variation_Search "Principal Variation Search") with [quiescence](Quiescence_Search "Quiescence Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [late move reductions](Late_Move_Reductions "Late Move Reductions") and [check extensions](Check_Extensions "Check Extensions") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. 
[Move ordering](Move_Ordering "Move Ordering") considers the [killer](Killer_Heuristic "Killer Heuristic"), [countermove](Countermove_Heuristic "Countermove Heuristic") and [history heuristics](History_Heuristic "History Heuristic"). A modified version of a [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") routine from Jazz is used to evaluate [captures](Captures "Captures") . 



### Evaluation


Sjaak's static [evaluation](Evaluation "Evaluation") takes [material balance](Material#Balance "Material"), static [piece-square tables](Piece-Square_Tables "Piece-Square Tables") derived from heuristics based on how [pieces](Pieces "Pieces") move, [mobility](Mobility "Mobility") and [king safety](King_Safety "King Safety") into account, the latter only in chess variants with one king per side <a id="cite-note-8" href="#cite-ref-8">[8]</a>.



## Namesake


* [Sjaak](Sjaak "Sjaak") (TrojanKnight) by [Ronald de Man](Ronald_de_Man "Ronald de Man")


## See also


* [Jazz](Jazz "Jazz")
* [Leonidas](index.php?title=Leonidas&action=edit&redlink=1 "Leonidas (page does not exist)")
* [Sjakk](Sjakk "Sjakk")


## Forum Posts


### 2011 ...


* [New Spartan-Chess engine: Sjaak](http://www.talkchess.com/forum/viewtopic.php?t=37713) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 20, 2011
* [Sjaak 263](http://www.talkchess.com/forum/viewtopic.php?t=40956) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 31, 2011
* [Xiangqi chase algorithm](http://www.talkchess.com/forum/viewtopic.php?t=41110) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 16, 2011 » [Chinese Chess](Chinese_Chess "Chinese Chess")
* [Sjaak 342 - new variants](http://www.talkchess.com/forum/viewtopic.php?t=41115) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 16, 2011
* [Sjaak 437](http://www.talkchess.com/forum/viewtopic.php?t=41418) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), December 11, 2011
* [Sjaak 468 JA available](http://www.talkchess.com/forum/viewtopic.php?t=42126) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), January 23, 2012
* [Sjaak updated (revision 506)](http://www.talkchess.com/forum/viewtopic.php?t=47075) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), February 01, 2013
* [Shogi](http://www.talkchess.com/forum/viewtopic.php?t=54092) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 20, 2014 » [Shogi](Shogi "Shogi")
* [Xiangqi chase - again](http://www.talkchess.com/forum/viewtopic.php?t=54258) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 06, 2014 » [Chinese Chess](Chinese_Chess "Chinese Chess")
* [Sjaak II - beta release!](http://www.talkchess.com/forum/viewtopic.php?t=54390) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 19, 2014


### 2015 ...


* [SjaakII 1.0 RC1](http://www.talkchess.com/forum/viewtopic.php?t=55140) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 29, 2015
* [SjaakII 1.0.0](http://www.talkchess.com/forum/viewtopic.php?t=55705) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 18, 2015


**2016**



* [SjaakII 1.2 RC1](http://www.talkchess.com/forum/viewtopic.php?t=58787) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 02, 2016


 [SjaakII 1.2.0 is out!](http://www.talkchess.com/forum/viewtopic.php?t=58787&start=12) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 08, 2016
 [SjaakII 1.2.1 is out!](http://www.talkchess.com/forum/viewtopic.php?t=58787&start=28) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 10, 2016
* [Sjaak II question](http://www.talkchess.com/forum/viewtopic.php?t=59531) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") [CCC](CCC "CCC"), March 16, 2016
* [SjaakII 1.3.0 (the happy easter edition)](http://www.talkchess.com/forum/viewtopic.php?t=59644) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 26, 2016
* [Question about Sjaak](http://www.talkchess.com/forum/viewtopic.php?t=59709) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), April 01, 2016
* [Sjaak II, Wa Shogi and XBoard 4.9](http://www.talkchess.com/forum/viewtopic.php?t=59955) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 25, 2016 » [Shogi](Shogi "Shogi"), [XBoard](XBoard "XBoard")
* [SjaakII 1.3.1](http://www.talkchess.com/forum/viewtopic.php?t=60696) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), July 05, 2016
* [SjaakII 1.4.0](http://www.talkchess.com/forum/viewtopic.php?t=62283) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), November 27, 2016
* [Sjaak II 1.4.1 and Shogi](http://www.talkchess.com/forum/viewtopic.php?t=62484) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 14, 2016 » [Shogi](Shogi "Shogi")


**2017**



* [I hate this hobby...](http://www.talkchess.com/forum/viewtopic.php?t=62878) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 20, 2017 » [Shogi](Shogi "Shogi")


## External Links


### Chess Engine


* [Chess (Jazz & Sjaak) home](http://www.eglebbk.dds.nl/program/chess-index.html)
* [Chess (Jazz & Sjaak) downloads](http://www.eglebbk.dds.nl/program/chess-download.html)
* [Sjaak](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Sjaak&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Sjaak from Wikipedia](https://en.wikipedia.org/wiki/Sjaak)
* [Willem Breuker](Category:Willem_Breuker "Category:Willem Breuker"), [Pierre Courbois](Category:Pierre_Courbois "Category:Pierre Courbois"), [Victor Kaihatu](http://www.jazzpodiumdetor.nl/victor-kaihatu/) - Wonderful Girl of 17 Springs (1966), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Sjaak](https://en.wikipedia.org/wiki/Sjaak) - Dutch [given name](Category:Given_Name "Category:Given Name") derived from [Jacob](https://en.wikipedia.org/wiki/Jacob_%28name%29), pronunciation similar to [Schaak](http://nl.wikipedia.org/wiki/Schaak)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: New Spartan-Chess engine: Sjaak](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=389447&t=37713) by [Vladimir Xern](index.php?title=Vladimir_Xern&action=edit&redlink=1 "Vladimir Xern (page does not exist)"), [CCC](CCC "CCC"), January 21, 2011
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [SjaakII 1.0.0](http://www.talkchess.com/forum/viewtopic.php?t=55705) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 18, 2015
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Shogi](http://www.talkchess.com/forum/viewtopic.php?t=54092) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 20, 2014
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [\_\_int128 - Using the GNU Compiler Collection (GCC)](https://gcc.gnu.org/onlinedocs/gcc-4.7.3/gcc/_005f_005fint128.html#g_t_005f_005fint128)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Chess (Jazz & Sjaak) design](http://www.eglebbk.dds.nl/program/chess-design.html)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Chess (Jazz & Sjaak) search](http://www.eglebbk.dds.nl/program/chess-search.html)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Chess (Jazz & Sjaak) evaluation](http://www.eglebbk.dds.nl/program/chess-eval.html)

**[Up one level](Engines "Engines")**







 
