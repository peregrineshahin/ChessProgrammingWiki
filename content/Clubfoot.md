---
title: Clubfoot
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Clubfoot**

[](https://github.com/zd3nik/Clubfoot/blob/master/Clubfoot-Logo.png) Clubfoot logo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Clubfoot**,

a very basic [UCI](UCI "UCI") [open source chess engine](Category:Open_Source "Category:Open Source") by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), written in [C++](Cpp "Cpp").
It was started as a real-world example of how to implement a UCI chess engine using the [Senjo](index.php?title=Senjo&action=edit&redlink=1 "Senjo (page does not exist)") UCI adapter <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
It uses [0x88](0x88 "0x88") board representation, [null move pruning](Null_Move_Pruning "Null Move Pruning"), [PVS](Principal_Variation_Search "Principal Variation Search") with [aspiration windows](Aspiration_Windows "Aspiration Windows"), [iterative deepening](Iterative_Deepening "Iterative Deepening"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [transposition table](Transposition_Table "Transposition Table"), [killer heuristic](Killer_Heuristic "Killer Heuristic"), [check extensions](Check_Extensions "Check Extensions"), and [late move reductions](Late_Move_Reductions "Late Move Reductions") using a custom version of the [history heuristic](History_Heuristic "History Heuristic") - among other common concepts.

This engine is available as source code <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and [Dann Corbit](Dann_Corbit "Dann Corbit") has provided binaries <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
Links to 32 and 64 bit binaries for [Windows](Windows "Windows") and [Linux](Linux "Linux") are also available in the Clubfoot README, found in the github source repository <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 Selected Games](#selected-games)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Selected Games

Here is a sample 5 minute game to demonstrate the [strength](Playing_Strength "Playing Strength") - or lack thereof - of Clubfoot:

```

[Event "Clubfoot vs Komodo"]
[Site "?"]
[Date "2015.03.07"]
[Round "1"]
[White "Clubfoot-1.0.2eb8144"]
[Black "Komodo-5-64bit"]
[Result "0-1"]

1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 d5 5.cxd5 Nxd5 6.Bg2 Nb6 7.O-O Be7 8.a3 O-O 9.d3 Be6 
10.e3 Qd7 11.b4 f6 12.d4 exd4 13.exd4 Rad8 14.Re1 Rfe8 15.Be3 Nd5 16.Qd3 Nxc3 17.Qxc3 
Bf8 18.Rac1 Bd5 19.h4 a6 20.Rcd1 Na7 21.Qd3 Nb5 22.Ra1 Be4 23.Qc4+ Qd5 24.Qxd5+ Bxd5 
25.Red1 Bb3 26.Re1 c6 27.Bf1 g6 28.Bxb5 axb5 29.Bf4 Kf7 30.Rxe8 Rxe8 31.Re1 Rd8 32.Bc1 
Be6 33.Bb2 b6 34.Rc1 Bd5 35.Nd2 Re8 36.Kf1 Bh6 37.Rc2 Re7 38.f4 g5 39.fxg5 fxg5 40.hxg5 
Bxg5 41.Ba1 Kg6 42.Bb2 Kh5 43.Bc1 Be3 44.Rc3 Bxd4 45.Rd3 c5 46.Bb2 Bc4 47.Nxc4 bxc4 
48.Rxd4 cxd4 49.Bxd4 b5 50.Kf2 Kg4 51.Bb2 Rd7 52.Be5 Rd3 53.Ke2 Rxa3 54.Kd2 h5 55.Ke2 
Rxg3 56.Kf2 h4 57.Ke2 h3 58.Kf2 h2 59.Bxg3 h1=Q 60.Be5 Qf3+ 61.Ke1 Qd3 62.Kf2 Qd2+ 
63.Kf1 Kf3 64.Bg3 Kxg3 65.Kg1 Qe1# 0-1

```

## See also

- [Bitfoot](Bitfoot "Bitfoot")

## Forum Posts

- [Clubfoot (UCI) by Shawn Chidester](http://www.talkchess.com/forum/viewtopic.php?t=55584) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), March 07, 2015

[Re: Clubfoot (UCI) by Shawn Chidester](http://www.talkchess.com/forum/viewtopic.php?t=55584&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 10, 2015

- [Introducing Bitfoot](http://www.talkchess.com/forum/viewtopic.php?t=56625) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), June 08, 2015 » [Bitfoot](Bitfoot "Bitfoot")
- [New Clubfoot and Bitfoot release builds available](http://www.talkchess.com/forum/viewtopic.php?t=57536) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), September 07, 2015

## External Links

## Chess Engine

- [Clubfoot source code on Github](https://github.com/zd3nik/Clubfoot)
- [Senjo UCI Adapter source code on Github](https://github.com/zd3nik/SenjoUCIAdapter)

## Misc

- [Club foot (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Club_foot_%28disambiguation%29)
- [Club foot from Wikipedia](https://en.wikipedia.org/wiki/Club_foot)
- [Club foot (furniture) from Wikipedia](https://en.wikipedia.org/wiki/Club_foot_%28furniture%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Compressed Logo (9KB) captured from [Clubfoot/Clubfoot-Logo.png at master · zd3nik](https://github.com/zd3nik/Clubfoot/blob/master/Clubfoot-Logo.png) (415 KB)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [zd3nik/SenjoUCIAdapter · GitHub](https://github.com/zd3nik/SenjoUCIAdapter)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Clubfoot source code on github.](https://github.com/zd3nik/Clubfoot)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Clubfoot (UCI) by Shawn Chidester](http://www.talkchess.com/forum/viewtopic.php?t=55584&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 10, 2015
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Clubfoot source code on github](https://github.com/zd3nik/Clubfoot)

**[Up one Level](Engines "Engines")**

