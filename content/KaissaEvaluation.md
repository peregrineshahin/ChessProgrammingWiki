---
title: KaissaEvaluation
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Kaissa**



[ Caïssa [[1]](#cite_note-1)
**Kaissa**, (Russian: Каисса)


the famous chess program developed from [1970](Timeline#1970 "Timeline") at the Moscow [Institute of Control Sciences](Institute_of_Control_Sciences "Institute of Control Sciences") by a group of researchers around [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") and authors of the former [ITEP Chess Program](ITEP_Chess_Program "ITEP Chess Program"). In 1972 it was named after the goddess of chess [Caïssa](https://en.wikipedia.org/wiki/Ca%C3%AFssa) and won the [1st World Computer Chess Championship](WCCC_1974 "WCCC 1974") 1974 in Stockholm, where it ran on an [IBM 360](IBM_360 "IBM 360") compatible [ICL 4/70](ICL_4-70 "ICL 4-70") [[2]](#cite_note-2) [[3]](#cite_note-3). Kaissa was a quite sophisticated program for that time. It was a [Shannon Type A program](Type_A_Strategy "Type A Strategy"), using [Bitboards](Bitboards "Bitboards") for the internal [board representation](Board_Representation "Board Representation") and advanced search techniques, notably already the idea of [null move pruning](Null_Move_Pruning "Null Move Pruning") [[4]](#cite_note-4) [[5]](#cite_note-5).



## Primary Authors


* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy")
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky")
* [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov")


## Further Authors


directly working on the program [[11]](#cite_note-11) :



* [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov")
* [Alexander Bitman](Alexander_Bitman "Alexander Bitman")
* A. Baraev [[12]](#cite_note-12)
* A. Leman [[13]](#cite_note-13)
* M. Rozenfeld [[14]](#cite_note-14)


## History of Kaissa


by [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (1999) [[15]](#cite_note-15)



### Introduction


By now it is already difficult to represent the era of mainframes - the large computers, each of which occupied decent bay but at the beginning of the 70th this was to be all the rage. In those years the computers only began to appear in the regions distant from the military needs. In the USSR for incomprehensible reasons were [produced copies](ICL_4-70 "ICL 4-70") of the computers of the British company [[1]](https://en.wikipedia.org/wiki/International_Computers_Limited) (but not the then legislator of modes - [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)")) at that time.


One of them felt in [ITEP](Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics"), where it was necessary for the group of [Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") to be the trailblazers of package multitasking on the computer. Thus as far the programmers worked with that code, it became obvious, to use appropriate programming languages. Specifically, it was necessary, because multitasking did not allow the traditional at that time manual fastening of regions memory behind areas of program code and variables. However, the programming languages (FORTRAN and Assembler) seemed by violence above the creative thought. As a result an expensive and powerful (for those times) technology stayed almost always.


In essence the machine was used by two tasks. The probability calculation of earthquakes by the specialists of the institute of geophysics - which predicted the improbable of the earthquake in Rumania (from the point of view of seismologists). Second the development of a chess playing program on base of the old [ITEP Chess Program](ITEP_Chess_Program "ITEP Chess Program").


By 1972 a decent chess program was made and the newspaper of [Pravda](https://en.wikipedia.org/wiki/Komsomolskaya_Pravda%7CKomsomolskaya)] (then very popular) organized a match of this program with the readers. A catchy name was required, and chess reviewer of Komsomolskaya, A. Khenkin devised the word of Kaissa. The regulations of the match was simple. Each side played one game white, and another black. The move of each side was done in one week. The moves of the readers were selected according to the number of voices. Kaissa was able to [ponder](Pondering "Pondering"), but we did not use this feature.


The newspaper left the sequential positions on Saturday, and until Tuesday letters were collected, Thursday night Kaissa checked its answers. Match engaged almost year - since January until November - and it ended by the victory of the readers with the score 1.5 to 0.5. Those, who remember the hot summer of 1972, can envy to the authors of Kaissa, that carried out the pair of days in the week in the conditioned machine room - the coolest place of Moscow.


The match drew the attention of the entire world (I know even foreigner, who learned cyrillic alphabet and a little the Russian language in order to be up to date in the game), and they invited us to participate in the [world championship 1974](WCCC_1974 "WCCC 1974").


Since 1972 in the USA and Canada were hold the yearly [championships of North America](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") among the chess programs, organized by the [ACM](ACM "ACM"). The team of Kaissa directed the organizers of these tournaments to the thought to conduct a world championship, whose organization within the framework its regular congress took upon itself.


There were 16 programs from the different European countries, Canada and USA. The championship as declared previously, took place at one of the best hotels of Stockholm. Tickets into the concert hall of the hotel, where participants sat, were sold, and it is expensive. However, then Sweden was one of the richest countries of the world.


Naturally, to bring mainframes from the entire world to Stockholm was impossible. Computer- substitutes also were located not for all participants; therefore the telephone (not the Internet, but common telephone) was the basic means of connection. In the machine rooms, where program- participants played, were situated the special representatives of the [ICF](Institute_of_Control_Sciences "Institute of Control Sciences"), whose task was to control that the programmers would not interfere the moves of the programs.


In the tournament hall the authors of programs sat with the hand receivers in their hands. The regulations of the tournament made demands on presence in the hall precisely of the author of the program (or one of them, if they were several, as in our case), and not the representative (it was hardly necessary for me to visit Stockholm).


Difference of the championship of programs from usual chess tournament - wild noise in the hall. First, participants were forced to shout into the tube. I proved to be happy exception - connection with Moscow worked magnificently, because it was organized on the special joint solution of three departments: Committee on science and technology, the ministries of connection and one additional committee. However, my telephone negotiations presented no secret, because they according to the loud connection were transmitted into the conference hall, where our fans were gathering.


Additional noise in the tournament hall was created by spectators, who loudly comment on the moves of participants. Many new Russian words were heard in the honorable hall during these four days. The chief arbitor of tournament, Scotsman [David Levy](David_Levy "David Levy"), chess player and chess journalist - commented the games for the spectators. David presented the possibilities of the chess programs well and guessed moves very frequently.


Finally that was the most important thing for me, directly behind a little table authors of programs exchanged words. While programs thought over moves, their authors spent rather specific scientific conference, after all for many it there was a first meeting of group of the people who have made friends then for many long years. Games were not postponed, and played to the end (one was occupied not only evening, but also all night long). For participants in the hall, the bar where it was possible not only to drink has been opened, but also to talk about all on light. With me they communicated, as with an alien. Data on the size of my rent have been apprehended as straight propaganda. (Then, in Moscow, at me on a visit, one of participants of tournament recognised that is more expensive for such apartment to pay and does not follow.)


I was separated from the remaining participants not only by my socialist origin, but also by two additional things. I was, in spite of entire force of Soviet chess school, deliberately weakest chess player of all authors of programs. My participation in the consideration of positions was rapidly acknowledged superfluous. Furthermore, I was only participant, who pretended in the second place in the championship (this - precisely that I promised to competent people in Moscow), nevertheless rest pretended only to the first. As a result all was wrapped up on the contrary, precisely Kaissa was engaged the first place. To me it was entrusted for Kaissa the gold (in the sense from pure gold) medal of the champion among the chess programs, returned then to the storage in ICF. In the years of reconstruction its track was mislaid in the museums of different chess clubs, where it was transferred without the agreement of the members of group of authors.


From the point of view of the [strength](Playing_Strength "Playing Strength") of chess programs of the first World championship to brag there is nothing. Kaissa played strong in the weak first category that now is not quoted even among programs for personal computers. But from the scientific point of view the first championship was breakthrough in several directions. Thin methods of reduction of search (named those who could not understand them, "brute force"), considering of a course in parallel with the opponent, debut help on the basis of databases, not trivial algorithms of distribution of time for considering — all it now seems obvious, but seriously after that in algorithms one group [Deep Blue](Deep_Blue "Deep Blue"), which has deservedly won a match with Kasparov.


The scientific community has adequately reacted to the World championships among chess programs. Game in chess has ceased to be considered as an artificial intellect problem, having given way to expert systems. As a result today in the field of an artificial intellect serious scientists work few. The matter is that the degree of quality of chess programs is easy for estimating objectively (unlike expert system). Long time chess programs were range for working off of methods of decision-making. And now, when there is no reference points, it is very difficult to understand, the method works or is simple its author is able to speak convincingly.


Difficult tasks anywhere do not share and among them a lot of such where quality of result can be estimated objectively. The majority of serious experts, before engaged in an artificial intellect also has moved. Especially their work in the field of computer and user interaction (better to say, the user interface). But it already another history.



### Official Information


Kaissa participated in the first three [world championships](World_Computer_Chess_Championship "World Computer Chess Championship") among the chess programs (1974, 1977, 1980) were occupied respectively first, second and fourth places. Officially the authors of Kaissa appear [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") and [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy"). Directly on the program worked [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), A. Baraev, [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov"), A. Leman, M. Rozenfeld.


[Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") - one of the first Soviet programmers (together with [Alexander Kronrod](Alexander_Kronrod "Alexander Kronrod"), [Alexander Brudno](Alexander_Brudno "Alexander Brudno"), [Evgenii Landis](Mathematician#Landis "Mathematician") and others). He was occupied by the programs, connected with [nuclear physics](https://en.wikipedia.org/wiki/Nuclear_physics) at [ITEP](Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics"), where he devised many algorithms which became classical. Especially the equilibrium binary trees, which in the entire world are called [AVL trees](https://en.wikipedia.org/wiki/AVL_tree) after the names of the authors - Adelson-Velsky and Landis. After short-term teaching at [MGU](Moscow_State_University "Moscow State University") he worked at IPU and VNIISI (All-Union Scientific Research Institute of Sanitary Testing) on discrete algorithms, [network planning](https://en.wikipedia.org/wiki/Network_planning_and_design) and [artificial intelligence](Artificial_Intelligence "Artificial Intelligence"). He now lives in Israel and works at [Technion](https://en.wikipedia.org/wiki/Technion_%E2%80%93_Israel_Institute_of_Technology) on [NP problems of complete tasks](https://en.wikipedia.org/wiki/NP_%28complexity%29).


[Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") - creator of original Soviet [DBMS](https://en.wikipedia.org/wiki/Database) (Data Base Management System) INES, on base of which were made many information systems of different level. He worked his entire life on programs of [pattern recognition](Pattern_Recognition "Pattern Recognition"). At present Head of *Cognitive Technologies* company, by its famous [OCR-system](https://en.wikipedia.org/wiki/Optical_character_recognition) *CuneiForm* and by the *System for Discrete Speech Recognition*. [[16]](#cite_note-16)


[Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") - author of archive system INES, by the former basis of system support many VTs on the base YeS EVM (Unified System of Computers). He is recently occupied by the problems of the user interface. Now the Director-General of DISCo (Donskoy Interactive Software Company), with a number of products for the Internet and others.


From June 14 to 20 this year (1999) in Paderborn (FRG) will helt the [world championship](WCCC_1999 "WCCC 1999") among the chess programs. As the acknowledgement of the merits of the group of authors of Kaissa in the development of chess programming to the championship, as the honorable guest, [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") is invited. One should mention that by the honorable guests of world championships in the different years they were [Claude Shannon](Claude_Shannon "Claude Shannon") (author of information theory), [Ken Thompson](Ken_Thompson "Ken Thompson") (author of the operating system [Unix](Unix "Unix")), [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (long time world chess champion).



### Kaissa: The chronology of the events


[1963](Timeline#1963 "Timeline") (1961) - beginning of the works on the first Soviet chess program in the [Institute of Theoretical and Experimental Physics](Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics") (ITEP) in the laboratory under [Alexander Kronrod's](Alexander_Kronrod "Alexander Kronrod") management. The first authors - [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), [Alexander Zhivotovsky](Alexander_Zhivotovsky "Alexander Zhivotovsky"), [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov"), A. Leman, M. Rozenfeld.


[1967](Timeline#1967 "Timeline") - first international match of chess programs. Competed the program ITEP and the program of [Stanford University](Stanford_University "Stanford University"), made under the management [John McCarthy](John_McCarthy "John McCarthy"). McCarthy is famous fact that in 1952 on the beach in San Diego together with [Alan Turing](Alan_Turing "Alan Turing") devised the word combination of "Artificial Intelligence", and fact that he is the author of the language Lisp - the first programming language, specially created for the tasks in the problems of artificial intelligence. Regulations of the [match](Stanford-ITEP_Match "Stanford-ITEP Match") - four games. From the side of Stanford played one and the same version, from the ITEP side - two, which were being distinguished by the depth of search. Moves were transferred by the telegraph once a week (this to those- that times from "yadernogo" institute!). Match continued entire year and ended with the score the 3:1 in favor of ITEP.


[1969](Timeline#1969 "Timeline") (1968) - a [letter](https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%81%D1%8C%D0%BC%D0%BE_%D0%B4%D0%B5%D0%B2%D1%8F%D0%BD%D0%BE%D1%81%D1%82%D0%B0_%D0%B4%D0%B5%D0%B2%D1%8F%D1%82%D0%B8) in support of mathematician [Esenin-Volpin](https://en.wikipedia.org/wiki/Alexander_Esenin-Volpin) (son of [poet](https://en.wikipedia.org/wiki/Sergei_Yesenin)) and his incorrect psychiatric confinement, among others signed by [Alexander Kronrod](Alexander_Kronrod "Alexander Kronrod") and [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"). As a result, the laboratory was disbanded and its major portion under [Vladimir Arlazarov's](Vladimir_Arlazarov "Vladimir Arlazarov") management, but without Kronrod, after a certain time he settled in [Institute of Control Sciences](Institute_of_Control_Sciences "Institute of Control Sciences") (ICF).


[1970](Timeline#1970 "Timeline") - the mechanic mathematical department of [MGU](Moscow_State_University "Moscow State University") finished the entire group of the students of [Alexander Kronrod](Alexander_Kronrod "Alexander Kronrod") and [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), that was being occupied in the famous seminar for discrete algorithms. Sums of the seminar:



* For [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") it was forbidden to teach in MGU
* [Alexander Kronrod](Alexander_Kronrod "Alexander Kronrod") made the record and unimprovable algorithm of searching
* E. Dinits and A. Karzanov recut the theory of flows in the networks
* A. Karzanov created the qualitatively new theory of linear programming
* Remaining participants in the seminar developed a number of unique effective algorithms for solving the classical discretized problems
* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") began the work on the algorithms of the reduction of search in the chess program.


[1972](Timeline#1972 "Timeline") - in ICF the new chess program is created, which played a correspondence match with the readers of the newspaper of [Komsomolskaya Pravda](https://en.wikipedia.org/wiki/Komsomolskaya_Pravda). From the light hand of the journalists of "Komsomolki" program obtained the name of **Kaissa**. The result of match - 1.5-0.5 in favor for the readers, which was an enormous success. Kaissa world known publicity was obtained to initiate the idea to conduct world championship among the chess programs to the [ACM](ACM "ACM").


[1974](Timeline#1974 "Timeline") on August 4 to 8, Stockholm - [first world championship](WCCC_1974 "WCCC 1974") among the chess programs. 12 programs participated. Regulations - 4 tours along the Swiss system. After obtaining 100% result, Kaissa he becomes the first champion of peace. But in the course of tournament to it was not necessary to meet with the strongest American program of that time, Chess 4.0. Took place the exponential encounter, which was ended a draw and removed a question about the validity of the victory of Kaissa. Again the victory of Kaissa confirmed the subsequent seminar, at which were presented the unique methods, realized into Kaissa.


[1977](Timeline#1977 "Timeline") July - entire team of Kaissa ([Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") et. al) passed from IPU to the institute of systems research.


[1977](Timeline#1977 "Timeline") on August 6 to 9, Toronto - [second championship](WCCC_1977 "WCCC 1977") among the chess programs. [Chess 4.0](Chess_(Program) "Chess (Program)") took revenge and became champion. Kaissa however, divides the second place with the American program [Duchess](Duchess "Duchess").


[1980](Timeline#1980 "Timeline") September - last appearance of Kaissa on the [world championship](WCCC_1980 "WCCC 1980"). Result - subdivided places from the fourth on the seventh. Delay in the utilized computational infrastructure makes further appearance of Kaissa on world championships senseless.



## Kaissa for PC


In 1990, Kaissa was re-written by a 9-member team around [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") to run on a [PC](IBM_PC "IBM PC"). Kaissa played the [2nd Computer Olympiad 1990](2nd_Computer_Olympiad#Chess "2nd Computer Olympiad") in [London](https://en.wikipedia.org/wiki/London) and became shared fourth out of eleven with four wins and two losses [[17]](#cite_note-17). [GreKo](GreKo "GreKo") author [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev") hosts a 1992 [Turbo C](C "C") version plus sources and manual, with kind permission given by its authors [[18]](#cite_note-18). Three excerpts, quoted from the Kaissa manual are given below [[19]](#cite_note-19), an introduction with historical background and authors mentioned, on Kaissa's [Search](#Search), and [Evaluation](#Evaluation), slightly edited concerning names and links. A screenshot could be found at [Meca Foro](Computer_Chess_Forums "Computer Chess Forums") [[20]](#cite_note-20).



### Introduction


from Kaissa's manual [[21]](#cite_note-21) :


You have made a good choice purchasing Kaissa chess program. It will help you to spend a free time playing the old, sophisticated and lovely game, will let you understand how computer in general can play chess and, if you would be really interested in computer chess, will be your first teacher in computer chess. Kaissa has all possibilities for that.


Kaissa is a program with a history. Its history began in 1965, when Kaissa's ancestor had played [the match](Stanford-ITEP_Match "Stanford-ITEP Match") against [Stanford University program](Kotok-McCarthy-Program "Kotok-McCarthy-Program") and had beaten it 3:1. That match was the first computer chess competition. Next event was played by Kaissa itself. It was [First World Computer Chess Championship](WCCC_1974 "WCCC 1974") in Stockholm in 1974. Kaissa was successful and became the champion. In World Computer Chess Championships in [1977](WCCC_1977 "WCCC 1977") and [1980](WCCC_1980 "WCCC 1980") Kaissa tied for the second and sixth places correspondingly. At that time it was running on [IBM-360](IBM_360 "IBM 360") like computers. Many articles and two books were published, where the results of work with Kaissa were presented. One of the books is translated into English. Almost every present chess program makes use of the ideas first published by the Kaissa's authors.


The program you purchased is the new version written in Turbo-C language for IBM-PC compatible computers. In August of 1990 it successfully played in the [Second Computer Olympiad](2nd_Computer_Olympiad#Chess "2nd Computer Olympiad") in London and tied for fourth place behind programs running on better computers. After that time several refinements were introduced in the program.


At first glance Kaissa is more complicated than regular marketed chess programs. It has many windows, bushy menus and various words on the screen unusual for chess players. But if computer is not only a toy for you, but also a working tool (regardless of a particular goal you are using it for), the skill, you obtain while working with Kaissa, will be very helpful in your main work on computer.


It is due to the fact that Kaissa is designed according to the new computer usage standards. These standards are followed by all good software (except may be the simplest game programs). Kaissa is developed in Soviet-American Joint Venture ParaGraph, which is well known for other first class software products, and we hope that you have already appreciated them in your work.


The original Kaissa's authors at the very beginning of her life were [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov"), [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), and [Alexander Zhivotovsky](Alexander_Zhivotovsky "Alexander Zhivotovsky") under [Kronrod's](Alexander_Kronrod "Alexander Kronrod") authority in [ITEP](Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics"). Then the work on Kaissa was continued in the [Institute of Control Sciences](Institute_of_Control_Sciences "Institute of Control Sciences") and in the Institute for Systems Studies by Georgy Adelson-Velsky, Vladimir Arlazarov and [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy").


The Kaissa you see now was developed in ParaGraph by Mikhail Donskoy, A.V. Dubets, M.YU. Karaev, V.A. Kokin, D.V. Posvyansky, I.R. Shabalin, A.G. Sidorovich, and E.A. Sokolinsky. Chess assistance was rendered by Alexander Bitman.



### Move Selection Algorithm


Kaissa's [Search](Search "Search") [[22]](#cite_note-22):


If you want not only to play with Kaissa but also to understand, even a little bit, the principles which Kaissa uses for move selection (and that possibility is just what makes Kaissa to differ so much from other chess programs!), you have to read this and the following sections. If, on the other hand, Kaissa is just a chess partner for you and you do not care how it selects a move, you can skip these sections. Kaissa selects a move using the [tree search algorithm](Search "Search"). That means that it considers all moves feasible in the position on the board, and all opponent's replies to them and all replies to these replies and so on up till a certain [depth](Depth "Depth") where Kaissa [evaluates](Evaluation "Evaluation") positions. Let us call all that "the [search tree](Search_Tree "Search Tree")". The position, where Kaissa should select the move is the [root](Root "Root") of the "search tree", all the possible continuations of the position are the branches, and the positions where Kaissa does not search any of the moves are the [leaves](Leaf_Node "Leaf Node"). Theoretically speaking, we may create the "search tree" of the whole game, where the leaves are the positions with the known result (the [checkmate](Checkmate "Checkmate"), [stalemate](Stalemate "Stalemate"), or the position where the rule of the moves [repetition](Repetitions "Repetitions") should be used, or the [50 moves-rule](Fifty-move_Rule "Fifty-move Rule").). After this tree is built, one can make one move back and evaluate all the positions in which the game will be finished in one move. The result depends on the one hand on the result of the game in leaf positions and on the other hand on wish of the party, which has a turn to move, to choose the best opportunity. If to ascribe to each leaf position a value such as: the whites win - 1, the Blacks win - -1, draw - 0, it is quite obvious that it is more profitable while playing for white to choose the maximum continuation, and while playing for black - the minimum one. Thus the position where it is the Whites' turn to move will be won in case if one continuation will be evaluated as 1, and it will be the lost if all the possible continuations will be evaluated as -1. Then by [moving back](Retrograde_Analysis "Retrograde Analysis") one can evaluate all the positions up to the initial one and to find the best way to play in all the positions. This principle was developed by [Zermelo](Ernst_Zermelo "Ernst Zermelo") at the beginning of this century and it was called the [MiniMax](Minimax "Minimax") principle. Unfortunately it has a sufficient drawback. The tree of the chess game is so large that though it is possible to search the whole tree it takes ages to do it. And already in 1948 [Claude Shannon](Claude_Shannon "Claude Shannon"), the classic of the informatics who took interest in chess, proposed the algorithm, according to which the leaf positions of the search tree are not deemed to coincide with the leaf positions of the game tree. One of the simplest way to shorten the tree is to cut it off at the given depth. In this case the leaf positions of the new tree are all the positions, which are possible to achieve by the given number of [plies](Ply "Ply") from the position on the board. 


Thus the problem arises - how to evaluate these new leaf positions. These evaluations should reflect the [material](Material "Material") and positional advantages of one of the sides. Each chess program has a procedure for computing the evaluation function. When all the leaf positions are evaluated one can use the MiniMax principle for the evaluation of the position on the board and the move, achieving the minimum or the maximum (it depends on the program's playing color), is chosen as the best in the position. The quality of the algorithm which computes the evaluation function affects greatly the program's playing strength.
To evaluate a position Kaissa, as many other programs, uses the search too, but in this evaluation search not all moves are feasible but only forcing ones - [captures](Captures "Captures"), [checks](Check "Check") and replies to checks. That is the reason for Russian name of this search - forcing variation or FV (in the English language literature it is usually called [quiescence analysis](Quiescence_Search "Quiescence Search")). In every FV position each side chooses what is more profitable for it either to prolong FV making forcing moves or to be satisfied by the value of the static evaluation function of the position. The static evaluation function is computed as a sum of material and positional components, and the material component is always more important than positional. The material evaluation is computed as the sum of material weights of all pieces on the board, counting weights for pieces of the side to move as positive values and for pieces of the other side as negative. 


The positional evaluation is computed as the sum of different factors with weights. They are enlisted in the [Appendix B](Kaissa#Evaluation "Kaissa"). The difference between the static evaluation of a position, which is computed by special function, and the value of the position, which is defined by minimax, is worth noting. For example, the static material evaluation of a position in which there is equality of pieces but the queen is under attack, is zero, but its material value is minus queen. Of course, the value of any position is the static evaluation of some, may be another, position. In our example, the value of the position was equal to the static evaluation after the queen capture.


The so called [alpha-beta algorithm](Alpha-Beta "Alpha-Beta") cuts the search off essentially. Its idea is following: if the White has found already some satisfactory move (for example the move which wins a pawn) and started searching another move to which the Black has found the refutation, which does not loss anything, the Blacks does not need to search other moves. The point is that the White will never choose the second move because it is anyway worse then the previous one. So there is no use to waste time on thinking over the bad move too carefully. Such refutation moves are called "killers", because they "kill" the previous bad move. The better is the [order](Move_Ordering "Move Ordering") of move searching from intermediate positions of the search and the more exactly the borders of the current position evaluation are defined, the more effective are alpha-beta cutoffs. So in Kaissa and in some other chess programs the [artificial narrowing](Aspiration_Windows "Aspiration Windows") of the evaluation borders is used, i.e. the existence of a move without any material losses is taken for granted. And in this case the search is going much faster.


The selection algorithm of Kaissa is a [sequence of MiniMax tree searches](Iterative_Deepening "Iterative Deepening") at different depths. They are called iterations. First and the only obligatory iteration for all Kaissa levels is the preliminary FV0 search. It is just FV after each possible move in the position on the board. All moves are ordered according to the results of this search and if Kaissa playing strength level is set to be FV0, Kaissa makes the first move of that order. For all other levels it repeats the procedure for the opponent's moves after the best FV0 move. This search is called FV1.


On all other levels Kaissa uses other searches as well. Every one of the searches is controlled by two parameters (X.Y). These parameters define which positions may be evaluated by FV search. The position may be evaluated only if two conditions are held. The first condition is that the number of plies (moves of each side) leading from the position on the board (the root position of the tree) to the current one should be no less than X and the number of non-forcing moves from them should not be less than Y. The exact definition of non-forcing moves here is a little bit complicated to avoid ever-looping of the program, but roughly speaking these are moves which are not captures, checks or replies to check.


The larger are X and Y the stronger Kaissa plays on the one hand but the more time it spends on move selection on the other hand. It should be taken into account when you choose the level of Kaissa thinking. Unfortunately exact estimations of thinking time are impossible because of the difference in computing power of various computers. On IBM-PC/AT, with the speed five times more than on the standard XT, Kaissa on the default level (3.1) makes a move in 20 seconds in average, on the tournament level (5.1) it makes a move in 6 minutes, on the speed chess level FV0 - in three seconds. However these are average figures, the exact thinking time depends on a particular position. The more forcing moves (especially checks) are possible in a position, the more time Kaissa spends on thinking.


At every search iteration Kaissa first tries to guess (using FV0 and previous iterations) the material value of the root position (and, which is the same, the material value of the best move) and makes narrow borders for the root position value. That is called aspiration search. If Kaissa guesses right, which is about 90% of cases, the search is sped up greatly. If Kaissa guesses wrong, it has to redo the search with the different material borders. Every such part of search is called Round. The rounds are over when Kaissa determines the right material value of the root position.


To accelerate search Kaissa may also use the transposition table. In this table all the information on the results of search from all the searching positions is entered. If the current position is found in the table, under under certain conditions the information from the table may be used instead of the new search. In any case the information on what move was the best in such a position before, may be used, and the alpha-beta procedure ef-fectiveness may be bettered.


More details on computer chess algorithms you can find in the books "[Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")" ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), Springer-Verlag, 1977, "[Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")" ed. [Tony Marsland](Tony_Marsland "Tony Marsland") & [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), Springer-Verlag 1990 and "Algorithms for Games." by [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") and [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy"), Springer-Verlag 1988.



### Evaluation


[Evaluation](Evaluation "Evaluation") Factors and their Weights [[23]](#cite_note-23) :



### Material


[Material](Material "Material") [point values](Point_Value "Point Value"):





|  Piece
 |  Value
 |
| --- | --- |
|  King
 |  255
 |
|  Queen
 |  19
 |
|  Rook
 |  10
 |
|  Bishop
 |  7
 |
|  Knight
 |  7
 |
|  Pawn
 |  2
 |


### Positional Weights




|  Feature
 |  Weight
 |  Remarks
 |
| --- | --- | --- |
| [Isolated pawns](Isolated_Pawn "Isolated Pawn") |  -10
 |  for each pawn
 |
| [Isolated pawns](Isolated_Pawn "Isolated Pawn") on semiopen files
 |  -10
 |  for each pawn to add up to the previous point
 |
| [Doubled pawns](Doubled_Pawn "Doubled Pawn") |  -5
 |  for each pawn beginning with the second on the file, tripled pawns are evaluated as -10
 |
| [Phalanga](Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)") |  20
 |  for each Phalanga is two pawns on the neighboring files and the same rank. The three neighboring pawns, two phalangs
 |
| [Pawns in the center](Pawn_Center "Pawn Center") |  20
 |  for each square [[24]](#cite_note-24) |
| [Pawn attacks](Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") |  1
 |  for every attacked square
 |
|  Pawns attacks on [center](Center "Center") |  10
 |  for every attacked square in the center
 |
|  Strong Square
 |  20
 |  for each square, the strong square is the one, which is attacked by a pawn of one color and never may be attacked by a pawn of opposite color [[25]](#cite_note-25) |
| [Backward Pawn](Backward_Pawn "Backward Pawn") |  10
 |  for each pawn, these are pawns behind the strong squares
 |
|  Pawn attacks adjacent to enemy king
 |  20
 |  for each square
 |
|  Pawns blocked by enemy on F and C files
 |  -50
 |  black pawn on f7 and c7 squares, white - on f2 and c2 squares
 |
|  Pawns block on D and E files
 |  -50
 |  black pawn on d7 and e7 squares, white - on d2 and e2 squares
 |
|  Bishop/knight attacks on enemy rook/queen
 |  10
 |  |
| [Rook on seventh rank](Rook_on_Seventh "Rook on Seventh") |  40
 |  |
|  Rook on seventh in endgame
 |  20
 |  |
|  Profitable attacks on bound enemy pieces
 |  300
 |
| [Double profitable attacks](Double_Attack "Double Attack") |  10 000
 |  on the pieces of the enemy
 |
|  Bishops and knights at initial squares
 |  -15
 |  for each piece
 |
| [Knights on strong squares](Outposts "Outposts") |  20
 |  |
|  Bishops on strong squares
 |  20
 |  |
| [Kings opposition](Opposition "Opposition") in endgame
 |  15
 |  |
| [Piece attacks on center](Center_Control "Center Control") |  10
 |  for each attack
 |
| [Rooks on open files](Rook_on_Open_File "Rook on Open File") |  35
 |  for every rook
 |
| [Rooks on semiopen files](Rook_on_Open_File "Rook on Open File") |  25
 |  for each rook
 |
|  Rooks attacks on open files
 |  10
 |  |
|  Rooks attacks on semiopen files
 |  5
 |  |
| [Two bishops exist](Bishop_Pair "Bishop Pair") |  20
 |  |
|  Knight and Queen exist
 |  10
 |  |
|  Knights in the center
 |  20
 |  |
|  Pieces attacked by bishop
 |  15
 |  |
|  Bound pieces
 |  20
 |  |
| [Rooks behind passed pawns](Tarrasch_Rule "Tarrasch Rule") |  30/20
 |  |
| [Castle right](Castling_Rights "Castling Rights") lost
 |  -60
 |  |
| [Castle made](Castling "Castling") |  30
 |  |
|  Bishop attacks an enemy piece
 |  15
 |  |
|  Queen's mobility from the king square
 |  -2
 |  It characterize [king's security](King_Safety "King Safety") |
|  Bishop/knight attacks adjacent to king
 |  -10
 |  for each attack
 |
|  Bishop/knight attacks on a strong square
 |  20
 |  for each attack
 |
|  Pieces [mobility](Mobility "Mobility") |  1
 |  for each attack
 |
| [Passed pawn](Passed_Pawn "Passed Pawn") [blocks](Blockade_of_Stop "Blockade of Stop") |  -15
 |  |
|  Profitable attacks on passed pawn blocks
 |  10
 |  for each attack
 |
|  Attacks on passed pawns [trajectories](Pawn_Spans "Pawn Spans") |  5
 |  for each attack
 |
|  King distance from passed pawns in the endgame
 |  -2
 |  for each square
 |
|  King distance
 |  -100
 |  |
|  King distance from center
 |  -200
 |  |


## See also


* [ITEP Chess Program](ITEP_Chess_Program "ITEP Chess Program")
* [Scotch versus Vodka](David_Levy#ScotchVersusVodka "David Levy") - one of [David Levy's](David_Levy "David Levy") bets
* [Bitboard History](Bitboards#BitboardHistory "Bitboards")
* [History of Computer Chess](History "History")
* [History of Null Move Pruning](Null_Move_Pruning#History "Null Move Pruning")
* [Kaissa](Evaluation_Overlap#Kaissa "Evaluation Overlap") from [Evaluation Overlap](Evaluation_Overlap "Evaluation Overlap") by [Mark Watkins](Mark_Watkins "Mark Watkins")
* [Walter Faxon](Walter_Faxon "Walter Faxon")


## Namesakes


* [Kaissa](Kaissa_(BY) "Kaissa (BY)") by [Vladimir Yelin](Vladimir_Yelin "Vladimir Yelin")


## Publications


### 1970 ...


* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov") (**1974**). *Methods of strengthening chess programs.* in Problems of Cybernetic, No. 29 , pp. 167-168


 [Г.М. Адельсон-Вельский](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [В.Л. Арлазаров](Vladimir_Arlazarov "Vladimir Arlazarov") (**1974**). *Методы усиления шахматных программ.*/ Сб. Проблемы кибернетики №29, стр. 167-168
* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1974**). *About the program playing chess.* in Problems of Cybernetic, No. 29 , pp. 169-200


 [М.В. Донской](Mikhail_Donskoy "Mikhail Donskoy") (**1974**). *О программе играющей в шахматы.*/ Сб. Проблемы кибернетики №29, стр. 169-200
* [Ya. Yu. Gol'fand](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=96114), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Implementation of the opening book for the chess program.* in Problems of Cybernetic, No. 29 , pp. 201-210


 Я.Ю. Гольфанд, [А.Л. Футер](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Реализация дебютной справочной для шахматной программы.*/ Сб. Проблемы кибернетики №29, стр. 201-210
* [Edward Komissarchik](Edward_Komissarchik "Edward Komissarchik"), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1974**). *On the analysis of the queen endgame using a computer.* in Problems of Cybernetic, No. 29 , pp. 211-220


 [Э.А. Комиссарчик](Edward_Komissarchik "Edward Komissarchik"), [А.Л. Футер](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Об анализе ферзевого эндшпиля при помощи ЭВМ.*/ Сб. Проблемы кибернетики №29, стр. 211-220, English translation by [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), revised in [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* R. Guter, [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1974**). *The machine plays chess.* in [Kvant](https://en.wikipedia.org/wiki/Kvant_(magazine)), No. 11, 12, pp. 17-22, 34-38


 Р.С. Гутер, [М.В. Донской](Mikhail_Donskoy "Mikhail Donskoy") (**1974**). *Машина играет в шахматы.* в журн. [Квант](https://en.wikipedia.org/wiki/Kvant_(magazine)) № 11, 12, стр. 17-22, 34-38
* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy"), V. Khenkin (**1974**). *Stockholm evenings. The nights of Kaissa.* in [64](https://en.wikipedia.org/wiki/64_(magazine)), No. 33, pp. 4-7


 [М.В. Донской](Mikhail_Donskoy "Mikhail Donskoy"), В. Хенкин (**1974**). *Стокгольмские вечера. Ночи Каиссы.* в журн. [64](https://en.wikipedia.org/wiki/64_(magazine)) № 33, стр. 4-7
* V. Tumanov, [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1974**). *The tale has come true.* [Shakhmaty v SSSR](https://en.wikipedia.org/wiki/Shakhmaty_v_SSSR), No. 10, 16–17


 В. Туманов, [Ю. Авербах](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1974**). *Сказка стала былью.* [Шахматы в СССР](https://en.wikipedia.org/wiki/Shakhmaty_v_SSSR) № 10, 16–17
### 1975 ...


* [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1975**). *Kaissa's four victories.* in [Znanie - sila](https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%E2%80%94_%D1%81%D0%B8%D0%BB%D0%B0), No. 1, pp. 30-32


 [Ю. Авербах](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1975**). *Четыре победы Каиссы.* в журн. [Знание - сила](https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%E2%80%94_%D1%81%D0%B8%D0%BB%D0%B0), № 1, стр. 30-32
* V. Khenkin (**1975**). *Kaissa is the world champion.* in [Nauka i Zhizn](https://en.wikipedia.org/wiki/Nauka_i_Zhizn), No. 1, pp. 118-124


 В. Хенкин (**1975**). *"Каисса" - чемпион мира.* в журн. [Наука и жизнь](https://en.wikipedia.org/wiki/Nauka_i_Zhizn), № 1, стр. 118-124
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1975**). *Some Methods of Controlling the Tree Search in Chess Programs*. [Artificial Ingelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp. 361-371. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") [[26]](#cite_note-26)
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), New York, N.Y. ISBN 0-125-17250-8.


 Chapter VIII. Kaissa
* [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1976**). *The bet.* in [Znanie - sila](https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%E2%80%94_%D1%81%D0%B8%D0%BB%D0%B0), No. 8, pp. 53-54


 [Ю. Авербах](https://en.wikipedia.org/wiki/Yuri_Averbakh) (**1976**). *Пари.* в журн. [Знание - сила](https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%E2%80%94_%D1%81%D0%B8%D0%BB%D0%B0), № 8, стр. 53-54
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1977**). *On the Structure of an Important Class of Exhaustive Problems and Methods of Search Reduction for them*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
* [Peter Jennings](Peter_Jennings "Peter Jennings") (**1978**). *The Second World Computer Chess Championships - Where KAISSA Founders on a Bug and CHESS 4.6 Conquers All*. » [WCCC 1977](WCCC_1977 "WCCC 1977"), [Chess](Chess_(Program) "Chess (Program)")
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1978**). *Chess game programming.* in [Herald of the RAoS](https://en.wikipedia.org/wiki/Herald_of_the_Russian_Academy_of_Sciences), No. 4 , pp. 82-91, [doc](https://www.ras.ru/FStorage/download.aspx?Id=6ec533b1-a7f6-42a7-82bd-48dffec3ea0d)


 [Г.М. Адельсон-Вельский](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [В.Л. Арлазаров](Vladimir_Arlazarov "Vladimir Arlazarov"), [М.В. Донской](Mikhail_Donskoy "Mikhail Donskoy") (**1978**). *Программирование шахматной игры.*/ Сб. [Вестник РАН](https://en.wikipedia.org/wiki/Herald_of_the_Russian_Academy_of_Sciences), №4, стр. 82-91, [doc](https://www.ras.ru/FStorage/download.aspx?Id=6ec533b1-a7f6-42a7-82bd-48dffec3ea0d)
### 1980 ...


* [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1980**). *From Russia with Games*. [Personal Computing, Vol. 4, No. 5](Personal_Computing#4_5 "Personal Computing"), pp. 77
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**1981**). *A brighter future for Soviet computer chess?* [ICCA Newsletter, Vol. 4, No. 1](ICGA_Journal#4_1 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Marsland-Newborn-1981.pdf)
* [Г.М. Адельсон-Вельский](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [В.Л. Арлазаров](Vladimir_Arlazarov "Vladimir Arlazarov"), [А.Р. Битман](Alexander_Bitman "Alexander Bitman"), [М.В. Донской](Mikhail_Donskoy "Mikhail Donskoy") (**1983**). *Машина играет в шахматы*. [pdf](http://genes1s.net/files/kaissa.pdf) (book with detailed explanations of Kaissa algorithms, language: Russian)
* [Evgenii Landis](Mathematician#Landis "Mathematician"), [Isaak Yaglom](Mathematician#Yaglom "Mathematician") (**1987**). *Remembering A.S. Kronrod*. (**2002**). Translation by [Viola Brudno](http://www.translatorscafe.com/cafe/member16949.htm), Edited by [Walter Gautschi](Mathematician#WaGautschi "Mathematician"), [ps](https://www.cs.purdue.edu/homes/wxg/Kronrod.ps)
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1988**). *[Algorithms for Games](https://link.springer.com/book/10.1007%2F978-1-4612-3796-9)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Michael Brudno](http://www.cs.toronto.edu/%7Ebrudno/) (**2000**). *Competitions, Controversies, and Computer Chess*, [pdf](http://www.cs.toronto.edu/%7Ebrudno/essays/cchess.pdf)


## Forum Posts


* [Kaissa & Botvinik](https://groups.google.com/d/msg/rec.games.chess.computer/6fW4CaesCVI/LCQcjEpaI4kJ) by [Shay Bushinsky](Shay_Bushinsky "Shay Bushinsky"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 16, 1997
* [Re: What Chess programs existed in the '60s?](http://www.stmintz.com/ccc/index.php?id=105999) by [David Blackman](David_Blackman "David Blackman"), [CCC](CCC "CCC"), April 14, 2000
* [KAISSA for PC, I'm the proud owner](http://www.stmintz.com/ccc/index.php?id=210429) by Joshua Lee, [CCC](CCC "CCC"), January 28, 2002
* [Markoff -- Botvinnik -- Kaissa -- Hsu -- ABC -- Berliner](http://www.stmintz.com/ccc/index.php?id=299987) by [Walter Faxon](Walter_Faxon "Walter Faxon"), [CCC](CCC "CCC"), June 09, 2003
* [Authors of Kaissa on quiscence search](http://www.stmintz.com/ccc/index.php?id=389134) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 26, 2004 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Re: La Máquina Preservadora. Programas de Ajedrez](http://www.foro.meca-web.es/viewtopic.php?f=9&t=72&start=50#p8496) by Tibono, [Meca Foro](Computer_Chess_Forums "Computer Chess Forums"), October 03, 2015 (Spanish)


## External Links


### Chess Program


* [Kaissa's ICGA Tournaments](http://www.game-ai-forum.org/icga-tournaments/program.php?id=40)
* [Kaissa from Wikipedia](https://en.wikipedia.org/wiki/Kaissa)
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm)] by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) [[27]](#cite_note-27)
* [KAISSA](http://www.chess.com/blog/billwall/kaissa-computer-chess-program) by [Bill Wall](index.php?title=Bill_Wall&action=edit&redlink=1 "Bill Wall (page does not exist)"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), December 29, 2011
* [GreKo - Download](http://sites.google.com/site/grekochess/) has a Kaissa [PC](IBM_PC "IBM PC") port in [Turbo C](C "C") from 1992, hosted by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev")
* ["Каисса" - Историю программы рассказывает один из ее создателей Михаил Донской](https://www.computer-museum.ru/games/kaissa1.htm) (Russian)
* [История компьютерных игр](http://www.computer-museum.ru/games/donchess.htm) from the [Russian Virtual Computer Museum](Russian_Virtual_Computer_Museum "Russian Virtual Computer Museum") (Russian)
* [Компьютерные программы, как конец спортивных шахмат](https://www.svoboda.org/a/24203756.html) (Russian)
* [Михаил Донской: "Шахматные программы перестали быть искусственным интеллектом, как только научились прилично играть"](https://gorod.tomsk.ru/index-1232431930.php) (Russian)
* [Михаил Донской: Жизненный цикл программиста - ПОЛИТ.РУ](http://www.polit.ru/article/2008/08/20/programmist/) (Russian) [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") - [The life cycle of a programmer](http://translate.google.com/translate?sl=ru&tl=en&js=n&prev=_t&hl=en&ie=UTF-8&u=http%3A%2F%2Fwww.polit.ru%2Farticle%2F2008%2F08%2F20%2Fprogrammist%2F) translated by [Google Translate](https://en.wikipedia.org/wiki/Google_Translate), [polit.ru](https://www.facebook.com/politru) August 20, 2008
* [Развитие искусственного интеллекта в шахматных программах](http://acm.mipt.ru/twiki/bin/view/Algorithms/ArlazarovChessHistory) (Russian)
* [Владимир Арлазаров: «Игры помогли нам понять, как человек решает трудные логические задачи»](https://arzamas.academy/materials/2233) (Russian)
* Photo: 1) In the computer room of the Institute of Control Sciences in August 1974 [[2]](https://www.facebook.com/AdelsonVelsky/photos/a.316678225153119/316678128486462/) and (presumably) in December 1975 [[3]](https://www.facebook.com/photo/?fbid=936618083023458&set=a.768126203205981) [[4]](https://ruchess.ru/upload/7tur/14_4%20Untitled-5R_resize.jpg). 2) Kaissa's Gold Medal [[5]](https://ruchess.ru/upload/7tur/14_5%20%D0%A8_0032-2.jpg).


### Misc


* [Caissa (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Caissa)
* [Caïssa from Wikipedia](https://en.wikipedia.org/wiki/Ca%C3%AFssa)


## References


1. [↑](#cite_ref-1) An early illustration of [Jones'](https://en.wikipedia.org/wiki/William_Jones_%28philologist%29) Caïssa, [Caïssa from Wikipedia](https://en.wikipedia.org/wiki/Ca%C3%AFssa)
2. [↑](#cite_ref-2) [Five ICL computers for the Soviet Union](https://www.computer-museum.ru/articles/materialy-mezhdunarodnoy-konferentsii-sorucom-2017/1733/) (Russian)
3. [↑](#cite_ref-3) [IBM or ICL?](https://a-jelly.livejournal.com/429560.html) (Russian)
4. [↑](#cite_ref-4) [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1975**). *Some Methods of Controlling the Tree Search in Chess Programs*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp. 361-371. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
5. [↑](#cite_ref-5) [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1977**). *On the Structure of an Important Class of Exhaustive Problems and Methods of Search Reduction for them*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1").
6. [↑](#cite_ref-6) [Kaissa at the 1st World Computer Chess Championship in Stockholm](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbd92710), Photo by [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
7. [↑](#cite_ref-7) [Tony Marsland](Tony_Marsland "Tony Marsland"), [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**1981**). *A brighter future for Soviet computer chess?* [ICCA Newsletter, Vol. 4, No. 1](ICGA_Journal#4_1 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Marsland-Newborn-1981.pdf)
8. [↑](#cite_ref-8) [Arlazarov, Uskov, and Donskoy in Moscow 1980](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc15a4a7), Gift of [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
9. [↑](#cite_ref-9) [Tony Marsland](Tony_Marsland "Tony Marsland"), [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**1981**). *A brighter future for Soviet computer chess?* [ICCA Newsletter, Vol. 4, No. 1](ICGA_Journal#4_1 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Marsland-Newborn-1981.pdf)
10. [↑](#cite_ref-10) [Computer chess pioneer Adelson-Velsky at chalkboard in Moscow 1980](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc168f00), Photo by [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
11. [↑](#cite_ref-11) [История “Каиссы” Михаил Донской](https://www.computer-museum.ru/games/kaissa1.htm) see [History of Kaissa](#HistoryofKaissa)
12. [↑](#cite_ref-12) [A. Baraev](https://www.facebook.com/AdelsonVelsky/photos/a.316678225153119/316678128486462/) In the photo at the ICL computer console together with Marianna Rozenfeld (the names are indicated in the photo in the magazine "64" 1974, №33, p.1, [link](http://publ.lib.ru/ARCHIVES/SH/%27%2764_-_shahmatnoe_obozrenie%27%27/_%27%2764_-_shahmatnoe_obozrenie%27%27.html#1974) )
13. [↑](#cite_ref-13) [Andrey Leman](https://ichi.pro/ru/zabytaa-istoria-sovetskogo-ii-82419796384991) (Russian)
14. [↑](#cite_ref-14) [Marianna Rozenfeld](https://www.facebook.com/AdelsonVelsky/photos/a.316678225153119/316678128486462/) In the photo at the ICL computer console together with A. Baraev (the names are indicated in the photo in the magazine "64" 1974, №33, p.1, [link](http://publ.lib.ru/ARCHIVES/SH/%27%2764_-_shahmatnoe_obozrenie%27%27/_%27%2764_-_shahmatnoe_obozrenie%27%27.html#1974) )
15. [↑](#cite_ref-15) [История “Каиссы” Михаил Донской](https://www.computer-museum.ru/games/kaissa1.htm) from [Russian Virtual Computer Museum](Russian_Virtual_Computer_Museum "Russian Virtual Computer Museum")
16. [↑](#cite_ref-16) [Cognitive Technologies: Главная](http://www.cognitive.ru/)
17. [↑](#cite_ref-17) [Zsuzsa Horváth](Zsuzsa_Horv%C3%A1th "Zsuzsa Horváth") (**1990**). *Report on the 2nd Computer Olympiad*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal") » [2nd Computer Olympiad](2nd_Computer_Olympiad#Chess "2nd Computer Olympiad")
18. [↑](#cite_ref-18) [GreKo - Download](http://sites.google.com/site/grekochess/)
19. [↑](#cite_ref-19) KAISSA.zip/ks\_sell/KAIS1.DOC
20. [↑](#cite_ref-20) [Re: La Máquina Preservadora. Programas de Ajedrez](http://www.foro.meca-web.es/viewtopic.php?f=9&t=72&start=50#p8496) by Tibono, [Meca Foro](Computer_Chess_Forums "Computer Chess Forums"), October 03, 2015 (Spanish)
21. [↑](#cite_ref-21) Excerpt from KAISSA.zip/ks\_sell/KAIS1.DOC - Introduction
22. [↑](#cite_ref-22) Excerpt from KAISSA.zip/ks\_sell/KAIS1.DOC - 3.1. Short description of the move selection algorithm
23. [↑](#cite_ref-23) Excerpt from KAISSA.zip/ks\_sell/KAIS1.DOC - Appendix B. Evaluation function's parameters and their weights
24. [↑](#cite_ref-24) The center are the squares e4, d4, e5, d5 and e6, d6 for the White and e3 and d3 for the Black accordingly
25. [↑](#cite_ref-25) Not every square of the board may be the strong one. The squares which may be strong for the White are the following: b6, b7, c5, c6, c7, d5, d6, d7, e5, e6 ,e7, f5, f6, f7, g6, g7. For the Black the symmetry holds
26. [↑](#cite_ref-26) [Method of Analogies??](http://www.stmintz.com/ccc/index.php?id=19469) by Bruce Cleaver, [CCC](CCC "CCC"), May 29, 1998
27. [↑](#cite_ref-27) [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**







 
