---
title: De Bruijn Sequence Generator
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Algorithms](Algorithms "Algorithms") * [Backtracking](Backtracking "Backtracking") * De Bruijn Sequence Generator**

A [recursive](Recursion "Recursion") backtracking implementation of a [64-bit](Bitboards "Bitboards") [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence") generator in [C++](Cpp "Cpp"), to build a "private" [bitScanForward](BitScan#DeBruijnMultiplation "BitScan")-routine. Compile the program, and start it with a parameter between 1 and 67108864 (2^26). Test-output with some "unique" private number. By [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg").

## Program Output

```C++
C:\source\DeBruijn>debruijn 4061955

const BitBoard magic = 0x022fdd63cc95386d; // the 4061955.

const unsigned int magictable[64] =
{
    0,  1,  2, 53,  3,  7, 54, 27,
    4, 38, 41,  8, 34, 55, 48, 28,
   62,  5, 39, 46, 44, 42, 22,  9,
   24, 35, 59, 56, 49, 18, 29, 11,
   63, 52,  6, 26, 37, 40, 33, 47,
   61, 45, 43, 21, 23, 58, 17, 10,
   51, 25, 36, 32, 60, 20, 57, 16,
   50, 31, 19, 15, 30, 14, 13, 12,
};

unsigned int bitScanForward (BitBoard b) {
    return magictable[((b&-b)*magic) >> 58];
}

```

## Source

```C++
##include <stdio.h>
##include <stdlib.h>
##include <time.h>

typedef unsigned __int64 U64; // long long

class CGenBitScan
{
public:
   //==========================================
   // constructor immediately starts the search
   //==========================================
   CGenBitScan(int match4nth) {
      clock_t start, stop;
      m_dBCount = 0;
      m_Match4nth  = match4nth;
      initPow2();
      start = clock();
      m_Lock = pow2[32]; // optimization to exclude 32, see remarks 
      try {findDeBruijn(0, 64-6, 0, 6);} catch(int){}
      stop = clock();
      printf("\n%.3f Seconds for %d De Bruijn Sequences found\n", (float)(stop - start) / CLOCKS_PER_SEC, m_dBCount);
   }

private:
   U64 pow2[64];    // single bits
   U64 m_Lock;      // locks each bit used
   int m_dBCount;   // counter
   int m_Match4nth; // to match

   //==========================================
   // on the fly initialization of pow2
   //==========================================
   void initPow2()  {
      pow2[0] = 1;
      for (int i=1; i < 64; i++)
         pow2[i] = 2*pow2[i-1];
   }

   //==========================================
   // print the bitscan routine and throw
   //==========================================
   void bitScanRoutineFound(U64 deBruijn) {
      int index[64], i;
      for (i=0; i<64; i++) // init magic array
         index[ (deBruijn<<i) >> (64-6) ] = i;
      printf("\nconst U64 magic = 0x%08x%08x; // the %d.\n\n",
              (int)(deBruijn>>32), (int)(deBruijn), m_dBCount);
      printf("const unsigned int magictable[64] =\n{\n");
      for (i=0; i<64; i++) {
         if ( (i & 7) == 0 ) printf("\n  ");
         printf(" %2d,", index[i]);
      }
      printf("\n};\n\nunsigned int bitScanForward (U64 b) {\n");
      printf("    return magictable[((b&-b)*magic) >> 58];\n}\n");
      // throw 0; // unwind the stack until catched
   }

   //============================================
   // recursive search
   //============================================
   void findDeBruijn(U64 seq, int depth, int vtx, int nz) {
      if ( (m_Lock & pow2[vtx]) == 0 && nz <= 32 ) { // only if vertex is not locked
         if ( depth == 0 ) { // depth zero, De Bruijn Sequence found, see remarks
            if ( ++m_dBCount == m_Match4nth )
               bitScanRoutineFound(seq);
         } else {
            m_Lock ^= pow2[vtx]; // set bit, lock the vertex to don't appear multiple
            if ( vtx == 31 && depth > 2 ) { // optimization, see remarks
                findDeBruijn( seq | pow2[depth-1], depth-2, 62, nz+1);
            } else {
                findDeBruijn( seq, depth-1, (2*vtx)&63, nz+1); // even successor
                findDeBruijn( seq | pow2[depth-1], depth-1, (2*vtx+1)&63, nz); // odd successor
            }
            m_Lock ^= pow2[vtx]; // reset bit, unlock
         }
      }
   }
};

int main(int argc, char* argv[])
{
   if (argc < 2)
      printf("usage: genBitScan 1 .. %d\n", 1<<26);
   else
      CGenBitScan(atoi(argv[1]));
   return 0;
}

```

## Remarks

With findDeBruijn(0, 64-6, 0, 6), starting with six leading zeros on its most significant top, the routine has 58 decrements to reach depth zero claiming a found De Bruijn Sequence. The algorithm does not explicitly prove the uniqueness of six remaining indices which result from the up to five trailing hidden zeros with 100000B = 32 as least significant subsequence. However, the constraints of the odd De Bruin sequence seem strong enough to make that test redundant, that is proving 64-6 unique keys seems sufficient.

As demonstrated in the [De Bruijn Graph on a Chess Board](De_Bruijn_Sequence#BruijnGraphChessBoard "De Bruijn Sequence"), there are two branch-less series {32, 0, 1} and {31, 63, 62} respectively. The recursive search routine performs some kind of pruning and reductions to take advantage of that. 63 to follow 31 must not be locked and skipped for the 62 with an extra depth reduction. 32 can not appear as index inside the 58 recursive tests in one path, and is therefor locked initially before the findDeBruijn(0, 64-6, 0, 6) call.

A small improvement was introducing an additional parameter for the number of binary zeros to check it not to become greater 32. This makes also the depth > 0 condition for the even successors no longer necessary, to enumerate all 2^26 De Bruijn Sequences.

## Forum Posts

- [De Bruijn Sequence Generator](https://www.stmintz.com/ccc/index.php?id=339184) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), December 30, 2003

## [Re: De Bruijn Sequence Generator](https://www.stmintz.com/ccc/index.php?id=339225) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), December 30, 2003 » [BitScan](BitScan "BitScan") External Links

- [De Bruijn sequence from Wikipedia](https://en.wikipedia.org/wiki/De_Bruijn_sequence)
- [De Bruijn Sequence Generator](https://sites.google.com/site/sydfhd/articles-tutorials/de-bruijn-sequence-generator) from [Syed Fahad's](Syed_Fahad "Syed Fahad") Website

**[Up one Level](Backtracking "Backtracking")**

