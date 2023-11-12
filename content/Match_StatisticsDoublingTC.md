---
title: Match StatisticsDoublingTC
---
**[Home](Home "Home") \* [Engine Testing](Engine_Testing "Engine Testing") \* Match Statistics**



 [](https://commons.wikimedia.org/wiki/File:Standard_deviation_diagram.svg) Match Statistics [[1]](#cite_note-1) 
**Match Statistics**,  

the [statistics](https://en.wikipedia.org/wiki/Statistics) of chess [tournaments and matches](Tournaments_and_Matches "Tournaments and Matches"), that is a collection of [chess games](Chess_Game "Chess Game") and the presentation, [analysis](https://en.wikipedia.org/wiki/Analysis), and interpretation of game related data, most common game results to determine the relative [playing strength](Playing_Strength "Playing Strength") of chess playing entities, here with focus on [chess engines](Engines "Engines"). To apply match statistics, beside considering [statistical population](https://en.wikipedia.org/wiki/Statistical_population), it is conventional to hypothesize a [statistical model](https://en.wikipedia.org/wiki/Statistical_model) describing a set of [probability distributions](https://en.wikipedia.org/wiki/Probability_distribution). 



### Number of games


The total number of games played by an engine in a tournament.




```C++
N = wins + draws + losses

```

### Score


The score is a representation of the tournament-outcome from the viewpoint of a certain engine.




```C++
score\_difference = wins - losses

```


```C++
score = wins + draws/2

```





### Win & Draw Ratio



```C++
win\_ratio = score/N

```


```C++
draw\_ratio = draws/N

```

These two ratios depend on the [strength](Playing_Strength "Playing Strength") difference between the competitors, the average strength level, the color and the drawishness of the [opening book-line](Opening_Book "Opening Book"). Due to the second reason given, these ratios are very much influenced by the [timecontrol](Time_Management#Time_Controls "Time Management"), what is also confirmed by the published statistics of the testing orgnisations [CCRL](CCRL "CCRL") and [CEGT](CEGT "CEGT"), showing an increase of the [draw](Draw "Draw") rate at longer time controls. This correlation was also shown by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), who was analyzing statistics of his test-games [[2]](#cite_note-2) . The program playing white seems to be more supported by the additional level of strength. So, although one would expect with increasing draw rates the win ratio to approach 50%, in fact it is remaining about equal.





|  Timecontrol
 |  Draw Ratio
 |  Win Ratio (white)
 |  Source
 |
| --- | --- | --- | --- |
|  40/4
 |  30.9%
 |  55.0%
 |  CEGT
 |
|  40/20
 |  35.6%
 |  54.6%
 |  CEGT
 |
|  40/120
 |  41.3%
 |  55.4%
 |  CEGT
 |
|  40/120 (4cpu)
 |  45.2%
 |  55.9%
 |  CEGT
 |




|  Timecontrol
 |  Draw Ratio
 |  Win Ratio (white)
 |  Source
 |
| --- | --- | --- | --- |
|  40/4
 |  31.0%
 |  54.1%
 |  CCRL
 |
|  40/40
 |  37.2%
 |  54.6%
 |  CCRL
 |



**Doubling Time Control**
As posted in October 2016 [[3]](#cite_note-3) , [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller") conducted an experiment with [Komodo 9.3](Komodo "Komodo"), [time control](Time_Management "Time Management") doubling matches under [Cutechess-cli](Cutechess-cli "Cutechess-cli"), playing 3000 games with 1500 [opening](Opening "Opening") positions each, without [pondering](Pondering "Pondering"), [learning](Learning "Learning"), and [tablebases](Endgame_Tablebases "Endgame Tablebases"), [Intel i5-750](https://en.wikipedia.org/wiki/List_of_Intel_Core_i5_microprocessors#Desktop_processors) @ 3.5 GHz, 1 Core, 128 MB Hash [[4]](#cite_note-4) , see also [Kai Laskos'](Kai_Laskos "Kai Laskos") 2013 results with [Houdini 3](Houdini "Houdini") [[5]](#cite_note-5) and [Diminishing Returns](Depth#DiminishingReturns "Depth"):





|  Time Control
 |  2vs 1
 |  20+0.210+0.1
 |  40+0.420+0.2
 |  80+0.840+0.4
 |  160+1.680+0.8
 |  320+3.2160+1.6
 |  640+6.4320+3.2
 |  1280+12.8640+6.4
 |  2560+25.61280+12.8
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Elo
 |  144
 |  133
 |  112
 |  101
 |  93
 |  73
 |  59
 |  51
 |
|  Win
 |  44.97%
 |  41.27%
 |  36.67%
 |  32.67%
 |  30.47%
 |  25.17%
 |  21.77%
 |  18.97%
 |
|  Draw
 |  49.20%
 |  54.00%
 |  57.93%
 |  63.03%
 |  65.33%
 |  70.47%
 |  73.17%
 |  76.63%
 |
|  Loss
 |  5.83%
 |  4.73%
 |  5.40%
 |  4.30%
 |  4.20%
 |  4.37%
 |  5.07%
 |  4.40%
 |


### Elo-Rating & Win-Probability


*see [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")*




```C++
Expected win\_ratio, win\_probability (E)

```


```C++
Elo Rating Difference (Δ) = Elo\_Player1 - Elo\_Player2

```


```C++
E = 1 / ( 1 + 10-Δ/400)

```


```C++
Δ = 400 log10(E / (1 - E))

```

Generalization of the Elo-Formula:
*win\_probability of player i in a tournament with n players*




```C++
Ei = 10Eloi / (10Elo1 + 10Elo2 + ... + 10Elon-1 + 10Elon)

```

### Likelihood of Superiority


*See [LOS Table](LOS_Table "LOS Table")*


The likelihood of superiority (LOS) denotes how likely it would be for two players of the same [strength](Playing_Strength "Playing Strength") to reach a certain result - in other fields called a [p-value](https://en.wikipedia.org/wiki/P-value), a measure of [statistical significance](https://en.wikipedia.org/wiki/Statistical_significance) of a departure from the [null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) [[6]](#cite_note-6). Doing this analysis after the tournament one has to differentiate between the case where one knows that a certain engine is either stronger or equally strong (directional or one-tailed test) or the case where one has no information of whether the other engine is stronger or weaker (non-directional or [two-tailed test](https://en.wikipedia.org/wiki/Two-tailed_test)). The latter due to the reduced information results in larger [confidence intervals](https://en.wikipedia.org/wiki/Confidence_interval).


**Two-tailed Test**  

[Null](https://en.wikipedia.org/wiki/Null_hypothesis)- and [alternative hypothesis](https://en.wikipedia.org/wiki/Alternative_hypothesis):




```C++
H0 : Elo\_Player1 = Elo\_Player2 

H1 : Elo\_Player1 ≠ Elo\_Player2 

```


```C++
LOS = P(Score > score of 2 programs with equal strength)

```

The probability of the [null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) being true can be calculated given the tournament outcome. In other words, how likely would it be for two players of the same strength to reach a certain result. The LOS would then be the inverse, 1 - the resulting probability.


For this type of analysis the [trinomial distribution](https://en.wikipedia.org/wiki/Multinomial_distribution), a generalization of the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution), is needed. Whilest the binomial distribution can only calculate the probability to reach a certain outcome with two possible events, the trinominal distribution can account for all three possible events (win, draw, loss).


The following functions gives the probability of a certain game outcome assuming both players were of equal strength:




```C++
win\_probability = (1 - draw\_ratio) / 2

```


```C++
P(wins,draws,losses) = N!/(wins! draws! losses!) win\_probabilitywins draw\_ratiodrwas win\_probabilitylosses

```

This calculation becomes very inefficient for larger number of games. In this case the [standard normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Standard_normal_distribution) can give a good approximation:




```C++
***N***(N/2, N(1-draw\_ratio))

```

where N(1 - draw\_ratio) is the sum of wins and losses:




```C++
***N***(N/2, wins + losses)

```

To calculate the LOS one needs the [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) of the given normal distribution. However, as pointed out by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), calculation can be done cleverly, and the normal approximation is not really required [[7]](#cite_note-7) . As further emphasized by [Kai Laskos](Kai_Laskos "Kai Laskos") [[8]](#cite_note-8) and Rémi Coulom [[9]](#cite_note-9) [[10]](#cite_note-10) , draws do not count in LOS calculation and don't make a difference whether the game results were obtained when playing Black or White. It is a good approximation when the two players played the same number of games with each color:




```C++
LOS = ϕ((wins - losses)/√(wins + losses))

LOS = ½[1 + erf((wins - losses)/√(2wins + 2losses))]

```

[[11]](#cite_note-11) [[12]](#cite_note-12) [[13]](#cite_note-13)


**One-tailed Test**  

[Null](https://en.wikipedia.org/wiki/Null_hypothesis)- and [alternative hypothesis](https://en.wikipedia.org/wiki/Alternative_hypothesis):




```C++
H0 : Elo\_Player1 ≤ Elo\_Player2 

H1 : Elo\_Player1 > Elo\_Player2 

```


**Sample Program**  

A tiny [C++11](Cpp "Cpp") program to compute Elo difference and LOS from W/L/D counts was given by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") [[14]](#cite_note-14) :




```C++

##include <cstdio>
##include <cstdlib>
##include <cmath>

int main(int argc, char **argv) {
  if (argc != 4) {
    std::printf("Wrong number of arguments.\n\nUsage:%s <wins> <losses> <draws>\n", argv[0]);
    return 1;
  }
  int wins = std::atoi(argv[1]);
  int losses = std::atoi(argv[2]);
  int draws = std::atoi(argv[3]);

  double games = wins + losses + draws;
  std::printf("Number of games: %g\n", games);
  double winning_fraction = (wins + 0.5*draws) / games;
  std::printf("Winning fraction: %g\n", winning_fraction);
  double elo_difference = -std::log(1.0/winning_fraction-1.0)*400.0/std::log(10.0);
  std::printf("Elo difference: %+g\n", elo_difference);
  double los = .5 + .5 * std::erf((wins-losses)/std::sqrt(2.0*(wins+losses)));
  std::printf("LOS: %g\n", los);
}

```

### Statistical Analysis


**The trinomial versus the 5-nomial model**


As indicated above a match between two engines is usually modeled as a sequence of independent trials taken from a trinomial distribution with probabilities (win\_ratio,draw\_ratio,loss\_ratio). This model is appropriate for a match with randomly selected opening positions and randomly assigned colors (to maintain fairness). However one may show that under reasonable elo models the trinomial model is not correct in case games are played in pairs with reversed colors (as is commonly the case) and unbalanced opening positions are used.


This was also empirically observed by [Kai Laskos](Kai_Laskos "Kai Laskos") [[15]](#cite_note-15) . He noted that the statistical predictions of the trinomial model do not match reality very well in the case of paired games. In particular he observed that for some data sets the variance of the match score as predicted by the trinomial model greatly exceeds the variance as calculated by the [jackknife](https://en.wikipedia.org/wiki/Jackknife_resampling) estimator. The jackknife estimator is a non-parametric estimator, so it does not depend on any particular statistical model. It appears the mismatch may even occur for balanced opening positions, an effect which can only be explained by the existence of correlations between paired games - something not considered by any elo model.


Over estimating the variance of the match score implies that derived quantities such as the number of games required to establish the superiority of one engine over another with a given level of significance are also over estimated. To obtain agreement between statistical predictions and actual measurements one may adopt the more general 5-nomial model. In the 5-nomial model the outcome of paired games is assumed to follow a 5-nomial distribution with probabilities




```C++
(p0, p1/2, p1, p3/2, p2)

```

These unknown probabilities may be estimated from the outcome frequencies of the paired games and then subsequently be used to compute an estimate for the variance of the match score. Summarizing: in the case of paired games the 5-nomial model handles the following effects correctly which the trinomial model does not:



* Unbalanced openings
* Correlations between paired games


For further discussion on the potential use of unbalanced opening positions in engine testing see the posting by [Kai Laskos](Kai_Laskos "Kai Laskos") [[16]](#cite_note-16) .



### SPRT


The [sequential probability ratio test](https://en.wikipedia.org/wiki/Sequential_probability_ratio_test) (SPRT) is a specific [sequential hypothesis test](https://en.wikipedia.org/wiki/Sequential_analysis) - a statistical analysis where the [sample size](https://en.wikipedia.org/wiki/Sample_size_determination) is not fixed in advance - developed by [Abraham Wald](Mathematician#AWald "Mathematician") [[17]](#cite_note-17) . While originally developed for use in quality control studies in the realm of manufacturing, SPRT has been formulated for use in the computerized testing of human examinees as a termination criterion [[18]](#cite_note-18). As mentioned by [Arthur Guez](Arthur_Guez "Arthur Guez") in this 2015 Ph.D. thesis *Sample-based Search Methods for Bayes-Adaptive Planning* [[19]](#cite_note-19), [Alan Turing](Alan_Turing "Alan Turing") assisted by [Jack Good](Jack_Good "Jack Good") used a similar sequential testing technique to help decipher [enigma codes](https://en.wikipedia.org/wiki/Enigma_machine) at [Bletchley Park](https://en.wikipedia.org/wiki/Bletchley_Park) [[20]](#cite_note-20). SPRT is applied in [Stockfish](Stockfish "Stockfish") testing to terminate self-testing series early if the result is likely outside a given elo-window [[21]](#cite_note-21) . In August 2016, [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh") posted following [Python](Python "Python") code in [CCC](CCC "CCC") to implement the SPRT a la [Cutechess-cli](Cutechess-cli "Cutechess-cli") or [Fishtest](Stockfish#TestingFramework "Stockfish"): [[22]](#cite_note-22) [[23]](#cite_note-23)




```C++

from __future__ import division

import math

def LL(x):
    return 1/(1+10**(-x/400))

def LLR(W,D,L,elo0,elo1):
    """
This function computes the log likelihood ratio of H0:elo_diff=elo0 versus
H1:elo_diff=elo1 under the logistic elo model

expected_score=1/(1+10**(-elo_diff/400)).

W/D/L are respectively the Win/Draw/Loss count. It is assumed that the outcomes of
the games follow a trinomial distribution with probabilities (w,d,l). Technically
this is not quite an SPRT but a so-called GSPRT as the full set of parameters (w,d,l)
cannot be derived from elo_diff, only w+(1/2)d. For a description and properties of
the GSPRT (which are very similar to those of the SPRT) see

http://stat.columbia.edu/~jcliu/paper/GSPRT_SQA3.pdf

This function uses the convenient approximation for log likelihood
ratios derived here:

http://hardy.uhasselt.be/Toga/GSPRT_approximation.pdf

The previous link also discusses how to adapt the code to the 5-nomial model
discussed above.
"""
## avoid division by zero
    if W==0 or D==0 or  L==0:
        return 0.0
    N=W+D+L
    w,d,l=W/N,D/N,L/N
    s=w+d/2
    m2=w+d/4
    var=m2-s**2
    var_s=var/N
    s0=LL(elo0)
    s1=LL(elo1)
    return (s1-s0)*(2*s-s0-s1)/var_s/2.0

def SPRT(W,D,L,elo0,elo1,alpha,beta):
    """
This function sequentially tests the hypothesis H0:elo_diff=elo0 versus
the hypothesis H1:elo_diff=elo1 for elo0<elo1. It should be called after
each game until it returns either 'H0' or 'H1' in which case the test stops
and the returned hypothesis is accepted.

alpha is the probability that H1 is accepted while H0 is true
(a false positive) and beta is the probability that H0 is accepted
while H1 is true (a false negative). W/D/L are the current win/draw/loss
counts, as before.
"""
    LLR_=LLR(W,D,L,elo0,elo1)
    LA=math.log(beta/(1-alpha))
    LB=math.log((1-beta)/alpha)
    if LLR_>LB:
        return 'H1'
    elif LLR_<LA:
        return 'H0'
    else:
        return ''

```

Beside the above SPRT implementation using pentanomial frequencies and a simulation tool in [Python](Python "Python") [[24]](#cite_note-24) [[25]](#cite_note-25), [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh") wrote a much faster multi-threaded [C](C "C") version [[26]](#cite_note-26) [[27]](#cite_note-27).






## Tournaments


* [Chess Server](Chess_Server "Chess Server")
* [Engine Rating Lists](Engine_Rating_Lists "Engine Rating Lists")
* [Tournament Manager](Tournament_Manager "Tournament Manager")
* [Tournaments and Matches](Tournaments_and_Matches "Tournaments and Matches")


## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Bishop versus Knight - Winning Percentages](Bishop_versus_Knight#WinningPercantages "Bishop versus Knight")
* [Depth | Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Draw](Draw "Draw")
* [Engine Similarity](Engine_Similarity "Engine Similarity")
* [LOS Table](LOS_Table "LOS Table")
* [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Playing Strength](Playing_Strength "Playing Strength")
* [Search Statistics](Search_Statistics "Search Statistics")
* [The Technology Curve](Alexander_Szabo#TechnologyCurve "Alexander Szabo")
* [Time Controls](Time_Management#Time_Controls "Time Management")
* [Who is the Master?](Jean-Marc_Alliot#WhoistheMaster "Jean-Marc Alliot")


## Publications


### 1920 ...


* [L. L. Thurstone](Mathematician#LLThurstone "Mathematician") (**1927**). *[A law of comparative judgement](https://psycnet.apa.org/record/1928-00527-001)*. [Psychological Review](https://en.wikipedia.org/wiki/Psychological_Review), Vol. 34, No. 4 [[28]](#cite_note-28)
* [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") (**1929**). *Die Berechnung der Turnier-Ergebnisse als ein Maximumproblem der Wahrscheinlichkeitsrechnung*. [pdf](http://gdz.sub.uni-goettingen.de/dms/load/img/?IDDOC=82727) (German)


### 1930 ...


* [Alexander Aitken](Mathematician#ACAitken "Mathematician") (**1935**). *[On Least Squares and Linear Combinations of Observations](https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh/article/ivon-least-squares-and-linear-combination-of-observations/7106C26F19F2EBF75BCEE7FA285780B9)*. Proceedings of the [Royal Society of Edinburgh](https://en.wikipedia.org/wiki/Royal_Society_of_Edinburgh)


### 1940 ...


* [Abraham Wald](Mathematician#AWald "Mathematician") (**1945**). *Sequential Tests of Statistical Hypotheses*. [Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 16, No. 2, [doi](https://en.wikipedia.org/wiki/Digital_object_identifier): [10.1214/aoms/1177731118](http://projecteuclid.org/euclid.aoms/1177731118)
* [Abraham Wald](Mathematician#AWald "Mathematician") (**1947**). *Sequential Analysis*. [John Wiley and Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons), [AbeBooks](http://www.abebooks.com/book-search/title/sequential-analysis/author/abraham-wald/)


### 1950 ...


* [Frederick Mosteller](Mathematician#Mosteller "Mathematician") (**1951**). *[Remarks on the method of paired comparisons: I. The least squares solution assuming equal standard deviations and equal correlations](https://psycnet.apa.org/record/1951-07176-001)*. [Psychometrika](https://en.wikipedia.org/wiki/Psychometrika), Vol. 16, No. 1
* [Ralph A. Bradley](Mathematician#RABradley "Mathematician"), [Milton E. Terry](Mathematician#METerry "Mathematician") (**1952**). *[Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons](http://biomet.oxfordjournals.org/content/39/3-4/324.citation)*. [Biometrika](https://en.wikipedia.org/wiki/Biometrika), Vol. 39, Nos. 3/4


### 1960 ...


* [William A. Glenn](Mathematician#WAGlenn "Mathematician"), [Herbert A. David](Mathematician#HADavid "Mathematician") (**1960**). *[Ties in Paired-Comparison Experiments Using a Modified Thurstone-Mosteller Model](https://www.jstor.org/stable/2527957?seq=1#page_scan_tab_contents)*. [Biometrics](https://en.wikipedia.org/wiki/Biometrics_(journal)), Vol. 16, No. 1
* [Florence Nightingale David](Mathematician#FNDavid "Mathematician") (**1962**). *[Games, Gods & Gambling: A History of Probability and Statistical Ideas](http://books.google.com/books/about/Games_Gods_and_Gambling.html?id=8ddP8zNx9nQC&redir_esc=y)*. [Dover Publications](https://en.wikipedia.org/wiki/Dover_Publications)
* [P. V. Rao](Mathematician#PVRao "Mathematician"), [L. L. Kupper](Mathematician#LLKupper "Mathematician") (**1967**). *[Ties in Paired-Comparison Experiments: A Generalization of the Bradley-Terry Model](https://www.tandfonline.com/doi/abs/10.1080/01621459.1967.10482901)*. [Journal of the American Statistical Association](https://en.wikipedia.org/wiki/Journal_of_the_American_Statistical_Association), Vol. 62, No. 317


### 1970 ...


* [Roger R. Davidson](https://www.semanticscholar.org/author/Roger-R.-Davidson/32819150) (**1970**). *[On Extending the Bradley-Terry Model to Accommodate Ties in Paired Comparison Experiments](https://www.jstor.org/stable/2283595)*. [Journal of the American Statistical Association](https://en.wikipedia.org/wiki/Journal_of_the_American_Statistical_Association), Vol. 64, No. 329
* [F. Donald Bloss](http://what-when-how.com/earth-scientists/bloss-f-donald-earth-scientist/) (**1973**). *[Rate your own Chess](https://www.amazon.de/Rate-Your-Chess-F-Donald-Bloss/dp/0442008295)*. Van Nostrand Reinhold Inc.
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Paul Rushton](Paul_Rushton "Paul Rushton") (**1973**). *[Mechanisms for Comparing Chess Programs](http://dl.acm.org/citation.cfm?id=805703).* [ACM Annual Conference](ACM_1973 "ACM 1973"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Marsland-Rushton-ACM73)
* [James Gillogly](James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [CMU-CS-77 pdf](http://reports-archive.adm.cs.cmu.edu/anon/anon/usr/ftp/scan/CMU-CS-77-gillogly.pdf) » [Tech](Tech "Tech")
* [Arpad Elo](https://en.wikipedia.org/wiki/Arpad_Elo) (**1978**). *The Rating of Chessplayers, Past and Present*. Arco Publications [[29]](#cite_note-29)
* [David Cahlander](David_Cahlander "David Cahlander") (**1979**). *Strength of a Chess Playing Computer*. [ICCA Newsletter, Vol. 2, No. 1](ICGA_Journal#2_1 "ICGA Journal")
* [Jack Good](Jack_Good "Jack Good") (**1979**). *On the Grading of Chess Players*. [Personal Computing, Vol. 3, No. 3](Personal_Computing#3_3 "Personal Computing"), pp. 47
* [Gary L. Ratliff](index.php?title=Gary_L._Ratliff&action=edit&redlink=1 "Gary L. Ratliff (page does not exist)") (**1979**). *Practical Rating Program*. [Personal Computing, Vol. 3, No. 9](Personal_Computing#3_9 "Personal Computing"), pp. 62  » [Bloss](#Bloss)
* [Frieder Schwenkel](Frieder_Schwenkel "Frieder Schwenkel") (**1979**). *Berating the ratings system*. [Personal Computing, Vol. 3, No. 11](Personal_Computing#3_11 "Personal Computing"), pp. 77 » [Ratliff](#Ratliff), [Bloss](#Bloss)
* [John Shaposka](index.php?title=John_Shaposka&action=edit&redlink=1 "John Shaposka (page does not exist)") (**1979**). *"JS" Takes the Bloss Test*. [Personal Computing, Vol. 3, No. 12](Personal_Computing#3_12 "Personal Computing"), pp. 75 » [Ratliff](#Ratliff), [Bloss](#Bloss)


### 1980 ...


* Floyd R. Kirk (**1980**). *Bloss Flunks Test*. [Personal Computing, Vol. 4, No. 8](Personal_Computing#4_8 "Personal Computing"), pp. 72  » [Ratliff](#Ratliff), [Bloss](#Bloss)
* [John F. White](John_F._White "John F. White") (**1981**). *[Survey-Chess Games](http://yourcomputeronline.wordpress.com/2010/12/10/survey-chess-games/)*. [Your Computer](Your_Computer "Your Computer"), [August/September 1981](http://yourcomputeronline.wordpress.com/2010/10/31/augustseptember-1981-contents-and-editorial/) [[30]](#cite_note-30)
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Computer Chess Strength*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [David Siegmund](Mathematician#DavidSiegmund "Mathematician") (**1985**). *Sequential Analysis. Tests and confidence intervals*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1989**). *Measuring the Performance Potential of Chess Programs*, [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
* [Eric Hallsworth](Eric_Hallsworth "Eric Hallsworth") (**1989**). *Playing Levels*. [Computer Chess News Sheet](Selective_Search "Selective Search") 23, pp 2, [pdf](http://www.chesscomputeruk.com/SS_23.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")


### 1990 ...


* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Carl Ebeling](Carl_Ebeling "Carl Ebeling") (**1990**). *Measuring the Performance Potential of Chess Programs.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
* [Hal Stern](Mathematician#HSStern "Mathematician") (**1990**). *Are all Linear Paired Comparison Models Equivalent*. [pdf](http://www.dtic.mil/dtic/tr/fulltext/u2/a236856.pdf)
* [Eric Hallsworth](Eric_Hallsworth "Eric Hallsworth") (**1990**). *Speed, Processors and Ratings*. [Computer Chess News Sheet](Selective_Search "Selective Search") 25, pp 6, [pdf](http://www.chesscomputeruk.com/SS_25.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Danny Kopec](Danny_Kopec "Danny Kopec"), [Ed Northam](Ed_Northam "Ed Northam") (**1991**). *A taxonomy of concepts for evaluating chess strength: examples from two difficult categories*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_20_C.pdf)
* [Steve Maughan](Steve_Maughan "Steve Maughan") (**1992**). *Are You Sure It's Better?* [Selective Search](Selective_Search "Selective Search") 40, pp. 21, [pdf](http://www.chesscomputeruk.com/SS_40.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
* [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1993**). *Rating Systems for Gameplayers, and Learning*. [ps](http://scorevoting.net/WarrenSmithPages/homepage/ratingspap.ps)
* [Mark E. Glickman](index.php?title=Mark_E._Glickman&action=edit&redlink=1 "Mark E. Glickman (page does not exist)") (**1993**). *Paired Comparison Models with Time Varying Parameters*. Ph.D. thesis, [Harvard University](Harvard_University "Harvard University"), advisor [Hal Stern](Mathematician#HSStern "Mathematician"), [pdf](http://www.glicko.net/research/thesis.pdf)
* [Mark E. Glickman](index.php?title=Mark_E._Glickman&action=edit&redlink=1 "Mark E. Glickman (page does not exist)") (**1995**). *A Comprehensive Guide To Chess Ratings*. [pdf](http://www.glicko.net/research/acjpaper.pdf)
* [Mark E. Glickman](index.php?title=Mark_E._Glickman&action=edit&redlink=1 "Mark E. Glickman (page does not exist)"), [Christopher Chabris](Christopher_Chabris "Christopher Chabris") (**1996**). *Using Chess Ratings as Data in Psychological Research*. [pdf](https://pdfs.semanticscholar.org/1ffd/3432f56476f0047426b37f7f433f5a6575b0.pdf)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *CRAFTY Goes Deep*. [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal") » [Crafty](Crafty "Crafty")
* [Mark E. Glickman](index.php?title=Mark_E._Glickman&action=edit&redlink=1 "Mark E. Glickman (page does not exist)"), [Albyn C. Jones](Mathematician#ACJones "Mathematician") (**1999**). *Rating the Chess Rating System*. [pdf](http://www.glicko.net/research/chance.pdf)


### 2000 ...


* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *[New Self-Play Results in Computer Chess](http://link.springer.com/chapter/10.1007/3-540-45579-5_18)*. [CG 2000](CG_2000 "CG 2000")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-play Experiments in Computer Chess Revisited.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Modeling the “Go Deep” Behaviour of CRAFTY and DARK THOUGHT.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") » [Crafty](Crafty "Crafty"), [Dark Thought](index.php?title=Dark_Thought&action=edit&redlink=1 "Dark Thought (page does not exist)")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-Play, Deep Search and Diminishing Returns.* [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2002**). *[Self-play: Statistical Significance](http://centaur.reading.ac.uk/5952/)*. [7th Computer Olympiad Workshop](7th_Computer_Olympiad#Workshop "7th Computer Olympiad")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2003**). *[Self-Play: Statistical Significance](http://centaur.reading.ac.uk/4549/)*. [ICGA Journal, Vol. 26, No. 2](ICGA_Journal#26_2 "ICGA Journal")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2003**). *Follow-Up on Self-Play, Deep Search, and Diminishing Returns.* [ICGA Journal, Vol. 26, No. 2](ICGA_Journal#26_2 "ICGA Journal")
* [David R. Hunter](Mathematician#DHunter "Mathematician") (**2004**). *MM Algorithms for Generalized Bradley-Terry Models*. [The Annals of Statistics](https://en.wikipedia.org/wiki/Annals_of_Statistics), Vol. 32, No. 1, 384–406, [pdf](http://sites.stat.psu.edu/~dhunter/papers/bt.pdf) [[31]](#cite_note-31) [[32]](#cite_note-32) [[33]](#cite_note-33) [[34]](#cite_note-34)


### 2005 ...


* [Jan Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen") (**2005**). *New Results in Deep-Search Behaviour*. [ICGA Journal, Vol. 28, No. 4](ICGA_Journal#28_4 "ICGA Journal"), [pdf](http://www.st.ewi.tudelft.nl/%7Erenze/doc/ICGA_2005_4_DeepSearch.pdf)
* [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2005**). *[Comparing Move Choices of Chess Search Engines](https://www.researchgate.net/publication/220174440_Comparing_Move_Choices_of_Chess_Search_Engines)*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal"), [pdf](http://www.dcs.bbk.ac.uk/~mark/download/fritz_junior_icga.pdf) » [Fritz](Fritz "Fritz"), [Junior](Junior "Junior")
* [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2006**). *Comparing Typical Opening Move Choices Made by Humans and Chess Engines*. [arXiv:cs/0610060](https://arxiv.org/abs/cs/0610060)
* [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2007**). *Comparing Typical Opening Move Choices Made by Humans and Chess Engines*. [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal), Vol. 50, No. 5
* [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [CGW 2007](CGW_2007 "CGW 2007") » [Crafty](Crafty "Crafty"), [Rybka](Rybka "Rybka"), [Shredder](Shredder "Shredder"), [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2007**). *[Statistical Minefields with Version Testing](http://www.aifactory.co.uk/newsletter/2007_04_stat_minefields.htm)*. [AI Factory](AI_Factory "AI Factory"), Winter 2007 » [Engine Testing](Engine_Testing "Engine Testing")
* [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kazunori Yamaguchi](Kazunori_Yamaguchi "Kazunori Yamaguchi"), [Satoru Kawai](Satoru_Kawai "Satoru Kawai") (**2007**). *Visualization and Adjustment of Evaluation Functions Based on Evaluation Values and Win Probability*. [AAAI 2007](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2007.html), [pdf](https://www.aaai.org/Papers/AAAI/2007/AAAI07-136.pdf)
* [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2008**). *[Whole-History Rating: A Bayesian Rating System for Players of Time-Varying Strength](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_11)*. [CG 2008](CG_2008 "CG 2008"), [draft as pdf](http://remi.coulom.free.fr/WHR/WHR.pdf)
* [Giuseppe Di Fatta](index.php?title=Giuseppe_Di_Fatta&action=edit&redlink=1 "Giuseppe Di Fatta (page does not exist)"), [Guy McCrossan Haworth](Guy_Haworth "Guy Haworth"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2009**). *Skill Rating by Bayesian Inference*. [CIDM 2009](http://www.informatik.uni-trier.de/~ley/db/conf/cidm/cidm2009.html), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/DFHR09.pdf) [[35]](#cite_note-35)
* [Guy McCrossan Haworth](Guy_Haworth "Guy Haworth"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Giuseppe Di Fatta](index.php?title=Giuseppe_Di_Fatta&action=edit&redlink=1 "Giuseppe Di Fatta (page does not exist)") (**2009**). *Performance and Prediction: Bayesian Modelling of Fallible Choice in Chess*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://www.cse.buffalo.edu/faculty/regan/papers/pdf/HRdF10.pdf)


### 2010 ...


* [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2010**). *[Predicting the Outcome of Chess Games based on Historical Data](http://web.ist.utl.pt/diogo.ferreira/chess/)*. [IST](https://en.wikipedia.org/wiki/Instituto_Superior_T%C3%A9cnico) - [Technical University of Lisbon](https://en.wikipedia.org/wiki/Technical_University_of_Lisbon) [[36]](#cite_note-36)
* [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2011**). *[Intrinsic Chess Ratings](http://www.aaai.org/ocs/index.php/AAAI/AAAI11/paper/view/3779)*. [AAAI 2011](http://www.informatik.uni-trier.de/%7Eley/db/conf/aaai/aaai2011.html#ReganH11), [pdf](http://www.aaai.org/ocs/index.php/AAAI/AAAI11/paper/view/3779/3962), [slides as pdf](http://www.cse.buffalo.edu/%7Eregan/Talks/IntrinsicRatings.pdf) [[37]](#cite_note-37)
* [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Bartłomiej Macieja](index.php?title=Bart%C5%82omiej_Macieja&action=edit&redlink=1 "Bartłomiej Macieja (page does not exist)"), [Guy McCrossan Haworth](Guy_Haworth "Guy Haworth") (**2011**). *[Understanding Distributions of Chess Performances](http://centaur.reading.ac.uk/23800/)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/RMH11.pdf)
* [Trevor Fenner](Trevor_Fenner "Trevor Fenner"), [Mark Levene](Mark_Levene "Mark Levene"), [George Loizou](Mathematician#GLoizou "Mathematician") (**2011**). *A Discrete Evolutionary Model for Chess Players' Ratings*. [arXiv:1103.1530](https://arxiv.org/abs/1103.1530)
* [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2012**). *Determining the Strength of Chess Players based on actual Play*. [ICGA Journal, Vol. 35, No. 1](ICGA_Journal#35_1 "ICGA Journal")
* [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2013**). *Paired Comparisons with Ties: Modeling Game Outcomes in Chess*. [[38]](#cite_note-38) [[39]](#cite_note-39)
* [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2013**). *The Impact of the Search Depth on Chess Playing Strength*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal") » [Depth](Depth "Depth"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Houdini](Houdini "Houdini") [[40]](#cite_note-40)
* [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") (**2014**). *ORDO v0.9.6 Ratings for chess and other games*. September 2014, [pdf](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxnYXZpb3RhY2hlc3NlbmdpbmV8Z3g6NmQ0NmNhNGM4YjA3YTc5ZQ) » [Ordo](index.php?title=Ordo&action=edit&redlink=1 "Ordo (page does not exist)") [[41]](#cite_note-41)
* [Don Dailey](Don_Dailey "Don Dailey"), [Adam Hair](Adam_Hair "Adam Hair"), [Mark Watkins](Mark_Watkins "Mark Watkins") (**2014**). *[Move Similarity Analysis in Chess Programs](http://www.sciencedirect.com/science/article/pii/S1875952113000177)*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 5, No. 3, [preprint as pdf](http://magma.maths.usyd.edu.au/~watkins/papers/DHW.pdf) [[42]](#cite_note-42)
* [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Jason Zhou](index.php?title=Jason_Zhou&action=edit&redlink=1 "Jason Zhou (page does not exist)") (**2014**). *Human and Computer Preferences at Chess*. [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/RBZ14aaai.pdf)
* [Erik Varend](index.php?title=Erik_Varend&action=edit&redlink=1 "Erik Varend (page does not exist)") (**2014**). *Quality of play in chess and methods for measuring*. [pdf](http://www.chessanalysis.ee/Quality%20of%20play%20in%20chess%20and%20methods%20for%20measuring.pdf) [[43]](#cite_note-43) [[44]](#cite_note-44)
* [Xiaoou Li](Mathematician#XiaoouLi "Mathematician"), [Jingchen Liu](Mathematician#JingchenLiu "Mathematician"), [Zhiliang Ying](Mathematician#ZhiliangYing "Mathematician") (**2014**). *[Generalized Sequential Probability Ratio Test for Separate Families of Hypotheses](https://www.tandfonline.com/doi/abs/10.1080/07474946.2014.961861)*. [Sequential Analysis](https://www.tandfonline.com/loi/lsqa20?open=36&year=2017&repitition=0), Vol. 33, No. 4, [pdf](http://stat.columbia.edu/~jcliu/paper/GSPRT_SQA3.pdf)


### 2015 ...


* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Quantifying Depth and Complexity of Thinking and Knowledge*. [ICAART 2015](http://www.icaart.org/EuropeanProjectSpace.aspx?y=2015), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/BiReICAART15CR.pdf)
* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Measuring Level-K Reasoning, Satisficing, and Human Error in Game-Play Data*. [IEEE](IEEE "IEEE") [ICMLA 2015](http://www.icmla-conference.org/icmla15/), [pdf preprint](http://www.cse.buffalo.edu/~regan/papers/pdf/BiRe15_ICMLA2015.pdf)
* [Guy Haworth](Guy_Haworth "Guy Haworth"), [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *[A Comparative Review of Skill Assessment: Performance, Prediction and Profiling](http://centaur.reading.ac.uk/39431/)*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2015**). *[Estimating Ratings of Computer Players by the Evaluation Scores and Principal Variations in Shogi](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7336038)*. [ACIT-CSI](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7335993)
* [Jean-Marc Alliot](Jean-Marc_Alliot "Jean-Marc Alliot") (**2017**). *Who is the Master*? [ICGA Journal, Vol. 39, No. 1](ICGA_Journal#39_1 "ICGA Journal"), [draft as pdf](http://www.alliot.fr/CHESS/draft-icga-39-1.pdf) » [Stockfish](Stockfish "Stockfish"), [Who is the Master?](Jean-Marc_Alliot#WhoistheMaster "Jean-Marc Alliot")
* [Ilan Adler](Mathematician#IAdler "Mathematician"), [Yang Cao](Mathematician#YangCao "Mathematician"), [Richard Karp](Richard_Karp "Richard Karp"), [Erol A. Peköz](Mathematician#EAPekoz "Mathematician"), [Sheldon M. Ross](Mathematician#SMRoss "Mathematician") (**2017**). *[Random Knockout Tournaments](https://pubsonline.informs.org/doi/10.1287/opre.2017.1657)*. [Operations Research](https://en.wikipedia.org/wiki/Operations_Research_(journal)), Vol. 65, No. 6, [arXiv:1612.04448](https://arxiv.org/abs/1612.04448)
* [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh") (**2017**). *A Practical Introduction to the GSPRT*. [pdf](http://hardy.uhasselt.be/Toga/GSPRT_approximation.pdf)
* [Leszek Szczecinski](index.php?title=Leszek_Szczecinski&action=edit&redlink=1 "Leszek Szczecinski (page does not exist)"), [Aymen Djebbi](index.php?title=Aymen_Djebbi&action=edit&redlink=1 "Aymen Djebbi (page does not exist)") (**2019**). *Understanding and Pushing the Limits of the Elo Rating Algorithm*. [arXiv:1910.06081](https://arxiv.org/abs/1910.06081) [[45]](#cite_note-45)
* [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh") (**2019**). *The Generalized Maximum Likelihood Ratio for the Expectation Value of a Distribution*. [pdf](http://hardy.uhasselt.be/Fishtest/support_MLE_multinomial.pdf)


## Forum & Blog Postings


### 1996 ...


* [Theoretical chess rating question...](https://groups.google.com/d/msg/rec.games.chess.computer/GkgFc3jOl84/vWn-SG8kVboJ) by Cyber Linguist, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 17, 1996
* [Statistical validity of medium-length match results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3014e4ea570dbf38) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 15, 1997
* [Small number statistics and small differences](https://www.stmintz.com/ccc/index.php?id=24669) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), August 14, 1998
* [Re: Waltzing Matilda (was: statistics, 10 events tell us what ?](https://www.stmintz.com/ccc/index.php?id=24978) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), August 17, 1998
* [ELO performance?](https://www.stmintz.com/ccc/index.php?id=52542) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), May 22, 1999 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), [Playing Strength](Playing_Strength "Playing Strength")


### 2000 ...


* [Some thougths about statistics](https://www.stmintz.com/ccc/index.php?id=98901) by Martin Schubert, [CCC](CCC "CCC"), February 24, 2000
* [Who is better? Some statistics...](https://www.stmintz.com/ccc/index.php?id=174578) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), June 11, 2001
* [Simulating the result of a single game by random numbers](https://www.stmintz.com/ccc/index.php?id=178041) by Christoph Fieberg, [CCC](CCC "CCC"), July 03, 2001
* [Simulating the result of a single game by random numbers - Update!](https://www.stmintz.com/ccc/index.php?id=179091) by Christoph Fieberg, [CCC](CCC "CCC"), July 10, 2001
* [Simulating the result of a single game by random numbers - Update!](https://www.stmintz.com/ccc/index.php?id=178939) by Christoph Fieberg, [CCC](CCC "CCC"), August 02, 2001
* [ELO & statistics question](https://www.stmintz.com/ccc/index.php?id=226275) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), April 26, 2002
* [Statistical significance of a match result](https://www.stmintz.com/ccc/index.php?id=267056) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), November 23, 2002
* [Value of playing different versions of a program against each other](https://www.stmintz.com/ccc/index.php?id=275347) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 06, 2003
* [A question about statistics...](https://www.stmintz.com/ccc/index.php?id=340148) by [Roger Brown](index.php?title=Roger_Brown&action=edit&redlink=1 "Roger Brown (page does not exist)"), [CCC](CCC "CCC"), January 04, 2004
* [New tool to estimate the statistical significance of match results](https://www.stmintz.com/ccc/index.php?id=377487) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), July 17, 2004
* [ELOStat algorithm ?](http://www.open-aurec.com/wbforum/viewtopic.php?t=949) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 10, 2004 » [EloStat](index.php?title=EloStat&action=edit&redlink=1 "EloStat (page does not exist)")


### 2005 ...


* [bayeselo: new Elo-rating tool, applied to CCT7](https://www.stmintz.com/ccc/index.php?id=411278) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), February 13, 2005 » [CCT7](CCT7 "CCT7")
* [table for detecting significant difference between two engines](https://www.stmintz.com/ccc/index.php?id=484357) by [Joseph Ciarrochi](index.php?title=Joseph_Ciarrochi&action=edit&redlink=1 "Joseph Ciarrochi (page does not exist)"), [CCC](CCC "CCC"), February 03, 2006 [[46]](#cite_note-46)
* [Observator bias or...](http://www.talkchess.com/forum/viewtopic.php?t=14107) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), May 29, 2007
* [a beat b,b beat c,c beat a question](http://www.talkchess.com/forum/viewtopic.php?t=13800) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 16, 2007
* [how to do a proper statistical test](http://www.talkchess.com/forum/viewtopic.php?t=16545) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), September 19, 2007
* [Comparing two version of the same engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=24590) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), October 26, 2008
* [Debate: testing at fast time controls](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=25461) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), December 15, 2008
* [Elo Calcuation](http://www.talkchess.com/forum/viewtopic.php?t=27516) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), April 19, 2009
* [Likelihood of superiority](http://www.talkchess.com/forum/viewtopic.php?t=30624) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 15, 2009


### 2010 ...


* [Engine Testing - Statistics](http://www.talkchess.com/forum/viewtopic.php?t=31699) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), January 14, 2010


 [Re: Engine Testing - Statistics](http://www.talkchess.com/forum/viewtopic.php?t=31699&start=4) by John Major, [CCC](CCC "CCC"), January 14, 2010
* [Chess Statistics](http://www.talkchess.com/forum/viewtopic.php?t=34989) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), June 17, 2010
* [Do You really need 1000s of games for testing?](http://www.talkchess.com/forum/viewtopic.php?t=36592) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 04, 2010
* [GUI idea: Testing until certainty](http://www.talkchess.com/forum/viewtopic.php?t=36979) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), December 07, 2010
* [SPRT and Engine testing](http://www.talkchess.com/forum/viewtopic.php?t=37056) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), December 13, 2010 » [SPRT](#SPRT)


**2011**



* [Testing very small changes ( <= 5 ELO points of gain)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=38698) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), April 08, 2011
* [Pairwise Analysis of Chess Engine Move Selections](http://www.talkchess.com/forum/viewtopic.php?t=38772) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 17, 2011
* [Ply vs ELO](http://www.talkchess.com/forum/viewtopic.php?t=39511) by Andriy Dzyben, [CCC](CCC "CCC"), June 28, 2011
* [One billion random games](http://www.talkchess.com/forum/viewtopic.php?t=40193) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 27, 2011
* [Increase in Elo ..Question For The Experts](http://www.talkchess.com/forum/viewtopic.php?t=41341) by [Steve B](Steve_Blincoe "Steve Blincoe"), [CCC](CCC "CCC"), December 05, 2011


**2012**



* [Are all test the same?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42032) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), January 17, 2012
* [Advantage for White; Bayeselo (to Rémi Coulom)](http://www.talkchess.com/forum/viewtopic.php?t=42729) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), March 03, 2012
* [Pairwise Analysis of Chess Engine Move Selections Revisited](http://www.talkchess.com/forum/viewtopic.php?t=42737) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), March 04, 2012
* [Human Elo ratings: averages and standard deviations](http://www.talkchess.com/forum/viewtopic.php?t=44219) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), March 18, 2012 [[47]](#cite_note-47)
* [Elo uncertainties calculator](http://www.talkchess.com/forum/viewtopic.php?t=42998) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), March 24, 2012
* [Elo versus speed](http://www.talkchess.com/forum/viewtopic.php?t=43134) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 02, 2012
* [Pawn Advantage, Win Percentage, and Elo](http://www.talkchess.com/forum/viewtopic.php?t=43323) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 15, 2012 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Elo Increase per Doubling](http://www.talkchess.com/forum/viewtopic.php?t=43598) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), May 07, 2012
* [Rybka odds matches and the strength of engines](http://www.talkchess.com/forum/viewtopic.php?t=44003) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 09, 2012 » [Rybka](Rybka "Rybka")
* [A new way to compare chess programs](http://www.talkchess.com/forum/viewtopic.php?t=44147) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), June 21, 2012 » [Komodo](Komodo "Komodo")
* [EloStat, Bayeselo and Ordo](http://www.talkchess.com/forum/viewtopic.php?t=44180) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 24, 2012 » [EloStat](index.php?title=EloStat&action=edit&redlink=1 "EloStat (page does not exist)"), [Bayeselo](index.php?title=Bayeselo&action=edit&redlink=1 "Bayeselo (page does not exist)"), [Ordo](index.php?title=Ordo&action=edit&redlink=1 "Ordo (page does not exist)")
* [about error margins?](http://www.talkchess.com/forum/viewtopic.php?t=44657) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), August 01, 2012
* [normal vs logistic curve for elo model](http://www.talkchess.com/forum/viewtopic.php?t=44670) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 02, 2012
* [Derivation of bayeselo formula](http://www.talkchess.com/forum/viewtopic.php?t=44715) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), August 07, 2012 [[48]](#cite_note-48)
* [Yet Another Testing Question](http://www.talkchess.com/forum/viewtopic.php?t=45158) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), September 15, 2012
* [margin of error](http://www.talkchess.com/forum/viewtopic.php?t=45174) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 16, 2012
* [Average number of plies in {1-0, ½-½, 0-1}](http://www.talkchess.com/forum/viewtopic.php?t=45257) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), September 21, 2012
* [Another testing question](http://www.talkchess.com/forum/viewtopic.php?t=45287) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 23, 2012
* [LOS calculation: Does the same result is always the same?](http://www.talkchess.com/forum/viewtopic.php?t=45406) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 01, 2012
* [LOS (again)](http://www.talkchess.com/forum/viewtopic.php?t=45788) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 30, 2012
* [Elo points gain from doubling time](http://www.talkchess.com/forum/viewtopic.php?t=46370) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 10, 2012
* [A word for casual testers](http://www.talkchess.com/forum/viewtopic.php?t=46572) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 25, 2012


**2013**



* [A poor man's testing environment](http://www.talkchess.com/forum/viewtopic.php?t=46759) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 04, 2013 » [Engine Testing](Engine_Testing "Engine Testing")
* [Noise in ELO estimators: a quantitative approach](http://www.talkchess.com/forum/viewtopic.php?t=46786) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), January 06, 2013
* [Updated Dendrogram](http://www.talkchess.com/forum/viewtopic.php?t=47086) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), February 02, 2013
* [Experiment: influence of colours at fixed depth](http://www.talkchess.com/forum/viewtopic.php?t=47469) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), March 10, 2013
* [LOS](http://www.open-chess.org/viewtopic.php?f=5&t=2296) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 31, 2013
* [Fishtest Distributed Testing Framework](http://www.talkchess.com/forum/viewtopic.php?t=47885) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 01, 2013
* [The influence of the length of openings](http://www.talkchess.com/forum/viewtopic.php?t=48649) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 14, 2013
* [Scaling at 2x nodes (or doubling time control)](http://www.talkchess.com/forum/viewtopic.php?t=48733) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 23, 2013 » [Doubling TC](#DoublingTC), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Houdini](Houdini "Houdini")
* [Type I error in LOS based early stopping rule](http://www.talkchess.com/forum/viewtopic.php?t=48863) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 06, 2013 [[49]](#cite_note-49)
* [How much elo is pondering worth](http://www.talkchess.com/forum/viewtopic.php?t=48864) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), August 07, 2013 » [Pondering](Pondering "Pondering")
* [Contempt and the ELO model](http://www.talkchess.com/forum/viewtopic.php?t=49248) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), September 05, 2013 » [Contempt Factor](Contempt_Factor "Contempt Factor")
* [1 draw=1 win + 1 loss (always!)](http://www.talkchess.com/forum/viewtopic.php?t=49393) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), September 19, 2013
* [SPRT and narrowing of (elo1 - elo0) difference](http://www.talkchess.com/forum/viewtopic.php?t=49584) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), October 05, 2013 » [SPRT](#SPRT)
* [sprt and margin of error](http://www.talkchess.com/forum/viewtopic.php?t=49727) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), October 15, 2013 » [SPRT](#SPRT)
* [How (not) to use SPRT ?](http://www.open-chess.org/viewtopic.php?f=5&t=2477) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), October 19, 2013
* [Houdini, much weaker engines, and Arpad Elo](http://www.talkchess.com/forum/viewtopic.php?t=50266) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 29, 2013 » [Houdini](Houdini "Houdini"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") [[50]](#cite_note-50)
* [Testing on time control versus nodes | ply](http://www.talkchess.com/forum/viewtopic.php?t=50332) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 04, 2013


**2014**



* [Calculating the LOS (likelihood of superiority) from results](http://www.talkchess.com/forum/viewtopic.php?t=51003) by Robert Tournevisse, [CCC](CCC "CCC"), January 22, 2014
* [LOS --> Draws are irrelevant](http://www.open-chess.org/viewtopic.php?f=5&t=2578) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2014
* [Empirically 1 win + 1 loss ~ 2 draws](http://www.talkchess.com/forum/viewtopic.php?t=52746) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 24, 2014
* [Ordo 0.9.6](http://www.talkchess.com/forum/viewtopic.php?t=53645) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), September 10, 2014 » [Ordo](index.php?title=Ordo&action=edit&redlink=1 "Ordo (page does not exist)")
* [Using the Stockfish position evaluation score to predict victory probability](https://chesscomputer.tumblr.com/post/98632536555/using-the-stockfish-position-evaluation-score-to/embed) by unavoidablegrain, [Tumblr](https://en.wikipedia.org/wiki/Tumblr), September 28, 2014 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), [Stockfish](Stockfish "Stockfish")
* [Elo estimation using quasi-Monte Carlo integration](http://www.talkchess.com/forum/viewtopic.php?t=53891) by Branko Radovanovic, [CCC](CCC "CCC"), September 30, 2014
* [SPRT question](http://www.talkchess.com/forum/viewtopic.php?t=54331) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 13, 2014 » [SPRT](#SPRT)
* [Usage sprt / cutechess-cli](http://www.talkchess.com/forum/viewtopic.php?t=54359) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), November 16, 2014 » [Cutechess-cli](Cutechess-cli "Cutechess-cli"), [SPRT](#SPRT)


### 2015 ...


* [2-SPRT](http://www.talkchess.com/forum/viewtopic.php?t=55130) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), January 28, 2015 » [SPRT](#SPRT)
* [Script for computing SPRT probabilities](http://www.talkchess.com/forum/viewtopic.php?t=55893) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), April 05, 2015
* [Maximum ELO gain per test game played?](http://www.talkchess.com/forum/viewtopic.php?t=56067) by Forrest Hoch, [CCC](CCC "CCC"), April 20, 2015
* [Getting SPRT right](http://www.talkchess.com/forum/viewtopic.php?t=56095) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 22, 2015 » [SPRT](#SPRT)
* [SPRT questions](http://www.talkchess.com/forum/viewtopic.php?t=56358) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 15, 2015 » [SPRT](#SPRT)
* [Adam Hair's article on Pairwise comparison of engines](http://www.talkchess.com/forum/viewtopic.php?t=56426) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), May 19, 2015
* [computing elo of multiple chess engines](http://www.talkchess.com/forum/viewtopic.php?t=57223) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 09, 2015
* [Some musings about search](http://www.talkchess.com/forum/viewtopic.php?t=57270) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 14, 2015 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Search](Search "Search")
* [Bullet vs regular time control, say 40/4m CCRL/CEGT](http://www.talkchess.com/forum/viewtopic.php?t=57437) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 29, 2015
* [The SPRT without draw model, elo model or whatever...](http://www.talkchess.com/forum/viewtopic.php?t=57465) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), September 01, 2015 » [SPRT](#SPRT)


 [Re: The SPRT without draw model, elo model or whatever..](http://talkchess.com/forum/viewtopic.php?t=57465&start=19) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), August 18, 2016
* [Name for elo without draws?](http://www.talkchess.com/forum/viewtopic.php?t=57482) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), September 02, 2015
* [The future of chess and elo ratings](http://www.talkchess.com/forum/viewtopic.php?t=57696) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), September 20, 2015 » [Opening Book](Opening_Book "Opening Book")
* [Depth of Satisficing](https://rjlipton.wordpress.com/2015/10/06/depth-of-satisficing/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), October 06, 2015 » [Depth](Depth "Depth"), Match Statistics, [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo") [[51]](#cite_note-51)
* [ELO error margin](http://www.talkchess.com/forum/viewtopic.php?t=57969) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), October 17, 2015
* [testing multiple versions & elo calculation](http://www.talkchess.com/forum/viewtopic.php?t=58067) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 27, 2015
* [A simple expression](http://www.talkchess.com/forum/viewtopic.php?t=58543) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 09, 2015
* [Counting 1 win + 1 loss as 2 draws](http://www.talkchess.com/forum/viewtopic.php?t=58600) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 15, 2015


**2016**



* [A Chess Firewall at Zero?](https://rjlipton.wordpress.com/2016/01/21/a-chess-firewall-at-zero/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), January 21, 2016
* [Ordo 1.0.9 (new features for testers)](http://www.talkchess.com/forum/viewtopic.php?t=59038) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 25, 2016
* [Why the errorbar is wrong ... simple example!](http://www.talkchess.com/forum/viewtopic.php?t=59333) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), February 23, 2016
* [a direct comparison of FIDE and CCRL rating systems](http://www.talkchess.com/forum/viewtopic.php?t=59332) by [Erik Varend](index.php?title=Erik_Varend&action=edit&redlink=1 "Erik Varend (page does not exist)"), [CCC](CCC "CCC"), February 22, 2016 » [FIDE](FIDE "FIDE"), [CCRL](CCRL "CCRL")
* [Some properties of the Type I error in p-value stopping rule](http://www.talkchess.com/forum/viewtopic.php?t=59406) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 01, 2016
* [A Visual Look at 2 Million Chess Games - Thinking Through the Party](https://blog.ebemunk.com/a-visual-look-at-2-million-chess-games/) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)"), March 02, 2016
* [Type I error for p-value stopping: Balanced and Unbalanced](http://www.talkchess.com/forum/viewtopic.php?t=60508) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 16, 2016
* [Empirically Logistic ELO model better suited than Gaussian](http://www.talkchess.com/forum/viewtopic.php?t=60791) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 12, 2016
* [Testing resolution and combining results](http://www.talkchess.com/forum/viewtopic.php?t=60960) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 28, 2016
* [Error margins via resampling (jackknifing)](http://www.talkchess.com/forum/viewtopic.php?t=61105) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 12, 2016 [[52]](#cite_note-52) [[53]](#cite_note-53)
* [Properties of unbalanced openings using Bayeselo model](http://www.talkchess.com/forum/viewtopic.php?t=61245) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 27, 2016 » [Opening Book](Opening_Book "Opening Book")
* [ELO inflation ha ha ha](http://www.talkchess.com/forum/viewtopic.php?t=61444) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), September 16, 2016 » [Delphil](Delphil "Delphil"), [Stockfish](Stockfish "Stockfish"), [Playing Strength](Playing_Strength "Playing Strength"), [TCEC Season 9](TCEC_Season_9 "TCEC Season 9") [[54]](#cite_note-54)


 [About expected scores and draw ratios](http://www.talkchess.com/forum/viewtopic.php?t=61444&start=17) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), September 17, 2016
* [The scaling with time of opening books](http://www.talkchess.com/forum/viewtopic.php?t=61506) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 23, 2016 » [Opening Book](Opening_Book "Opening Book")
* [Perfect play](http://www.talkchess.com/forum/viewtopic.php?t=61548) by Patrik Karlsson, [CCC](CCC "CCC"), September 28, 2016
* [Stockfish underpromotes much more often than Komodo](http://www.talkchess.com/forum/viewtopic.php?t=61601) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), October 05, 2016 » [Komodo](Komodo "Komodo"), [Promotions](Promotions "Promotions"), [Stockfish](Stockfish "Stockfish")
* [Differences between top engines related to "style"](http://www.talkchess.com/forum/viewtopic.php?t=61636) by [Kai Laskos](Kai_Laskos "Kai Laskos"), October 07, 2016
* [SPRT when not used for self testing](http://www.talkchess.com/forum/viewtopic.php?t=61781) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 21, 2016
* [Doubling of time control](http://www.talkchess.com/forum/viewtopic.php?t=61784) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 21, 2016 » [Doubling TC](#DoublingTC), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Komodo](Komodo "Komodo")
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](#DoublingTC), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")
* [When Data Serves Turkey](https://rjlipton.wordpress.com/2016/11/30/when-data-serves-turkey/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), November 30, 2016
* [Magnus and the Turkey Grinder](https://rjlipton.wordpress.com/2016/12/08/magnus-and-the-turkey-grinder/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), December 08, 2016 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") [[55]](#cite_note-55)
* [Regan's conundrum](http://www.talkchess.com/forum/viewtopic.php?t=62435) by [Carl Lumma](index.php?title=Carl_Lumma&action=edit&redlink=1 "Carl Lumma (page does not exist)"), [CCC](CCC "CCC"), December 09, 2016
* [Statistical Interpretation](http://www.talkchess.com/forum/viewtopic.php?t=62438) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), December 10, 2016
* [Absolute ELO scale](http://www.talkchess.com/forum/viewtopic.php?t=62510) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), December 17, 2016
* [A question about SPRT](http://www.talkchess.com/forum/viewtopic.php?t=62598) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 25, 2016 » [SPRT](#SPRT)
* [Diminishing returns and hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=62622) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 27, 2016 » [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Thread](Thread "Thread")


**2017**



* [Progress in 30 years by four intervals of 7-8 years](http://www.talkchess.com/forum/viewtopic.php?t=62868) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 19, 2017 » [Playing Strength](Playing_Strength "Playing Strength")
* [sprt tourney manager](http://www.talkchess.com/forum/viewtopic.php?t=62922) by [Richard Delorme](Richard_Delorme "Richard Delorme"), [CCC](CCC "CCC"), January 24, 2017 » [Amoeba Tournament Manager](Amoeba#TournamentManager "Amoeba"), [SPRT](#SPRT)
* [Binomial distribution for chess statistics](http://www.talkchess.com/forum/viewtopic.php?t=63327) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [CCC](CCC "CCC"), March 03, 2017
* [Higher than expected by me efficiency of Ponder ON](http://www.talkchess.com/forum/viewtopic.php?t=63355) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 06, 2017 » [Pondering](Pondering "Pondering")
* [What can be said about 1 - 0 score?](http://www.talkchess.com/forum/viewtopic.php?t=63572) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 28, 2017
* [6-men Syzygy from HDD and USB 3.0](http://www.talkchess.com/forum/viewtopic.php?t=63652) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 04, 2017 » [Komodo](Komodo "Komodo"), [Playing Strength](Playing_Strength "Playing Strength"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases"), [USB 3.0](Memory#USB3 "Memory")
* [Scaling of engines from FGRL rating list](http://www.talkchess.com/forum/viewtopic.php?t=63687) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 07, 2017 » [FGRL](FGRL "FGRL")
* [Low impact of opening phase in engine play?](http://www.talkchess.com/forum/viewtopic.php?t=63763) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 18, 2017 » [Opening](Opening "Opening")
* [How to simulate a game outcome given Elo difference?](http://www.talkchess.com/forum/viewtopic.php?t=63813) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 25, 2017
* [Wilo rating properties from FGRL rating lists](http://www.talkchess.com/forum/viewtopic.php?t=63875) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 01, 2017 » [FGRL](FGRL "FGRL")
* [MATCH sanity](http://www.talkchess.com/forum/viewtopic.php?t=63888) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 03, 2017 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")


 [Re: MATCH sanity](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=63888&start=2) by [Salvatore Giannotti](Salvatore_Giannotti "Salvatore Giannotti"), [CCC](CCC "CCC"), May 03, 2017
* [Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum/viewtopic.php?t=63903) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 05, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Symmetric multiprocessing (SMP) scaling - K10.4 Contempt=0](http://www.talkchess.com/forum/viewtopic.php?t=63955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 11, 2017 » [SMP](SMP "SMP"), [Komodo](Komodo "Komodo"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Symmetric multiprocessing (SMP) scaling - SF8 Contempt=10](http://www.talkchess.com/forum/viewtopic.php?t=63967) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 13, 2017 » [SMP](SMP "SMP"), [Stockfish](Stockfish "Stockfish"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Likelihood Of Success (LOS) in the real world](http://www.talkchess.com/forum/viewtopic.php?t=64084) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 26, 2017
* [Opening testing suites efficiency](http://www.talkchess.com/forum/viewtopic.php?t=64358) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 21, 2017 » [Engine Testing](Engine_Testing "Engine Testing"), [Opening](Opening "Opening")
* [Testing A against B by playing a pool of others](http://www.talkchess.com/forum/viewtopic.php?t=64394) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 24, 2017
* [Engine testing & error margin ?](http://www.talkchess.com/forum/viewtopic.php?t=64519) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), July 05, 2017
* [Invariance with time control of rating schemes](http://www.talkchess.com/forum/viewtopic.php?t=64683) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 22, 2017 [[56]](#cite_note-56)
* [Ways to avoid "Draw Death" in Computer Chess](http://www.talkchess.com/forum/viewtopic.php?t=64719) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 25, 2017
* [SMP NPS measurements](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=2) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Parallel Search](Parallel_Search "Parallel Search"), [Nodes per Second](Nodes_per_Second "Nodes per Second")


 [ELO measurements](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=3) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Playing Strength](Playing_Strength "Playing Strength")
* [What is a Match?](http://www.talkchess.com/forum/viewtopic.php?t=65061) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), September 01, 2017
* [Scaling from FGRL results with top 3 engines](http://www.talkchess.com/forum/viewtopic.php?t=65288) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 26, 2017 » [FGRL](FGRL "FGRL"), [Houdini](Houdini "Houdini"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Statistical interpretation of search and eval scores](http://www.talkchess.com/forum/viewtopic.php?t=65764) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), November 18, 2017 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), [Score](Score "Score")
* ["Intrinsic Chess Ratings" by Regan, Haworth -- seq](http://www.talkchess.com/forum/viewtopic.php?t=65772) by Kai Middleton, [CCC](CCC "CCC"), November 19, 2017


 [Re: "Intrinsic Chess Ratings" by Regan, Haworth --](http://www.talkchess.com/forum/viewtopic.php?t=65772&start=2) by [Kenneth Regan](Kenneth_W._Regan "Kenneth W. Regan"), [CCC](CCC "CCC"), November 20, 2017 » [Who is the Master?](Jean-Marc_Alliot#WhoistheMaster "Jean-Marc Alliot")
* [ELO progression measured by year](http://www.talkchess.com/forum/viewtopic.php?t=66000) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 13, 2017


**2018**



* [Wrong use of SPRT](https://groups.google.com/d/msg/fishcooking/nqgLNUfjkok/gfMr7amXCAAJ) by [Uri Blass](Uri_Blass "Uri Blass"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 09, 2018 » [Contempt Factor](Contempt_Factor "Contempt Factor"), [SPRT](#SPRT)
* [Feed bayeselo with pure game results without PGN](http://www.talkchess.com/forum/viewtopic.php?t=66775) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 08, 2018
* [Elo measurement of contempt in SF in self-play](http://www.talkchess.com/forum/viewtopic.php?t=66793) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), March 10, 2018 » [Contempt](Contempt_Factor "Contempt Factor"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")
* [Time control envelope in top engines could be improved?](http://www.talkchess.com/forum/viewtopic.php?t=66821) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 13, 2018 » [Time Management](Time_Management "Time Management")
* [LCZero: Progress and Scaling. Relation to CCRL Elo](http://www.talkchess.com/forum/viewtopic.php?t=66945) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 28, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [Elostat Question](http://www.talkchess.com/forum/viewtopic.php?t=66969) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 30, 2018
* [Issue with self play testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67485) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), May 18, 2018 » [Engine Testing](Engine_Testing "Engine Testing")
* [Why Lc0 eval (in cp) is asymmetric against AB engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68072) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 25, 2018 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation"), [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Are draws hard to predict?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69069) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 27, 2018 » [Draw](Draw "Draw"), [Neural Networks](Neural_Networks "Neural Networks")
* [testing consistency](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69284) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 16, 2018
* [Fixed nodes games and the pentanomial model](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69407) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), December 29, 2018


**2019**



* [Schizophrenic rating model for Leela](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69672) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 21, 2019 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [best way to determine elos of a group](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71419) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), July 30, 2019


### 2020 ...


* [Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962) by Deberger, [CCC](CCC "CCC"), February 01, 2020 » [Stockfish](Stockfish "Stockfish")


 [Re: Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962&start=6) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), February 02, 2020
* [repackaging of Fishtest's SPRT calculation code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73419) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 20, 2020 » [SPRT](#SPRT)
* [Stockfish\_dev is probably stronger than Sargon 1978 v1.00](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74037) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 29, 2020 » [Stockfish](Stockfish "Stockfish"), [Sargon](Sargon "Sargon")
* [Throwing out draws to calculate Elo](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74319) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 29, 2020
* [Jackknife estimate of the variance of engine results for Arasan test suite](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75006) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 05, 2020 » [Statistical Analysis](#Statistical_Analysis)


**2021**



* [What K factor should be used if two players are in different K factor brackets?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76261) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), January 09, 2021 [[57]](#cite_note-57) [[58]](#cite_note-58)
* [Cutechess-cli and SPRT](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76370) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 19, 2021 » [Cutechess-cli](Cutechess-cli "Cutechess-cli"), [SPRT](#SPRT)
* [correspondence chess in the age of NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76382) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 21, 2021 » [NNUE](NNUE "NNUE")
* [what is the rating of engines when you do not count draws?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77544) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 23, 2021


**2022**



* [How do you know you improved ?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79280) by Philippe Chevalier, [CCC](CCC "CCC"), February 03, 2022


## External Links


### Rating Systems


* [Chessmetrics from Wikipedia](https://en.wikipedia.org/wiki/Chessmetrics)
* [Chess rating system from Wikipedia](https://en.wikipedia.org/wiki/Chess_rating_systems)
* [Elo rating system from Wikipedia](https://en.wikipedia.org/wiki/Elo_rating_system)
* [Arpad Elo and the Elo Rating System](http://en.chessbase.com/post/arpad-elo-and-the-elo-rating-system) by [Dan Ross](index.php?title=Dan_Ross&action=edit&redlink=1 "Dan Ross (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), December 16, 2007
* [Chess ratings - Elo versus the Rest of the World](https://www.kaggle.com/c/chess) | [Kaggle](https://en.wikipedia.org/wiki/Kaggle)
* [Elo Win Probability Calculator](http://wismuth.com/elo/calculator.html) by [François Labelle](Mathematician#FLabelle "Mathematician")
* [LOS Table](http://www.husvankempen.de/nunn/rating/tablejoseph.htm) by [Joseph Ciarrochi](index.php?title=Joseph_Ciarrochi&action=edit&redlink=1 "Joseph Ciarrochi (page does not exist)") from [CEGT](CEGT "CEGT") [[59]](#cite_note-59)
* [Kirr's Chess Engine Comparison KCEC - Draw rate](http://kirill-kryukov.com/chess/kcec/draw_rate.html) » [KCEC](KCEC "KCEC")
* [Chessanalysis homepage](http://www.chessanalysis.ee/chessanalysiseng.htm) by [Erik Varend](index.php?title=Erik_Varend&action=edit&redlink=1 "Erik Varend (page does not exist)") [[60]](#cite_note-60)
* [Who is the Master?](http://www.alliot.fr/CHESS/ficga.html.en) by [Jean-Marc Alliot](Jean-Marc_Alliot "Jean-Marc Alliot") » [Who is the Master?](Jean-Marc_Alliot#WhoistheMaster "Jean-Marc Alliot")
* [How Should Chess Players Be Rated?](https://news.cnrs.fr/articles/how-should-chess-players-be-rated) by [Martin Koppe](https://news.cnrs.fr/authors/martin-koppe), [CNRS News](https://news.cnrs.fr/), April 25, 2017
* [Ranking chess players according to the quality of their moves](https://en.chessbase.com/post/ranking-chess-players-according-to-the-quality-of-their-moves) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), April 27, 2017
* [Rating List Stats](http://rebel13.nl/misc/stats.html) by [Ed Schroder](Ed_Schroder "Ed Schroder") » [CCRL](CCRL "CCRL")


### Tools


* [BayesElo](http://remi.coulom.free.fr/Bayesian-Elo/) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") builds tournament-statistics from a [pgn-file](Portable_Game_Notation "Portable Game Notation")
* [Elostat](http://wbec-ridderkerk.nl/html/download.htm) by [Frank Schubert](index.php?title=Frank_Schubert&action=edit&redlink=1 "Frank Schubert (page does not exist)") builds tournament-statistics from a pgn-file
* [Online Elo-Calculator](http://www.dirtychess.com/tools.php) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan")
* [Ordo](https://sites.google.com/site/gaviotachessengine/ordo) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora")


### Statistics


* [Statistics from Wikipedia](https://en.wikipedia.org/wiki/Statistics)
* [Statistical assumption from Wikipedia](https://en.wikipedia.org/wiki/Statistical_assumptions)
* [Statistical inference from Wikipedia](https://en.wikipedia.org/wiki/Statistical_inference)
* [Probability theory from Wikipedia](https://en.wikipedia.org/wiki/Probability_theory)
* [Probability from Wikipedia](https://en.wikipedia.org/wiki/Probability)
* [Probability density function from Wikipedia](https://en.wikipedia.org/wiki/Probability_density_function)
* [Likelihood function from Wikipedia](https://en.wikipedia.org/wiki/Likelihood_function)
* [p-value from Wikipedia](https://en.wikipedia.org/wiki/P-value)
* [Misunderstandings of p-values from Wikipedia](https://en.wikipedia.org/wiki/Misunderstandings_of_p-values)
* [Probability distribution from Wikipedia](https://en.wikipedia.org/wiki/Probability_distribution)
* [Binomial distribution from Wikipedia](https://en.wikipedia.org/wiki/Binomial_distribution)
* [Cumulative distribution function from Wikipedia](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
* [Multinomial distribution from Wikipedia](https://en.wikipedia.org/wiki/Multinomial_distribution)
* [Multivariate normal distribution from Wikipedia](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
* [Normal distribution from Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution)
* [Standard deviation from Wikipedia](https://en.wikipedia.org/wiki/Standard_deviation)
* [Standard error from Wikipedia](https://en.wikipedia.org/wiki/Standard_error_%28statistics%29)
* [Error bar from Wikipedia](https://en.wikipedia.org/wiki/Error_bar)
* [Margin of error from Wikipedia](https://en.wikipedia.org/wiki/Margin_of_error)
* [Confidence interval from Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval)
* [Null hypothesis from Wikipedia](https://en.wikipedia.org/wiki/Null_hypothesis)
* [Alternative hypothesis from Wikipedia](https://en.wikipedia.org/wiki/Alternative_hypothesis)
* [Two-tailed test from Wikipedia](https://en.wikipedia.org/wiki/Two-tailed_test)
* [Type I and type II errors from Wikipedia](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
* [Type 1 Errors | Hypothesis testing with one sample](https://www.khanacademy.org/math/probability/statistics-inferential/hypothesis-testing/v/type-1-errors) | [Khan Academy](https://en.wikipedia.org/wiki/Khan_Academy)


### Hypothesis Testing


* [Statistical hypothesis testing from Wikipedia](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
* [Likelihood-ratio test from Wikipedia](https://en.wikipedia.org/wiki/Likelihood-ratio_test)
* [Score test from Wikipedia](https://en.wikipedia.org/wiki/Score_test)
* [Wald test from Wikipedia](https://en.wikipedia.org/wiki/Wald_test)


### Sequential Analysis


* [Sequential analysis from Wikipedia](https://en.wikipedia.org/wiki/Sequential_analysis)
* [Sequential probability ratio test from Wikipedia](https://en.wikipedia.org/wiki/Sequential_probability_ratio_test)
* [GitHub - vdbergh/pentanomial: SPRT for pentanomial frequencies and simulation tools](https://github.com/vdbergh/pentanomial) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
* [GitHub - vdbergh/simul: A multi-threaded pentanomial simulator](https://github.com/vdbergh/simul) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")


### Data Visualization


* [A Visual Look at 2 Million Chess Games - Thinking Through the Party](https://blog.ebemunk.com/a-visual-look-at-2-million-chess-games/) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)"), March 02, 2016 [[61]](#cite_note-61)
* [GitHub - ebemunk/chess-dataviz: chess visualization library written for d3.js](https://github.com/ebemunk/chess-dataviz) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)") » [JavaScript](JavaScript "JavaScript")
* [GitHub - ebemunk/pgnstats: parses PGN files and extracts statistics for chess games](https://github.com/ebemunk/pgnstats) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)") » [Go (Programming Language)](Go_(Programming_Language) "Go (Programming Language)"), [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")


### Misc


* [Jeff Beck](Category:Jeff_Beck "Category:Jeff Beck"), [Jan Hammer](Category:Jan_Hammer "Category:Jan Hammer"), [Fernando Saunders](https://en.wikipedia.org/wiki/Fernando_Saunders), [Simon Phillips](Category:Simon_Phillips "Category:Simon Phillips") - [Definitely Maybe](https://en.wikipedia.org/wiki/Definitely_Maybe_%28disambiguation%29), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [ARMS Charity Concert](https://en.wikipedia.org/wiki/ARMS_Charity_Concerts), [Madison Square Garden](https://en.wikipedia.org/wiki/Madison_Square_Garden), [December 08, 1983](http://forums.ledzeppelin.com/index.php?/topic/394-arms-benefit-concerts-in-nyc-dec-1983/)
 
* [Björk](Category:Bj%C3%B6rk "Category:Björk") - [Possibly Maybe](https://en.wikipedia.org/wiki/Possibly_Maybe) (1996), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) Image based on [Standard deviation diagram](https://commons.wikimedia.org/wiki/File:Standard_deviation_diagram.svg) by [Mwtoews](https://commons.wikimedia.org/wiki/User:Mwtoews), April 7, 2007 with [R code](https://en.wikipedia.org/wiki/R_(programming_language)) given, [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Normal distribution from Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution)
2. [↑](#cite_ref-2) [Kirr's Chess Engine Comparison KCEC - Draw rate](http://kirill-kryukov.com/chess/kcec/draw_rate.html) » [KCEC](KCEC "KCEC")
3. [↑](#cite_ref-3) [Doubling of time control](http://www.talkchess.com/forum/viewtopic.php?t=61784) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 21, 2016
4. [↑](#cite_ref-4) [K93-Doubling-TC.pdf](http://fastgm.de/K93-Doubling-TC.pdf)
5. [↑](#cite_ref-5) [Scaling at 2x nodes (or doubling time control)](http://www.talkchess.com/forum/viewtopic.php?t=48733) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 23, 2013
6. [↑](#cite_ref-6) [Re: Likelihood Of Success (LOS) in the real world](http://www.talkchess.com/forum/viewtopic.php?t=64084&start=5) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), May 26, 2017
7. [↑](#cite_ref-7) [Re: Calculating the LOS (likelihood of superiority) from results](http://www.talkchess.com/forum/viewtopic.php?t=51003&start=5) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 23, 2014
8. [↑](#cite_ref-8) [Re: Calculating the LOS (likelihood of superiority) from results](http://www.talkchess.com/forum/viewtopic.php?t=51003&start=1) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 22, 2014
9. [↑](#cite_ref-9) [Re: Likelihood of superiority](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=303382&t=30624) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), November 15, 2009
10. [↑](#cite_ref-10) [Re: Likelihood of superiority](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=303405&t=30624) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), November 15, 2009
11. [↑](#cite_ref-11) [Error function from Wikipedia](https://en.wikipedia.org/wiki/Error_function)
12. [↑](#cite_ref-12) [The Open Group Base Specifications Issue 6IEEE Std 1003.1, 2004 Edition: erf](http://pubs.opengroup.org/onlinepubs/000095399/functions/erf.html)
13. [↑](#cite_ref-13) [erf(x) and math.h](http://stackoverflow.com/questions/631629/erfx-and-math-h) by user76293, [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow_%28website%29), March 10, 2009
14. [↑](#cite_ref-14) [Re: Calculating the LOS (likelihood of superiority) from results](http://www.talkchess.com/forum/viewtopic.php?t=51003&start=2) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 22, 2014
15. [↑](#cite_ref-15) [Error margins via resampling (jackknifing)](http://www.talkchess.com/forum/viewtopic.php?t=61105) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 12, 2016
16. [↑](#cite_ref-16) [Properties of unbalanced openings using Bayeselo model](http://talkchess.com/forum/viewtopic.php?t=61245) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 27, 2016
17. [↑](#cite_ref-17) [Abraham Wald](Mathematician#AWald "Mathematician") (**1945**). *Sequential Tests of Statistical Hypotheses*. [Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 16, No. 2, [doi](https://en.wikipedia.org/wiki/Digital_object_identifier): [10.1214/aoms/1177731118](http://projecteuclid.org/euclid.aoms/1177731118)
18. [↑](#cite_ref-18) [Sequential probability ratio test from Wikipedia](https://en.wikipedia.org/wiki/Sequential_probability_ratio_test)
19. [↑](#cite_ref-19) [Arthur Guez](Arthur_Guez "Arthur Guez") (**2015**). *Sample-based Search Methods for Bayes-Adaptive Planning*. Ph.D. thesis, Gatsby Computational Neuroscience Unit, [University College London](https://en.wikipedia.org/wiki/University_College_London), [pdf](http://www.gatsby.ucl.ac.uk/~aguez/files/guez_phdthesis2015.pdf)
20. [↑](#cite_ref-20) [Jack Good](Jack_Good "Jack Good") (**1979**). *[Studies in the history of probability and statistics. XXXVII AM Turing’s statistical work in World War II](https://www.jstor.org/stable/2335677)*. [Biometrika](https://en.wikipedia.org/wiki/Biometrika), Vol. 66, No. 2
21. [↑](#cite_ref-21) [How (not) to use SPRT ?](http://www.open-chess.org/viewtopic.php?f=5&t=2477) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), October 19, 2013
22. [↑](#cite_ref-22) [Re: The SPRT without draw model, elo model or whatever..](http://talkchess.com/forum/viewtopic.php?t=57465&start=19) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), August 18, 2016
23. [↑](#cite_ref-23) [GSPRT approximation](http://hardy.uhasselt.be/Toga/GSPRT_approximation.pdf) (pdf) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
24. [↑](#cite_ref-24) [Re: Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962&start=6) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), February 02, 2020
25. [↑](#cite_ref-25) [GitHub - vdbergh/pentanomial: SPRT for pentanomial frequencies and simulation tools](https://github.com/vdbergh/pentanomial) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
26. [↑](#cite_ref-26) [Re: Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962&start=7) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), February 02, 2020
27. [↑](#cite_ref-27) [GitHub - vdbergh/simul: A multi-threaded pentanomial simulator](https://github.com/vdbergh/simul) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
28. [↑](#cite_ref-28) [Law of comparative judgment - Wikipedia](https://en.wikipedia.org/wiki/Law_of_comparative_judgment)
29. [↑](#cite_ref-29) [Elo's Book: The Rating of Chess Players](http://www.anusha.com/elosbook.htm) by [Sam Sloan](Sam_Sloan "Sam Sloan")
30. [↑](#cite_ref-30) [The Master Game from Wikipedia](https://en.wikipedia.org/wiki/The_Master_Game)
31. [↑](#cite_ref-31) [Handwritten Notes on the 2004 David R. Hunter Paper 'MM Algorithms for Generalized Bradley-Terry Models'](http://remi.coulom.free.fr/Bayesian-Elo/MMNotes.pdf) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom")
32. [↑](#cite_ref-32) [Derivation of bayeselo formula](http://www.talkchess.com/forum/viewtopic.php?t=44715) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), August 07, 2012
33. [↑](#cite_ref-33) [Mm algorithm from Wikipedia](https://en.wikipedia.org/wiki/Mm_algorithm)
34. [↑](#cite_ref-34) [Pairwise comparison from Wikipedia](https://en.wikipedia.org/wiki/Pairwise_comparison)
35. [↑](#cite_ref-35) [Bayesian inference from Wikipedia](https://en.wikipedia.org/wiki/Bayesian_inference)
36. [↑](#cite_ref-36) [How I did it: Diogo Ferreira on 4th place in Elo chess ratings competition | no free hunch](http://blog.kaggle.com/2010/11/30/how-i-did-it-diogo-ferreira-on-4th-place-in-elo-chess-ratings-competition/)
37. [↑](#cite_ref-37)  ["Intrinsic Chess Ratings" by Regan, Haworth -- seq](http://www.talkchess.com/forum/viewtopic.php?t=65772) by Kai Middleton, [CCC](CCC "CCC"), November 19, 2017
38. [↑](#cite_ref-38) [Re: EloStat, Bayeselo and Ordo](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=471004&t=44180) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), June 25, 2012
39. [↑](#cite_ref-39) [Re: Understanding and Pushing the Limits of the Elo Rating Algorithm](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72087&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 15, 2019
40. [↑](#cite_ref-40) [Ply versus ELO](https://www.hiarcs.net/forums/viewtopic.php?t=10004) by Greg, [HIARCS Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2020 » [Diogo R. Ferreira - Impact of the Search Depth ...](Diogo_R._Ferreira#Impact "Diogo R. Ferreira")
41. [↑](#cite_ref-41) [Ordo](https://sites.google.com/site/gaviotachessengine/ordo) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora")
42. [↑](#cite_ref-42) [Pairwise Analysis of Chess Engine Move Selections](http://www.talkchess.com/forum/viewtopic.php?t=38772) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 17, 2011
43. [↑](#cite_ref-43) [Questions regarding rating systems of humans and engines](http://www.talkchess.com/forum/viewtopic.php?t=54571) by [Erik Varend](index.php?title=Erik_Varend&action=edit&redlink=1 "Erik Varend (page does not exist)"), [CCC](CCC "CCC"), December 06, 2014
44. [↑](#cite_ref-44) [chess statistics scientific article](http://www.talkchess.com/forum/viewtopic.php?t=60721) by Nuno Sousa, [CCC](CCC "CCC"), July 06, 2016
45. [↑](#cite_ref-45) [Understanding and Pushing the Limits of the Elo Rating Algorithm](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72087) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), October 15, 2019
46. [↑](#cite_ref-46) [LOS Table](http://www.husvankempen.de/nunn/rating/tablejoseph.htm) by [Joseph Ciarrochi](index.php?title=Joseph_Ciarrochi&action=edit&redlink=1 "Joseph Ciarrochi (page does not exist)") from [CEGT](CEGT "CEGT")
47. [↑](#cite_ref-47) [Arpad Elo and the Elo Rating System](http://en.chessbase.com/post/arpad-elo-and-the-elo-rating-system) by [Dan Ross](index.php?title=Dan_Ross&action=edit&redlink=1 "Dan Ross (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), December 16, 2007
48. [↑](#cite_ref-48) [David R. Hunter](Mathematician#DHunter "Mathematician") (**2004**). *MM Algorithms for Generalized Bradley-Terry Models*. [The Annals of Statistics](https://en.wikipedia.org/wiki/Annals_of_Statistics), Vol. 32, No. 1, 384–406, [pdf](http://sites.stat.psu.edu/~dhunter/papers/bt.pdf)
49. [↑](#cite_ref-49) [Type I and type II errors from Wikipedia](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
50. [↑](#cite_ref-50) [Arpad Elo - Wikipedia](https://en.wikipedia.org/wiki/Arpad_Elo)
51. [↑](#cite_ref-51) [Regan's latest: Depth of Satisficing](http://www.talkchess.com/forum/viewtopic.php?t=57890) by [Carl Lumma](index.php?title=Carl_Lumma&action=edit&redlink=1 "Carl Lumma (page does not exist)"), [CCC](CCC "CCC"), October 09, 2015
52. [↑](#cite_ref-52) [Resampling (statistics) from Wikipedia](https://en.wikipedia.org/wiki/Resampling_(statistics))
53. [↑](#cite_ref-53) [Jackknife resampling from WIkipedia](https://en.wikipedia.org/wiki/Jackknife_resampling)
54. [↑](#cite_ref-54) [Delphil 3.3b2 (2334) - Stockfish 030916 (3228), TCEC Season 9 - Rapid, Round 11](http://tcec.chessdom.com/archive.php?se=9&rapid&ga=163), September 16, 2016
55. [↑](#cite_ref-55) [World Chess Championship 2016 from Wikipedia](https://en.wikipedia.org/wiki/World_Chess_Championship_2016)
56. [↑](#cite_ref-56) [Normalized Elo](http://hardy.uhasselt.be/Toga/normalized_elo.pdf) (pdf) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
57. [↑](#cite_ref-57) [Most accurate K-factor - Elo rating system from Wikipedia](https://en.wikipedia.org/wiki/Elo_rating_system#Most_accurate_K-factor)
58. [↑](#cite_ref-58) [FIDE Chess Rating calculators: Chess Rating change calculator](https://ratings.fide.com/calculator_rtd.phtml)
59. [↑](#cite_ref-59) [table for detecting significant difference between two engines](https://www.stmintz.com/ccc/index.php?id=484357) by [Joseph Ciarrochi](index.php?title=Joseph_Ciarrochi&action=edit&redlink=1 "Joseph Ciarrochi (page does not exist)"), [CCC](CCC "CCC"), February 03, 2006
60. [↑](#cite_ref-60) [an interesting study from Erik Varend](http://www.hiarcs.net/forums/viewtopic.php?t=8526) by scandien, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), August 13, 2017
61. [↑](#cite_ref-61) [A Visual Look at 2 Million Chess Games](http://www.talkchess.com/forum/viewtopic.php?t=65610) by Brahim Hamadicharef, [CCC](CCC "CCC"), November 02, 2017

**[Up one level](Engine_Testing "Engine Testing")**







 
