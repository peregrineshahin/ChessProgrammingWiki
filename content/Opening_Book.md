---
title: Opening Book
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* Opening Book**



 [](https://en.wikipedia.org/wiki/File:Modern_Chess_Openings_Second_Edition.jpg) [Modern Chess Openings](https://en.wikipedia.org/wiki/Modern_Chess_Openings) [[1]](#cite_note-1) 
Chess programs often look up the positions at the [beginning of the game](Opening "Opening") in an **Opening Book**. The opening database can then be used as long as the opponent plays a new move from the database, so usually more common opening lines will be stored to a much higher depth than the uncommon ones. As soon as the program is "out of book" it has to continue using the normal search routines. 



### Contents


* [1 Purposes](#Purposes)
* [2 Types](#Types)
	+ [2.1 Text](#Text)
	+ [2.2 Binary](#Binary)
* [3 Generation](#Generation)
	+ [3.1 Handcrafted](#Handcrafted)
	+ [3.2 From game collection](#From_game_collection)
	+ [3.3 By computing](#By_computing)
* [4 Book Building Tools](#Book_Building_Tools)
* [5 Book Playing](#Book_Playing)
* [6 Quotes](#Quotes)
* [7 Formats](#Formats)
* [8 Classification of Chess Openings](#Classification_of_Chess_Openings)
* [9 Book Issues](#Book_Issues)
* [10 See also](#See_also)
* [11 Selected Publications](#Selected_Publications)
	+ [11.1 1974 ...](#1974_...)
	+ [11.2 1980 ...](#1980_...)
	+ [11.3 1990 ...](#1990_...)
	+ [11.4 2000 ...](#2000_...)
	+ [11.5 2005 ...](#2005_...)
	+ [11.6 2010 ...](#2010_...)
	+ [11.7 2015 ...](#2015_...)
* [12 Forum Posts](#Forum_Posts)
	+ [12.1 1990 ...](#1990_..._2)
	+ [12.2 1995 ...](#1995_...)
	+ [12.3 2000 ...](#2000_..._2)
	+ [12.4 2005 ...](#2005_..._2)
	+ [12.5 2010 ...](#2010_..._2)
	+ [12.6 2015 ...](#2015_..._2)
	+ [12.7 2020 ...](#2020_...)
* [13 External Links](#External_Links)
	+ [13.1 Engine Books](#Engine_Books)
	+ [13.2 Online Opening Tree](#Online_Opening_Tree)
	+ [13.3 Misc](#Misc)
* [14 References](#References)






* Save time: Chess programs could use [search](Search "Search") from the beginning and look through all possible continuations in detail to find the best next move, but as this is quite time-consuming. In contrast, opening books can play opening moves almost instantly without searching nor heavy computing and help to save time.
* Provide a higher quality of play: Searching even with large depths can't see deep tactics, strategy, compensation. It may lose temporarily material for long term advantage.
* Provide variety: there already exists a lot of [literature](https://en.wikipedia.org/wiki/Chess_opening_book_%28literature%29) about different opening lines. As book moves can be chosen [randomly](Pseudorandom_Number_Generator "Pseudorandom Number Generator"), whereas searches are more or less deterministic.


## Types


Opening books are typically stored in two main formats:



### Text


The most advantage by using text form is that they are readable, understandable, and editable by humans and can be viewed, edited with normal text editors. However, the main disadvantage is that they may take too much space as well as time for searching since an item may take from 50 bytes (for FEN strings) to hundreds of bytes (for PGN text). If we store openings "continuously" (all possible opening positions) both data size and searching time become too huge and unacceptable for playing. They are usually missing weight values (to compare between items to know which ones are better) either. In practice, those opening books are usually very small with some lines or positions only, they are hard to be used for real game playing but for testing.


They are stored in typical ways for games and positions:



* [EPD](EPD "EPD"): They are the last positions of opening lines
* [PGN](PGN "PGN"): Opening lines are stored as individual games






* Special text formats: In 1999, [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget") published a **Book Builder** [[2]](#cite_note-2) in conjunction with his engine [La Dame Blanche](La_Dame_Blanche "La Dame Blanche"), a standalone open source program [[3]](#cite_note-3) to convert a [PGN file](Portable_Game_Notation "Portable Game Notation") into an opening book of the format proposed by [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") [[4]](#cite_note-4):



```

(e4(e5)(c5))(d4d5)) etc.

```

### Binary


Binary books have some important advantages, especially for computer chess engines: space-efficient, fast on accessing and searching, more useful information. At the most simple form, they are just a conversion of above text-opening books into binary, in the ready form for software and save text-binary converting steps. However, the major number of top books is built and worked with hash values from [transpositions](Transposition "Transposition"). Often each position is stored as a hash value (8 bytes) and some extra information such as the number of times occurred, number of games won by white/black / drawn with this position, average/maximum Elo of players playing to this opening position, chess program's success with the position. To save space those extra information typically about 2-8 bytes. For example, [PolyGlot](PolyGlot "PolyGlot") uses 16 bytes for each item, including hash, move, weight, learning values. Items of a book should be sorted by their hash. So when a chess program has to decide on a move, it will look up (by using binary-search) using the hash value of the current position to collect all information come with that hash value and then make a decision upon it.


To build and/or edit those opening books, users need to use special software.


The most popular format is [PolyGlot](PolyGlot "PolyGlot").



## Generation


All in all the information stored in an opening database should guide the chess game into a type of middle game in which the chess program proves itself most successful. But to achieve this there are two main ways.



### Handcrafted


If the opening database designer has some special preference of a certain opening line, he might create it fully manually. This is often the case if a chess program is about to play an important game against a grandmaster. Then the opening style will probably be chosen to be difficult and dangerous for the opponent. Another option is to first automatically generate a database and then fine-tune it manually.



### From game collection


Another option is to select a number of games (the type of which will affect the openings played: e.g. drawn games only, GM games only, etc) and then up to a certain depth store all positions in the opening database. It is true that by using this way of database generation some severe errors might by copied as well, but usually the chess programs are set to stop playing according to the book if a position occurred less than a certain number times before.



### By computing


Chess [engines](Engines "Engines") can be used to evaluate positions in a book opening tree to rank them, and/or decide to stop or expand.



## Book Building Tools


* [Bookbuilder](index.php?title=Bookbuilder&action=edit&redlink=1 "Bookbuilder (page does not exist)")
* [Bookup](Bookup "Bookup")
* [Chess Opening Wizard](index.php?title=Chess_Opening_Wizard&action=edit&redlink=1 "Chess Opening Wizard (page does not exist)") (COW)
* [Banksia GUI](Banksia_GUI "Banksia GUI")


## Book Playing


* [Engines](Engines "Engines"): They can directly use opening books to make move. Some engines use external books, some others integrate books inside their codes. Those engines need both opening book code and book data to run
* [GUI](GUI "GUI"): They can play opening books thus engines don't need to deal with and they just start computing from the middle period only. This way is quite popular because of some advantages (compared with letting engines play opening books themselves): simplifier for chess engines, save space, easier to manage opening books, more various ways to select openings, more fair-play to compare engines... The main disadvantage is that engines can’t or hardly use some book learning techniques


## Quotes


[Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") in *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)* [[5]](#cite_note-5) :




```
To solve the opening problems of his chess machine, [Belle](Belle "Belle"), [Ken Thompson](Ken_Thompson "Ken Thompson") typed in opening lines from the *[Encyclopedia of Chess Openings](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)* (in five thick volumes). Religiously, he dedicated one hour a day for almost three years (!) to the tedious pursuit of entering lines of play from the books and having his Belle computer verify them. The result was an opening library of roughly three-hundred thousand moves. The results were immediate and obvious: Belle became a much stronger chess program, and Ken probably aged prematurely. Later Ken developed a program to automatically read the *Encyclopedia*, allowing him to do in a few days what had taken him three years to do manually. [[6]](#cite_note-6) 

```





## Formats


* [ABK](ABK "ABK") - [Arena's](Arena "Arena") book format
* [BIN](PolyGlot "PolyGlot") - [PolyGlot](PolyGlot "PolyGlot") book fomat
* [CTG](CTG "CTG") - [ChessBase](ChessBase "ChessBase") book format


## Classification of Chess Openings


* [Encyclopaedia of Chess Openings (ECO)](ECO "ECO")
* [NIC-Key](NIC-Key "NIC-Key")






## Book Issues


* [Chaos vs. Nuchess @ WCCC 1980](WCCC_1980#BookIssues "WCCC 1980")
* [Cray Blitz vs. Fidelity X @ ACM 1984](Boris_Baczynskyj#CrayBlitzFidelity "Boris Baczynskyj")


## See also


* [Book Learning](Book_Learning "Book Learning")
* [Brainfish](Brainfish "Brainfish")
* [CPW-Engine\_book](CPW-Engine_book "CPW-Engine book")
* [Chess Databases](Databases "Databases")
* [La Dame Blanche](La_Dame_Blanche "La Dame Blanche") (Book Builder)
* [Opening](Opening "Opening")
* [Opening Book Authors](Category:Opening_Book_Author "Category:Opening Book Author")
* [Opening Suites](Test-Positions#OpeningSuites "Test-Positions")
* [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")
* [Transposition](Transposition "Transposition")


## Selected Publications


### 1974 ...


* [Ya. Yu. Gol'fand](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=96114), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Implementation of the opening book for the chess program.* in Problems of Cybernetic, No. 29 , pp. 201-210


 Я.Ю. Гольфанд, [А.Л. Футер](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Реализация дебютной справочной для шахматной программы.*/ Сб. Проблемы кибернетики №29, стр. 201-210
### 1980 ...


* [John F. White](John_F._White "John F. White") (**1982**). *[Chess-Book Openings](http://yourcomputeronline.wordpress.com/2011/01/19/chess-book-openings/)*. [Your Computer](Your_Computer "Your Computer"), [February 1982](http://yourcomputeronline.wordpress.com/2011/01/15/february-1982-contents-and-editorial/)
* [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1983**). *Tutorial: Representation of an Opening Tree*. [ICCA Newsletter, Vol. 6, No. 1](ICGA_Journal#6_1 "ICGA Journal")
* [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1983**). *BELLE*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")


### 1990 ...


* [John F. White](John_F._White "John F. White") (**1990**). *The Amateur's Book-Opening Routine*. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
* [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)") (**1996**). *[Improving Opening Book Performance Through Modeling of Chess Opponents](http://portal.acm.org/citation.cfm?id=228334&dl=ACM&coll=DL&CFID=34101495&CFTOKEN=18614940)*. [ACM](ACM "ACM") Conference on Computer Science 1996: 53-57
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Book Learning - a Methodology to Tune an Opening Book Automatically](http://www.craftychess.com/hyatt/learning.html)*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")
* [Michael Buro](Michael_Buro "Michael Buro") (**1999**). *Toward Opening Book Learning.* [ICCA Journal, Vol. 22, No. 2](ICGA_Journal#22_2 "ICGA Journal"), [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/book.pdf)


### 2000 ...


* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2000**). *[Strategies for the Automatic Construction of Opening Books](http://www.springerlink.com/content/detrvtjevmqd5p2g/)*. [CG 2000](CG_2000 "CG 2000")
* [Marty Hirsch](Marty_Hirsch "Marty Hirsch") (**2001**). *Machine Learning in MChess Professional*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") » [MChess](MChess "MChess")
* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2002**). *Exploring the Computational Limits of Large Exhaustive Search Problems*. Ph.D thesis, [ETH Zurich](ETH_Zurich "ETH Zurich"), [pdf](http://e-collection.library.ethz.ch/eserv/eth:25905/eth-25905-02.pdf)
* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2002**). *[Position-Value Representation in Opening Books](http://www.springerlink.com/content/aqbcher49k48affn/)*. [CG 2002](CG_2002 "CG 2002")
* [Marek Strejczek](Marek_Strejczek "Marek Strejczek") (**2004**). *Some aspects of chess programming*. M.Sc. thesis, [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź"), 4.2 Experiments with book learning
* [Thomas Widjaja](index.php?title=Thomas_Widjaja&action=edit&redlink=1 "Thomas Widjaja (page does not exist)") (**2004**). *Knowledge Engineering und Lernen in Spielen - Opening Book Learning*. [slides as pdf](http://www.ke.tu-darmstadt.de/lehre/archiv/ss04/se-spiele/OpeningBookLearning.pdf) (German)


### 2005 ...


* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2005**). *[Innovative Opening-Book Handling](http://link.springer.com/chapter/10.1007/11922155_1)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/publications/icga_open_springer.pdf)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Fuzzy books - Approximate opening knowledge](http://www.aifactory.co.uk/newsletter/2006_01_fuzzy_books.htm)*. [AI Factory](AI_Factory "AI Factory"), Spring 2006
* [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2006**). *Comparing Typical Opening Move Choices Made by Humans and Chess Engines*. [arXiv:cs/0610060](https://arxiv.org/abs/cs/0610060)
* [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2007**). *Comparing Typical Opening Move Choices Made by Humans and Chess Engines*. [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal), Vol. 50, No. 5
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2007**). *[Creating Book Knowledge](http://www.aifactory.co.uk/newsletter/2007_03_creating_book.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2007
* [Pierre Audouard](http://gobase.org/information/players/?pp=Pierre%20Audouard), [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2009**). *Grid co-evolution for adaptive simulations; application to the building of opening books in the game of Go*. [pdf](http://www.lri.fr/~rimmel/publi/ouvertures.pdf)
* [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Mark Winands](Mark_Winands "Mark Winands") (**2009**). *Meta Monte-Carlo Tree Search for Automatic Opening Book Generation*. [pdf](http://www.personeel.unimaas.nl/m-winands/documents/ouvertures9x9.pdf)
* [Bernd Blasius](index.php?title=Bernd_Blasius&action=edit&redlink=1 "Bernd Blasius (page does not exist)"), [Ralf Tönjes](index.php?title=Ralf_T%C3%B6njes&action=edit&redlink=1 "Ralf Tönjes (page does not exist)") (**2009**). *[Zipf's Law in the Popularity Distribution of Chess Openings](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.103.218701)*. [Physical Review Letters](https://en.wikipedia.org/wiki/Physical_Review_Letters), 103, 218701, [pdf](http://www.icbm.de/fileadmin/user_upload/icbm/ag/mathmod/download/BlasiusToenjes2009.pdf) [[7]](#cite_note-7)


### 2010 ...


* [Romaric Gaudel](index.php?title=Romaric_Gaudel&action=edit&redlink=1 "Romaric Gaudel (page does not exist)"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Nataliya Sokolovska](index.php?title=Nataliya_Sokolovska&action=edit&redlink=1 "Nataliya Sokolovska (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2010**). *A Principled Method for Exploiting Opening Books*. [CG 2010](CG_2010 "CG 2010"), [pdf](http://hal.inria.fr/docs/00/48/40/43/PDF/exploitingOB.pdf)
* [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Huang](index.php?title=Hong_Huang&action=edit&redlink=1 "Hong Huang (page does not exist)"), [Litao Deng](index.php?title=Litao_Deng&action=edit&redlink=1 "Litao Deng (page does not exist)") (**2011**). *[Dynamic Opening-Book in Computer Games](http://ieeexplore.ieee.org/document/5968713/)*. CCDC 2011 (Chinese)
* [Bo-Nian Chen](Bo-Nian_Chen "Bo-Nian Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2013**). *Automatic Generation of Chinese Dark Chess Opening Books*. [CG 2013](CG_2013 "CG 2013")


### 2015 ...


* [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [Bing-Tsung Chiang](Bing-Tsung_Chiang "Bing-Tsung Chiang"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Chang-Shing Lee](Chang-Shing_Lee "Chang-Shing Lee") (**2015**). *Job-Level Algorithms for Connect6 Opening Book Construction*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
* [John P. Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**2016**). *Search-Based Opening Book Construction*. [pdf](https://drive.google.com/file/d/0B2pvWWlf39g-NWN0OUpkRE0tem8/view) [[8]](#cite_note-8), [2017 edition](https://drive.google.com/file/d/0B2pvWWlf39g-Z2ZmbHhtWTUwZFE/view) [[9]](#cite_note-9)
* [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**2018**). *Search-based opening book construction*. [ICGA Journal, Vol. 40, No. 1](ICGA_Journal#40_1 "ICGA Journal")


## Forum Posts


### 1990 ...


* [gnuchess.book in Lisp](http://groups.google.com/group/gnu.chess/browse_frm/thread/329b9401059f679b) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 23, 1990


### 1995 ...


* [Opening taxonomy](https://groups.google.com/d/msg/rec.games.chess.computer/twuuIKTUqRw/bCN6Jn9zGOcJ) by [Hugh S. Myers](Hugh_S._Myers "Hugh S. Myers"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 12, 1995
* [The MCHESS5 computer killer book...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/656439670bd7c7fb) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 14, 1996
* [Killer Books](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f14614c6bdebff95) by [Andreas Mader](Andreas_Mader "Andreas Mader"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 29, 1996
* [Book learning and rating bias](https://www.stmintz.com/ccc/index.php?id=17861) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 01, 1998
* [How Rebel plays at SSDF the bare facts, just statistics and thoughts](https://www.stmintz.com/ccc/index.php?id=20650) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), June 15, 1998
* [Re: Killer Book](https://www.stmintz.com/ccc/index.php?id=20918) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 19, 1998
* [BookLearning Under the Microscope!!!](https://www.stmintz.com/ccc/index.php?id=25754) by Robert Henry Durrett, [CCC](CCC "CCC"), August 31, 1998
* [MCP8 - Rebel8, SSDF](https://www.stmintz.com/ccc/index.php?id=34711) by [Tony Hedlund](Tony_Hedlund "Tony Hedlund"), [CCC](CCC "CCC"), December 04, 1998 » [MChess](MChess "MChess")
* [Book learning?](https://www.stmintz.com/ccc/index.php?id=37968) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), December 31, 1998
* [Re: A separate process for the chess engine - How do I do this?](https://www.stmintz.com/ccc/index.php?id=43888) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), February 20, 1999
* [Web site updated and new program Book Builder](https://www.stmintz.com/ccc/index.php?id=44407) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), February 24, 1999
* [Opening book](https://www.stmintz.com/ccc/index.php?id=47747) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), April 01, 1999
* [Book learning](https://www.stmintz.com/ccc/index.php?id=68359) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), September 12, 1999


### 2000 ...


* [random book moves/ random generator](https://www.stmintz.com/ccc/index.php?id=88292) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), January 13, 2000 » [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")
* [Gromitchess bookcheating (for Vincent DIEPEVEEN)](https://www.stmintz.com/ccc/index.php?id=185200) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 23, 2001
* [question about book and learning](https://www.stmintz.com/ccc/index.php?id=226258) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 26, 2002
* [Book design](https://www.stmintz.com/ccc/index.php?id=267805) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), November 28, 2002
* [Opening Bug in Nejmet and Pharaon](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42820) by Mainflame, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2003 » [Nejmet](Nejmet "Nejmet"), [Pharaon](Pharaon "Pharaon")
* [Why use opening books in machine-machine competitions?](https://www.stmintz.com/ccc/index.php?id=330362) by [Mig Greengard](index.php?title=Mig_Greengard&action=edit&redlink=1 "Mig Greengard (page does not exist)"), [CCC](CCC "CCC"), November 25, 2003
* [Performance rating calculation](https://www.stmintz.com/ccc/index.php?id=368697) by [Dan Wulff](Dan_Wulff "Dan Wulff"), [CCC](CCC "CCC"), June 02, 2004


### 2005 ...


* [Nunn openings](https://www.stmintz.com/ccc/index.php?id=460363) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 07, 2005 » [Opening Suites](Test-Positions#OpeningSuites "Test-Positions")
* [Nunn2 openings](https://www.stmintz.com/ccc/index.php?id=460364) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), November 07, 2005
* [CTG specification](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2319) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), September 30, 2007 » [CTG](CTG "CTG")
* [Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661) by James Constance, [CCC](CCC "CCC"), April 14, 2008


 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=5) by [Jury Osipov](Jury_Osipov "Jury Osipov"), [CCC](CCC "CCC"), April 15, 2008 » [ABK](ABK "ABK") 
 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=6) by [Richard Pijl](Richard_Pijl "Richard Pijl"), [CCC](CCC "CCC"), April 15, 2008
 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=9) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 15, 2008
* [Leaving/Returning to Book Annoyance](http://www.talkchess.com/forum/viewtopic.php?t=27746) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), May 05, 2009
* [Book: KLO 150 ECO A00-E97 Variations](http://www.talkchess.com/forum/viewtopic.php?t=31392) by [kingliveson](Franklin_Titus "Franklin Titus"), [CCC](CCC "CCC"), December 31, 2009


### 2010 ...


* [Opening book formats and UIs](http://www.talkchess.com/forum/viewtopic.php?t=34795) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), June 08, 2010
* [Opening Books Battle..](http://www.open-chess.org/viewtopic.php?f=3&t=1073) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 04, 2011
* [ICGA rule #2 / opening books / Diep-Crafty, Turino 2006](http://www.talkchess.com/forum/viewtopic.php?t=40853) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), October 22, 2011 » [WCCC 2006](WCCC_2006 "WCCC 2006")
* [Creating Books from .PGN files](http://www.talkchess.com/forum/viewtopic.php?t=41529) by [David Nash](index.php?title=David_Nash&action=edit&redlink=1 "David Nash (page does not exist)"), [CCC](CCC "CCC"), December 20, 2011
* [CookieCat's opening book implementation](http://www.talkchess.com/forum/viewtopic.php?t=41804) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 05, 2012 » [CookieCat](CookieCat "CookieCat")
* [Bookbuilding 101](http://www.talkchess.com/forum/viewtopic.php?t=44705) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), August 06, 2012
* [Book format for the new engine](http://www.talkchess.com/forum/viewtopic.php?t=44758) by [Dragan Zdravkovic](Dragan_Zdravkovic "Dragan Zdravkovic"), [CCC](CCC "CCC"), August 10, 2012


**2013**



* [Ranking moves based on empirical information](http://www.talkchess.com/forum/viewtopic.php?t=46828) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), January 10, 2013
* [Opening Book (for Aquarium)](http://www.open-chess.org/viewtopic.php?f=7&t=2234) by andytl755, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 21, 2013 » [Aquarium](Aquarium "Aquarium")
* [Search-based opening book](http://www.talkchess.com/forum/viewtopic.php?t=48583) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 07, 2013
* [Opening Books - Something does not add up](http://hiarcs.net/forums/viewtopic.php?t=6083&sid=cbd0ee48fb78857cc4f62710aab154cc) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2013
* [Opening book cleanup](https://groups.google.com/d/msg/fishcooking/08k5kE5yAhM/bWGGQgWk9P0J) by [Dariusz Orzechowski](index.php?title=Dariusz_Orzechowski&action=edit&redlink=1 "Dariusz Orzechowski (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 03, 2013
* [2 Moves Engine Book](http://www.talkchess.com/forum/viewtopic.php?t=50358) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), December 07, 2013


 [Re: 2 Moves Engine Book](http://www.talkchess.com/forum/viewtopic.php?t=50358&start=13) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 08, 2013 » [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)")
**2014**



* [My new book](http://www.talkchess.com/forum/viewtopic.php?t=50721) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 02, 2014 » [UCT](UCT "UCT")
* [Perfect 2014 opening book is released](http://www.talkchess.com/forum/viewtopic.php?t=51299) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)"), [CCC](CCC "CCC"), February 16, 2014
* [Scid.eco](https://www.mail-archive.com/scid-users@lists.sourceforge.net/msg06639.html) by [Gregor Cramer](index.php?title=Gregor_Cramer&action=edit&redlink=1 "Gregor Cramer (page does not exist)"), [scid-users](https://www.mail-archive.com/scid-users@lists.sourceforge.net/), April 19, 2014
* [UCI, ownbooks, and a potential problem](http://www.talkchess.com/forum/viewtopic.php?t=52661) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), June 16, 2014 » [UCI](UCI "UCI")
* [Perfect 2014 Final (Full Package)](http://www.talkchess.com/forum/viewtopic.php?t=53126) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)"), [CCC](CCC "CCC"), July 30, 2014


### 2015 ...


* [Re: ICGA's 2015 World Computer Chess Championship/Events](http://www.talkchess.com/forum/viewtopic.php?t=55395&start=224) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 27, 2015
* [On Opening books in 2015](http://www.talkchess.com/forum/viewtopic.php?t=55569) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), March 06, 2015
* [creating an opening book](http://www.talkchess.com/forum/viewtopic.php?t=56770) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), June 24, 2015
* [Making Symbolic's opening book](http://www.talkchess.com/forum/viewtopic.php?t=56995) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 16, 2015 » [Symbolic](Symbolic "Symbolic")
* [The future of chess and elo ratings](http://www.talkchess.com/forum/viewtopic.php?t=57696) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 20, 2015 » [Match Statistics](Match_Statistics "Match Statistics")


**2016**



* [Introducing the \*.EBF project](http://www.talkchess.com/forum/viewtopic.php?t=58913) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 14, 2016
* [Statistical assessment of chess opening book moves](http://www.talkchess.com/forum/viewtopic.php?t=59374) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), February 27, 2016
* [REBEL | ProDeo book available in Polyglot format](http://www.talkchess.com/forum/viewtopic.php?t=59435) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 05, 2016 » [Rebel](Rebel "Rebel"), [ProDeo](ProDeo "ProDeo"), [PolyGlot](PolyGlot "PolyGlot")
* [How much benefit from opening book?](http://www.talkchess.com/forum/viewtopic.php?p=662580) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), March 06, 2016 » [Playing Strength](Playing_Strength "Playing Strength")
* [reversed-color transpositions](http://www.talkchess.com/forum/viewtopic.php?p=663148) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), March 11, 2016 » [Color Flipping](Color_Flipping "Color Flipping")
* [My new book is out: Noomen.ctg](http://www.talkchess.com/forum/viewtopic.php?t=60237) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), May 22, 2016 [[10]](#cite_note-10)
* [How to use openings books?](http://www.talkchess.com/forum/viewtopic.php?t=60939) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), July 25, 2016
* [CCRL - CEGT matches](http://www.talkchess.com/forum/viewtopic.php?t=60961) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 28, 2016 » [CCRL](CCRL "CCRL"), [CEGT](CEGT "CEGT")
* [Opening book from a statistical point of view](http://www.talkchess.com/forum/viewtopic.php?t=60980) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), July 29, 2016
* [opening book standards](http://www.talkchess.com/forum/viewtopic.php?t=61092) by [Jef Kaan](index.php?title=Jan_Kaan&action=edit&redlink=1 "Jan Kaan (page does not exist)"), [CCC](CCC "CCC"), August 10, 2016
* [Noomen.ctg: UPDATE](http://www.talkchess.com/forum/viewtopic.php?t=61176) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), August 20, 2016
* [Properties of unbalanced openings using Bayeselo model](http://www.talkchess.com/forum/viewtopic.php?t=61245) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 27, 2016 » [Match Statistics](Match_Statistics "Match Statistics")
* [The scaling with time of opening books](http://www.talkchess.com/forum/viewtopic.php?t=61506) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 23, 2016 » [Match Statistics](Match_Statistics "Match Statistics")
* [Winboard book settings](http://www.talkchess.com/forum/viewtopic.php?t=61780) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), October 20, 2016 » [WinBoard](WinBoard "WinBoard")
* [Search-Based Opening Book Construction](http://www.talkchess.com/forum/viewtopic.php?p=698871) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), December 14, 2016
* [Cumulative building of a shared search tree](http://www.talkchess.com/forum/viewtopic.php?t=62639) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), December 28, 2016 » [Chinese Chess](Chinese_Chess "Chinese Chess"), [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")


**2017**



* [Opening book trees](http://www.talkchess.com/forum/viewtopic.php?t=63287) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), February 27, 2017
* [Generate Opening Book from Scratch](http://www.talkchess.com/forum/viewtopic.php?t=63291) by [Stefan Edlich](Stefan_Edlich "Stefan Edlich"), [CCC](CCC "CCC"), February 27, 2017
* [Book ChessGUI](http://www.talkchess.com/forum/viewtopic.php?t=63478) by Krzysztof Grzelak, [CCC](CCC "CCC"), March 17, 2017 » [ChessGUI](ChessGUI "ChessGUI")
* [Search-Based Opening Book Construction](http://www.talkchess.com/forum/viewtopic.php?t=63862) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), April 29, 2017
* [FEOBOS 2.0 is available ...](http://www.talkchess.com/forum/viewtopic.php?t=63877) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 01, 2017
* [Opening testing suites efficiency](http://www.talkchess.com/forum/viewtopic.php?t=64358) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 21, 2017 » [Engine Testing](Engine_Testing "Engine Testing"), [Opening](Opening "Opening"), [Match Statistics](Match_Statistics "Match Statistics")
* [HERT - brand new openings-set by Thomas Zipproth](http://www.talkchess.com/forum/viewtopic.php?t=64894) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), August 14, 2017
* [New: Noomen 2-move Testsuite](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32336) by [[[Jeroen Noomen]], [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 22, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")


**2018**



* [SALC V5 openings and books launched](http://www.talkchess.com/forum/viewtopic.php?t=66311) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), January 13, 2018
* [Some opening book design questions](http://www.talkchess.com/forum/viewtopic.php?t=66657) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), February 21, 2018
* [Is there a program to build opening books based on engines?](http://www.talkchess.com/forum/viewtopic.php?t=66680) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 23, 2018
* [Rebel Book Draw?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68558) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), October 03, 2018 » [Draw](Draw "Draw")


**2019**



* [Book creation papers](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70518) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), April 18, 2019
* [Database snapshot](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71386) by [noobpwnftw](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), July 27, 2019
* [ChessDBCN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71764) by [noobpwnftw](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), September 09, 2019
* [Polyglot FRC/960 Opening Book](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72432) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 27, 2019 » [PolyGlot](PolyGlot "PolyGlot"), [Chess960](Chess960 "Chess960")


### 2020 ...


* [How many Elo points is a book?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75205) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 25, 2020 » [Playing Strength](Playing_Strength "Playing Strength")
* [Chess opening database with names](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75878) by Peperoni, [CCC](CCC "CCC"), November 20, 2020 » [ECO](ECO "ECO")


**2021**



* [Opening book implementation questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77507) by Pedro Duran, [CCC](CCC "CCC"), June 18, 2021


## External Links


* [Chess opening book from Wikipedia](https://en.wikipedia.org/wiki/Chess_opening_book)
* [Chess opening book (computers) from Wikipedia](https://en.wikipedia.org/wiki/Chess_opening_book_(computers))
* [Chess opening book (literature) from Wikipedia](https://en.wikipedia.org/wiki/Chess_opening_book_%28literature%29)
* [List of chess openings from Wikipedia](https://en.wikipedia.org/wiki/List_of_chess_openings)
* [Encyclopaedia of Chess Openings (ECO) from Wikipedia](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)
* [Chess opening theory table from Wikipedia](https://en.wikipedia.org/wiki/Chess_opening_theory_table)
* [Chess Opening Theory - Wikibooks](https://en.wikibooks.org/wiki/Chess_Opening_Theory)
* [Opening Books](http://www.fierz.ch/strategy4.htm) from [Strategy Game Programming](http://www.fierz.ch/strategy.htm) by [Martin Fierz](Martin_Fierz "Martin Fierz")
* [The use of openings books](https://www.game-ai-forum.org/icga-tournaments/news_item.php?id=35) by the [ICGA](ICGA "ICGA"), September 15, 2008


### Engine Books


* [HIARCS 13 – the Professional Openings Book](http://chessbase.com/newsdetail.asp?newsid=7069) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [ChessBase News](ChessBase "ChessBase"), March 10, 2011 » [HIARCS](HIARCS "HIARCS") [[11]](#cite_note-11)
* [Polyglot book format](http://hardy.uhasselt.be/Toga/book_format.html)
* [Arena Chess GUI - Opening Books](http://www.playwitharena.com/?User_Files%2C_Engines:Opening_Books_%2821%29%26nbsp%3B) » [Arena](Arena "Arena")
* [Book Bilder of La Dame Blanche](http://www.quarkchess.de/ladameblanche/) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), hosted by [Thomas Mayer](Thomas_Mayer "Thomas Mayer")
* [Perfect 2014 book](http://www.sedatcanbaz.com/chess/?page_id=127) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)") [[12]](#cite_note-12)
* [Fauzi's Opening Books](http://www.g-sei.org/wp-content/Users/Fauzi/fauzi.html) by [Fauzi Akram Dabat](Fauzi_Akram_Dabat "Fauzi Akram Dabat"), [G 6](G_6 "G 6") site


### Online Opening Tree


* [Chess Cloud Database Query Interface](https://www.chessdb.cn/queryc_en/) by [noobpwnftw](Bojun_Guo "Bojun Guo") [[13]](#cite_note-13)
* [ChessDB Online Opening Book](https://fsmosca.github.io/ChessDB-Online-Book/) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca")
* [Chess database with eight million games. Openings, players, tournaments - Online](https://database.chessbase.com/?lang=en/) - [ChessBase](ChessBase_(Database) "ChessBase (Database)")
* [Chess Opening Explorer](http://www.chessgames.com/perl/explorer) from [chessgames.com](http://www.chessgames.com/index.html)
* [NICBase Online - New In Chess](https://secure.newinchess.com/NICBase/Default.aspx?PageID=400) - [NICBase](NICBase "NICBase")
* [Opening Tree Mode](http://chessok.com/?page_id=352) - [ChessOK](ChessOK "ChessOK")
* [OPEX - Chess Openings Explorer](https://opex.ebemunk.com/) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)")
* [Shredder Computer Chess Download - Opening Database](http://www.shredderchess.com/online-chess/online-databases/opening-database.html) - [Shredder](Shredder "Shredder")


### Misc


* [Jan Klare's](Category:Jan_Klare "Category:Jan Klare") [The Dorf](Category:The_Dorf "Category:The Dorf") - Overtüre/Pose, [Moers Festival](https://en.wikipedia.org/wiki/Moers_Festival) 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) Worn copy of second edition of Modern Chess Openings (1913) by [Richard Clewin Griffith](https://en.wikipedia.org/wiki/Richard_Griffith_%28chess_player%29) (1872–1955) and [John Herbert White](https://en.wikipedia.org/wiki/John_Herbert_White) (1880–1920), with an introduction by [Henry Ernest Atkins](https://en.wikipedia.org/wiki/Henry_Ernest_Atkins) (1872–1955), [Modern Chess Openings from Wikipedia](https://en.wikipedia.org/wiki/Modern_Chess_Openings)
2. [↑](#cite_ref-2) [Web site updated and new program Book Builder](https://www.stmintz.com/ccc/index.php?id=44407) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), February 24, 1999
3. [↑](#cite_ref-3) [Book Bilder of La Dame Blanche](http://www.quarkchess.de/ladameblanche/) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), hosted by [Thomas Mayer](Thomas_Mayer "Thomas Mayer")
4. [↑](#cite_ref-4) [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1983**). *Tutorial: Representation of an Opening Tree*. [ICCA Newsletter, Vol. 6, No. 1](ICGA_Journal#6_1 "ICGA Journal")
5. [↑](#cite_ref-5) [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*. 11. I Feel Like a Teenager Again, pp. 184
6. [↑](#cite_ref-6) [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
7. [↑](#cite_ref-7) [Zipf's law from WIkipedia](https://en.wikipedia.org/wiki/Zipf%27s_law)
8. [↑](#cite_ref-8) [Search-Based Opening Book Construction](http://www.talkchess.com/forum/viewtopic.php?p=698871) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), December 14, 2016
9. [↑](#cite_ref-9) [Search-Based Opening Book Construction](http://www.talkchess.com/forum/viewtopic.php?t=63862) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), April 29, 2017
10. [↑](#cite_ref-10) [Books](http://rebel13.nl/download/books/) hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
11. [↑](#cite_ref-11) [Re: Opening Books Battle..](http://www.open-chess.org/viewtopic.php?f=3&t=1073#p11368) by BB+ ([Mark Watkins](Mark_Watkins "Mark Watkins")), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 12, 2011
12. [↑](#cite_ref-12) [Perfect 2014 Final (Full Package)](http://www.talkchess.com/forum/viewtopic.php?t=53126) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)"), [CCC](CCC "CCC"), July 30, 2014
13. [↑](#cite_ref-13) [GitHub - noobpwnftw/chessdb: ChessDB](https://github.com/noobpwnftw/chessdb)

**[Up one level](Knowledge "Knowledge")**







 
