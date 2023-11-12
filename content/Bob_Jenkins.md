---
title: Bob Jenkins
---
**[Home](Home "Home") * [People](People "People") * Bob Jenkins**

[](http://burtleburtle.net/bob/) Bob Jenkins <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Robert John Jenkins Jr.**,

an American computer scientist, software developer, M.Sc. in CS from [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), and [Microsoft](Microsoft "Microsoft") and former [Oracle](https://en.wikipedia.org/wiki/Oracle_Corporation) employee. At Microsoft, he worked in the *Cosmos* team <a id="cite-note-2" href="#cite-ref-2">[2]</a> , and under [Andrew Kadatch](Andrew_Kadatch "Andrew Kadatch") on the *Cosmos* storage distributed [file system](https://en.wikipedia.org/wiki/File_system) <a id="cite-note-3" href="#cite-ref-3">[3]</a> , written by Andrew in [C++](Cpp "Cpp"), and on the *Scope* query language <a id="cite-note-4" href="#cite-ref-4">[4]</a> . He was Oracle's resident expert on [hash functions](https://en.wikipedia.org/wiki/Hash_function) <a id="cite-note-5" href="#cite-ref-5">[5]</a> , and he designed and published various [pseudorandom number generators](Pseudorandom_Number_Generator "Pseudorandom Number Generator") and hash functions for [hash table lookup](Hash_Table "Hash Table") <a id="cite-note-6" href="#cite-ref-6">[6]</a> , competing with [Paul Hsieh](Paul_Hsieh "Paul Hsieh") <a id="cite-note-7" href="#cite-ref-7">[7]</a> .

## RKISS

Bob Jenkins' small noncryptographic PRNG approach is suited for [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing"). [Heinz van Saanen's](index.php?title=Heinz_van_Saanen&action=edit&redlink=1 "Heinz van Saanen (page does not exist)") RKISS as used in [Stockfish](Stockfish "Stockfish") since version 2.0 <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> uses almost the same code despite embedded it into a C++ class and initialization <a id="cite-note-10" href="#cite-ref-10">[10]</a>. Van Saanen admitted he took an obviously free and quite raw C-snippet from a random-related newsgroup long time ago. When turned this to a functional C++-class years later he could not find the initial source any longer, and gave credit to [George Marsaglia](Mathematician#GMarsaglia "Mathematician") as inventor of the RNG-Kiss-family <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>. This is Bob's 64 bit code <a id="cite-note-15" href="#cite-ref-15">[15]</a>:

```C++
If you want to use 8-byte terms instead of 4-byte terms, the proper rotate amounts are (39,11) for the two-rotate version (yielding at least 13.3 bits of [avalanche](https://en.wikipedia.org/wiki/Avalanche_effect) after 5 rounds) or (7,13,37) for the three-rotate version (yielding 18.4 bits of avalanche after 5 rounds). I think I'd got with the three-rotate version, because the ideal is 32 bits of avalanche, and 13.3 isn't even half of that. 

```

```C++

typedef unsigned long long u8;
typedef struct ranctx { u8 a; u8 b; u8 c; u8 d; } ranctx;

##define rot(x,k) (((x)<<(k))|((x)>>(64-(k))))
u8 ranval( ranctx *x ) {
    u8 e = x->a - rot(x->b, 7);
    x->a = x->b ^ rot(x->c, 13);
    x->b = x->c + rot(x->d, 37);
    x->c = x->d + e;
    x->d = e + x->a;
    return x->d;
}

void raninit( ranctx *x, u8 seed ) {
    u8 i;
    x->a = 0xf1ea5eed, x->b = x->c = x->d = seed;
    for (i=0; i<20; ++i) {
        (void)ranval(x);
    }
}

```

## Selected Publications

- Bob Jenkins (**1997**). *Hash functions*. [Dr. Dobb's Journal](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal), September 1997
- Ronnie Chaiken, Bob Jenkins, Per-Åke Larson, Bill Ramsey, Darren Shakib, Simon Weaver, Jingren Zhou (**2008**). *[SCOPE: Easy and Efficient Parallel Processing of Massive Data Sets](https://dl.acm.org/citation.cfm?id=1454166)*. [Microsoft Corporation](Microsoft "Microsoft"), [pdf](https://www.goland.org/Scope-VLDB-final.pdf)
- [Andrew Kadatch](Andrew_Kadatch "Andrew Kadatch"), Bob Jenkins (**2010**). *[Everything we know about CRC but afraid to forget](https://www.researchgate.net/publication/268184499_Everything_we_know_about_CRC_but_afraid_to_forget)*. <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a>

## External Links

- [Robert John Jenkins Junior from Wikipedia](https://en.wikipedia.org/wiki/Robert_John_Jenkins_Junior)
- [Bob Jenkins' Web Site](http://burtleburtle.net/bob/)
- [Random Number Results](http://burtleburtle.net/bob/rand/index.html)
- [Hash Functions and Block Ciphers](http://burtleburtle.net/bob/hash/index.html)
- [A Hash Function for Hash Table Lookup](http://burtleburtle.net/bob/hash/doobs.html) updated [Dr. Dobb's](https://en.wikipedia.org/wiki/Dr._Dobb%27s_Journal) article
- [Perfect Hashing](http://burtleburtle.net/bob/hash/perfect.html)
- [Jenkins hash function from Wikipedia](https://en.wikipedia.org/wiki/Jenkins_hash_function)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Bob Jenkins' Web Site](http://burtleburtle.net/bob/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Stuff Yaron Finds Interesting - What is Microsoft's Cosmos service?](http://www.goland.org/whatiscosmos/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Dryad - Microsoft Research](http://research.microsoft.com/en-us/projects/dryad/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ronnie Chaiken](http://www.linkedin.com/pub/ronnie-chaiken/26/571/143), Bob Jenkins, [Per-Åke Larson](http://research.microsoft.com/en-us/people/palarson/), [Bill Ramsey](http://portal.acm.org/author_page.cfm?id=81344496896&coll=DL&dl=ACM&trk=0&cfid=28619666&cftoken=49088236), [Darren Shakib](http://www.microsoft.com/presspass/exec/de/Shakib/default.mspx), [Simon Weaver](http://www.linkedin.com/in/simonjweaver), [Jingren Zhou](http://research.microsoft.com/en-us/um/people/jrzhou/) (**2008**). *[SCOPE: Easy and Efficient Parallel Processing of Massive Data Sets](http://portal.acm.org/citation.cfm?id=1454166)*. [Microsoft Corporation](Microsoft "Microsoft"), [pdf](http://www.goland.org/Scope-VLDB-final.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Resume for Bob Jenkins](http://burtleburtle.net/bob/other/resume3.html)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Hash Functions for Hash Table Lookup](http://burtleburtle.net/bob/hash/evahash.html), Robert J. Jenkins Jr., 1995-1997
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Hash functions](http://www.azillionmonkeys.com/qed/hash.html) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Stockfish Blog - Stockfish 2.0](http://blog.stockfishchess.com/)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [RKISS](http://www.talkchess.com/forum/viewtopic.php?t=37406) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 01, 2011
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [RKISS copyright?](http://www.talkchess.com/forum/viewtopic.php?start=0&t=38313) by Giorgio Medeot, [CCC](CCC "CCC"), March 07, 2011
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [64-bit KISS RNGs](http://compgroups.net/comp.lang.fortran/64-bit-kiss-rngs/601519) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician"), [comp.lang.fortran | Computer Group](http://compgroups.net/comp.lang.fortran/), February 28, 2009
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: RKISS copyright?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=398196&t=38313) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), March 09, 2011
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [RANDOM.ORG - Integer Generator](http://www.random.org/integers/?mode=advanced)
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [The Marsaglia Random Number CDROM including the Diehard Battery of Tests](http://www.stat.fsu.edu/pub/diehard/)
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [A small noncryptographic pseudorandom number generator - 64-bit variants](http://www.burtleburtle.net/bob/rand/smallprng.html) by Bob Jenkins
1. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Cyclic redundancy check from Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
1. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Mathematics of CRC from Wikipedia](https://en.wikipedia.org/wiki/Mathematics_of_CRC)

**[Up one level](People "People")**

