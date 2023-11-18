---
title: El Ajedrecista
---
**[Home](Home "Home") * [Engines](Engines "Engines") * El Ajedrecista**

**[Home](Home "Home") * [History](History "History") * El Ajedrecista**

**El Ajedrecista**,[](File:Ajedrecista200x206.jpg) El Ajedrecista <a id="cite-note-1" href="#cite-ref-1">[1]</a>
the [electro-mechanical](Electro-Mechanical "Electro-Mechanical") [KRK](KRK "KRK") solver by [Leonardo Torres y Quevedo](Leonardo_Torres_y_Quevedo "Leonardo Torres y Quevedo"). In 1910 Torres began (other sources state 1890, or 1901 <a id="cite-note-2" href="#cite-ref-2">[2]</a>) to construct the chess automaton. In [1912](Timeline#1912 "Timeline") it was able to automatically play a white king (initially on a8) and white rook (initially on b7) against the lonesome black king placed on any square, except 7th or 8th rank. The algorithm was suboptimal, but could win in less than 50 moves against any defense <a id="cite-note-3" href="#cite-ref-3">[3]</a> . It used mechanical arms to make its moves and electrical sensors to detect its opponent's replies.
A second, mechanical but not algorithmic improved El Ajedrecista was built by Leonardo Torres Quevedo's son **Gonzalo** in 1922, under the direction of his father. At the 1951 Paris Cybernetic Congress the advanced machine was introduced to a greater audience and explained to [Norbert Wiener](Norbert_Wiener "Norbert Wiener") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Even if only playing KRK, El Ajedrecista can be considered as the world’s **first** chess computer, even a [dedicated](Dedicated_Chess_Computers "Dedicated Chess Computers") [robot](Robots "Robots") able to move its own pieces. It is still functional and can be visited at the Torres Quevedo Museum of Engineering, Institute of Civil Engineering at the [Universidad Politécnica de Madrid](Technical_University_of_Madrid "Technical University of Madrid") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. During the [WCCC 1992](WCCC_1992 "WCCC 1992"), hosted by the Universidad Politécnica de Madrid, the original El Ajedrecista was an exhibit in the tournament hall <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Photos

## El Ajedrecista I

[](https://www.torresquevedo.org/LTQ10/index.php?title=Archivo:PrimerAjedrecista.jpg)
Front view of the 1911 chess playing automation. The chessboard is shown in the lower right of center. Horizontal and vertical arms moved the pieces (which were actually [electrical jacks](https://en.wikipedia.org/wiki/Electrical_connector)) [from square](Origin_Square "Origin Square") [to square](Target_Square "Target Square"), and the logic circuitry consisted of [battery](https://en.wikipedia.org/wiki/Battery_%28electricity%29) driven [relays](https://en.wikipedia.org/wiki/Relay) arranged in a logical tree structure <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## El Ajedrecista II

Gonzalo Torres y Quevedo and [Norbert Wiener](Norbert_Wiener "Norbert Wiener") <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## Description

On March 17, 2007, the [Institute of Electrical and Electronics Engineers](IEEE "IEEE") (IEEE) recognized Torres’ [Telekine](https://en.wikipedia.org/wiki/Remote_control#History) <a id="cite-note-11" href="#cite-ref-11">[11]</a> with an [IEEE Milestone](https://en.wikipedia.org/wiki/List_of_IEEE_milestones) in [Electrical Engineering](https://en.wikipedia.org/wiki/Electrical_engineering) and [Computing](https://en.wikipedia.org/wiki/Computing) <a id="cite-note-12" href="#cite-ref-12">[12]</a> . The dedication was held at the Torres Quevedo Museum of Engineering, Institute of Civil Engineering, [Universidad Politécnica de Madrid](Technical_University_of_Madrid "Technical University of Madrid"), and following description of El Ajedrecista was given in the Celebration Ceremony Booklet *Early Developments in Remote-Control, 1901 - The Telekine* <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a> :

`Roughly speaking, the movement of white pieces depends on the movement of the black king. Each of the 64 squares of the chess board (8 rows x 8 columns) are formed by three metallic pieces separated each other by an insulating material; the central piece is circular and is connected to the positive terminal whereas the side pieces are triangular and are respectively connected to two conductors, one horizontal and one vertical.`

`The black king has a silver mesh-base that connects the central piece of the square to the triangular ones, thus closing two electrical circuits that move two respective sliding bars, one horizontal and one vertical, until they reach two positions that determine the black king position on the chess board. Similarly, positions of the white king and rook are defined by four sliding bars, two for each of the pieces. When the black king moves into a position, the corresponding sliding bars move and close, by means of suitable contacts, the electrical circuits which act in turn on the white pieces making them move according to the game strategy. The white pieces have a steel ball in their base and are driven by electromagnets, which are placed under the table and suitably activated for each black king position.`

`When a check situation occurs, a phonographic disc pronounces the sentence “check to the king”. When checkmate occurs, the disc pronounces the corresponding sentence and a warning light indicating mate is turned on. In these cases, an electromagnet removes the tension from the board, thus ending the game. The automaton won. Although the chess automaton function was limited to particular chess endgames, Torres Quevedo proved that further advances in computer technology were possible at a time when the information about “artificial intelligence” was very limited. At the time of this invention Torres Quevedo was President of the Academy of Sciences of Madrid, Spain.`

## The Robot

A detailed explanation of El Ajedrecista can be found in *Les Automates* by [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") <a id="cite-note-15" href="#cite-ref-15">[15]</a> :

`If the opponent plays an illegal move, a light comes on and the robot refuses to make a move. Once three such illegal moves have been made, the robot ceases to play altogether. If, on the contrary, the robot will carry out one of six operations, depending upon the position of the (just moved) black king. In order to archive this, Mr Torres use two zones on the chessboard: the one on the left consisting of the a-, b-, c-files, and the corresponding one on the right consisting of the h-, g-, and f-files (and a center zone consisting of d-, and e-file). We then have six operations as shown in the figure:`

|  |
| --- |
|  The (defending) black King
|
|  is in the samezone as the(white) rook
|  is not in the same zone as the rook and the verticaldistance between the black king and the rook is
|
|  |  more thana square
|  one square, with the vertical distancebetween the two kings being
|
|  |  |  more thantwo squares
|  two squares, with the numberof square representing theirhorizontal distance apart being
|
|  |  |  |  odd  |  even  |  zero
|
|  The rookmovesawayhorizontally
|  The rookmovesdown onesquare
|  The kingmovesdown onesquare
|  The rookmoves onesquarehorizontally
|  The whiteking movesone squaretowards theblack king
|  The rookmovesdown onesquare
|
|  1  |  2  |  3  |  4  |  5  |  6
|

## Assembly

[](File:Quevedo-Hauptschaltung.png)
El Ajedrecista - principle assembly diagram <a id="cite-note-16" href="#cite-ref-16">[16]</a>

## Making own Moves

Eight [electro-mechanical](Electro-Mechanical "Electro-Mechanical") [actuators](https://en.wikipedia.org/wiki/Actuator) [make](Make_Move "Make Move") the robot's own white king (left, right, down) or rook (left, right, down one square, horizontally to a- and h-file) [moves](Moves "Moves") and [update](Incremental_Updates "Incremental Updates") its internal [board representation](Board_Representation "Board Representation"). They are build using a disc (D) under [friction](https://en.wikipedia.org/wiki/Friction) [torque](https://en.wikipedia.org/wiki/Torque) of a [spindle](https://en.wikipedia.org/wiki/Spindle_%28tool%29) (O) driven by [weights](https://en.wikipedia.org/wiki/Weight) suspended from a cord wrapped around a [pulley](https://en.wikipedia.org/wiki/Pulley) <a id="cite-note-17" href="#cite-ref-17">[17]</a>. The disc has one sawtooth to prevent motion by an [pawl](https://en.wikipedia.org/wiki/Ratchet_%28device%29) unless an [electromagnet](https://en.wikipedia.org/wiki/Electromagnet) (E) shortly attracts [armature](https://en.wikipedia.org/wiki/Armature_%28electrical_engineering%29) (A), allowing a full disc rotation, running a kind of mechanical microprogram for a specific piece movement. Using vertical and horizontal sliding arms, the robot addresses the [origin square](Origin_Square "Origin Square"), grasps the piece from the board's plug hole, moves it over the [target square](Target_Square "Target Square") to reinsert it into the board again.

- [](File:ElAjedrecistaActuator.jpg)

Actuator principle ...

- [](File:ElAjedrecistaActuatorDisc.jpg)

and photo detail <a id="cite-note-18" href="#cite-ref-18">[18]</a>

- [](File:ElAjedrecistaBoardAndArms.jpg)

Board with sliding arms

## See also

- [History of Computer Chess](History "History")
- [Mate-in-two](Mate-in-two "Mate-in-two") by [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz")
- [Nemes' Chess Machine](Tiham%C3%A9r_Nemes#Machine "Tihamér Nemes") by [Tihamér Nemes](Tiham%C3%A9r_Nemes "Tihamér Nemes")

## Publications

- [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") (**1914**). *Les Automates*. [La Nature](https://en.wikipedia.org/wiki/La_Nature), [pdf](http://cyberneticzoo.com/wp-content/uploads/2011/01/Automates-La-Nature-Torres-1914.pdf) from [cyberneticzoo.com](http://cyberneticzoo.com/), Translation by [David Levy](David_Levy "David Levy") as *Robots* in [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *All About Chess and Computers*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), pp. 14-23, also in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, pp. 273-278.
- Anonymmous (**1915**). *Torre and His Remarkable Automatic Devices*. [Scientific American](Scientific_American "Scientific American"), [Supplement 80, Number 2079, November 06, 1915](http://books.google.co.uk/books?id=XwUiAQAAMAAJ&pg=PA296&dq=%22Torres+and+his+remarkable+automatic+devices%22&hl=en&ei=oBhxTvGkNrS80AHrxoysCg&sa=X&oi=book_result&ct=result&redir_esc=y#v=onepage&q=%22Torres%20and%20his%20remarkable%20automatic%20devices%22&f=false)
- [Donald Michie](Donald_Michie "Donald Michie") (**1977**). *King and Rook Against King: Historical Background and a Problem on the Infinite Board*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
- [James M. Williams](http://www.devili.iki.fi/library/author/1504.en.html) (**1978**). *[Antique Mechanical Computers, Part 3: The Torres Chess Automation](https://archive.org/stream/byte-magazine-1978-09/1978_09_BYTE_03-09_Graphic_Manipulations#page/n83/mode/2up)*. [BYTE, Vol. 3, No. 9](Byte_Magazine#BYTE309 "Byte Magazine")
- [David Levy](David_Levy "David Levy") (**1982**). *Robots*. Translation of [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") (**1914**). *Les Automates*. in [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *All About Chess and Computers*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), also in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, pp. 273-278. [pdf](http://cyberneticzoo.com/wp-content/uploads/2011/01/Levy-Torres-Vigneron-Translation.pdf) from [cyberneticzoo.com](http://cyberneticzoo.com/)
- [Brian Randell](https://en.wikipedia.org/wiki/Brian_Randell) (**1982**). *From Analytical Engine to Electronic Digital Computer: The Contributions of Ludgate, Torres, and Bush*. [Annals of the History of Computing](https://en.wikipedia.org/wiki/IEEE_Annals_of_the_History_of_Computing), Vol. 4, No. 4, October 1982, [pdf](http://www.cs.ncl.ac.uk/publications/articles/papers/398.pdf) <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a>
- [Ulrich Thiemonds](Ulrich_Thiemonds "Ulrich Thiemonds") (**1999**). *Ein regelbasiertes Spielprogramm für Schachendspiele*. [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn), Diplom thesis, [pdf](https://www.idb.uni-bonn.de/publications/da/da_thiemonds_1999.pdf), pp 34-36 "Historischer" Ansatz von Torres y Quevedo" (German)

## Forum Posts

- ["El Ajedristica" Programming Challenge](http://www.stmintz.com/ccc/index.php?id=422897) by Ricardo Gibert, [CCC](CCC "CCC"), April 25, 2005
- [One hundred years ago, the first chess computer](http://www.talkchess.com/forum/viewtopic.php?t=41801) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 05, 2012
- [Re: Programmer wanted to write chess game for an exhibition](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490496&t=45840) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 04, 2012 (El Ajedrecista algorithm)
- [chess-playing automaton , circa 1914](http://www.talkchess.com/forum/viewtopic.php?t=51226) by Tom Glenn, [CCC](CCC "CCC"), February 10, 2014

## External Links

- [El Ajedrecista from Wikipedia](https://en.wikipedia.org/wiki/El_Ajedrecista)
- [El Ajedrecista from Wikipedia.es](https://es.wikipedia.org/wiki/El_Ajedrecista) (Spanish)
- [Universidad Politécnica de Madrid - Museo "Torres Quevedo"](http://www.upm.es/institucional/UPM/MuseosUPM/MuseoTorresQuevedo)
- [The first chess computer](http://www.chesshistory.com/winter/winter24.html#4470._The_first_chess_computer) Chess Notes Archive by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29) (note 4470, 4482)
- [The first chess computer](http://www.chesshistory.com/winter/winter25.html#4525._The_first_chess_computer_C.N.s) Chess Notes Archive by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29) (note 4525, 4547)
- [1911 El Ajedrecista](https://sites.google.com/site/caroluschess/chess-computers/1911-el-ajedrecista) from [Carolus Chess](https://sites.google.com/site/caroluschess/home)
- [1911-20 - Chess Playing Machines - Leonardo Torres y Quevedo](http://cyberneticzoo.com/not-quite-robots/1911-20-chess-playing-machines-leonardo-torres-y-quevedo-spanish/) from [cyberneticzoo.com](http://cyberneticzoo.com/)
- [History of Computers and Computing, Automata, Leonardo Torres's chess-machine](http://history-computer.com/Dreamers/Torres_chess.html)
- [Cyber Heroes of the past: Leonardo Torres y Quevedo](http://wvegter.hivemind.net/abacus/CyberHeroes/Quevedo.htm)
- [Mechanical Chess Opponent | Modern Mechanix](http://blog.modernmechanix.com/mechanical-chess-opponent/)
- [Spain, September 6, 1955 - Leonardo Torres Quevedo: inventor of the first chess machine El Ajedrecista in 1911](http://www.tri.org.au/chess/Spain55.html)
- [Imágenes del Autómata ajedrecista](http://www.torresquevedo.org/LTQ10/index.php?title=Im%C3%A1genes_del_Aut%C3%B3mata_ajedrecista) - [Torres Quevedo](http://www.torresquevedo.org/LTQ10/index.php?title=Portada) (Spanish)
- [Die Schachautomaten des Torres Quevedo](http://www.schachklub-tempelhof.de/?q=quevedo) by [Hans-Peter Ketterling](index.php?title=Hans-Peter_Ketterling&action=edit&redlink=1 "Hans-Peter Ketterling (page does not exist)"), [Schachklub Tempelhof](http://www.schachklub-tempelhof.de.vu/) (German)
- [Computer Schach](http://www.andreadrian.de/schach/) by [Andre Adrian](Andre_Adrian "Andre Adrian"), see Torres y Quevedo, Endspielautomat (German)
- [The Rook Endgame Machine of Torres y Quevedo](http://en.chessbase.com/post/torres-y-quevedo-s-rook-endgame-automaton) by Ramón Jiménez, [ChessBase](ChessBase "ChessBase"), July 20, 2004
- ["El Ajedrecista" - an analog chess-playing computer from 1912](http://www.collisiondetection.net/mt/archives/2011/09/el_ajedrecista.php), September 14, 2011 <a id="cite-note-22" href="#cite-ref-22">[22]</a>
- [Chess and the Automaton Endgame](http://www.engadget.com/2014/02/09/torres-quevedo-chess-player-automaton/) by [Jon Turi](http://www.engadget.com/about/editors/jon-turi/), February 9th, 2014 <a id="cite-note-23" href="#cite-ref-23">[23]</a>
- Leonardo Torres Quevedo Chess Automaton 1951, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A New Photograph of “El jugador ajedrecista,” the World’s First Chess Computer by Nathan Bauman, July 16th, 2006
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The first chess computer](http://www.chesshistory.com/winter/winter25.html#4525._The_first_chess_computer_C.N.s) Chess Notes Archive by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29) (note 4525, 4547)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [David Levy](David_Levy "David Levy") in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), Special Purpose Software and Hardware, pp. 266
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [David Mindell](http://mindell.scripts.mit.edu/homepage/), [Jérôme Segal](http://jerome-segal.de/acc-en.htm), [Slava Gerovitch](http://web.mit.edu/slava/homepage/) (**2003**). *[Cybernetics and Information Theory in the United States, France and the Soviet Union](https://www.infoamerica.org/documentos_word/shannon-wiener.htm)*. in [Mark Walker](<https://de.wikipedia.org/wiki/Mark_Walker_(Wissenschaftshistoriker)>) (ed.) (**2003**). *[Science and Ideology: A Comparative History](https://www.crcpress.com/Science-and-Ideology-A-Comparative-History/Walker/p/book/9780415279994)*. [Routledge](https://en.wikipedia.org/wiki/Routledge) » [Claude Shannon](Claude_Shannon "Claude Shannon"), [Norbert Wiener](Norbert_Wiener "Norbert Wiener"), covers the 1951 Paris Cybernetic Congress
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Universidad Politécnica de Madrid - Museo "Torres Quevedo"](http://www.upm.es/institucional/UPM/MuseosUPM/MuseoTorresQuevedo) (Spanish)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1992**). *The 7th World Computer-Chess Championship. Report on the Tournament*. [ICCA Journal, Vol. 15, No. 4](ICGA_Journal#15_4 "ICGA Journal")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Fotografía del primer ajedrecista. Del libro Obra e Inventos de Torres Quevedo. José García Santesmases. Editado en 1980 por el Instituto de España en la "Colección Cultura y Cienci](https://www.torresquevedo.org/LTQ10/index.php?title=Archivo:PrimerAjedrecista.jpg), [Imágenes del Autómata ajedrecista](http://www.torresquevedo.org/LTQ10/index.php?title=Im%C3%A1genes_del_Aut%C3%B3mata_ajedrecista) - [Torres Quevedo](http://www.torresquevedo.org/LTQ10/index.php?title=Portada) (Spanish)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [James M. Williams](http://www.devili.iki.fi/library/author/1504.en.html) (**1978**). *[Antique Mechanical Computers, Part 3: The Torres Chess Automation](https://archive.org/stream/byte-magazine-1978-09/1978_09_BYTE_03-09_Graphic_Manipulations#page/n83/mode/2up)*. [BYTE, Vol. 3, No. 9](Byte_Magazine#BYTE309 "Byte Magazine")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> A New Photograph of “El jugador ajedrecista,” the World’s First Chess Computer by Nathan Bauman, July 16th, 2006
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [David Mindell](http://mindell.scripts.mit.edu/homepage/), [Jérôme Segal](http://jerome-segal.de/), [Slava Gerovitch](http://web.mit.edu/slava/homepage/) (**2003**). *[Cybernetics and Information Theory in the United States, France and the Soviet Union](http://www.infoamerica.org/documentos_word/shannon-wiener.htm)*. in [Mark Walker](https://de.wikipedia.org/wiki/Mark_Walker), [Science and Ideology](http://books.google.com/books/about/Science_and_Ideology.html?id=0Nz7Gs-C-9MC&redir_esc=y): A Comparative History » [Claude Shannon](Claude_Shannon "Claude Shannon"), [Norbert Wiener](Norbert_Wiener "Norbert Wiener"), covers the 1951 Paris Cybernetic Congress
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Antonio Pérez Yuste](https://en.wikipedia.org/wiki/Antonio_P%C3%A9rez_Yuste), [Magdalena Salazar Palma](http://www.ieeeaps.org/offandadcom.html) (**2004**). *The First Wireless Remote-Control: The Telekine of Torres Quevedo*. [pdf](http://www.torresquevedo.org/LTQ10/images/Yuste.pdf)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Cyber Heroes of the past: Leonardo Torres y Quevedo](http://wvegter.hivemind.net/abacus/CyberHeroes/Quevedo.htm)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Torres-Quevedo Museum of Engineering - Early Developments in Remote-Control, 1901 - The Telekine](http://www.torresquevedo.org/LTQ10/images/TelekinoMilestone2007.pdf) (pdf, Spanish/English) [Escuela Técnica Superior de Ingenieros de Caminos, Canales y Puertos](http://www.caminos.upm.es/) (Institute of Civil Engineering) - [Universidad Politécnica de Madrid](Technical_University_of_Madrid "Technical University of Madrid")
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [José Luis López Aranguren](http://es.wikipedia.org/wiki/Jos%C3%A9_Luis_L%C3%B3pez_Aranguren), [Complutense University of Madrid](https://en.wikipedia.org/wiki/Complutense_University_of_Madrid)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") (**1914**). *Les Automates*. [La Nature](https://en.wikipedia.org/wiki/La_Nature), [pdf](http://cyberneticzoo.com/wp-content/uploads/2011/01/Automates-La-Nature-Torres-1914.pdf) from [cyberneticzoo.com](http://cyberneticzoo.com/), Translation by [David Levy](David_Levy "David Levy") as *Robots* in [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *All About Chess and Computers*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), pp. 14-23, also in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, pp. 273-278.
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") (**1914**). *Les Automates*. [La Nature](https://en.wikipedia.org/wiki/La_Nature), image pp. 61, [pdf](http://cyberneticzoo.com/wp-content/uploads/2011/01/Automates-La-Nature-Torres-1914.pdf) from [cyberneticzoo.com](http://cyberneticzoo.com/)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Mechanical movements - Movement (clockwork) from Wikipedia](https://en.wikipedia.org/wiki/Movement_%28clockwork%29#Mechanical_movements)
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> Detail photos cropped from A New Photograph of “El jugador ajedrecista,” the World’s First Chess Computer by Nathan Bauman, July 16th, 2006
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Analytical Engine from Wikipedia](https://en.wikipedia.org/wiki/Analytical_Engine)
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Percy Ludgate from Wikipedia](https://en.wikipedia.org/wiki/Percy_Ludgate)
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Vannevar Bush](Mathematician#VannevarBush "Mathematician")
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> El Ajedrecista deals with discrete states and should not considered as [analog computer](https://en.wikipedia.org/wiki/Analog_computer)
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [chess-playing automaton , circa 1914](http://www.talkchess.com/forum/viewtopic.php?t=51226) by Tom Glenn, [CCC](CCC "CCC"), February 10, 2014

**[Up one level](History "History")**

