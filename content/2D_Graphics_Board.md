---
title: 2D Graphics Board
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Graphics Programming](Graphics_Programming "Graphics Programming") * 2D Graphics Board**

[](File:Machackdisplay02.jpg) Mac Hack [display](Lawrence_J._Krakauer#DEC340 "Lawrence J. Krakauer") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>
**2D Graphics Board**,

a [2D graphics](https://en.wikipedia.org/wiki/2D_computer_graphics) image of a [chessboard](Chessboard "Chessboard") and the [pieces](Pieces "Pieces") of a [chess position](Chess_Position "Chess Position") on a [computer display](https://en.wikipedia.org/wiki/Computer_monitor), either [fullscreen](https://en.wikipedia.org/wiki/Fullscreen) or [board window](GUI#BoardWindow "GUI") of a chess [GUI](GUI "GUI"), or [printer](https://en.wikipedia.org/wiki/Printer_%28computing%29), similar to a [chess diagram](index.php?title=Chess_Diagrams&action=edit&redlink=1 "Chess Diagrams (page does not exist)") in print media. A 2D board window should be [isotropic](https://en.wikipedia.org/wiki/Isotropy) and quadratic, with all squares of same size.

## Screenshots

## [GNU Chess](GNU_Chess "GNU Chess")

\[
[GNU Chess](GNU_Chess "GNU Chess") on [XBoard](XBoard "XBoard") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [MChess](MChess "MChess")

[](http://www.schachcomputer.info/forum/showthread.php?t=3531)
[M-Chess Pro 3.5](MChess "MChess") (1993) <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [IsiChess](IsiChess "IsiChess")

[](File:IsiChess.jpg)
[IsiChess](IsiChess "IsiChess") 2D board with [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics)

## Drawing Pieces

## 2D Vector Graphics

|  |  |
| --- | --- |
| [IsiKnight.JPG](File:IsiKnight.JPG) |  The [C++](Cpp "Cpp") code is based on the [Windows](Windows "Windows") [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library), a class extension of the [Device Context](https://en.wikipedia.org/wiki/Graphics_Device_Interface#Technical_details) of the [Graphics Device Interface](https://en.wikipedia.org/wiki/Graphics_Device_Interface) <a id="cite-note-6" href="#cite-ref-6">[6]</a> , in conjunction with "handmade" [polygons](https://en.wikipedia.org/wiki/Polygon) with coordinates in a x- and y-range of ±16 (positive values right and down), is used in [IsiChess](IsiChess "IsiChess") to apply [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) to draw the [pieces](Pieces "Pieces") in the [board window](GUI#BoardWindow "GUI") or as [figurine notation](Algebraic_Chess_Notation#FAN "Algebraic Chess Notation"). For each piece an array of connected lines is declared, the first one a closed polygon, which is filled by the piece color <a id="cite-note-7" href="#cite-ref-7">[7]</a> :
|

```C++

/* Piece Coordinates */
static POINT KnightPoint0[] = {
   { 10, 12},{ 11,  2},{ 10, -3},{  8, -6},
   {  6, -8},{  4, -9},{  1,-11},{  0,-12},
   { -1,-11},{ -2,-11},{ -3,-12},{ -3,-10},
   { -5, -8},{ -6, -6},{ -8,  0},{-10,  2},
   {-10,  4},{ -8,  6},{ -6,  5},{ -5,  4},
   { -4,  2},{ -2,  1},{ -1,  0},{  0, -2},
   { -1,  0},{ -1,  2},{ -2,  4},{ -6,  8},
   { -8, 12},{ 10, 12}
};

static POINT KnightPoint1[] = { { -3, -7},{ -4, -6} };
static POINT KnightPoint2[] = { { -8,  2},{ -9,  3} };

static POINT BishopPoint0[] = {
...

struct PIECEPOLY {
   unsigned int nPoints;
   const POINT *Points;
};

static PIECEPOLY KnightPoly[] = {
   {sizeof (KnightPoint0) / sizeof (KnightPoint0[0]), KnightPoint0},
   {sizeof (KnightPoint1) / sizeof (KnightPoint1[0]), KnightPoint1},
   {sizeof (KnightPoint2) / sizeof (KnightPoint2[0]), KnightPoint2}
};
...

struct PIECEIMAGE {
   int nPolys;
   PIECEPOLY *Poly;
};

static PIECEIMAGE PieceImage[] = {
   {0,  NULL},
   {sizeof (PawnPoly)   / sizeof (PawnPoly  [0]),  PawnPoly},
   {sizeof (BishopPoly) / sizeof (BishopPoly[0]),  BishopPoly},
   {sizeof (KnightPoly) / sizeof (KnightPoly[0]),  KnightPoly},
   {sizeof (RookPoly)   / sizeof (RookPoly  [0]),  RookPoly},
   {sizeof (KingPoly)   / sizeof (KingPoly  [0]),  KingPoly},
   {sizeof (QueenPoly)  / sizeof (QueenPoly [0]),  QueenPoly},
   {0,  NULL},
};

/* Drawing implemented as extension of Windows MFC Device Context Class CDC */
void CIsiDC::drawPiece(const CRect &r, int piece) {
   drawPiece(r, piece, m_sPieceColor[piece&1], m_sPieceBorderColor[piece&1]);
}

void CIsiDC::drawPiece(const CRect &r, int piece, COLORREF piececolor, COLORREF pencolor) {
   CPen pen(PS_SOLID, 1, pencolor);
   CBrush brush(piececolor);
   CPen* pOldPen = SelectObject(&pen);
   CBrush* pOldBrush = SelectObject(&brush);

   PIECEIMAGE *pim = PieceImage + (piece >> 1);
   int i; PIECEPOLY  *p;
   for (i=0, p = pim->Poly; i < pim->nPolys; ++i, ++p) {
      POINT points[64];
      transformPoints (points, p->Points, p->nPoints, r);
      if (i == 0) { /* closed polygon */
         BeginPath();
         Polyline(points, p->nPoints);
         EndPath();
         FillPath();
      }
      Polyline(points, p->nPoints);
   }
   SelectObject(pOldBrush);
   SelectObject(pOldPen);
}

void CIsiDC::transformPoints (POINT* target, const POINT* source, int nPoints, const CRect &r) {
   int width = r.Width();
   int height = r.Height();
   CPoint center = r.CenterPoint();
   while (nPoints--)
      *target++ = transfrom (*source++, width, height, 32, center);
}

POINT CIsiDC::transfrom (const POINT &c, int scalx, int scaly, int qxy, const POINT &trans) {
   return CPoint((c.x*scalx)/qxy, (c.y*scaly)/qxy) + trans;
}

```

## Bitmaps

A more common way is to display pieces in form of [bitmaps](https://en.wikipedia.org/wiki/Bitmap) or pixmaps, small images of pieces, painted with an external program such as [GIMP](https://en.wikipedia.org/wiki/GIMP), [Paint](https://en.wikipedia.org/wiki/Paint_%28software%29) etc., stored as [Raster graphics](https://en.wikipedia.org/wiki/Raster_graphics) in an external file or resource format, such as [Portable Network Graphics](https://en.wikipedia.org/wiki/Portable_Network_Graphics) <a id="cite-note-8" href="#cite-ref-8">[8]</a> or [Windows](Windows "Windows") [BMP file format](https://en.wikipedia.org/wiki/BMP_file_format), which may be used in conjunction with [Bit blit](https://en.wikipedia.org/wiki/Bit_blit) for [scaling](https://en.wikipedia.org/wiki/Image_scaling).

## Unicode

An alternative technique for [drawing pieces](Pieces#Unicode "Pieces") is the use of [Symbols](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode#Chessboard_using_Unicode_symbols) in [Unicode](https://en.wikipedia.org/wiki/Unicode) as scalable [TrueType](https://en.wikipedia.org/wiki/TrueType)[fonts](https://en.wikipedia.org/wiki/Font) <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  8
| ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ |
|  7
| ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ |
|  6
|  |  |  |  |  |  |  |  |
|  5
|  |  |  |  |  |  |  |  |
|  4
|  |  |  |  |  |  |  |  |
|  3
|  |  |  |  |  |  |  |  |
|  2
| ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
|  1
| ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |
|  |  a
|  b
|  c
|  d
|  e
|  f
|  g
|  h
|

## See also

- [3D Graphics Board](3D_Graphics_Board "3D Graphics Board")
- [GPU](GPU "GPU")
- [Pieces](Pieces "Pieces")

## Publications

- [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**2006**). *[Computergrafik](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/skript.html)*. [pdf](http://www-lehre.inf.uos.de/%7Ecg/2006/PDF/skript.pdf) (German)
- [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal") and [Kang Zhang](http://www.utdallas.edu/%7Ekzhang/) (**2007**). *[Computer Graphics for Java Programmers, 2nd Edition](http://home.planet.nl/%7Eammeraal/grjava2e.html)*, ISBN-13: 978-0-470-03160-5 / ISBN-10: 0-470-03160-3 by [John Wiley](http://eu.wiley.com/WileyCDA/Section/id-300022.html)

## Forum Posts

- [Unicode values for chessmen](http://www.talkchess.com/forum/viewtopic.php?t=38318) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 07, 2011
- [Piece graphics](http://www.talkchess.com/forum/viewtopic.php?t=57995) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 19, 2015 » [XBoard](XBoard "XBoard")
- [MinGW AlphaBlend](http://www.talkchess.com/forum/viewtopic.php?t=62315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 29, 2016 » [WinBoard](WinBoard "WinBoard"), [Windows](Windows "Windows") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>

## External Links

- [2D computer graphics from Wikipedia](https://en.wikipedia.org/wiki/2D_computer_graphics)
- [Vector graphics from Wikipedia](https://en.wikipedia.org/wiki/Vector_graphics)
- [Raster graphics from Wikipedia](https://en.wikipedia.org/wiki/Raster_graphics)
- [GitHub - oakmac/chessboardjs: JavaScript chessboard](https://github.com/oakmac/chessboardjs)  » [JavaScript](JavaScript "JavaScript")

## [Coordinates](https://en.wikipedia.org/wiki/Coordinate_system)

- [Coordinate system from Wikipedia](https://en.wikipedia.org/wiki/Coordinate_system)

[Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system)
[Curvilinear coordinates](https://en.wikipedia.org/wiki/Curvilinear_coordinates)

- [Coordinate rotations and reflections from Wikipedia](https://en.wikipedia.org/wiki/Coordinate_rotations_and_reflections)
- [Euclidean space from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_space)
- [List of common coordinate transformations from Wikipedia](https://en.wikipedia.org/wiki/List_of_common_coordinate_transformations)
- [Orthogonal group from Wikipedia](https://en.wikipedia.org/wiki/Orthogonal_group)
- [Transformation (function) from Wikipedia](https://en.wikipedia.org/wiki/Transformation_%28function%29)

## [Reflection (mathematics)](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29) [Rotation (mathematics)](https://en.wikipedia.org/wiki/Rotation_%28mathematics%29) [Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) [Transformation matrix](https://en.wikipedia.org/wiki/Transformation_matrix) [Translation (geometry)](https://en.wikipedia.org/wiki/Translation_%28geometry%29) [Geometric primitives](https://en.wikipedia.org/wiki/Geometric_primitive)

- [Arc (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Arc_%28geometry%29)
- [B-spline from Wikipedia](https://en.wikipedia.org/wiki/B-spline)
- [Bit blit from Wikipedia](https://en.wikipedia.org/wiki/Bit_blit)
- [Bitmap from Wikipedia](https://en.wikipedia.org/wiki/Bitmap)
- [Bézier curve from Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [Circle from Wikipedia](https://en.wikipedia.org/wiki/Circle)
- [Ellipse from Wikipedia](https://en.wikipedia.org/wiki/Ellipse)
- [Line segment from Wikipedia](https://en.wikipedia.org/wiki/Line_segment)
- [Image scaling from Wikipedia](https://en.wikipedia.org/wiki/Image_scaling)
- [Pixel from Wikipedia](https://en.wikipedia.org/wiki/Pixel)
- [Plane (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Plane_%28geometry%29)
- [Polygon from Wikipedia](https://en.wikipedia.org/wiki/Polygon)
- [Polygonal chain from Wikipedia](https://en.wikipedia.org/wiki/Polygonal_chain)
- [Point (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Point_%28geometry%29)
- [Point in polygon from Wikipedia](https://en.wikipedia.org/wiki/Point_in_polygon)
- [Quadrilateral from Wikipedia](https://en.wikipedia.org/wiki/Quadrilateral)
- [Rectangle from Wikipedia](https://en.wikipedia.org/wiki/Rectangle)
- [Spline (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Spline_%28mathematics%29)

## Toolkits, Libraries and APIs

- [DirectX from Wikipedia](https://en.wikipedia.org/wiki/DirectX) » [Windows](Windows "Windows")

[Direct2D from Wikipedia](https://en.wikipedia.org/wiki/Direct2D)
[Direct3D from Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Direct3D)
[DirectDraw from Wikipedia](https://en.wikipedia.org/wiki/DirectDraw)
[DirectDraw Surface from Wikipedia](https://en.wikipedia.org/wiki/DirectDraw_Surface)

- [Fast Light Tool Kit (FLTK) from Wikipedia](https://en.wikipedia.org/wiki/FLTK)
- [GDK](https://en.wikipedia.org/wiki/GDK) / [XLib from Wikipedia](https://en.wikipedia.org/wiki/Xlib) » [Unix](Unix "Unix"), [Linux](Linux "Linux")
- [Graphics Device Interface from Wikipedia](https://en.wikipedia.org/wiki/Graphics_Device_Interface) (GDI) » [Windows](Windows "Windows")

[CDC Class - Device Context](http://msdn.microsoft.com/de-de/library/fxhhde73%28v=VS.100%29.aspx), [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library), [MSDN](https://en.wikipedia.org/wiki/Microsoft_Developer_Network)

- [GTK+ (GIMP Toolkit) from Wikipedia](https://en.wikipedia.org/wiki/GTK%2B)

[gtkmm from Wikipedia](https://en.wikipedia.org/wiki/Gtkmm)
[Gtk Sharp from Wikipedia](https://en.wikipedia.org/wiki/Gtk_Sharp)

- [Google Web Toolkit (GWT) from Wikipedia](https://en.wikipedia.org/wiki/Google_Web_Toolkit)

[lib-gwt-svg « vectomatic](http://www.vectomatic.org/libs/lib-gwt-svg)
[vectomatic - standard dynamic 2D graphics in web browsers - Google Project Hosting](https://code.google.com/p/vectomatic/)

- [List of widget toolkits from Wikipedia](https://en.wikipedia.org/wiki/List_of_widget_toolkits)
- [Motif (widget toolkit) from Wikipedia](https://en.wikipedia.org/wiki/Motif_%28widget_toolkit%29)
- [OpenGL from Wikipedia](https://en.wikipedia.org/wiki/OpenGL)

[Graphics Programming - Introduction to OpenGL](http://graphics.usc.edu/~suyay/class/Programming.pdf) (pdf)
[Comparison of OpenGL and Direct3D from Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_OpenGL_and_Direct3D)

- [Quartz from Wikipedia](https://en.wikipedia.org/wiki/Quartz_%28graphics_layer%29) » [OS X](Mac_OS "Mac OS")
- [QuickDraw from Wikipedia](https://en.wikipedia.org/wiki/QuickDraw) » [OS X](Mac_OS "Mac OS")
- [QT toolkit from Wikipedia](https://en.wikipedia.org/wiki/Qt_%28toolkit%29)
- [S3 Texture Compression from Wikipedia](https://en.wikipedia.org/wiki/S3_Texture_Compression)
- [Scalable Vector Graphics from Wikipedia](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)
- [Standard Widget Toolkit from Wikipedia](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit) » [Java](Java "Java")
- [Swing from Wikipedia](https://en.wikipedia.org/wiki/Swing_%28Java%29) » [Java](Java "Java")
- [Texture compression from Wikipedia](https://en.wikipedia.org/wiki/Texture_compression)
- [Tk (framework) from Wikipedia](https://en.wikipedia.org/wiki/Tk_%28framework%29)
- [Vector Graphics from Wikipedia](https://en.wikipedia.org/wiki/Vector_graphics)
- [Visual Component Library (VCL) from Wikipedia](https://en.wikipedia.org/wiki/Visual_Component_Library)
- [Widget toolkit from Wikipedia](https://en.wikipedia.org/wiki/Widget_toolkit)
- [wxWidgets from Wikipedia](https://en.wikipedia.org/wiki/WxWidgets)
- [X Window System (X11) from Wikipedia](https://en.wikipedia.org/wiki/X_Window_System) » [Unix](Unix "Unix"), [Linux](Linux "Linux")

## [X11.app (XQuartz) from Wikipedia](https://en.wikipedia.org/wiki/X11.app) » [OS X](Mac_OS "Mac OS") References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [I resign](http://ljkrakauer.com/LJK/60s/resign.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess stories](http://ljkrakauer.com/LJK/60s/chess1.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> see also [63-chess.mp4](http://projects.csail.mit.edu/video/history/aifilms/63-chess.mp4) hosted by [MIT CSAIL](https://www.csail.mit.edu/)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [XBoard from Wikipedia](https://en.wikipedia.org/wiki/XBoard)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Studie: Schachspielen mit ein 286er 12 MHz Laptop - Schachcomputer.info Community](http://www.schachcomputer.info/forum/showthread.php?t=3531) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), May 22, 2010 (German)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CDC Class - Device Context](http://msdn.microsoft.com/de-de/library/fxhhde73%28v=VS.100%29.aspx), [Microsoft Foundation Class Library](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library), [MSDN](https://en.wikipedia.org/wiki/Microsoft_Developer_Network)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> Code by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), written in about 2000
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [File:Chess bdl40.png - Wikimedia Commons](http://commons.wikimedia.org/wiki/File:Chess_bdl40.png)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Unicode values for chessmen](http://www.talkchess.com/forum/viewtopic.php?t=38318) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 07, 2011
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Alpha compositing from Wikipedia](https://en.wikipedia.org/wiki/Alpha_compositing)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [MinGW from Wikipedia](https://en.wikipedia.org/wiki/MinGW)

**[Up one Level](Graphics_Programming "Graphics Programming")**

