---
title: SSSE3
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86](X86 "X86") \* SSSE3**


**SSSE3** (Supplemental Streaming SIMD Extension 3) is [Intel's](Intel "Intel") name for the [SSE](SSE "SSE") instruction set's fourth iteration. 16 new instructions, also available as [MMX](MMX "MMX")-extension with \_m64 intrinsic datatype. SSSE3 was introduced in [Intel's Core Microarchitecture](https://en.wikipedia.org/wiki/Intel_Core_microarchitecture). SSSE3-intrinsic functions are available in [Visual C](https://en.wikipedia.org/wiki/Visual_C%2B%2B) <a id="cite-note-1" href="#cite-ref-1">[1]</a> or [Intel-C](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler) <a id="cite-note-2" href="#cite-ref-2">[2]</a> .


SSSE3 instructions are not available for [AMD](AMD "AMD") processors until Bulldozer, which also implements [SSE4](SSE4 "SSE4") and [AVX](AVX "AVX").



### PH(ADD/SUB)W


Packed Horizontal Add/Subtract Words. Each of the eight shorts integers is the sum/difference between adjacent pairs of elements in the input parameters. Saturating versions, PHADDSW and PHSUBSW, are also available.


The primary downside of these instructions is that they tend to be very slow multiple-uop instructions on most CPUs, resulting in alternate instruction sequences almost always being faster.



### Intrinsic


\_m128i [\_mm\_hadd\_epi16](http://msdn.microsoft.com/en-us/library/bb514049%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);



### Pseudocode



```C++

signed short a[ 8]; // input a
signed short b[ 8]; // input b
signed short r[ 8]; // output r

for (i=0; i < 4; i++) {
   r[  i] = a[2i] + a[2i+1];
   r[4+i] = b[2i] + b[2i+1];
}

```





### PMADDUBSW


Packed Multiply and Add a vector of 16 unsigned bytes (char) with a vector of 16 signed bytes (not [commutative](https://en.wikipedia.org/wiki/Commutative)! <a id="cite-note-3" href="#cite-ref-3">[3]</a> ). Two consecutive products are added and the saturated signed 16-bit results are stored as vector of eight signed shorts.



### Intrinsic


\_m128i [\_mm\_maddubs\_epi16](http://msdn.microsoft.com/en-us/library/bb514017%28v=vs.100%29.aspx) (\_m128i a, \_m128i b); 



### Pseudocode



```C++

unsigned char  a[16]; // input a
signed   char  b[16]; // input b
signed   short r[ 8]; // output r

for (i=0; i < 8; i++)
   r[i] = SATURATE_16(a[2i]*b[2i] + a[2i+1] * b[2i+1]);

```





### PMULHRSW


Packed Multiply High with Round and Scale is an instruction designed for fixed-point math. It is similar to the existing pmulhw, but only shifts right by 15 instead of 16, and adds a factor for correct rounding.



### Intrinsic


\_m128i [\_mm\_mulhrs\_epi16](http://msdn.microsoft.com/en-us/library/bb513995%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);



### Pseudocode



```C++

signed short a[8]; // input a
signed short b[8]; // input b
signed short r[8]; // output r

for (i=0; i < 8; i++)
   r[i] = INT16((a[i]*b[i] + 0x4000) >> 15);

```





### PSHUFB


Packed Shuffle Bytes is a very powerful instruction that can perform a fast arbitrary byte-shuffle of a register. It can also set some output bytes to zero instead of selecting them from the input. Packed Shuffle Bytes is used inside the [SSSE3 Version of Hyperbola Quintessence](SSSE3#SSSE3Version "SSSE3") to perform byte swaps. There might be some other interesting applications too, such as [SSSE3 Population Count](SSSE3#PopCount "SSSE3"). [VPPERM](XOP#VPPERM "XOP") from [XOP](XOP "XOP") is an even more powerful variant on this instruction.



### Intrinsic


\_m128i [\_mm\_shuffle\_epi8](http://msdn.microsoft.com/en-us/library/bb531427%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);



### Pseudocode



```C++

char a[16]; // input a
char b[16]; // input b
char r[16]; // output r

for (i=0; i < 16; i++)
   r[i] = (b[i] < 0) ? 0 : a[b[i] % 16];

```





### PSIGN


Multiplies each element of one vector with the [sign function](https://en.wikipedia.org/wiki/Sign_function) {-1,0,1} of the second vector. The instruction is available for signed [bytes](Byte "Byte") (8-bit char psignb), signed [words](Word "Word") (16-bit short psignw) and [double words](Double_Word "Double Word") (32-bit int psignd). If both input operands are equal, the result is a vector of absolute values, though PABS is probably preferred for this purpose.



### Intrinsic


\_m128i [\_mm\_sign\_epi8](http://msdn.microsoft.com/en-us/library/bb531461%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);
\_m128i [\_mm\_sign\_epi16](http://msdn.microsoft.com/en-us/library/bb531410%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);
\_m128i [\_mm\_sign\_epi32](http://msdn.microsoft.com/en-us/library/bb514081%28v=vs.100%29.aspx) (\_m128i a, \_m128i b);



### Pseudocode



```C++

/* type := {char, short, int}, N = {16, 8, 4} */
##define N (sizeof(__m128i)/sizeof(type))
type a[N]; // input a
type b[N]; // input b
type r[N]; // output r

for (i=0; i < N; i++)
   r[i] = (b[i] < 0) ? -a[i] : ((b[i] == 0) ? 0 : a[i])

```

## Applications


### SSE3 Population Count


In 2008, [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła") introduced a SSSE3 [Population Count](Population_Count "Population Count") performing a pair of [PSHUFB](SSSE3#PSHUFB "SSSE3") 16 parallel [nibble](Nibble "Nibble") in-xmm lookups <a id="cite-note-4" href="#cite-ref-4">[4]</a>, in the meantime due to [AVX2](AVX2 "AVX2") or [AVX-512](AVX-512 "AVX-512") even possible with doubled or fourfold register widths, competing the native [x86-64](X86-64 "X86-64") [popcount instruction](X86-64#gpinstructions "X86-64") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++

/**
 * popCount2 
 * @author Wojciech Muła
 * @param v vector of two bitboards
 * @return quad word vector of two popcounts
*/
__m128i popCount(__m128i v) {
  __m128i lu = _mm_setr_epi8(0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4);
  __m128i lm = _mm_set1_epi8(0x0f);
  __m128i lo = _mm_and_si128(v, lm);
  __m128i hi = _mm_and_si128(_mm_srli_epi16(v, 4), lm);
  __m128i cl = _mm_shuffle_epi8(lu, lo); /* 16 low nibble counts */
  __m128i ch = _mm_shuffle_epi8(lu, hi); /* 16 high nibble counts */
  __m128i cb = _mm_add_epi8(cl, ch); /* 16 byte counts */
  return _mm_sad_epu8(cb, _mm_setzero_si128());
}

```





### Byte-wise Dot-Product


This SSSE3-dot-product multiplies a vector of 64 unsigned chars with a vector of 64 signed char, and adds all 64 intermediate signed 16-bit products with saturation. It uses the [pmaddubsw](SSSE3#PMADDUBSW "SSSE3") and [phaddsw](SSSE3#PHADDSW "SSSE3") SSSE3 instructions, in total 11 SSE instructions.




```C++

int dotProduct(unsigned char features[], char weights[] /* XMM_ALIGN */) {
   __m128i r0, r1, r2, r3;
   __m128i* a = (__m128i*) features;
   __m128i* b = (__m128i*) weights;
   r0 = _mm_maddubs_epi16 (a[0], b[0]);
   r1 = _mm_maddubs_epi16 (a[1], b[1]);
   r2 = _mm_maddubs_epi16 (a[2], b[2]);
   r3 = _mm_maddubs_epi16 (a[3], b[3]);
   r0 = _mm_adds_epi16    (r0, r1);
   r2 = _mm_adds_epi16    (r2, r3);
   r0 = _mm_adds_epi16    (r0, r2); // 8 shorts
   r0 = _mm_hadds_epi16   (r0, r0); // 4 shorts
   r0 = _mm_hadds_epi16   (r0, r0); // 2 shorts
   r0 = _mm_hadds_epi16   (r0, r0); // 1 final short
   short s = (short)_mm_extract_epi16(r0, 0);
   return (int) s; // sign extended
}

```





### SSSE3 Hyperbola Quintessence


Following routine calculates bishop attacks performing the [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence"). Both [anti-diagonal](Anti-Diagonals "Anti-Diagonals") and [diagonal](Diagonals "Diagonals") attacks are processed in parallel, using both halves of a 128-bit xmm register and pre-calculated [arrays](Array "Array") of bitboard pairs for line-masks, single- and eventually reversed bits. [PSHUFB](SSSE3#PSHUFB "SSSE3") is used to swap bytes inside a [bitboard](Bitboards "Bitboards") <a id="cite-note-6" href="#cite-ref-6">[6]</a> .



### Intrinsic Version



```C++

__m128i diaAntiMaskXMM[64]; // 1 KByte  antidiag : diagonal, excluding square
__m128i singleBitsXMM [64]; // 1 KByte    1<<sq  : 1<<sq
__m128i swapMaskXMM; // needs to be initialized to swap the bytes in both quad-words

// SSSE3 Hyperbola Quintessence
U64 bishopAttacks(U64 occ, enumSquare sq) {
   __m128i o, r, m, b, s;
   m = diaAntiMaskXMM[sq];         // antidiag : diagonal, excluding square
   b = singleBitsXMM [sq];         // bishop bits, equal qwords
   s = swapMaskXMM;
   o = _mm_cvtsi64x_si128  (occ) ; // general purpose 64 bit to xmm low qword
   o = _mm_unpacklo_epi64  (o, o); // occ : occ
   o = _mm_and_si128       (o, m); // o (antidiag : diagonal)
   r = _mm_shuffle_epi8    (o, s); // o'(antidiag : diagonal)
   o = _mm_sub_epi64       (o, b); // o - bishop
   b = _mm_shuffle_epi8    (b, s); // bishop', one may also use singleBitsXMM [sq^56]
   r = _mm_sub_epi64       (r, b); // o'- bishop'
   r = _mm_shuffle_epi8    (r, s); // re-reverse
   o = _mm_xor_si128       (o, r); // attacks
   o = _mm_and_si128       (o, m); // antidiag : diagonal
   r = _mm_unpackhi_epi64  (o, o); // antidiag : antidiag
   o = _mm_add_epi64       (o, r); // diagonal + antidiag
   return _mm_cvtsi128_si64(o);    // convert xmm to general purpose 64 bit
}

```





### Peshkov's Optimization


The pioneer of Hyperbola Quintessence, [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), applies a more sophisticated, optimized [C++](Cpp "Cpp") approach, further utilizing disjoint ray-attacks, and [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") instruction is own inverse and distributive over [mirroring or flipping](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating"). Once per [node](Node "Node") he instantiates an [occupied object](Occupancy "Occupancy") based on a [type-safe](https://en.wikipedia.org/wiki/Type_safety) [curiously recurring template pattern](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern) aka the [Barton–Nackman trick](https://en.wikipedia.org/wiki/Barton%E2%80%93Nackman_trick) to encapsulate the SSE intrinsic data types, to keep a twin of normal and flipped occupancy as base for further [file](Files "Files")-, [diagonal](Diagonals "Diagonals") or [anti-diagonal](Anti-Diagonals "Anti-Diagonals") attack generations, which then requires only one final shuffle per piece attack getter, whether it is a bishop or even a queen.




```C++

class Occupied : public BitSet<Occupied, char_x16_t> {
    typedef BitSet<Occupied, char_x16_t> Base;

    struct Mask {
        value_type singleton;
        value_type file;
        value_type diagonal;
        value_type antidiag;

        Mask operator () (Square);
    };
    typedef Square::const_array<Mask, Mask> CACHE_ALIGN AttackMask;
    static const AttackMask mask;

    struct Shuffle {
        value_type hyperbola;
        value_type flipShift;
        Shuffle ();
    };
    static const Shuffle shuffle;

    static BitBoard bitboard(value_type value) {
        return BitBoard(static_cast<BitBoard::value_type>(_mm_cvtsi128_si64(value)));
    }

    static BitBoard hyperbola(value_type value) {
        value_type reverse = _mm_shuffle_epi8(value, shuffle.hyperbola);
        return bitboard(value ^ reverse); //xor is principal here
    }

    INLINE BitBoard bishopAttack(Square from) const {
        value_type d = value;
        value_type a = value;
        d &= mask[from].diagonal;
        a &= mask[from].antidiag;
        d = _mm_sub_epi64(d, mask[from].singleton);
        a = _mm_sub_epi64(a, mask[from].singleton);
        d &= mask[from].diagonal;
        a &= mask[from].antidiag;
        return hyperbola(d ^ a);
    }

    ...
public:
    Occupied (const BitBoard& myB, const BitBoard& opB) {
        value_type my = _mm_cvtsi64_si128(reinterpret_cast<const U64&>(myB));
        value_type op = _mm_cvtsi64_si128(reinterpret_cast<const U64&>(opB));
        op = _mm_shuffle_epi8(op, shuffle.flipShift);
        assert (Occupied(my & op) == empty()); //no intersection
        this->value = my ^ op;
    }

    ...
};

```

## See also


* [AltiVec](AltiVec "AltiVec")
* [AVX](AVX "AVX")
* [AVX2](AVX2 "AVX2")
* [AVX-512](AVX-512 "AVX-512")
* [MMX](MMX "MMX")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SSE2](SSE2 "SSE2")
* [SSE3](SSE3 "SSE3")
* [SSE4](SSE4 "SSE4")
* [SSE5](SSE5 "SSE5")
* [x86-64](X86-64 "X86-64")
* [XOP](XOP "XOP")


## External Links


* [SSSE3 from Wikipedia](https://en.wikipedia.org/wiki/SSSE3)
* [SSEPlus Project Documentation](http://sseplus.sourceforge.net/index.html)
* [Agner`s CPU blog](http://www.agner.org/optimize/blog/) by [Agner Fog](http://www.agner.org/)
* [SSSE3: fast popcount](http://0x80.pl/articles/sse-popcount.html) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), May 24, 2008 » [Population Count](Population_Count "Population Count")
* [Intel Intrinsics Guide](http://software.intel.com/sites/landingpage/IntrinsicsGuide/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Supplemental Streaming SIMD Extensions 3 Instructions](http://msdn.microsoft.com/en-us/library/vstudio/bb892952%28v=vs.100%29.aspx)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Intel C++ Compiler for Linux Intrinsics Reference](https://www.cs.fsu.edu/~engelen/courses/HPC-adv/intref_cls.pdf) (pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [fixing SSSE3 pmaddubsw description](http://gcc.gnu.org/ml/gcc-patches/2008-03/msg00619.html) from the mail archive of the [[[1]](mailto:gcc-patches@gcc.gnu.org%7Cgcc-patches@gcc.gnu.org)] mailing list for the [GCC project](Free_Software_Foundation#GCC "Free Software Foundation")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [SSSE3: fast popcount](http://0x80.pl/articles/sse-popcount.html) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), May 24, 2008
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), [Nathan Kurz](http://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: Plain and fancy magic on modern hardware](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=367616&t=35858) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), August 23, 2010

**[Up one Level](X86 "X86")**







 
