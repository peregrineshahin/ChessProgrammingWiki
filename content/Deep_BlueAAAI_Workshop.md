---
title: Deep BlueAAAI Workshop
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Deep Blue**

\[ Deep Blue <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Deep Blue**,

the [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") sponsored successor of the chess entity [Deep Thought](Deep_Thought "Deep Thought"). The project initially started in 1985 as [ChipTest](ChipTest "ChipTest") at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") by the computer science doctoral students [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") and [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"). [Murray Campbell](Murray_Campbell "Murray Campbell"), former co-developer of [HiTech](HiTech "HiTech"), joined the ChipTest team a few months later.
The program was named *Deep Thought* after the fictional computer of the same name from [The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy). Hsu and Campbell joined IBM in 1989, Deep Blue was developed out of this. The name is a play on Deep Thought and [Big Blue](https://en.wikipedia.org/wiki/Big_Blue), IBM's nickname.
The declared target was to become the strongest chess entity ever and to beat the human world champion, which eventually happened in [1997 versus](Kasparov_versus_Deep_Blue_1997 "Kasparov versus Deep Blue 1997") [Garry Kasparov](Garry_Kasparov "Garry Kasparov"),
winning the $100,000 [Fredkin prize](Edward_Fredkin#Prize "Edward Fredkin"), awarded at the [AAAI Conference](Conferences#AAAI-97 "Conferences") in [Providence, Rhode Island](https://en.wikipedia.org/wiki/Providence,_Rhode_Island).

## Description

## [](http://www.computerhistory.org/chess/full_record.php?iid=art-431614f45291e) Deep blue chip <a id="cite-note-2" href="#cite-ref-2">[2]</a> 1995

Description given in 1995 from the [ICGA](ICGA "ICGA") site <a id="cite-note-3" href="#cite-ref-3">[3]</a> :

```C++Deep Blue Prototype consists of an IBM [RS/6000](index.php?title=RS/6000&action=edit&redlink=1 "RS/6000 (page does not exist)") workstation with 14 chess search engines as slave processors. Each processor contains a VLSI chip for [move generation](Move_Generation "Move Generation"), as well as additional hardware for [search](Search "Search") and [evaluation](Evaluation "Evaluation"). Each [Deep Thought 2](Deep_Thought "Deep Thought") processor searches about 500,000 [positions per second](Nodes_per_Second "Nodes per Second") standalone, or about 400,000 positions per second as a slave processor. (This is about 1/10th of the projected speed of the Deep Blue single-processor currently in fabrication.) The 14-processor Deep Thought 2 typically searches between 3 and 5 million positions per second. When conducting a search, the search tree near the root position is processed on the host workstation, and includes [selective](Selectivity "Selectivity") search [extension](Extensions "Extensions") algorithms such as [singular extensions](Singular_Extensions "Singular Extensions"). The deepest nodes in the search tree are handled by the slave search engines which usually do 4-ply [alpha-beta](Alpha-Beta "Alpha-Beta") searches. 

```

## 1997

The 1997 Deep Blue system was based on an IBM [RS/6000 SP](index.php?title=RS/6000&action=edit&redlink=1 "RS/6000 (page does not exist)") supercomputer, using 30 workstation nodes of [PowerPC](PowerPC "PowerPC") processors controlling 16 chess chips each, distributed over two [Micro Channel](https://en.wikipedia.org/wiki/Micro_Channel_architecture) boards.
A chess chip features of a full-fledged chess machine on its own, along with [move generator](Move_Generation "Move Generation"), a smart move stack, hardware [evaluation function](Evaluation_Function "Evaluation Function"), and
an [alpha-beta](Alpha-Beta "Alpha-Beta") hardware search controller. The [search](Search "Search") occurs in [parallel](Parallel_Search "Parallel Search") on two levels, one distributed over the IBM RS/6000 SP switching network and the other over the Micro Channel bus inside a workstation node.
A master workstation node first starts the software search exclusively, to distribute work to all 30 workstation nodes only at a certain [depth](Depth "Depth") (i.e. 4 [plies](Ply "Ply")). After generation an appropriate number of childs and grandchilds etc., the software search per node utilize the 16 chess chips to search the final four plies plus [quiescence search](Quiescence_Search "Quiescence Search") in hardware. Since each chess chip could search 2 to 2.5 million [nodes per second](Nodes_per_Second "Nodes per Second"), the system speed reached about one billion nps (480 chips). During the 1997 match, the software search extended the search to about 40 plies along the forcing lines, even though the nonextended search reached only about 12 plies <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Tournaments & Matches

## WCCC 1995

**Deep Blue Prototype** missed the expected win at the [WCCC 1995](WCCC_1995 "WCCC 1995") by losing the [decisive match](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=5&id=4) in round 5 against [Fritz](Fritz "Fritz") after king castling into Fritz's half open g-file.

## Kasparov versus Deep Blue

*Main article*: [Kasparov versus Deep Blue 1996](Kasparov_versus_Deep_Blue_1996 "Kasparov versus Deep Blue 1996")

Deep Blue was the first machine to win a chess game against a reigning world champion [Garry Kasparov](Garry_Kasparov "Garry Kasparov") under regular time controls. This first win occurred on February 10, 1996, Game 1. However, Kasparov won three games and drew two of the following games, beating Deep Blue by a score of 4–2.

## The Rematch

*Main article*: [Kasparov versus Deep Blue 1997](Kasparov_versus_Deep_Blue_1997 "Kasparov versus Deep Blue 1997")

In 1997 Deep Blue won the rematch against Kasparov. He did not recover after the shock by Deep Blues' play in [game 2](Kasparov_versus_Deep_Blue_1997#Games "Kasparov versus Deep Blue 1997"). Kasparov resigned a possibly drawn position, since he missed a deep tricky perpetual check, while he wrongly was confident the machine would not have blundered to allow him to draw. In the final decisive [game 6](Kasparov_versus_Deep_Blue_1997#Games "Kasparov versus Deep Blue 1997") Kasparov was rather indisposed and blundered in the early opening.

## The Deep Blue Team

- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") - The man who started the Deep Blue project while still in college
- [Murray Campbell](Murray_Campbell "Murray Campbell") - A former chess champion who works with Deep Blue's evaluation function
- [A. Joseph Hoane](Joe_Hoane "Joe Hoane") - Deep Blue's software engineer
- C. J. Tan - Senior manager of the Deep Blue development team
- [Jerry Brody](index.php?title=Jerry_Brody&action=edit&redlink=1 "Jerry Brody (page does not exist)") - The project's support engineer
- [Joel Benjamin](https://en.wikipedia.org/wiki/Joel_Benjamin) - development team chess consultant, opening book author

## Photos

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f67157b)
Deep Blue's core team, [Joe Hoane](Joe_Hoane "Joe Hoane"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), and [Murray Campbell](Murray_Campbell "Murray Campbell") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## See also

- [Computer Chess - A Movie](History#ComputerChess "History")
- [The Machine](Kasparov_versus_Deep_Blue_1997#TheMachine "Kasparov versus Deep Blue 1997")

## Selected Publications

## 1995 ...

- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Joe Hoane](Joe_Hoane "Joe Hoane") (**1995**). *[Deep Blue System Overview](http://www.computerhistory.org/chess/doc-431614f6de120/)*. International Conference on Supercomputing

## 1996

- [Paul Hsieh](Paul_Hsieh "Paul Hsieh") (**1996**). *Deep Blue - Deep Thought 2*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol 5, No 3+4, pp. 45
- [Tony Marsland](Tony_Marsland "Tony Marsland") (ed.) (**1996**). *The ACM Chess Challenge*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/5-4.ACM_brochure_1996_Kasparov_vs_Deep_Blue/ACM_brochure_1996_Kasparov_vs_Deep_Blue.062303049.sm.pdf) from the [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), Courtesy of [ACM](ACM "ACM")
- [Tony Marsland](Tony_Marsland "Tony Marsland") (**1996**). *[The Future of Computer Chess](http://ilk.uvt.nl/icga/games/chess/future.php)*. [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal")
- [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1996**). *The Kasparov - Deep Blue Match*. [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal")
- [Yasser Seirawan](https://en.wikipedia.org/wiki/Yasser_Seirawan) (**1996**). *The Kasparov - Deep Blue Games*. [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1996**). *Why did Kasparov Blink?* [ICCA Journal, Vol. 19, No. 2](ICGA_Journal#19_2 "ICGA Journal")
- [Toshinori Munakata](Toshinori_Munakata "Toshinori Munakata") (**1996**). *[Thoughts on Deep Blue vs. Kasparov](https://dl.acm.org/citation.cfm?id=234001)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 39, No. 7, [pdf](http://cis.csuohio.edu/~munakata/publs/pdf/cacm96.pdf)

## 1997

- [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *[Kasparov versus Deep Blue: Computer Chess Comes of Age](https://link.springer.com/book/10.1007/978-1-4612-2260-6).* [Springer](https://de.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Yasser Seirawan](https://en.wikipedia.org/wiki/Yasser_Seirawan), [Herbert Simon](Herbert_Simon "Herbert Simon"), [Toshinori Munakata](Toshinori_Munakata "Toshinori Munakata") (**1997**). *[The Implications of Kasparov vs. Deep Blue](http://dl.acm.org/citation.cfm?id=257878)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 40, No. 8, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/5-4.The_implications_of_deep_blue_vs_kasparov/5-4.The_implications_of_deep_blue_vs_kasparov.simon_seirawan.1997.ACM.062303057.sm.pdf) hosted from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Daniel C. Dennet](https://en.wikipedia.org/wiki/Daniel_Dennett) (**1997**). *Can Machines Think? Deep Blue and Beyond*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1997**). *Evaluation Tuning for Computer Chess: Linear Discriminant Methods*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")
- [Richard Korf](Richard_Korf "Richard Korf") (**1997**). *Does DEEP BLUE use Artificial Intelligence?* [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal") <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**1997**). *[Kasparov versus Deep Blue: The Rematch](http://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Grad/Papers/db.html)*. [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal")
- [Tom R. Halfhill](index.php?title=Tom_R._Halfhill&action=edit&redlink=1 "Tom R. Halfhill (page does not exist)") (**1997**). *[Searching for Deep Blue](https://dl.acm.org/citation.cfm?id=258116).* [BYTE, Vol. 22, No. 07](Byte_Magazine#BYTE2207 "Byte Magazine")
- [Carol McKenna Hamilton](index.php?title=Carol_McKenna_Hamilton&action=edit&redlink=1 "Carol McKenna Hamilton (page does not exist)"), [Sara Hedberg](index.php?title=Sara_Hedberg&action=edit&redlink=1 "Sara Hedberg (page does not exist)") (**1997**). *Modern Masters of an Ancient Game*. [AI Magazine](AAAI#AIMAG "AAAI"), Vol. 18, No. 4, [pdf](http://www.aaai.org/ojs/index.php/aimagazine/article/view/1329/1230)
- [Eric Hallsworth](Eric_Hallsworth "Eric Hallsworth") (**1997**). *Deep\[er\] Blue2 vs Gary Kasparov - IBM Challenge - the Re-Match*. [Selective Search](Selective_Search "Selective Search") 70, pp. 19, [pdf](http://www.chesscomputeruk.com/SS_70.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")

## AAAI Workshop

- [Robert Morris](index.php?title=Robert_Morris&action=edit&redlink=1 "Robert Morris (page does not exist)") (ed.) (**1997**). *[Deep Blue Versus Kasparov: The Significance for Artificial Intelligence](https://aaai.org/Library/Workshops/ws97-04.php)*. Technical Report WS-97-04, [AAAI Press](AAAI#Press "AAAI") <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>

1. [Richard Korf](Richard_Korf "Richard Korf") (**1997**). *Does Deep Blue use AI?* [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](http://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-001.pdf)
1. [Robert Levinson](Robert_Levinson "Robert Levinson"), [Jeff Wilkinson](index.php?title=Jeff_Wilkinson&action=edit&redlink=1 "Jeff Wilkinson (page does not exist)") (**1997**). *[Deep Blue is Still an Infant](https://www.semanticscholar.org/paper/Deep-Blue-is-Still-an-Infant-Levinson-Wilkinson/3ce74263ef7b5d04fdf709b2dd3a519d780ae47f)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop)
1. [Dennis DeCoste](index.php?title=Dennis_DeCoste&action=edit&redlink=1 "Dennis DeCoste (page does not exist)") (**1997**). *[The Future of Chess-Playing Technologies and the Significance of Kasparov Versus deep Blue](https://www.semanticscholar.org/paper/The-Future-of-Chess-Playing-Technologies-and-the-of-DeCoste/0fb4b9659178cd4f516386725243994fde9e7069)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop)
1. [Selmer Bringsjord](index.php?title=Selmer_Bringsjord&action=edit&redlink=1 "Selmer Bringsjord (page does not exist)"), [Adam Lally](index.php?title=Adam_Lally&action=edit&redlink=1 "Adam Lally (page does not exist)") (**1997**). *Chess Isn't Tough Enough: Better Games for Mind-Machine Competition*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-004.pdf)
1. [Fernand Gobet](Fernand_Gobet "Fernand Gobet") (**1997**). *[Can Deep Blue™ make us happy? Reflections on human and artificial expertise](https://bura.brunel.ac.uk/handle/2438/2264)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://pdfs.semanticscholar.org/8e1a/c42a7c63c27ae7986940606829ef629a27da.pdf)
1. [Tony Marsland](Tony_Marsland "Tony Marsland") (**1997**). *The Anatomy of Chess Programs*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf (95)](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1995_WCCC/1995%20WCCC.062303014.sm.pdf)
1. [Carl W. Turner](index.php?title=Carl_W._Turner&action=edit&redlink=1 "Carl W. Turner (page does not exist)") (**1997**). *Attributing Intelligence to Humans and Machines: Between the Devil and the Deep Blue, See*? [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-007.pdf)
1. [Tony Marsland](Tony_Marsland "Tony Marsland"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"). (**1997**). *[From MiniMax to Manhattan](https://www.semanticscholar.org/paper/From-MiniMax-to-Manhattan-Marsland-Bj%C3%B6rnsson/35b30c2508d0d68e4154eab4fdbb87a75926d839)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](http://www.ru.is/faculty/yngvi/pdf/MarslandB97.pdf)
1. [Amol Dattatraya Mali](index.php?title=Amol_Dattatraya_Mali&action=edit&redlink=1 "Amol Dattatraya Mali (page does not exist)"), [Amitabha Mukerjee](index.php?title=Amitabha_Mukerjee&action=edit&redlink=1 "Amitabha Mukerjee (page does not exist)") (**1997**). *[Modularity Assumptions in Situated Agency](https://dl.acm.org/citation.cfm?id=2908800)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop)
1. [Cyrus F. Nournai](index.php?title=Cyrus_F._Nournai&action=edit&redlink=1 "Cyrus F. Nournai (page does not exist)") (**1997**). *Multiagent Chess Games*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-010.pdf)
1. [Kenneth M. Ford](index.php?title=Kenneth_M._Ford&action=edit&redlink=1 "Kenneth M. Ford (page does not exist)"), [Patrick J. Hayes](index.php?title=Patrick_J._Hayes&action=edit&redlink=1 "Patrick J. Hayes (page does not exist)") (**1997**). *What's Wrong With Hal*? [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-011.pdf)
1. [Franz-Günter Winkler](Franz-G%C3%BCnter_Winkler "Franz-Günter Winkler"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**1997**). *[On Effort in AI Research: A Description Along Two Dimensions](https://www.aaai.org/Library/Workshops/1997/ws97-04-012.php)*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop)
1. [David Heath](index.php?title=David_Heath&action=edit&redlink=1 "David Heath (page does not exist)"), [Derek Allum](index.php?title=Derek_Allum&action=edit&redlink=1 "Derek Allum (page does not exist)") (**1997**). *The Historical Development of Computer Chess and its Impact on Artificial Intelligence*. [Deep Blue versus Kasparov, AAAI Workshop](#AAAI_Workshop), [pdf](https://www.aaai.org/Papers/Workshops/1997/WS-97-04/WS97-04-013.pdf)

## 1998 ...

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1998**). *Review of Monty Newborn: Kasparov versus Deep Blue*. [pdf](http://www.ams.org/notices/199804/bkrev-berliner.pdf) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *IBM’s Deep Blue Chess Grandmaster Chips*. [IEEE Micro](IEEE#Micro "IEEE"), Vol. 19, No. 2, [pdf](http://www.csis.pace.edu/~ctappert/dps/pdf/ai-chess-deep.pdf)
- [Murray Campbell](Murray_Campbell "Murray Campbell") (**1999**). *Knowledge Discovery in Deep Blue.* [Communications of the ACM](ACM#Communications "ACM"), Vol. 42, No. 11
- [Murray Campbell](Murray_Campbell "Murray Campbell"), [Joe Hoane](Joe_Hoane "Joe Hoane"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *Search Control Methods in Deep Blue*. [AAAI](AAAI "AAAI") Technical Report SS-99-07, [pdf](https://pdfs.semanticscholar.org/211d/7268093b4dfce8201e8da321201c6cd349ef.pdf), [pdf](https://web.archive.org/web/20160914070926/http://aaaipress.org/Papers/Symposia/Spring/1999/SS-99-07/SS99-07-004.pdf)

## 2000 ...

- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2001**). *Ken Thompson and DEEP BLUE*. [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2001**). *[Comparison Training of Chess Evaluation Functions](http://dl.acm.org/citation.cfm?id=644397)*. In [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (eds.) (**2001**). *[Machines that learn to play games](https://www.novapublishers.com/catalog/product_info.php?products_id=720)*, 117–130, [Nova Science Publishers](https://en.wikipedia.org/wiki/Nova_Science_Publishers) » [Automated Tuning](Automated_Tuning "Automated Tuning"), [SCP](SCP "SCP") <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Murray Campbell](Murray_Campbell "Murray Campbell"), [Joe Hoane](Joe_Hoane "Joe Hoane"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2002**). *[Deep Blue](https://www.sciencedirect.com/science/article/pii/S0004370201001291)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 134, Nos. 1-2
- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2002**). *[Behind Deep Blue: Building the Computer that Defeated the World Chess Champion](http://press.princeton.edu/titles/7342.html)*. [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)

[](http://press.princeton.edu/titles/7342.html)

- [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**2002**). *Deep Blue: An Artificial Intelligence Milestone*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Brian Bloomfield](http://www.lancaster.ac.uk/lums/people/brian-bloomfield), [Theodore Vurdubakis](http://www.lancaster.ac.uk/lums/people/theodore-vurdubakis) (**2008**). *[IBM's Chess Players: On AI and Its Supplements](http://www.tandfonline.com/doi/abs/10.1080/01972240701883922)*. [The Information Society](https://en.wikipedia.org/wiki/The_Information_Society), Vol. 24, No. 2

## 2010 ...

- [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**2011**). *[Beyond Deep Blue: Chess in the Stratosphere](http://www.springer.com/computer/general+issues/book/978-0-85729-340-4)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) <a id="cite-note-12" href="#cite-ref-12">[12]</a>

[](http://www.springer.com/computer/general+issues/book/978-0-85729-340-4)

- [Garry Kasparov](Garry_Kasparov "Garry Kasparov"), [Mig Greengard](index.php?title=Mig_Greengard&action=edit&redlink=1 "Mig Greengard (page does not exist)") (**2017**). *[Deep Thinking: Where Machine Intelligence Ends and Human Creativity Begins](https://www.goodreads.com/book/show/31934455-deep-thinking)*. [PublicAffairs](https://en.wikipedia.org/wiki/PublicAffairs) or [John Murray](<https://en.wikipedia.org/wiki/John_Murray_(publisher)>) <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>

## Forum Posts

## 1992 ...

- [IBM Deep Blue](https://groups.google.com/d/msg/rec.games.chess/xUbJgDIIuic/PywNZYqCvPkJ) by Jens Palsberg, [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), December 12, 1992
- [Deep Blue at Copenhagen: PGN games 1 to 8](https://groups.google.com/d/msg/rec.games.chess/SHgDnUQ9lQI/QgtjswObioIJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 03, 1993
- [Deep Blue Prototype Copenhagen matches (games and comments)](https://groups.google.com/d/msg/rec.games.chess/QnGRalJ_pjg/e6gFjYxc_RAJ) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 07, 1993
- [Request for Deep Blue Prototype information](https://groups.google.com/d/msg/rec.games.chess/MZKdra-ZX88/f6uv2YFCHy4J) by [Garth E. Courtois Jr.](Garth_Courtois_Jr. "Garth Courtois Jr."), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 12, 1993
- [IBM and Deep Blue research](https://groups.google.com/d/msg/rec.games.chess/ktZPD3EjJpk/IuUwtYXaD5gJ) by Edward G. Maillet, [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 28, 1993
- [Judit Polgar at IBM T. J. Watson](https://groups.google.com/d/msg/rec.games.chess/vFrYcF0oiVo/BHILciL9Ot4J) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 23, 1993
- [Deep Blue??? PLEASE](https://groups.google.com/d/msg/rec.games.chess/d1bikHu2e7Y/YhMFN50duWwJ) by Jason M. Rotenberg, [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 02, 1994

## 1995 ...

- [Old Deep Blue News -- since we're all parched](https://groups.google.com/d/msg/rec.games.chess/ERWZGcmWmX0/aydT9w_1AKwJ) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), January 22, 1995
- [Hongkong results!](http://groups.google.com/group/rec.games.chess/browse_frm/thread/222ea8ba3be8bd63) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), May 29, 1995 » [WCCC 1995](WCCC_1995 "WCCC 1995")
- [WCCC round 5 PGN games](http://groups.google.com/group/rec.games.chess/browse_frm/thread/2429681369e468c5) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), May 30, 1995
- [Deep Thought /WCCC Round 5 vs Fritz](http://groups.google.com/group/rec.games.chess/browse_frm/thread/39985e763f042a25) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), May 31, 1995
- [Deep Blue vs Kasparov, and some thoughts on 8th WCCC](http://groups.google.com/group/rec.games.chess/browse_frm/thread/c7204a7e6dfb52d6) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), June 05, 1995
- [Is Computer Chess A Science?](https://groups.google.com/d/msg/rec.games.chess.computer/hsi5bMdZgLU/1EkWxhNVuw0J) by Dr Nancy's Sweetie, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 21, 1996

**1997**

- [Deep Blue vs Micros](https://groups.google.com/d/msg/rec.games.chess.computer/tgR2EbQpqm4/YtR3KqW-FQ4J) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 18, 1997
- [DB Tweaking Between Games](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8d9e40f52871cd85) by [Mike Gherrity](Michael_Gherrity "Michael Gherrity"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 13, 1997
- [Learning necessary for chess champion?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4b36406ce4053ad5) by [Mike Gherrity](Michael_Gherrity "Michael Gherrity"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 16, 1997
- [Deep Blue vs Micros - an interesting result just available](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b7d9a8ab0b57ff60) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 22, 1997
- [Deep Blue news](https://www.stmintz.com/ccc/index.php?id=10093) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [CCC](CCC "CCC"), September 23, 1997
- [Deep Blue team to disclose their files](https://www.stmintz.com/ccc/index.php?id=10952) by [Jack van Rijswijck](index.php?title=Jack_van_Rijswijck&action=edit&redlink=1 "Jack van Rijswijck (page does not exist)"), [CCC](CCC "CCC"), October 20, 1997
- [Meeting M. Campbell and Joe Hoane](https://groups.google.com/d/msg/rec.games.chess.computer/sZ2l8iNhXe4/LLHVNBOKcgkJ) by Han Schut, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 21, 1997

**1998**

- [LCT II Fin4, Deep Thought, and Deep Blue (was Re: LCT II results...)](https://www.stmintz.com/ccc/index.php?id=13703) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), January 05, 1998 » [LCT II](LCT_II "LCT II")
- [Deep Blue eval function tuning technique](https://www.stmintz.com/ccc/index.php?id=13794) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 08, 1998 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Deep Blue-Part I](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ff798bc0d17bcecc) by Keith Ian Price, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 1, 1998
- [Deep Blue-Part II](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1d619119f7c3085b) by Keith Ian Price, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 2, 1998
- [Deep Blue afterthoughts](https://www.stmintz.com/ccc/index.php?id=18229) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), May 09, 1998
- [Deep Blue-Part III](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a49f01a6832f200f) by Keith Ian Price, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 10, 1998
- [Deep Blue chip talk](https://www.stmintz.com/ccc/index.php?id=25080) by [David Fotland](David_Fotland "David Fotland"), [CCC](CCC "CCC"), August 19, 1998

## 2000 ...

- [Nolot Bxh7 and deep thought/deep blue](https://www.stmintz.com/ccc/index.php?id=88032) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), January 12, 2000 » [The Nolot Suite](The_Nolot_Suite "The Nolot Suite")
- [DB NPS (anyone know the position used)?](https://www.stmintz.com/ccc/index.php?id=91692) by Chris Carson, [CCC](CCC "CCC"), January 25, 2000 » [Nodes per Second](Nodes_per_Second "Nodes per Second")
- [Wanted: Deep Blue vs. today's top programs recap](https://www.stmintz.com/ccc/index.php?id=185561) by [Mig Greengard](index.php?title=Mig_Greengard&action=edit&redlink=1 "Mig Greengard (page does not exist)"), [CCC](CCC "CCC"), August 25, 2001
- [Some facts about Deep Thought / Deep Blue](https://www.stmintz.com/ccc/index.php?id=186072) by Erkki Malkamaki, [CCC](CCC "CCC"), August 29, 2001
- [Is Deep Blue still considered better than Deep Junior ?](https://www.stmintz.com/ccc/index.php?id=246006) by Jorge Pichard, [CCC](CCC "CCC"), August 18, 2002 » [Deep Junior](Junior "Junior")
- ["Deep Blue ..." in 1995](https://www.stmintz.com/ccc/index.php?id=259002) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), October 14, 2002
- [DeepBlue && SingularExtensions && !Nullmoving](https://www.stmintz.com/ccc/index.php?id=259497) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), October 16, 2002 » [Singular Extensions](Singular_Extensions "Singular Extensions"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [deep blue's automatic tuning of evaluation function](https://www.stmintz.com/ccc/index.php?id=290239) by Emerson Tan, [CCC](CCC "CCC"), March 22, 2003 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Behind Deep Blue: 3rd print with new Hsu afterword](https://www.stmintz.com/ccc/index.php?id=363852) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), May 07, 2004
- [Article by Tesauro on Deep Blue's evaluation-tuning](https://www.stmintz.com/ccc/index.php?id=375936) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), July 11, 2004 <a id="cite-note-16" href="#cite-ref-16">[16]</a>

## 2005 ...

- [Deep Blue Language](https://www.stmintz.com/ccc/index.php?id=405037) by Daniel Marquez Lisboa, [CCC](CCC "CCC"), January 11, 2005
- [Kasparov \[HBR interview\] : 'IBM committed a crime against science.'](https://www.stmintz.com/ccc/index.php?id=422970) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), April 26, 2005 <a id="cite-note-17" href="#cite-ref-17">[17]</a>
- [(Obvious troll) Kasparov vs DB-I was a disaster for human chess](https://www.stmintz.com/ccc/index.php?id=424608) by [Walter Faxon](Walter_Faxon "Walter Faxon"), [CCC](CCC "CCC"), May 06, 2005
- [Robert question, Deep Blue 3.1x](https://www.stmintz.com/ccc/index.php?id=450405) by K. Burcham, [CCC](CCC "CCC"), September 19, 2005
- [Adjusting weights the Deep Blue way](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49450) by [Tony van Roon-Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 29, 2008 » [Automated Tuning](Automated_Tuning "Automated Tuning")

## 2010 ...

- [The blunders in 1995 chess programs, Deep Blue vs fritz](http://www.talkchess.com/forum/viewtopic.php?t=42012) by kgburcham, [CCC](CCC "CCC"), January 15, 2012
- [Performancerating of Kasparov and Deep Blue in their matches](http://www.talkchess.com/forum/viewtopic.php?t=45538) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), October 11, 2012
- [24 February 1993 - a disastrous day for Deep Blue](http://www.talkchess.com/forum/viewtopic.php?t=47320) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), February 24, 2013
- [4 hours video: B Larsen met Deep Blue in 1993 in Copenhagen](http://www.talkchess.com/forum/viewtopic.php?t=52512) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), June 01, 2014

## 2015 ...

- [New Pictures from Kasparov vs. Deep Blue](http://www.talkchess.com/forum/viewtopic.php?t=59211) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), February 10, 2016 <a id="cite-note-18" href="#cite-ref-18">[18]</a>
- [Hash Tables Deep Blue](http://www.talkchess.com/forum/viewtopic.php?t=64021) by Gustavo Mallada, [CCC](CCC "CCC"), May 18, 2017 » [Transposition Table](Transposition_Table "Transposition Table")

## 2020 ...

- [Deep Blue | Down the Rabbit Hole](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75649) by Anthony Wilson, [CCC](CCC "CCC"), November 02, 2020 » [Down the Rabbit Hole](#DowntheRabbitHole)

## External Links

- [Deep Blue from Wikipedia](https://en.wikipedia.org/wiki/Deep_Blue_%28chess_computer%29)
- [Deep Blue Prototype ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=349)
- [Games at chessgames.com](http://www.chessgames.com/perl/ezsearch.pl?search=Deep+Blue)
- [IBM100 - Deep Blue](https://www.ibm.com/ibm/history/ibm100/us/en/icons/deepblue/)
- [IBM Archives: Deep Blue](https://www.ibm.com/ibm/history/exhibits/vintage/vintage_4506VV1001.html?mhq=Deep%20Blue&mhsrc=ibmsearch_a)
- [IBM Research | Kasparov vs. Deep Blue: The Rematch - IBM](https://researcher.watson.ibm.com/researcher/view_group.php?id=2942)
- [Challenging the World Champion | Mastering the Game](http://www.computerhistory.org/chess/challenging-the-world-champion/) [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Deep Blue screenshot](http://www.computerhistory.org/chess/stl-431e1a0802660/) hosted by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") » [XBoard](XBoard "XBoard")
- [Deep Blue II](http://www.computerhistory.org/chess/art-43305f13ef377/) by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [IBM advertisement: Deep Blue Castles](http://www.computerhistory.org/chess/doc-431615395dc2e/) hosted by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

## By Date

### 1997

- ["Deep Blue" inspires deep thinking about artificial intelligence by computer scientist](https://www.sciencedaily.com/releases/1997/05/970501194114.htm) by [Robert Irion](https://scicom.ucsc.edu/faculty/), [University of California, Santa Cruz](University_of_California,_Santa_Cruz "University of California, Santa Cruz"), May 5, 1997
- [Techmate](https://www.forbes.com/asap/1999/0222/071.html) by [Garry Kasparov](Garry_Kasparov "Garry Kasparov"), February 22, 1999, [Forbes.com](https://en.wikipedia.org/wiki/Forbes) <a id="cite-note-19" href="#cite-ref-19">[19]</a>

### 2000 ...

- [The Week in Chess Magazine: Open Letter](http://theweekinchess.com/html/twic270.html) from [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), January 10, 2000
- [ChessBase: Behind Deep Blue](https://en.chessbase.com/post/behind-deep-blue) (review) by James E. DuBois, [ChessBase News](ChessBase "ChessBase"), October 13, 2002
- [Von Kemplen's "The Turk" and IBM's "Deep Blue"](http://www.conceptlab.com/uci/2005fall/krapp/turk-kasparov/), Conspiracies of a Hidden Human by [Garnet Hertz](https://en.wikipedia.org/wiki/Garnet_Hertz), November 9, 2005
- [A Decade After Kasparov's Defeat, Deep Blue Coder Relives Victory](https://www.wired.com/2007/05/a-decade-after-kasparovs-defeat-deep-blue-coder-relives-victory/), Interview with [Murray Campbell](Murray_Campbell "Murray Campbell") by [Robert Andrews](https://www.wired.com/author/robert-andrews/), [Wired News](<https://en.wikipedia.org/wiki/Wired_(magazine)#Website>), November 05, 2007

### 2010 ...

- [The Man vs. The Machine documentary](https://en.chessbase.com/post/the-man-vs-the-machine-documentary) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), October 26, 2014
- [Komodo 8: Deep Blue revisited (part one)](https://en.chessbase.com/post/komodo-8-deep-blue-revisited-part-one) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 26, 2014 » [Komodo](Komodo "Komodo"), [Kasparov versus Deep Blue 1997](Kasparov_versus_Deep_Blue_1997 "Kasparov versus Deep Blue 1997") <a id="cite-note-20" href="#cite-ref-20">[20]</a>
- [Komodo 8: Deep Blue revisited (part two)](https://en.chessbase.com/post/komodo-8-deep-blue-revisited-part-two) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 31, 2014
- [Komodo 8: Deep Blue revisited (part three)](https://en.chessbase.com/post/komodo-8-deep-blue-revisited-part-three) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), January 09, 2015
- [Deep Blue's cheating move](https://en.chessbase.com/post/deep-blue-s-cheating-move) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 19, 2015
- [20 years ago, a computer first beat a chess world champion - 1996-1997 The Kasparov-Deep Blue chess matches](https://mashable.com/2016/02/10/kasparov-deep-blue/) by [Alex Q. Arbuckle](http://www.alexqarbuckle.com/bio), February 10, 2016
- [Garry Kasparov: Don't fear intelligent machines. Work with them](https://www.ted.com/talks/garry_kasparov_don_t_fear_intelligent_machines_work_with_them) | [TED Talk](<https://en.wikipedia.org/wiki/TED_(conference)>), April 2017 <a id="cite-note-21" href="#cite-ref-21">[21]</a>
- [Twenty years on from Deep Blue vs Kasparov: how a chess match started the big data revolution](http://theconversation.com/twenty-years-on-from-deep-blue-vs-kasparov-how-a-chess-match-started-the-big-data-revolution-76882) by [Mark Robert Anderson](https://theconversation.com/profiles/mark-robert-anderson-273683), [The Conversation](<https://en.wikipedia.org/wiki/The_Conversation_(website)>), May 11, 2017
- [20 Years after Deep Blue: How AI Has Advanced Since Conquering Chess](https://www.scientificamerican.com/article/20-years-after-deep-blue-how-ai-has-advanced-since-conquering-chess/) by [Larry Greenemeier](https://www.crunchbase.com/person/larry-greenemeier), [Scientific American](Scientific_American "Scientific American"), June 2, 2017 <a id="cite-note-22" href="#cite-ref-22">[22]</a> » [Kasparov versus Deep Blue 1997](Kasparov_versus_Deep_Blue_1997 "Kasparov versus Deep Blue 1997"), [Murray Campbell](Murray_Campbell "Murray Campbell")
- [Kasparov on Deep Learning in chess](https://en.chessbase.com/post/kasparov-on-deep-learning-in-chess) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), December 13, 2017

## Videos

- [Chess computer Deep Blue and Bent Larsen in Copenhagen 1993 part 1](https://www.youtube.com/watch?v=xBggvYjWJmk), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos <a id="cite-note-23" href="#cite-ref-23">[23]</a>

- [Chess computer Deep Blue and Bent Larsen in Copenhagen 1993 part 2](https://www.youtube.com/watch?v=R-ARSPzcXKE)

- [Chess computer Deep Blue and Bent Larsen in Copenhagen 1993 part 3 (final)](https://www.youtube.com/watch?v=FCK71czc3bc)

- IBM Research scientist [Murray Campbell](Murray_Campbell "Murray Campbell") on Deep Blue, May 11, 2012, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [Checkmate: Members of IBM’s Deep Blue Team Discuss the World of Computer Chess](https://www.worldsciencefestival.com/videos/checkmate-how-computer-chess-changed-the-world/), June 1, 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video » [Computer Chess - A Movie](History#ComputerChess "History"), [Murray Campbell](Murray_Campbell "Murray Campbell")

- [Deep Blue | Down the Rabbit Hole](https://youtu.be/HwF229U2ba8) by [Fredrik Knudsen](https://www.youtube.com/channel/UCbWcXB0PoqOsAvAdfzWMf0w), October 30, 2020, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-24" href="#cite-ref-24">[24]</a>

- [Deep Purple](Category:Deep_Purple "Category:Deep Purple") - [Highway Star](https://en.wikipedia.org/wiki/Highway_Star_%28song%29), [Machine Head](https://en.wikipedia.org/wiki/Machine_Head_%28album%29) (1972), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Deep Blue, a computer similar to this one defeated [Garry Kasparov](Garry_Kasparov "Garry Kasparov") in May 1997. Photo taken by [James the photographer](https://www.flickr.com/photos/jamesthephotographer/) at [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), June 14, 2007, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Deep blue chip](http://www.computerhistory.org/chess/full_record.php?iid=art-431614f45291e), [International Business Machines (IBM)](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)"), 1997, Gift of [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Deep Thought (Chess) (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/program.php?id=349)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *IBM’s Deep Blue Chess Grandmaster Chips*. [IEEE Micro](IEEE#Micro "IEEE"), Vol. 19, No. 2, [pdf](http://www.csis.pace.edu/~ctappert/dps/pdf/ai-chess-deep.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [The core Deep Blue team](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f67157b) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), Courtesy of IBM Archives
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1998**). *Review of Monty Newborn: Kasparov versus Deep Blue*. [pdf](http://www.ams.org/notices/199804/bkrev-berliner.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: ICCA Journal Sinks To A New Low](https://www.stmintz.com/ccc/index.php?id=14647) by [Amir Ban](Amir_Ban "Amir Ban"), [CCC](CCC "CCC"), January 25, 1998
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [AAAI Workshop: Deep Blue Versus Kasparov: The Significance for Artificial Intelligence 1997](https://www.dblp.org/db/conf/aaai/aaai1997w6.html)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> ["Deep Blue" inspires deep thinking about artificial intelligence by computer scientist](https://www.sciencedaily.com/releases/1997/05/970501194114.htm) by [Robert Irion](https://scicom.ucsc.edu/faculty/), [University of California, Santa Cruz](University_of_California,_Santa_Cruz "University of California, Santa Cruz"), May 5, 1997
1. <a id="cite-ref-10" href="#cite-note-10">↑</a>  [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *[Kasparov versus Deep Blue: Computer Chess Comes of Age](http://link.springer.com/book/10.1007/978-1-4612-2260-6).* [Springer](https://de.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Article by Tesauro on Deep Blue's evaluation-tuning](https://www.stmintz.com/ccc/index.php?id=375936) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), July 11, 2004
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [New CC book: Beyond Deep Blue](http://www.talkchess.com/forum/viewtopic.php?t=41053) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), November 11, 2011
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Garry Kasparov: Don't fear intelligent machines. Work with them](https://www.ted.com/talks/garry_kasparov_don_t_fear_intelligent_machines_work_with_them) | [TED Talk](<https://en.wikipedia.org/wiki/TED_(conference)>), April 2017
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [The Day the Machines Took Over](https://medium.com/@AdamThierer/the-day-the-machines-took-over-51076ba8e4f4) by [Adam Thierer](https://www.mercatus.org/adam-thierer), [Medium](<https://en.wikipedia.org/wiki/Medium_(website)>), May 11, 2017
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Kasparov on Deep Learning in chess](https://en.chessbase.com/post/kasparov-on-deep-learning-in-chess) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), December 13, 2017
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2001**). *[Comparison Training of Chess Evaluation Functions](http://dl.acm.org/citation.cfm?id=644397)*. In [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (eds.) (**2001**). *[Machines that learn to play games](https://www.novapublishers.com/catalog/product_info.php?products_id=720)*, 117–130, [Nova Science Publishers](https://en.wikipedia.org/wiki/Nova_Science_Publishers)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Strategic Intensity - A Conversation with World Chess Champion Garry Kasparov](http://hbr.org/2005/04/strategic-intensity/ar/1) by [Diane L. Coutu](http://www.linkedin.com/pub/diane-coutu/9/111/67a), [Harvard Business Review](https://en.wikipedia.org/wiki/Harvard_Business_Review), April 2005
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [20 years ago, a computer first beat a chess world champion - 1996-1997 The Kasparov-Deep Blue chess matches](http://mashable.com/2016/02/10/kasparov-deep-blue/#NdUYEzkSGkqJ) by [Alex Q. Arbuckle](http://www.alexqarbuckle.com/bio), February 10, 2016
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> ["Techmate" by Garry Kasparov](https://www.stmintz.com/ccc/index.php?id=108799) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), May 02, 2000
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Komodo 8: Deep Blue revisited (1/2)](http://www.talkchess.com/forum/viewtopic.php?t=54759) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), December 27, 2014
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Garry Kasparov](Garry_Kasparov "Garry Kasparov"), [Mig Greengard](index.php?title=Mig_Greengard&action=edit&redlink=1 "Mig Greengard (page does not exist)") (**2017**). *[Deep Thinking: Where Machine Intelligence Ends and Human Creativity Begins](https://www.goodreads.com/book/show/31934455-deep-thinking)*. [PublicAffairs](https://en.wikipedia.org/wiki/PublicAffairs) or [John Murray](<https://en.wikipedia.org/wiki/John_Murray_(publisher)>)
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Scientific American article on Computer Chess](http://www.talkchess.com/forum/viewtopic.php?t=64158) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 03, 2017
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [4 hours video: B Larsen met Deep Blue in 1993 in Copenhagen](http://www.talkchess.com/forum/viewtopic.php?t=52512) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), June 01, 2014
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Deep Blue | Down the Rabbit Hole](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75649) by Anthony Wilson, [CCC](CCC "CCC"), November 02, 2020

**[Up one Level](Engines "Engines")**

