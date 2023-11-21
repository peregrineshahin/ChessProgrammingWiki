---
title: ZurichessFribourg
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Zurichess**



[ [Zurich German](https://en.wikipedia.org/wiki/Zurich_German) [monophthongs](https://en.wikipedia.org/wiki/Monophthong) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Zurichess**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") and chess library by [Alexandru Moșoi](Alexandru_Mosoi "Alexandru Mosoi"), written in the [Go](Go_(Programming_Language) "Go (Programming Language)") programming language <a id="cite-note-2" href="#cite-ref-2">[2]</a> , first released in January 2015. The name Zurichess is in dependence on [Züritüütsch](https://en.wikipedia.org/wiki/Zurich_German), the [High Alemannic dialect](https://en.wikipedia.org/wiki/High_Alemannic_German) spoken in the [Canton of Zurich](https://en.wikipedia.org/wiki/Canton_of_Z%C3%BCrich), [Switzerland](https://en.wikipedia.org/wiki/Switzerland) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Versions are named after [Swiss Cantons](https://en.wikipedia.org/wiki/Cantons_of_Switzerland) in alphabetical order <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### A-B


Zurichess uses [bitboards](Bitboards "Bitboards") with [De Bruijn bitscan](BitScan#DeBruijnMultiplation "BitScan") for [serialization](Bitboard_Serialization "Bitboard Serialization"), and [fancy magic bitboards](Magic_Bitboards#Fancy "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). The [search](Search "Search") applies [fail soft](Fail-Soft "Fail-Soft") [negamax](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta") plus [transposition table](Transposition_Table "Transposition Table") inside the [iterative deepening](Iterative_Deepening "Iterative Deepening") loop with [aspiration windows](Aspiration_Windows "Aspiration Windows") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. [Move ordering](Move_Ordering "Move Ordering") is improved by the [killer heuristic](Killer_Heuristic "Killer Heuristic") and considers [MVV/LVA](MVV-LVA "MVV-LVA") for [captures](Captures "Captures"). [Evaluation](Evaluation "Evaluation") relies on the [simplified evaluation function](index.php?title=Simplified_evaluation_function&action=edit&redlink=1 "Simplified evaluation function (page does not exist)") using a [tapered eval](Tapered_Eval "Tapered Eval") interpolating between [opening](Opening "Opening") and [endgame](Endgame "Endgame") [scores](Score "Score") of [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables"). While the first public release **Aargau** lacked all kinds of [forward pruning](Pruning "Pruning"), [reductions](Reductions "Reductions") and [extensions](Extensions "Extensions"), subsequent versions, **Appenzeller** and **Basel** improved on various search and evaluation topics, now addressing [null move pruning](Null_Move_Pruning "Null Move Pruning") and [mobility](Mobility "Mobility") beside a lot of other things and optimizations, not to mention fixing bugs <a id="cite-note-6" href="#cite-ref-6">[6]</a>. **Bern** release in June 2015 is about 130 Elo stronger than Basel <a id="cite-note-7" href="#cite-ref-7">[7]</a>. 




### Fribourg


Zurichess **Fribourg**, released on August 30, 2015, now has [passed pawn](Passed_Pawn "Passed Pawn") evaluation, considering [connected](Connected_Passed_Pawns "Connected Passed Pawns") and [isolated](Isolated_Pawn "Isolated Pawn") pawns. [Tuning](Automated_Tuning "Automated Tuning") was done using [Texel's tuning method](Texel%27s_Tuning_Method "Texel's Tuning Method") implemented by **txt** <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>. [LMR](Late_Move_Reductions "Late Move Reductions") was added, as well as [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") (SEE) to sort [captures](Captures "Captures"), to [prune](Pruning "Pruning") bad captures (SEE < 0) in [quiescence search](Quiescence_Search "Quiescence Search") and to aggressively [reduce](Reductions "Reductions") bad [quiet moves](Quiet_Moves "Quiet Moves") (SEE < 0) at higher depths. Further, [staged move generation](Move_Generation#Staged "Move Generation") and [pondering](Pondering "Pondering") were added, and [two-fold repetitions](Repetitions "Repetitions") at non-root nodes pruned. Zurichess Fribourg is about 200 Elo stronger than Bern <a id="cite-note-10" href="#cite-ref-10">[10]</a> .




### Geneva


Zurichess **Geneva**, released on November 29, 2015, and now aware of the [fifty-move draw rule](Fifty-move_Rule "Fifty-move Rule"), has added basic [futility pruning](Futility_Pruning "Futility Pruning") and relaxed [null move conditions](Null_Move_Pruning "Null Move Pruning") allowing [double null moves](Double_Null_Move "Double Null Move"). In eval, [tuning](Automated_Tuning "Automated Tuning") switched from **txt** to [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) <a id="cite-note-11" href="#cite-ref-11">[11]</a> - a two layers [neural network](Neural_Networks "Neural Networks") is used, where the second layer is responsible for a [tapered eval](Tapered_Eval "Tapered Eval") to phase [endgame](Endgame "Endgame") and [middlegame](Middlegame "Middlegame") [scores](Score "Score") <a id="cite-note-12" href="#cite-ref-12">[12]</a>. Rooks were evaluated on [open and half-open files](Rook_on_Open_File "Rook on Open File"), and [mobility](Mobility "Mobility") calculation was improved. Zurichess Geneva is about 100 Elo stronger than Fribourg <a id="cite-note-13" href="#cite-ref-13">[13]</a>.




### Glarus


Announced and released on April 17, 2016, Zurichess **Glarus** has improved [futility conditions](Futility_Pruning "Futility Pruning") and added [history leaf pruning](History_Leaf_Pruning "History Leaf Pruning"), further improving [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") utilization by caching [pawn shelter](King_Safety#PawnShield "King Safety"), [king safety](King_Safety "King Safety") by considering number of simultaneous attackers, and [time control](Time_Management "Time Management"). Glarus is about 80 Elo stronger than Geneva in self-play <a id="cite-note-14" href="#cite-ref-14">[14]</a>. 




### Graubuenden


Zurichess **Graubuenden** was released on August 16, 2016 with various tweaks, search and evaluation improvements such as [hashing](Transposition_Table "Transposition Table") in [quiescence search](Quiescence_Search "Quiescence Search"), and new features like skill levels and [multi-PV](Principal_Variation#MultiPV "Principal Variation"). Further, a new version of the Go compiler yields in increased search speed. In self-play Graubuenden is about 110 Elo stronger than Glarus <a id="cite-note-15" href="#cite-ref-15">[15]</a>.




### Jura


Zurichess **Jura** appeared on February 18, 2017 with improved [selectivity](Selectivity "Selectivity"), [move ordering](Move_Ordering "Move Ordering") and evaluation, introducing [razoring](Razoring "Razoring"), [countermove heuristic](Countermove_Heuristic "Countermove Heuristic"), [king-queen tropism](King_Safety#KingTropism "King Safety") and [rook-square tables](Piece-Square_Tables "Piece-Square Tables") plus various tweaks and re-tuning. In self play at fast time controls Jura is about 85 Elo stronger than Graubuenden <a id="cite-note-16" href="#cite-ref-16">[16]</a>. 




### Luzern


Zurichess **Luzern**, released on May 08, 2017, further enhanced its search and evaluation, in particular a 16% faster search and considering defended minors, [pawn attacks](Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") an potential pawn attacks. In self play Luzern is about 64 Elo stronger than Jura <a id="cite-note-17" href="#cite-ref-17">[17]</a>.




### Neuchâtel


Zurichess **Neuchâtel** became a stable release in September 2017 <a id="cite-note-18" href="#cite-ref-18">[18]</a> with an expected gain of 50 Elo <a id="cite-note-19" href="#cite-ref-19">[19]</a>.



## See also


* [ETH Zurich](ETH_Zurich "ETH Zurich")
* [Winter](Winter "Winter")


## Forum Posts


### 2015


* [zurichess - new chess engine](http://www.talkchess.com/forum/viewtopic.php?t=54990) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 16, 2015
* [zurichess appenzeller - new version](http://www.talkchess.com/forum/viewtopic.php?t=55404) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), February 21, 2015
* [Re: txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696&start=81) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 11, 2015 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [zurichess basel released](http://www.talkchess.com/forum/viewtopic.php?t=56136) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 27, 2015
* [zurichess bern released](http://www.talkchess.com/forum/viewtopic.php?t=56617) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), June 07, 2015
* [zurichess fribourg released](http://www.talkchess.com/forum/viewtopic.php?t=57440) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 30, 2015
* [zurichess geneva released](http://www.talkchess.com/forum/viewtopic.php?t=58415) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 29, 2015


### 2016


* [hacking on zurichess](http://www.talkchess.com/forum/viewtopic.php?t=58826) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 06, 2016
* [trivia: ELO boost from a better compiler](http://www.talkchess.com/forum/viewtopic.php?t=59600) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 22, 2016 » [Go (Programming Language)](Go_(Programming_Language) "Go (Programming Language)")
* [king safety: hard positions for zurichess](http://www.talkchess.com/forum/viewtopic.php?t=59647) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 27, 2016 » [King Safety](King_Safety "King Safety"), [Test-Positions](Test_Positions "Test-Positions")
* [zurichess glarus released](http://www.talkchess.com/forum/viewtopic.php?t=59885) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 17, 2016
* [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=1) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016


 [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=4) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016
* [zurichess graubuenden released](http://www.talkchess.com/forum/viewtopic.php?t=61141) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 16, 2016


### 2017


* [zurichess jura - preview release](http://www.talkchess.com/forum/viewtopic.php?t=62875) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 19, 2017
* [zurichess jura released](http://www.talkchess.com/forum/viewtopic.php?t=63202) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), February 18, 2017
* [improved evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=63408) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 11, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [speed up or avoiding move sorting](http://www.talkchess.com/forum/viewtopic.php?t=63502) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 19, 2017 » [Move Ordering](Move_Ordering "Move Ordering")
* [zurichess - new version release](http://www.talkchess.com/forum/viewtopic.php?t=63931) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), May 08, 2017
* [zurichess neuchatel - preview release](http://www.talkchess.com/forum/viewtopic.php?t=65033) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 29, 2017
* [need some help assessing the evaluation](http://www.talkchess.com/forum/viewtopic.php?t=65886) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), December 02, 2017


### 2018 ...


* [Zurichess Nidwalden](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68561) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), October 03, 2018


 [Re: Zurichess Nidwalden](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68561&start=8) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), October 22, 2018
### 2019


* [MCTS: How to deal with extreme imbalances](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69612) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 16, 2019 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


## External Links


### Chess Engine


* [brtzsnr / zurichess — Bitbucket](https://bitbucket.org/brtzsnr/zurichess/)
* [zurichess / zurichess — Bitbucket](https://bitbucket.org/zurichess/zurichess)
* [Zurichess](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Zurichess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


### Aargau


* [Aargau from Wikipedia](https://en.wikipedia.org/wiki/Aargau)


### Appenzell


* [Appenzell (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Appenzell_%28disambiguation%29)
* [Appenzell (town) from Wikipedia](https://en.wikipedia.org/wiki/Appenzell_%28town%29)
* [Appenzeller cheese from Wikipedia](https://en.wikipedia.org/wiki/Appenzeller_cheese)


### Basel


* [Basel (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Basel_%28disambiguation%29)
* [Basel from Wikipedia](https://en.wikipedia.org/wiki/Basel)
* [Canton of Basel from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Basel)


### Bern


* [Bern (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bern_%28disambiguation%29)
* [Bern from Wikipedia](https://en.wikipedia.org/wiki/Bern)
* [Canton of Bern from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Bern)


### Fribourg


* [Fribourg (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Freiburg_%28disambiguation%29)
* [Fribourg from Wikipedia](https://en.wikipedia.org/wiki/Fribourg)
* [Canton of Fribourg from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Fribourg)


### Geneva


* [Geneva (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Geneva_%28disambiguation%29)
* [Geneva from Wikipedia](https://en.wikipedia.org/wiki/Geneva)
* [Canton of Geneva from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Geneva)
* [Geneva Conventions from Wikipedia](https://en.wikipedia.org/wiki/Geneva_Conventions)
* [Geneva Protocol from Wikipedia](https://en.wikipedia.org/wiki/Geneva_Protocol)


### Glarus


* [Glarus from Wikipedia](https://en.wikipedia.org/wiki/Glarus)
* [Canton of Glarus from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Glarus)
* [Glarus Alps from Wikipedia](https://en.wikipedia.org/wiki/Glarus_Alps)
* [Glarus thrust from Wikipedia](https://en.wikipedia.org/wiki/Glarus_thrust)


### Graubünden


* [Graubünden (Grisons) from Wikipedia](https://en.wikipedia.org/wiki/Grisons)
* [Three Leagues from Wikipedia](https://en.wikipedia.org/wiki/Three_Leagues)


### Jura


* [Canton of Jura from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Jura)
* [Jura Mountains from Wikipedia](https://en.wikipedia.org/wiki/Jura_Mountains)


### Luzern


* [Lucerne from Wikipedia](https://en.wikipedia.org/wiki/Lucerne)
* [Canton of Lucerne from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Lucerne)


### Neuchâtel


* [Neuchâtel (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Neuch%C3%A2tel_(disambiguation))
* [Neuchâtel from Wikipedia](https://en.wikipedia.org/wiki/Neuch%C3%A2tel)
* [Canton of Neuchâtel from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Neuch%C3%A2tel)


### Zurich


* [Zurich (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Zurich_%28disambiguation%29)
* [Zürich from Wikipedia](https://en.wikipedia.org/wiki/Z%C3%BCrich)
* [Canton of Zürich from Wikipedia](https://en.wikipedia.org/wiki/Canton_of_Z%C3%BCrich)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Jürg Fleischer](http://www.uni-marburg.de/fb09/igs/mitarbeiter/fleischer/index_html), [Stephan Schmid](https://www.philosophie.hu-berlin.de/institut/lehrbereiche/theorie/mitarbeiter/schmid) (**2006**).  *[Illustrations of the IPA: Zurich German](http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=591416&fileId=S0025100306002441)*. [Journal of the International Phonetic Association](https://en.wikipedia.org/wiki/Journal_of_the_International_Phonetic_Association), Vol. 36, No. 2, page 256; doi:10.1017/S0025100306002441, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Zurich German from Wikipedia](https://en.wikipedia.org/wiki/Zurich_German)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [brtzsnr / zurichess — Bitbucket](https://bitbucket.org/brtzsnr/zurichess/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Mr.Ruxy versus Zurichess](http://www.talkchess.com/forum/viewtopic.php?t=54990&start=17) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 17, 2015
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [zurichess / zurichess / source / CHANGELOG.md — Bitbucket](https://bitbucket.org/zurichess/zurichess/src/d80fadb47a1ecac6692cd582554d806b8e95ed62/CHANGELOG.md?at=master&fileviewer=file-view-default)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Aspiration window - effect? Issue with hashtables?! LONG POST](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=499768&t=46624) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), December 29, 2012
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [zurichess basel released](http://www.talkchess.com/forum/viewtopic.php?t=56136) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 27, 2015
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [zurichess bern released](http://www.talkchess.com/forum/viewtopic.php?t=56617) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), June 07, 2015
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 18, 2015
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [zurichess / txt — Bitbucket](https://bitbucket.org/zurichess/txt)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a>  [zurichess fribourg released](http://www.talkchess.com/forum/viewtopic.php?t=57440) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 30, 2015
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [tensorflow](http://www.talkchess.com/forum/viewtopic.php?t=58211) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 10, 2015
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=1) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [zurichess geneva released](http://www.talkchess.com/forum/viewtopic.php?t=58415) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 29, 2015
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [zurichess glarus released](http://www.talkchess.com/forum/viewtopic.php?t=59885) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 17, 2016
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [zurichess graubuenden released](http://www.talkchess.com/forum/viewtopic.php?t=61141) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 16, 2016
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [zurichess jura released](http://www.talkchess.com/forum/viewtopic.php?t=63202) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), February 18, 2017
17. <a id="cite-ref-17" href="#cite-note-17">↑</a>  [zurichess - new version release](http://www.talkchess.com/forum/viewtopic.php?t=63931) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), May 08, 2017
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [zurichess / zurichess / commit / f5f1b02de174 — Bitbucket](https://bitbucket.org/zurichess/zurichess/commits/f5f1b02de17478f3166c06d138d95178ea0c7941)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [zurichess neuchatel - preview release](http://www.talkchess.com/forum/viewtopic.php?t=65033) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 29, 2017

**[Up one Level](Engines "Engines")**







 
