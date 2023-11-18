---
title: Bruja
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bruja**

\[ [Hans Baldung](Category:Hans_Baldung "Category:Hans Baldung") - Witch and Dragon, 1515 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bruja**,

a [WinBoard](WinBoard "WinBoard") compatible chess engine by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), written in [C++](Cpp "Cpp") and first released in March 2004. In the program's readme file, Dan Honeycutt states that Bruja would never had come to be without the contributions of others, and credits [Adrien Regimbald](Adrien_Regimbald "Adrien Regimbald"), [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), and [Ed Schröder](Ed_Schroder "Ed Schroder") with their respective programs and descriptions as source of inspiration <a id="cite-note-2" href="#cite-ref-2">[2]</a> . A stripped version of Bruja, called [Simon](Simon "Simon"), was published as [open source engine](Category:Open_Source "Category:Open Source") <a id="cite-note-3" href="#cite-ref-3">[3]</a> .

## Description

Bruja has a [bitboard](Bitboards "Bitboards") infrastructure, and uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). It performs strictly [legal move generation](Move_Generation#Legal "Move Generation").

## Search

Bruja applies [PVS](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") [fractional ply](Depth#FractionalPlies "Depth") framework in conjunction with [null move pruning](Null_Move_Pruning "Null Move Pruning"), [singular](Singular_Extensions "Singular Extensions"), [recapture](Recapture_Extensions "Recapture Extensions") and [passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions").

## Evaluation

Bruja's [evaluation](Evaluation "Evaluation") initializes [attack tables](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps") as described in *Evaluation in REBEL* by [Ed Schröder](Ed_Schroder "Ed Schroder") <a id="cite-note-4" href="#cite-ref-4">[4]</a> , to do [hanging piece](Hanging_Piece "Hanging Piece") and [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), and to apply progressive [king safety](King_Safety "King Safety") evaluation. Further, Bruja has some [pawn structure](Pawn_Structure "Pawn Structure") knowledge and applies [piece-square tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## Etymology

Bruja is the Spanish word for [Witch](https://en.wikipedia.org/wiki/Witch) and can mean some worse things depending on context <a id="cite-note-6" href="#cite-ref-6">[6]</a>. The development of Bruja has started on [Friday](https://en.wikipedia.org/wiki/Friday), [October 31](https://en.wikipedia.org/wiki/Halloween), 2003, during the [Halloween storm](https://en.wikipedia.org/wiki/Geomagnetic_storm#Historical_occurrences) when major [flares](https://en.wikipedia.org/wiki/Solar_flare) erupted on the [Sun](https://en.wikipedia.org/wiki/Sun) with heavy influence on the [Earth](https://en.wikipedia.org/wiki/Earth) <a id="cite-note-7" href="#cite-ref-7">[7]</a> and spectacular [aurora](https://en.wikipedia.org/wiki/Aurora_%28astronomy%29) with [green phantom “northern lights”](Green_Light_Chess "Green Light Chess") seen as far south as [Texas](https://en.wikipedia.org/wiki/Texas), [Georgia](https://en.wikipedia.org/wiki/Georgia_%28U.S._state%29) and [Florida](https://en.wikipedia.org/wiki/Florida) <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## See also

- [Cupcake](Cupcake "Cupcake")
- [Hexxpawn](index.php?title=Hexxpawn&action=edit&redlink=1 "Hexxpawn (page does not exist)")
- [Sidonia](index.php?title=Sidonia&action=edit&redlink=1 "Sidonia (page does not exist)")
- [Simon](Simon "Simon")
- [Witchess](Witchess "Witchess")

## Forum Posts

- [Bruja - new engine](https://www.stmintz.com/ccc/index.php?id=354429) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 13, 2004
- [Simon](https://www.stmintz.com/ccc/index.php?id=407625) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), January 26, 2005
- [Bug in Bruja/Simon](https://www.stmintz.com/ccc/index.php?id=431094) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), June 13, 2005

## External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/BRUJA](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/BRUJA/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Bruja 1.9 64-bit JA No-int-book](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Bruja%201.9%2064-bit%20JA%20No-int-book) in [KCEC](KCEC "KCEC")

## Misc

- [bruja - Wiktionary](http://en.wiktionary.org/wiki/bruja)
- [Bruja (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bruja_%28disambiguation%29)
- [Brujería from Wikipedia](https://en.wikipedia.org/wiki/Brujer%C3%ADa)
- [Bruja - Wikipedia.es](http://es.wikipedia.org/wiki/Bruja) (Spanish)
- [Flying ointment from Wikipedia](https://en.wikipedia.org/wiki/Flying_ointment)
- [Hexenbesen (Mythologie) - Wikipedia.de](http://de.wikipedia.org/wiki/Hexenbesen_%28Mythologie%29) (German)

[Besom from Wikipedia](https://en.wikipedia.org/wiki/Besom)

- [Wicca from Wikipedia](https://en.wikipedia.org/wiki/Wicca)
- [Witch (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Witch_%28disambiguation%29)
- [Witch of Agnesi from Wikipedia](https://en.wikipedia.org/wiki/Witch_of_Agnesi)
- [Witchcraft from Wikipedia](https://en.wikipedia.org/wiki/Witchcraft)
- [Witch-hunt from Wikipedia](https://en.wikipedia.org/wiki/Witch-hunt)
- [Witch trial (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Witch_trial_%28disambiguation%29)
- [Witch trials in the early modern period - Wikipedia](https://en.wikipedia.org/wiki/Witch_trials_in_the_early_modern_period)

[Protests against early modern witch trials - Wikipedia](https://en.wikipedia.org/wiki/Protests_against_early_modern_witch_trials)

- [Albert King](https://en.wikipedia.org/wiki/Albert_King) and [Stevie Ray Vaughan](Category:Stevie_Ray_Vaughan "Category:Stevie Ray Vaughan") - [Born Under a Bad Sign](http://en.wikipedia.org/wiki/Born_Under_a_Bad_Sign_%28song%29), [YouTube](http://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Hans Baldung](Category:Hans_Baldung "Category:Hans Baldung"), [Stehende Hexe mit Ungeheuer](https://en.wikipedia.org/wiki/File:Hans_Baldung_-_Stehende_Hexe_mit_Ungeheuer.jpg), 1515; Feder, weiß gehöht, auf braun grundiertem Papier, 295 × 207 mm, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Bruja - new engine](https://www.stmintz.com/ccc/index.php?id=354429) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 13, 2004
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Simon](https://www.stmintz.com/ccc/index.php?id=407625) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), January 26, 2005
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Evaluation in REBEL (hanging pieces)](http://www.top-5000.nl/authors/rebel/chess840.htm#HW) from [How Rebel Plays Chess](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), also available as [pdf](http://members.home.nl/matador/Inside%20Rebel.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Bruja - new engine](https://www.stmintz.com/ccc/index.php?id=354429) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 13, 2004
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Bruja - new engine](https://www.stmintz.com/ccc/index.php?id=354429) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 13, 2004
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Giant Halloween Solar Storm Sparked Earth Scares 10 Years Ago (Video) | Space.com](http://www.space.com/23396-scary-halloween-solar-storm-2003-anniversary.html)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [The Magnetic Storm of Halloween 2003 | Science Features](http://www.usgs.gov/blogs/features/usgs_top_story/the-magnetic-storm-of-halloween-2003-2/) by [Jeffrey J. Love](http://scholar.google.com/citations?user=xhXV9WUAAAAJ&hl=de), [E. Joshua Rigler](http://geomag.usgs.gov/contact.php), and [Jessica K. Robertson](https://profile.usgs.gov/jrobertson), [United States Department of the Interior](https://en.wikipedia.org/wiki/United_States_Department_of_the_Interior) | [United States Geological Survey](https://en.wikipedia.org/wiki/United_States_Geological_Survey), October 15, 2013

**[Up one Level](Engines "Engines")**

