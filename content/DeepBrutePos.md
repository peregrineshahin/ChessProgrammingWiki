---
title: DeepBrutePos
---
**[Home](Home "Home") * [Engines](Engines "Engines") * DeepBrutePos**

[](https://vanheusden.com/DeepBrutePos/) DeepBrutePOS Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**DeepBrutePos**,

an experimental chess engine by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), written in [Java](Java "Java"). It is a partial rewrite of [Pos](index.php?title=Pos&action=edit&redlink=1 "Pos (page does not exist)").
Pos was a wild experiment, while DeepBrutePos is a more conventional [brute force](Brute-Force "Brute-Force") [negamax](Negamax "Negamax") with [alpha-beta](Alpha-Beta "Alpha-Beta") program, using [iterative deepening](Iterative_Deepening "Iterative Deepening") with [transposition table](Transposition_Table "Transposition Table") and [quiescence search](Quiescence_Search "Quiescence Search") within a [multithreaded](Parallel_Search "Parallel Search") implementation.
It "talks" both the [XBoard](XBoard "XBoard") and [UCI](UCI "UCI") protocols.

## Puppet Master

Apart from being a regular chess engine, it also includes a "[puppet master](PuppetMaster "PuppetMaster")" mode with which it presents itself as an UCI- or XBoard engine and underneath talks to UCI or XBoard engines running on other systems. For each move it asks them what move to do and then selects the most common suggested one <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## See also

- [Brute-Force](Brute-Force "Brute-Force")
- [PuppetMaster](PuppetMaster "PuppetMaster")

## Forum Posts

- [raspberry pi cluster versus fairymax](http://www.talkchess.com/forum/viewtopic.php?t=49892) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 31, 2013
- [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=41) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014

## External Links

## Chess Engine

- [DeepBrutePOS - An experimental chess program](https://vanheusden.com/DeepBrutePos/)

## Misc

- [Deep from Wikipedia](https://en.wikipedia.org/wiki/Deep)
- [Brute-force search from Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)
- [Poseidon from Wikipedia](https://en.wikipedia.org/wiki/Poseidon)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [DeepBrutePOS - An experimental chess program](https://vanheusden.com/DeepBrutePos/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=41) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014

**[Up one Level](Engines "Engines")**

