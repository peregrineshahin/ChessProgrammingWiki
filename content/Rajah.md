---
title: Rajah
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Rajah**


**Rajah** (RajahX),  

a chess program by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"). Its development started from scratch in early 1996. Rajah played the [DOCCC 1996](DOCCC_1996 "DOCCC 1996") and the [Aegon 1997](Aegon_1997 "Aegon 1997"), and its design, like many programs influenced by [Chess 4.5](Chess_(Program) "Chess (Program)") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, was described in [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Rajah is a [leaf-evaluator](Evaluation "Evaluation") and performs no [pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") at the [root](Root "Root") or interiour of the [tree](Search_Tree "Search Tree"). Rajah was further subject of research in the author's 2001 M.Sc. thesis on [parallel alpha-beta search](Parallel_Search "Parallel Search") from [University of Toronto](University_of_Toronto "University of Toronto") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Search


Rajah uses a full width [principal variation search](Principal_Variation_Search "Principal Variation Search") followed by [quiescence search](Quiescence_Search "Quiescence Search") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, where the [move generator](Move_Generation "Move Generation") only generates [captures](Captures "Captures") and [promotions](Promotions "Promotions") to a [queen](Queen "Queen"), where a first layer in [pruning](Pruning "Pruning") removes any capture that fails to bring the [material](Material "Material") score above a value based on [alpha](Alpha "Alpha") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. A second layer in QS performs [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), to prune all moves with a SEE values less than zero <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Additionally, Rajah applies [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") similar as described by [Donninger](Chrilly_Donninger "Chrilly Donninger") in 1993 <a id="cite-note-8" href="#cite-ref-8">[8]</a> with a [depth reduction](Depth_Reduction_R "Depth Reduction R") of two. It [extends](Extensions "Extensions") [checks](Check_Extensions "Check Extensions"), [recapturers](Recapture_Extensions "Recapture Extensions") and [passed pawn moves](Passed_Pawn_Extensions "Passed Pawn Extensions") to the 7th and 8th rank. Extension are switched off, when the search depth exceeds two times the current iteration depth.


The [transposition table](Transposition_Table "Transposition Table") is used in both full width and quiescence search, the replacement strategy is the one given by [Dennis Breuker](Dennis_Breuker "Dennis Breuker") et al. in 1994 <a id="cite-note-9" href="#cite-ref-9">[9]</a>. The [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic") is used in the full-width search only.




## 0x88


Rajah's [board representation](Board_Representation "Board Representation") relies on [0x88](0x88 "0x88") <a id="cite-note-10" href="#cite-ref-10">[10]</a>, to take advantage of testing those two bits in [target square](Target_Square "Target Square") traversal of [move generation](Move_Generation "Move Generation") <a id="cite-note-11" href="#cite-ref-11">[11]</a>, and specially for the unique square difference property for attack detection. In his article, Valavan gives the [C](C "C") source snippet of a typical inner loop in move generation, e.g. a white bishop moving diagonally up:




```C++

target_sq = current_sq;
while (1) {
  target_sq += 15; /* the move up and left */
  if ( target_sq & 0x88 ) break; /* check for out of bounds condition */
  if ( board[target_sq] == empty) {
    /* add a non-capture move to the move list */
  } else {
    if ( board[target_sq] & black_piece {
       /* add a capture move to the move list */
    }
    break;
  }
}

```

## Publications


* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1997**). *Augmentes Ideas*. Editorial [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal") <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**1997**). *Rajah: The Design of a Chess Program.* [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal")
* [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**). *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. M.Sc. thesis, [pdf](http://www.top-5000.nl/ps/Parallel%20Alpha-Beta%20Search%20on%20Shared%20Memory%20Multiprocessors.pdf)


## Forum Posts


* [X88 board representations](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ab3b34d5716dffa2) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 17, 1996 » [0x88](0x88 "0x88")
* [Computer Chess Hardware Design](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/83a6d26294a5ef99) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 30, 1997
* [Misinformation about RAJAH in the ICCA](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/36325d4b7bb0eea4) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 5, 1997
* [Re: Computerised Chess Games](http://groups.google.com/group/rec.games.chess.computer/msg/10c8fd07bc7f5d9a) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 07, 1997
* [Re: Mobility in evaluation functions- how much is it worth?](http://groups.google.com/group/rec.games.chess.computer/msg/cd5a7d7973636ca9) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 08, 1997 » [Mobility](Mobility "Mobility")
* [Re: GNU Chess for Pilot?](http://groups.google.com/group/comp.sys.palmtops/msg/fc370f4de81410ce) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 09, 1997 » [GNU Chess](GNU_Chess "GNU Chess")
* [Anyone want to represent Rajah at the WMCCC?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/fd1158b39a3fb7f5) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 14, 1997


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *Chess 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**1997**). *Rajah: The Design of a Chess Program.* [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal"), pp. 87-91
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**). *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. M.Sc. thesis
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Aegon 1996-97](http://www.thorstenczub.de/aegon.html) Photos by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1986**). *A Review of Game-Tree Pruning.* [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Günther Schrüfer](G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1989**). *A Strategic Quiescence Search*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [mvv/lva vs SEE capture ordering test results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1fa5e36362f5dde4) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 10, 1995
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"). (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *Replacement Schemes for Transposition Tables*. [ICCA Journal, Vol. 17, No. 4](ICGA_Journal#17_4 "ICGA Journal")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [X88 board representations](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ab3b34d5716dffa2) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 17, 1996
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> see [Vector Attacks - Increment Vectors](Vector_Attacks#IncrementVectors "Vector Attacks") why the cheap looking 0x88 test is not so "smart", [0x88 is not so smart](https://www.stmintz.com/ccc/index.php?id=114438) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), June 13, 2000
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Misinformation about RAJAH in the ICCA](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/36325d4b7bb0eea4#) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 5, 1997
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Re: Misinformation about RAJAH in the ICCA - APOLOGY](http://groups.google.com/group/rec.games.chess.computer/msg/47916b5f26aee711) by [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 8, 1997

**[Up one level](Engines "Engines")**







 
