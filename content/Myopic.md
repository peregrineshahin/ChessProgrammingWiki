---
title: Myopic
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Myopic**



[ Myopia <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Myopic**,  

a simple [open source chess program](Category:Open_Source "Category:Open Source") for small systems by [Steven Edwards](Steven_Edwards "Steven Edwards"), written in [C++](Cpp "Cpp") and released under the [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Myopic is suited for the [Arduino](Arduino "Arduino") **Mega** <a id="cite-note-2" href="#cite-ref-2">[2]</a> with the optional addition of a [SparkFun](https://en.wikipedia.org/wiki/SparkFun_Electronics) 8x8 [RGB LED](https://en.wikipedia.org/wiki/Light-emitting_diode#RGB_systems) backpack <a id="cite-note-3" href="#cite-ref-3">[3]</a> as move indicator output device. Otherwise, all I/O is gated through a single pair of routines that currently use the default [serial](https://en.wikipedia.org/wiki/Serial_communication) I/O pins <a id="cite-note-4" href="#cite-ref-4">[4]</a> . 



### Contents


* [1 Description](#description)
* [2 Download](#download)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






The board is represented by a [vector of 64](8x8_Board "8x8 Board") chessmen including vacant square chessmen. Search is plain [alpha-beta](Alpha-Beta "Alpha-Beta") inside the [iterative deepening](Iterative_Deepening "Iterative Deepening") loop with [leaf evaluation](Evaluation "Evaluation") considering [material balance](Material "Material"), [pawn placement](Pawn_Structure "Pawn Structure"), [pinned pieces](Pin "Pin") and [piece mobility](Mobility "Mobility"), and scaled [king center distance](Center_Distance "Center Distance") as bonus in the [middlegame](Middlegame "Middlegame") and penalty in the [endgame](Endgame "Endgame").



## Download


[File:Myopic.tar](File:Myopic.tar "File:Myopic.tar")



## See also


* [Arduino](Arduino "Arduino")
* [CookieCat](CookieCat "CookieCat")


## Forum Posts


* [Chess for the Arduino](http://forum.arduino.cc/index.php?topic=8330.0) by [chessplayer](Steven_Edwards "Steven Edwards"), [Arduino Forum](http://forum.arduino.cc/), December 06, 2009
* [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 22, 2010
* [Re: SAN Move Disambiguation -- looking for test positition](http://www.talkchess.com/forum/viewtopic.php?t=33764&start=3) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 11, 2010 » [SAN](Algebraic_Chess_Notation#SAN "Algebraic Chess Notation")
* [For a limited time, two sources](http://www.talkchess.com/forum/viewtopic.php?t=46964) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 22, 2013 » [CookieCat](CookieCat "CookieCat")


## External Links


* [myopic - Wiktionary](https://en.wiktionary.org/wiki/myopic)
* [Myopia (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Myopia_%28disambiguation%29)
* [Myopia from Wikipedia](https://en.wikipedia.org/wiki/Myopia)
* [Agnes Obel](Category:Agnes_Obel "Category:Agnes Obel") - [Myopia](https://en.wikipedia.org/wiki/Agnes_Obel#Myopia) (2020), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Diagram of Myopia](https://commons.wikimedia.org/wiki/File:Myopia_Diagram.jpg) in the [human eye](https://en.wikipedia.org/wiki/Human_eye), 2005, [National Eye Institute](https://en.wikipedia.org/wiki/National_Eye_Institute), [Myopia from Wikipedia](https://en.wikipedia.org/wiki/Myopia), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 22, 2010
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [LED Matrix - Tri Color - Large - COM-00683 - SparkFun Electronics](https://www.sparkfun.com/products/683)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess for the Arduino](http://forum.arduino.cc/index.php?topic=8330.0) by [chessplayer](Steven_Edwards "Steven Edwards"), [Arduino Forum](http://forum.arduino.cc/), December 06, 2009

**[Up one level](Engines "Engines")**







 
