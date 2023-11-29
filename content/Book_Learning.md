---
title: Book Learning
---
**[Home](Home "Home") * [Learning](Learning "Learning") * Book Learning**

\[ Book Learning <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Book Learning**,

is a technique of unsupervised [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") motivated by basic requirements for successfully playing a sequence of games, such as avoiding losing games in the same way from certain lines from the [opening book](Opening_Book "Opening Book"), or to recognize its own strong points and guide the engine into positions it does well.

Unsupervised reinforcement learning is characterized by [trial and error](Trial_and_Error "Trial and Error") and feeding back reinforcement signals, in this context to modify move probabilities or to add new book moves. The signals are either based on the final outcome of the game, called result-driven learning, and/or by [search-driven](Search "Search") learning, i.e. from the [score](Score "Score") and trend of first few searches after leaving the book to determine how the program likes the position <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Chess Engines

## Crafty

[Robert Hyatt](Robert_Hyatt "Robert Hyatt") on Book learning in [Crafty](Crafty "Crafty") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

- `Crafty does two kinds of 'book learning'. Result learning sound just like what you are doing. If it loses a game, it won't play the last book move it played ever again. And this gets backed up several moves back as well to get it out of bad lines quickly.`
- `Normal book learning uses the first ten non-book moves (search results) to determine the 'trend' of the game. This trend score is then used to adjust the book move that was played in this game...`

Both are on by default... and further <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

1. `Crafty remembers the evaluations for the first 10 moves out of book, after each search has been completed. It uses these evaluations to detect a "trend". IE is the evaluation good and getting better? Is it bad and getting worse? Is it good but dropping (ie it grabbed a gambit pawn and is beginning to see that it was bad) or is it bad but getting better (IE it offered a gambit, the opponent took it, and the score is going up). It factors all of that together and marks the book line as good or bad.`
1. `Crafty takes the result of a game when it loses, and updates the book line so that moves tried near the end of the line simply don't get played, and alternatives near the front of the book line get tried next.`
1. `There is more to it than that, and you can look at the crafty.doc file <a id="cite-note-5" href="#cite-ref-5">[5]</a> to at least see what I am doing in more detail. It is **very** effective.`

## MChess

[Marty Hirsch](Marty_Hirsch "Marty Hirsch") in [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") on machine learning in [MChess Pro](MChess "MChess"), excerpt <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```C++Some sets of heuristics are employed to decide which moves to add to the opening book, and which to delete from it. Moves are deleted when the score just out of book is not too high, and the score later in the game is worse. Moves are added when the score just out of book is not too low, and the score later in the game is satisfactory. A further pre-condition for moves that may be added to the opening book is that the increase in score has been mainly monotonic. If this condition is not met, a future game may enable better moves to be found due to the general learning. In other words, only the best moves the program is able to discover (at a given level) are added to the opening book. Different thresholds are applied for the storage and deletion of moves for White and Black. 
...
Some programs now support a different type of book learning in which no moves are added to the book, but instead, unsuccessful moves are given a lower probability of selection. This approach narrows the book over the time and may optimize the results against a specific opponent, at the expense of the results against other opponents. The book learning described in this paper maintains the opening book variety and improves the book against multiple opponents. 

```

## RomiChess

As explained by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [RomiChess](RomiChess "RomiChess") applies [Monkey see Monkey do](https://en.wikipedia.org/wiki/Monkey_see,_monkey_do) [mimicry](https://en.wikipedia.org/wiki/Mimicry) to learn book lines <a id="cite-note-7" href="#cite-ref-7">[7]</a> :

```C++Romi remembers and incorporates winning lines regardless of which side played the moves into the [opening book](Opening_Book "Opening Book") and can play them back instantly up to 180 [ply](Ply "Ply") if the stats for that line remain good. 

```

## See also

- [Brainfish](Brainfish "Brainfish")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Opening Book](Opening_Book "Opening Book")
- [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
- [PolyGlot](PolyGlot "PolyGlot")
- [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
- [Trial and Error](Trial_and_Error "Trial and Error")

## Selected Publications

- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959
- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://researcher.watson.ibm.com/researcher/files/us-beygel/samuel-checkers.pdf)
- [Michael Byrne](Michael_Byrne "Michael Byrne") (**1996**). *M-Chess Pro 5.0 Book Learning Feature*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, Nos. 3+4, p. 85 » [MChess](MChess "MChess")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Book Learning - a Methodology to Tune an Opening Book Automatically](http://www.craftychess.com/hyatt/learning.html)*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")
- [Michael Buro](Michael_Buro "Michael Buro") (**1999**). *Toward Opening Book Learning.* [ICCA Journal, Vol. 22, No. 2](ICGA_Journal#22_2 "ICGA Journal"), [pdf](https://skatgame.net/mburo/ps/book.pdf) <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**) *Machine Learning in Games: A Survey*. Austrian Research Institute for Artificial Intelligence, Technical Report OEFAI-TR-2000-3, [pdf](http://www.ofai.at/cgi-bin/get-tr?download=1&paper=oefai-tr-2000-31.pdf) - Chapter 2, Book Learning
- [Marty Hirsch](Marty_Hirsch "Marty Hirsch") (**2001**). *Machine Learning in MChess Professional* - [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Marek Strejczek](Marek_Strejczek "Marek Strejczek") (**2004**). *Some aspects of chess programming*. M.Sc. thesis, [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź"), 4.2 Experiments with book learning
- [Thomas Widjaja](index.php?title=Thomas_Widjaja&action=edit&redlink=1 "Thomas Widjaja (page does not exist)") (**2004**). *Knowledge Engineering und Lernen in Spielen - Opening Book Learning*. [slides as pdf](http://www.ke.tu-darmstadt.de/lehre/archiv/ss04/se-spiele/OpeningBookLearning.pdf) (German)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2006**). *[Innovative Opening-Book Handling](http://www.springerlink.com/content/b01701g6kx317574/)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/publications/icga_open_springer.pdf)

## Forum Posts

## 1998 ...

- [Book learning and rating bias](https://www.stmintz.com/ccc/index.php?id=17861) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 01, 1998
- [BookLearning Under the Microscope!!!](https://www.stmintz.com/ccc/index.php?id=25754) by Robert Henry Durrett, [CCC](CCC "CCC"), August 31, 1998
- [Book learning?](https://www.stmintz.com/ccc/index.php?id=37968) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), December 31, 1998
- [Book learning](https://www.stmintz.com/ccc/index.php?id=68359) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), September 12, 1999

## 2000 ...

- [Opening book learning](https://www.stmintz.com/ccc/index.php?id=135774) by Gordon Rattray, [CCC](CCC "CCC"), October 31, 2000
- [What information to store in book learning?](https://www.stmintz.com/ccc/index.php?id=147500) by [Christian Söderström](Christian_S%C3%B6derstr%C3%B6m "Christian Söderström"), [CCC](CCC "CCC"), January 02, 2001
- [question about opening book and learning](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37030) by [Uri Blass](Uri_Blass "Uri Blass"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 26, 2002
- [question about book and learning](https://www.stmintz.com/ccc/index.php?id=226258) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 26, 2002
- [Shredder and Engine Book Learning](https://www.stmintz.com/ccc/index.php?id=294486) by [Stephen Ham](index.php?title=Stephen_Ham&action=edit&redlink=1 "Stephen Ham (page does not exist)"), [CCC](CCC "CCC"), April 24, 2003 » [Shredder](Shredder "Shredder")
- [A simple book learning method](http://www.talkchess.com/forum/viewtopic.php?t=21754) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), June 12, 2008 » [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")

## 2010 ...

- [Computer based Opening theory](http://talkchess.com/forum/viewtopic.php?t=50662) by Lucas Braesch, [CCC](CCC "CCC"), December 28, 2013
- [Re: Computer based Opening theory](http://talkchess.com/forum/viewtopic.php?t=50662&start=16) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), December 28, 2013
- [Anybody tried Logistello's book learning for chess?](http://www.talkchess.com/forum/viewtopic.php?t=50680) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), December 29, 2013
- [Position learning and opening books](http://www.talkchess.com/forum/viewtopic.php?t=56313) by Forrest Hoch, [CCC](CCC "CCC"), May 11, 2015
- [Polyglot book learning](http://www.talkchess.com/forum/viewtopic.php?t=61210) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), August 24, 2016 » [PolyGlot](PolyGlot "PolyGlot")
- [Cumulative building of a shared search tree](http://www.talkchess.com/forum/viewtopic.php?t=62639) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), December 28, 2016 » [Chinese Chess](Chinese_Chess "Chinese Chess"), [Opening Book](Opening_Book "Opening Book"), [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")

## External Links

- [Stanley Clarke](Category:Stanley_Clarke "Category:Stanley Clarke") - [School Days](<https://en.wikipedia.org/wiki/School_Days_(album)>) (1976), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> France in 2000 year (XXI century). Future school. France, paper card, A reproduction of the early 20th century, scan, [Learning from Wikipedia](https://en.wikipedia.org/wiki/Learning)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Book Learning - a Methodology to Tune an Opening Book Automatically](http://www.craftychess.com/hyatt/learning.html)*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Book learning](https://www.stmintz.com/ccc/index.php?id=68381) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 12, 1999
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: questions about book learning](https://www.stmintz.com/ccc/index.php?id=340060) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 03, 2004
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Crafty Documentation](http://www.craftychess.com/hyatt/craftydoc.html)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Marty Hirsch](Marty_Hirsch "Marty Hirsch") (**2001**). *Machine Learning in MChess Professional* - [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), pp. 133-142, 135
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062&start=15) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 18, 2010
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Anybody tried Logistello's book learning for chess?](http://www.talkchess.com/forum/viewtopic.php?t=50680) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), December 29, 2013

**[Up one Level](Learning "Learning")**

