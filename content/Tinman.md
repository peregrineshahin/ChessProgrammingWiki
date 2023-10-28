---
title: Tinman
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Tinman**



[ Tin Woodman <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Tinman**,  

a didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [Mike Leany](Mike_Leany "Mike Leany"), written in [Rust](Rust "Rust"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Tinman is licensed under the [Mozilla Public License](https://en.wikipedia.org/wiki/Mozilla_Public_License), V. 2.0, and was first released in January 2020 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### Contents


* [1 Description](#description)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc)
* [5 References](#references)






So far, Tinman is quite rudimentary and lacks state of the art [search](Search "Search") techniques and [evaluation](Evaluation "Evaluation") terms - and has therefore huge potential to improve further.
It [represents the board](Board_Representation "Board Representation") with a [little-endian file-rank mapped](Square_Mapping_Considerations#LittleEndianFileRankMapping "Square Mapping Considerations") [bitboard definition](Bitboard_Board-Definition "Bitboard Board-Definition"),
and applies [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Search is plain [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [check extension](Check_Extensions "Check Extensions") and [quiescence](Quiescence_Search "Quiescence Search") inside the [iterative deepening](Iterative_Deepening "Iterative Deepening") loop <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
considering [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") as evaluation terms at the [leaves](Leaf_Node "Leaf Node") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## See also


* [Zilch](Zilch "Zilch")
* [Vapor](Vapor "Vapor")


## Forum Posts


* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=53) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), January 26, 2020
* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=75) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), February 16, 2020


## External Links


### Chess Engine


* [GitHub - mikeleany/tinman: A Rusty Chess Engine](https://github.com/mikeleany/tinman)
* [Tinman](https://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Tinman&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [tinman - Wiktionary](https://en.wiktionary.org/wiki/tinman)
* [tin man - Wiktionary](https://en.wiktionary.org/wiki/tin_man)
* [Tin Man - Wiktionary](https://en.wiktionary.org/wiki/Tin_Man)
* [Tinman - Wiktionary](https://en.wiktionary.org/wiki/Tinman)
* [Tin Man from Wikipedia](https://en.wikipedia.org/wiki/Tin_Man)
* [Tin Woodman from Wikipedia](https://en.wikipedia.org/wiki/Tin_Woodman)
* [Tin Man (Star Trek: The Next Generation) from Wikipedia](https://en.wikipedia.org/wiki/Tin_Man_(Star_Trek:_The_Next_Generation))
* [The Tin Man (American horse) from Wikipedia](https://en.wikipedia.org/wiki/The_Tin_Man_(American_horse))
* [The Tin Man (British horse) from Wikipedia](https://en.wikipedia.org/wiki/The_Tin_Man_(British_horse))
* [America](Category:America "Category:America") - [Tin Man](https://en.wikipedia.org/wiki/Tin_Man_(America_song)) (1974), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [Tin Woodman](https://en.wikipedia.org/wiki/Tin_Woodman) as pictured by [William Wallace Denslow](https://en.wikipedia.org/wiki/William_Wallace_Denslow) in [The Wonderful Wizard of Oz](https://en.wikipedia.org/wiki/The_Wonderful_Wizard_of_Oz) by [L. Frank Baum](https://en.wikipedia.org/wiki/L._Frank_Baum), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=53) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), January 26, 2020
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [tinman/attacks.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/chess/bitboard/attacks.rs)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [tinman/mod.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/engine/mod.rs)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [tinman/eval.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/engine/eval.rs)

**[Up one level](Engines "Engines")**







 
