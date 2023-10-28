---
title: 3D Graphics Board
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Graphics Programming](Graphics_Programming "Graphics Programming") * 3D Graphics Board**

\[ A [rendered](https://en.wikipedia.org/wiki/3D_rendering) [3D animation](https://en.wikipedia.org/wiki/Computer_animation) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**3D Graphics Board**,

a [3D graphics](https://en.wikipedia.org/wiki/3D_computer_graphics) [projection](https://en.wikipedia.org/wiki/3D_projection) of a [3D model](https://en.wikipedia.org/wiki/3D_modeling) of a [chessboard](Chessboard "Chessboard") and the [pieces](Pieces "Pieces") of a [chess position](Chess_Position "Chess Position") to the two dimensional surface of a [computer display](https://en.wikipedia.org/wiki/Computer_monitor), either as [fullscreen](https://en.wikipedia.org/wiki/Fullscreen) or [board window](GUI#BoardWindow "GUI") of a chess [GUI](GUI "GUI"), or [printer](https://en.wikipedia.org/wiki/Printer_%28computing%29). For simplicity, some programs or 3D capable GUIs combine [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) for drawing the board with [raster graphics](https://en.wikipedia.org/wiki/Raster_graphics) for drawing the pieces. A [perspective center projection](https://en.wikipedia.org/wiki/3D_projection#Perspective_projection) applies for the board, where farther square [trapezoids](https://en.wikipedia.org/wiki/Trapezoid) are [scaled](https://en.wikipedia.org/wiki/Image_scaling) smaller, while a [orthographic projection](https://en.wikipedia.org/wiki/Orthographic_projection) applies for the pieces, i.e. drawing fixed sized piece-bitmaps with 3D-effect. More sophisticated implementations use 3D vector graphics in the [wire-frame model](https://en.wikipedia.org/wiki/Wire-frame_model) for the projection, and 2D raster graphics in the [rendered](https://en.wikipedia.org/wiki/3D_rendering) display, and feature a variable camera's position, [angle of view](https://en.wikipedia.org/wiki/Angle_of_view), [field of view](https://en.wikipedia.org/wiki/Field_of_view), may [rotate](https://en.wikipedia.org/wiki/Rotation) the object around various axis, apply [ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29) with one or more [light sources](https://en.wikipedia.org/wiki/Light#Light_sources) for [photorealistic](https://en.wikipedia.org/wiki/Photorealism) [shading](https://en.wikipedia.org/wiki/Shading) with [shadow](https://en.wikipedia.org/wiki/Shadow) and [reflection](https://en.wikipedia.org/wiki/Reflection_%28computer_graphics%29) effects, and perform more or less sophisticated [animations](https://en.wikipedia.org/wiki/Computer_animation) of piece movements.

A full perspective projected 3D board requires additional hardware and software resources, such as sophisticated [graphic cards](https://en.wikipedia.org/wiki/Video_card) with [GPUs](GPU "GPU") and 3D graphic libraries or frameworks like [OpenGL](https://en.wikipedia.org/wiki/OpenGL) or [Direct3D](https://en.wikipedia.org/wiki/Microsoft_Direct3D) as subset of the [DirectX](https://en.wikipedia.org/wiki/DirectX) collection.

## Contents

- [1 Ergonomics](#ergonomics)
- [2 Screenshots & Images](#screenshots-.26-images)
  - [2.1 Early 3D Boards](#early-3d-boards)
  - [2.2 Chessmaster](#chessmaster)
  - [2.3 ChessPartner](#chesspartner)
  - [2.4 KnightCap](#knightcap)
  - [2.5 Nemeton](#nemeton)
  - [2.6 Uragano 3D](#uragano-3d)
- [3 See also](#see-also)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
  - [6.1 Basics](#basics)
  - [6.2 Projection](#projection)
  - [6.3 3D Graphics API and Frameworks](#3d-graphics-api-and-frameworks)
  - [6.4 3D-Editors](#3d-editors)
  - [6.5 Tutorials](#tutorials)
  - [6.6 3D Chess](#3d-chess)
    - [6.6.1 Chessmaster](#chessmaster-2)
    - [6.6.2 Fritz GUI](#fritz-gui)
- [7 References](#references)

## Ergonomics

Despite the more challenging task for the GUI or graphics programmer and progress to simulate the view on a real chessboard, the 3D Board is usually harder to grasp for a human chess player than good [2D Boards](2D_Graphics_Board "2D Graphics Board"). Pieces and specially pawns are often partly covered by pieces in front, and movement of head and eyes of the chess player lack the same visual feedback as looking on a real chess board. Therefor 3D Boards are often featured in mass market products and some programs where authors are interested in 3D graphics programming. The really sophisticated 3D boards of [Chessmaster](Chessmaster "Chessmaster") and [Fritz](Fritz "Fritz") are eye catchers and rich of features, but rarely used for serious playing.

## Screenshots & Images

## Early 3D Boards

|  |  |
| --- | --- |
| [Colossus Chess 4 C64 3D.png](https://en.wikipedia.org/wiki/Colossus_Chess) | [CyrusII.gif](http://www.worldofspectrum.org/infoseekid.cgi?id=0001213) |
| [Colossus Chess 4.0](Colossus_Chess "Colossus Chess") 3D chessboard <a id="cite-note-2" href="#cite-ref-2">[2]</a> | [Cyrus II](Cyrus "Cyrus") 3D screen <a id="cite-note-3" href="#cite-ref-3">[3]</a> |

## [Chessmaster](Chessmaster "Chessmaster")

[](http://chessmaster.de.ubi.com/xi/pcScreens.php)
[Chessmaster XI](Chessmaster "Chessmaster") - House of Staunton chess sets <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [ChessPartner](ChessPartner "ChessPartner")

[](http://www.lokasoft.nl/chesspartner.aspx)
[ChessPartner 6](ChessPartner "ChessPartner"), 3D pieces <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [KnightCap](KnightCap "KnightCap")

[](http://www.samba.org/KnightCap/)
KnightCap's 3D Board <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## [Nemeton](Nemeton "Nemeton")

[](http://www.talkchess.com/forum/viewtopic.php?t=64177)
[Nemeton3D](Nemeton "Nemeton") 1.51 with its 3D Graphics Board <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## [Uragano 3D](Uragano "Uragano")

[](http://www.naddei.it/uragano_3d/)
[Uragano 3D](Uragano "Uragano") board <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## See also

- [2D Graphics Board](2D_Graphics_Board "2D Graphics Board")
- [GPU](GPU "GPU")
- [Kasparov versus X3D Fritz 2003](Kasparov_versus_X3D_Fritz_2003 "Kasparov versus X3D Fritz 2003")

## Publications

- [Nina Amenta](http://www.cs.ucdavis.edu/%7Eamenta/), [Yong Joo Kil](http://graphics.cs.ucdavis.edu/%7Eyjkil/) (**2005**). *[Defining Point-Set Surfaces](http://graphics.cs.ucdavis.edu/%7Eyjkil/pub/defining.html)*. [pdf](http://graphics.stanford.edu/courses/cs468-05-winter/Papers/PCD/amenta_PCD.pdf) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**2006**). *[Computergrafik](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/skript.html)*. [pdf](http://www-lehre.inf.uos.de/%7Ecg/2006/PDF/skript.pdf) (German)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") and [Kang Zhang](http://www.utdallas.edu/%7Ekzhang/) (**2007**). *[Computer Graphics for Java Programmers, 2nd Edition](http://home.planet.nl/%7Eammeraal/grjava2e.html)*, ISBN-13: 978-0-470-03160-5 / ISBN-10: 0-470-03160-3 by [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)
- [Eric Lengye](https://en.wikipedia.org/wiki/Eric_Lengyel) (**2011**). *[Mathematics for 3D Game Programming and Computer Graphics, Third Edition](http://www.mathfor3dgameprogramming.com/)*. ISBN-13: 978-1435458864, [amazon.com](http://www.amazon.com/exec/obidos/tg/detail/-/1435458869)

## Forum Posts

- [Re: Going commercial, maybe](https://groups.google.com/group/rec.games.chess.computer/msg/ded7e4e4304d8d4e) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 9, 1997 » [KnightCap](KnightCap "KnightCap")

## External Links

## Basics

- [3D from Wikipedia](https://en.wikipedia.org/wiki/3D)
- [3D computer graphics from Wikipedia](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [3D display from Wikipedia](https://en.wikipedia.org/wiki/3D_display)
- [3D modeling from Wikipedia](https://en.wikipedia.org/wiki/3D_modeling)
- [Introduction to 3-D Modeling](http://dsearls.org/courses/C122CompSci/Graphics/IntroModeling.htm) by [Delmar E. Searls](http://www.asbury.edu/academics/departments/mathematics/faculty-staff/delmar-searls)
- [3D rendering from Wikipedia](https://en.wikipedia.org/wiki/3D_rendering)
- [Camera matrix from Wikipedia](https://en.wikipedia.org/wiki/Camera_matrix)
- [Homography from Wikipedia](https://en.wikipedia.org/wiki/Homography)
- [Perspective (graphical) from Wikipedia](https://en.wikipedia.org/wiki/Perspective_%28graphical%29)
- [Polygon mesh from Wikipedia](https://en.wikipedia.org/wiki/Polygon_mesh)
- [Ray tracing (graphics) from Wikipedia](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29)
- [Raytracing](https://www.ads.tuwien.ac.at/research/Raytracing.html) by [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (German)
- [Rendering (computer graphics)](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29)

[Artistic rendering](https://en.wikipedia.org/wiki/Artistic_rendering)
[Rendering equation](https://en.wikipedia.org/wiki/Rendering_equation)
[Non-photorealistic rendering](https://en.wikipedia.org/wiki/Non-photorealistic_rendering)

- [Stereoscopy from Wikipedia](https://en.wikipedia.org/wiki/Stereoscopy)
- [Texture mapping from Wikipedia](https://en.wikipedia.org/wiki/Texture_mapping)
- [Three-dimensional space from Wikipedia](https://en.wikipedia.org/wiki/Three-dimensional_space)
- [Wire-frame model from Wikipedia](https://en.wikipedia.org/wiki/Wire-frame_model)

## Projection

- [3D projection from Wikipedia](https://en.wikipedia.org/wiki/3D_projection)
- [Graphical projection from Wikipedia](https://en.wikipedia.org/https://en.wikipedia.org/wiki/Graphical_projection)
- [Projection (linear algebra) from Wikipedia](https://en.wikipedia.org/wiki/Projection_%28linear_algebra%29)
- [Axonometric projection from Wikipedia](https://en.wikipedia.org/wiki/Axonometric_projection)
- [Isometric projection from Wikipedia](https://en.wikipedia.org/wiki/Isometric_projection)
- [Oblique projection from Wikipedia](https://en.wikipedia.org/wiki/Oblique_projection)
- [Orthographic projection from Wikipedia](https://en.wikipedia.org/wiki/Orthographic_projection)
- [Parallel projection from Wikipedia](https://en.wikipedia.org/wiki/Parallel_projection)
- [Planar projection from Wikipedia](https://en.wikipedia.org/wiki/Planar_projection)

## 3D Graphics API and Frameworks

- [OpenGL from Wikipedia](https://en.wikipedia.org/wiki/OpenGL)

[Mesa (computer graphics)](https://en.wikipedia.org/wiki/Mesa_%28computer_graphics%29)
[Lightweight Java Game Library](https://en.wikipedia.org/wiki/Lightweight_Java_Game_Library)

- [Java 3D from Wikipedia](https://en.wikipedia.org/wiki/Java_3D)
- [Microsoft Direct3D from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Direct3D)
- [VRML from Wikipedia](https://en.wikipedia.org/wiki/VRML)
- [X3D from Wikipedia](https://en.wikipedia.org/wiki/X3D)
- [X3D for Developers](http://www.web3d.org/x3d/) from [Web3D Consortium | Open Standards for Real-Time 3D Communication](http://www.web3d.org/)

## 3D-Editors

- [Ardor3D from Wikipedia](https://en.wikipedia.org/wiki/Ardor3D)
- [Autodesk 3ds Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max)
- [MeshLab from Wikipedia](https://en.wikipedia.org/wiki/MeshLab)

[MeshLab](http://meshlab.sourceforge.net/)

- [Blender (software) from Wikipedia](https://en.wikipedia.org/wiki/Blender_%28software%29)

[Blender 3D: MemoBook - Wikibooks](http://en.wikibooks.org/wiki/Blender_3D:_MemoBook)

- [Code archives/3D Graphics - Mesh/3D chessboard](http://www.blitzbasic.com/codearcs/codearcs.php?code=1964) Rotational solids editor using example by [Matt Merkulov](http://ru-ru.facebook.com/MattMerkulov), March 15, 2007 » [Blitz BASIC](https://en.wikipedia.org/wiki/Blitz_BASIC)
- [Pointshop3D](http://graphics.ethz.ch/pointshop3d/) developed at the Computer Graphics Lab at [ETH Zurich](ETH_Zurich "ETH Zurich")
- [ShiVa from Wikipedia](https://en.wikipedia.org/wiki/ShiVa)

## Tutorials

- [Chess set modeling tutorial « Tutorial-z.com](http://tutorial-z.com/chess-set-modeling-tutorial/)
- [Blender Magician: Model a Chess Piece](http://blendermagician.blogspot.de/2012/04/model-chess-piece.html) requires [blender](https://en.wikipedia.org/wiki/Blender_%28software%29) and [gimp](https://en.wikipedia.org/wiki/GIMP)
- [How to draw a chessboard with central perspective](http://www.slideshare.net/Sweedie/chessboard) from [SlideShare](https://en.wikipedia.org/wiki/SlideShare)

## 3D Chess

- [3D chess computing for browser « Chessforeva's Blog](http://chessforeva.wordpress.com/2010/06/26/3d-chess-computing-for-browser/)
- [Chessforeva online 3D chess game in browser](http://chessforeva.appspot.com/)
- [Chessforeva for Web developments](http://chessforeva.blogspot.de/2009/06/chessforeva-for-web-developments.html)
- [Chessforeva 3D chess - play with Lokasoft java chess engine](http://chessforeva.appspot.com/C0_Loka.htm) » [Lokasoft](Lokasoft "Lokasoft")
- [Chessforeva: 3D chess diagram from FEN](http://chessforeva.blogspot.de/2009/10/3d-chess-diagram-from-fen.html) » [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- [chessboard3.js](http://jtiscione.github.io/chessboard3js/play.html) [JavaScript](JavaScript "JavaScript") [GUI](GUI "GUI") by [Jason Tiscione](index.php?title=Jason_Tiscione&action=edit&redlink=1 "Jason Tiscione (page does not exist)")

### [Chessmaster](Chessmaster "Chessmaster")

- [Chessmaster 10th Edition - PC Review at IGN](http://pc.ign.com/articles/542/542613p1.html) by [Steve Butts](http://stars.ign.com/objects/142/14245913.html), August 26, 2004

### [Fritz GUI](Fritz#GUI "Fritz")

- [Fritz Help - Board design – 3D](http://help.chessbase.com/Fritz/16/Eng/index.html?board_3d.htm)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image selfmade with [Blender](https://en.wikipedia.org/wiki/Blender_%28software%29), Author: [J.A. Freyre](https://en.wikipedia.org/wiki/User:Jfreyre), January 22 2006, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Colossus Chess from Wikipedia](https://en.wikipedia.org/wiki/Colossus_Chess)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Cyrus II - World of Spectrum](http://www.worldofspectrum.org/infoseekid.cgi?id=0001213)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [PC-Screenshots | Chessmaster XI: The Art of Learning](http://chessmaster.de.ubi.com/xi/pcScreens.php) | [Ubisoft](index.php?title=Ubisoft&action=edit&redlink=1 "Ubisoft (page does not exist)")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ChessPartner Screen shots | ChessPartner - Lokasoft - Home of ChessPartner](http://www.lokasoft.nl/chesspartner.aspx)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Welcome to the KnightCap home page](http://samba.anu.edu.au/KnightCap/)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Going commercial, maybe](https://groups.google.com/group/rec.games.chess.computer/msg/ded7e4e4304d8d4e) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 9, 1997
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Nemeton3D 1.51](http://www.talkchess.com/forum/viewtopic.php?t=64177) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), June 04, 2017
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Home page Uragano 3D](http://www.naddei.it/uragano_3d/)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Pointshop3D](http://graphics.ethz.ch/pointshop3d/) developed at the Computer Graphics Lab at [ETH Zurich](ETH_Zurich "ETH Zurich")

**[Up one Level](Graphics_Programming "Graphics Programming")**

