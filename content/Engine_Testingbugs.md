---
title: Engine Testingbugs
---
**[Home](Home "Home") * Engine Testing**

[](http://sanseverything.wordpress.com/2008/01/16/hope-springs-eternal/) The ever-optimistic [Wile E. Coyote](https://en.wikipedia.org/wiki/Wile_E._Coyote_and_Road_Runner) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Engine Testing**,

the process either to eliminate [bugs](https://en.wikipedia.org/wiki/Software_bug) and to measure [performance](Playing_Strength "Playing Strength") of a chess engine. New implementations of [move generation](Move_Generation "Move Generation") are tested with [Perft](Perft "Perft"), while new features and [tuning](Automated_Tuning "Automated Tuning") of [search](Search "Search") and [evaluation](Evaluation "Evaluation") are verified by [test-positions](Test-Positions "Test-Positions") and by playing [matches](Match_Statistics "Match Statistics") against other engines.

## Bug Hunting

- [Perft](Perft "Perft") ([Perft Results](Perft_Results "Perft Results"))
- [Debugging](Debugging "Debugging")

## Analyzing

- [Logging](Logging "Logging")
- [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
- [Search Statistics](Search_Statistics "Search Statistics")

## Tuning

- [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Engine Similarity](Engine_Similarity "Engine Similarity")

## Test-Positions

Running sets of test-positions with number of solutions per fixed time-frame is useful to prove whether things are broken after program changes or to get hints about missing knowledge. But one should be careful to tune engines based on test-position results, since solving (possible tactical) test-positions does not necessarily correlate with practical [playing strength](Playing_Strength "Playing Strength") in matches against other opponents.

- [Test-Positions](Test-Positions "Test-Positions")

## Matches

Most testing involves running different versions of a program in matches, and comparing results.

## Time Controls

Generally speaking, for testing changes that don't alter the search tree itself, but only affect performance (eg. [move generation](Move_Generation "Move Generation")) can be tested with given fixed nodes, fixed time or fixed depth. In all other cases the [time management](Time_Management "Time Management") should be left to the engine to simulate real tournament conditions. On the other hand, [debugging](Debugging "Debugging") is much easier under fixed conditions as the games become deterministic.

A side from the type of [time control](Time_Management#Time_Controls "Time Management") one also has to decide on how much time should be spent per game, ie. what the average quality of the games should be like. While one can test more changes in the a certain time at short time controls, it is also relevant how a certain change scales to different strengths. So for example should one increase the [R](Depth_Reduction_R "Depth Reduction R") in [Null move pruning](Null_Move_Pruning "Null Move Pruning") to 3 in depths > 7, this change may only be effectively tested on time controls where this new condition is triggered frequently enough, ie. where the average search depth is far greater than seven. It is hard to generalize, but on average changes of the search functions ([LMR](Late_Move_Reductions "Late Move Reductions"), [nullmove](Null_Move "Null Move"), [futility](Futility_Pruning "Futility Pruning") or similar [pruning](Pruning "Pruning"), [reductions](Reductions "Reductions") and [extensions](Extensions "Extensions") ) tend to be more sensitive to the time control than the tuning of [evaluation](Evaluation "Evaluation") parameters.

## Opening

During testing the engines should ideally play the same style of openings they would play in a normal tournament, so not to optimize them for different types of positions. One option is to use the engines own [opening book](Opening_Book "Opening Book") or one can use [opening suites](Test-Positions#OpeningSuites "Test-Positions"), a set of quiet test positions. In the latter case the same opening suit would be used for each tournament conducted and furthermore each position is played a second time with colors reversed. With these measures one can try to minimize the disparity between tests caused by different openings.

## Tournament Manager

[User interfaces](User_Interface "User Interface") or [command line tools](CLI "CLI") for [UCI](UCI "UCI") and [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible engines in engine-engine matches are mentioned under [Tournament Manager](Tournament_Manager "Tournament Manager").

## Frameworks

- [Fishtest](Stockfish#TestingFramework "Stockfish")
- [OpenBench](OpenBench "OpenBench")

## Chess Server

One can also test an engine's performance by comparing it to other programs on the various internet platforms <a id="cite-note-2" href="#cite-ref-2">[2]</a> . In this case the different hardware and features like different [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") or [Opening Books](Opening_Book "Opening Book") have to be considered.

- [Chess Server](Chess_Server "Chess Server")
- [Tournaments](Tournaments_and_Matches "Tournaments and Matches")

## Statistics

The question whether certain results actually indicates a [strength](Playing_Strength "Playing Strength") increase or not, can be answered with

- [Match Statistics](Match_Statistics "Match Statistics")
- [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
- [LOS Table](LOS_Table "LOS Table")

## Ratings

- [Rating System](index.php?title=Rating_System&action=edit&redlink=1 "Rating System (page does not exist)")
- [Engine Rating Lists](Engine_Rating_Lists "Engine Rating Lists")

## Test Results

- [Null Move Pruning Test Results](Null_Move_Pruning_Test_Results "Null Move Pruning Test Results")
- [Late Move Reduction Test Results](Late_Move_Reduction_Test_Results "Late Move Reduction Test Results")

## Notable Bugs

- [Brute Force (Program)](</Brute_Force_(Program)> "Brute Force (Program)"), [En passant bug](En_passant#bugs "En passant"), [ACM 1977](ACM_1977 "ACM 1977") and [ACM 1978](ACM_1978 "ACM 1978")
- [Coko - Mate in One?](Coko#MateBug "Coko"), [ACM 1971](ACM_1971 "ACM 1971")
- [Chess 2175X vs. Genesis](4th_Computer_Olympiad#PromotionBug "4th Computer Olympiad"), [Promotion](Promotions "Promotions") bug, [4th Computer Olympiad 1992](4th_Computer_Olympiad#Chess "4th Computer Olympiad")
- [Nimzo's winning white-black bug](WMCCC_1993#NimzoBug "WMCCC 1993"), [WMCCC 1993](WMCCC_1993 "WMCCC 1993")
- [Novag Micro Chess - Castling bug](Novag_Micro_Chess#CastlingBug "Novag Micro Chess"), [CPWTIPC 1981](CPWTIPC_1981 "CPWTIPC 1981")
- [Proscha](Proscha#bugs "Proscha") capturing its own king versus [Daja](Daja "Daja"), [First GI Computer Chess Tournament 1975](First_GI_Computer_Chess_Tournament "First GI Computer Chess Tournament")
- [System Tal vs. XXXX](WMCCC_1995#TalXXXX "WMCCC 1995"), [Promotion](Promotions "Promotions") bug, [WMCCC 1995](WMCCC_1995 "WMCCC 1995")
- [Xinix - Mate in One](XiniX "XiniX"), [DOCCC 2000](DOCCC_2000 "DOCCC 2000") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Publications

- [Tony Marsland](Tony_Marsland "Tony Marsland"), [Paul Rushton](Paul_Rushton "Paul Rushton") (**1973**). *[Mechanisms for Comparing Chess Programs](http://dl.acm.org/citation.cfm?id=805703).* [ACM Annual Conference](ACM_1973 "ACM 1973"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Marsland-Rushton-ACM73)
- [Tim Breitkreutz](Tim_Breitkreutz "Tim Breitkreutz"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1984**). *Computer vs Computer via Computer*. [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal"), reprinted in [Computer Chess Reports 1985](Computer_Chess_Reports "Computer Chess Reports"), Vol. 3, No. 2 » [Phoenix](Phoenix "Phoenix"), [Super Constellation](Super_Constellation "Super Constellation")
- [John Stanback](John_Stanback "John Stanback") (**1990**). *Supercomputing '90: Computer-Chess Testing and Programming Session*. [ICCA Journal, Vol. 13, No. 4](ICGA_Journal#13_4 "ICGA Journal") » [ACM 1990](ACM_1990 "ACM 1990")
- [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1993**). *How Our PC Chess Programs Are Developed*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports") 1992-93, Vol. 3, No. 2, pp. 12
- [Thomas Mally](Thomas_Mally "Thomas Mally") (**1993**). *Matt in Wieviel?* [PC Schach](PC_Schach "PC Schach") 3/93 (German)
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2007**). *[Statistical Minefields with Version Testing](http://www.aifactory.co.uk/newsletter/2007_04_stat_minefields.htm)*. [AI Factory](AI_Factory "AI Factory"), Winter 2007 » [Match Statistics](Match_Statistics "Match Statistics")
- [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir") (**2007**). *GTQL: A Query Language for Game Trees*. M.Sc. thesis, [Reykjavík University](https://en.wikipedia.org/wiki/Reykjav%C3%ADk_University), [pdf](http://www.ru.is/lisalib/getfile.aspx?itemid=9655)
- [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"). (**2008**). *[GTQ: A Language and Tool for Game-Tree Analysis](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_20)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.ru.is/faculty/yngvi/pdf/IsleifsdottirB08.pdf)

## Forum Posts

## 1995 ...

- [Testing Chess Programs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2aaa054105f1445e) by [Jan Eric Larsson](Jan_Eric_Larsson "Jan Eric Larsson"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 09, 1996
- [Self-test and others rating stuffs...](https://www.stmintz.com/ccc/index.php?id=13569) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), January 01, 1998
- [Proposal: New testing methods for SSDF (1)](https://www.stmintz.com/ccc/index.php?id=16851) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), April 13, 1998

## 2000 ...

- [Using 2 machines for matches (Linux)](https://www.stmintz.com/ccc/index.php?id=176716) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 24, 2001 » [XBoard](XBoard "XBoard"), [Linux](Linux "Linux")
- [A proposed WAC replacement for testing](https://www.stmintz.com/ccc/index.php?id=189308) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), September 18, 2001 » [Win at Chess](Win_at_Chess "Win at Chess")
- [Value of playing different versions of a program against each other](https://www.stmintz.com/ccc/index.php?id=275347) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 06, 2003
- [testing of evaluation function](https://www.stmintz.com/ccc/index.php?id=293815) by Steven Chu, [CCC](CCC "CCC"), April 17, 2003 » [Evaluation](Evaluation "Evaluation")
- [Testing the reliability of forward pruning](https://www.stmintz.com/ccc/index.php?id=296689) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), May 15, 2003 » [Pruning](Pruning "Pruning")
- [To programmers: Hints for testing after a partial rewrite](https://www.stmintz.com/ccc/index.php?id=334370) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), December 08, 2003
- [Is there a way?](https://www.stmintz.com/ccc/index.php?id=400589) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 13, 2004

## 2005 ...

- [table for detecting significant difference between two engines](https://www.stmintz.com/ccc/index.php?id=484357) by Joseph Ciarrochi, [CCC](CCC "CCC"), February 03, 2006
- [test methodology](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5866) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 13, 2006
- [Testing and debugging chess engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5955) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2006

**2007**

- [Programmer bug hunt challenge](http://www.talkchess.com/forum/viewtopic.php?t=13557) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 04, 2007 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"), [En passant](En_passant "En passant")
- [a beat b,b beat c,c beat a question](http://www.talkchess.com/forum/viewtopic.php?t=13800) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 16, 2007 » [Playing Strength](Playing_Strength "Playing Strength")
- [An objective test process for the rest of us?](http://www.talkchess.com/forum/viewtopic.php?t=16412) by [Nicolai Czempin](Nicolai_Czempin "Nicolai Czempin"), [CCC](CCC "CCC"), September 12, 2007
- [My new testing scheme](http://www.talkchess.com/forum/viewtopic.php?t=17947) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), November 20, 2007

**2008**

- [Test you engine](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=20082) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 10, 2008
- [New testing thread](http://www.talkchess.com/forum/viewtopic.php?t=22832) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 07, 2008
- [Comparing two version of the same engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=24590) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), October 26, 2008
- [Debate: testing at fast time controls](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=25461) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), December 15, 2008

**2009**

- [Cutechess-cli: A command line tool for engine-engine matches](http://www.talkchess.com/forum/viewtopic.php?t=27024), by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), March 16, 2009
- [Testing procedure](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=28130) by [Matt Gingell](Matt_Gingell "Matt Gingell"), [CCC](CCC "CCC"), May 27, 2009
- [Cutechess-cli version 0.1.8 released](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=293506&t=27024) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), September 29, 2009
- [A reason for testing at fixed number of nodes](http://www.talkchess.com/forum/viewtopic.php?t=30513) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), November 06, 2009
- [different kinds of testing](http://www.talkchess.com/forum/viewtopic.php?t=30550) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), November 09, 2009
- [more on fixed nodes](http://www.talkchess.com/forum/viewtopic.php?t=30565) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 10, 2009

## 2010 ...

- [XBoard and epd tournament](http://www.talkchess.com/forum/viewtopic.php?t=32254) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), January 31, 2010 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [Long game vs short game testing](http://www.talkchess.com/forum/viewtopic.php?t=33685) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), April 08, 2010
- [Pairings generation based on a big PGN file](http://www.talkchess.com/forum/viewtopic.php?t=35537) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), July 22, 2010
- [hiatus good for bug-finding](http://www.talkchess.com/forum/viewtopic.php?p=358600) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), June 27, 2010

**2011**

- [testing question](http://www.talkchess.com/forum/viewtopic.php?t=39255) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), June 01, 2011
- [Debugging regression tests](http://www.talkchess.com/forum/viewtopic.php?t=39390) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), June 16, 2011 <a id="cite-note-4" href="#cite-ref-4">[4]</a>

**2012**

- [fast game testing](http://www.talkchess.com/forum/viewtopic.php?t=41876) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 08, 2012
- [Your best bug ?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=477389&t=44706&sid=8b10031146b44f86ac4c4a129debf451) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 06, 2012
- [Yet Another Testing Question](http://www.talkchess.com/forum/viewtopic.php?t=45158) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), September 15, 2012
- [Another testing question](http://www.talkchess.com/forum/viewtopic.php?t=45287) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 23, 2012
- [A word for casual testers](http://www.talkchess.com/forum/viewtopic.php?t=46572) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 25, 2012

**2013**

- [A poor man's testing environment](http://www.talkchess.com/forum/viewtopic.php?t=46759) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 04, 2013 <a id="cite-note-5" href="#cite-ref-5">[5]</a> » [Match Statistics](Match_Statistics "Match Statistics")
- [engine-engine testing isues](http://www.talkchess.com/forum/viewtopic.php?t=46948) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), January 20, 2013
- [Beta for Stockfish distributed testing](http://www.talkchess.com/forum/viewtopic.php?t=47407) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 05, 2013 » [Fishtest](Stockfish#TestingFramework "Stockfish")
- [Fishtest Distributed Testing Framework](http://www.talkchess.com/forum/viewtopic.php?t=47885) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 01, 2013  » [Fishtest](Stockfish#TestingFramework "Stockfish")
- [cutechess-cli 0.6.0 released](http://www.talkchess.com/forum/viewtopic.php?t=48626) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), July 12, 2013
- [fast testing NIT algorithm](http://www.talkchess.com/forum/viewtopic.php?t=49054) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), August 22, 2013
- [OICS: Computers Only ICS based Chess server for anyone](http://www.talkchess.com/forum/viewtopic.php?t=49103) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), August 26, 2013 » [OICS](index.php?title=OICS&action=edit&redlink=1 "OICS (page does not exist)")

**2014**

- [testing procedure](http://www.talkchess.com/forum/viewtopic.php?t=51383) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), February 23, 2014

## 2015 ...

- [Bullet vs regular time control, say 40/4m CCRL/CEGT](http://www.talkchess.com/forum/viewtopic.php?t=57437) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 29, 2015
- [Static evaluation test posistions](http://www.talkchess.com/forum/viewtopic.php?t=58359) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), November 25, 2015

[Re: Static evaluation test posistions](http://www.talkchess.com/forum/viewtopic.php?t=58359&start=2) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), November 26, 2015 » [Python](Python "Python")
**2016**

- [Ordo 1.0.9 (new features for testers)](http://www.talkchess.com/forum/viewtopic.php?t=59038) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 25, 2016
- [cluster versus single server](http://www.talkchess.com/forum/viewtopic.php?t=59984) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), April 28, 2016
- [Testing using many computers and architectures](http://www.talkchess.com/forum/viewtopic.php?t=61422) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 14, 2016
- [command line engine match?](http://www.talkchess.com/forum/viewtopic.php?t=61988) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), November 06, 2016 » [CLI](CLI "CLI")
- [Looking for an epd file for sanity checks...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61991) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), November 06, 2016
- [Testing with different EPD suits for search vs eval changes](http://www.talkchess.com/forum/viewtopic.php?t=62576) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 23, 2016

**2017**

- [sprt tourney manager](http://www.talkchess.com/forum/viewtopic.php?t=62922) by [Richard Delorme](Richard_Delorme "Richard Delorme"), [CCC](CCC "CCC"), January 24, 2017 » [Amoeba Tournament Manager](Amoeba#TournamentManager "Amoeba"), [SPRT](Match_Statistics#SPRT "Match Statistics")
- [how to properly test the changes to the engine ?](http://www.talkchess.com/forum/viewtopic.php?t=63001) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 01, 2017
- [How to go about chasing a bug like this?](http://www.talkchess.com/forum/viewtopic.php?t=63119) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), February 09, 2017 » [Debugging](Debugging "Debugging")
- [How to find SMP bugs ?](http://www.talkchess.com/forum/viewtopic.php?t=63454) by Lucas Braesch, [CCC](CCC "CCC"), March 15, 2017 » [Debugging](Debugging "Debugging"), [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Testing for Move Ordering Improvements](http://www.talkchess.com/forum/viewtopic.php?t=63555) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), March 25, 2017 » [Move Ordering](Move_Ordering "Move Ordering"), [Search Statistics](Search_Statistics "Search Statistics")
- [Testing endgame strength](http://www.talkchess.com/forum/viewtopic.php?t=64356) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 21, 2017 » [Endgame](Endgame "Endgame"), [RuyDos](RuyDos "RuyDos")
- [Opening testing suites efficiency](http://www.talkchess.com/forum/viewtopic.php?t=64358) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 21, 2017 » [Opening](Opening "Opening"), [Match Statistics](Match_Statistics "Match Statistics")
- [Testing A against B by playing a pool of others](http://www.talkchess.com/forum/viewtopic.php?t=64394) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 24, 2017 » [Match Statistics](Match_Statistics "Match Statistics")
- [Core behaviour](http://www.talkchess.com/forum/viewtopic.php?t=64441) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 28, 2017 » [Process](Process "Process"), [Thread](Thread "Thread")
- [Engine testing & error margin ?](http://www.talkchess.com/forum/viewtopic.php?t=64519) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), July 05, 2017
- [Engines for testing (Linux, fast time control)](http://www.talkchess.com/forum/viewtopic.php?t=65766) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 18, 2017 » [Linux](Linux "Linux")

**2018**

- [Issue with self play testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67485) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), May 18, 2018
- [Basic automated testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68531) by Josh Odom, [CCC](CCC "CCC"), September 28, 2018

[Re:Basic automated testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68531&start=6) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 30, 2018 » [OpenBench](OpenBench "OpenBench")

- [testing consistency](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69284) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 16, 2018

**2019**

- [Any testing framwork similair to Fishtest that can be run locally ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70383) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), April 02, 2019
- [self test](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71848) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), September 18, 2019

## 2020 ...

- [EPD destruction tests](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73129) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), February 19, 2020
- [EPD destruction tests, part 2](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73208) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), February 27, 2020
- [Looking for automatic Engine Testing Software](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74503) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), July 19, 2020

**2021**

- [Testing strategies for my engines playing strength](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76225) by Thomas Jahn, [CCC](CCC "CCC"), January 04, 2021
- [Effect of adjudication and TC on testing process](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76536) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 09, 2021 » [Minic](Minic "Minic")

**2022**

- [Strategies to unit testing the search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79276) by Olexiy Svitashev, [CCC](CCC "CCC"), February 03, 2022 » [Search](Search "Search")
- [How do you know you improved ?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79280) by Philippe Chevalier, [CCC](CCC "CCC"), February 03, 2022

## External Links

- [Cute Chess](http://ajonsson.kapsi.fi/cutechess.html)
- [cutechess · GitHub](https://github.com/cutechess/cutechess)
- [GitHub - OpenBench a Distributed SPRT Testing Framework for Chess Engines](https://github.com/AndyGrant/OpenBench) by [Andrew Grant](Andrew_Grant "Andrew Grant") » [OpenBench](OpenBench "OpenBench"), [SPRT](Match_Statistics#SPRT "Match Statistics")
- [GitHub - ChrisWhittington/Chess-EPDs: Various EPD test suites](https://github.com/ChrisWhittington/Chess-EPDs) by [Chris Whittington](Chris_Whittington "Chris Whittington")
- [Regression testing from Wikipedia](https://en.wikipedia.org/wiki/Regression_testing)
- [SPCC](http://www.sp-cc.de/index.htm) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)")
- [CHESS - Microsoft Research](http://research.microsoft.com/en-us/projects/chess/) a tool for finding and reproducing [Heisenbugs](https://en.wikipedia.org/wiki/Unusual_software_bug) in concurrent programs.
- [Engine test stand from Wikipedia](https://en.wikipedia.org/wiki/Engine_test_stand)
- [Terje Rypdal Group](Category:Terje_Rypdal "Category:Terje Rypdal") feat. [Palle Mikkelborg](Category:Palle_Mikkelborg "Category:Palle Mikkelborg"), [Håkon Graf](https://de.wikipedia.org/wiki/Haakon_Graf), [Sveinung Hovensjø](http://no.wikipedia.org/wiki/Sveinung_Hovensj%C3%B8) and [Jon Christensen](Category:Jon_Christensen "Category:Jon Christensen") - [Per Ulv](http://no.wikipedia.org/wiki/Per_Ulv), 1978, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Hope Springs Eternal](http://sanseverything.wordpress.com/2008/01/16/hope-springs-eternal/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Internet chess servers from Wikipedia](https://en.wikipedia.org/wiki/Category:Internet_chess_servers)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Defending Humanity's Honor](http://www.xs4all.nl/~timkr/chess2/honor.htm) by [Tim Krabbé](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Regression testing from Wikipedia](https://en.wikipedia.org/wiki/Regression_testing)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Testing a chess engine from the ground up](http://www.top-5000.nl/tuning.htm) from [Home of the Dutch Rebel](http://www.top-5000.nl/) by [Ed Schröder](Ed_Schroder "Ed Schroder")

**[Up one Level](Home "Home")**

