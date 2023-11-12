---
title: Esc
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Esc**

\[ [ISO keyboard](https://en.wikipedia.org/wiki/ISO/IEC_9995) symbol for "Esc" <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Esc**, (ESC)

a [WinBoard](WinBoard "WinBoard") compatible chess engine by [Claudio Della Corte](Claudio_Della_Corte "Claudio Della Corte"), written in [C++](Cpp "Cpp"), first released in February 2001.
Esc won the *2nd Italian Engine Contest* played on-line in 2001/2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a> , and participated at three [CIPS tournaments](Italian_Computer_Chess_Championship#CIPS "Italian Computer Chess Championship"), third place at the [CIPS 2001](CIPS_2001 "CIPS 2001") with 3½/5 and [CIPS 2002](CIPS_2002 "CIPS 2002") with 4½/6 repectively, and runner-up at [CIPS 2004](CIPS_2004 "CIPS 2004") with 4/5. Esc further played the [CCT4](CCT4 "CCT4") with 5½/11.

## Desciption

Esc applies a [principal variation search](Principal_Variation_Search "Principal Variation Search") within an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, and uses [null move-](Null_Move_Pruning "Null Move Pruning"), [futility-](Futility_Pruning "Futility Pruning"), [extended futility pruning](Futility_Pruning#Extendedfutilityprunning "Futility Pruning"), [razoring](Razoring "Razoring") and various [extensions](Extensions "Extensions") to sharpen the [search tree](Search_Tree "Search Tree") as reported in its [search statistics](Search_Statistics "Search Statistics") given in the [log-file](Logging "Logging") <a id="cite-note-3" href="#cite-ref-3">[3]</a> , as well as [lazy evaluation](Lazy_Evaluation "Lazy Evaluation"). Further Esc utilizes three separate [hash tables](Hash_Table "Hash Table"), the main [transposition table](Transposition_Table "Transposition Table"), a smaller TT for the [quiescence search](Quiescence_Search "Quiescence Search") and a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"). [Move ordering](Move_Ordering "Move Ordering") considers [hash-](Hash_Move "Hash Move") and [PV-moves](PV-Move "PV-Move"), winning and equal [captures](Captures "Captures"), and two [killer moves](Killer_Move "Killer Move").

## Photos & Games

[](File:Nicola-claudio_cips2002.jpg)
[CIPS 2002](CIPS_2002 "CIPS 2002"), round 2, [Nicola Rizzuti](Nicola_Rizzuti "Nicola Rizzuti") and [Claudio Della Corte](Claudio_Della_Corte "Claudio Della Corte"), [Gargamella](Gargamella "Gargamella") - Esc <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "CIPS 2002"]
[Site "Pontedera"]
[Date "2002.06.01"]
[Round "2"]
[White "Gargamella 0.6"]
[Black "Esc 1.16"]
[Result "0-1"]

1.e4 c6 2.d4 d5 3.exd5 cxd5 4.Nc3 Nf6 5.Bb5+ Bd7 6.Nge2 Bxb5 7.Nxb5 Qa5+ 8.Nbc3 e6 9.Bg5 Ne4 
10.Bd2 Nxc3 11.Bxc3 Qb6 12.a4 Bd6 13.Ng3 O-O 14.O-O Qc7 15.Qd3 Rc8 16.Rae1 Qc4 17.Qxc4 Rxc4 
18.Ra1 Bxg3 19.fxg3 Nc6 20.Rad1 Rxa4 21.Rf2 Ra2 22.g4 b5 23.b4 a5 24.bxa5 b4 25.Be1 R8xa5
26.g5 R5a3 27.Kf1 Rb2 28.g4 Raa2 29.Rdd2 Na5 30.Rde2 Nc4 31.Rf3 Na3 32.Ref2 Nxc2 33.Rxf7 Ne3+ 
34.Kg1 Rxf2 35.Rxf2 Rxf2 36.Kxf2 b3 37.Kxe3 b2 38.h4 b1=Q 39.Bf2 e5 40.dxe5 Qe4+ 41.Kd2 d4 
42.e6 Qf4+ 43.Ke2 Qxg4+ 44.Kd2 Qf4+ 45.Ke1 d3 46.Bd4 Qc1+ 47.Kf2 d2 48.e7 Qe1+ 49.Kg2 d1=Q 
50.e8=Q+ Qxe8 51.Kg3 Qee2 52.Bc5 Qf3+ 53.Kh2 Qdh1# 0-1 

```

## Forum Posts

- [Nuovo Esc](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35617) by [Claudio Della Corte](Claudio_Della_Corte "Claudio Della Corte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 06, 2002
- [2nd "Italian Chess Engine Contest", (last round results)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35745) by [gianluigi](Gianluigi_Masciulli "Gianluigi Masciulli"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2002
- [ESC won his first offical tournament!](https://www.stmintz.com/ccc/index.php?id=218969) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 21, 2002
- [test position esc-movei](https://www.stmintz.com/ccc/index.php?id=251033) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 09, 2002
- [ESC 1.16 von Claudio della Corte](http://www.talkchess.com/forum/viewtopic.php?t=23416) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 31, 2008

## External Links

## Chess Engine

- [Esc « G 6](https://www.g-sei.org/category/chess-engines/esc/)
- [Esc 1.16](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Esc%201.16) in [KCEC](KCEC "KCEC")
- [Index of /chess/engines/Norbert's collection/Esc](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Esc%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

## Misc

- [ESC (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/ESC)
- [Esc key from Wikipedia](https://en.wikipedia.org/wiki/Esc_key)
- [Escape (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Escape)
- [Escape character from Wikipedia](https://en.wikipedia.org/wiki/Escape_character)
- [Escape sequence from Wikipedia](https://en.wikipedia.org/wiki/Escape_sequence)
- [Indigo Jam Unit](Category:Indigo_Jam_Unit "Category:Indigo Jam Unit") - Escape, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Esc key from Wikipedia](https://en.wikipedia.org/wiki/Esc_key)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [2nd "Italian Chess Engine Contest", (last round results)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35745) by [gianluigi](Gianluigi_Masciulli "Gianluigi Masciulli"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2002
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Index of /chess/engines/Norbert's collection/Esc/Esc 1.16/Esc000.log](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Esc%20%28Compilation%29/v1.16%20CIPS/Esc000.log)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [2° CIPS - le foto](https://www.g-sei.org/2-campionato-italiano/)

**[Up one level](Engines "Engines")**

