---
title: King SafetyKingTropism
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* King Safety**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb0) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - King <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
Good evaluation of the **king safety** is one of the most challenging tasks in writing an evaluation function, but also the most rewarding. The subjects are placed here in order of approximate (implementation) difficulty. If this page grows, it might be worthwhile to create a sub-page for each term. 




## Pawn Storm


If the enemy pawns are near to the king, there might be a threat of opening a file, even if the pawn shield is intact. Penalties for storming enemy pawns must be lower than penalties for (semi)open files, otherwise the pawn storm might backfire, resulting in a blockage.




## King Tropism


King [tropism](https://en.wikipedia.org/wiki/Tropism) is a simplified form of king safety evaluation. It takes into account the [distance](Distance "Distance") between the King and the attacking pieces, possibly weighted against [piece value](Point_Value "Point Value"). For example, one may double the distance value for a queen, and halve it for bishops and rooks. This kind of evaluation acts in a probabilistic way - it is by no means certain that being close to the king helps in attacking it. For example, if white castles short, black rook on h8 gets a higher tropism value regardless whether it stands on an open file. Nevertheless, using this kind of crude evaluation term increases a probability of building up an attack.


This kind of algorithm is used by [Crafty](Crafty "Crafty"). Another, perhaps more basic example is the [CPW-Engine](CPW-Engine "CPW-Engine") as implemented in [CPW-Engine\_eval](CPW-Engine_eval "CPW-Engine eval"), and the one demonstrated in the [Evaluation Function Draft](Evaluation_Function_Draft "Evaluation Function Draft").




## Virtual Mobility


Another heuristic is to temporary replace the king by a [queen](Queen "Queen"), to use her virtual [mobility](Mobility "Mobility") as a measure of opponent's [sliding piece](Sliding_Pieces "Sliding Pieces") [attacking](Sliding_Piece_Attacks "Sliding Piece Attacks") chances and therefore an unsafe king.
One may even temporary modify the [occupancy](Occupancy "Occupancy") to improve this virtual mobility, e.g by removing mobile opponent pieces.




## Scaling


Usually king safety value is scaled one way or the other. Even [TSCP](TSCP "TSCP") uses the pawn shield and pawn storm score, scaled by the opponent's material. This way, whenever the engine finds itself with a broken pawn shield, it tends to exchange pieces in order to alleviate the danger. [Fruit](Fruit "Fruit") uses a more elaborate scheme, counting the bonuses for attacking the squares near to the enemy king, and then multiplying their sum by the constant derived from the number of attackers. For an approximation of such approach, see [CPW\_King](CPW_King "CPW King") evaluation function.




## Attacking King Zone


*sample specification*
King zone is usually defined as squares to which enemy King can move plus two or three additional squares facing enemy position. Basic King safety function, similar to the one described in [Toga log user manual](Toga_Log#UserManual "Toga Log"), can work as follows: we have two variables, **attackingPiecesCount** and **valueOfAttacks**, zeroed at startup. If a piece attacks enemy king zone, we increase attackingPiecesCount by one, and count how many squares within enemy King zone are attacked. We multpily the number of attacked squares by a constant: 20 for a knight, 20 for a bishop, 40 for a rook and 80 for a queen. The result of multiplication is added to valueOfAttacks. After finding all attacks, we look at attackingPiecesCount, use it as an index to the table given below, and our king attack score is  
 **valueOfAttacks \* attackWeight[attackingPiecesCount] / 100**.





|  Nr ofAttackers
 |  Attackweight
 |
| --- | --- |
|  1
 |  0
 |
|  2
 |  50
 |
|  3
 |  75
 |
|  4
 |  88
 |
|  5
 |  94
 |
|  6
 |  97
 |
|  7
 |  99
 |






### Square Control


The most elaborate king safety evaluation schemes gather information about [control of the squares](Square_Control "Square Control") near the enemy king. A good explanation of such an algorithm might be found on [Ed Schröder's](Ed_Schroder "Ed Schroder") [Programmer Corner](Rebel#ProgrammerCorner "Rebel"). If a program, unlike [Rebel](Rebel "Rebel"), does not keep [incrementally updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), this knowledge is likely to be uncovered while calculating [mobility](Mobility "Mobility").



### Attack Units


[Rebel](Rebel "Rebel") (as we know from its description) and [Stockfish](Stockfish "Stockfish") (as we know from its code) use attack counter as an index to a table holding king attack scores. Stockfish counts each minor piece attack on a king zone (defined as squares that enemy king can reach + three more forward squares facing enemy position) as 2 attack units, rook attack on king zone as 3 attack units and a queen attack as 5 attack units. The virtue of such approach is twofold. **(1)** other factors beside these attacks can be counted. For example, Stockfish adds 6 attack units for a safe queen contact check and a couple attack units for a safe rook contact check. **(2)** the values held in the table may reflect attitude that "the whole is greater than the sum of parts". Typical curve is S-shaped: it raises slowly at first, then it goes up faster, becoming almost flat at the end.


This is the table from [Glaurung](Glaurung "Glaurung") 1.2:




```C++

static const int SafetyTable[100] = {
   0,   0,   0,   1,   1,   2,   3,   4,   5,   6,
   8,  10,  13,  16,  20,  25,  30,  36,  42,  48,
  55,  62,  70,  80,  90, 100, 110, 120, 130, 140,
 150, 160, 170, 180, 190, 200, 210, 220, 230, 240,
 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
 350, 360, 370, 380, 390, 400, 410, 420, 430, 440,
 450, 460, 470, 480, 490, 500, 510, 520, 530, 540,
 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
 650, 650, 650, 650, 650, 650, 650, 650, 650, 650,
 650, 650, 650, 650, 650, 650, 650, 650, 650, 650
};

```

This is the table generated using a formula from [Stockfish](Stockfish "Stockfish"), rescaled to [centipawns](Centipawns "Centipawns") :




```C++

static const int SafetyTable[100] = {
    0,  0,   1,   2,   3,   5,   7,   9,  12,  15,
  18,  22,  26,  30,  35,  39,  44,  50,  56,  62,
  68,  75,  82,  85,  89,  97, 105, 113, 122, 131,
 140, 150, 169, 180, 191, 202, 213, 225, 237, 248,
 260, 272, 283, 295, 307, 319, 330, 342, 354, 366,
 377, 389, 401, 412, 424, 436, 448, 459, 471, 483,
 494, 500, 500, 500, 500, 500, 500, 500, 500, 500,
 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
 500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
 500, 500, 500, 500, 500, 500, 500, 500, 500, 500
};

```

Using such tables, it is advisable not to evaluate king attack if only two pieces are attacking.




## Patterns


There are positions that tend to be notoriously difficult for the chess programs. One of them is a sacrifice of a minor piece on g5/g4, when it is simultaneously attacked and protected by the "h" pawns. Another one occurs after a standard Bxh7 sacrifice: White knight stands unchallenged on g5, white queen on h5, black King on g8 (positions with Kg6 are best left to the search). Hard-coding such patterns raises program's tactical awareness.



## See also


* [Castling Rights](Castling_Rights "Castling Rights")
* [Pawn Chain Direction](Pawn_Chain#ChainDirection "Pawn Chain")
* [Evaluation Function Draft](Evaluation_Function_Draft "Evaluation Function Draft")
* [Evaluation Patterns](Evaluation_Patterns "Evaluation Patterns")
* [King Safety](King_Pattern#KingSafety "King Pattern") in [King Pattern](King_Pattern "King Pattern") with [Bitboards](Bitboards "Bitboards")
* [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")


## Forums Posts


### 1998 ...


* [King Safety](https://www.stmintz.com/ccc/index.php?id=17373) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 22, 1998
* [King safety evaluation](https://www.stmintz.com/ccc/index.php?id=19415) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), May 28, 1998
* [Asymetric king safety](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/462b49226d1f1dfe#) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 13, 1999


### 2000 ...


* [What is Piece´s tropism?](https://www.stmintz.com/ccc/index.php?id=192418) by carlos, [CCC](CCC "CCC"), October 08, 2001
* [Bishop tropism?](https://www.stmintz.com/ccc/index.php?id=235856) by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), June 17, 2002


### 2005 ...


* [king safety](http://www.talkchess.com/forum/viewtopic.php?t=17546) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), November 02, 2007


### 2010 ...


* [Distance to King](http://www.talkchess.com/forum/viewtopic.php?t=31571) by [Adam Berent](Adam_Berent "Adam Berent"), [CCC](CCC "CCC"), January 08, 2010
* [About king safety](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=38756) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), April 15, 2011 » [Rodin](Rodin "Rodin")
* [value of king tropism in eval function](http://www.talkchess.com/forum/viewtopic.php?t=39102) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), May 17, 2011
* [Approaches to king safety?](http://www.talkchess.com/forum/viewtopic.php?t=42065) by [Mike Robinson](index.php?title=Mike_Robinson&action=edit&redlink=1 "Mike Robinson (page does not exist)"), [CCC](CCC "CCC"), January 19, 2012
* [For Ed Schroeder: Rebel's Pawn Shield and Pawn Storm Eval](http://www.talkchess.com/forum/viewtopic.php?t=44849) by Marcel Fournier, [CCC](CCC "CCC"), August 21, 2012
* [Pinned pieces in king safety](https://groups.google.com/d/msg/fishcooking/lIjQUH3dsYg/4VEtHUkrdBsJ) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2014 » [Pin](Pin "Pin"), [Stockfish](Stockfish "Stockfish")
* [King shelter x-ray attacks](http://www.talkchess.com/forum/viewtopic.php?t=52774) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), June 27, 2014 » [X-ray Attacks (Bitboards)](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")
* [Heavy piece shelter](http://www.talkchess.com/forum/viewtopic.php?t=52779) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), June 27, 2014
* [King safety refinements](http://www.talkchess.com/forum/viewtopic.php?t=53508) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), August 31, 2014


### 2015 ...


* [about king attack](http://www.talkchess.com/forum/viewtopic.php?t=57403) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 27, 2015
* [king shelter - when and how?](http://www.talkchess.com/forum/viewtopic.php?t=59583) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 21, 2016
* [king safety: hard positions for zurichess](http://www.talkchess.com/forum/viewtopic.php?t=59647) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 27, 2016 » [Zurichess](Zurichess "Zurichess")
* [Castling Evaluation](http://www.talkchess.com/forum/viewtopic.php?t=61014) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 02, 2016 » [Castling](Castling "Castling")
* [enemy edge pawn as part of own king shelter](http://www.talkchess.com/forum/viewtopic.php?t=65338) by Bram Mourik, [CCC](CCC "CCC"), September 30, 2017
* [Pawn Storm - Theory](http://www.talkchess.com/forum/viewtopic.php?t=66599) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), February 14, 2018 » [Pawn Storm](King_Safety#PawnStorm "King Safety")


### 2020 ...


* [Pruning / reduction depending on king safety](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72981) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 02, 2020 » [Pruning](Pruning "Pruning"), [Reductions](Reductions "Reductions")
* [Positional evaluation of your engine on this?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73877) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), May 09, 2020
* [King safety evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76976) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), March 29, 2021


## External Links


* [Middle game - King safety](http://www.mark-weeks.com/aboutcom/aa03e17.htm) from [Chess Tutorial : Improve Your Middle Game](http://www.mark-weeks.com/aboutcom/aa02j19.htm) by [Mark Weeks](Mark_Weeks "Mark Weeks")
* [Chess Strategy/The positions of the kings - Wikibooks](https://en.wikibooks.org/wiki/Chess_Strategy/The_positions_of_the_kings)
* [The Rolling Stones](Category:The_Rolling_Stones "Category:The Rolling Stones") - [Gimme Shelter](https://en.wikipedia.org/wiki/Gimme_Shelter) (1998 promotion video), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Bridges to Babylon Tour](https://en.wikipedia.org/wiki/Bridges_to_Babylon_Tour_%2797%E2%80%9398) feat. [Lisa Fischer](https://en.wikipedia.org/wiki/Lisa_Fischer) and [Darryl Jones](Category:Darryl_Jones "Category:Darryl Jones"), et al., December 12 1997, [Trans World Dome](https://en.wikipedia.org/wiki/The_Dome_at_America%27s_Center), [St. Louis](https://en.wikipedia.org/wiki/St._Louis) [Missouri](https://en.wikipedia.org/wiki/Missouri)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb0), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")

**[Up one Level](Evaluation "Evaluation")**







 
