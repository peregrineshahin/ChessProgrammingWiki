---
title: PieceSets
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* Piece-Sets**



 [](http://www.irvingamen.com/works/Chessboard.htm) [Irving Amen](Category:Irving_Amen "Category:Irving Amen") - Chess Board <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Piece-Sets**,  

a set-wise representation with one bit for each [piece](Pieces "Pieces") inside one [32-bit word](Double_Word "Double Word") or two [16-bit words](Word "Word") for each side. Piece-sets have some similarities with [bitboards](Bitboards "Bitboards"), but each set bit does not directly associate a [square](Squares "Squares"), but an index inside a [piece-list](Piece-Lists "Piece-Lists"). Thus to get the square, one additional indirection is necessary. Often the bit-position of a piece-set directly implies the information, what type and color the piece is - while bitboards usually maintains distinct sets for different pieces. That has advantages for instance in [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), if one maintains an [attack-set](Attack_and_Defend_Maps "Attack and Defend Maps") as [incremental updated](Incremental_Updates "Incremental Updates") [array](Array "Array") or 64 piece-sets for each square. 



### Contents


* [1 Serialization](#serialization)
* [2 Move Generation](#move-generation)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 References](#references)






Techniques to traverse piece-sets are similar to [bitboard serialization](Bitboard_Serialization "Bitboard Serialization"), but of course more 32-bit friendly. Same applies for [general set-wise operations](General_Setwise_Operations "General Setwise Operations").



## Move Generation


As proposed by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") and used in [KnightCap](KnightCap "KnightCap"), piece-sets can be used to generate moves, as seen in the move generation code of [Dorpsgek](Dorpsgek "Dorpsgek") by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), with some code omitted:




```C++

    /* Iterate over all squares */
    for (dest = 0; dest < 64; dest++) {

        /* Do we have any pieces attacking this square? */
        if ((index = (b->bitlist[dest] & b->sidemask[b->side]))) {

            /* Yes, we do, iterate over them. */
            while (index) {
                bit = BitScanForward(index); /* Retrieve index of lowest attacker. */
                from = b->piecelist[bit];    /* Retrieve the square it is on. */
                type = (b->board[dest] == INVALID) ? MoveTypeNormal : MoveTypeCapture; /* Check if capture */
                index &= index - 1; /* Reset LSB */

                /* Don't allow own-piece captures. */
                if (type == MoveTypeCapture && ((1 << b->index[dest]) & b->sidemask[b->side])) {
                    continue;
                }

                /* Pawn related code */
                if ((1 << bit) & b->piecemask[PAWN]) {

                    /* En-passant captures can move to nothing, so we avoid skipping them */
                    if (b->ep != INVALID && dest == b->ep) {
                        if ((b->side == WHITE && ROW(from) == 4) ||
                                (b->side == BLACK && ROW(from) == 3)) {
                            type = MoveTypeEnPassant;
                        }
                    }
                    /* Don't allow pawns to capture diagonally when there is nothing to capture. */
                    if (type == MoveTypeNormal) {
                        continue;
                    }

                    /* Captures with promotion */
                    if ((b->side == WHITE && ROW(from) == 6) ||
                            (b->side == BLACK && ROW(from) == 1)) {
                        AddMove(m, &movecount, from, dest, MoveTypePromotionKnight);
                        AddMove(m, &movecount, from, dest, MoveTypePromotionBishop);
                        AddMove(m, &movecount, from, dest, MoveTypePromotionRook);
                        AddMove(m, &movecount, from, dest, MoveTypePromotionQueen);
                        continue;
                    }
                }

                /* Add this move to the list and increment the pointer. */
                AddMove(m, &movecount, from, dest, type);
            }
        }
    }

```

## See also


* [32-bit BitScan](Kim_Walisch#Bitscan "Kim Walisch") by [Kim Walisch](Kim_Walisch "Kim Walisch")
* [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [Chest](Chest "Chest")
* [IsiChess](IsiChess "IsiChess")
* [KnightCap](KnightCap "KnightCap")
* [Piece-Lists](Piece-Lists "Piece-Lists")


## Forum Posts


* [Re: Bit Board Bonkers?? - other alternatives](https://groups.google.com/group/rec.games.chess.computer/msg/4d6c328e8e8e0cd4) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 9, 1997
* [Nomenclature suggestion: Bit target programs](http://www.talkchess.com/forum/viewtopic.php?t=54810) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 31, 2014
* [PieceLists ?](http://www.talkchess.com/forum/viewtopic.php?t=63126) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 10, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Woodcuts with a Chess Theme](http://www.irvingamen.com/woodcutChess.htm) by [Irving Amen](Category:Irving_Amen "Category:Irving Amen")

**[Up one Level](Board_Representation "Board Representation")**







 
