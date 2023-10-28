---
title: Chess 0.5
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chess 0.5**

[](https://archive.org/details/byte-magazine-1978-10) [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chess 0.5**,

a program by [Larry Atkin](Larry_Atkin "Larry Atkin") and [Peter W. Frey](Peter_W._Frey "Peter W. Frey") for didactic purposes, written in the [ETH Zurich](ETH_Zurich "ETH Zurich") dialect of [Pascal](Pascal "Pascal") for the [CDC 6600](CDC_6600 "CDC 6600") series of mainframes, published 1978/1979 in [Byte Magazine](Byte_Magazine "Byte Magazine"), and re-published on-line in 2005, available from Scott A. Moore's <a id="cite-note-2" href="#cite-ref-2">[2]</a> sites, unfortunately with some [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition)-errors such as syntactical correct replacement of '\*' by '+' with score factor by side (XTMV, ±1) in some places <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Chess 0.5 may be compiled with [GNU Pascal](Pascal#GNUPascal "Pascal") for recent hardware. Due to non-local [goto](https://en.wikipedia.org/wiki/Goto) statements over procedure or function boundaries compiling with [Free Pascal](Pascal#FreePascal "Pascal") is not possible <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

Larry Atkin is co-author of the famous [Northwestern University](Northwestern_University "Northwestern University") [Chess](</Chess_(Program)> "Chess (Program)") line of programs. At the time of the article, Chess was at about version 4.6 <a id="cite-note-5" href="#cite-ref-5">[5]</a> . Chess 0.5 is based on his intimate knowledge of that program, but is a seperate program designed for pedagogical purposes to play chess vaguely well <a id="cite-note-6" href="#cite-ref-6">[6]</a> using Chess 4.x like structures of a [Shannon Type A](Type_A_Strategy "Type A Strategy") approach with [alpha-beta](Alpha-Beta "Alpha-Beta") and [quiescence search](Quiescence_Search "Quiescence Search"), [bitboards](Bitboards "Bitboards") and [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps").

## Contents

- [1 Blueprint](#blueprint)
- [2 Description](#description)
  - [2.1 Board Representation](#board-representation)
  - [2.2 Bitboard Infrastructure](#bitboard-infrastructure)
    - [2.2.1 Setwise Operations](#setwise-operations)
    - [2.2.2 BitScan](#bitscan)
    - [2.2.3 Popcount](#popcount)
  - [2.3 Evaluation](#evaluation)
  - [2.4 Search](#search)
- [3 See also](#see-also)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Blueprint

As encouraged by Frey and Atkin in their article "The reader with an interest in chess and programming should use this listing as starting point for developing a program" <a id="cite-note-7" href="#cite-ref-7">[7]</a> , Chess 0.5 was origin of at least three other competing programs, the Austrian [Merlin](Merlin "Merlin") by [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") and [Roland Schreier](index.php?title=Roland_Schreier&action=edit&redlink=1 "Roland Schreier (page does not exist)"), further developed in Pascal except some time critical, often called routines, which were re-written in [CDC](CDC_6600 "CDC 6600") [assembly](Assembly "Assembly") by Wagner <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> , the Dutch [Chess 0.5X](Chess_0.5X "Chess 0.5X") by [Wim Elsenaar](Wim_Elsenaar "Wim Elsenaar"), a [PDP-11](PDP-11 "PDP-11") assembly port, and according to postings in [rgcc](Computer_Chess_Forums "Computer Chess Forums") <a id="cite-note-10" href="#cite-ref-10">[10]</a> , the Finnish [Shy](Shy "Shy") by [Juha Kasanen](Juha_Kasanen "Juha Kasanen"), [Mika Korhonen](Mika_Korhonen "Mika Korhonen") and [Timo Saari](Timo_Saari "Timo Saari"), written in [Algol](Algol "Algol").

## Description

## Board Representation

Chess 0.5 keeps an [8x8 board](8x8_Board "8x8 Board") either indexed by [square](Squares "Squares") or [rank](Ranks "Ranks") and [file](Files "Files"), ...

```

CONST
  AX = 0;       ZX = 31;               (* SUBSETS OF SQUARES *)
  AS = 0;       ZS = 63;               (* BOARD VECTOR LIMITS *)
TYPE
  TF = (F1,F2,F3,F4,F5,F6,F7,F8);      (* FILES *)
  TR = (R1,R2,R3,R4,R5,R6,R7,R8);      (* RANKS *)
  TI = INTEGER;                        (* NUMBERS *)
  TS = AS..ZS;                         (* SQUARES *)
  TX = AX..ZX;                         (* SOME SQUARES *)
  TY = AY..ZY;                         (* NUMBER OF TX'S IN A BOARD *)
  TM = (LITE,DARK,NONE);               (* SIDES *)
  TP = (LP,LR,LN,LB,LQ,LK,DP,DR,DN,DB,DQ,DK,MT); (* PIECES: LIGHT PAWN,... , DARK KING, EMPTY SQUARE *)
  SX = SET OF TX;                      (* SET OF SOME SQUARES *)

  RB = RECORD                          (*   BOARDS  *)
    RBTM : TM;                         (*  SIDE  TO MOVE  *)
    RBTS : TT;                         (*  ENPASSANT  SQUARE   *)
    RBTI : TI;                         (*  MOVE   NUMBER   *)
    RBSQ : SQ;                         (*  CASTLE  FLAGS   *)
    CASE INTEGER OF
      0: ( RBIS  : ARRAY [TS] OF TP);   (* INDEXED BY SQUARE *)
      1: ( RBIRF : ARRAY [TR,TF] OF TP);(* INDEXED BY RANK AND FILE *)
    END;

```

... and further relies on [bitboards](Bitboards "Bitboards"), defined as union of arrays of sets and integers:

```

  RS = RECORD                          (* BIT BOARDS *)
    CASE INTEGER OF
      0: (RSSS: ARRAY [TY] OF SX);     (* ARRAY OF SETS *)
      1: (RSTI: ARRAY [TY] OF TI);     (* ARRAY OF INTEGERS *)
    END;

```

Beside the [mailbox](Mailbox "Mailbox") arrays (BOARD, MBORD) and [bitboard board definition](Bitboard_Board-Definition "Bitboard Board-Definition") (TPLOC, TMLOC), Chess 0.5 maintains [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), two 8x8 arrays ATKTO and ATKFR, the first for every square a attack bitboard **to** other squares of the piece (if any) residing on that square, the second for each square a bitboard of all white and black man [attacking this square](Square_Attacked_By "Square Attacked By").

```

  BOARD : RB;                          (* THE BOARD *)
  MBORD : ARRAY [TS] OF TP;            (* LOOK-AHEAD BOARD *)
  ATKFR : ARRAY [TS] OF RS;            (* ATTACKS FROM A SQUARE *)
  ATKTO : ARRAY [TS] OF RS;            (* ATTACKS TO A SQUARE *)
  ALATK : ARRAY [TM] OF RS;            (* ATTACKS BY EACH COLOR *)
  TPLOC : ARRAY [TP] OF RS;            (* LOCATIONS OF PIECE BY TYPE *)
  TMLOC : ARRAY [TM] OF RS;            (* LOCATIONS OF PIECE BY COLOR *)

```

## Bitboard Infrastructure

### Setwise Operations

[Bitboard intersection](General_Setwise_Operations#Intersection "General Setwise Operations"), [union](General_Setwise_Operations#Union "General Setwise Operations") and [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations") are implemented with [set-wise operations](http://www.freepascal.org/docs-html/ref/refsu50.html) "\*, +, -", [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") (not) by relative complement from the [universe](General_Setwise_Operations#EmptyAndUniverse "General Setwise Operations") (\[AX..ZX\]):

```

PROCEDURE ANDRS                        (* INTERSECTION OF TWO BITBOARDS *)
  (VAR C:RS;                           (* RESULT *)
   A, B:RS);                           (* OPERANDS *)
VAR
  INTY : TY;                           (* BIT BOARD WORD INDEX *)
BEGIN
  FOR INTY := AY TO ZY DO
    C.RSSS[INTY] := A.RSSS[INTY] * B.RSSS[INTY];
END;  (* ANDRS *)

PROCEDURE IORRS                        (* UNION OF TWO BIT BOARDS *)
 (VAR C:RS;                            (* RESULT *)
  A, B:RS);                            (* OPERANDS *)
VAR
  INTY : TY;                           (* BIT BOARD WORD INDEX *)
BEGIN
  FOR   INTY :=  AY TO ZY DO
    C.RSSS[INTY] := A.RSSS[INTY] + B.RSSS[INTY];
END;  (* IORRS *)

PROCEDURE NOTRS                        (* COMPLEMENT OF A BIT BOARD *)
 (VAR C:RS;                            (* RESULT *)
  A:RS);                               (* OPERAND *)
VAR
  INTY : TY;                           (* BIT BOARD WORD INDEX *)
BEGIN
  FOR INTY := AY TO ZY DO
    C.RSSS[INTY] := [AX..ZX] - A.RSSS[INTY];
END;  (* NOTRS *)

```

### BitScan

[BitScan reverse with reset](BitScan#BitscanwithReset "BitScan") is implemented with machine dependent [CDC 6600](CDC_6600 "CDC 6600") [float conversion](Float#BitScan "Float") (omitted here) - the machine independent code inefficiently loops over up to 2\*32 bits of the set and cries for improvement:

```

FUNCTION NXTTS                         (* NEXT ELEMENT IN BIT BOARD *)
 (VAR A:RS;                            (* BIT BOARD TO LOCATE FIRST SQUARE, AND THEN REMOVE *)
  VAR B:TS                             (* SQUARE NUMBER OF FIRST SQUARE IN BIT BOARD *)
 ): TB;                                (* TRUE IFF ANY SQUARES WERE SET INITIALLY *)
LABEL
  11;                                  (* RETURN *)
VAR
  INTX : TX;                           (* BIT BOARD BIT INDEX *)
  INTY : TY;                           (* BIT BOARD WORD INDEX *)
  X : RK;                              (* KLUDGE WORD *)
BEGIN
  FOR INTY := ZY DOWNTO AY DO          (* LOOP THRU BIT BOARD WORDS *)
    IF A.RSTI[INTY] <> 0 THEN
    BEGIN
      FOR INTX := ZX DOWNTO AX DO      (* LOOP THROUGH BITS IN WORD OF SET *)
        IF INTX IN  A.RSSS[INTY] THEN
        BEGIN
          B := INTX+INTY*(ZX+1);       (* RETURN SQUARE NUMBER *)
          A.RSSS[INTY] := A.RSSS[INTY] - [INTX]; (* REMOVE  BIT FROM WORD *)
          NXTTS := TRUE;               (* RETURN A BIT SET *)
          GOTO 11;                     (* RETURN *)
        END;
    END;
  NXTTS := FALSE;                      (* ELSE RETURN NC BITS SET *)
11:                                    (* RETURN *)
END;  (* NXTTS *)

```

### Popcount

The machine independent [population count](Population_Count "Population Count") relies on the above [bitscan with reset](Chess_0.5#BitScan "Chess 0.5")!

```

FUNCTION CNTRS                         (* COUNT NENBERS OF A BIT BOARD *)
(A:RS): TS;                            (* BIT BOARD TO COUNT *)
VAR
  INTS : TS;                           (* TEMPORARY *)
  INRS : RS;                           (* SCRATCH *)
  IMTS : TS;                           (* SCRATCH *)
BEGIN
  INTS := 0;
  CPYRS(INRS,A);
  WHILE NXTTS(INRS,IMTS) DO
    INTS := INTS+1;                    (* COUNT SQUARES *)
  CNTRS := INTS;                       (* RETURN SUM *)
END;  (* CNTRS *)

```

## Evaluation

Chess 0.5's [evaluation](Evaluation "Evaluation") routine **EVALU8** implements a [lazy evaluation](Lazy_Evaluation "Lazy Evaluation") only for too worse [scores](Score "Score"). If the [incremental updated](Incremental_Updates "Incremental Updates") [material balance](Material "Material") plus the maximum positional score is still less or equal than [alpha](Alpha "Alpha") (best value two plies up BSTVL\[JNTK-2\]), only the material balance is assigned without further positional analysis. Otherwise **EVALU8** consides [piece mobility](Mobility "Mobility") (counting attacks), [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety") and some rook terms such as doubled rooks and [rook on 7th rank](Rook_on_Seventh "Rook on Seventh"). Differences of light minus dark positional terms are adjusted by appropriate feature weights. To make white point of view scores relative to the [side to move](Side_to_move "Side to move"), they are multiplied by a score factor (+1, -1) indexed by side.

```

PROCEDURE EVALU8;                      (* EVALUATE CURRENT POSITION *)
  FUNCTION EVKING                      (* EVALUATE KING *)
  FUNCTION EVMOBL                      (* EVALUATE MOBILITY *)
  FUNCTION EVPAWN                      (* EVALUATE PAWNS *)
  FUNCTION EVROOK                      (* EVALUATE ROOKS *)
BEGIN
  IF XTMV[JNTM]*MBVAL[JNTK] + MAXPS <= BSTVL[JNTK-2] THEN   (* !!! OCR  *)
                                       (* MOVE WILL PRUNE ANYWAY *)
    INTV := XTMV[JNTM] * MBVAL[JNTK]
  ELSE
  BEGIN
    INTV := (  FWPAWN*(EVPAWN(TPLOC[LP],S2,R2)-EVPAWN(TPLOC[DP],S4,R7))
             + FWMINM*(EVMOBL(LB,LN)          -EVMOBL(DB,DN)          )
             + FWMAJM*(EVMOBL(LR,LQ)          -EVMOBL(DR,DQ)          )
             + FWROOK*(EVROOK(TPLOC[LR],XRRS[R7])
                      -EVROOK(TPLOC[DR],XRRS[R2])                     )
             + FWKING*(EVKING(TPLOC[LK],TPLOC[LP])
                      -EVKING(TPLOC[DK],TPLOC[DP])                    )
            ) DIV 64;
    MAXPS := MAX(MAXPS,ABS(INTV));
    INTV := XTMV[JNTM] * (MBVAL[JNTK] + INTV);
  END;
  IF SWTR THEN
    BEGIN
      WRITE(" EVALU8",JNTK,JNTW,INDEX[JNTK],INTV);
      PRIMOV(MOVES[INDEX[JNTK]]);
    END;
  VALUE[INDEX[JNTK]] := INTV;          (* RETURN SCORE *)
END;  (* EVALU8 *)

```

## Search

The [search](Search "Search") is implemented spaghetti like [non-recursively](Iterative_Search "Iterative Search") as [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) with [goto](https://en.wikipedia.org/wiki/Goto) labels using explicit [stacks](Stack "Stack") aka [ply](Ply "Ply") indexed [arrays](Array "Array"), and features [iterative deepening](Iterative_Deepening "Iterative Deepening") with [aspiration](Aspiration_Windows "Aspiration Windows") and [alpha-beta pruning](Alpha-Beta "Alpha-Beta"). The value array of [best moves](Best_Move "Best Move") indexed by current ply is the current [alpha](Alpha "Alpha") of a newly entered node, initialized by grand parent's best value (ply-2) - best value of the parent node (ply-1) is minus [beta](Beta "Beta") in the [negamax](Negamax "Negamax") sense. The nested function SELECT implements a [staged move generation](Move_Generation#Staged "Move Generation"), considering [root search](Root "Root") (ply 0), full-width and [quiescence](Quiescence_Search "Quiescence Search"), generating [captures](Captures "Captures") in [MVV/LVA](MVV-LVA "MVV-LVA") order, [killers](Killer_Move "Killer Move"), and remaining moves. While the ply indices range from 0 to 16, the best value array needs three additional sentinels due to ply-2, ply-1, and ply+1 accesses. The outline of the search routine with jump labels (:) is given below, most lines omitted:

```

  BSTVL : ARRAY [AKM2..ZKP1] OF TV;    (* VALUE OF BEST MOVE [-2..17] *)

FUNCTION SEARCH                        (* SEARCH LOOK-AHEAD TREE *)
: TW;                                  (* RETURNS THE BEST MOVE *)
  PROCEDURE NEWBST                     (* SAVE BEST MOVE INFORMATION *)
    (A:TK);                            (* PLY OF BEST MOVE *)

  FUNCTION MINMAX                      (* PERFORM MINIMAX OPERATION *)
    (A:TK)                             (* PLY TO MINIMAX AT *)
     : TB;                             (* TRUE IF REFUTATION *)
    MINMAX := FALSE;                   (* DEFAULT IS NO PRUNING *)
    IF -BSTVL[A+1] > BSTVL[A] THEN     (* Score > Alpha ? *)
    BEGIN
      BSTVL[A] := -BSTVL[A+1];         (* Alpha = Score  *)
      NEWBST(A);                       (* SAVE BEST MOVE *)
      MINMAX := BSTVL[A+1] <= BSTVL[A-1]; (* -Score < -Beta => Score > Beta *)
    END;
  END;  (* MINMAX *)

  FUNCTION SELECT                      (* SELECT NEXT MOVE TO SEARCH *)
     : TB;                             (* TRUE IF MOVE RETURNED *)
  BEGIN
  21:  (* NEW SEARCH MOOE *)
    CASE SRCHM[JNTK] OF
      H0:  (* INITIALIZE FOR NEW MOVE *)
      H1:  (* INITIALIZE AT  NEW DEPTH *)
      H2:  (* CAPTURE SEARCH *)
      H3:  (* FULL WIDTH SEARCH - CAPTURES *)
      H4:  (* INITIALIZE SCAN OF CASTLE MOVES AND OTHER MOVES BY KILLER PIECE *)
      H5:  (* FULL WIDTH SEARCH - CASTLES AND OTHER MOVES BY KILLER PIECE *)
      H6:  (* FULL WIDTH SEARCH - REMAINING MOVES *)
      H7:  (* RESEARCH FIRST PLY *)
  22:  (* SELECT EXIT *)
    SELECT := INTB;                    (* RETURN VALUE *)
  END;  (* SELECT *)

BEGIN  (* SEARCH *)
  EVALU8;                              (* INITIAL GUESS AT SCORE *)
  BSTVL[AK-2] :=   VALUE[AW] - WINDOW; (* INITIALIZE ALPHA-BETA WINDON *)
  BSTVL[AK-1] := -(VALUE[AW] + WINDOW);
  JMTK := AK+1;
  WHILE (NODES < FNODEL) AND (JNTK < MAX(ZK DIV 2, ZK-8)) DO
  BEGIN
11:  (* START NEW PLY *)
12:  (* DIFFERENT  FIRST MOVE  *)
13:  (* FLOAT   VALUE   BACK  *)
      IF   MINMAX(JNTK)   THEN
        GOTO 15;                       (* PRUNE *)
14:  (* FIND ANOTHER MOVE AT THIS PLY *)
15:  (* BACK UP A PLY *)
16:  (* EXIT SEARCH *)
  SEARCH := BSTMV[AK];                 (* RETURN BEST MOVE *)
END;  (* SEARCH *)

```

## See also

- [Chess](</Chess_(Program)> "Chess (Program)")
- [Chess 0.5X](Chess_0.5X "Chess 0.5X")
- [Chess 7.0](Chess_7.0 "Chess 7.0")
- [CookieCat](CookieCat "CookieCat")
- [Merlin](Merlin "Merlin")
- [Shy](Shy "Shy")

## Publications

- [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1978**). *[Creating a Chess Player](https://archive.org/stream/byte-magazine-1978-10/1978_10_BYTE_03-10_Chess_for_the_Microcomputer#page/n181/mode/2up).* An Essay on Human and Computer Chess Skill, [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), pp. 182-191. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-3.Creating_A_Chess_Player/Creating_A_Chess_Player.Frey_Atkin.Byte_Magazine.Oct-1978.062303029.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1978**). *[Creating a Chess Player, Part 2: Chess 0.5](https://archive.org/stream/byte-magazine-1978-11/1978_11_BYTE_03-11_The_Sky_is_the_Limit#page/n163/mode/2up)*. [BYTE, Vol. 3, No. 11](Byte_Magazine#BYTE311 "Byte Magazine")
- [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1978**). *[Creating a Chess Player, Part 3: Chess 0.5 (continued)](https://archive.org/stream/byte-magazine-1978-12/1978_12_BYTE_03-12_Life#page/n141/mode/2up)*. [BYTE, Vol. 3, No. 12](Byte_Magazine#BYTE312 "Byte Magazine")
- [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1979**). *[Creating a Chess-Player, Part 4: Thoughts on Strategy](https://archive.org/stream/byte-magazine-1979-01/1979_01_BYTE_04-01_Life_Algorithms#page/n127/mode/2up)*. In [Blaise W. Liffick](http://cs.millersville.edu/~liffick/) (ed.), [The Byte Book of Pascal](http://books.google.com/books/about/The_BYTE_book_of_Pascal.html?id=ofpfQgAACAAJ), pp. 143-155. Byte Publications, also [BYTE, Vol. 4, No. 1](Byte_Magazine#BYTE401 "Byte Magazine")

## Forum Posts

- [Byte Chess 0.5 finally available. From Byte Magazine 1978](https://groups.google.com/d/msg/rec.games.chess.computer/3iSe8NsM024/-SrmrNv4saMJ) by I Forget, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2005
- [Update for Byte Chess 0.5](https://groups.google.com/d/msg/comp.lang.pascal.misc/ATJoB3c4-jM/9nM_TWmqAwUJ) by I Forget, [comp.lang.pascal.misc](http://groups.google.com/group/comp.lang.pascal.misc/topics), June 12, 2005
- [Missing from Computer-Chess Wiki](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=39612) by Sylwy, [CCC](CCC "CCC"), July 05, 2011
- [Need a little help from a Pascal guru (Chess05 Frey/Atkin)](http://www.talkchess.com/forum/viewtopic.php?t=41896) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), January 09, 2012

## External Links

- [Chess 0.5, Release 1 - 2005-05-30](http://www.moorecad.com/standardpascal/ByteChess.txt) by [Scott A. Moore](http://www.moorecad.com/standardpascal/scottmoore.html)

[Byte Chess 0.5 source code](http://www.moorecad.com/standardpascal/Chess05.pas) hosted by [Scott A. Moore](http://www.moorecad.com/standardpascal/scottmoore.html)

- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
- [Computer-Schach](http://www.andreadrian.de/schach/) by [Andre Adrian](Andre_Adrian "Andre Adrian") (German)

## [Chess05GNU.pas](http://www.andreadrian.de/schach/Chess05GNU.pas) References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Byte Vol. 3, No. 10, October 1978](https://archive.org/details/byte-magazine-1978-10) from the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Scott A. Moore's site](http://www.moorecad.com/standardpascal/scottmoore.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Byte Chess 0.5 source code](http://www.moorecad.com/standardpascal/Chess05.pas) (OCR-Errors!)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Need a little help from a Pascal guru (Chess05 Frey/Atkin)](http://www.talkchess.com/forum/viewtopic.php?t=41896&start=1) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 09, 2012
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Chess 4.6 source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431614f455002), gift of [David Slate](David_Slate "David Slate"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/3-3.Chess_4.6_Sourcecode.102645430/chess_4-6.sourcecode.102645430.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Chess 0.5, Release 1 - 2005-05-30](http://www.moorecad.com/standardpascal/ByteChess.txt)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1978**). *[Creating a Chess Player, Part 3: Chess 0.5 (continued)](https://archive.org/stream/byte-magazine-1978-12/1978_12_BYTE_03-12_Life#page/n141/mode/2up)*. [BYTE, Vol. 3, No. 12](Byte_Magazine#BYTE312 "Byte Magazine")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Werner DePauli-Schimanovich](Werner_Schimanovich "Werner Schimanovich") (**2006**). *Europolis 6*. Informatik für Spiele und Verkehr. Extension der Mengenlehre, Herausgeber: Franz Pichler, Universitätsverlag Rudolf Trauner, ISBN 978-3-85487-946-6, (SG7) Merlin (ein ComputerChess-Programm) s. 171 (German), [Google Books](http://books.google.com/books?id=Gf4WibmHVbcC&pg=PA175&lpg=PA175&source=bl&ots=YPtaHAp3Z4&sig=DNRPh11heo8Q1zS3UOBe0qoCF-8&hl=en&ei=0GmnTMX1GMfJswaL-NivDA&sa=X&oi=book_result&ct=result&resnum=1&ved=0CBgQ6AEwAA#v=onepage&q&f=false)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") (**1981**). *Das Schachprogramm Merlin, Verbesserung von Laufzeit-Effizient, Eröffnungsbibliothek und Bewertungsfunktion.* 4. Tagung "Berichte aus Informatik-Instituten" (German)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: Byte Chess 0.5 finally available. From Byte Magazine 1978](https://groups.google.com/d/msg/rec.games.chess.computer/3iSe8NsM024/DrW8Dzsr2tYJ) by I Forget, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 02, 2005

**[Up one Level](Engines "Engines")**

