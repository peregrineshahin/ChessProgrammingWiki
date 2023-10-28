---
title: RuyTune
---
**[Home](Home "Home") \* [Automated Tuning](Automated_Tuning "Automated Tuning") \* RuyTune**



 [](http://www.wolframalpha.com/input/?i=tanh(0.43s)+,+s%3D-10+to+10) RuyTune's [hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function) based Sigmoid <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**RuyTune**,  

an open source framework for tuning [evaluation function](Evaluation "Evaluation") parameters, written by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") in [C++](Cpp "Cpp"), released on [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket) <a id="cite-note-2" href="#cite-ref-2">[2]</a> as introduced in November 2016 <a id="cite-note-3" href="#cite-ref-3">[3]</a>. RuyTune applies [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") using a [limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS), a [quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method) that approximates the [Broyden–Fletcher–Goldfarb–Shanno](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm) algorithm with limited amount of [memory](Memory "Memory"). It uses the *libLBFGS* library <a id="cite-note-4" href="#cite-ref-4">[4]</a> along with [reverse-mode automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation#Reverse_accumulation) and requires that the evaluation function is converted to a [C++ template function](https://en.wikipedia.org/wiki/Template_(C%2B%2B)#Function_templates) where the score type is a template parameter, and a database of quiescent positions with associated results <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### Contents


* [1 Method](#method)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






The function to minimize the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) of the prediction is:



 [](File:TexelTuneMathE.jpg) 
where:



* N is the number of test positions.
* Ri is the result of the game corresponding to position i; **-1** for black win, **0** for draw and **+1** for white win.
* qi is corresponding to position i, the [value](Score "Score") returned by the chess engine evaluation function. (Computing the gradient on the [QS](Quiescence_Search "Quiescence Search") is a waste of time - it is much faster to run the QS saving the [PV](Principal_Variation "Principal Variation") and then compute the gradient using the evaluation function of the end-of-PV position - and not worry too much about the fact that tweaking the evaluation function could result in a different position being picked <a id="cite-note-6" href="#cite-ref-6">[6]</a>).
* [Sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) is implemented by [hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function) to convert [centipawn scores](Centipawns "Centipawns") into an expected result in [-1,1].



```
Sigmoid(s) = tanh(0.0043s)

```

## See also


* [Arasan's Tuning](Arasan#Tuning "Arasan")
* [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought")
* [RuyDos](RuyDos "RuyDos")
* [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## Forum Posts


* [A database for learning evaluation functions](http://www.talkchess.com/forum/viewtopic.php?t=61861) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 28, 2016
* [C++ code for tuning evaluation function parameters](http://www.talkchess.com/forum/viewtopic.php?t=62056) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 10, 2016
* [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=35) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), June 07, 2017


 [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=36) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 07, 2017 
## External Links


* [alonamaloh / ruy\_tune — Bitbucket](https://web.archive.org/web/20180820050927/https://bitbucket.org/alonamaloh/ruy_tune) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [tanh(0.43s) , s=-10 to 10](http://www.wolframalpha.com/input/?i=tanh(0.43s)+,+s%3D-10+to+10) pawnunit plot by [Wolfram Alpha](https://en.wikipedia.org/wiki/Wolfram_Alpha)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [alonamaloh / ruy\_tune — Bitbucket](https://web.archive.org/web/20180820050927/https://bitbucket.org/alonamaloh/ruy_tune) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [C++ code for tuning evaluation function parameters](http://www.talkchess.com/forum/viewtopic.php?t=62056) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 10, 2016
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [libLBFGS: L-BFGS library written in C](http://www.chokkan.org/software/liblbfgs/)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [A database for learning evaluation functions](http://www.talkchess.com/forum/viewtopic.php?t=61861) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 28, 2016
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=36) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 07, 2017

**[Up one Level](Automated_Tuning "Automated Tuning")**







 
