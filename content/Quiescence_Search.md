---
title: Quiescence Search
---
**[Home](Home "Home") \* [Search](Search "Search") \* Quiescence**



 [](http://www.yogachicago.com/jan06/art.shtml) [Karen Schuman](index.php?title=Category:Karen_Schuman&action=edit&redlink=1 "Category:Karen Schuman (page does not exist)") - Quiescence [[1]](#cite_note-1) 
Most chess programs, at the end of the main search perform a more limited **quiescence** search, containing fewer moves. The purpose of this search is to only [evaluate](Evaluation "Evaluation") "quiet" [positions](Chess_Position "Chess Position"), or positions where there are no winning [tactical moves](Tactical_Moves "Tactical Moves") to be made. This search is needed to avoid the [horizon effect](Horizon_Effect "Horizon Effect"). Simply stopping your search when you reach the desired [depth](Depth "Depth") and then evaluate, is very dangerous. Consider the situation where the last move you consider is QxP. If you stop there and evaluate, you might think that you have won a pawn. But what if you were to search one move deeper and find that the next move is PxQ? You didn't win a pawn, you actually lost a queen. Hence the need to make sure that you are evaluating only quiescent (quiet) positions. 



### Contents


* [1 Limiting Quiescence](#Limiting_Quiescence)
* [2 Standing Pat](#Standing_Pat)
* [3 Checks](#Checks)
* [4 Pseudo Code](#Pseudo_Code)
* [5 See also](#See_also)
* [6 Publications](#Publications)
	+ [6.1 1975](#1975)
	+ [6.2 1980 ...](#1980_...)
	+ [6.3 1990 ...](#1990_...)
	+ [6.4 2000 ...](#2000_...)
* [7 Forum Posts](#Forum_Posts)
	+ [7.1 1994 ...](#1994_...)
	+ [7.2 2000 ...](#2000_..._2)
	+ [7.3 2005 ...](#2005_...)
	+ [7.4 2010 ...](#2010_...)
	+ [7.5 2015 ...](#2015_...)
	+ [7.6 2020 ...](#2020_...)
* [8 External Links](#External_Links)
* [9 References](#References)






Despite the fact that quiescence searches are typically very short, about 50%-90% nodes are spent there, so it is worthwhile to apply some [pruning](Pruning "Pruning") there. Apart from not trying moves with the [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") < 0, [delta pruning](Delta_Pruning "Delta Pruning") can be used for that purpose.




## Standing Pat


In order to allow the quiescence search to stabilize, we need to be able to stop searching without necessarily searching all available [captures](Captures "Captures"). In addition, we need a score to return in case there are no captures available to be played. This is done by a using the [static evaluation](Evaluation "Evaluation") as a "stand-pat" score (the term is taken from the game of poker, where it denotes playing one's hand without drawing more cards). At the beginning of quiescence, the position's evaluation is used to establish a [lower bound](Lower_Bound "Lower Bound") on the score. This is theoretically sound because we can usually assume that there is at least one move that can either match or beat the lower bound. This is based on the [Null Move Observation](Null_Move_Observation "Null Move Observation") - it assumes that we are not in [Zugzwang](Zugzwang "Zugzwang"). If the lower bound from the stand pat score is already greater than or equal to beta, we can return the stand pat score ([fail-soft](Fail-Soft "Fail-Soft")) or [beta](Beta "Beta") ([fail-hard](Fail-Hard "Fail-Hard")) as a [lower bound](Lower_Bound "Lower Bound"). Otherwise, the search continues, keeping the evaluated "stand-pat" score as an [lower bound](Lower_Bound "Lower Bound") if it exceeds [alpha](Alpha "Alpha"), to see if any [tactical moves](Tactical_Moves "Tactical Moves") can increase [alpha](Alpha "Alpha").




## Checks


Some programs search treat [checks](Check "Check") and check evasions specially in quiescence. The idea behind this is that if the side to move is in check, the position is not quiet, and there is a threat that needs to be resolved. In this case, all evasions to the check are searched. Stand pat is not allowed if we are in check, for two reasons. First, because we are not sure that there is a move that can match alpha--in many positions a check can mean a serious threat that cannot be resolved. Second, because we are searching every move in the position, rather than only [captures](Captures "Captures"). 
Standing pat assumes that even if we finish searching all moves, and none of them increase alpha, one of the non-tactical moves can most likely raise alpha. This is not valid if we search every move. The other case of treating checks specially is the checking moves themselves. Some programs, after searching all the captures in a position without finding a move to raise alpha, will generate non-capture moves that give check. This has to be limited somehow, however, because in most given positions there will be very many long and pointless checking sequences that do not amount to anything. Most programs achieve this limit by delta pruning checks, as well as limiting the generation of checks to the first X plies of quiescence.



## Pseudo Code



```C++

int Quiesce( int alpha, int beta ) {
    int stand_pat = Evaluate();
    if( stand_pat >= beta )
        return beta;
    if( alpha < stand_pat )
        alpha = stand_pat;

    until( every_capture_has_been_examined )  {
        MakeCapture();
        score = -Quiesce( -beta, -alpha );
        TakeBackMove();

        if( score >= beta )
            return beta;
        if( score > alpha )
           alpha = score;
    }
    return alpha;
}

```

## See also


* [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
* [CPW-Engine\_quiescence](CPW-Engine_quiescence "CPW-Engine quiescence")
* [Crossovers](Horizon_Effect#Crossovers "Horizon Effect")
* [Delta Pruning](Delta_Pruning "Delta Pruning")
* [Generalized Quiescence Search](Null_Move_Pruning#NMQS "Null Move Pruning") by [Don Beal](Don_Beal "Don Beal")
* [Horizon Effect](Horizon_Effect "Horizon Effect")
* [Horizon Node](Horizon_Node "Horizon Node")
* [MVV-LVA](MVV-LVA "MVV-LVA")
* [Quiescent Node](Quiescent_Node "Quiescent Node")
* [Search Explosion](Search_Explosion "Search Explosion")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Swap-off algorithm - SOMA](SOMA#Swapoff "SOMA")
* [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")
* [Tactical Quiescence Search](Excalibur_Mirage#TacticalQuiescence "Excalibur Mirage") in [Excalibur Mirage](Excalibur_Mirage "Excalibur Mirage")
* [Vice Video on Quiescence](Vice#Quiescence "Vice")
* [Zzzzzz' Quiescence Search](Zzzzzz#Quiescence "Zzzzzz")


## Publications


### 1975


* [Larry Harris](Larry_Harris "Larry Harris") (**1975**) *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [IJCAI](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/index.html) 1975 Tbilisi, Georgia: 334-339. reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1980 ...


* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *Dynamic Control of the Quiescence Search in Computer Chess*. Cybernetics and Systems Research (ed. R. Trappl), pp. 973-977. North-Holland, Amsterdam.
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *Quiescence Search in Computer Chess.* SIGART Newsletter, 80, pp. 124-131. Reprinted (1983) in Computer-Game-Playing: Theory and Practice, pp. 39-52. Ellis Horwood Ltd., Chichester.
* [Don Beal](Don_Beal "Don Beal") (**1984**). *Mating Sequences in the Quiescence Search*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
* [Prakash Bettadapur](Prakash_Bettadapur "Prakash Bettadapur") (**1986**). *Experiments in Chess Capture Search*, M.Sc. Thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta").
* [Prakash Bettadapur](Prakash_Bettadapur "Prakash Bettadapur") (**1986**). *Influence of Ordering on Capture Search*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Prakash Bettadapur](Prakash_Bettadapur "Prakash Bettadapur"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1988**). *Accuracy and Savings in Depth-Limited Capture Search*. In [International Journal of Man-Machine Studies, 29](http://www.informatik.uni-trier.de/%7Eley/db/journals/ijmms/ijmms29.html#BettadapurM88) (5) pp. 497-502
* [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), a revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702, edited version in (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, IKAT, ISBN 90-62-16-6348. Chapter 10, pp. 101-116 » [Null Move](Null_Move "Null Move")
* [Günther Schrüfer](G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1989**). *A Strategic Quiescence Search*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal") » [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")


### 1990 ...


* [Don Beal](Don_Beal "Don Beal") (**1990**). *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702
* [Sören Walter Perrey](index.php?title=S%C3%B6ren_Walter_Perrey&action=edit&redlink=1 "Sören Walter Perrey (page does not exist)") (**1991**). *Mathematische Methoden der Künstlichen Intelligenz: Zur Quiescence-Suche in Spielbäumen*. Diplom thesis, Sonderforschungsbereich 343, [E91-006](http://www.mathematik.uni-bielefeld.de/sfb343/preprints/index91.html), [University of Bielefeld](https://en.wikipedia.org/wiki/Bielefeld_University) (German) [[2]](#cite_note-2)
* [Michael Gherrity](Michael_Gherrity "Michael Gherrity"), [Paul Kube](Mathematician#PKube "Mathematician") (**1993**). *Quiescent Search is Beneficial.* Technical Report CS93-289, [University of California, San Diego](http://de.wikipedia.org/wiki/University_of_California,_San_Diego)
* [Don Beal](Don_Beal "Don Beal") (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, IKAT, ISBN 90-62-16-6348


### 2000 ...


* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2000**). *SUPER-SOMA - Solving Tactical Exchanges in Shogi without Tree Searching*. [Lecture Notes In Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 2063, [CG 2000](CG_2000 "CG 2000"), [Word preprint](http://www.aifactory.co.uk/downloads/SUPER-SOMA.doc) [[3]](#cite_note-3)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Looking for Alternatives to Quiescence Search](http://www.aifactory.co.uk/newsletter/2006_03_quiescence_alts.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2006
* [Don Beal](Don_Beal "Don Beal") (**2006**). *Review of a nullmove-quiescence search mechanism from 1986*. [File:Alg1986review.txt](File:Alg1986review.txt "File:Alg1986review.txt") (Draft) [[4]](#cite_note-4)
* [Maarten Schadd](index.php?title=Maarten_Schadd&action=edit&redlink=1 "Maarten Schadd (page does not exist)"), [Mark Winands](Mark_Winands "Mark Winands") (**2009**). *Quiescence Search for Stratego*. In BNAIC 2009, [pdf](http://www.personeel.unimaas.nl/Maarten-Schadd/Papers/2009StrategoBNAIC1.pdf)


## Forum Posts


### 1994 ...


* [Efficient quiescence](http://groups.google.com/group/rec.games.chess/browse_frm/thread/ee86982df38f003c) by [Hans Bogaards](index.php?title=Hans_Bogaards&action=edit&redlink=1 "Hans Bogaards (page does not exist)"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), January 19, 1994
* [Computer Chess: swap down evaluators vs capture search](http://groups.google.com/group/rec.games.chess/browse_frm/thread/dd1c55ecc9f48717) by [Jon Dart](Jon_Dart "Jon Dart"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 24, 1994 » [Swap-off algorithm - SOMA](SOMA#Swapoff "SOMA")


 [Re: Computer Chess: swap down evaluators vs capture search](http://groups.google.com/group/rec.games.chess/msg/527be476c5dd22d1) by [Deniz Yuret](Deniz_Yuret "Deniz Yuret"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 26, 1994
* [quiescence search problems](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a027ac0e2fb5892e) by [Matt Craighead](Matt_Craighead "Matt Craighead"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 01, 1995


 [Re: Quiescence search problems](https://groups.google.com/group/rec.games.chess.computer/msg/fedfcfaf26d04dfa) by [David Blackman](David_Blackman "David Blackman"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 3, 1995 » [Integrated Bounds and Values](Integrated_Bounds_and_Values "Integrated Bounds and Values")
* [quiescent vs non-quiescent node counting](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/926eaf0869b6f176) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 01, 1996
* [Deep Quiesence Searching](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/6fb02db95638ade1) by Steve Dicks, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 22, 1997
* [quiescence search](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ca0300b50438a388) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1997 » [Check](Check "Check"), [Crafty](Crafty "Crafty")
* [Limiting the QSearch](https://www.stmintz.com/ccc/index.php?id=13485) by John Scalo, [CCC](CCC "CCC"), December, 30, 1997
* [Quiescence vs swapoff](https://www.stmintz.com/ccc/index.php?id=17016) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), April 15, 1998
* [SEE for forward pruning in Q. Search](https://www.stmintz.com/ccc/index.php?id=63511) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 04, 1999 » [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [SEE for forward pruning in the Q. search - I'm confused!](https://www.stmintz.com/ccc/index.php?id=64357) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 11, 1999


### 2000 ...


* [What is the q-search?](https://www.stmintz.com/ccc/index.php?id=86662) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 07, 2000
* [Qsearch problems...(about sorting and SEE)](https://www.stmintz.com/ccc/index.php?id=141230) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 26, 2000 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


**2001**



* [Bonus points for side to move in qsearch?](https://www.stmintz.com/ccc/index.php?id=148445) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), January 06, 2001 » [Tempo](Tempo "Tempo")
* [About limiting Qsearch, again...](https://www.stmintz.com/ccc/index.php?id=204243) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 29, 2001
* [About qsearch...](https://www.stmintz.com/ccc/index.php?id=203771) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 27, 2001
* [Qsearch survey](https://www.stmintz.com/ccc/index.php?id=204492) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 30, 2001


**2002**



* [Checks in the Qsearch](https://www.stmintz.com/ccc/index.php?id=237893) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), June 28, 2002 » [Check](Check "Check")
* [A question about quiescence search](https://www.stmintz.com/ccc/index.php?id=260485) by Nagendra Singh Tomar, [CCC](CCC "CCC"), October 19, 2002
* [Quiescence Explosion](https://www.stmintz.com/ccc/index.php?id=267486) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), November 26, 2002
* [Quiescent Explosion](https://www.stmintz.com/ccc/index.php?id=303257) by macaroni, [CCC](CCC "CCC"), June 26, 2003
* [Regarding Qsearch with Fractional ply extensions](https://www.stmintz.com/ccc/index.php?id=310897) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), August 11, 2003 » [Depth - Fractional Plies](Depth#FractionalPlies "Depth")
* [real job of the qSearch? find quiet vs stop horizon effect](https://www.stmintz.com/ccc/index.php?id=313206) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), August 28, 2003
* [quiescence](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d451877add19a50e) by Noah Roberts, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2003


**2004**



* [QSearch() as PVS() ?](https://www.stmintz.com/ccc/index.php?id=342287) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 14, 2004
* [Rebel's long checks concept in QS](https://www.stmintz.com/ccc/index.php?id=344282) by [milix](Anastasios_Milikas "Anastasios Milikas"), [CCC](CCC "CCC"), January 23, 2004 » [Rebel](Rebel "Rebel"), [Check](Check "Check")
* [quiesce node explosion](https://www.stmintz.com/ccc/index.php?id=344566) by Mike Siler, [CCC](CCC "CCC"), January 24, 2004
* [Qsearch Checks](https://www.stmintz.com/ccc/index.php?id=385027) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 29, 2004 » [Check](Check "Check")
* [Checks in QSearch](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=702&p=2642) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), November 23, 2004


### 2005 ...


* [quiescence search / horizon question](https://www.stmintz.com/ccc/index.php?id=445400) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), August 26, 2005
* [How to Best Limit Checks in the Quiescence ?](http://www.talkchess.com/forum/viewtopic.php?p=139285) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 20, 2007 » [Check](Check "Check"), [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
* [Quiescence Search Explosions](http://www.talkchess.com/forum/viewtopic.php?t=20727) by [Mike Leany](Mike_Leany "Mike Leany"), [CCC](CCC "CCC"), April 18, 2008
* [checks in q-search](http://www.talkchess.com/forum/viewtopic.php?t=23447) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 02, 2008
* [Limiting Quiescent Search Depth](http://www.talkchess.com/forum/viewtopic.php?t=28023) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), May 20, 2009
* [Null move in quiescence search idea from Don Beal, 1986](http://www.talkchess.com/forum/viewtopic.php?t=29439) by [Eelco de Groot](index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), [CCC](CCC "CCC"), Aug 17, 2009 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [Don Beal](Don_Beal "Don Beal")
* [Threat information from evaluation to inform q-search](http://www.talkchess.com/forum/viewtopic.php?p=291259) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), September 15, 2009
* [Only recaptures in qsearch?](http://www.talkchess.com/forum/viewtopic.php?t=30738) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), November 21, 2009


### 2010 ...


* [Avoiding qsearch explosion](http://www.talkchess.com/forum/viewtopic.php?t=32148) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), January 29, 2010
* [Problems when implementing checks in qsearch](http://talkchess.com/forum/viewtopic.php?t=32345) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), February 03, 2010
* [Standpat and check](http://www.talkchess.com/forum/viewtopic.php?t=32424) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), February 06, 2010 » [Standing Pat](Quiescence_Search#StandPat "Quiescence Search"), [Check](Check "Check")
* [This is totally weird ... Don't understand at all](http://www.talkchess.com/forum/viewtopic.php?t=36692) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), November 13, 2010


**2012**



* [checks in quies](http://www.talkchess.com/forum/viewtopic.php?t=42971) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 22, 2012
* [stand pat or side to move bonus](http://www.talkchess.com/forum/viewtopic.php?t=42982) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 22, 2012
* [TT question?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=43769) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), May 19, 2012 » [Transposition Table](Transposition_Table "Transposition Table")
* [Some thoughts on QS](http://www.talkchess.com/forum/viewtopic.php?t=44507) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 19, 2012
* [QSearch, checks and the lack of progress...](http://www.talkchess.com/forum/viewtopic.php?t=44599) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), July 27, 2012
* [Quiescence - Check Evaluation and Depth Control](http://www.talkchess.com/forum/viewtopic.php?t=45942) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), November 10, 2012


**2013**



* [Quiescence Search and Checkmates](http://www.open-chess.org/viewtopic.php?f=5&t=2212) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2013 » [Checkmate](Checkmate "Checkmate")
* [Quiescent search, and side to move is in check](http://www.talkchess.com/forum/viewtopic.php?t=47162) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 08, 2013
* [Transposition table usage in quiescent search?](http://www.talkchess.com/forum/viewtopic.php?t=47373) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), March 01, 2013 » [Transposition Table](Transposition_Table "Transposition Table")
* [Pruning in QS](http://www.talkchess.com/forum/viewtopic.php?t=47423) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 06, 2013 » [Pruning](Pruning "Pruning")
* [QS investigation](http://www.talkchess.com/forum/viewtopic.php?t=47436) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 07, 2013
* [qsearch question](http://www.open-chess.org/viewtopic.php?f=5&t=2402) by nak3c, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 19, 2013
* [about qs](http://www.talkchess.com/forum/viewtopic.php?t=49311) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), September 11, 2013


**2014**



* [Positional quiesence](http://www.talkchess.com/forum/viewtopic.php?t=51967) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 12, 2014
* [Transposition table in Q-search](http://www.talkchess.com/forum/viewtopic.php?t=54755) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), December 26, 2014 » [Transposition Table](Transposition_Table "Transposition Table")


### 2015 ...


* [Detail evaluation within quiescence search](http://www.talkchess.com/forum/viewtopic.php?t=55424) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), February 22, 2015
* [hanging piece at starting quiescence search - how to handle?](http://www.talkchess.com/forum/viewtopic.php?t=55427) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), February 22, 2015 » [Hanging Piece](Hanging_Piece "Hanging Piece")
* [Search algorithm in it's simplest forum](http://www.talkchess.com/forum/viewtopic.php?t=55474) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 25, 2015 » [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Check-extension in QS](http://www.talkchess.com/forum/viewtopic.php?t=55874) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 03, 2015 » [Check](Check "Check")
* [quiescence search (best practices)](http://www.open-chess.org/viewtopic.php?f=5&t=2852) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 02, 2015
* [Null Move in Quiescent search](http://www.talkchess.com/forum/viewtopic.php?t=58527) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 09, 2015 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [Search Pathology](Search_Pathology "Search Pathology")


**2016**



* [Checks in qsearch - must-have or optional?](http://www.talkchess.com/forum/viewtopic.php?t=59529) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 15, 2016 » [Check](Check "Check"), [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
* [Hashing in Qsearch?](http://talkchess.com/forum/viewtopic.php?t=59740) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 03, 2016 » [Transposition Table](Transposition_Table "Transposition Table")
* [Quiescence node explosion](http://www.open-chess.org/viewtopic.php?f=5&t=2984) by [sandermvdb](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2016 » [Search Explosion](Search_Explosion "Search Explosion")
* [Starting with quiescence search](http://www.talkchess.com/forum/viewtopic.php?t=60962) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), July 28, 2016
* [Quiescence Search Performance](http://www.talkchess.com/forum/viewtopic.php?t=60964) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), July 28, 2016
* [Removing Q-search](http://www.talkchess.com/forum/viewtopic.php?t=61307) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 02, 2016
* [Searching using slow eval with tactical verification](http://www.talkchess.com/forum/viewtopic.php?t=61348) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 06, 2016
* [Collecting PVs of Qsearch ?](http://www.talkchess.com/forum/viewtopic.php?t=61796) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 22, 2016 » [Principal Variation](Principal_Variation "Principal Variation"), [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")


**2017**



* [capturing PV in QSearch](http://www.open-chess.org/viewtopic.php?f=5&t=3072) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2017 » [Principal Variation](Principal_Variation "Principal Variation"), [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")
* [Ridiculous QSearch Depth](http://www.talkchess.com/forum/viewtopic.php?t=63326) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), March 03, 2017 » [Depth](Depth "Depth")
* [Q search explosion](http://www.talkchess.com/forum/viewtopic.php?t=63590) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), March 30, 2017 » [Search Explosion](Search_Explosion "Search Explosion")
* [Probe EGT in quiescence?](http://www.talkchess.com/forum/viewtopic.php?t=64030) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), May 20, 2017 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"), [Xiangqi](Chinese_Chess "Chinese Chess")
* [Is expensive eval required for QS?](http://www.talkchess.com/forum/viewtopic.php?t=64674) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2017 » [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Cutoffs in Quiescence Search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64940) by jfern2011, [CCC](CCC "CCC"), August 20, 2017 » [Beta-Cutoff](Beta-Cutoff "Beta-Cutoff")
* [TT in Qsearch](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65903) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 05, 2017 » [Transposition Table](Transposition_Table "Transposition Table")


**2019**



* [Playing transposition table moves in the Quiescence search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69629) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 17, 2019 » [Transposition Table](Transposition_Table "Transposition Table")


### 2020 ...


* [Tactical search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74170) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), June 13, 2020 » [Tactics](Tactics "Tactics")
* [Qsearch() variant](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75059) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 09, 2020
* [Quiescence Search doesn't improve strength](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76706) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), February 25, 2021
* [For or against the transposition table probe in quiet search?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77286) by [Eugene Kotlov](index.php?title=Eugene_Kotlov&action=edit&redlink=1 "Eugene Kotlov (page does not exist)"), [CCC](CCC "CCC"), May 11, 2021 » [Transposition Table](Transposition_Table "Transposition Table")
* [Qsearch dynamic order besides MVV/LVA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77380) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), May 25, 2021 » [Move Ordering](Move_Ordering "Move Ordering")
* [Futility Pruning and its Relation to Quiescence Search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77451) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), June 06, 2021 » [Futility Pruning](Futility_Pruning "Futility Pruning")


## External Links


* [Quiescence search from Wikipedia](https://en.wikipedia.org/wiki/Quiescence_search)
* [Quiescence from Wikipedia](https://en.wikipedia.org/wiki/Quiescence)
* [Quiescence Search](http://web.archive.org/web/20070813042640/www.seanet.com/~brucemo/topics/quiescent.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Quiescent Search in REBEL](https://web.archive.org/web/20120331060714/http://www.top-5000.nl/authors/rebel/chess840.htm#QS)  from [Ed Schröder's](Ed_Schroder "Ed Schroder") [Programmer Stuff](http://www.top-5000.nl/authors/rebel/chess840.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Pim Jacobs](https://en.wikipedia.org/wiki/Pim_Jacobs), [Ruud Jacobs](Category:Ruud_Jacobs "Category:Ruud Jacobs"), [Ruud Brink](http://nl.wikipedia.org/wiki/Ruud_Brink), [Wim Overgaauw](https://en.wikipedia.org/wiki/Wim_Overgaauw), [Dom Um Romão](Category:Dom_Um_Rom%C3%A3o "Category:Dom Um Romão"), [Astrud Gilberto](Category:Astrud_Gilberto "Category:Astrud Gilberto") - [Meditation](https://en.wikipedia.org/wiki/Meditation_%28song%29), [It Might as Well Be Spring](https://en.wikipedia.org/wiki/It_Might_as_Well_Be_Spring), Telephone Song, [Only Trust Your Heart](https://en.wikipedia.org/wiki/Only_Trust_Your_Heart), [Corcovado (Quiet Nights of Quiet Stars)](https://en.wikipedia.org/wiki/Corcovado_%28song%29), [The Girl From Ipanema](https://en.wikipedia.org/wiki/The_Girl_from_Ipanema); from [Dzjes Zien à la Bossa Nova](http://www.cultura.nl/genres/kunst/2014/brazili-.html), [NCRV](https://en.wikipedia.org/wiki/Nederlandse_Christelijke_Radio_Vereniging) 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) Quiescence by [Karen Schuman](index.php?title=Category:Karen_Schuman&action=edit&redlink=1 "Category:Karen Schuman (page does not exist)") from [Artist Karen Schuman’s Personal Mythology](http://www.yogachicago.com/jan06/art.shtml) Reviewed by [Anna Poplawska](http://www.chicagoartcriticsassociation.org/B/poplawska.html)
2. [↑](#cite_ref-2) [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1991**). *Mathematische Methoden der Künstlichen Intelligenz: Zur Quiescence-Suche in Spielbäumen*. Review, [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
3. [↑](#cite_ref-3) [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Looking for Alternatives to Quiescence Search](http://www.aifactory.co.uk/newsletter/2006_03_quiescence_alts.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2006
4. [↑](#cite_ref-4) courtesy of [Don Beal](Don_Beal "Don Beal") and [Carey Bloodworth](Carey_Bloodworth "Carey Bloodworth"), [Re: Antique chess programs](http://www.talkchess.com/forum/viewtopic.php?t=58603&start=13) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), December 16, 2015

**[Up one level](Search "Search")**







 
