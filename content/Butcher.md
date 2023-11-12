---
title: Butcher
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Butcher**

\[ 14th century butcher <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Butcher** (Rzeźnik in Polish <a id="cite-note-2" href="#cite-ref-2">[2]</a> )

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Marek Kołacz](Marek_Ko%C5%82acz "Marek Kołacz"), written in [C](C "C"), first released in September 2001 <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Executables are available for [Windows](Windows "Windows") and [Linux](Linux "Linux"), early versions ran under [DOS](MS-DOS "MS-DOS").

## Parallel Search

Since version 1.60, Butcher is able to perform a [parallel search](Parallel_Search "Parallel Search") under [Windows](Windows "Windows") using [processes](Process "Process") and a [shared hash table](Shared_Hash_Table "Shared Hash Table"). A master process spawns worker processes, which run independently without any supervision. The Master process prepares all the structures necessary to split the node and continues the search. Worker processes simply use existing "split nodes" to start their search and report the results. The master process is responsible to kill the workers upon exit <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Tournament Play

Rzeźnik aka Butcher played all [Polish Computer Chess Championships](Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), and won its first edition, the [PCCC 2002](PCCC_2002 "PCCC 2002"), and the open category of the [PCCC 2004](PCCC_2004 "PCCC 2004") and [PCCC 2006](PCCC_2006 "PCCC 2006") <a id="cite-note-5" href="#cite-ref-5">[5]</a> , and otherwise was always a top scorer, at the [PCCC 2012](PCCC_2012 "PCCC 2012") best Polish program.
Butcher further played multiple [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), and had its tournament debut at the [CCT3](CCT3 "CCT3") in May 2001.

## Publications

- [Maciej Szmit](Maciej_Szmit "Maciej Szmit") (**2006**). *The 5th Polish Computer-Chess Championship: The Second Comeback of Butcher*. [ICGA Journal, Vol. 29, No. 4](ICGA_Journal#29_4 "ICGA Journal") » [PCCC 2006](PCCC_2006 "PCCC 2006")

## Forum Posts

- [New Butcher](https://www.stmintz.com/ccc/index.php?id=190209) by [Grzegorz Sidorowicz](Grzegorz_Sidorowicz "Grzegorz Sidorowicz"), [CCC](CCC "CCC"), September 24, 2001
- [Gauntlet Petir v2.0 and Butcher v1.53 with download](https://www.stmintz.com/ccc/index.php?id=400642) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), December 13, 2004
- [Gauntlets Liste B 5' + 5" - Butcher v1.56 - games](https://www.stmintz.com/ccc/index.php?id=436144) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), July 11, 2005

## External Links

## Chess Engine

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Butcher 1.61 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Butcher%201.61%2064-bit#Butcher_1_61_64-bit) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Butcher (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Butcher_%28disambiguation%29)
- [Butcher from Wikipedia](https://en.wikipedia.org/wiki/Butcher)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Butcher's [Tacuinum Sanitatis](https://en.wikipedia.org/wiki/Tacuinum_Sanitatis) [Casanatensis](https://en.wikipedia.org/wiki/Biblioteca_Casanatense), This picture is showing a 14th century butcher doing his trade in a traditional manner - unknown master, [Butcher from Wikipedia](https://en.wikipedia.org/wiki/Butcher)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Rzeźnictwo from Wikipedia.pl](http://pl.wikipedia.org/wiki/Rze%C5%BAnictwo) (Polish)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New Butcher](https://www.stmintz.com/ccc/index.php?id=190209) by [Grzegorz Sidorowicz](Grzegorz_Sidorowicz "Grzegorz Sidorowicz"), [CCC](CCC "CCC"), September 24, 2001
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Butcher's Homepage](http://markol4.republika.pl/) (expired link)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Maciej Szmit](Maciej_Szmit "Maciej Szmit") (**2006**). *The 5th Polish Computer-Chess Championship: The Second Comeback of Butcher*. [ICGA Journal, Vol. 29, No. 4](ICGA_Journal#29_4 "ICGA Journal")

**[Up one Level](Engines "Engines")**

