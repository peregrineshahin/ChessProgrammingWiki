---
title: GambitVB
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GambitVB**

[](File:GambitVB.PNG) GambitVB [GUI](GUI "GUI"), a [Windows](Windows "Windows") [Forms](https://en.wikipedia.org/wiki/Windows_Forms) collection <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GambitVB**,

a chess program by [Wim Rens](Wim_Rens "Wim Rens") running under the [Windows](Windows "Windows") [.NET framework](https://en.wikipedia.org/wiki/.NET_Framework). GambitVB plays reasonable chess, has an own [GUI](GUI "GUI"), and is [open source](Category:Open_Source "Category:Open Source").
GambitVB is written in [Visual Basic](Basic "Basic") and time critical parts in none [managed](https://en.wikipedia.org/wiki/Managed_code) [C++](Cpp "Cpp"), incorporating old ideas of Wim Rens' earlier commercial program [Gambiet](Gambiet "Gambiet"), as well as old ideas not possible to implement with the hardware of the 80s.
GambitVB is [object-oriented](https://en.wikipedia.org/wiki/Object-orientation), as described elaborately with [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) [class diagrams](https://en.wikipedia.org/wiki/Class_diagram) in a developer guide in [MS Word](https://en.wikipedia.org/wiki/Microsoft_Word) format.
The original GambitVB.info site is no longer available, **VBChess 4.4.rar** is hosted by [Ron Murawski](Ron_Murawski "Ron Murawski") <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
and contains [self-extracting executables](https://en.wikipedia.org/wiki/Self-extracting_archive) for the sources, [pdf](https://en.wikipedia.org/wiki/PDF) and [word document](https://en.wikipedia.org/wiki/Microsoft_Word#File_formats) files.

## Description

GambitVB uses a [10x12 Board](10x12_Board "10x12 Board") to apply [alpha-beta](Alpha-Beta "Alpha-Beta") with [killer heuristic](Killer_Heuristic "Killer Heuristic") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). Since GambitVB v2, the program performs some kind of [best-first](Best-First "Best-First") algorithm and keeps huge parts of the [search tree](Search_Tree "Search Tree") in [memory](Memory "Memory"),
which offers fast access to valuable move tree search informations, missing in the standard [depth-first](Depth-First "Depth-First") approach. This can grow up to millions of [tree nodes](Node "Node") linked to a tree structure, which is still a small fraction of the total search tree.
So called [Score](Score "Score") objects, consisting of a vector of [material balance](Material#Balance "Material") and positional [evaluation](Evaluation "Evaluation") also considering [game phases](Game_Phases "Game Phases"), are used to compare board positions as better, equal, or worse.

## See also

- [Gambiet](Gambiet "Gambiet")

## External Links

- [Native Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:native_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Screenshot from no longr avaibale GambitVB sitde - Last Version - Free game and code
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Native Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:native_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

**[Up one level](Engines "Engines")**

