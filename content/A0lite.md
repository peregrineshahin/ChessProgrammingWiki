---
title: A0lite
---
**[Home](Home "Home") * [Engines](Engines "Engines") * A0lite**

**A0lite**,

a didactic [UCI](UCI "UCI") compliant [neural network](Neural_Networks "Neural Networks") chess engine by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), written in [Python](Python "Python"), released in March 2020 under the permissive [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-1" href="#cite-ref-1">[1]</a> as successor of **LeelaLite**, already announced in October 2018 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
A0lite applies [upper confidence bounds](UCT "UCT") to [Monte-Carlo trees](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), and requires the installation of the [Bad Gyal](index.php?title=Bad_Gyal&action=edit&redlink=1 "Bad Gyal (page does not exist)") [PyTorch](https://en.wikipedia.org/wiki/PyTorch) net evaluator, by default using *MeanGirl-8 (32x4)* net on CPU <a id="cite-note-3" href="#cite-ref-3">[3]</a>. A0lite had its official tournament debut at the [Qualification League](TCEC_Season_19#Fourth "TCEC Season 19") of [TCEC Season 19](TCEC_Season_19 "TCEC Season 19").

## Quotes

[Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe") explained his motivation for writing A0lite on [CCC](CCC "CCC"), Mar 06, 2021 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```
1. Teaching other people how simple it is to write a basic mcts/nn engine with a0lite python.
2. Experimenting with new nn architectures and non-RL training approaches.
3. Combining ab/nnue and mcts/nn in a hybrid approach. (Was a0lite julia, renamed Bender)
4. Reach 3300 ccrl

```

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Maia Chess](Maia_Chess "Maia Chess")

## Forum Posts

- [Leela Lite: A toolkit for experimenting with leela nets in python](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68789) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), October 31, 2018
- [An opponent for humans: Bad Gyal](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71171) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), July 02, 2019
- [Mean Girl 8 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72723) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), January 04, 2020
- [New engine: a0lite](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73495) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), March 28, 2020
- [a0lite problems with badygal configuration etc.](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74088) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 03, 2020
- [Night Nurse 0.2](http://talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), August 19, 2020 » [Igel](Igel "Igel"), [NNUE](NNUE "NNUE")

## External Links

## Engine

- [GitHub - dkappe/a0lite: A neural net chess engine in 95 lines of python](https://github.com/dkappe/a0lite)
- [GitHub - dkappe/badgyal: Simple pytorch net evaluator with Bad Gyal 8 and Mean Girl 8 net included](https://github.com/dkappe/badgyal)
- [GitHub - joergoster/a0lite: A neural net chess engine in 95 lines of python](https://github.com/joergoster/a0lite)
- [GitHub - dkappe/leela_lite: A toolkit for experimenting with UCT and Leela Chess nets in Python](https://github.com/dkappe/leela_lite) (predecessor of A0lite)

## Misc

- [A0 from Wikipedia](https://en.wikipedia.org/wiki/A0)
- [Lite from Wikipedia](https://en.wikipedia.org/wiki/Lite)
- [lite - Wiktionary](https://en.wiktionary.org/wiki/lite)
- [Bad Gyal from Wikipedia](https://en.wikipedia.org/wiki/Bad_Gyal)
- [Status Quo](<https://en.wikipedia.org/wiki/Status_Quo_(band)>) - [Mean Girl](https://en.wikipedia.org/wiki/Mean_Girl) (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [New engine: a0lite](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73495) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), March 28, 2020
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Leela Lite: A toolkit for experimenting with leela nets in python](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68789) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), October 31, 2018
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [a0lite/README.md at master · dkappe/a0lite · GitHub](https://github.com/dkappe/a0lite/blob/master/README.md)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Your motivation for writing a chess engine?](http://talkchess.com/forum3/viewtopic.php?f=2&t=76787) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), Mar 06, 2021

**[Up one Level](Engines "Engines")**

