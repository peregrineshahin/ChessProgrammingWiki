---
title: Ceres
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Ceres**

\[\_(cropped).jpg) Ceres <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ceres**, (**C**hess **e**ngine for **res**earch)

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [David J. Elliott](index.php?title=David_J._Elliott&action=edit&redlink=1 "David J. Elliott (page does not exist)"), written in [C#](C_sharp "C sharp") for the [Microsoft](Microsoft "Microsoft") [.NET 5](https://en.wikipedia.org/wiki/.NET_Core) framework, released under the [GPL version 3](Free_Software_Foundation#GPL "Free Software Foundation").
Ceres provides an [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") implementation with many novel algorithmic improvements and low level optimizations, searching over the [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") backends <a id="cite-note-2" href="#cite-ref-2">[2]</a> with the perspective of an enormous increase in [playing strength](Playing_Strength "Playing Strength") over Lc0. Ceres' [move generation](Move_Generation "Move Generation") code is adapted from [Judd Niemann's](Judd_Niemann "Judd Niemann") [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards") based [Perft](Perft "Perft") approach [Juddperft](index.php?title=Juddperft&action=edit&redlink=1 "Juddperft (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
As posted by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk") on January 01, 2021, it is possible that Ceres will co-exist in parallel to Lc0 and LCZero developers will try to back-port new ideas, or LCZero developers will abandon Lc0 completely and switch to Ceres <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 See also](#see-also)
- [2 Postings](#postings)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")

## Postings

- [Ceres](https://www.themissingdocs.net/?p=874) by [Tilps](Gareth_Pearce "Gareth Pearce"), [The Missing Docs.Net](https://www.themissingdocs.net/), January 01, 2021
- [Announcing Ceres](https://lczero.org/blog/2021/01/announcing-ceres/) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), January 01, 2021
- [+100 elo breakthrough in new rewritten Lco engine ( Ceres)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76201) by Nay Lin Tun, [CCC](CCC "CCC"), January 01, 2021
- [Ceres 0.87 is Out](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76534) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), February 09, 2021

## External Links

## Chess Engine

- [GitHub - dje-dev/Ceres: Ceres - an MCTS chess engine for research and recreation](https://github.com/dje-dev/Ceres)

## Misc

- [Ceres from Wikipedia](https://en.wikipedia.org/wiki/Ceres)
- [Ceres (mythology) from Wikipedia](<https://en.wikipedia.org/wiki/Ceres_(mythology)>)
- [Ceres (dwarf planet) from Wikipedia](<https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)>)
- [Asteroid Ceres in fiction from Wikipedia](https://en.wikipedia.org/wiki/Asteroid_Ceres_in_fiction)
- [Ceres (workstation) from Wikipedia](<https://en.wikipedia.org/wiki/Ceres_(workstation)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Approximate true-color [image](<https://commons.wikimedia.org/wiki/File:Ceres_-_RC3_-_Haulani_Crater_(22381131691)_(cropped).jpg>) of [Ceres](<https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)>), using the F7 ('red'), F2 ('green') and F8 ('blue') filters, projected onto a clear filter image. Images were acquired by Dawn at 04:13 UT May 4, 2015, at a distance of 13641 km. At the time, Dawn was over Ceres' northern hemisphere. The prominent, bright crater at right is [Haulani](<https://en.wikipedia.org/wiki/Haulani_(crater)>). The smaller bright spot to its left is exposed on the floor of [Oxo](https://www.jpl.nasa.gov/images/haulani-and-oxo-craters/). [Ejecta](https://en.wikipedia.org/wiki/Ejecta) from these impacts appears to have exposed high [albedo](https://en.wikipedia.org/wiki/Albedo) material similar to deposits found on the floor of [Occator Crater](<https://en.wikipedia.org/wiki/Occator_(crater)>). Image Credit: [NASA](https://en.wikipedia.org/wiki/NASA) / [JPL](https://en.wikipedia.org/wiki/Jet_Propulsion_Laboratory)-[Caltech](https://en.wikipedia.org/wiki/California_Institute_of_Technology) / [UCLA](https://en.wikipedia.org/wiki/University_of_California,_Los_Angeles) / [MPS](https://en.wikipedia.org/wiki/Max_Planck_Institute_for_Solar_System_Research) / [DLR](https://en.wikipedia.org/wiki/German_Aerospace_Center) / [IDA](https://en.wikipedia.org/wiki/International_Dark-Sky_Association) / [Justin Cowart](https://www.flickr.com/people/132160802@N06), October 21, 2015, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ceres](https://www.themissingdocs.net/?p=874) by [Tilps](Gareth_Pearce "Gareth Pearce"), [The Missing Docs.Net](https://www.themissingdocs.net/), January 01, 2021
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GitHub - jniemann66/juddperft: Chess move generation engine](https://github.com/jniemann66/juddperft)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ceres/AUTHORS.txt at main · dje-dev/Ceres · GitHub](https://github.com/dje-dev/Ceres/blob/main/AUTHORS.txt)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Announcing Ceres](https://lczero.org/blog/2021/01/announcing-ceres/) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), January 01, 2021

**[Up one Level](Engines "Engines")**

