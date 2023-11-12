---
title: Piece Recognition
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Position](Chess_Position "Chess Position") \* Piece Recognition**



 [](File:Schachspiel2016Henrichshuette.JPG) Chessgame <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Piece Recognition**, (Chess Board or Chess Position Recognition)  

 the ability of [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") or chess playing [robots](Robots "Robots") to automatically recognize all the [pieces](Pieces "Pieces") on a [chessboard](Chessboard "Chessboard"), or in [computer vision](https://en.wikipedia.org/wiki/Computer_vision) to convert an image of a real chessboard with pieces, or a [chess diagram](https://en.wikipedia.org/wiki/Chess_diagram) into a machine readable format specifying a chess position, such as [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN) or [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD). 



## Piece Recognition Boards


The [user interface](User_Interface "User Interface") task to [enter moves](Entering_Moves "Entering Moves") on a [sensory board](Sensory_Board "Sensory Board") is often implemented with pressure sensitive or [magnetic switches](https://en.wikipedia.org/wiki/Magnetic_switch) to determine [origin](Origin_Square "Origin Square") and [target squares](Target_Square "Target Square") with the implicit knowledge of the game state which piece was on the origin square and moved. The incremental update during [game play](Chess_Game "Chess Game") starting from the [initial position](Initial_Position "Initial Position") requires some care to keep internal and external board representation in sync, specially if analyzing with taking moves back. Here, real piece recognition offers not only much more comfort in entering arbitrary positions, but also more fault tolerant move recognition for dedicated units.


Piece recognition sensory boards require special [electronics](https://en.wikipedia.org/wiki/Electronics), and pieces with integrated [passive components](https://en.wikipedia.org/wiki/Electronic_component#Passive_components), such as [piece type](Pieces#PieceTypeCoding "Pieces") and piece color specific [coils](https://en.wikipedia.org/wiki/Coil) on [ferrite core](https://en.wikipedia.org/wiki/Ferrite_core) of a [LC circuit](https://en.wikipedia.org/wiki/LC_circuit). Selected via file- and rank [multiplexer](https://en.wikipedia.org/wiki/Multiplexer), the LC circuit forms a [inductive coupled](https://en.wikipedia.org/wiki/Inductive_coupling) [feedback loop](https://en.wikipedia.org/wiki/Feedback) of an [amplifier](https://en.wikipedia.org/wiki/Amplifier) forcing [oscillation](https://en.wikipedia.org/wiki/Oscillation) in piece type specific [resonance](https://en.wikipedia.org/wiki/Resonance), which could be measured or filtered, to detect the piece (if any) on the selected square. As reported by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Ken Thompson](Ken_Thompson "Ken Thompson") already had a piece recognition board based on coils in the base of the pieces, as demonstrated at [ACM 1978](ACM_1978 "ACM 1978") with [Belle](Belle "Belle") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Along with [Henry S. Baird](Mathematician#HSBaird "Mathematician"), Ken Thompson further contributed to computer vision applied to [reading chess](Algebraic_Chess_Notation#ReadingChess "Algebraic Chess Notation") a few years later <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



## Selected Systems


* [Certabo Chessboard](Certabo_Chessboard "Certabo Chessboard")
* [Chess-Master](Chess-Master "Chess-Master")
* [DGT Board](DGT_Board "DGT Board")
* [Mephisto Bavaria](Mephisto_Module_Systems "Mephisto Module Systems")
* [Millennium ChessGenius](Millennium_ChessGenius "Millennium ChessGenius")
* [Raspberry Turk](Raspberry_Turk "Raspberry Turk")
* [Revelation II](Revelation_II "Revelation II")
* [TASC R30](TASC_R30 "TASC R30")
* [TASC R40](TASC_R40 "TASC R40")
* [TASC SmartBoard](TASC_SmartBoard "TASC SmartBoard")


## See also


* [DGT Board - Piece Recognition](DGT_Board#PieceRecognition "DGT Board")
* [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
* [Reading Chess](Algebraic_Chess_Notation#ReadingChess "Algebraic Chess Notation")
* [Robots](Robots "Robots")
* [Sensory Board](Sensory_Board "Sensory Board")
* [TASC SmartBoard - Patent Infringement](TASC_SmartBoard#PatentInfringement "TASC SmartBoard")


## Publications


### 2000 ...


* [Timothée Cour](https://scholar.google.com/citations?user=pkFzb9QAAAAJ), [Rémy Lauranson](https://www.linkedin.com/in/r%C3%A9my-lauranson-3799a623/), [Matthieu Vachette](http://fr.linkedin.com/pub/matthieu-vachette/1b/bb5/571) (**2002**). *Autonomous Chess-playing Robot*. [École Polytechnique](https://en.wikipedia.org/wiki/%C3%89cole_Polytechnique), [pdf](http://www.timotheecour.com/papers/ChessAutonomousRobot.pdf), [pdf](https://pdfs.semanticscholar.org/57e7/9b85d53597d59a1009ea964876de260935ea.pdf)
* [David Urting](http://be.linkedin.com/pub/david-urting/4/82b/448), [Yolande Berbers](http://distrinet.cs.kuleuven.be/people/showMember.do?memberID=u0006685) (**2003**). *[MarineBlue: A Low-Cost Chess Robot](https://lirias.kuleuven.be/handle/123456789/132621?mode=full&submit_simple=Show+full+item+record)*. [Katholieke Universiteit Leuven](https://en.wikipedia.org/wiki/Katholieke_Universiteit_Leuven), [RA 2003](http://dblp.uni-trier.de/db/conf/ra/ra2003.html#UrtingB03). [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=CE76646F8F250AB5DAA36951D4D28335?doi=10.1.1.83.6961&rep=rep1&type=pdf)


### 2010 ...


* [Arturo De la Escalera](https://www.linkedin.com/in/arturo-de-la-escalera-hueso-b82a0138/), [Jose María Armingol](https://scholar.google.com/citations?user=VBUqG3AAAAAJ) (**2010**). *[Automatic Chessboard Detection for Intrinsic and Extrinsic Camera Parameter Calibration](http://www.mdpi.com/1424-8220/10/3/2027)*. [Sensors](https://en.wikipedia.org/wiki/Sensors_(journal)), vol. 10, No. 3
* [Cynthia Matuszek](http://www.cs.washington.edu/homes/cynthia/), [Brian Mayton](http://bdm.cc/), [Roberto Aimi](http://web.media.mit.edu/~roberto/), [Marc Peter Deisenroth](http://www.ias.informatik.tu-darmstadt.de/Team/MarcDeisenroth), [Liefeng Bo](http://www.cs.washington.edu/homes/lfb/), [Robert Chu](http://www.linkedin.com/pub/robert-chu/2a/6bb/714), [Mike Kung](http://www.linkedin.com/pub/mike-kung/14/2a5/89a), [Louis LeGrand](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/l/LeGrand:Louis.html), [Joshua R. Smith](http://web.media.mit.edu/~jrs/), [Dieter Fox](http://www.cs.washington.edu/homes/fox/) (**2011**). *[Gambit: A Robust Chess-Playing Robotic System](http://www.cs.washington.edu/ai/Mobile_Robotics//projects/gambit/abstracts/chess-icra-11.abstract.html)*. Proc. of [ICRA 2011](http://www.icra2011.org/), [pdf](http://www.cs.washington.edu/ai/Mobile_Robotics/postscripts/chess-icra-11.pdf) <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Nandan Banerjee](https://scholar.google.com/citations?user=c9eehXcAAAAJ&hl=en), [Debal Saha](https://www.linkedin.com/in/debalsaha/?ppe=1), [Atikant Singh](https://scholar.google.co.in/citations?user=vyadjhgAAAAJ&hl=en), [Gautam Sanyal](https://scholar.google.co.in/citations?user=W4uu_30AAAAJ&hl=en) (**2011**). *A Simple Autonomous Robotic Manipulator for Playing Chess Against any Opponent in Real Time*. [pdf](http://nandanbanerjee.com/files/ICCVR-08AUG12-011%20paper.pdf)
* [Cheryl Danner](https://www.linkedin.com/in/cheryl-danner-b315bb5/), [Mai Kafafy](https://scholar.google.com.eg/citations?user=IiJjdPsAAAAJ&hl=en) (**2015**). *Visual Piece Recognition*. [Stanford University](Stanford_University "Stanford University"), [pdf](https://web.stanford.edu/class/ee368/Project_Spring_1415/Reports/Danner_Kafafy.pdf) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [Raghuveer Kanchibail](https://www.linkedin.com/in/raghuveerkanchibail/), [Supreeth Suryaprakash](https://www.linkedin.com/in/supreethprakash/), [Suhas Jagadish](https://www.linkedin.com/in/jsuhas89/) (**2016**). *Chess Board Recognition*. School of Informatics and Computing, [Indiana University](https://en.wikipedia.org/wiki/Indiana_University), [pdf](http://vision.soic.indiana.edu/b657/sp2016/projects/rkanchib/paper.pdf)


## Forum Posts


* [Re: Tasc R30 v 2.5?](https://www.stmintz.com/ccc/index.php?id=67834) by [Steven Schwartz](Steven_Schwartz "Steven Schwartz"), [CCC](CCC "CCC"), September 08, 1999
* [Re: What happened to TASC?](https://www.stmintz.com/ccc/index.php?id=194531) by [Steven Schwartz](Steven_Schwartz "Steven Schwartz"), [CCC](CCC "CCC"), October 27, 2001
* [Web-cam based chessboard position digital recognition?](https://www.chess.com/forum/view/chess-equipment/web-cam-based-chessboard-position-digital-recognition) by Clifton Prince, [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), June 04, 2016
* [Vice solving problems on Twitter](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78620) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), November 08, 2021 » [Vice](Vice "Vice")


## External Links


* [Patent US5129654 - Electronic game apparatus - Google Patents](http://www.google.com/patents/US5129654) » [TASC SmartBoard - Patent Infringement](TASC_SmartBoard#PatentInfringement "TASC SmartBoard")
* [Chess Grabber](http://chessgrabber.nicolaas.net/acknowledgements)
* [Webcam Chess](http://webcamchess.fr/)
* [Building Chess ID – Medium](https://medium.com/@daylenyang/building-chess-id-99afa57326cd) by [Daylen Yang](Daylen_Yang "Daylen Yang")
* [GitHub - daylen/chess-id: Board localization and piece recognition](https://github.com/daylen/chess-id) by [Daylen Yang](Daylen_Yang "Daylen Yang")
* [Visual Chess Recognition - Semantic Scholar](https://www.semanticscholar.org/paper/Visual-Chess-Recognition-Danner-Kafafy/84f766e32665138f78bdc61486ca13a52bbc7d39) by [Cheryl Danner](https://www.linkedin.com/in/cheryl-danner-b315bb5/) and [Mai Kafafy](https://scholar.google.com.eg/citations?user=IiJjdPsAAAAJ&hl=en) <a id="cite-note-10" href="#cite-ref-10">[10]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Schachspiel by Lür Henning Flake, from the [Technophilia](https://www.lwl.org/industriemuseum/standorte/henrichshuette-hattingen/sonderausstellung/technophilia) art exhibition at [Henrichshütte Ironworks - Museum of iron and steel](Category:Henrichsh%C3%BCtte "Category:Henrichshütte"), [Hattingen](https://en.wikipedia.org/wiki/Hattingen), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), [Germany](https://en.wikipedia.org/wiki/Germany), part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), October 01, 2016
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Building Chess ID – Medium](https://medium.com/@daylenyang/building-chess-id-99afa57326cd) by [Daylen Yang](Daylen_Yang "Daylen Yang")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Vice solving problems on Twitter](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78620) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), November 08, 2021
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Tasc R30 v 2.5?](https://www.stmintz.com/ccc/index.php?id=67909) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 08, 1999
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [The Gambit Manipulator at UW RSE-lab](http://www.cs.washington.edu/ai/Mobile_Robotics//projects/gambit/)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Personal Robotics at Intel Labs Seattle](http://www.seattle.intel-research.net/robotics/)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Chess Playing Robot](http://www.chessplayingrobot.com/)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Visual Chess Recognition - Semantic Scholar](https://www.semanticscholar.org/paper/Visual-Chess-Recognition-Danner-Kafafy/84f766e32665138f78bdc61486ca13a52bbc7d39)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a>  [Cheryl Danner](https://www.linkedin.com/in/cheryl-danner-b315bb5/), [Mai Kafafy](https://scholar.google.com.eg/citations?user=IiJjdPsAAAAJ&hl=en) (**2015**). *Visual Piece Recognition*. [Stanford University](Stanford_University "Stanford University"), [pdf](https://web.stanford.edu/class/ee368/Project_Spring_1415/Reports/Danner_Kafafy.pdf)

**[Up one level](Chess_Position "Chess Position")**







 
