---
title: Stockfish27s Tuning Method
---
**[Home](Home "Home") \* [Automated Tuning](Automated_Tuning "Automated Tuning") \* Stockfish's Tuning Method**


**Stockfish's Tuning Method** by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), October 2011 <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>



### Step 1. Single variable


Let's assume that we have a single variable x which we want to tune. Current value for x is 100. We assume that this value is quite good (because we already have a strong engine), but not perfect. Next we need to choose delta for x. Delta must be big enough that engine(x = 100 - delta) and engine(x = 100 + delta) has at least a 1-3 ELO point difference. However delta must not to be too big, because then asymmetries start to play a big role. One just need to use his intuition here. Let's choose delta = 20.


Now we match engines engine(80) and engine(120) [self-play]. If engine 120 wins, we tune x slightly upwards. In our tuning sessions We successfully used apply\_factor = 0.002. So in that case new value for x would be. 




```C++
x = 100 + (120 - 100) * 0.002 = 100.04 

```

Next match would be engine(80.004) vs. engine(120.04)


In our tuning session we used 30000-100000 super-fast games, before reading final result.



### Step 2. Varying delta


Instead of fixing delta, we fixed [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of [Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution) and calculated a [random value](Pseudorandom_Number_Generator "Pseudorandom Number Generator") for delta for each iteration. But again one needs to use his intuition to pick a suitable value for standard deviation.



### Step 3. Multiple variables


Doing this for only one variable at a time would be a way too slow. Instead we used to tune 7-35 variables at the same time. As an example let's say that we have three variables: 




```C++
 x = 100
 y = 100 
 z = 100

```

We would then calculate a random delta with sign for each of these variables based on Gaussian distribution. Let's say we get 




```C++
 x_delta = +15
 y_delta = -10
 z_delta = +12

```

We then match engine(x=115, y=90, z=112) vs. engine(x=85, x=110, x=88). If first engine wins and apply\_factor = 0.002 is used,
new values are: 




```C++
 x = 100 + (115 - 100) * 0.002
 y = 100 + ( 90 - 100) * 0.002
 z = 100 + (112 - 100) * 0.002

```

With 30000-100000 super-fast games, we usually got some improvement compared to only by hand tuned values.



## Pros and Cons


What actually happens with multiple variables is that most important variables shall dominate and they shall approach their optimal values, while less important variables take "a random walk". In the beginning this increases strength. But after a while important variables stop approaching optimal values and "random walk" takes over and the strength starts to decrease. So the method doesn't converge and it needs to be stopped at "suitable moment". This is a big problem as well as manual selection of deltas (or standard deviation of delta).


Most other tuning algorithms start "from scratch". Although we know a value which is very close to optimal, they make no use of it. They start matching engine(x=0) vs. pool of other engines and engine(x=200) vs. pool of other engines. And it takes tens of thousands or hundreds of thousands iteration before they can even reach the current level (x=100) and only after that we can get some improvement. Instead method described in here starts from that "very good" value and attempts to improve it slightly.



## Variable Selection


Variable selection is extremely important. for example if you tune each piece-square table value separately, you are doomed the fail, because changing only one value is going to change the strength of the program only very little. So in tuning we end up doing only random walk and the strength of the program only goes slightly downhill.


But instead using ampli-bias knobs for tables proved to be very successful approach for us. Each value for the table is adjusted using these two knobs like (Here we optimize variables var\_bias and var\_amplitude): 




```C++
 new_value = orig_value + var_bias + orig_value * var_amplitude / 100

```

Each chess engine is full of different kind of tables and if we can give even "a slight push" for each of these tables, it'll result in considerable increase in the end.



## See also


* [CLOP](CLOP "CLOP")
* [SPSA](SPSA "SPSA")


## Publications


* [James C. Spall](James_C._Spall "James C. Spall") (**1998**). *[Implementation of the Simultaneous Perturbation Algorithm for Stochastic Optimization](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=705889&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D705889)*. [IEEE Transactions on Aerospace and Electronic Systems](IEEE#TOCAES "IEEE"), [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Implementation_of_the_Simultaneous.PDF) <a id="cite-note-3" href="#cite-ref-3">[3]</a>


## Forum Posts


* [Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=40662) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), October 07, 2011


 [Re: Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?start=0&t=40662&start=6) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), October 07, 2011
* [Re: Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545&start=2) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 06, 2014 <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>


## External Links


* [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
* [SPSA Algorithm](http://www.jhuapl.edu/spsa/)
* [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/) » [Evaluation](Evaluation "Evaluation")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Following text is released under [public domain](https://en.wikipedia.org/wiki/Public_domain) and can be freely distributed
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=40662) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), October 07, 2011
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a>  [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [NOMAD - A blackbox optimization software](https://www.gerad.ca/nomad/Project/Home.html)

**[Up one Level](Automated_Tuning "Automated Tuning")**







 
