---
title: Simulated Annealing
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Simulated Annealing**



[ Glowing [train wheels](https://en.wikipedia.org/wiki/Train_wheel) [[1]](#cite_note-1)
**Simulated Annealing**, (SA)  

a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) based algorithm for [combinatorial optimization problems](https://en.wikipedia.org/wiki/Combinatorial_optimization) inspired by [statistical mechanics](https://en.wikipedia.org/wiki/Statistical_mechanics) in [thermodynamics](https://en.wikipedia.org/wiki/Thermodynamics) with the [statistical ensemble](https://en.wikipedia.org/wiki/Statistical_ensemble_(mathematical_physics)) of the [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution) over all possible [states](https://en.wikipedia.org/wiki/Thermodynamic_state) of a [system](https://en.wikipedia.org/wiki/Thermodynamic_system) described by a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain), where its [stationary distribution](https://en.wikipedia.org/wiki/Stationary_distribution) converts to an optimal distribution during a [cooling process](https://en.wikipedia.org/wiki/Cooling) after reaching the [equilibrium](https://en.wikipedia.org/wiki/Thermodynamic_equilibrium). Thus, the annealing algorithm simulates a nonstationary [finite state Markov chain](https://en.wikipedia.org/wiki/Markov_chain#Finite_state_space) whose [state space](https://en.wikipedia.org/wiki/State_space) is the domain of the [cost function](https://en.wikipedia.org/wiki/Loss_function) called [energy](https://en.wikipedia.org/wiki/Internal_energy) to be minimized [[2]](#cite_note-2). 



### Contents


- [Quotes](#quotes)
- [Applications](#applications)
- [Algorithm](#algorithm)
  - [Description](#description)
  - [Animation](#animation)
  - [Pseudo Code](#pseudo-code)
- [See also](#see-also)
- [Selected Publications](#selected-publications)
  - [1948 ...](#1948-)
  - [1950 ...](#1950-)
  - [1970 ...](#1970-)
  - [1980 ...](#1980-)
  - [1990 ...](#1990-)
  - [2000 ...](#2000-)
  - [2010 ...](#2010-)
- [Forum Posts](#forum-posts)
- [External Links](#external-links)
  - [Simulated Annealing](#simulated-annealing)
  - [Related Topics](#related-topics)
  - [Misc](#misc)
- [References](#references)






The annealing algorithm is an adaptation of the [Metropolis–Hastings algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) to generate sample states of a [thermodynamic system](https://en.wikipedia.org/wiki/Thermodynamic_system), invented by [Marshall Rosenbluth](Mathematician#MRosenbluth "Mathematician") and published by [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis) et al. in 1953 [[3]](#cite_note-3) [[4]](#cite_note-4) , later generalized by [W. Keith Hastings](Mathematician#WKHastings "Mathematician") at [University of Toronto](University_of_Toronto "University of Toronto") [[5]](#cite_note-5). According to [Roy Glauber](Mathematician#RJlauber "Mathematician") and [Emilio Segrè](Mathematician#ESegre "Mathematician"), the original algorithm was invented by [Enrico Fermi](Mathematician#EFermi "Mathematician") and reinvented by [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam") [[6]](#cite_note-6). 


SA was independently described by [Scott Kirkpatrick](Mathematician#SKirkpatrick "Mathematician"), [C. Daniel Gelatt](Mathematician#CDGelatt "Mathematician") and Mario P. Vecchi in 1983 [[7]](#cite_note-7), at that time affiliated with [IBM Thomas J. Watson Research Center, Yorktown Heights](https://en.wikipedia.org/wiki/Thomas_J._Watson_Research_Center), and by Vlado Černý from [Comenius University](https://en.wikipedia.org/wiki/Comenius_University), [Bratislava](https://en.wikipedia.org/wiki/Bratislava) in 1985 [[8]](#cite_note-8).



## Quotes


In the 2003 conference proceedings *Celebrating the 50th Anniversary of the Metropolis Algorithm* [[9]](#cite_note-9) [[10]](#cite_note-10), [Marshall Rosenbluth](Mathematician#MRosenbluth "Mathematician") describes the algorithm in the following beautifully concise and clear manner [[11]](#cite_note-11):




```
A simple way to do this [sampling configurations with the [Boltzmann weight](https://en.wikipedia.org/wiki/Boltzmann_distribution)], as emerged after discussions with [Teller](Mathematician#ETeller "Mathematician"), would be to make a trial move: if it decreased the energy of the system, allow it; if it increased the energy, allow it with [probability](https://en.wikipedia.org/wiki/Probability) exp(−ΔE/kT) as determined by a comparison with a [random number](Pseudorandom_Number_Generator "Pseudorandom Number Generator"). Each step, after an initial annealing period, is counted as a member of the ensemble, and the appropriate ensemble average of any quantity determined. 

```

## Applications


SA has multiple applications in discrete [NP-hard](https://en.wikipedia.org/wiki/NP-hardness) optimization problems such as the [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), in [machine learning](Learning "Learning"), in training of [neural networks](Neural_Networks "Neural Networks"), and in the domain of computer games and computer chess in [automated tuning](Automated_Tuning "Automated Tuning") as elaborated by [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") in his Ph.D. thesis [[12]](#cite_note-12) to optimize the [evaluation](Evaluation "Evaluation") weight vector in [Zugzwang](Zugzwang_(Program) "Zugzwang (Program)"). In its variant of [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") to adjust pattern weights in [Morph](Morph "Morph"), [Robert Levinson](Robert_Levinson "Robert Levinson") at al. used simulated annealing as [metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic) to set its own learning rate for each pattern, the more frequently a pattern is updated, the slower becomes its learning rate [[13]](#cite_note-13) [[14]](#cite_note-14) [[15]](#cite_note-15). 



## Algorithm


### Description


The [control flow](https://en.wikipedia.org/wiki/Control_flow) of the algorithm is determined by two nested loops, the outer loop over decreasing [temperature](https://en.wikipedia.org/wiki/Temperature) simulates the cooling, and an inner loop times n Monte Carlo [iterations](Iteration "Iteration"). Each time a randomly picked neighbor state inside the inner loop provides a better energy or [fitness](https://en.wikipedia.org/wiki/Fitness_function) than the current state, the neighbor becomes the new current and even new optimum if fitter than fittest so far. Otherwise, if the neighbor fitness does not exceed current, it might still become current depending on the positive fitness or energy difference ΔE, and [absolute temperature](https://en.wikipedia.org/wiki/Kelvin) T, with a [probability](https://en.wikipedia.org/wiki/Probability) p according to the [Boltzmann factor](https://en.wikipedia.org/wiki/Boltzmann_distribution):



 [](File:SimulatedAnnealingBoltzmannFactor.jpg) 
where k the [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant), and [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)) base of the [exponential function](https://en.wikipedia.org/wiki/Exponential_function) whose negative exponent ensures the [0, 1] probability interval. Accepting worse solutions is a primary feature of SA, and important to stop [greedy](https://en.wikipedia.org/wiki/Greedy_algorithm) [exploitation](https://en.wikipedia.org/wiki/Exploitation) a [local optimum](https://en.wikipedia.org/wiki/Local_optimum) but to explore other areas - higher temperatures favor [exploration](https://en.wikipedia.org/wiki/Exploration), while decreasing temperatures make the algorithm to behave greedier in favoring exploitation of the hopefully global optimum.



### Animation


Simulated annealing - searching for a maximum. [[16]](#cite_note-16)  
With the high temprature, the numerous local maxima are left quickly through the strong noise movement -   
but the global maximum is reliably found because of cooling temperature is no longer sufficient to leave it. 



### Pseudo Code


The [C](C "C") like pseudo code is based on [Peter Mysliwietz'](Peter_Mysliwietz "Peter Mysliwietz") description as given in his Ph.D. thesis [[17]](#cite_note-17). Several neighbor functions used to modify the weight vector were tried, where one randomly chosen element changed randomly performed well. The [fitness function](https://en.wikipedia.org/wiki/Fitness_function) inside the inner loop is of course the most time consuming part. For [Zugzwang](Zugzwang_(Program) "Zugzwang (Program)"), Mysliwietz used a database of 500 [test-positions](Test-Positions "Test-Positions") with a [search depth](Depth "Depth") of one [ply](Ply "Ply"), which took about three minutes on a [T 800 Transputer](Transputer "Transputer") per iteration - the higher the hit rate of found expert moves, the fitter. The whole optimization used a tHight to tLow ratio of 100, a reduction factor r of 0.95, and n=40 inner iterations. 




```

/**
 * simulatedAnnealing
 * @author Peter Mysliwietz, slightly modified
 * @param tHigh is the start temperature
 * @param  tLow is the minimal end temperature
 * @param     r is the temperature reduction factor < 1.0   
 * @param     n number of iterations for each temperature     
 * @return best weight vector
 */
vector simulatedAnnealing(double tHigh, double tLow, double r, int n) {
   vector currentWeights = randomWeights();
   vector bestWeights = currentWeights;
   double fittest = fitness(currentWeights);

   for (double t = tHigh; t > tLow; t *= r) {
      for (int i = 0; i < n; ++i) {
         vector neighborWeights = neighbor(currentWeights);
         if ( fitness(neighborWeights ) > fitness(currentWeights) ) {
            currentWeights = neighborWeights;         
            if ( fitness(neighborWeights ) > fittest ) {
               fittest = fitness(neighborWeights);
               bestWeights = neighborWeights;
            }
         } else if (accept( fitness(currentWeights) - fitness(neighborWeights ), t) ) {
            currentWeights = neighborWeights;
         }
      } /* for i */
   } /* for t */
   return bestWeights;
}

/**
 * accept
 * @param d is the energy difference >= 0
 * @param t is the current temperature
 * @return true with probability of Boltzmann factor e^(-d/kt) 
 */
bool accept(double d, double t ) {
   const double k = 1.38064852e−23; /* joule / kelvin */
   double p = exp(-d / (k*t) ); 
   double r = rand() / (RAND_MAX + 1.0);
   return r < p;
}

```

[[18]](#cite_note-18) [[19]](#cite_note-19)



## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Genetic Programming](Genetic_Programming "Genetic Programming")
* [Iteration](Iteration "Iteration")
* [Learning](Learning "Learning")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [SPSA](SPSA "SPSA")
* [Trial and Error](Trial_and_Error "Trial and Error")


## Selected Publications


[[20]](#cite_note-20)



### 1948 ...


* [Enrico Fermi](Mathematician#EFermi "Mathematician"), [Robert D. Richtmyer](Mathematician#RDRichtmyer "Mathematician") (**1948**). *Note on census-taking in Monte Carlo calculations*. [Los Alamos National Laboratory](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), [pdf](http://scienze-como.uninsubria.it/bressanini/montecarlo-history/fermi-1948.pdf)
* [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis), [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam") (**1949**). *The Monte Carlo Method*. [Journal of the American Statistical Association](https://en.wikipedia.org/wiki/Journal_of_the_American_Statistical_Association), Vol. 44, No. 247, [pdf](http://scienze-como.uninsubria.it/bressanini/montecarlo-history/metropolis-ulam-1949.pdf)


### 1950 ...


* [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis), [Arianna W. Rosenbluth](http://scitation.aip.org/content/contributor/AU0719025), [Marshall N. Rosenbluth](Mathematician#MRosenbluth "Mathematician"), [Augusta H. Teller](https://commons.wikimedia.org/wiki/File:Augusta_H._Teller_Los_Alamos_ID.png), [Edward Teller](Mathematician#ETeller "Mathematician") (**1953**). *[Equation of State Calculations by Fast Computing Machines](https://en.wikipedia.org/wiki/Equation_of_State_Calculations_by_Fast_Computing_Machines)*. [Journal of Chemical Physics](https://en.wikipedia.org/wiki/Journal_of_Chemical_Physics), Vol. 21, No. 6
* [Marshall N. Rosenbluth](Mathematician#MRosenbluth "Mathematician"), [Arianna W. Rosenbluth](http://scitation.aip.org/content/contributor/AU0719025) (**1954**). *Further Results on Monte Carlo Equations of State*. [Journal of Chemical Physics](https://en.wikipedia.org/wiki/Journal_of_Chemical_Physics), Vol. 22, No. 5, [pdf](http://scienze-como.uninsubria.it/bressanini/montecarlo-history/rosenbluth-1954.pdf)


### 1970 ...


* [W. Keith Hastings](Mathematician#WKHastings "Mathematician") (**1970**). *[Monte Carlo Sampling Methods Using Markov Chains and Their Applications](http://biomet.oxfordjournals.org/content/57/1/97)*. [University of Toronto](University_of_Toronto "University of Toronto"), [Biometrika](https://en.wikipedia.org/wiki/Biometrika), Vol. 57, No. 1, [pdf](http://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Basic/Hastings1970.pdf)


### 1980 ...


* [Scott Kirkpatrick](Mathematician#SKirkpatrick "Mathematician"), [C. Daniel Gelatt](Mathematician#CDGelatt "Mathematician"), [Mario P. Vecchi](https://www.linkedin.com/in/mariovecchi) (**1983**). *[Optimization by Simulated Annealing](http://science.sciencemag.org/content/220/4598/671)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 220, No. 4598, [pdf](http://wexler.free.fr/library/files/kirkpatrick%20(1983)%20optimization%20by%20simulated%20annealing.pdf)
* [Vlado Černý](https://sites.google.com/site/cernyv/Home) (**1985**). *[Thermodynamical approach to the traveling salesman problem: An efficient simulation algorithm](http://link.springer.com/article/10.1007%2FBF00940812)*. [Journal of Optimization Theory and Applications](http://www.springer.com/mathematics/journal/10957), Vol. 45, No. 1
* [Saul B. Gelfand](Mathematician#SBGelfand "Mathematician"), [Sanjoy K. Mitter](Mathematician#SKMitter "Mathematician") (**1985**). *Analysis of simulated annealing for optimization*. [24th IEEE Conference on Decision and Control](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4048220)
* [Saul B. Gelfand](Mathematician#SBGelfand "Mathematician") (**1987**). *Analysis of Simulated Annealing Type Algorithms*. Ph.D. thesis, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), advisor: [Sanjoy K. Mitter](Mathematician#.23SKMitter "Mathematician"), [pdf](http://www.mit.edu/~mitter/SKM_theses/87_2_Gelfand_PhD.pdf)
* [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis) (**1987**). *The Beginning of the Monte Carlo Method*. [Los Alamos Science Special](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), [pdf](http://library.lanl.gov/cgi-bin/getfile?00326866.pdf)
* [Rob A. Rutenbar](https://scholar.google.com/citations?user=avq8-1QAAAAJ) (**1989**). *[Simulated Annealing Algorithms](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=avq8-1QAAAAJ&citation_for_view=avq8-1QAAAAJ:u-x6o8ySG0sC)*. [IEEE](IEEE "IEEE") Circuits and Devices Magazine, [pdf](http://www.cs.amherst.edu/~ccm/cs34/papers/rutenbar.pdf)


### 1990 ...


* [Gunter Dueck](Mathematician#GDueck "Mathematician"), [Tobias Scheuer](Mathematician#TScheuer "Mathematician") (**1990**). *[Threshold Accepting: A General Purpose Optimization Algorithm Appearing Superior to Simulated Annealing](http://adsabs.harvard.edu/abs/1990JCoPh..90..161D)*. [Journal of Computational Physics](https://en.wikipedia.org/wiki/Journal_of_Computational_Physics), Vol. 90, No. 1 [[21]](#cite_note-21)
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Klaus-Uwe Koschnick](Klaus-Uwe_Koschnick "Klaus-Uwe Koschnick") (**1991**). *[On the convergence of “Threshold Accepting”](http://link.springer.com/article/10.1007/BF01447741)*. [Applied Mathematics and Optimization](http://link.springer.com/journal/245), Vol. 24, No. 1
* [Andrey Grigoriev](index.php?title=Andrey_Grigoriev&action=edit&redlink=1 "Andrey Grigoriev (page does not exist)") (**1991**). *Artificial Intelligence or Stochastic Relaxation: Simulated Annealing Challenge*. [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
* [Bernd Brügmann](Bernd_Br%C3%BCgmann "Bernd Brügmann") (**1993**). *Monte Carlo Go*. [pdf](http://www.ideanest.com/vegos/MonteCarloGo.pdf)
* [René V. V. Vidal](http://www.imm.dtu.dk/~rvvv/) (ed.) (**1993**). *[Applied Simulated Annealing](http://link.springer.com/book/10.1007%2F978-3-642-46787-5)*. [Lecture Notes in Economics and Mathematical Systems](http://www.springer.com/series/300), Vol. 396, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1994**). *Experience-Based Creativity*. Artificial Intelligence and Creativity: An Interdisciplinary Approach, Kluwer
* [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
* [Olivier C. Martin](https://scholar.google.com/citations?user=-2E52C0AAAAJ&hl=en), [Steve Otto](Steve_Otto "Steve Otto") (**1996**). *[Combining simulated annealing with local search heuristics](https://www.semanticscholar.org/paper/Combining-simulated-annealing-with-local-search-Martin-Otto/379efcc32f7588f276830fca7310da094f2c624d)*. [Annals of Operations Research](https://en.wikipedia.org/wiki/Annals_of_Operations_Research), Vol. 63, No. 1, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [James C. Spall](James_C._Spall "James C. Spall") (**1999**). *Stochastic Optimization: Stochastic Approximation and Simulated Annealing*. in [John G. Webster](https://en.wikipedia.org/wiki/John_G._Webster) (ed.) (**1999**). [Encyclopedia of Electrical and Electronics Engineering](http://onlinelibrary.wiley.com/book/10.1002/047134608X), Vol. 20, [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons), [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Stochastic_Optimization.PDF)


### 2000 ...


* [Ari Shapiro](index.php?title=Ari_Shapiro&action=edit&redlink=1 "Ari Shapiro (page does not exist)"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2002**). *[Learning a Game Strategy Using Pattern-Weights and Self-play](http://www.arishapiro.com/researchportfolio/Learning%20Game%20Strategy/index.htm)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.arishapiro.com//ShapiroA_CG2002.pdf)
* [Eric Triki](Eric_Triki "Eric Triki"), [Yann Collette](https://dblp.uni-trier.de/pers/hd/c/Collette:Yann), [Patrick Siarry](https://dblp.uni-trier.de/pers/hd/s/Siarry:Patrick) (**2002**). *[Empirical study of Simulated Annealing aimed at improved multiobjective optimization](https://www.researchgate.net/publication/265288492_Empirical_study_of_Simulated_Annealing_aimed_at_improved_multiobjective_optimization)*. Research Paper
* [James Gubernatis](http://cnls.lanl.gov/External/people/James_Gubernatis.php) (ed.) (**2003**). *[The Monte Carlo Method in Physical Sciences: Celebrating the 50th Anniversary of the Metropolis Algorithm](http://scitation.aip.org/content/aip/proceeding/aipcp/690)*. [AIP Conference Proceedings](http://scitation.aip.org/content/aip/proceeding/aipcp) [[22]](#cite_note-22)
* [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")
* [James Gubernatis](http://cnls.lanl.gov/External/people/James_Gubernatis.php) (**2005**). *Marshall Rosenbluth and the Metropolis Algorithm*. [Physics of Plasmas](https://en.wikipedia.org/wiki/Physics_of_Plasmas), Vol. 12, No. 5, [pdf](http://www.z-cam.es/historique/Gubernatis_on_Rosenbluth.pdf)
* [Eric Triki](Eric_Triki "Eric Triki"), [Yann Collette](https://dblp.uni-trier.de/pers/hd/c/Collette:Yann), [Patrick Siarry](https://dblp.uni-trier.de/pers/hd/s/Siarry:Patrick) (**2005**). *[A Theoretical Study on the Behavior of Simulated Annealing leading to a new Cooling Schedule](https://www.sciencedirect.com/science/article/abs/pii/S0377221704003388)*. [European Journal of Operational Research](https://en.wikipedia.org/wiki/European_Journal_of_Operational_Research), Vol. 166, No. 1


### 2010 ...


* [Todd W. Neller](Todd_W._Neller "Todd W. Neller"), [Christopher J. La Pilla](https://dblp.uni-trier.de/pers/hd/p/Pilla:Christopher_J=_La) (**2010**). *[Decision-Theoretic Simulated Annealing](https://www.semanticscholar.org/paper/Decision-Theoretic-Simulated-Annealing-Neller-Pilla/a159e8642ccfc9c63ab1190899fca6e403bcbb21)*. [FLAIRS Conference 2010](https://dblp.uni-trier.de/db/conf/flairs/flairs2010.html)
* [Zbigniew J. Czech](http://sun.aei.polsl.pl/~zjc/), [Wojciech Mikanik](http://sun.aei.polsl.pl/pub/wmikanik/index.html), [Rafał Skinderowicz](index.php?title=Rafa%C5%82_Skinderowicz&action=edit&redlink=1 "Rafał Skinderowicz (page does not exist)") (**2010**). *[Implementing a Parallel Simulated Annealing Algorithm](http://link.springer.com/chapter/10.1007%2F978-3-642-14390-8_16?LI=true)*. [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Volume 6067, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Rafał Skinderowicz](index.php?title=Rafa%C5%82_Skinderowicz&action=edit&redlink=1 "Rafał Skinderowicz (page does not exist)") (**2011**). *[Co-operative, Parallel Simulated Annealing for the VRPTW](http://www.researchgate.net/publication/220906163_Co-operative_Parallel_Simulated_Annealing_for_the_VRPTW)*. Computational Collective Intelligence. Technologies and Applications, [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) [[23]](#cite_note-23)
* [Peter Rossmanith](Mathematician#PRossmanith "Mathematician") (**2011**). *Simulated Annealing*. in [Berthold Vöcking](Mathematician#BVoecking "Mathematician") et al. (eds.) (**2011**). *[Algorithms Unplugged](http://www.springer.com/gp/book/9783642153273)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2011**). *[Real-Space Evolutionary Annealing](http://www.cs.utexas.edu/users/ai-lab/?lockett:gecco11)*. [GECCO 2011](https://dblp.uni-trier.de/db/conf/gecco/gecco2011.html)
* [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett") (**2012**). *General-Purpose Optimization Through Information Maximization*. Ph.D. thesis, [University of Texas at Austin](https://en.wikipedia.org/wiki/University_of_Texas_at_Austin), advisor [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen"), [pdf](http://www.alockett.com/static/pdf/lockett-thesis.pdf)
* [Ben Ruijl](index.php?title=Ben_Ruijl&action=edit&redlink=1 "Ben Ruijl (page does not exist)"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2013**). *Combining Simulated Annealing and Monte Carlo Tree Search for Expression Simplification*. [CoRR abs/1312.0841](http://arxiv.org/abs/1312.0841)
* [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2014**). *[Evolutionary Annealing: Global Optimization in Arbitrary Measure Spaces](http://nn.cs.utexas.edu/?lockett:jogo13)*. [Journal of Global Optimization](https://www.springer.com/journal/10898), Vol. 58


## Forum Posts


* [Re: Parameter tuning](http://www.talkchess.com/forum/viewtopic.php?t=38412&start=12) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), March 23, 2011 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Idea for Automatic Calibration of Evaluation Function...](http://www.talkchess.com/forum/viewtopic.php?t=31935) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 22, 2010


## External Links


### Simulated Annealing


* [Simulated annealing from Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing)
* [Adaptive simulated annealing from Wikipedia](https://en.wikipedia.org/wiki/Adaptive_simulated_annealing)
* [Simulated Annealing](http://mathworld.wolfram.com/SimulatedAnnealing.html) from [Wolfram MathWorld](https://en.wikipedia.org/wiki/MathWorld)
* [Algorithmus der Woche - Informatikjahr 2006](http://www-i1.informatik.rwth-aachen.de/~algorithmus/algo41.php) by [Peter Rossmanith](Mathematician#PRossmanith "Mathematician"), [RWTH Aachen](https://en.wikipedia.org/wiki/RWTH_Aachen_University) (German)
* [Simulated Annealing Tutorial](http://apmonitor.com/me575/index.php/Main/SimulatedAnnealing) by [John D. Hedengren](https://scholar.google.com/citations?user=BD6fjEYAAAAJ), [Brigham Young University](https://en.wikipedia.org/wiki/Brigham_Young_University)
* [The Simulated Annealing Algorithm](http://katrinaeg.com/simulated-annealing.html) by [Katrina Ellison Geltman](http://katrinaeg.com/), February 20, 2014


### Related Topics


* [Combinatorial optimization from Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)
* [Cross-entropy method from Wikipedia](https://en.wikipedia.org/wiki/Cross-entropy_method)
* [Expectation–maximization algorithm from Wikipedia](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
* [Gibbs sampling from Wikipedia](https://en.wikipedia.org/wiki/Gibbs_sampling)
* [Global optimization from Wikipedia](https://en.wikipedia.org/wiki/Global_optimization)
* [Greedy algorithm from Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
* [Hill climbing from Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
* [Local search (optimization) from Wikipedia](https://en.wikipedia.org/wiki/Local_search_(optimization))
* [Markov chain Monte Carlo from Wikipedia](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)
* [Monte Carlo method from Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
* [Quantum annealing from Wikipedia](https://en.wikipedia.org/wiki/Quantum_annealing)
* [Simultaneous perturbation stochastic approximation from Wikipedia](https://en.wikipedia.org/wiki/Simultaneous_perturbation_stochastic_approximation)
* [Stochastic gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
* [Stochastic optimization from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_optimization)
* [Tabu search from Wikipedia](https://en.wikipedia.org/wiki/Tabu_search)


### Misc


* [Annealing (metallurgy) from Wikipedia](https://en.wikipedia.org/wiki/Annealing_(metallurgy))
* [Esperanza Spalding](Category:Esperanza_Spalding "Category:Esperanza Spalding") - [Good Lava](http://genius.com/Esperanza-spalding-good-lava-lyrics), [Emily's D+Evolution](https://en.wikipedia.org/wiki/Emily%27s_D%2BEvolution), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. [↑](#cite_ref-1) [train wheel production](https://en.wikipedia.org/wiki/Train_wheel), [Bochumer Verein](https://de.wikipedia.org/wiki/Bochumer_Verein), [Bochum](https://en.wikipedia.org/wiki/Bochum), Germany, [ExtraSchicht](https://de.wikipedia.org/wiki/ExtraSchicht) [2010](http://www.ruhr-guide.de/freizeit/industriekultur/extraschicht-2010/16187,0,0.html), [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail"), [image](https://commons.wikimedia.org/wiki/File:Bochumer_Verein-23-50078.jpg) by [Rainer Halama](https://commons.wikimedia.org/wiki/User:Rainer_Halama), June 19, 2010, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Glühen from Wikipedia.de](https://de.wikipedia.org/wiki/Gl%C3%BChen) (German) 
2. [↑](#cite_ref-2) [Saul B. Gelfand](Mathematician#SBGelfand "Mathematician"), [Sanjoy K. Mitter](Mathematician#SKMitter "Mathematician") (**1985**). *Analysis of simulated annealing for optimization*. [24th IEEE Conference on Decision and Control](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4048220)
3. [↑](#cite_ref-3) [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis), [Arianna W. Rosenbluth](http://scitation.aip.org/content/contributor/AU0719025), [Marshall N. Rosenbluth](Mathematician#MRosenbluth "Mathematician"), [Augusta H. Teller](https://commons.wikimedia.org/wiki/File:Augusta_H._Teller_Los_Alamos_ID.png), [Edward Teller](Mathematician#ETeller "Mathematician") (**1953**). *[Equation of State Calculations by Fast Computing Machines](https://en.wikipedia.org/wiki/Equation_of_State_Calculations_by_Fast_Computing_Machines)*. [Journal of Chemical Physics](https://en.wikipedia.org/wiki/Journal_of_Chemical_Physics), Vol. 21, No. 6
4. [↑](#cite_ref-4) [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis) (**1987**). *The Beginning of the Monte Carlo Method*. [Los Alamos Science Special](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), [pdf](http://library.lanl.gov/cgi-bin/getfile?00326866.pdf)
5. [↑](#cite_ref-5) [W. Keith Hastings](Mathematician#WKHastings "Mathematician") (**1970**). *[Monte Carlo Sampling Methods Using Markov Chains and Their Applications](http://biomet.oxfordjournals.org/content/57/1/97)*. [University of Toronto](University_of_Toronto "University of Toronto"), [Biometrika](https://en.wikipedia.org/wiki/Biometrika), Vol. 57, No. 1, [pdf](http://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Basic/Hastings1970.pdf)
6. [↑](#cite_ref-6) [Metropolis–Hastings algorithm from Wikipedia](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)
7. [↑](#cite_ref-7) [Scott Kirkpatrick](Mathematician#SKirkpatrick "Mathematician"), [C. Daniel Gelatt](Mathematician#CDGelatt "Mathematician"), [Mario P. Vecchi](https://www.linkedin.com/in/mariovecchi) (**1983**). *[Optimization by Simulated Annealing](http://science.sciencemag.org/content/220/4598/671)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 220, No. 4598, [pdf](http://wexler.free.fr/library/files/kirkpatrick%20(1983)%20optimization%20by%20simulated%20annealing.pdf)
8. [↑](#cite_ref-8) [Vlado Černý](https://sites.google.com/site/cernyv/Home) (**1985**). *[Thermodynamical approach to the traveling salesman problem: An efficient simulation algorithm](http://link.springer.com/article/10.1007%2FBF00940812)*. [Journal of Optimization Theory and Applications](http://www.springer.com/mathematics/journal/10957), Vol. 45, No. 1
9. [↑](#cite_ref-9) [The Monte Carlo Method in Physical Sciences: Celebrating the 50th Anniversary of the Metropolis Algorithm](http://cnls.lanl.gov/Conferences/MonteCarloMethods/)
10. [↑](#cite_ref-10) [James Gubernatis](http://cnls.lanl.gov/External/people/James_Gubernatis.php) (ed.) (**2003**). *[The Monte Carlo Method in Physical Sciences: Celebrating the 50th Anniversary of the Metropolis Algorithm](http://scitation.aip.org/content/aip/proceeding/aipcp/690)*. [AIP Conference Proceedings](http://scitation.aip.org/content/aip/proceeding/aipcp)
11. [↑](#cite_ref-11) [James Gubernatis](http://cnls.lanl.gov/External/people/James_Gubernatis.php) (**2005**). *Marshall Rosenbluth and the Metropolis Algorithm*. [Physics of Plasmas](https://en.wikipedia.org/wiki/Physics_of_Plasmas), Vol. 12, No. 5, [pdf](http://www.z-cam.es/historique/Gubernatis_on_Rosenbluth.pdf)
12. [↑](#cite_ref-12) [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
13. [↑](#cite_ref-13) [Robert Levinson](Robert_Levinson "Robert Levinson") (**1994**). *Experience-Based Creativity*. Artificial Intelligence and Creativity: An Interdisciplinary Approach, Kluwer
14. [↑](#cite_ref-14) [Ari Shapiro](index.php?title=Ari_Shapiro&action=edit&redlink=1 "Ari Shapiro (page does not exist)"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2002**). *[Learning a Game Strategy Using Pattern-Weights and Self-play](http://www.arishapiro.com/researchportfolio/Learning%20Game%20Strategy/index.htm)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.arishapiro.com//ShapiroA_CG2002.pdf)
15. [↑](#cite_ref-15) [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**). *Machine Learning in Games: A Survey*. [Austrian Research Institute for Artificial Intelligence](https://en.wikipedia.org/wiki/Austrian_Research_Institute_for_Artificial_Intelligence), OEFAI-TR-2000-3, [pdf](http://www.ofai.at/cgi-bin/get-tr?download=1&paper=oefai-tr-2000-31.pdf)
16. [↑](#cite_ref-16) Start temperature: 25 step: 0.1 End temperature: 0 - 1,000,000 iterations at each temperature: [Animated GIF](https://en.wikipedia.org/wiki/GIF) [Hill Climbing with Simulated Annealing](https://commons.wikimedia.org/wiki/File:Hill_Climbing_with_Simulated_Annealing.gif) by [Kingpin13](https://en.wikipedia.org/wiki/User:Kingpin13?rdfrom=commons:User:Kingpin13), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Simulated annealing from Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing)
17. [↑](#cite_ref-17) [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis, 7.4. Simulated Annealing, 7.4.2. Beschreibung des Algorithmus, Abb. 29, pp. 146 (German)
18. [↑](#cite_ref-18) [Exponential function from Wikipedia](https://en.wikipedia.org/wiki/Exponential_function)
19. [↑](#cite_ref-19) [C mathematical functions - Random number generation from Wikipedia](https://en.wikipedia.org/wiki/C_mathematical_functions#Random_number_generation)
20. [↑](#cite_ref-20) [Monte Carlo History](http://scienze-como.uninsubria.it/bressanini/montecarlo-history/) by [Dario Bressanini](http://scienze-como.uninsubria.it/bressanini/index.html)
21. [↑](#cite_ref-21) [Schwellenakzeptanz from Wikipedia.de](https://de.wikipedia.org/wiki/Schwellenakzeptanz) (German)
22. [↑](#cite_ref-22) [The Monte Carlo Method in Physical Sciences: Celebrating the 50th Anniversary of the Metropolis Algorithm](http://cnls.lanl.gov/Conferences/MonteCarloMethods/)
23. [↑](#cite_ref-23) [Vehicle routing problem from Wikipedia](https://en.wikipedia.org/wiki/Vehicle_routing_problem)

**[Up one Level](Algorithms "Algorithms")**







 
