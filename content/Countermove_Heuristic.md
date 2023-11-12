---
title: Countermove Heuristic
---
**[Home](Home "Home") * [Search](Search "Search") * [Move Ordering](Move_Ordering "Move Ordering") * Countermove Heuristic**

\[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Static-Dynamic Gradation, 1923 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Countermove Heuristic**,

a dynamic move ordering heuristic introduced by [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") in 1992, which shows some similarities with the [killer-](Killer_Heuristic "Killer Heuristic"), [refutation-](Refutation_Table "Refutation Table") and [history heuristic](History_Heuristic "History Heuristic") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . This heuristic assumes that many moves have a "natural" response, irrespective of the actual position, and is easy to implement either with a 64 * 64 [butterfly table](Butterfly_Boards "Butterfly Boards") or alternatively a more memory friendly 6 * 64 [array](Array "Array") for each [side to move](Side_to_move "Side to move"), indexed by \[from\]\[to\] or by \[piece\]\[to\] <a id="cite-note-3" href="#cite-ref-3">[3]</a> of the previous move, containing the counter move. The nature of the countermove heuristic renders it complementary to the killer heuristic, substituting position with same distance to the root with the last move played.

## Update

This is how the counter move [array](Array "Array") is updated, if a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") occurs:

```C++

   if ( score >= beta ) { // cutoff
      if ( isNonCapture (move) )
         counterMove[previousMove.from][previousMove.to] = move;
      ...
      return score;
   }

```

## Move Score

While assigning scores to moves for move ordering, a bonus is earned for the move which matches the countermove of the last move played:

```C++

   if ( movelist[i].move == counterMove[previousMove.from][previousMove.to] )
      movelist[i].score += counterMoveBonus;

```

## Butterfly Moves

Independently of Uiterwijk's work, [Dap Hartmann](Dap_Hartmann "Dap Hartmann") and [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") reported on the similar technique of [Butterfly board](Butterfly_Boards "Butterfly Boards") moves at [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), London 1990, being different from the [Butterfly heuristic](Butterfly_Heuristic "Butterfly Heuristic") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Their aim was to safe [move generation](Move_Generation "Move Generation") by proving only [legality](Legal_Move#LegalityTest "Legal Move") of a butterfly move. If both [transposition-](Transposition_Table "Transposition Table") and [killer table](Killer_Heuristic "Killer Heuristic") fail to supply a move, then 1 in 5 times the butterfly board was able to supply a legal killer which saved the complete move generation <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## See also

- [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
- [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic")
- [Counter Moves History](History_Heuristic#CMHist "History Heuristic")
- [History Heuristic](History_Heuristic "History Heuristic")
- [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [Last Best Reply](Last_Best_Reply "Last Best Reply")
- [Refutation Table](Refutation_Table "Refutation Table")

## Publications

- [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
- [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
- [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *Memory Efficiency in some Heuristics*. [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
- [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University")
- [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf)

## Forum Posts

## 2005 ...

- [Counter move heuristic](https://www.stmintz.com/ccc/index.php?id=446349) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), August 30, 2005

## 2010 ...

- [The LBR move ordering heuristic](http://www.talkchess.com/forum/viewtopic.php?t=38556) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 26, 2011 » [Last Best Reply](Last_Best_Reply "Last Best Reply")
- [Move ordering idea (old and new?)](http://www.talkchess.com/forum/viewtopic.php?t=44749) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), Aug 09, 2012
- [Re: History pruning / move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=47953&start=2) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 10, 2013

## [Re: History pruning / move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=47953&start=10) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), May 12, 2013 2015 ...

- [countermove heuristic](http://www.talkchess.com/forum/viewtopic.php?t=62676) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), December 31, 2016
- [Storing Countermoves by Ply](http://www.talkchess.com/forum/viewtopic.php?t=65107) by [Jason Fernandez](index.php?title=Jason_Fernandez&action=edit&redlink=1 "Jason Fernandez (page does not exist)"), [CCC](CCC "CCC"), September 08, 2017
- [Depth reduced but ELO increased](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70217) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 16, 2019

## 2020 ...

- [Problem with counter move heuristic](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=76255) by John Garrison, [CCC](CCC "CCC"), January 08, 2021

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Static-Dynamic Gradation, 1923, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *Memory Efficiency in some Heuristics*. [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Paul Lu](Paul_Lu "Paul Lu") (**1990**). *Report on the Advances in Computer Chess 6 Conference*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal")

**[Up one Level](Move_Ordering "Move Ordering")**

