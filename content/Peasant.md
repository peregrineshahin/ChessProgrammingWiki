---
title: Peasant
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Peasant**



[ Celebrating Peasants <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Peasant**,  

a [pawn endgame](Pawn_Endgame "Pawn Endgame") chess program written by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") as research project started in 1973 at [Technion](https://en.wikipedia.org/wiki/Technion_%E2%80%93_Israel_Institute_of_Technology), [Haifa](https://en.wikipedia.org/wiki/Haifa), Israel, where the author had a visiting appointment. The goal was to examine whether the poor endgame play of the chess programs of that time was due to a basic weakness of [minimax](Minimax "Minimax") as suggested by [Larry Harris](Larry_Harris "Larry Harris") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, or simply because of [evaluation functions](Evaluation "Evaluation") used were not intended for those endings. 



### Terminal Nodes


A position is defined to be a [terminal node](Terminal_Node "Terminal Node") if one of the following conditions holds:



1. The maximum preset [depth](Depth "Depth") is met
2. One side has one or two pawns and the other has none (special static evaluator).
3. There is a queen on the board and the last move was not a promotion.
4. There is a [passed pawn](Passed_Pawn "Passed Pawn") which [cannot be caught by the enemy king](Unstoppable_Passer "Unstoppable Passer") and can [outrace](Pawn_Race "Pawn Race") all enemy pawns with a move to spare.
5. The depth is equal to that of a node where a win can be guaranteed. (This appears to be a special case of alpha-beta.)
6. The same position has occurred previously at the same depth in the [tree](index.php?title=Tree&action=edit&redlink=1 "Tree (page does not exist)") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.
7. [Stalemate](Stalemate "Stalemate")
8. The position is equivalent to a parent position which occurs four plies higher in the tree.
9. The winning side allows [draw](Draw "Draw") by [repetition](Repetitions "Repetitions")


### Evaluator


The static Evaluator is:



 *10\*MAT + 5\*PP - PRO + K1 + K2 + R*
with



* MAT ≡ the difference between the number of white pieces and the number of black pieces
* PP ≡ the difference between the number of white [passed pawns](Passed_Pawn "Passed Pawn") and the number of black passed pawns
* PRO ≡ the number of moves the most advanced white pawn must take before promotion minus the number of moves for the most advanced black pawn
* K1 ≡ factor measuring [king distance from the pawns](King_Pawn_Tropism "King Pawn Tropism"): five points deducted for every space that separates the king from the "center of gravity" of the pawns
* K2 ≡ three points if the king has [opposition](Opposition "Opposition")
* R ≡ ten points times the rank of each pawn that is passed and [cannot be stopped](Unstoppable_Passer "Unstoppable Passer") by the defending king


## Modified Rules


The [rules of chess](Rules_of_Chess "Rules of Chess") were modified in a way, that only [promotions](Promotions "Promotions") to a [queen](Queen "Queen") were possible, and to avoid later queen moves, the [side to move](Side_to_move "Side to move") had a win if one queen ahead and a draw if both sides had same number of queens (> 0), and no queening actually possible. 



## See also


* [Chunker](Chunker "Chunker")
* [PawnKing](PawnKing "PawnKing")


## Publications


* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *PEASANT: An endgame program for kings and pawns*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *Computer Chess Endgame Play with Pawns: Then and Now*. [ICGA Journal, Vol. 37, No. 4](ICGA_Journal#37_4 "ICGA Journal") » [Crafty](Crafty "Crafty")


## External Links


* [Peasant from Wikipedia](https://en.wikipedia.org/wiki/Peasant)
* [Peasant (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Peasant_%28disambiguation%29)
* [Peasant movement from Wikipedia](https://en.wikipedia.org/wiki/Peasant_movement)
* [Peasants' Party from Wikipedia](https://en.wikipedia.org/wiki/Peasants%27_Party)


 [Via Campesina from Wikipedia](https://en.wikipedia.org/wiki/Via_Campesina)
* [Peasants' Revolt from Wikipedia](https://en.wikipedia.org/wiki/Peasants%27_Revolt)


 [List of peasant revolts from Wikipedia](https://en.wikipedia.org/wiki/List_of_peasant_revolts)
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Celebrating Peasants](http://commons.wikimedia.org/wiki/File:Unbekannter_Meister_18-19_Jh_Feiernde_Bauern.jpg), artist unknown, 18th or 19th century, [Duesseldorfer Auktionshaus](http://www.duesseldorfer-auktionshaus.de/en/welcome/index), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Larry Harris](Larry_Harris "Larry Harris") (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *PEASANT: An endgame program for kings and pawns*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1978**). *[Co-ordinate Squares: A Solution to Many Chess Pawn Endgames](http://dl.acm.org/citation.cfm?id=67030)*. B.Sc. thesis, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), advisor [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") in his Co-ordinate Squares footnote on Peasant: "most serious design error is that rule six is too weak. A better condition is to terminate if the position has been reached in the tree search at any depth. Especially in these endgames, this is a very serious error"

**[Up one Level](Engines "Engines")**







 
