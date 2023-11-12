---
title: Simplified Evaluation Function
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Simplified Evaluation Function**


The content of this page has been originally posted by [Tomasz Michniewski](Tomasz_Michniewski "Tomasz Michniewski") on the Polish chess programming discussion list (progszach). It contains a proposal of extremely basic evaluation function required from the participants of a "Unified Evaluation" test tournament. Please note that the values presented here have been designed specifically to compensate for the lack of any other chess knowledge, and **not** for being supplemented by it.


There are two parts of this email, the first is about simple [piece values](Point_Value "Point Value"), the second is about [piece-square tables](Piece-Square_Tables "Piece-Square Tables").



## Piece-Square Tables


Now, let's move for piece-square values. Generally I would like to give bonuses for pieces standing well and penalties for pieces standing badly. Other squares will have neutral value of 0. Of course one may incorporate above [piece values](Point_Value "Point Value") into [piece-square tables](Piece-Square_Tables "Piece-Square Tables") if they wish. I don't do this.



### Pawns


For pawns we simply encourage the pawns to advance. Additionally we try to discourage the engine from leaving central pawns unmoved. The problem I could see here is that this is contradictory to keeping pawns in front of the king. We also ignore the factor whether the pawn is passed or not. So more advanced evaluation is called for, especially that "pawns are soul of the game".




```C++

// pawn
 0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0

```

OK, let's comment this table. Firstly the shelter in front of white short castle (long castle - it's symmetrical) - pawns at f2, g2 and h2 get bonuses. Additionally we set negative values for f3 and smaller for g3 which both create holes around king. Pawn h2 have the same value on h2 and h3, so the engine may create the hole if the situation calls for it. Moreover - if it gets position with a pawn at g3 and a bishop at g2, then it still may play h3 or not. Therefore h3 has the same value as h2.


Zero value on f4, g4, h4 prevents playing with pawns in front of the king. Moving these pawns to f5, g5, h5 still brings nothing, but at this moment we have the same values as on rank 2.


In the centre we have the most negative values on d2 and e2. We don't like these pawns. d3 and e3 aren't good either. Only d4 and e4 in the centre. Even better on d5 and e5.


Beginning with rank 6th we give bonus for advanced pawns. On rank 7th even bigger.



### Knights


With knights we simply encourage them to go to the center. Standing on the edge is a bad idea. Standing in the corner is a terrible idea. Probably it was Tartakover who said that "one piece stands badly, the whole game stands badly". And knights move slowly.




```C++

// knight
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50,

```

As you can see I would happily trade for three pawns any knight standing on the edge. Additionally I put slight bonuses for e2, d2, b5, g5, b3 and g3. Then there are bonuses for being in the center.



### Bishops



```C++

// bishop
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20,

```

We avoid corners and borders. Additionally we prefer squares like b3, c4, b5, d3 and the central ones. Moreover, I wouldn't like to exchange white bishop at d3 (or c3) for black knight at e4, so squares at c3 (f3) have value of 10. As a result white bishop at d3 (c3) is worth (330+10) and black knight at e4 is worth (320+20). So the choice of whether to exchange or not should depend on other issues. On the contrary white bishop at e4 (330+10) would be captured by black knight from f6 (320+10). White bishop at g5 (330+5) won't capture black knight at f6 (320+10).



### Rooks



```C++

rook
  0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0

```

The only ideas which came to my mind was to centralize, occupy the 7th rank and avoid a, h columns (in order not to defend pawn b3 from a3). So generally this is [Gerbil](Gerbil "Gerbil") like.



### Queen



```C++

//queen
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20

```

Generally with queen I marked places where I wouldn't like to have a queen. Additionally I slightly marked central squares to keep the queen in the centre and b3, c2 squares (Paweł's suggestion). The rest should be done by tactics.



### King



```C++

king middle game
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20

```

This is to make the king stand behind the pawn shelter.


In the ending the values change.




```C++

// king end game
-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50

```

And of course "These values are for white, for black I use mirrored values." Additionally we should define where the ending begins. For me it might be either if:



1. Both sides have no queens or
2. Every side which has a queen has additionally no other pieces or one minorpiece maximum.


## See also


* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")


**[Up one Level](Evaluation "Evaluation")**







 
