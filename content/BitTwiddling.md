---
title: BitTwiddling
---
**[Home](Home "Home") * [Programming](Programming "Programming") * Bit-Twiddling**

**Bit-twiddling** is a family of techniques used in [manipulating](https://en.wikipedia.org/wiki/Bit_manipulation) integers in a non-obvious manner in order to obtain a result either more quickly or with less code. Bit-twiddling is often associated with [bitboards](Bitboards "Bitboards"), but there are both easy-to-read [bitboard](Bitboards "Bitboards") implementations and difficult-to-read implementations of other board representations.

## Bit-Twiddling related to Bitboards

- [BitScan](BitScan "BitScan")
- [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
- [Obtaining and Clearing the Least Significant Bit (LS1B)](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")
- [Population Count](Population_Count "Population Count")
- [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")

## Bit-Manipulation

- [ABM](SSE4#ABM "SSE4")
- [BMI1](BMI1 "BMI1")
- [BMI2](BMI2 "BMI2")
- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
- [TBM](TBM "TBM")

## Forum Posts

- [Bit twiddlement question: greater of two popcounts](http://talkchess.com/forum/viewtopic.php?t=29269) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 06, 2009
- [Bit twiddling question, part 2: arbitrary bitscan order](http://talkchess.com/forum/viewtopic.php?t=29333) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 11, 2009
- [Bit position hack](http://www.open-chess.org/viewtopic.php?f=5&t=2419) by nak3c, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 01, 2013

## Important online resources

Online Papers by [Donald Knuth](Donald_Knuth "Donald Knuth"):

- [Preprints of Recent Papers](http://www-cs-faculty.stanford.edu/%7Eknuth/preprints.html) including [dancing links](https://en.wikipedia.org/wiki/Dancing_Links)
- [The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html)

**Vol 4** as Pre-Fascicle PostScripts:

- [Pre-Fascicle 0b (Boolean basics)](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc0b.ps.gz)
- [Pre-Fascicle 0c (Boolean evaluation)](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc0c.ps.gz)
- [Pre-Fascicle 1a (Bitwise tricks and techniques)](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz)

Online Papers by [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.")

- [Hacker’s Delight](Henry_S._Warren,_Jr.#HackersDeligh "Henry S. Warren, Jr."), [2nd Edition](http://www.informit.com/store/product.aspx?isbn=0321842685)
- [Sample section of Hacker's Delight, Chapter 2 Basics](http://www.hackersdelight.org/basics1.pdf) (pdf)
- [C code for most of the programs that appear in HD](http://www.hackersdelight.org/hdcode.htm)

## Other Bit-Twiddling resources

- Michael Beeler, [Bill Gosper](Bill_Gosper "Bill Gosper"), [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](https://dspace.mit.edu/handle/1721.1/6086)*, Memo 239, Artificial Intelligence Laboratory, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")

[HAKMEMC -- HAKMEM Programming hacks in C](http://www.cl.cam.ac.uk/~am21/hakmemc.html) by [Alan Mycroft](http://www.cl.cam.ac.uk/~am21/)
[HAKMEM from Wikipedia](https://en.wikipedia.org/wiki/HAKMEM)

- [Matters Computational - ideas, algorithms, source code](http://www.jjj.de/fxt/fxtbook.pdf) (pdf) Ideas and Source Code by [Jörg Arndt](Mathematician#Arndt "Mathematician")
- [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC) by [Hank Dietz](Hank_Dietz "Hank Dietz")
- [Bit Twiddling Hacks](http://graphics.stanford.edu/%7Eseander/bithacks.html) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
- [the bit twiddler](http://bits.stephan-brumme.com/) by [Stephan Brumme](http://www.stephan-brumme.com/)
- [Programming pages](http://programming.sirrida.de) of [Jasper Neumann](http://sourceforge.net/users/jasper_neumann/)
- [GitHub - keon/awesome-bits: A curated list of awesome bitwise operations and tricks](https://github.com/keon/awesome-bits)
- [Bitwise Optimization in Java: Bitfields, Bitboards, and Beyond](https://web.archive.org/web/20050205014648/http://www.onjava.com/pub/a/onjava/2005/02/02/bitsets.html) by [Glen Pepicelli](Glen_Pepicelli "Glen Pepicelli"), ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2005), [O'Reilly's](http://en.wikipedia.org/wiki/O%27Reilly_Media) [OnJava.com](https://web.archive.org/web/20050203015229/http://onjava.com/) » [Java](Java "Java"), [Bitboards](Bitboards "Bitboards")
- [math/bits: an integer bit twiddling library · Issue #18616 · golang/go · GitHub](https://github.com/golang/go/issues/18616) » [Go (Programming Language)](</Go_(Programming_Language)> "Go (Programming Language)")

## External Links

- [Bit twiddler from Wikipedia](https://en.wikipedia.org/wiki/Bit_twiddler)
- [Bit manipulation from Wikipedia](https://en.wikipedia.org/wiki/Bit_manipulation)
- [bit twiddling ...](http://mridulm.blogspot.com/2006/09/bit-twiddling.html) from [Random thoughts](http://mridulm.blogspot.com/) blog by [Mridul Muralidharan](Mridul_Muralidharan "Mridul Muralidharan")
- [Twiddling the Bits](http://zimbry.blogspot.de/) by [David Stafford](David_Stafford "David Stafford")
- [NHØP](Category:NHOP "Category:NHOP") & [Tania Maria](Category:Tania_Maria "Category:Tania Maria") - Baião improvisado, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

**[Up one Level](Programming "Programming")**

