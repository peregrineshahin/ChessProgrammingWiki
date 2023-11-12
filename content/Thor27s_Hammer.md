---
title: Thor27s Hammer
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Thor's Hammer**



[ Thor's Hammer <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
**Thor's Hammer**, (Mjoelner)  

a [WinBoard](WinBoard "WinBoard") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Toma Roncevic](Toma_Roncevic "Toma Roncevic") written in [C++](Cpp "Cpp"), first released in December 2002. Mjoelner participated at the *2nd Italian Engine Contest* played on-line in 2001/2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and Thor's Hammer played the [CIPS 2003](CIPS_2003 "CIPS 2003") with 3½/7. Thor's Hammer is available from [Jim Ablett's](Jim_Ablett "Jim Ablett") Winboard Chess Projects site, who also reported a huge speed gain of the 64-bit over the 32-bit build <a id="cite-note-3" href="#cite-ref-3">[3]</a>, which is quite typical for [bitboard](Bitboards "Bitboards") engines. 



### Move Generation


Thor's Hammer is a [bitboard](Bitboards "Bitboards") engine without explicitly [scanning bits](BitScan "BitScan") of set-wise [attack](Attacks "Attacks") [intersections](General_Setwise_Operations#Intersection "General Setwise Operations"), in particular [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). It applies a [staged move generation](Move_Generation#Staged "Move Generation") with [testing legality](Square_Attacked_By#LegalityTest "Square Attacked By") of [hash-](Hash_Move "Hash Move") and [killer moves](Killer_Move "Killer Move"). Otherwise, it generates [quiet moves](Quiet_Moves "Quiet Moves") of [sliding pieces](Sliding_Pieces "Sliding Pieces") loop-wise for each [ray-direction](Direction#RayDirections "Direction"). Even sliding [captures](Captures "Captures") are generated quite similar to the [blocker loop](Vector_Attacks#NewArchitecture "Vector Attacks") of a [vector attack](Vector_Attacks "Vector Attacks") [array representation](Board_Representation#SquareCentric "Board Representation"), but with the important difference that testing the capture condition is done before entering the loop rather than after loop execution. If the intersection of the [negative rays](On_an_empty_Board#NegativeRays "On an empty Board") [from a square](Origin_Square "Origin Square") with the opponent pieces as capture target is greater than the intersection with own pieces, a capture is possible on that ray.




```C++

south east (f6)    &  opponent pieces  &  own pieces
 . . . . . . . .      . . . . . . . .     . . . . . . . . 
 . . . . . . . .      . . . . . . . .     . . . . . . . . 
 . . . . . . . .      . . . . . . . .     . . . . . . . . 
 . . . . 1 . . .      . . . . . . . .     . . . . . . . . 
 . . . 1 . . . .      . . . 1 . . . .  >  . . . . . . . . 
 . . 1 . . . . .      . . . . . . . .     . . . . . . . . 
 . 1 . . . . . .      . . . . . . . .     . 1 . . . . . . 
 1 . . . . . . .      . . . . . . . .     1 . . . . . . . 

```

To apply the same trick for the [positive rays](On_an_empty_Board#PositiveRays "On an empty Board"), [incremental updated](Incremental_Updates "Incremental Updates") [reverse bitboards](Reverse_Bitboards "Reverse Bitboards") are used <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```C++

  if(ptype[color][i]==BISHOP || ptype[color][i]==QUEEN) {
    fmask=~omask;
    if((seFrom[xp]&omask) > (seFrom[xp]&nmask)) {
      c=xp-7;
      while((setBit(c) & (fmask))) c-=7;
      *moves++ = setMove(i,c);
    }
    if((seFrom[63-xp]&orotmask) > (seFrom[63-xp]&nrotmask)) {
      c=xp+7;
      while((setBit(c) & (fmask))) c+=7;
      *moves++ = setMove(i,c);
    }
    if( ...
  }
  ...

```

On processors with slow bitscan, i.e. [Intel's](Intel "Intel") [x86](X86 "X86") [NetBurst microarchitecture](https://en.wikipedia.org/wiki/NetBurst_%28microarchitecture%29), the compact scan loops to skip empty squares inside the [instruction pipeline](https://en.wikipedia.org/wiki/Pipeline_%28computing%29) should not that much slower on average.



### Search


The [search](Search "Search") relies on [iterative deepening](Iterative_Deepening "Iterative Deepening") with [aspiration windows](Aspiration_Windows "Aspiration Windows") and [PVS](Principal_Variation_Search "Principal Variation Search"), [transpostion table](Transposition_Table "Transposition Table"), [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [check-](Check_Extensions "Check Extensions"), [passed pawn-](Passed_Pawn_Extensions "Passed Pawn Extensions") and [recapture extensions](Recapture_Extensions "Recapture Extensions").



### Evaluation


[Evaluation](Evaluation "Evaluation") counts [material](Material "Material") and positionally considers [pawn structure](Pawn_Structure "Pawn Structure") utilizing a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), [passed pawns](Passed_Pawn "Passed Pawn") including [rule of the square](Rule_of_the_Square "Rule of the Square") in the [pawn endings](Pawn_Endgame "Pawn Endgame"), [king safety](King_Safety "King Safety") in the [middlegame](Middlegame "Middlegame") and [centralization](King_Centralization "King Centralization") in the [endgame](Endgame "Endgame"), [mobility](Mobility "Mobility") and multiple other features.



## See also


* [Freyr](Freyr "Freyr")
* [Loki](Loki "Loki")


## Forum Posts


* [Thor's Hammer new version](http://www.open-aurec.com/wbforum/viewtopic.php?t=601) by [toma](Toma_Roncevic "Toma Roncevic"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 15, 2004
* [Thor's Hammer 2.25](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1644&p=7640) by [toma](Toma_Roncevic "Toma Roncevic"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 14, 2005
* [Gauntlet Thor's Hammer v2.25 and GES v1.36 - games](https://www.stmintz.com/ccc/index.php?id=418983) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), March 30, 2005
* [Gauntlets Liste B 5' + 5" Thor's Hammer v2.28 - games](https://www.stmintz.com/ccc/index.php?id=439476) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), August 01, 2005
* [Gosu 0.16 v Thor's Hammer 2.28 (queen sac)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=25286) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), December 06, 2008 » [Gosu](Gosu "Gosu")
* [Jim, do you remember?](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50055) by [Gábor Szots](Gabor_Szots "Gabor Szots"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2009
* [Re: Jim, do you remember?](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50055&start=20#p190004) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 24, 2009


## External Links


### Chess Engine


* [Thor's Hammer Home Page](http://web.archive.org/web/20060614102734/http://www.geocities.com/toma_st/thorshammer.html) archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) (June 2006)
* [Index of /chess/engines/Jim Ablett/THORS HAMMER](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/THORS%20HAMMER/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Thor's Hammer 2.28 32-bit](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&eng=Thor%27s%20Hammer%202.28%2032-bit#Thor_s_Hammer_2_28_32-bit) in [KCEC](KCEC "KCEC")
* [Thor's Hammer](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Thor%27s%20Hammer&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Thor's Hammer (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Thor%27s_Hammer_%28disambiguation%29)
* [Mjölnir from Wikipedia](https://en.wikipedia.org/wiki/Mj%C3%B6lnir)
* [Mjolnir (comics) from Wikipedia](https://en.wikipedia.org/wiki/Mjolnir_%28comics%29)
* [Thor from Wikipedia](https://en.wikipedia.org/wiki/Thor)
* [Hammer from Wikipedia](https://en.wikipedia.org/wiki/Hammer)
* [Hammer of Thor (monument) from Wikipedia](https://en.wikipedia.org/wiki/Hammer_of_Thor_%28monument%29)
* [Thors Hammer](http://www.alexgitlin.com/npp/thors.htm) - Evasive Dreams Beyond, 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> *The third gift — an enormous hammer* by [Elmer Boyd Smith](https://en.wikipedia.org/wiki/Elmer_Boyd_Smith). The [dwarven](https://en.wikipedia.org/wiki/Dwarf_%28Germanic_mythology%29) [Sons of Ivaldi](https://en.wikipedia.org/wiki/Sons_of_Ivaldi) forge the [hammer Mjolnir](https://en.wikipedia.org/wiki/Mj%C3%B6lnir) for the god [Thor](https://en.wikipedia.org/wiki/Thor) while [Loki](https://en.wikipedia.org/wiki/Loki) watches on. On the table before them sits their other creations: the multiplying ring [Draupnir](https://en.wikipedia.org/wiki/Draupnir), the [boar](https://en.wikipedia.org/wiki/Wild_boar) [Gullinbursti](https://en.wikipedia.org/wiki/Gullinbursti), the ship [Skíðblaðnir](https://en.wikipedia.org/wiki/Sk%C3%AD%C3%B0bla%C3%B0nir), the spear [Gungnir](https://en.wikipedia.org/wiki/Gungnir), and [golden hair](https://en.wikipedia.org/wiki/Golden_Hair) for the goddess [Sif](https://en.wikipedia.org/wiki/Sif), Page 88 of [Abbie Farwell Brown](https://en.wikipedia.org/wiki/Abbie_Farwell_Brown) (**1902**). *[In the Days of Giants: A Book of Norse Tales](http://www.germanicmythology.com/works/EBOYDSMITHART.html)*. Illustrations by Elmer Boyd Smith. [Houghton, Mifflin & Co.](https://en.wikipedia.org/wiki/Houghton_Mifflin_Harcourt), [Mjölnir from Wikipedia](https://en.wikipedia.org/wiki/Mj%C3%B6lnir)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [2nd "Italian Chess Engine Contest", (last round results)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35745) by [gianluigi](Gianluigi_Masciulli "Gianluigi Masciulli"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2002
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Jim, do you remember?](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50055&start=20#p190004) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 24, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> thorshammer-229-ja.zip, Position.cpp, line 1329, slightly edited

**[Up one level](Engines "Engines")**







 
