---
title: BikJump
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BikJump**

**BikJump**,

an [UCI chess engine](UCI "UCI") written in [C++](Cpp "Cpp") by [Aart Bik](Aart_Bik "Aart Bik"). All source code of BikJump (except the probing and decompression code for the [endgame tablebases](Nalimov_Tablebases "Nalimov Tablebases"), which are used with kind permission of [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") and [Andrew Kadatch](Andrew_Kadatch "Andrew Kadatch")) has been built from the ground up by Aart as a simple after-hours project to gain some experience with chess engine programming and experiment with new ideas.

## Contents

- [1 Features](#features)
- [2 Java Version](#java-version)
- [3 Platforms](#platforms)
- [4 History and Future Plans](#history-and-future-plans)
- [5 External Links](#external-links)

## Features

- [UCI](UCI "UCI") compliant chess engine (runs in e.g. [Chessbase](ChessBase "ChessBase") [Fritz](Fritz "Fritz"), [Chess for Android](Chess_for_Android "Chess for Android"), or [Arena](Arena "Arena") [GUI](GUI "GUI")).
- [Iterative deepening](Iterative_Deepening "Iterative Deepening") with [alpha-beta](Alpha-Beta "Alpha-Beta") pruning and [quiescent search](Quiescence_Search "Quiescence Search").
- [Transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), and tactical extensions.
- Ability to query [Nalimov Endgame Tablebases](Nalimov_Tablebases "Nalimov Tablebases") (3,4,5,6-piece) during search.

## Java Version

A derived [Java](Java "Java") version is used as built-in engine in [Chess for Android](Chess_for_Android "Chess for Android") and [Chess for Glass](Chess_for_Glass "Chess for Glass"). This application also supports the Universal Chess Interface (UCI) and the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") to allow users to play against more powerful third party engines or even play tournaments between engines.

## Platforms

BikJump is available for the following platforms:

- [32-bit Windows](Windows "Windows")
- [64-bit Windows](Windows "Windows")
- [32-bit Linux](Linux "Linux")
- [64-bit Linux](Linux "Linux")
- [64-bit MacOS](Mac_OS "Mac OS")
- [Android](Android "Android")

## History and Future Plans

BikJump was first released In January, 2007. The first generation (v1.x) was based on a [mailbox](Mailbox "Mailbox") representation, and over time increased in strength from about 1750 to 2000 [RUEL](UEL "UEL"). The second and current generation (v2.x), based on a [bitboard](Bitboards "Bitboards") representation, was released in November, 2008. Aart now has started work on "Deep" BikJump, featuring multi-threading to perform the search in parallel (commonly referred to as SMP support). Upcoming versions will be designated with the suffix P (e.g. v2.1P) to denote this new parallel support.

## External Links

- [Aart's Computer Chess Page](http://www.aartbik.com/MISC/chess.html)
- [Aart's Blog](http://aartbik.blogspot.com/).

**[Up one Level](Engines "Engines")**

