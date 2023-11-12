---
title: Drofa
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Drofa**

\[\_(2416576086).jpg) [Дрофа](https://ru.wikipedia.org/wiki/%D0%94%D1%80%D0%BE%D1%84%D0%B0) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Drofa**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Alexander Litov](Alexander_Litov "Alexander Litov"), written in [C++ 11](Cpp "Cpp"), and first released in August 2020 under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Drofa started as [fork](<https://en.wikipedia.org/wiki/Fork_(software_development)>) of [Shallow Blue](Shallow_Blue "Shallow Blue") and improved considerably in subsequent versions, also incorporating [knowledge](Knowledge "Knowledge") from several open source engines such as [Vice](Vice "Vice"), [Weiss](Weiss "Weiss"), [Ethereal](Ethereal "Ethereal") and [Stockfish](Stockfish "Stockfish"),
due to [AdaGrad](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad) [tuning](Automated_Tuning "Automated Tuning") as proposed by [Andrew Grant](Andrew_Grant "Andrew Grant"), and using [Koivisto's](Koivisto "Koivisto") [OpenBench](OpenBench "OpenBench") instance <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP") (3.0.0)
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows") (3.0.0) <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [PV-Move](PV-Move "PV-Move")
  - [Captures](Captures "Captures") by [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") (3.0.0)
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") (2.0.0)
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") (2.0.0)
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") (1.0)
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") (2.0.0)
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (2.0.0)
  - [Razoring](Razoring "Razoring") (2.0.0)
  - [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning") (2.0.0)
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (2.0.0)
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
  - [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
  - [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Outposts](Outposts "Outposts")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table") (1.0)
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Connected Pawns](Connected_Pawns "Connected Pawns")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
- [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism") (2.2.0)
- [Tempo](Tempo "Tempo") (2.2.0)
- [Automated Tuning](Automated_Tuning "Automated Tuning") by [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning"), [AdaGrad](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad) (3.0.0)

## See also

- [Shallow Blue](Shallow_Blue "Shallow Blue")

## Forum Posts

- [Drofa 1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74950) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), August 31, 2020
- [Re: Is cloning a hobby?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75040&start=69) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), September 19, 2020
- [Drofa 2.0.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75744) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), November 09, 2020
- [Re: Are Aspiration Windows Worthless?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76115&start=12) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), December 23, 2020 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Drofa 2.2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=69) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), February 01, 2021
- [Re: New engine releases & news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=237) (Drofa 3.0.0) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), April 17, 2021

## External Links

## Chess Engine

- [GitHub - justNo4b/Drofa: UCI chess engine](https://github.com/justNo4b/Drofa)
- [Drofa](https://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Drofa&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")
- [Drofa](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Drofa&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [дрофа - Wiktionary](https://en.wiktionary.org/wiki/%D0%B4%D1%80%D0%BE%D1%84%D0%B0)
- [Great bustard from Wikipedia](https://en.wikipedia.org/wiki/Great_bustard)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Great bustard](https://en.wikipedia.org/wiki/Great_bustard), [Image](https://www.flickr.com/photos/andrej_chudy/2416576086/) by [Andrej Chudý](https://www.flickr.com/people/76362620@N00), March 30, 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Drofa 1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74950) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), August 31, 2020
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Drofa/README.md at master · justNo4b/Drofa · GitHub](https://github.com/justNo4b/Drofa/blob/master/README.md)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Are Aspiration Windows Worthless?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76115&start=12) by [Alexander Litov](Alexander_Litov "Alexander Litov"), [CCC](CCC "CCC"), December 23, 2020

**[Up one level](Engines "Engines")**

