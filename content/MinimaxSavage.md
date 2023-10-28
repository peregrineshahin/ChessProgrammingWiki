---
title: MinimaxSavage
---
**[Home](Home "Home") \* [Search](Search "Search") \* Minimax**



 [](https://en.wikipedia.org/wiki/Little_Machine_Constructed_by_Minimax_Dadamax_in_Person) [Max Ernst](Category:Max_Ernst "Category:Max Ernst") - [Little Machine Constructed](https://en.wikipedia.org/wiki/Little_Machine_Constructed_by_Minimax_Dadamax_in_Person) by [Minimax Dadamax in Person](https://en.wikipedia.org/wiki/Little_Machine_Constructed_by_Minimax_Dadamax_in_Person), 1919-1920 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Minimax**,  

an algorithm used to determine the [score](Score "Score") in a [zero-sum](https://en.wikipedia.org/wiki/Zero-sum) game after a certain number of moves, with best play according to an [evaluation](Evaluation "Evaluation") function. The algorithm can be explained like this: In a [one-ply](Ply "Ply") search, where only move sequences with length one are examined, the side to move (max player) can simply look at the [evaluation](Evaluation "Evaluation") after playing all possible [moves](Moves "Moves"). The move with the best evaluation is chosen. But for a two-[ply](Ply "Ply") search, when the opponent also moves, things become more complicated. The opponent (min player) also chooses the move that gets the best score. Therefore, the score of each move is now the score of the worst that the opponent can do. 




### Contents


* [1 History](#history)
* [2 Implementation](#implementation)
* [3 Negamax](#negamax)
* [4 See also](#see-also)
	+ [4.1 Search](#search)
	+ [4.2 People](#people)
* [5 Selected Publications](#selected-publications)
	+ [5.1 1920 ...](#1920-...)
	+ [5.2 1940 ...](#1940-...)
	+ [5.3 1950 ...](#1950-...)
	+ [5.4 1960 ...](#1960-...)
	+ [5.5 1970 ...](#1970-...)
	+ [5.6 1980 ...](#1980-...)
	+ [5.7 1990 ...](#1990-...)
	+ [5.8 2000 ...](#2000-...)
	+ [5.9 2010 ...](#2010-...)
	+ [5.10 2020 ...](#2020-...)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






[Jaap van den Herik's](Jaap_van_den_Herik "Jaap van den Herik") thesis (1983) <a id="cite-note-2" href="#cite-ref-2">[2]</a> contains a detailed account of the known publications on that topic. It concludes that although [John von Neumann](John_von_Neumann "John von Neumann") is usually associated with that concept ([1928](Timeline#1928 "Timeline")) <a id="cite-note-3" href="#cite-ref-3">[3]</a> , [primacy](https://en.wikipedia.org/wiki/Primacy_of_mind) probably belongs to [Émile Borel](Mathematician#Borel "Mathematician"). Further there is a conceivable claim that the first to credit should go to [Charles Babbage](Mathematician#Babbage "Mathematician") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. The original minimax as defined by Von Neumann is based on exact values from [game-terminal positions](Terminal_Node "Terminal Node"), whereas the minimax search suggested by [Norbert Wiener](Norbert_Wiener "Norbert Wiener") <a id="cite-note-5" href="#cite-ref-5">[5]</a> is based on [heuristic evaluations](Evaluation "Evaluation") from positions a few moves distant, and far from the end of the game.



## Implementation


Below the pseudo code for an indirect [recursive](Recursion "Recursion") [depth-first search](Depth-First "Depth-First"). For clarity [move making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") before and after the recursive call is omitted.




```

int maxi( int depth ) {
    if ( depth == 0 ) return evaluate();
    int max = -oo;
    for ( all moves) {
        score = mini( depth - 1 );
        if( score > max )
            max = score;
    }
    return max;
}

int mini( int depth ) {
    if ( depth == 0 ) return -evaluate();
    int min = +oo;
    for ( all moves) {
        score = maxi( depth - 1 );
        if( score < min )
            min = score;
    }
    return min;
}

```

## Negamax


Usually the [Negamax](Negamax "Negamax") algorithm is used for simplicity. This means that the evaluation of a position is equivalent to the negation of the evaluation from the opponent's viewpoint. This is because of the zero-sum property of chess: one side's win is the other side's loss.



## See also


### Search


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Minimax (program)](Minimax_(program) "Minimax (program)")
* [Negamax](Negamax "Negamax")
* [Search Pathology](Search_Pathology "Search Pathology")
* [Theorem-Proving and M & N procedure](James_R._Slagle#TheoremProving "James R. Slagle")
* [Theorem-Proving from Five-Year Plan](Jack_Good#TheoremProving "Jack Good")


### People


* [John von Neumann](John_von_Neumann "John von Neumann")
* [Claude Shannon](Claude_Shannon "Claude Shannon")
* [Norbert Wiener](Norbert_Wiener "Norbert Wiener")


## Selected Publications


### 1920 ...


* [Émile Borel](Mathematician#Borel "Mathematician") (**1921**). *La théorie du jeu et les équations intégrales à noyau symétrique*. Comptes Rendus de Académie des Sciences, Vol. 173, pp. 1304-1308, English translation by [Leonard J. Savage](Mathematician#LJSavage "Mathematician") (**1953**). *[The Theory of Play and Integral Equations with Skew Symmetric Kernels](Minimax#Savage "Minimax")*.
* [John von Neumann](John_von_Neumann "John von Neumann") (**1928**). *[Zur Theorie der Gesellschaftsspiele](http://gdz.sub.uni-goettingen.de/dms/load/img/?IDDOC=29357)*. Berlin <a id="cite-note-6" href="#cite-ref-6">[6]</a>


### 1940 ...


* [John von Neumann](John_von_Neumann "John von Neumann"), [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) (**1944**). *[Theory of Games and Economic Behavior](https://en.wikipedia.org/wiki/Theory_of_Games_and_Economic_Behavior)*. Princeton University Press, Princeton, NJ.
* [Norbert Wiener](Norbert_Wiener "Norbert Wiener") (**1948**). *[Cybernetics or Control and Communication in the Animal and the Machine](http://www.amazon.com/gp/reader/026273009X/ref=sib_dp_pt#reader-link)* - MIT Press, Cambridge, MA.


### 1950 ...


* [Claude Shannon](Claude_Shannon "Claude Shannon") (**1950**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*, Philosophical Magazine, Ser.7, Vol. 41, No. 314 - March 1950
* [Hermann Weyl](Mathematician#Weyl "Mathematician") (**1950**). *Elementary Proof of a Minimax Theorem due to von Neumann*. in


 [Harold W. Kuhn](Mathematician#HWKuhn "Mathematician") and [Albert W. Tucker](Mathematician#AWTucker "Mathematician") (eds) (**1950**). *[Contributions to the Theory of Games I](http://books.google.com/books?id=TpbbVU4tA58C&printsec=frontcover&dq=isbn:9780691079349&hl=de&ei=r2i1TabJL8_usgaW-rj7Cw&sa=X&oi=book_result&ct=result&resnum=1&ved=0CCoQ6AEwAA#v=onepage&q&f=false)*. [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)
* [Émile Borel](Mathematician#Borel "Mathematician"), [Maurice R. Fréchet](Mathematician#MRFrechet "Mathematician"), [John von Neumann](John_von_Neumann "John von Neumann") (**1953**). *Discussion of the Early History of the Theory of Games, with Special Reference to the Minimax Theorem*. [Econometrica](https://en.wikipedia.org/wiki/Econometrica), Vol. 21
* [Leonard J. Savage](Mathematician#LJSavage "Mathematician") (**1953**). *The Theory of Play and Integral Equations with Skew Symmetric Kernels*. [Econometrica](https://en.wikipedia.org/wiki/Econometrica), Vol. 21, pp. 101-115, English translation of [Émile Borel](Mathematician#Borel "Mathematician") (**1921**). *[La théorie du jeu et les équations intégrales à noyau symétrique](Minimax#Borel "Minimax")*.
* [David Blackwell](Mathematician#DHBlackwell "Mathematician") (**1956**). *[An analog of the minimax theorem for vector payoffs](http://projecteuclid.org/euclid.pjm/1103044235)*. [Pacific Journal of Mathematics](https://en.wikipedia.org/wiki/Pacific_Journal_of_Mathematics), Vol. 6, No, 1
* [Maurice Sion](Mathematician#MSion "Mathematician") (**1958**). *[On general minimax theorems](https://projecteuclid.org/euclid.pjm/1103040253)*. [Pacific Journal of Mathematics](https://en.wikipedia.org/wiki/Pacific_Journal_of_Mathematics), Vol. 8, No. 1 <a id="cite-note-7" href="#cite-ref-7">[7]</a>


### 1960 ...


* [James R. Slagle](James_R._Slagle "James R. Slagle") (**1963**). *Game Trees, M & N Minimaxing, and the M & N alpha-beta procedure.* Artificial Intelligence Group Report 3, UCRL-4671, University of California
* [Donald Michie](Donald_Michie "Donald Michie") (**1966**). *Game Playing and Game Learning Automata.* Advances in Programming and Non-Numerical Computation, [Leslie Fox](https://en.wikipedia.org/wiki/Leslie_Fox) (ed.), pp. 183-200. Oxford, Pergamon. » Includes Appendix: *Rules of SOMAC* by [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), introduces [Expectiminimax tree](https://en.wikipedia.org/wiki/Expectiminimax_tree) <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [Philip Bursky](Philip_Bursky "Philip Bursky") (**1968**). *[Experiments With a Multipurpose, Theorem-Proving Heuristic Program](http://portal.acm.org/citation.cfm?id=321444)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 15, No. 1
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [John K. Dixon](John_K._Dixon "John K. Dixon") (**1969**). *Experiments With Some Programs That Search Game Trees*. [Journal of the ACM](ACM#Journal "ACM"), Vol 16, No. 2, [pdf](http://wiki.cs.pdx.edu/wurzburg2009/nfp/abmin.pdf)


### 1970 ...


* [James R. Slagle](James_R._Slagle "James R. Slagle"), [John K. Dixon](John_K._Dixon "John K. Dixon") (**1970**). *[Experiments with the M & N Tree-Searching Program](http://portal.acm.org/citation.cfm?id=362052.362054)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 13, No. 3
* [Thiruvenkatachari Parthasarathy](Mathematician#TParthasarathy "Mathematician") (**1970**). *[On Games Over the Unit Square](https://epubs.siam.org/doi/abs/10.1137/0119047?journalCode=smjmap)*. [SIAM Journal on Applied Mathematics](https://en.wikipedia.org/wiki/SIAM_Journal_on_Applied_Mathematics), Vol. 19, No. 2 <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [Minimax](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p004.htm#index54) in [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*.


### 1980 ...


* [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams") (**1982**). *Error Analysis of the Minimax Principle*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [Chun-Hung Tzeng](Chun-Hung_Tzeng "Chun-Hung Tzeng"), [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom") (**1983**). *[A Theory of Game Trees](https://www.aaai.org/Library/AAAI/1983/aaai83-080.php)*. [AAAI-83](Conferences#AAAI-83 "Conferences")
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom"), [Chun-Hung Tzeng](Chun-Hung_Tzeng "Chun-Hung Tzeng") (**1986**). *Experiments on Alternatives to Minimax*. [International Journal of Parallel Programming, Vol. 15](https://dblp.uni-trier.de/db/journals/ijpp/ijpp15.html#NauPT86), No. 2
* [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom"), [Chun-Hung Tzeng](Chun-Hung_Tzeng "Chun-Hung Tzeng") (**1986, 2013**). *An Evaluation of Two Alternatives to Minimax*. Machine Intelligence and Pattern Recognition, Vol. 4, [arXiv:1304.3445](https://arxiv.org/abs/1304.3445)
* [Ronald L. Rivest](Ronald_L._Rivest "Ronald L. Rivest") (**1987**). *Game Tree Searching by Min/Max Approximation*. Artificial Intelligence Vol. 34, 1, [pdf 1995](http://people.csail.mit.edu/rivest/Rivest-GameTreeSearchingByMinMaxApproximation.pdf)


### 1990 ...


* [Liwu Li](Liwu_Li "Liwu Li"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1990**). *On Minimax Game Tree Search Pathology and Node-value Dependence*. TR90-24, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR90-24.pdf)
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich") (**1993**). *[A Bibliography on Minimax Trees](http://portal.acm.org/citation.cfm?id=165007)*. [ACM SIGACT News](ACM#SIG "ACM"), Vol. 24, No. 4
* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Evolving Neural Networks to focus Minimax Search](http://nn.cs.utexas.edu/?moriarty:aaai94)*. [AAAI-94](Conferences#AAAI-94 "Conferences") » [Othello](Othello "Othello")
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich"), [Marc Gengler](index.php?title=Marc_Gengler&action=edit&redlink=1 "Marc Gengler (page does not exist)") (**1995**). *[A Survey on Minimax Trees and Associated Algorithms](http://link.springer.com/chapter/10.1007/978-1-4613-3557-3_2)*. *[Minimax and Its Applications](http://link.springer.com/book/10.1007/978-1-4613-3557-3)*. [Kluwer Academic Publishers](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Richard Korf](Richard_Korf "Richard Korf"), [Max Chickering](Max_Chickering "Max Chickering") (**1996**). *[Best-first minimax search](https://www.microsoft.com/en-us/research/publication/best-first-minimax-search/)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 84, Nos 1-2 » [Best-First](Best-First "Best-First")
* [Yoav Freund](Yoav_Freund "Yoav Freund"), [Robert Schapire](Robert_Schapire "Robert Schapire") (**1996**). *Game Theory, On-line Prediction and Boosting*. [COLT 1996](http://dblp.uni-trier.de/db/conf/colt/colt1996.html#FreundS96), [pdf](http://www.cs.princeton.edu/~schapire/papers/FreundSc96b.pdf)
* [Don Beal](Don_Beal "Don Beal") (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis


### 2000 ...


* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich"), [Marc Gengler](index.php?title=Marc_Gengler&action=edit&redlink=1 "Marc Gengler (page does not exist)") (**2001**). *[Minimax Game Tree Searching](http://link.springer.com/referenceworkentry/10.1007%2F0-306-48332-7_280)*. [Encyclopedia of Optimization](http://link.springer.com/book/10.1007/0-306-48332-7), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Tinne Hoff Kjeldsen](http://milne.ruc.dk/~thk/) (**2001**). *John von Neumann’s Conception of the Minimax Theorem: A Journey Through Different Mathematical Contexts*. [Archive for History of Exact Sciences](https://en.wikipedia.org/wiki/Archive_for_History_of_Exact_Sciences), Vol. 56, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Thomas Hauk](index.php?title=Thomas_Hauk&action=edit&redlink=1 "Thomas Hauk (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *[Rediscovering \*-Minimax Search](http://link.springer.com/chapter/10.1007/11674399_3)*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://skatgame.net/mburo/ps/STAR-A.pdf)
* [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2005**). *Why Minimax Works: An Alternative Explanation*. [IJCAI 2005](Conferences#IJCAI2005 "Conferences"), [pdf](https://www.ijcai.org/Proceedings/05/Papers/1223.pdf) » [Search Pathology](Search_Pathology "Search Pathology")
* [Mitja Luštrek](Mitja_Lu%C5%A1trek "Mitja Luštrek"), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *Is Real-Valued Minimax Pathological*? [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 170, [pdf](https://dis.ijs.si/MitjaL/documents/Is_Real-Valued_Minimax_Pathological-AIJ-06.pdf)
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich"), [Marc Gengler](index.php?title=Marc_Gengler&action=edit&redlink=1 "Marc Gengler (page does not exist)") (**2009**). *[Minimax Game Tree Searching](http://link.springer.com/referenceworkentry/10.1007%2F978-0-387-74759-0_370)*. [Encyclopedia of Optimization](http://link.springer.com/book/10.1007/978-0-387-74759-0), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


### 2010 ...


* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2014**). *[Interest Search - Another way to do Minimax](http://www.aifactory.co.uk/newsletter/2014_01_interest_minimax.htm)*. [AI Factory](AI_Factory "AI Factory"), Summer 2014
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Anton Scheucher](index.php?title=Anton_Scheucher&action=edit&redlink=1 "Anton Scheucher (page does not exist)") (**2017**). *[Product Propagation: A Back-up Rule Better than Minimaxing?](https://ieeexplore.ieee.org/document/7358032)* [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 9, No. 2, [pdf](File:KaindlProductPropagation.pdf "File:KaindlProductPropagation.pdf")


### 2020 ...


* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2020**). *Minimax Strikes Back*. [arXiv:2012.10700](https://arxiv.org/abs/2012.10700) » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")


## Forum Posts


* [beyond minimax](http://www.talkchess.com/forum/viewtopic.php?t=13433) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 27, 2007
* [The evaluation value and value returned by minimax search](http://www.talkchess.com/forum/viewtopic.php?t=42806) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), March 09, 2012 » [Evaluation](Evaluation "Evaluation")
* [Why minimax is fundamentally flawed](http://www.talkchess.com/forum/viewtopic.php?t=54295) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 09, 2014 » [KRK](KRK "KRK")


## External Links


* [Min-Max Search](http://web.archive.org/web/20070820195815/www.seanet.com/%7Ebrucemo/topics/minmax.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
* [Minimax from Wikipedia](https://en.wikipedia.org/wiki/Minimax)
* [Minimax theorem from Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)
* [Parthasarathy's theorem from Wikipedia](https://en.wikipedia.org/wiki/Parthasarathy%27s_theorem)
* [Sion's minimax theorem from Wikipedia](https://en.wikipedia.org/wiki/Sion%27s_minimax_theorem)
* [Minimax estimator from Wikipedia](https://en.wikipedia.org/wiki/Minimax_estimator)
* [Expectiminimax tree from Wikipedia](https://en.wikipedia.org/wiki/Expectiminimax_tree)
* [Maxima and minima from Wikipedia](https://en.wikipedia.org/wiki/Maxima_and_minima)
* [Analog voltage maximizer and minimizer circuits](http://www.freepatentsonline.com/5414310.html) from [FreePatentsOnline](http://www.freepatentsonline.com/)
* [Kraftwerk](Category:Kraftwerk "Category:Kraftwerk") - Pocket Calculator, [Minimum-Maximum](https://en.wikipedia.org/wiki/Minimum-Maximum), [Moscow](https://en.wikipedia.org/wiki/Moscow), [Luzhniki](https://en.wikipedia.org/wiki/Luzhniki_Olympic_Complex), June 03, 2004 and [Tokyo](https://en.wikipedia.org/wiki/Tokyo), [Shibuya Station](https://en.wikipedia.org/wiki/Shibuya_Station), March 04, 2004, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Little Machine Constructed by Minimax Dadamax in Person from Wikipedia](https://en.wikipedia.org/wiki/Little_Machine_Constructed_by_Minimax_Dadamax_in_Person)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1983**). *Computerschaak, Schaakwereld en Kunstmatige Intelligentie*. Ph.D. thesis, [Delft University of Technology](Delft_University_of_Technology "Delft University of Technology"). Academic Service, The Hague. ISBN 90 62 33 093 2 (Dutch)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [John von Neumann](John_von_Neumann "John von Neumann") (**1928**). *[Zur Theorie der Gesellschaftsspiele](http://gdz.sub.uni-goettingen.de/dms/load/img/?IDDOC=29357)*. Berlin
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Don Beal](Don_Beal "Don Beal") (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, ISBN 90-62-16-6348, pp. 2, refers [Philip Morrison](Mathematician#PhilipMorrison "Mathematician") and Emily Morrison (**1961**). *Charles Babbage and his Calculating Engines*. Dover Publ. New York
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Norbert Wiener](Norbert_Wiener "Norbert Wiener") (**1948**). *[Cybernetics or Control and Communication in the Animal and the Machine](http://www.amazon.com/gp/reader/026273009X/ref=sib_dp_pt#reader-link)* - MIT Press, Cambridge, MA.
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**2005**). *Die Entwicklung der Spielprogrammierung: Von John von Neumann bis zu den hochparallelen Schachmaschinen*. [slides as pdf](http://www.informatik.hu-berlin.de/studium/ringvorlesung/ss05/slides/05-06-02.pdf), Themen der Informatik im historischen Kontext Ringvorlesung an der [HU Berlin](https://en.wikipedia.org/wiki/Humboldt_University_of_Berlin), 02.06.2005 (English paper, German title)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Sion's minimax theorem from Wikipedia](https://en.wikipedia.org/wiki/Sion%27s_minimax_theorem)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> see [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Parthasarathy's theorem from Wikipedia](https://en.wikipedia.org/wiki/Parthasarathy%27s_theorem)

**[Up one level](Search "Search")**







 
