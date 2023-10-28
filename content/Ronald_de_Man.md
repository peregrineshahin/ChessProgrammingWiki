---
title: Ronald de Man
---
**[Home](Home "Home") \* [People](People "People") \* Ronald de Man**


**Ronald de Man**, [alias](https://en.wikipedia.org/wiki/Alias) [Syzygy](https://en.wikipedia.org/wiki/Syzygy),  

a Dutch mathematician, computer scientist and IP lawyer, in the 90s researcher at [Eindhoven University of Technology](https://en.wikipedia.org/wiki/Eindhoven_University_of_Technology), competitor at the [International Mathematical Olympiad](https://en.wikipedia.org/wiki/International_Mathematical_Olympiad) 1990, winning the Silver medal <a id="cite-note-1" href="#cite-ref-1">[1]</a> , and the [ACM International Collegiate Programming Contest](https://en.wikipedia.org/wiki/ACM_International_Collegiate_Programming_Contest) 1995, to win Bronze within the *ARoMA* team from [Delft University of Technology](Delft_University_of_Technology "Delft University of Technology") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> . He is co-developer of the [Linux](Linux "Linux") [desktop environment](https://en.wikipedia.org/wiki/Desktop_environment) and [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface) [GNOME](https://en.wikipedia.org/wiki/GNOME) <a id="cite-note-4" href="#cite-ref-4">[4]</a> , and as chess programmer author of the chess and [Antichess](Losing_Chess "Losing Chess") <a id="cite-note-5" href="#cite-ref-5">[5]</a> playing program [Sjaak](Sjaak "Sjaak"), which plays at [FICS](index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") under the handle *TrojanKnight* <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>. He ported [Stockfish](Stockfish "Stockfish") to plain [C](C "C"), dubbed [CFish](CFish "CFish"), and to [Rust](Rust "Rust") as [Rustfish](Rustfish "Rustfish").




### Contents


* [1 Scoring Root Moves](#scoring-root-moves)
* [2 Bloom Filter](#bloom-filter)
* [3 Syzygy Bases](#syzygy-bases)
* [4 Selected Publications](#selected-publications)
* [5 Forum Posts](#forum-posts)
	+ [5.1 1995 ...](#1995-...)
	+ [5.2 2010 ...](#2010-...)
* [6 External Links](#external-links)
* [7 References](#references)






Ronald de Man proposed a method to apply [randomness](Search_with_Random_Leaf_Values "Search with Random Leaf Values") <a id="cite-note-9" href="#cite-ref-9">[9]</a> and/or bonuses, i.e. developing bonus, or penalties suggested by an [oracle](Oracle "Oracle"), in [scoring](Score "Score") [moves](Moves "Moves") at the [root](Root "Root") without any changes in [alpha-beta search](Alpha-Beta "Alpha-Beta") or [leaf evaluation](Evaluation "Evaluation"), and without any problems with the [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-10" href="#cite-ref-10">[10]</a>:




```
First of all, don't worry, it is possible. But you should not try to pass the bonus to the tip nodes. That would indeed give hash problems. The solution is to not change anything in your Search() procedure. That already solves all potential hash problems. You just add the bonus AFTER Search() has returned a value for a particular root move. So that would be done in your SearchRoot(). What you basically do there is change every occurrence of 

```


```
value = -Search(-beta, -alpha,...)
in
value = bonus[n] - Search(bonus[n]-beta, bonus[n]-alpha,...)

```


```
where bonus[n] is the development bonus value for the move you are currently searching. It is all very natural when you think about it. You should consider Search() as a black box. You give it some numbers alpha and beta, and Search() gives you a number x, with the properties that, relative to the real value v of this move,

```


```
1. If v <= alpha, then x <= alpha,
2. If v >= beta, then x >= beta,
3. If alpha < v < beta, then x = v.

```


```
If you search a move, you want to know if its real value + bonus[n] is bigger than alpha. So you want to know if its real value is bigger than alpha-bonus[n]. So you give Search() the bounds alpha-bonus[n] and beta-bonus[n], and add bonus[n] to the result. And you do this in SearchRoot().

```


```
So no fudging with hash table scores whatsoever!

```


```
Of course this trick gives all kinds of possibilities. Not only can you stimulate development, or add in some randomization. It is also easy to solve the 'underpromotion' problem: to prevent the program from under-promoting to a rook (in situations where the piece will probably be captured the next move anyway), you give underpromotion moves a penalty. Or in trivially drawn endgames like KRKR you give captures a bonus. Or in not-so-trivially drawn endgames for which tablebases give draw values you give moves that give away a piece (but do not change the outcome) a penalty, hoping that the opponent will make a fatal mistake further on in the game :-)

```


```
Ronald de Man 

```

## Bloom Filter


Ronald de Man revealed the trick to speed up [repetition detection](Repetitions "Repetitions") with a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter), implemented as a small [hash table](Hash_Table "Hash Table") indexed by some lower bits of the hash-key, to increment a counter while entering and decrement the counter while leaving a node <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> .



## Syzygy Bases


In April 2013, Ronald de Man published his [Syzygy Bases](Syzygy_Bases "Syzygy Bases") <a id="cite-note-13" href="#cite-ref-13">[13]</a> , a compact [endgame tablebase](Endgame_Tablebases "Endgame Tablebases") of up to six pieces. It consist of two sets of files, **WDL** files storing win/draw/loss information considering the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule"), for access during search, and **DTZ** files with [distance-to-zero](Endgame_Tablebases#DTZ "Endgame Tablebases") information for access at the [root](Root "Root") <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a> .



## Selected Publications


<a id="cite-note-16" href="#cite-ref-16">[16]</a>



* Ronald de Man (**1995**). *[On Composants of Solenoids](http://www.ams.org/journals/era/1995-01-02/S1079-6762-95-02005-1/home.html)*. [Fundamenta Mathematicae](https://en.wikipedia.org/wiki/Fundamenta_Mathematicae) 147, [pdf](http://matwbn.icm.edu.pl/ksiazki/fm/fm147/fm14726.pdf) <a id="cite-note-17" href="#cite-ref-17">[17]</a>
* Ronald de Man (**1999**). *[The Generating Function for the Number of Roots of a Coxeter Group](http://dl.acm.org/citation.cfm?id=312392)*. [Journal of Symbolic Computation, Vol. 27, No.6](http://www.informatik.uni-trier.de/~ley/db/journals/jsc/jsc27.html#Man99) <a id="cite-note-18" href="#cite-ref-18">[18]</a>
* [Richa Malhotra](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Malhotra:Richa.html), [Ronald van Haalen](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/h/Haalen:Ronald_van.html), Ronald de Man, [Michiel van Everdingen](http://nl.linkedin.com/in/michielvaneverdingen) (**2003**) *[Managing service-level agreements in metro ethernet networks using backpressure](http://onlinelibrary.wiley.com/doi/10.1002/bltj.10065/abstract)*. [Bell Labs Technical Journal, Vol. 8, No. 2](http://www.informatik.uni-trier.de/~ley/db/journals/bell/bell8.html#MalhotraHME03) <a id="cite-note-19" href="#cite-ref-19">[19]</a> .


## Forum Posts


### 1995 ...


* [Re: random play](http://groups.google.com/group/rec.games.chess.computer/msg/a30577d2a7a74a51) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 28, 1996 <a id="cite-note-20" href="#cite-ref-20">[20]</a>
* [Re: Hash functions for use with a transition table](http://groups.google.com/group/rec.games.chess.computer/msg/9b240379394bc968) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 7, 1997 » [BCH Hashing](BCH_Hashing "BCH Hashing")
* [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997 » [Oracle](Oracle "Oracle")
* [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
* [Re: triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b/d8f8d6ee1b252b86) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 27, 1997


### 2010 ...


* [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by Ronald de Man, [CCC](CCC "CCC"), April 01, 2013 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [tablebase caching / mmap() / page cache](http://www.talkchess.com/forum/viewtopic.php?t=49702) by Ronald de Man, [CCC](CCC "CCC"), October 13, 2013 » [Memory](Memory "Memory"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Question to syzygy author](http://www.talkchess.com/forum/viewtopic.php?t=59947) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 24, 2016
* [tablebase compression / academic integrity](http://www.talkchess.com/forum/viewtopic.php?t=60222) by Ronald de Man, [CCC](CCC "CCC"), May 19, 2016 <a id="cite-note-21" href="#cite-ref-21">[21]</a>
* [pin-aware see](https://groups.google.com/d/msg/fishcooking/S_4E_Xs5HaE/mS3VTnuEFgAJ) by Ronald de Man, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2016 » [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), [Pin](Pin "Pin"), [Stockfish](Stockfish "Stockfish")
* [DTM50](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67536) by Ronald de Man, [CCC](CCC "CCC"), May 22, 2018


## External Links


* [syzygy1 · GitHub](https://github.com/syzygy1)
* [GitHub - syzygy1/tb](https://github.com/syzygy1/tb) » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [GitHub - syzygy1/Cfish: C port of Stockfish](https://github.com/syzygy1/Cfish) » [CFish](CFish "CFish")
* [Syzygy from Wikipedia](https://en.wikipedia.org/wiki/Syzygy)


 [Syzygy (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy_%28mathematics%29)
* [ICGA: Losing Chess](http://icga.leidenuniv.nl/icga/games/losingchess/) by [Guy Haworth](Guy_Haworth "Guy Haworth")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [International Mathematical Olympiad - Ronald de Man](http://www.imo-official.org/participant_r.aspx?id=2462)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> ['Programmeren hoef je niet te kunnen' - TU Delta - Weekblad van de Technische Universiteit Delft](http://www.delta.tudelft.nl/artikel/-programmeren-hoef-je-niet-te-kunnen/10155), March 16, 1995 (Dutch)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [ACM Programming Contest World Finals](http://icpc.baylor.edu/past/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [gnome-libs-32bit-1.4.2-11.1.x86\_64 RPM](http://rpmfind.net/linux/RPM/opensuse/11.1/x86_64/gnome-libs-32bit-1.4.2-11.1.x86_64.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ICGA: Losing Chess](http://ilk.uvt.nl/icga/games/losingchess/) by [Guy Haworth](Guy_Haworth "Guy Haworth")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Statistics for TrojanKnight(C)](http://www.nicklong.net/chess/atomic/mewis/trojanknight.txt)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: AEGON 97/ 1st round: HIARCS lost](http://groups.google.com/group/rec.games.chess.computer/msg/6bb58a0605f7e2f1) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 25 1997
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [FICS Statistics - April 2004, Best Ratings - Computer List](http://poincare.matf.bg.ac.rs/~andrew/suicide/fics/en0404C.htm)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: random play](https://groups.google.com/d/msg/rec.games.chess.computer/AI3xadkLEIk/UUqnp9J3BaMJ) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 28, 1996
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: computer chess "oracle" ideas...](https://groups.google.com/d/msg/rec.games.chess.computer/me7GkjsEgds/iC_ZJm5UwswJ) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997, see also [Re: mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=390268) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 04, 2004 » [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [Null Move](Null_Move_Pruning "Null Move Pruning") and [WAC](Win_at_Chess "Win at Chess") booster
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Re: triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b/d8f8d6ee1b252b86) by Ronald de Man, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 27, 1997
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Re: New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681&start=45) by Ronald de Man, [CCC](CCC "CCC"), April 10, 2013
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by Ronald de Man, [CCC](CCC "CCC"), April 01, 2013
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [syzygy1/tb · GitHub](https://github.com/syzygy1/tb) by Ronald de Man
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [DBLP: Ronald de Man](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Man:Ronald_de.html)
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Solenoidal vector field from Wikipedia](https://en.wikipedia.org/wiki/Solenoidal_vector_field)
18. <a id="cite-ref-18" href="#cite-note-18">[18]</a> [Coxeter group from Wikipedia](https://en.wikipedia.org/wiki/Coxeter_group)
19. <a id="cite-ref-19" href="#cite-note-19">[19]</a> [Metro Ethernet from Wikipedia](https://en.wikipedia.org/wiki/Metro_Ethernet)
20. <a id="cite-ref-20" href="#cite-note-20">[20]</a> [Randomness in move selection](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ba5f8759ec0ce454) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 01, 1996
21. <a id="cite-ref-21" href="#cite-note-21">[21]</a> [Victor Zakharov](Victor_Zakharov "Victor Zakharov"), [Michael G. Malkovsky](Michael_G._Malkovsky "Michael G. Malkovsky"), [Vladislav Y. Shchukin](Vladislav_Y._Shchukin "Vladislav Y. Shchukin") (**2016**). *[Compression of underdetermined data in a 7-piece chess table](http://link.springer.com/article/10.3103%2FS0278641916010076)*. [Moscow University Computational Mathematics and Cybernetics](http://www.springer.com/mathematics/journal/11968), Vol. 40, No. 1

**[Up one level](People "People")**







 
