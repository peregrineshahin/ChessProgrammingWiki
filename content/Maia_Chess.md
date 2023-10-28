---
title: Maia Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Maia Chess**



[ Hermes and Maia <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Maia Chess**, (Maia, Maiachess)  

a chess engine featuring [deep learning](Deep_Learning "Deep Learning") - as elaborated by their authors [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), and [Ashton Anderson](Ashton_Anderson "Ashton Anderson") in their research paper presented at the 26th [ACM SIGKDD](ACM#SIGKDD "ACM") virtual conference in 2020 - with the aim to align [superhuman](https://en.wikipedia.org/wiki/Superhuman) [AI](Artificial_Intelligence "Artificial Intelligence") with [human behaviour](https://en.wikipedia.org/wiki/Human_behavior) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Russell Wang](Russell_Wang "Russell Wang") further joining the team.
Like [AlphaZero](AlphaZero "AlphaZero") and [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero"), Maia Chess uses a [deep](Neural_Networks#Deep "Neural Networks") [convolutional neural network](Neural_Networks#Convolutional "Neural Networks") (CNN) to predict moves.
In contrast to the **Zero** training approaches of their inspirer, using [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") - Maia models are entirely trained by [supervised learning](Supervised_Learning "Supervised Learning"), 
feeding in games of human players separated by 9 [rating levels](Playing_Strength "Playing Strength") between 1100 and 1900 Elo. Further, Maia Chess only predicts moves by probing the net without any [search](Search "Search").
Maia chess is [open source](Category:Open_Source "Category:Open Source") released under the terms under the [GPL version 3](Free_Software_Foundation#GPL "Free Software Foundation"), 
and consists of [Python](Python "Python") code relying on the [scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn) library, along with various [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) scripts.
To play chess, Maia requires its models used in [Lc0](Leela_Chess_Zero "Leela Chess Zero") <a id="cite-note-3" href="#cite-ref-3">[3]</a> similar to any other Leela weights file - in [UCI](UCI "UCI") mode, 
*nodes\_1* needs to disable any [search](Search "Search") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Contents


* [1 Model](#model)
* [2 Dedicated Maia](#dedicated-maia)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc)
* [7 References](#references)






[Boards were represented](Board_Representation "Board Representation") as a 8×8×17 dimensional [array](Array "Array") with the 12 channels [encoding pieces](Pieces#PieceTypeCoding "Pieces"), 4 channels encoding [castling rights](Castling_Rights "Castling Rights"), and one encoding whether the [active player](Side_to_move "Side to move") is white.
The [residual](Neural_Networks#Residual "Neural Networks") [CNN](Neural_Networks#Convolutional "Neural Networks") has 6 residual blocks with two set of 2D CNNs with 64 channels and a 3×3 kernel <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



## Dedicated Maia


Maia Chess is incorporated inside [modules](Module "Module") of the [Certabo Chessboard](Certabo_Chessboard "Certabo Chessboard") as chess playing engine, [Certabo DaVinci](Certabo_Chessboard#Maia_Chess "Certabo Chessboard") <a id="cite-note-6" href="#cite-ref-6">[6]</a> and [Certabo Nano](Certabo_Chessboard#Maia_Chess "Certabo Chessboard") <a id="cite-note-7" href="#cite-ref-7">[7]</a>.


  




## See also


* [AlphaZero](AlphaZero "AlphaZero")
* [A0lite](A0lite "A0lite")
* [Bad Gyal](index.php?title=Bad_Gyal&action=edit&redlink=1 "Bad Gyal (page does not exist)")
* [Certarbo Modules](Certabo_Chessboard#Maia_Chess "Certabo Chessboard")
* [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")


## Publications


* [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Aligning Superhuman AI with Human Behavior: Chess as a Model System*. In Proceedings of the 26th [ACM SIGKDD 2020](ACM#SIGKDD "ACM"), [arXiv:2006.01855](https://arxiv.org/abs/2006.01855)
* [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Russell Wang](Russell_Wang "Russell Wang"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Learning Personalized Models of Human Behavior in Chess*. [arXiv:2008.10086](https://arxiv.org/abs/2008.10086)
* [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) <a id="cite-note-8" href="#cite-ref-8">[8]</a>


## Forum Posts


* [Maiachess](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75985) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), December 04, 2020
* [Maia chess - the holy grail for computer chess?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76002) by PeterO, [CCC](CCC "CCC"), December 06, 2020
* [Re: Chess for Android and Electronic ChessBoards](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69257&start=23) by PeterO, [CCC](CCC "CCC"), December 06, 2020 » [Chess for Android](Chess_for_Android "Chess for Android")


## External Links


### Chess Engine


* [Maia Chess](https://maiachess.com/)
* [GitHub - CSSLab/maia-chess: Human like chess engines](https://github.com/CSSLab/maia-chess)
* [Maia Prediction Visualizer](https://csslab.github.io/Maia-Agreement-Visualizer/)
* [The human side of AI for chess - Microsoft Research](https://www.microsoft.com/en-us/research/blog/the-human-side-of-ai-for-chess/), November 30, 2020


### Misc


* [Maia from Wikipedia](https://en.wikipedia.org/wiki/Maia)
* [Maia (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Maia_(disambiguation))
* [Maia (nurse) from Wikipedia](https://en.wikipedia.org/wiki/Maia_(nurse))
* [Maia (star) from Wikipedia](https://en.wikipedia.org/wiki/Maia_(star))
* [Maia (given name) from Wikipedia](https://en.wikipedia.org/wiki/Maia_(given_name))
* [Maia Chiburdanidze from Wikipedia](https://en.wikipedia.org/wiki/Maia_Chiburdanidze)
* [Maia Lomineishvili from Wikipedia](https://en.wikipedia.org/wiki/Maia_Lomineishvili)
* [Arthur Maia](Category:Arthur_Maia "Category:Arthur Maia") - [Grooveland](https://pt.wikipedia.org/wiki/Paulinho_Braga#Discografia), [Ao Vivo](https://www.facebook.com/events/theatro-municipal-de-niter%C3%B3i/arthur-maia-ao-vivo-lan%C3%A7amento-do-dvd/2563374087023343/) 2015 at the [UFF Arts Center Theater](http://www.visit.niteroi.br/en/teatro-da-uff/), [Niterói](https://en.wikipedia.org/wiki/Niter%C3%B3i), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Ticão Freitas](https://www.facebook.com/Tic%C3%A3o-Freitas-230174837178995/), [Luiz Otavio](https://www.facebook.com/LuizOtavioPianista/), [Felipe Martins](https://pearldrumbrasil.com.br/felipe-martins/), [Marcelo Martins](https://www.rsberkeley.com/marcello-martins-1), [Enio Taquari](https://www.instagram.com/eniotaquari/?hl=en)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> God council in [Olympus](https://en.wikipedia.org/wiki/Mount_Olympus): [Hermes](https://en.wikipedia.org/wiki/Hermes) with his mother [Maia](https://en.wikipedia.org/wiki/Maia). Detail of the side B of an [Attic](https://en.wikipedia.org/wiki/Attica) [red-figure](https://en.wikipedia.org/wiki/Red-figure_pottery) [belly-amphora](https://en.wikipedia.org/wiki/Amphora) by [Nikoxenos Painter](https://en.wikipedia.org/wiki/Nikoxenos_Painter), ca. 500 BC, [Staatliche Antikensammlungen](https://en.wikipedia.org/wiki/Staatliche_Antikensammlungen), 
 [image](https://commons.wikimedia.org/wiki/File:Hermes_Maia_Staatliche_Antikensammlungen_2304.jpg) by [Bibi Saint-Pol](https://commons.wikimedia.org/wiki/User:Bibi_Saint-Pol), February 10, 2007, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Aligning Superhuman AI with Human Behavior: Chess as a Model System*. In Proceedings of the 26th [ACM SIGKDD 2020](ACM#SIGKDD "ACM"), [arXiv:2006.01855](https://arxiv.org/abs/2006.01855)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GitHub - CSSLab/lc0\_23](https://github.com/CSSLab/lc0_23)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [maia-chess/README.md at master · CSSLab/maia-chess · GitHub](https://github.com/CSSLab/maia-chess/blob/master/README.md)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Aligning Superhuman AI with Human Behavior: Chess as a Model System*. [arXiv:2006.01855](https://arxiv.org/abs/2006.01855). 7 Supplement
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [DaVinci Extreme Chess Computer 1,5 GHz QuadCore processor – 2 Gb ram BLACK - Certabo Chess](https://www.certabo.com/prodotto/davinci-extreme-chess-computer-15-ghz-quadcore-processor-2-gb-ram-black/)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [CERTABO NANO E-Paper - Certabo Chess](https://www.certabo.com/prodotto/certabo-nano-e-paper/)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021

**[Up one level](Engines "Engines")**







 
