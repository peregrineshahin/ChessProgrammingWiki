---
title: CAPS
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CAPS**

\[ Spherical Cap <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CAPS**, (Chess as Problem Solving, CAPS-II)

[Hans Berliner's](Hans_Berliner "Hans Berliner") experimental chess program which was subject of his 1974 Ph.D. thesis *Chess as Problem Solving: The Development of a Tactics Analyser* at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, further eloborated at the [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1") conference <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and, along with [B\*](B* "B*"), in a Panel on Computer Game Playing <a id="cite-note-4" href="#cite-ref-4">[4]</a>. CAPS is a [selective](Selectivity "Selectivity"), [knowledge](Knowledge "Knowledge") driven [depth-first](Depth-First "Depth-First") [alpha-beta](Alpha-Beta "Alpha-Beta") searcher in the domain of [chess tactics](Tactics "Tactics"). A [position](Chess_Position "Chess Position") is represented as [vector](Array "Array") of 1040 words of information, including the [list](Move_List "Move List") of [generated](Move_Generation "Move Generation") [pseudo-legal moves](Pseudo-Legal_Move "Pseudo-Legal Move"), kept on a [stack](Stack "Stack") of up to 20 [ply](Ply "Ply").

## Contents

- [1 CAPS-II](#caps-ii)
- [2 Refutation Description](#refutation-description)
- [3 Causality Facility](#causality-facility)
- [4 Method of Analogies](#method-of-analogies)
- [5 Quotes](#quotes)
- [6 See also](#see-also)
- [7 Publications](#publications)
- [8 Forum Posts](#forum-posts)
- [9 External Links](#external-links)
  - [9.1 Caps](#caps)
  - [9.2 Cap](#cap)
- [10 References](#references)

## CAPS-II

**CAPS-II** was tested on many middle-game chess tactics problems from standard textbooks on chess. It played a few complete games of chess. In both these modes it ran with a maximum depth of 10 ply. CAPS-II did not do too well in the games, since it had little positional knowledge, and more importantly the tactics mechanisms were still not completed, causing it to make occasional blunders which would wipe out whatever good it had achieved earlier. However, it did quite well on the tactics problems such as [Reinfeld's](https://en.wikipedia.org/wiki/Fred_Reinfeld) [Win at Chess](Win_at_Chess "Win at Chess") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Refutation Description

While visiting a [node](Node "Node"), CAPS determines [attack information](Attack_and_Defend_Maps "Attack and Defend Maps"), and whether [pieces](Pieces "Pieces") are completely or partial [en prise](En_prise "En prise") or overprotected, are [pinned](Pin "Pin"), or may be source of a [discovered attack](Discovered_Attack "Discovered Attack"), and further collects a so called **Refutation Description** of expandable sets ([bitboards](Bitboards "Bitboards") and [piece-sets](Piece-Sets "Piece-Sets")) of moving and captured [pieces](Pieces "Pieces"), their [source-](Origin_Square "Origin Square") and [target squares](Target_Square "Target Square"), and appropriate paths of [sliding pieces](Sliding_Pieces "Sliding Pieces") involved, associated with the full qualified [moves](Moves "Moves") (piece, from, to, captured piece if any) along the current search line. The description of the six sets of the Refutation Description is given from the [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1") paper <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

- **RPCS** - `is a bit-vector which has bits representing names of pieces. The name bit <code>of the piece that moved to produce this node is set in this vector.`
- **RSQS** - `is a bit-vector with bits representing squares on the board. The bit corresponding to the destination square of the move that produced this node is set in RSQS.`
- **RPATH** - `is a bit-vector with bits representing squares on the board. The bit for any square across which a sliding piece moved in making the made move is set in RPATH. If the move was a non-capture pawn move, then all squares over which it passed including the destination also have bits set for them.`
- **RTGTS** - `is a bit-vector with bits representing names of targets. A comparison is made of BEST for this node with BEST one ply previously. Any squares which are now named as containing material targets, but were not mentioned in the previous BEST, have bits set for the name of the piece on this square to indicate that this threat was created by the last move.`
- **TGTSQS** - `is a bit-vector with bits representing squares on the board. For any RTGTS detected as above, bits are set in TGTSQS for the corresponding squares.`
- **TPATH** - `is a bit-vector with bits representing squares on the board. For any TGTSQS detected as above, if a piece that has an ATTACKING function on this square is a sliding piece, then all the intervening squares have bits set for them in TPATH.`

## Causality Facility

While classical depth-first searchers may perform the [killer heuristic](Killer_Heuristic "Killer Heuristic"), or may analyze the backed-up [principal variation](Principal_Variation "Principal Variation") for refutations, i.e. to move or defend any captured piece, or capture or pin any capturer, or block the path of any moving piece, CAPS' refutation description allows for much more complete understanding of a set of consequences, not only restricted to the PV. The **Causality Facility** interprets the refutation descriptions and tries to determine tactical causes and goals to control a set of move generators for possible goal transitions, and allows [pruning](Pruning "Pruning") of large sub-trees. The facility may further execute a [null move](Null_Move "Null Move") to determine whether a suspected move was responsible for a bad position or not.

## Method of Analogies

Once a move was determined as in fact bad, it is possible to posit a [Lemma](https://en.wikipedia.org/wiki/Lemma_%28mathematics%29) along with its environment of the refutation description — this being knowledge that a certain move will be bad as long as the described environment does not change. With this knowledge, any proposed move may be looked up in the Lemma file and if it has been previously cataloged, the program may determine if the current position contains any essential changes from the Lemma environment which might make the move succeed. It is important to note that should it be decided to try the move, and should it again fail, that it would now be possible to generalize the Lemma to include the union of the two environments, thus making it stronger. In a somewhat similar way, it is possible to generalize about the movements of a single piece, if more than one Lemma exists with respect to its moves. Lemmas are also posited about winning moves. Whenever a move is suggested at some future point in the search, the lemma file is first examined to determine if a lemma exists about this move and if the partial board description matches. If so, the result of the move is assumed known and the search can be foregone. A similar system has been described by [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") and [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Quotes

[Hans Berliner](Hans_Berliner "Hans Berliner") on CAPS-II in his Oral History, March 2005 <a id="cite-note-9" href="#cite-ref-9">[9]</a>:

```C++
And here we are in 1970 and the [Northwestern](Northwestern_University "Northwestern University") people have just made a big splash and everybody realized that they were very, very good and that they were not the kind to rest on their laurels, they kept finding things to improve. Now I was at [Carnegie-Mellon](Carnegie_Mellon_University "Carnegie Mellon University") where I had been admitted at the age of 40, not because of any academic credentials but because I knew how to do chess and I’d already written a computer program and they had hopes that I could push this state of the art doing computer chess, which I tried to do. But my program was not in the style of these modern programs, it was a program based on conceptual things and it was a very - a lot of effort was devoted to structure; in other words every position had a lot of structure and there were programs that delineated the structure ... 

```

```C++
There was one thing in this dissertation that I’m proud of and that was something that I called ‘the causality facility’ and - this is a dead end though I have to say that ahead of time, it was a dead end but it was a nice one - and the idea was that when, lets say, a human being makes a certain move and then a rook comes down to the back rank and says ‘checkmate’ the human being says ‘oh I gotta do something about that, I can’t make a move over here and he’s gonna give me checkmate.’ And I was once having a conversation with [Minsky](Marvin_Minsky "Marvin Minsky") and he said you know ‘how do humans do this and why don’t machines do this?’ 

```

```C++
So I started thinking about that and when I did my dissertation I had descriptions - as I said I had a lot of structure - and I dragged descriptions back as one backed up from some terminal node and you backed the value not only do you back the value up, you’re backing up a description and the description said which pieces moved where and - and some other information. So in other words at some point you would arrive at the point where you say ‘oh, this last move must have been a mistake because I got checkmated’ and then you look at this description and see what the opponent did and say ‘oh probably I will lose again the same way unless I do something about that description’ which meant you either had to capture the piece that’s doing the moving or you had to block it or guard the square on which it landed or something like that. And that’s what my program was able to do, and it did so me very nice clever things where something was being threatened and it figured out the only way to block it without trying everything, by just reasoning about what the characteristics of a move would have to be in order to prevent this, so it was doing - it was good Ph.D. work but it didn’t fit into the main scheme <laughing>. Well I think as a knowledge exercise it was good. 

```

## See also

- [Paradise](Paradise "Paradise")

## Publications

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1973**). *Some Necessary Conditions for a Master Chess Program.* [3. IJCAI 1973](http://dblp.uni-trier.de/db/conf/ijcai/ijcai73.html)
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1974**). *Chess as Problem Solving: The Development of a Tactics Analyser*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *A Representation and Some Mechanisms for a Problem-Solving Chess Program.* [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
- [Hans Berliner](Hans_Berliner "Hans Berliner"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat"), [Arthur Samuel](Arthur_Samuel "Arthur Samuel"), [David Slate](David_Slate "David Slate") (**1977**). *Panel on Computer Game Playing*. 975-982 [5. IJCAI 1977](http://www.sigmod.org/dblp/db/conf/ijcai/ijcai77.html#BerlinerGPSS77), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-77-VOL2/PDF/087.pdf)
- Editor (**1979**). *Chess Ratings from Problem Solving*. [Personal Computing, Vol. 3, No. 12](Personal_Computing#3_12 "Personal Computing"), pp. 77 » [Chess Problems, Compositions and Studies](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies")

## Forum Posts

- [Re: Method of Analogies??](https://www.stmintz.com/ccc/index.php?id=19484) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 29, 1998
- [Re: Symbolic: Status Report 2007.04.25](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=114428&t=13382) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 26, 2007 » [Symbolic](Symbolic "Symbolic")

## External Links

## Caps

- [Caps (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Caps)
- [CAPS entreprise - many-core programming](http://www.caps-entreprise.com/)
- [Caps lock from Wikipedia](https://en.wikipedia.org/wiki/Caps_lock)
- [Calcyphosin (CAPS gene) from Wikipedia](https://en.wikipedia.org/wiki/Calcyphosin)
- [Computer Animation Production System - Wikipedia](https://en.wikipedia.org/wiki/Computer_Animation_Production_System)
- [Java Caps from Wikipedia](https://en.wikipedia.org/wiki/Java_Caps) » [Java](Java "Java")
- [Problem solving from Wikipedia](https://en.wikipedia.org/wiki/Problem_solving)

## Cap

- [Cap (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cap_%28disambiguation%29)
- [Cap from Wikipedia](https://en.wikipedia.org/wiki/Cap)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> An example of a spherical cap by [Pbroks13](https://commons.wikimedia.org/wiki/User:Pbroks13), October 2008, [Spherical cap from Wikipedia](https://en.wikipedia.org/wiki/Spherical_cap)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1974**). *Chess as Problem Solving: The Development of a Tactics Analyser*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *A Representation and Some Mechanisms for a Problem-Solving Chess Program.* [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Hans Berliner](Hans_Berliner "Hans Berliner"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat"), [Arthur Samuel](Arthur_Samuel "Arthur Samuel"), [David Slate](David_Slate "David Slate") (**1977**). *Panel on Computer Game Playing*. 975-982 [5. IJCAI 1977](http://www.sigmod.org/dblp/db/conf/ijcai/ijcai77.html#BerlinerGPSS77), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-77-VOL2/PDF/087.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *A Representation and Some Mechanisms for a Problem-Solving Chess Program.* [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *A Representation and Some Mechanisms for a Problem-Solving Chess Program.* [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1975**). *Some Methods of Controlling the Tree Search in Chess Programs*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp. 361-371. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") pp. 129-135
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Method of Analogies??](https://www.stmintz.com/ccc/index.php?id=19469) by Bruce Cleaver, [CCC](CCC "CCC"), May 29, 1998
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Oral History of Hans Berliner](http://www.computerhistory.org/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/index.php?iid=orl-43343bb768f00), Interviewed by: [Gardner Hendrie](http://www.computerhistory.org/trustee/gardner-hendrie), Recorded: March 7, 2005, [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/berliner.oral_history_transcript.2005.103630824.pdf), pp. 25.

**[Up one Level](Engines "Engines")**

