---
title: Pigeon
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Pigeon**



[ [Picasso](Category:Pablo_Picasso "Category:Pablo Picasso") - La Colombe <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Pigeon**,  

an original, experimental 64-bit [UCI](UCI "UCI") compliant chess engine by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), written in [C++](Cpp "Cpp"). 
Pigeon is [open source](Category:Open_Source "Category:Open Source"), released under the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"). 
To support [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") by [SSE2](SSE2 "SSE2") or [AVX2](AVX2 "AVX2") instructions as well as [CUDA](https://en.wikipedia.org/wiki/CUDA) for [Nvidia](Nvidia "Nvidia") [GPUs](GPU "GPU"), much of the critical code is branch-free. 
Pigeon generates [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") by [Kogge-Stone algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
It performs a [monochrome](Color_Flipping#Monochrome "Color Flipping") [move generation](Move_Generation "Move Generation") approach, [color flipping](Color_Flipping "Color Flipping") the board after [make move](Make_Move "Make Move") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
has an [iterative search](Iterative_Search "Iterative Search"), and used [automated tuning](Automated_Tuning "Automated Tuning") of [evaluation](Evaluation "Evaluation") weights by [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning").



## Forum Posts


* [Pigeon (new open source engine)](http://www.talkchess.com/forum/viewtopic.php?t=59782) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), April 07, 2016
* [New open source engine - Pigeon](http://www.talkchess.com/forum/viewtopic.php?t=59785) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), April 07, 2016
* [Pigeon now using opportunistic SIMD](http://www.talkchess.com/forum/viewtopic.php?t=59820) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), April 11, 2016
* [Pigeon 1.37 released](http://www.talkchess.com/forum/viewtopic.php?t=59900) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), April 19, 2016
* [Pigeon 1.5.0 released](http://www.talkchess.com/forum/viewtopic.php?t=61299) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), September 01, 2016
* [Pigeon 1.5.1 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61840&p=690810) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), October 25, 2016
* [Pigeon is now running on the GPU](http://www.talkchess.com/forum/viewtopic.php?t=61925) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), November 02, 2016 » [GPU](GPU "GPU")


## External Links


### Chess Engine


* [Pigeon Chess Engine](http://pigeonengine.com/)
* [Pigeon on GitHub](https://github.com/StuartRiffle/pigeon)
* [Pigeon](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Pigeon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) from [CCRL 40/15](CCRL "CCRL")


### Misc


* [Pigeon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Pigeon_%28disambiguation%29)
* [Columbidae from Wikipedia](https://en.wikipedia.org/wiki/Columbidae)
* [Domestic pigeon from Wikipedia](https://en.wikipedia.org/wiki/Domestic_pigeon)
* [Doves as symbols from Wikipedia](https://en.wikipedia.org/wiki/Doves_as_symbols)
* [Fancy pigeon from Wikipedia](https://en.wikipedia.org/wiki/Fancy_pigeon)
* [Homing pigeon from Wikipedia](https://en.wikipedia.org/wiki/Homing_pigeon)
* [Pigeon intelligence from Wikipedia](https://en.wikipedia.org/wiki/Pigeon_intelligence)
* [Pigeon post from Wikipedia](https://en.wikipedia.org/wiki/Pigeon_post)
* [Pigeon racing from Wikipedia](https://en.wikipedia.org/wiki/Pigeon_racing)
* [Cymande](Category:Cymande "Category:Cymande") - [Dove](https://en.wikipedia.org/wiki/Cymande_(album)) (1972), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Soviet postage stamp](https://en.wikipedia.org/wiki/Postage_stamps_of_the_Soviet_Union) from 1981 depicting [Picasso](Category:Pablo_Picasso "Category:Pablo Picasso") and his 1949 painting [La Colombe](https://www.moma.org/collection/works/60633), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [pigeon/bits.h at master · StuartRiffle/pigeon · GitHub](https://github.com/StuartRiffle/pigeon/blob/master/src/bits.h)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [pigeon/position.h at master · StuartRiffle/pigeon · GitHub](https://github.com/StuartRiffle/pigeon/blob/master/src/position.h)

**[Up one level](Engines "Engines")**







 
