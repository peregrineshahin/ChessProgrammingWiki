---
title: PeSTO27s Evaluation Function
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* PeSTO's Evaluation Function**


**PeSTO's Evaluation Function**,  

a [Piece-Square Tables Only](Piece-Square_Tables "Piece-Square Tables") evaluation function by [Ronald Friederich](Ronald_Friederich "Ronald Friederich") as tried in his chess engine [RofChade](RofChade "RofChade") <a id="cite-note-1" href="#cite-ref-1">[1]</a> further used in his experimental chess engine [PeSTO](PeSTO "PeSTO").
It performs a [tapered evaluation](Tapered_Eval "Tapered Eval") to interpolate by current [game stage](Game_Phases "Game Phases") between [piece-square tables](Piece-Square_Tables "Piece-Square Tables") values for [opening](Opening "Opening") and [endgame](Endgame "Endgame"), optimized by [Texel's tuning method](Texel%27s_Tuning_Method "Texel's Tuning Method"). Pesto's Evaluation Function is intended to replace [Tomasz Michniewski's](Tomasz_Michniewski "Tomasz Michniewski") [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function"), and was successfully applied in several engines.
[Maksim Korzh](Maksim_Korzh "Maksim Korzh") used and adapted Pesto's Evaluation Function in [Wukong JS](Wukong_JS "Wukong JS") along with his own Texel's tuning trials <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
[Pawel Koziol](Pawel_Koziol "Pawel Koziol") gave [TSCP](TSCP "TSCP") by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
an 200 Elo boost with Pesto's Evaluation Function <a id="cite-note-4" href="#cite-ref-4">[4]</a>, further tried by [Ed Schröder](Ed_Schroder "Ed Schroder") in [ProDeo](ProDeo "ProDeo") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## See also


* [PeSTO](PeSTO "PeSTO")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [ProDeo](ProDeo "ProDeo")
* [RofChade](RofChade "RofChade")
* [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [TSCP](TSCP "TSCP")
* [Wukong JS](Wukong_JS "Wukong JS")


## Forum Posts


* [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), Auguat 28, 2018
* [Re: Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238&start=15) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 07, 2021
* [little fun with TSCP](https://prodeo.actieforum.com/t252-little-fun-with-tscp) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021
* [ProDeo 3.1 - The PESTO version](https://prodeo.actieforum.com/t274-prodeo-3-1-the-pesto-version) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2021
* [ProDeo 3.1 - The PESTO version](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76643) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 19, 2021
* [Re: Hitting a wall at ~1860 Elo](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77427&start=17) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), June 02, 2021
* [Game Phase and tapered PSQT evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77546) by Jon12345, [CCC](CCC "CCC"), June 23, 2021
* [PeSTO's Evaluation Function, different"bestmove" for each depth](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77728) by Pedro Duran, [CCC](CCC "CCC"), July 15, 2021


## External Links


* [PeSTO: Piece Square Tables Only – RofChade](https://rofchade.nl/?p=307)
* [wukongJS/wukong.js at main · maksimKorzh/wukongJS · GitHub](https://github.com/maksimKorzh/wukongJS/blob/main/wukong.js#L897) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh") » [Wukong JS](Wukong_JS "Wukong JS")
* [Community - Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP/Community/) » [TSCP](TSCP "TSCP")
* [ProDeo 3.1 | The PeSTO Version](https://rebel13.nl/prodeo/prodeo-3.1.html) » [ProDeo](ProDeo "ProDeo")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), Auguat 28, 2018
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238&start=15) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 07, 2021
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Community - Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP/Community/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [little fun with TSCP](https://prodeo.actieforum.com/t252-little-fun-with-tscp) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ProDeo 3.1 - The PESTO version](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76643) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 19, 2021
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Community - Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP/Community/)

**[Up one Level](Evaluation "Evaluation")**







 
