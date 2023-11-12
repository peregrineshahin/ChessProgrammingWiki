---
title: Zobrist Hashing
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Transposition Table](Transposition_Table "Transposition Table") \* Zobrist Hashing**



[.svg) [King Wen sequence](https://en.wikipedia.org/wiki/King_Wen_sequence) [[1]](#cite_note-1) [[2]](#cite_note-2)
**Zobrist Hashing**,  

a technique to transform a board [position](Chess_Position "Chess Position") of arbitrary size into a number of a set length, with an equal distribution over all possible numbers, invented by [Albert Zobrist](Albert_Zobrist "Albert Zobrist") [[3]](#cite_note-3). In an early Usenet post in 1982, [Tom Truscott](Tom_Truscott "Tom Truscott") mentioned [Jim Gillogly's](James_Gillogly "James Gillogly") n-bit hashing technique [[4]](#cite_note-4), who apparently read Zobrist's paper early, and credits Zobrist in a 1997 [rgcc](Computer_Chess_Forums "Computer Chess Forums") post [[5]](#cite_note-5). Zobrist Hashing is an instance of [tabulation hashing](https://en.wikipedia.org/wiki/Tabulation_hashing) [[6]](#cite_note-6), a method for constructing [universal families of hash functions](https://en.wikipedia.org/wiki/Universal_hashing) by combining [table lookup](https://en.wikipedia.org/wiki/Lookup_table) with [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") operations. Zobrist Hashing was rediscovered by [J. Lawrence Carter](Mathematician#JLCarter "Mathematician") and [Mark N. Wegman](Mathematician#MNWegman "Mathematician") in 1977 [[7]](#cite_note-7) and studied in more detail by [Mihai Pătrașcu](Mathematician#MPatrascu "Mathematician") and [Mikkel Thorup](Mathematician#MThorup "Mathematician") in 2011 [[8]](#cite_note-8) [[9]](#cite_note-9).


The main purpose of Zobrist hash codes in chess programming is to get an almost unique index number for any chess position, with a very important requirement that two similar positions generate entirely different indices. These index numbers are used for faster and more space efficient [Hash tables](Hash_Table "Hash Table") or databases, e.g. [transposition tables](Transposition_Table "Transposition Table") and [opening books](Opening_Book "Opening Book"). 



### Contents


* [1 Metamorphosis](#Metamorphosis)
* [2 Initialization](#Initialization)
* [3 Runtime](#Runtime)
* [4 Collisions](#Collisions)
	+ [4.1 Theory](#Theory)
	+ [4.2 Praxis](#Praxis)
	+ [4.3 Lack a True Integer Type](#Lack_a_True_Integer_Type)
	+ [4.4 Linear Independence](#Linear_Independence)
* [5 See also](#See_also)
* [6 Publications](#Publications)
* [7 Forum Posts](#Forum_Posts)
	+ [7.1 1982 ...](#1982_...)
	+ [7.2 1990 ...](#1990_...)
	+ [7.3 2000 ...](#2000_...)
	+ [7.4 2005 ...](#2005_...)
	+ [7.5 2010 ...](#2010_...)
	+ [7.6 2015 ...](#2015_...)
	+ [7.7 2020 ...](#2020_...)
* [8 External Links](#External_Links)
* [9 References](#References)






[](http://www.mcescher.com/Gallery/gallery-recogn.htm)
[](http://www.mcescher.com/Gallery/gallery-recogn.htm)
[M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), [Metamorphosis](https://en.wikipedia.org/wiki/Metamorphosis) III, 1967-1968 [[10]](#cite_note-10)



## Initialization


At program initialization, we generate an [array](Array "Array") of [pseudorandom numbers](Pseudorandom_Number_Generator "Pseudorandom Number Generator") [[11]](#cite_note-11) [[12]](#cite_note-12):



* One number for each [piece](Pieces "Pieces") at each [square](Squares "Squares")
* One number to indicate the [side to move](Side_to_move "Side to move") is black
* Four numbers to indicate the [castling rights](Castling_Rights "Castling Rights"), though usually 16 (2^4) are used for speed
* Eight numbers to indicate the [file](Files "Files") of a valid [En passant](En_passant "En passant") square, if any


This leaves us with an array with 781 (12\*64 + 1 + 4 + 8) random numbers. Since pawns don't happen on first and eighth rank, one might be fine with 12\*64 though. There are even proposals and implementations to use overlapping keys from unaligned access up to an array of only 12 numbers for every piece and to rotate that number by square [[13]](#cite_note-13) [[14]](#cite_note-14) .


Programs usually implement their own [Pseudorandom number generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator") (PRNG), both for better quality random numbers than standard library functions, and also for reproducibility. This means that whatever platform the program is run on, it will use the exact same set of Zobrist keys. This is also useful for things like opening books, where the positions in the book can be stored by hash key and be used portably across machines, considering [endianness](Endianness "Endianness").



## Runtime


If we now want to get the Zobrist hash code of a certain position, we initialize the hash key by [xoring](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") all random numbers linked to the given feature, e.g. the [initial position](Initial_Position "Initial Position"):




```

[Hash for White Rook on a1] xor [Hash for White Knight on b1] xor [Hash for White Bishop on c1] xor ... ( all pieces )
... xor [Hash for White king castling] xor [Hash for White queeb castling] xor ... ( all castling rights )

```

The fact that xor-operation is [own inverse](https://en.wikipedia.org/wiki/Involution) and can be undone by using the same xor-operation again, is often used by chess engines. It allows a fast [incremental update](Incremental_Updates "Incremental Updates") of the hash key during [make](Make_Move "Make Move") or [unmake](Unmake_Move "Unmake Move") [moves](Moves "Moves"). E.g., for a White Knight that jumps from b1 to c3 capturing a Black Bishop, these operations are performed:




```

[Original Hash of position] xor [Hash for White Knight on b1] ... ( removing the knight from b1 )
... xor [Hash for Black Bishop on c3] ( removing the captured bishop from c3 )
... xor [Hash for White Knight on c3] ( placing the knight on the new square )
... xor [Hash for Black to move] ( change sides)

```

## Collisions


[Key collisions](Transposition_Table#KeyCollisions "Transposition Table") or type-1 errors are inherent in using Zobrist keys with far less bits than required to encode all reachable chess positions.



### Theory


An important issue is the question of what size the hash keys should have. Smaller hash keys are faster and more space efficient, while larger ones reduce the risk of a hash collision. A collision occurs if two positions map the same key [[15]](#cite_note-15) . The dangers of which were well assessed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") in their paper *Hash Collisions Effect* [[16]](#cite_note-16). Usually 64bit are used as a standard size in modern chess programs.


Hash collisions demonstrate the [birthday "paradox"](https://en.wikipedia.org/wiki/Birthday_problem), which is to say the chance of collisions approaches certainty at around the **square root** of the number of possible keys, contrary to some people's expectations. You can expect to encounter a collision in a 32 bit hash when you have evaluated sqrt(2 ^ 32) == 2 ^ 16 or around 65 thousand positions. With a 64 bit hash, you can expect a collision after about 2 ^ 32 or 4 billion positions.



### Praxis


Post by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") [[17]](#cite_note-17) :




```
... I can speak from experience here. In the early versions of my chess program [Phoenix](Phoenix "Phoenix"), I generated my Zobrist hash numbers using my student id number as a seed, naively thinking the random numbers generated by this seed would be good enough. A few years later I put code in to detect when my 32-bit hash key matched the wrong position. To my surprise, there were **lots** of errors. I changed my seed to another number and the error rate dropped dramatically. With this better seed, it became very, very rare to see a hash error. All randomly generated numbers are not the same! 

```

### Lack a True Integer Type


Some languages (such as [JavaScript](JavaScript "JavaScript") and [Lua](https://en.wikipedia.org/wiki/Lua_%28programming_language%29)) only have a [64-bit floating point](Double "Double") "Number" type. In JavaScript, this type breaks down into a 32 bit integer when bitwise operators are used. One way to get a 64 bit hash is to use two 32 bit numbers in parallel, as [Garbochess-JS](Garbochess-JS "Garbochess-JS") [[18]](#cite_note-18) does. Another, which [p4wn](P4wn "P4wn") used at one stage, is to use 47 or 48 bit **additive** hashes. 64 bit floating point numbers are true integers up to 53 bits, so it is possible to sum at least 32 (and on average close to 64) random 48 bit numbers, which was enough for p4wn's purposes. For additive Zobrist hashing, you add the number when placing a piece and subtract it when removing it, rather than using xor both ways. There is no difference in accuracy or speed, and 48 bit hashes give you collisions at around the 2 ^ 24 or 16 million point.



### Linear Independence


The minimum and average [Hamming Distance](Population_Count#HammingDistance "Population Count") over all Zobrist keys was often considered as "quality"-measure of the keys. However, maximizing the minimal hamming distance leads to very poor Zobrist keys. As long the minimum hamming distance is greater zero, [linear independence](https://en.wikipedia.org/wiki/Linear_independence) (that is a small subset of all keys doesn't xor to zero), is much more important than hamming distance as explained by [Sven Reichard](Sven_Reichard "Sven Reichard") [[19]](#cite_note-19) :


Assume we associate a bitstring to every piece-square combination. That is what's usually done in chess programs; some codes are added for the side to move, castling rights, e.p. squares, etc. We obtain the code of a position by xor-ing the codes of all the pieces contained in it.


What we want to avoid is collisions at nodes close to the root. For nodes close to the leaves the cost of recomputing the score is smaller. Hence we want to avoid that:




```C++

x1^x2^...^xm = y1^y2^...^yn
for codes xi, yi and small number m and n, and xi not equal to yj

```

To translate that to a language that is more familiar - at least for people of a mathematical background - we consider the [field F2](https://en.wikipedia.org/wiki/Field_%28mathematics%29#Finite_fields) of two elements. The elements are 0 and 1, and we can add and multiply them as usual, with the additional rule that 1 + 1 = 0. This is really a field, just like the [real](https://en.wikipedia.org/wiki/Real_number) or [complex numbers](https://en.wikipedia.org/wiki/Complex_number), and we can do calculations as usual. Note that addition is just the exclusive or.


Now the codes or bitstrings become [vectors](https://en.wikipedia.org/wiki/Vector_%28mathematics_and_physics%29) over the field F2, and the bitwise exclusive or becomes componentwise addition, i.e., usual addition of vectors. All these vectors form the [vector space](https://en.wikipedia.org/wiki/Vector_space) F2^k, where k is the length of the vectors. Typically, k = 64.


So, what we want to avoid is an equation




```C++

x1 + x2 + ... + xm = y1 + y2 + ... + yn

```

or




```C++

x1 + x2 + ... + xm + y1 + y2 + ... + yn = 0

```

since in F2, subtraction is the same as addition. Remembering some [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra), this just means that we want the set x1,...,xm,y1,...,yn to be linearly independent.


This leads to the following criterion for picking a set of hashcodes: A set of vectors in F2^k is a good set of hash codes if each small subset of non-zero vectors is linearly independent. What is not clear here is the meaning of "small", but we want small to be as big as possible. In other words, we consider sets of size up to a certain size as small, and if we can make that size bigger, it is better, since this leads to unique codes deeper in the tree.


However what is clear is that this quality criterion does not depend on the base of the vector space. I.e., if we have a good set and multiply each vector by an invertible matrix (in other words, if we rotate the vectors), the obtained set will be just as good, since the rotation does not change the linear independence. The Hamming distance, on the other hand, is highly dependent on the vector space base. Take for example the vectors (1,0) and (0,1) in F2^2; they have Hamming distance 2. If we multiply both of them by




```C++

(1 1)
(0 1)

```

we get (1,1) and (0,1), which have Hamming distance 1. Actually we can change any distance to anything else (except for 0) by an appropriate matrix. Thus we try to approximate something that is independent from the base (the quality of our hash codes) by something that depends on it (the Hamming distance). Simple logic tells you that this approximation has to be real bad. An example where it doesn't work: It has been said that the Hamming distance shouldn't be to small or to big. So, vectors at a distance which is half the length should be ok, right? Let the length be 8 (I don't want to type too many 0's and 1's), and consider the vectors




```C++

11110000
11001100
00111100

```

They all have weight 4, their pairwise distance is 4, and yet they add up to 0. Just by looking at Hamming distances, you have no chance of detecting that.


Summarizing I can say that I see no connection between the quality of hash codes and their Hamming distance. Using a good RNG like the one provided in GNU's stdlib will yield good hash codes ( you can actually prove that), and so I will take the codes as they are supplied by rand() or random() without messing with them and thereby most likely make them worse. 



## See also


* [CPW-Engine\_transposition](CPW-Engine_transposition "CPW-Engine transposition")
* [BCH Hashing](BCH_Hashing "BCH Hashing")


## Publications


* [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (1990) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
* [J. Lawrence Carter](Mathematician#JLCarter "Mathematician"), [Mark N. Wegman](Mathematician#MNWegman "Mathematician") (**1977**). *[Universal classes of hash functions](http://dl.acm.org/citation.cfm?id=803400)*. [STOC '77](http://dl.acm.org/citation.cfm?id=800105)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.craftychess.com/hyatt/collisions.html)*. [ICGA Journal, Vol. 28., No. 3](ICGA_Journal#28_3 "ICGA Journal")
* [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The Representation of Chess Game](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1491153)*. Proceedings of the 27th International Conference on Information Technology Interfaces
* [Mihai Pătrașcu](Mathematician#MPatrascu "Mathematician"), [Mikkel Thorup](Mathematician#MThorup "Mathematician") (**2011**). *The Power of Simple Tabulation Hashing*. [arXiv:1011.5200v2](http://arxiv.org/abs/1011.5200)


## Forum Posts


### 1982 ...


* [compact representation of chess positions](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_duke.1593_net.chess.txt) by [Tom Truscott](Tom_Truscott "Tom Truscott"), net.chess, January 7, 1982


### 1990 ...


* [Hash tables - Clash!!! What happens next?](https://groups.google.com/d/msg/rec.games.chess/h9Q2wik_kTg/Jq7rYE0vqtoJ) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 15, 1994


 [Re: Hash tables - Clash!!! What happens next?](https://groups.google.com/d/msg/rec.games.chess/h9Q2wik_kTg/9zrP0flwuzAJ) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), March 17, 1994
* [Collision probability](https://groups.google.com/d/msg/rec.games.chess.computer/C53jRusegwA/XzgyZLbzcn8J) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 15, 1996
* [Re: Berliner vs. Botvinnik Some interesting points](https://groups.google.com/d/msg/rec.games.chess.computer/JZ-_0rObjuQ/Mfwy9qBLxoAJ) by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 6, 1996
* [Re: Hashing function for board positions](https://groups.google.com/d/msg/rec.games.chess.computer/oKgv-7WbfO0/TH-p0KUIo2kJ)by [Jim Gillogly](James_Gillogly "James Gillogly"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 12, 1997
* [Fast hash algorithm](https://www.stmintz.com/ccc/index.php?id=13810) by John Scalo, [CCC](CCC "CCC"), January 08, 1998
* [Fast hash key method - Revisited!](https://www.stmintz.com/ccc/index.php?id=14053) by John Scalo, [CCC](CCC "CCC"), January 14, 1998
* [How to create a set of random integers for hashing?](https://www.stmintz.com/ccc/index.php?id=29817) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 18, 1998


### 2000 ...


* [Why Random Number Needed In HashFunction[piece](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/587d039679461fb8)[position]] by Cheok Yan Cheng, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 12, 2001
* [About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200366) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 04, 2001
* [Random keys and hamming distance](https://www.stmintz.com/ccc/index.php?id=245775) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), August 16, 2002
* [Hamming distance and lower hash table indexing](https://www.stmintz.com/ccc/index.php?id=313807) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), September 02, 2003
* [64-Bit random numbers](https://www.stmintz.com/ccc/index.php?id=324223) by [Martin Schreiber](index.php?title=Martin_Schreiber&action=edit&redlink=1 "Martin Schreiber (page does not exist)"), [CCC](CCC "CCC"), October 28, 2003
* [Is it necessary to include empty fields in the hash key of a position?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/42c6f293450dba50/) by Frank Hablizel, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2003
* [Hashkey collisions (typical numbers)](https://www.stmintz.com/ccc/index.php?id=358836) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), April 07, 2004


### 2005 ...


* [Zobrist key random numbers](http://www.talkchess.com/forum/viewtopic.php?t=26152) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 21, 2009
* [Incremental Zobrist - slow?](http://www.talkchess.com/forum/viewtopic.php?t=28523) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), June 20, 2009 » [Incremental Updates](Incremental_Updates "Incremental Updates")
* [On Zobrist keys](http://talkchess.com/forum/viewtopic.php?t=28545) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), June 21, 2009
* [Overlapped Zobrist keys array](http://www.talkchess.com/forum/viewtopic.php?t=30008) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), October 06, 2009


### 2010 ...


* [Transposition table random numbers](http://www.talkchess.com/forum/viewtopic.php?t=35415) by Justin Madru, [CCC](CCC "CCC"), July 13, 2010
* [TT Key Collisions, Workarounds?](http://www.talkchess.com/forum/viewtopic.php?t=40062) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), August 16, 2011
* [Key collision handling](http://www.talkchess.com/forum/viewtopic.php?t=40849) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson"), [CCC](CCC "CCC"), October 21, 2011
* [Using a Transposition Table with Zobrist Keys](http://www.open-chess.org/viewtopic.php?f=5&t=1872) by Miyagi403, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 21, 2012
* [MT or KISS ?](http://www.talkchess.com/forum/viewtopic.php?t=43910) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), June 02, 2012 [[20]](#cite_note-20) [[21]](#cite_note-21) [[22]](#cite_note-22)
* [Zobrist alternative?](http://www.talkchess.com/forum/viewtopic.php?t=44043) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 12, 2012
* [Zobrist Number Statistics and WHat to Look For](http://www.talkchess.com/forum/viewtopic.php?t=45605) by Andrew Templeton, [CCC](CCC "CCC"), October 16, 2012
* [Question about Zobrist code](http://www.open-chess.org/viewtopic.php?f=5&t=2178) by Hamfer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 19, 2012


### 2015 ...


* [Zobrist keys - measure of quality?](http://www.talkchess.com/forum/viewtopic.php?t=55449) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 24, 2015
* [On-the fly hash key generation?](http://www.talkchess.com/forum/viewtopic.php?t=58890) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 12, 2016


 [Re: On-the fly hash key generation?](http://www.talkchess.com/forum/viewtopic.php?t=58890&start=13) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), January 13, 2016
* [Rotated hash](http://www.talkchess.com/forum/viewtopic.php?t=61411) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), September 13, 2016
* [No Zobrist key](http://www.talkchess.com/forum/viewtopic.php?t=61533) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), September 26, 2016
* [Enpass + Castling for Zorbist hashes](http://www.talkchess.com/forum/viewtopic.php?t=62733) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 06, 2017 » [Castling Rights](Castling_Rights "Castling Rights"), [En passant](En_passant "En passant")
* [Zobrist hashing for text](http://www.talkchess.com/forum/viewtopic.php?t=66372) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), January 20, 2018


### 2020 ...


* [Zobrist key independence](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73110) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 17, 2020
* [Best practices for transposition tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76508) by Brian Adkins, [CCC](CCC "CCC"), February 06, 2021


## External Links


* [Zobrist hashing from Wikipedia](https://en.wikipedia.org/wiki/Zobrist_hashing)
* [Tabulation hashing from Wikipedia](https://en.wikipedia.org/wiki/Tabulation_hashing)
* [Zobrist keys](http://web.archive.org/web/20070810003508/www.seanet.com/%7Ebrucemo/topics/zobrist.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
* [Zobrist keys](http://mediocrechess.blogspot.com/2007/01/guide-zobrist-keys.html) from [Mediocre Chess](http://mediocrechess.blogspot.com/) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson")
* [Gödel numbering from Wikipedia](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)
* [John Cage](Category:John_Cage "Category:John Cage") - [Music of Changes](https://en.wikipedia.org/wiki/Music_of_Changes), Book 1 (1951), performed by [Vicky Chow](https://www.facebook.com/vickychowpianist), [DiMenna Center](https://www.facebook.com/DiMennaCenter), [NYC](https://en.wikipedia.org/wiki/New_York_City), June 09, 2012, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [King Wen sequence](https://en.wikipedia.org/wiki/King_Wen_sequence), [I Ching](https://en.wikipedia.org/wiki/I_Ching) [divination](https://en.wikipedia.org/wiki/I_Ching_divination) involves obtaining a [Hexagram](https://en.wikipedia.org/wiki/Hexagram_%28I_Ching%29) by random generation
2. [↑](#cite_ref-2) All of [Cage's](Category:John_Cage "Category:John Cage") [music](https://en.wikipedia.org/wiki/Music_of_Changes) since 1951 was composed using [chance](https://en.wikipedia.org/wiki/John_Cage#Chance) procedures, most commonly using the [I Ching](https://en.wikipedia.org/wiki/I_Ching)
3. [↑](#cite_ref-3) [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (1990) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
4. [↑](#cite_ref-4) [compact representation of chess positions](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_duke.1593_net.chess.txt) by [Tom Truscott](Tom_Truscott "Tom Truscott"), net.chess, January 7, 1982
5. [↑](#cite_ref-5) [Re: Hashing function for board positions](https://groups.google.com/d/msg/rec.games.chess.computer/oKgv-7WbfO0/TH-p0KUIo2kJ)by [Jim Gillogly](James_Gillogly "James Gillogly"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 12, 1997
6. [↑](#cite_ref-6) [Re: Zobrist keys - measure of quality?](http://www.talkchess.com/forum/viewtopic.php?t=55449&start=4) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), February 24, 2015
7. [↑](#cite_ref-7) [J. Lawrence Carter](Mathematician#JLCarter "Mathematician"), [Mark N. Wegman](Mathematician#MNWegman "Mathematician") (**1977**). *[Universal classes of hash functions](http://dl.acm.org/citation.cfm?id=803400)*. [STOC '77](http://dl.acm.org/citation.cfm?id=800105)
8. [↑](#cite_ref-8) [Mihai Pătrașcu](Mathematician#MPatrascu "Mathematician"), [Mikkel Thorup](Mathematician#MThorup "Mathematician") (**2011**). *The Power of Simple Tabulation Hashing*. [arXiv:1011.5200v2](http://arxiv.org/abs/1011.5200)
9. [↑](#cite_ref-9) [Tabulation hashing from Wikipedia](https://en.wikipedia.org/wiki/Tabulation_hashing)
10. [↑](#cite_ref-10) [Picture gallery "Recognition and Success 1955 - 1972"](http://www.mcescher.com/Gallery/gallery-recogn.htm)  from [The Official M.C. Escher Website](http://www.mcescher.com/)
11. [↑](#cite_ref-11) [RANDOM.ORG - Integer Generator](http://www.random.org/integers/?mode=advanced)
12. [↑](#cite_ref-12) [The Marsaglia Random Number CDROM including the Diehard Battery of Tests](http://www.stat.fsu.edu/pub/diehard/) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician")
13. [↑](#cite_ref-13) [Re: Zobrist key random numbers](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=245932&t=26152) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), January 22, 2009
14. [↑](#cite_ref-14) [Overlapped Zobrist keys array](http://www.talkchess.com/forum/viewtopic.php?t=30008) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), October 06, 2009
15. [↑](#cite_ref-15) [Hashkey collisions (typical numbers)](https://www.stmintz.com/ccc/index.php?id=358836) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), April 07, 2004
16. [↑](#cite_ref-16) [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.craftychess.com/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
17. [↑](#cite_ref-17) [Re: Hash tables - Clash!!! What happens next?](https://groups.google.com/d/msg/rec.games.chess/h9Q2wik_kTg/9zrP0flwuzAJ) by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), March 17, 1994
18. [↑](#cite_ref-18) [Garbochess-JS](http://forwardcoding.com/projects/ajaxchess/chess.html)
19. [↑](#cite_ref-19) [Re: About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200622) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), December 05, 2001
20. [↑](#cite_ref-20) [Mersenne twister from Wikipedia](https://en.wikipedia.org/wiki/Mersenne_twister)
21. [↑](#cite_ref-21) [64-bit KISS RNGs](http://compgroups.net/comp.lang.fortran/64-bit-kiss-rngs/601519) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician"), [comp.lang.fortran | Computer Group](http://compgroups.net/comp.lang.fortran/), February 28, 2009
22. [↑](#cite_ref-22) [RKISS](Bob_Jenkins#RKISS "Bob Jenkins") by [Bob Jenkins](Bob_Jenkins "Bob Jenkins")

**[Up one Level](Transposition_Table "Transposition Table")**







 
