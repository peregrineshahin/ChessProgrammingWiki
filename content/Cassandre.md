---
title: Cassandre
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cassandre**

\[ Cassandra <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cassandre**,

an [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the terms of the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") (GPL) by [Raphael Grundrich](index.php?title=Raphael_Grundrich&action=edit&redlink=1 "Raphael Grundrich (page does not exist)"), [Thomas Adolph](index.php?title=Thomas_Adolph&action=edit&redlink=1 "Thomas Adolph (page does not exist)") and [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"),
written in [C++](Cpp "Cpp") and first released in March 2003. Cassandre started as a student project at [Louis Pasteur University](https://en.wikipedia.org/wiki/Louis_Pasteur_University), [Strasbourg](https://en.wikipedia.org/wiki/Strasbourg) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Description

Cassandre is a [bitboard](Bitboards "Bitboards") engine using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") with 256 [occupancy states](Occupancy_of_any_Line "Occupancy of any Line") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"),
[bitscan](BitScan "BitScan") aka first- and last one by conditional 16-bit lookups, and [population count](Population_Count "Population Count") by eight byte lookups credited to [Dann Corbit](Dann_Corbit "Dann Corbit") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Cassandre greatly lacks any [move ordering](Move_Ordering "Move Ordering") except generating [captures](Captures "Captures") before [quiet moves](Quiet_Moves "Quiet Moves").
The structure of the [move generation](Move_Generation "Move Generation") [serialization loops](Bitboard_Serialization "Bitboard Serialization") is an instructive counterexample of how one shouldn't write a bitboard engine.

## See also

- [Gaïa](Gaia "Gaia")

## External Links

## Chess Engine

- [Cassandre - Chess Engine](http://cassandre.sourceforge.net/)
- [Cassandre - at SourceForge.net](http://sourceforge.net/projects/cassandre/files/cassandre/)
- [Cassandre 0.24](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Cassandre%200.24) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Cassandre - Wikipédia.fr](http://fr.wikipedia.org/wiki/Cassandre) (French)
- [Cassandra from Wikipedia](https://en.wikipedia.org/wiki/Cassandra)
- [Cassandra (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cassandra_%28disambiguation%29)
- [Cassandra (metaphor) from Wikipedia](https://en.wikipedia.org/wiki/Cassandra_%28metaphor%29)
- [Cassandra (name) from Wikipedia](<https://en.wikipedia.org/wiki/Cassandra_(name)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Evelyn De Morgan](Category:Evelyn_De_Morgan "Category:Evelyn De Morgan") - [Cassandra](https://en.wikipedia.org/wiki/Cassandra) (1898, London). Cassandra in front of the burning city of [Troy](https://en.wikipedia.org/wiki/Troy) at the peak of her insanity, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Cassandre - Chess Engine](http://cassandre.sourceforge.net/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Cassandre - Chess Engine - About](http://cassandre.sourceforge.net/about.html), cassandre-0.24\\src\\BitboardToolkit.cpp - contage de bits par table lookup (D. Corbit)

**[Up one level](Engines "Engines")**

