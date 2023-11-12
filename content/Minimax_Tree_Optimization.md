---
title: Minimax Tree Optimization
---
**[Home](Home "Home") \* [Automated Tuning](Automated_Tuning "Automated Tuning") \* Minimax Tree Optimization**



[ [Bonanza](https://en.wikipedia.org/wiki/Bonanza) full cast, 1962 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Minimax Tree Optimization** (MMTO),  

a [supervised](Supervised_Learning "Supervised Learning") [tuning method](Automated_Tuning "Automated Tuning") based on [move adaptation](Automated_Tuning#MoveAdaption "Automated Tuning"),
devised and introduced by [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") and [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
A MMTO predecessor, the initial **Bonanza-Method** was used in Hoki's [Shogi](Shogi "Shogi") engine [Bonanza](Bonanza "Bonanza") in 2006, winning the [WCSC16](index.php?title=WCSC16&action=edit&redlink=1 "WCSC16 (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The further improved MMTO version of Bonanaza won the [WCSC23](index.php?title=WCSC23&action=edit&redlink=1 "WCSC23 (page does not exist)") in 2013 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## MMTO


MMTO improved by performing a [minimax search](Minimax "Minimax") (One or two [ply](Ply "Ply") plus [quiescence](Quiescence_Search "Quiescence Search")), by grid-adjacent update, and using [equality constraint](https://en.wikipedia.org/wiki/Constraint_(mathematics)) and [L1 regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) to achieve [scalability](https://en.wikipedia.org/wiki/Scalability) and [stability](https://en.wikipedia.org/wiki/Stability).



### Objective Function


MMTO's [objective function](https://en.wikipedia.org/wiki/Loss_function) consists of the sum of three terms, where the first term **J(P,ω)** on the right side is the main part.



 [](File:MmtoObjectiveFunction2.jpg) 
The other terms **JC** and **JR** are constraint and regularization terms.
**JC(P,ω) = λ0g(ω')**, where **ω'** is subset of **ω**, **g(ω')=0** is an [equality constraint](https://en.wikipedia.org/wiki/Constraint_(mathematics)), and **λ0** is a [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier).
**JR(P,ω) = λ1|ω''|** is the [L1 regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)).
where **λ1** is a constant > 0 and **ω''** is subset of **ω**. The main part of objective function is similar to the H-formula of the Move Adaptation chapter:



 [](File:MmtoObjectiveFunction3.jpg) 
where **s(p,ω)** is the value identified by the [minimax](Minimax "Minimax") search for position **p**. **T(x) = 1/(1 + exp(ax))**, 
a [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) with slope controlled by **a**, to even become the [Heaviside step function](https://en.wikipedia.org/wiki/Heaviside_step_function). 



### Optimization


The iterative optimization process has three steps:



1. Perform a [minimax](Minimax "Minimax") [search](Search "Search") to identify [PV](Principal_Variation "Principal Variation") [leaves](Leaf_Node "Leaf Node") **πω(t)p.m** for all child positions **p.m** of position **p** in training set **P**, where **ω(t)** is the weight vector at the t-th iteration and **ω(0)** is the initial guess
2. Calculate a partial-derivative approximation of the objective function using both **πω(t)p.m** and **ω(t)**. The objective function employs a differentiable approximation of **T(x)**, as well as a constraint and regularization term
3. Obtain a new weight vector **ω(t+1)** from **ω(t)** by using a grid-adjacent update guided by the partial derivatives computed in step 2. Go back to step 1, or terminate the optimization when the objective function value converges


Because step 1 is the most time-consuming part, it is worth considering omitting it by assuming the PV does not change between iterations. 
In their experiments, Hoki and Kaneko used steps 2 and 3 32 times without running step 1.



### Grid-Adjacent Update


MMTO uses grid-adjacent update to get **ω(t+1)** from **ω(t)** using a small integer **h** along with the [sgn function](https://en.wikipedia.org/wiki/Sign_function) of the partial derivative approximation.



 [](File:MmtoGridAdjacentUpdate.jpg) 
### Partial Derivative Approximation


In each iteration, feature weights are updated on the basis of the [partial derivatives](https://en.wikipedia.org/wiki/Partial_derivative) of the objective function. 



 [](File:MmtoPartialDifferentation1.jpg) 
The **JR** derivative is treated in an intuitive manner [sgn](https://en.wikipedia.org/wiki/Sign_function)**(ωi)λ1** for **ωi ∈ ω''**, and **0** otherwise.


The partial derivative of the [constraint](https://en.wikipedia.org/wiki/Constraint_(mathematics)) term **JC** is 0 for **ωi ∉ ω'** .
Otherwise, the [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier) **λ0** is set to the [median](https://en.wikipedia.org/wiki/M-estimator#Median) of the partial derivatives in order to maintain the constraint **g(ω) = 0** in each iteration. As a result, **∆ω′i** is **h** for **n** feature weights, **−h** for **n** feature weights, and 0 in one feature weight, where the number of feature weights in ω' is 2n + 1.


Since the objective function with the minimax values **s(p, ω)** is not always [differentiable](https://en.wikipedia.org/wiki/Differentiable_function),
an approximation is used by using the evaluation of the [PV](Principal_Variation "Principal Variation") [leaf](Leaf_Node "Leaf Node"):



 [](File:MmtoPartialDifferentation.jpg) 
where **T'(x) = d/dx T(x)**.



## See also


* [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought")
* [NNUE](NNUE "NNUE")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## Publications


* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2006**). *Optimal control of minimax search result to learn positional evaluation*. [11th Game Programming Workshop](Conferences#GPW "Conferences") (Japanese)
* [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2011**). *Analysis of Evaluation-Function Learning by Comparison of Sibling Nodes*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2011**). *The Global Landscape of Objective Functions for the Optimization of Shogi Piece Values with a Game-Tree Search*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf)
* [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito"), [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2015**). *[Contemporary Computer Shogi](https://link.springer.com/referenceworkentry/10.1007/978-3-319-08234-9_22-1)*. [Encyclopedia of Computer Graphics and Games](https://link.springer.com/referencework/10.1007/978-3-319-08234-9)


## Forum Posts


* [MMTO for evaluation learning](http://www.talkchess.com/forum/viewtopic.php?t=55084) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 25, 2015
* [Re: Texel tuning method question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64189&start=21) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 07, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Photo](https://commons.wikimedia.org/wiki/File:Bonanza_full_cast_1962_larger.jpg) of the full cast of the television program [Bonanza](https://en.wikipedia.org/wiki/Bonanza) on the porch of the [Ponderosa](https://en.wikipedia.org/wiki/Ponderosa_Ranch) from 1962. 
From top: [Lorne Greene](https://en.wikipedia.org/wiki/Lorne_Greene), [Dan Blocker](https://en.wikipedia.org/wiki/Dan_Blocker), [Michael Landon](https://en.wikipedia.org/wiki/Michael_Landon), [Pernell Roberts](https://en.wikipedia.org/wiki/Pernell_Roberts). This episode, "Miracle Maker", aired in [May 1962](http://en.wikipedia.org/wiki/List_of_Bonanza_episodes), 
Author: Pat MacDermott Company, Directional Public Relations, for [Chevrolet](https://en.wikipedia.org/wiki/Chevrolet), the sponsor of the program. During the 1950s and 1960s, publicity information was often distributed through ad or public relations agencies by the network, studio, or program's sponsor. 
In this case, the PR agency was making this available for Chevrolet--the little "plug" about their vehicles is seen in the release. [Category:Bonanza (TV series) - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Bonanza_(TV_series))
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2006**). *Optimal control of minimax search result to learn positional evaluation*. [11th Game Programming Workshop](Conferences#GPW "Conferences") (Japanese)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito"), [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2015**). *[Contemporary Computer Shogi](https://link.springer.com/referenceworkentry/10.1007/978-3-319-08234-9_22-1)*. [Encyclopedia of Computer Graphics and Games](https://link.springer.com/referencework/10.1007/978-3-319-08234-9)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Description and Formulas based on [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf)

**[Up one Level](Automated_Tuning "Automated Tuning")**







 
