---
title: Ari Weinstein
---
**[Home](Home "Home") * [People](People "People") * Ari Weinstein**

**Ari Weinstein**,

an American computer scientist at [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"). He holds a Ph.D. from [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University) under advisor [Michael L. Littman](Michael_L._Littman "Michael L. Littman") on *Local Planning For Continuous Markov Decision Processes*, covering algorithms that create plans to maximize a numeric reward over time. While a general formulation of this problem in terms of
[reinforcement learning](Reinforcement_Learning "Reinforcement Learning") has traditionally been restricted to small discrete domains, Weinstein thesis include both continuous and high dimensional domains, with simulations of swimming, riding a bicycle, and walking as concrete examples.

## Contents

- [1 FSSS-Minimax](#fsss-minimax)
- [2 Selected Publications](#selected-publications)
- [3 External Links](#external-links)
- [4 References](#references)

## FSSS-Minimax

In their paper *Rollout-based Game-tree Search Outprunes Traditional Alpha-beta*, along with [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)") and his advisor Michael Littman <a id="cite-note-1" href="#cite-ref-1">[1]</a>, Weinstein introduce the rollout-based *FSSS* (Forward-search sparse sampling) <a id="cite-note-2" href="#cite-ref-2">[2]</a> applied to game-tree [search](Search "Search"), outpruning [alpha-beta](Alpha-Beta "Alpha-Beta") both empirically and formally. FSSS-Minimax only visits parts of the tree that alpha-beta visits, and is in terms of related work similar to the *Score Bounded* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") introduced by [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") and [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```C++
Recently, rollout-based planning and search methods have emerged as an alternative to traditional tree-search methods. The fundamental operation in rollout-based tree search is the generation of trajectories in the search tree from root to leaf. Game-playing programs based on Monte-Carlo rollouts methods such as “[UCT](UCT "UCT")” have proven remarkably effective at using information from trajectories to make state-of-the-art decisions at the root. In this paper, we show that trajectories can be used to prune more aggressively than classical alpha-beta search. We modify a rollout-based method, FSSS, to allow for use in game-tree search and show it outprunes alpha-beta both empirically and formally.

```

While FSSS-Minimax is guaranteed to never expand more leaves than alpha-beta, the [best-first](Best-First "Best-First") approach comes at a cost in terms of memory requirements as well as computational cost.

## Selected Publications

<a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>

- Ari Weinstein, [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2012**). *[Bandit-Based Planning and Learning in Continuous-Action Markov Decision Processes](https://www.aaai.org/ocs/index.php/ICAPS/ICAPS12/paper/view/4697)*. [ICAPS 2012](http://dblp.uni-trier.de/db/conf/aips/icaps2012.html)
- Ari Weinstein, [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)") (**2013**). *[Rollout-based Game-tree Search Outprunes Traditional Alpha-beta](http://proceedings.mlr.press/v24/weinstein12a.html)*. [PMLR](http://proceedings.mlr.press/), Vol. 24 » [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [UCT](UCT "UCT")
- [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)"), Ari Weinstein, [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2013**). *The Cross-Entropy Method Optimizes for Quantiles*. [ICML 2013](http://dblp.uni-trier.de/db/conf/icml/icml2013.html)
- Ari Weinstein, [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2013**). *Open-Loop Planning in Large-Scale Stochastic Domains*. [AAAI-2013](Conferences#AAAI-2013 "Conferences")
- Ari Weinstein (**2013**). *Local Planning For Continuous Markov Decision Processes*. Ph.D. thesis, [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University), advisor [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [pdf](http://cs.brown.edu/~mlittman/theses/weinstein.pdf)
- Ari Weinstein, [Matthew Botvinick](index.php?title=Matthew_Botvinick&action=edit&redlink=1 "Matthew Botvinick (page does not exist)") (**2017**). *Structure Learning in Motor Control: A Deep Reinforcement Learning Model*. [arXiv:1706.06827](https://arxiv.org/abs/1706.06827)

## External Links

- [Ari Weinstein - Google Scholar Citations](https://scholar.google.com/citations?user=MnUboHYAAAAJ&hl=en)
- [Ari Weinstein - The Mathematics Genealogy Project](https://genealogy.math.ndsu.nodak.edu/id.php?id=186285)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Ari Weinstein, [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)") (**2013**). *[Rollout-based Game-tree Search Outprunes Traditional Alpha-beta](http://proceedings.mlr.press/v24/weinstein12a.html)*. [PMLR](http://proceedings.mlr.press/), Vol. 24
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Thomas J. Walsh](index.php?title=Thomas_J._Walsh&action=edit&redlink=1 "Thomas J. Walsh (page does not exist)"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2010**). *Integrating sample-based planning and model-based reinforcement learning.* [AAAI-2010](Conferences#AAAI-2010 "Conferences"), [pdf](https://pdfs.semanticscholar.org/bdc9/bfb6ecc6fb5afb684df03d7220c46ebdbf4e.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine") (**2010**). *Score Bounded Monte-Carlo Tree Search*. [CG 2010](CG_2010 "CG 2010"), [pdf](http://www.lamsade.dauphine.fr/%7Ecazenave/papers/mcsolver.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [dblp: Ari Weinstein](http://dblp.uni-trier.de/pers/hd/w/Weinstein:Ari)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Doctoral Dissertations Advised by Michael Littman](http://cs.brown.edu/~mlittman/theses/)

**[Up one Level](People "People")**

