---
title: Ryan Mack
---
**[Home](Home "Home") \* [People](People "People") \* Ryan Mack**


**Ryan Mack**,  

in the late 90s an American teen programmer and inventor of the [Reverse Bitboards](Reverse_Bitboards "Reverse Bitboards") when he was a 16 year old schoolboy. In 2000, while introducing his *Hyperbola Project*, he explained the [x XOR (x - 2)](Subtracting_a_Rook_from_a_Blocking_Piece#oxoro2r "Subtracting a Rook from a Blocking Piece") [bit-twiddling](Bit-Twiddling "Bit-Twiddling") trick as the basic idea of Reverse Bitboards, essentially [subtracting a rook from a blocking piece](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece"), where the changed bits masked on a line remain the sliding [ray-attacks](On_an_empty_Board#RayAttacks "On an empty Board") in [positive](On_an_empty_Board#PositiveRays "On an empty Board") [ray-directions](Rays#RayDirections "Rays"). His idea to keep a [reversed or 180 degree rotated](Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") [occupancy](Occupancy "Occupancy") to apply the same trick for [negative](On_an_empty_Board#NegativeRays "On an empty Board") ray-directions to yield reversed attack bitboards, either requiring bitboard reversal or disjoint [serialization](Bitboard_Serialization "Bitboard Serialization") with reversion in the square centric world by [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") 63, turned out to be not that successful as the young author initially thought and claimed. However, [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence"), where fast vertical byteswap flipping is used on the fly to reverse [diagonals](Diagonals "Diagonals") and [files](Files "Files"), is somehow the resurrection of Ryan's ideas, vastly improved by [Aleks Peshkov's](Aleks_Peshkov "Aleks Peshkov") xor wizardry.






* [Software Speed Question](https://groups.google.com/d/msg/rec.games.chess.computer/DyRXuLL37q8/gFPq_JQGRQoJ) by Ryan Mack, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 02, 1998
* [NEW ENGINE IN PROGRESS WILL BLOW CRAFTY AWAY](https://groups.google.com/d/msg/rec.games.chess.computer/UZwoz0ubwVo/ys-MW8rQCEUJ) by Ryan Mack, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 08, 1999
* [Re: Need Advice: Pent III or AMD Athlon ? for Chess Programs](https://groups.google.com/d/msg/rec.games.chess.computer/eLB67qqGjpY/7Pe5nt2NVAUJ) by Hyperbola, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 29, 1999


**[Up one Level](People "People")**







 
