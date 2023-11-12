---
title: Freccia
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Freccia**

\[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Freccia in Giardino <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Freccia**,

a chess engine by [Stefano Gemma](Stefano_Gemma "Stefano Gemma") with a [command line interface](CLI "CLI"), a complete rewrite of [Raffaela](Raffaela "Raffaela") in [x86](X86 "X86") [assembly](Assembly "Assembly") using some 64 bit features <a id="cite-note-2" href="#cite-ref-2">[2]</a> ([MMX](MMX "MMX")).
Its [piece coding](Pieces#PieceCoding "Pieces") allows [move generation](Move_Generation "Move Generation") with one [x86 test instruction](<https://en.wikipedia.org/wiki/TEST_(x86_instruction)>) per [target square](Target_Square "Target Square") and [sliding piece](Sliding_Pieces "Sliding Pieces") [direction](Direction "Direction"), branching on different [processor flags](https://en.wikipedia.org/wiki/FLAGS_register) - either [jump if greater](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Jump_if_Greater) to next direction in case of invalid square outside the board or own piece obstruction,
and to [push](Stack "Stack") the [move](Moves "Moves") to a [list](Move_List "Move List") otherwise without affecting flags, to post-branch [if positive](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Jump_if_Not_Signed) after a [capture](Captures "Captures") was generated, or to continue with the next square of the same direction after a [quiet move](Quiet_Moves "Quiet Moves") otherwise <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Freccia played the [CCC 2009](CCC_2009 "CCC 2009"), the [IOCSC 2010](IOCSC_2010 "IOCSC 2010"), and the [IOCSC 2011](IOCSC_2011 "IOCSC 2011").

## See also

- [Drago](Drago "Drago")
- [Raffaela](Raffaela "Raffaela")
- [Strelka](Strelka "Strelka")

## Forum Posts

- [Perft and mate](http://www.talkchess.com/forum/viewtopic.php?t=29425) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), August 16, 2009 » [Perft](Perft "Perft")
- [Assembly move generation in Freccia](http://www.talkchess.com/forum/viewtopic.php?t=39873) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), July 26, 2011
- [Freccia 0.0.2.5 released](http://www.talkchess.com/forum/viewtopic.php?t=63785) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), April 21, 2017
- [Christmas gift](http://www.talkchess.com/forum/viewtopic.php?t=66129) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), December 25, 2017

## External Links

## Chess Engine

- [Chess software for free - Original software made in Italy](http://www.linformatica.com/index-scacchi.php) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma")

## Misc

- [Freccia from Wikipedia](https://en.wikipedia.org/wiki/Freccia)
- [freccia - Wiktionary](https://en.wiktionary.org/wiki/freccia)
- [Freccia - Wikipedia.it](https://it.wikipedia.org/wiki/Freccia) (Italian)
- [Freccia Verde - Wikipedia.it](https://it.wikipedia.org/wiki/Freccia_Verde) (Italian)
- [Green Arrow from Wikipedia](https://en.wikipedia.org/wiki/Green_Arrow)
- [Arrow from Wikipedia](https://en.wikipedia.org/wiki/Arrow)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - [Antike Fabel](https://commons.wikimedia.org/wiki/File:Paul_klee,_freccia_in_giardino,_1929,_01.JPG), 1923, [Musée National d'Art Moderne](https://en.wikipedia.org/wiki/Mus%C3%A9e_National_d%27Art_Moderne), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Freccia 0.0.2.5 released](http://www.talkchess.com/forum/viewtopic.php?t=63785) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), April 21, 2017
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Assembly move generation in Freccia](http://www.talkchess.com/forum/viewtopic.php?t=39873) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), July 26, 2011

**[Up one level](Engines "Engines")**

