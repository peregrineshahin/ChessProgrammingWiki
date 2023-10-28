---
title: Little Rook Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Little Rook Chess**



 [](https://github.com/olikraus/u8glib/wiki/little_rook_chess) Little Rook Chess <a id="cite-note-1" href="#cite-ref-1">[1]</a> with DOGM128 (128x64 dots) <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**Little Rook Chess**,  

a small [dedicated](Dedicated_Chess_Computers "Dedicated Chess Computers") [open source chess program](Category:Open_Source "Category:Open Source") by [Oliver Kraus](Oliver_Kraus "Oliver Kraus"), 
written in [C](C "C"), developed to run on an [Arduino Uno](Arduino#UNO "Arduino") with 32 KiB of [Flash memory](https://en.wikipedia.org/wiki/Flash_memory) 
and only 2 KiB of [RAM](Memory#RAM "Memory"). As a demonstration project how to use Oliver's *u8glib*, 
the universal graphics library (monochrom [OLEDs](https://en.wikipedia.org/wiki/OLED) and [GLCDs](https://en.wikipedia.org/wiki/Liquid-crystal_display)) for [embedded systems](https://en.wikipedia.org/wiki/Embedded_system)
<a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
the focus is on implementing the dedicated [user interface](User_Interface "User Interface") realized with an *Electronic Assembly DOG [LCD module](https://en.wikipedia.org/wiki/Liquid-crystal_display)*
<a id="cite-note-4" href="#cite-ref-4">[4]</a> 
and button shield. Little Rook Chess is part of *u8glib* under the terms of the [new bsd license](https://en.wikipedia.org/wiki/BSD_licenses)
<a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### Contents


* [1 Chess AI](#chess-ai)
* [2 See also](#see-also)
* [3 External Links](#external-links)
* [4 References](#references)






The "chess AI" of Little Rook Chess is rather rudimentary so far, with pure [minimax](Minimax "Minimax") rather than [alpha-beta](Alpha-Beta "Alpha-Beta"). 
The [evaluation](Evaluation "Evaluation") is based on [material](Material "Material") with [point values](Point_Value "Point Value") of {1, 3, 3, 5, 9} and has a few positional terms. 
The program keeps an [8x8 board](8x8_Board "8x8 Board") [array](Array "Array"), but uses [0x88](0x88 "0x88") coordinates to validate square indices, 
and always [transforms](0x88#Transformation "0x88") those coordinates at each board access <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Little Rook Chess lacks [minor promotions](Promotions#MinorPromotion "Promotions") and is unaware of [repetitions](Repetitions "Repetitions") and the [50-move rule](Fifty-move_Rule "Fifty-move Rule"), but otherwise plays legal chess with [castling](Castling "Castling") and [en passant](En_passant "En passant") implemented <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## See also


* [Arduino](Arduino "Arduino")
* [Micro-Max](Micro-Max "Micro-Max")


## External Links


* [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)
* [u8glib/chessengine.c at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/csrc/chessengine.c)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image from [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [dogm128e.pdf](http://www.lcd-module.com/eng/pdf/grafik/dogm128e.pdf) by *Electronic Assembly*
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chip-On-Glass DOG Displays from Electronic Assembly, Display Visions](https://www.lcd-module.com/produkte/dog.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [u8glib/license.txt at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/license.txt)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [u8glib/chessengine.c at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/csrc/chessengine.c)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)

**[Up one Level](Engines "Engines")**







 
