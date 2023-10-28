---
title: Fortran
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * Fortran**

**Fortran**, (FORTRAN)

a general purpose, [procedural](https://en.wikipedia.org/wiki/Procedural_programming) and [imperative](https://en.wikipedia.org/wiki/Imperative_programming_language) [programming language](https://en.wikipedia.org/wiki/Programming_language). Fortran was proposed and designed by [John W. Backus](https://en.wikipedia.org/wiki/John_Backus) as alternative for the [IBM 704](IBM_704 "IBM 704") [assembly](Assembly "Assembly") language. A draft specification for the [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") mathematical **For**mula **Tran**slating System was completed by mid 1954. The first Fortran compiler appeared in 1957 and was the first widely used [high-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language). Successive versions have added varios features over the years, such as [recursive routines](Recursion "Recursion") and [dynamic memory allocation](https://en.wikipedia.org/wiki/Dynamic_memory_allocation) in [Fortran 90](https://en.wikipedia.org/wiki/Fortran#Fortran_90). Many early chess programs were written in Fortran.

## Contents

- [1 Punched card](#punched-card)
- [2 Sample Chess Code](#sample-chess-code)
- [3 See also](#see-also)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Punched card

\[
[Punched card](https://en.wikipedia.org/wiki/Punched_card) from a Fortran program: Z(1) = Y + W(1) <a id="cite-note-1" href="#cite-ref-1">[1]</a>

## Sample Chess Code

A recursive Fortran 90 [Alpha-Beta](Alpha-Beta "Alpha-Beta") search routine <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```

RECURSIVE FUNCTION EVALUATE (ID, PRUNE) RESULT (RES) 
  USE GLOBALS 
  IMPLICIT INTEGER(A-Z) 
  DIMENSION XX(0:26), YY(0:26), CC(0:26) 
  LEVEL=LEVEL+1 
  BESTSCORE=10000*ID 
  DO B=7,0, -1 
     DO A=7,0, -1 
        ! generate the moves for all the pieces 
        ! and iterate through them 
        IF (SGN(BOARD(B,A))/=ID) CYCLE 
        CALL MOVELIST (A, B, XX, YY, CC, NDX) 
        DO I=0,NDX,1 
           X=XX(I); Y=YY(I); C=CC(I) 
           OLDSCORE=SCORE; MOVER=BOARD(B,A); TARG=BOARD(Y,X) 
           ! make the move and evaluate the new position 
           ! recursively. Targ holds the relative value of the piece 
           ! allowing use to calculate material gain/loss 
           CALL MAKEMOVE (A, B, X, Y, C) 
           IF (LEVEL<MAXLEVEL) THEN 
              SCORE=SCORE+EVALUATE(-ID, & 
                    BESTSCORE-TARG+ID*(8-ABS(4-X)-ABS(4-Y))) 
           END IF 
           SCORE=SCORE+TARG-ID*(8-ABS(4-X)-ABS(4-Y)) 
           ! we want to minimize the maximum possible loss 
           ! for black 
           IF ((ID<0 .AND. SCORE>BESTSCORE) .OR. & 
              (ID>0 .AND. SCORE<BESTSCORE)) THEN 
              BESTA(LEVEL)=A; BESTB(LEVEL)=B 
              BESTX(LEVEL)=X; BESTY(LEVEL)=Y 
              BESTSCORE=SCORE 
              IF ((ID<0 .AND. BESTSCORE>=PRUNE) .OR. & 
                 (ID>0 .AND. BESTSCORE<=PRUNE)) THEN 
                 BOARD(B,A)=MOVER; BOARD(Y,X)=TARG; SCORE=OLDSCORE 
                 LEVEL=LEVEL-1 
                 RES = BESTSCORE 
                 RETURN 
              END IF 
           END IF 
           BOARD(B,A)=MOVER; BOARD(Y,X)=TARG; SCORE=OLDSCORE 
        END DO 
     END DO 
  END DO 
  LEVEL=LEVEL-1 
  RES=BESTSCORE 
  RETURN 
END FUNCTION EVALUATE 

```

## See also

- [Basic](Basic "Basic")
- [Fortran Chess Programs](Category:Fortran "Category:Fortran")
- [IBM 704](IBM_704 "IBM 704")

## Publications

- [James Gillogly](James_Gillogly "James Gillogly") (**1970**). *[MAX : A FORTRAN Chess Player](http://www.rand.org/pubs/papers/P4428/)*. [RAND](https://en.wikipedia.org/wiki/RAND) paper
- [John Backus](https://en.wikipedia.org/wiki/John_Backus) (**1978**) *[The history of Fortran I, II, and III](http://portal.acm.org/citation.cfm?id=1198345)*. in [Richard L. Wexelblat](https://en.wikipedia.org/wiki/Richard_Wexelblat) (ed) [History of programming languages I](http://portal.acm.org/citation.cfm?id=800025&picked=prox&cfid=20756760&cftoken=81135282)
- [Alfio Marazz](http://www.iumsp.ch/Unites/us/Alfio/msp_Alfio.htm), [Johann Joss](Johann_Joss "Johann Joss"), [Alex Randriamiharisoa](http://www.365chess.com/players/Alex_Randriamiharisoa) (**1993**). *[Algorithms, routines, and S functions for robust statistics: the FORTRAN library ROBETH with an interface to S-PLUS](http://portal.acm.org/citation.cfm?id=134866)*. Wadsworth And Brooks/Cole Statistics/Probability Series, [amazon](http://www.amazon.com/exec/obidos/ASIN/0534196985/acmorg-20)

## Forum Posts

- [Any Fortran coder ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68944) by [Laurent Laborde](index.php?title=Laurent_Laborde&action=edit&redlink=1 "Laurent Laborde (page does not exist)"), [CCC](CCC "CCC"), November 15, 2018

## External Links

- [Fortran from Wikipedia](https://en.wikipedia.org/wiki/Fortran)
- [Microsoft® FORTRAN Version Features](http://www.emsps.com/oldtools/msforv.htm)
- [Intel Fortran Compiler](https://software.intel.com/en-us/fortran-compilers)
- [History of FORTRAN and FORTRAN II — Software Preservation Group](http://www.softwarepreservation.org/projects/FORTRAN/) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [comp.lang.fortran](https://groups.google.com/forum/#!forum/comp.lang.fortran) Discussion about Fortran

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Punched card from Wikipedia](https://en.wikipedia.org/wiki/Punched_card)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [chessf90.zip, Source and 64 bit Windows executable of A Fortran 90 chess program](http://cap.connx.com/chess-engines/new-approach/chessf90.zip) from [cap.connx.com](http://cap.connx.com/) by [Dann Corbit](Dann_Corbit "Dann Corbit")

**[Up one Level](Languages "Languages")**

