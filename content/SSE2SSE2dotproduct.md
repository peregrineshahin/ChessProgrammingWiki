---
title: SSE2SSE2dotproduct
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86](X86 "X86") \* SSE2**


**SSE2** (Streaming SIMD Extensions 2) and further [x86](X86 "X86")- or [x86-64](X86-64 "X86-64") streaming [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") extensions, like [SSE3](SSE3 "SSE3"), [SSSE3](SSSE3 "SSSE3"), [SSE4](SSE4 "SSE4") and AMD's announced [SSE5](SSE5 "SSE5"), as major enhancement to [SSE](SSE "SSE"), provide an instruction set on 128-bit registers, namely on [vectors](Array "Array") of four [floats](Float "Float") or two [doubles](Double "Double"), as well since SSE2 as vectors of 16 [bytes](Byte "Byte"), eight [words](Word "Word"), four [double words](Double_Word "Double Word") or two [quad words](Quad_Word "Quad Word") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. In 64-bit mode there are 16 xmm registers available, xmm0..xmm15, in 32-bit mode only eight, xmm0..xmm7. SSE is explicitly available through [C](C "C")-Compiler intrinsics <a id="cite-note-2" href="#cite-ref-2">[2]</a> or (inline) [assembly](Assembly "Assembly"). Some compiler implicitly use SSE-float and double instructions for floating point data types, others even provide automatic SSE2 vectorization, while processing [arrays](Array "Array") of various integer types. SSE- and SSE2-intrinsic functions are available in [Visual C](https://en.wikipedia.org/wiki/Visual_C%2B%2B) <a id="cite-note-3" href="#cite-ref-3">[3]</a> or [Intel-C](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Applications


Some vc2005 tested, sample SSE2 [bitboard](Bitboards "Bitboards") routines:




### One Step Only


Since 128-bit xmm registers may treated as vector of 16 bytes, shifting techniques such as  [one step](General_Setwise_Operations#OneStepOnly "General Setwise Operations") in all eight directions can be done more efficiently with respect to wraps from a- to the h-file or vice versa. It is recommend to write a own SSE2-wrapper class with overloaded operators in C++ to encapsulate a vector of two bitboards.




```C++

  northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast

```

Veritcal steps as usual with 64-byte shift a rank each:




```C++

__m128i nortOne(__m128i b) {
   b = _mm_slli_epi64 (b, 8);
   return b;
}

__m128i soutOne(__m128i b) {
   b = _mm_srli_epi64 (b, 8);
   return b;
}

```

Unfortunately there is no byte-wise shift in the SSE2-instruction set (as well as MMX), but using byte-wise parallel add avoids using the wrap masks, which need otherwise load from memory or computed. Applying the wraps mask takes two instructions.




```C++

__m128i butNotA(__m128i b) {
   b = _mm_srli_epi64 (b, 1);
   b = _mm_add_epi8   (b, b);
   return b;
}

__m128i butNotH(__m128i b) {
   b = _mm_add_epi8   (b, b);
   b = _mm_srli_epi64 (b, 1);
   return b;
}

```

This is how the east direction are computed based on parallel byte-wise add. Either one or two SSE2-instructions:




```C++

__m128i eastOne(__m128i b) {
   b = _mm_add_epi8   (b, b);
   return b;
}

__m128i noEaOne (__m128i b) {
   b = _mm_add_epi8   (b, b);
   b = _mm_slli_epi64 (b, 8);
   return b;
}

__m128i soEaOne (__m128i b) {
   b = _mm_add_epi8   (b, b);
   b = _mm_srli_epi64 (b, 8);
   return b;
}

```

West directions need a leading not A-file and take three instructions each:




```C++

__m128i westOne(__m128i b) {
   b = _mm_srli_epi64 (b, 1);
   b = _mm_add_epi8   (b, b);
   b = _mm_srli_epi64 (b, 1);
   return b;
}

__m128i soWeOne (__m128i b) {
   b = _mm_srli_epi64 (b, 1);
   b = _mm_add_epi8   (b, b);
   b = _mm_srli_epi64 (b, 9);
   return b;
}

__m128i noWeOne (__m128i b) {
   b = _mm_srli_epi64 (b, 1);
   b = _mm_add_epi8   (b, b);
   b = _mm_slli_epi64 (b, 7);
   return b;
}

```





### East Attacks


SIMD-wise [Fill by Subtraction](Fill_by_Subtraction "Fill by Subtraction") with byte- or rank-wise arithmetic takes only a few instructions with SSE2:




```C++

__m128i eastAttacks (__m128i occ, __m128i rooks) {
   __m128i tmp;
   occ  = _mm_or_si128 (occ, rooks);  //  make rooks member of occupied
   tmp  = _mm_xor_si128(occ, rooks);  // occ - rooks
   tmp  = _mm_sub_epi8 (tmp, rooks);  // occ - 2*rooks
   return _mm_xor_si128(occ, tmp);    // occ ^ (occ - 2*rooks)
}

```





### SSE2 dot product


The [dot product](https://en.wikipedia.org/wiki/Dot_product) <a id="cite-note-5" href="#cite-ref-5">[5]</a> of a vector of [bits](Bit "Bit") by a weight vector of [bytes](Byte "Byte") might be used in determining [mobility](Mobility "Mobility") for [evaluation](Evaluation "Evaluation") purposes. The vector of bits is a bitboard of all squares attacked by one (or multiple) piece(s), while the the weight vector considers the "importance" of [squares](Squares "Squares"), like center control, or even [square controls](King_Safety#SquareControl "King Safety") near the opponent [king](King "King"), e.g. by providing 64 weight vectors for each king square.




```C++
             64
bb·weights = ∑ bbi weightsi = bb1 weights1 + ... + bb64 weights64
             i=1

```

The 64-bit times 64-byte dot product implements a kind of weighted [population count](Population_Count "Population Count") similar than following loop approach, but completely unrolled and [branchless](Avoiding_Branches "Avoiding Branches"):




```C++

int dotProduct(U64 bb, BYTE weights[])
{
   U64 bit  = 1;
   int accu = 0;
   for (int sq=0; sq < 64; sq++, bit += bit) {
      if ( bb & bit) accu += weights[sq];
      // accu += weights[sq] & -((  bb & bit) == bit); // branchless 1
      // accu += weights[sq] & -(( ~bb & bit) == 0);   // branchless 2
   }
   return accu;
}

```

The SSE2 routine expands a bitboard as a vector of 64 bits into 64-bytes inside four 128-bit xmm registers, and performs the multiplication with the byte-vector by bitwise 'and', before it finally adds all bytes together. The bitboard is therefor manifolded eight times with a sequence of seven unpack and interleave instructions to remain the same expanded byte-order of the bits from the bitboards, before to mask and compare them with a vector of bytes with one appropriate bit set each.


The dot product is designed for unsigned weights in the 0..63 range, so that vertical bytewise adds of the four weights can not overflow. Nevertheless, three *PADDUSB - packed add unsigned byte with saturation* instructions ([\_mm\_adds\_epu8](http://msdn.microsoft.com/en-us/library/9hahyddy%28VS.80%29.aspx)) are used to limit the maximum four byte sum to 255 to make the routine more "robust" for cases with average weights greater than 63. The horizontal add of both [quad words](Quad_Word "Quad Word") of the 128-bit xmmregister is performed by the *PSADBW - packed sum of absolute differences of bytes into a word* instruction ([\_mm\_sad\_epu8](http://msdn.microsoft.com/en-us/library/b0yshs6s.aspx)) with zero, while the final add of the two resulting [word](Word "Word") sums in the high and low quad word of the xmm register is done with general purpose registers.




```C++

##include <emmintrin.h>
##define XMM_ALIGN __declspec(align(16))

/* for average weights < 64 */
int dotProduct64(U64 bb, BYTE weights[] /* XMM_ALIGN */)
{
   static const U64 XMM_ALIGN sbitmask[2] = {
     C64(0x8040201008040201),
     C64(0x8040201008040201)
   };
   __m128i x0, x1, x2, x3, bm;
   __m128i* pW = (__m128i*) weights;
   bm = _mm_load_si128 ( (__m128i*) sbitmask);
   x0 = _mm_cvtsi64x_si128(bb);        // 0000000000000000:8040201008040201
   // extend bits to bytes
   x0 = _mm_unpacklo_epi8  (x0, x0);   // 8080404020201010:0808040402020101
   x2 = _mm_unpackhi_epi16 (x0, x0);   // 8080808040404040:2020202010101010
   x0 = _mm_unpacklo_epi16 (x0, x0);   // 0808080804040404:0202020201010101
   x1 = _mm_unpackhi_epi32 (x0, x0);   // 0808080808080808:0404040404040404
   x0 = _mm_unpacklo_epi32 (x0, x0);   // 0202020202020202:0101010101010101
   x3 = _mm_unpackhi_epi32 (x2, x2);   // 8080808080808080:4040404040404040
   x2 = _mm_unpacklo_epi32 (x2, x2);   // 2020202020202020:1010101010101010
   x0 = _mm_and_si128      (x0, bm);
   x1 = _mm_and_si128      (x1, bm);
   x2 = _mm_and_si128      (x2, bm);
   x3 = _mm_and_si128      (x3, bm);
   x0 = _mm_cmpeq_epi8     (x0, bm);
   x1 = _mm_cmpeq_epi8     (x1, bm);
   x2 = _mm_cmpeq_epi8     (x2, bm);
   x3 = _mm_cmpeq_epi8     (x3, bm);
   // multiply by "and" with -1 or 0
   x0 = _mm_and_si128      (x0, pW[0]);
   x1 = _mm_and_si128      (x1, pW[1]);
   x2 = _mm_and_si128      (x2, pW[2]);
   x3 = _mm_and_si128      (x3, pW[3]);
   // add all bytes (with saturation)
   x0 = _mm_adds_epu8      (x0, x1);
   x0 = _mm_adds_epu8      (x0, x2);
   x0 = _mm_adds_epu8      (x0, x3);
   x0 = _mm_sad_epu8       (x0, _mm_setzero_si128 ());
   return _mm_cvtsi128_si32(x0)
        + _mm_extract_epi16(x0, 4);
}

```

### Rotated Dot Product


A little bit cheaper is to expand the bitboard to a vector of 90 degree rotated {0,255} bytes, which requires a rotated weight vector as well <a id="cite-note-6" href="#cite-ref-6">[6]</a>.




```C++

/* for average weights < 64 */
int dotProduct64(U64 bb, BYTE weightsRot90[] /* XMM_ALIGN */)
{
   static const U64 CACHE_ALIGN masks[8] = {
      C64(0x0101010101010101), C64(0x0202020202020202),
      C64(0x0404040404040404), C64(0x0808080808080808),
      C64(0x1010101010101010), C64(0x2020202020202020),
      C64(0x4040404040404040), C64(0x8080808080808080),
   };
   __m128i x0, x1, x2, x3, zr; U32 cnt;
   __m128i * pM = (__m128i*) masks;
   __m128i * pW = (__m128i*) weightsRot90;
   x0 = _mm_cvtsi64x_si128 (bb);
   x0 = _mm_unpacklo_epi64 (x0, x0);
   zr = _mm_setzero_si128  ();
   x3 = _mm_andnot_si128   (x0, pM[3]);
   x2 = _mm_andnot_si128   (x0, pM[2]);
   x1 = _mm_andnot_si128   (x0, pM[1]);
   x0 = _mm_andnot_si128   (x0, pM[0]);
   x3 = _mm_cmpeq_epi8     (x3, zr);
   x2 = _mm_cmpeq_epi8     (x2, zr);
   x1 = _mm_cmpeq_epi8     (x1, zr);
   x0 = _mm_cmpeq_epi8     (x0, zr);
   // multiply by "and" with -1 or 0
   x3 = _mm_and_si128      (x3, pW[3]);
   x2 = _mm_and_si128      (x2, pW[2]);
   x1 = _mm_and_si128      (x1, pW[1]);
   x0 = _mm_and_si128      (x0, pW[0]);
   // add all bytes (with saturation)
   x3 = _mm_adds_epu8      (x3, x2);
   x0 = _mm_adds_epu8      (x0, x1);
   x0 = _mm_adds_epu8      (x0, x3);
   x0 = _mm_sad_epu8       (x0, zr);
   return _mm_cvtsi128_si32(x0)
        + _mm_extract_epi16(x0, 4);
}

```





### SSE2 Population Count


Following proposal of a [SWAR-Popcount](Population_Count#SWARPopcount "Population Count") combined with a dot product might be quite competitive on recent [x86-64](X86-64 "X86-64") processors with a throughput of up to three simd-instructions per cycle <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> . It determines the cardinalities of eight bitboards, multiplies them with a corresponding weight, a signed 16-bit [word](Word "Word"), to finally add all together as integer. However, [Wojciech Muła's](Wojciech_Mu%C5%82a "Wojciech Muła") [SSSE3 PopCnt](SSSE3#PopCount "SSSE3") would save some more cycles, even more with doubled or fourfold register widths using [AVX2](AVX2 "AVX2") or [AVX-512](AVX-512 "AVX-512").




```C++

/**
 * popCountWeight8
 * @author Gerd Isenberg
 * @param bb vector of eight bitboards
 *        weight vector of eight short weights
 * @return sum(0,7) popcnt(bb[i]) * weight[i]
 */
int popCountWeight8(const U64 bb[8], const short weight[8]) {
   static const U64 XMM_ALIGN masks[6] = {
      C64(0x5555555555555555), C64(0x5555555555555555),
      C64(0x3333333333333333), C64(0x3333333333333333),
      C64(0x0f0f0f0f0f0f0f0f), C64(0x0f0f0f0f0f0f0f0f)
   };
   const __m128i* pM = (const __m128i*) masks;
   const __m128i* pb = (const __m128i*) bb;
   __m128i v = pb[0], w = pb[1], x = pb[2], y = pb[3];
   v = _mm_sub_epi8(v, _mm_and_si128(_mm_srli_epi64(v, 1), pM[0]));
   w = _mm_sub_epi8(w, _mm_and_si128(_mm_srli_epi64(w, 1), pM[0]));
   x = _mm_sub_epi8(x, _mm_and_si128(_mm_srli_epi64(x, 1), pM[0]));
   y = _mm_sub_epi8(y, _mm_and_si128(_mm_srli_epi64(y, 1), pM[0]));

   v = _mm_add_epi8(_mm_and_si128(v, pM[1]), _mm_and_si128(_mm_srli_epi64(v, 2), pM[1]));
   w = _mm_add_epi8(_mm_and_si128(w, pM[1]), _mm_and_si128(_mm_srli_epi64(w, 2), pM[1]));
   x = _mm_add_epi8(_mm_and_si128(x, pM[1]), _mm_and_si128(_mm_srli_epi64(x, 2), pM[1]));
   y = _mm_add_epi8(_mm_and_si128(y, pM[1]), _mm_and_si128(_mm_srli_epi64(y, 2), pM[1]));

   v = _mm_and_si128(_mm_add_epi8 (v, _mm_srli_epi64(v, 4)), pM[2]);
   w = _mm_and_si128(_mm_add_epi8 (w, _mm_srli_epi64(w, 4)), pM[2]);
   x = _mm_and_si128(_mm_add_epi8 (x, _mm_srli_epi64(x, 4)), pM[2]);
   y = _mm_and_si128(_mm_add_epi8 (y, _mm_srli_epi64(y, 4)), pM[2]);

   __m128i z = _mm_setzero_si128();
   v = _mm_packs_epi16(_mm_sad_epu8(v, z), _mm_sad_epu8(w, z));
   x = _mm_packs_epi16(_mm_sad_epu8(x, z), _mm_sad_epu8(y, z));
   const __m128i* pW = (const __m128i*) weight;
   v = _mm_madd_epi16 (_mm_packs_epi16(v, x), pW[0]);
   v = _mm_add_epi32  (v, _mm_srli_si128(v, 4));
   v = _mm_add_epi32  (v, _mm_srli_si128(v, 8));
   return _mm_cvtsi128_si32(v);
}

```





## SSE2-Wrapper in C++


[C++](Cpp "Cpp") quite efficiently allows to wrap all the intrinsics and to write classes with appropriate operators overloaded - the proposal here overloads + and - operators for byte- or rank-wise arithmetic, shifts work on 64-bit entities as often used in mentioned SSE2-routines or [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") fill-stuff. A base class for the memory layout and two derivations provide to implement routines with SSE2 or general purpose instructions - or any other available SIMD-architecture like [AltiVec](AltiVec "AltiVec"). For instance a [quad-bitboard](Quad-Bitboards "Quad-Bitboards") attack-getter:




```C++

// T is either XMM or GPR
template <class T> inline
void eastAttacks(QBB& t, const QBB& s, U64 occ) {
   T* pt = (T*)&t;
   T r0(s.bb[0]);
   T r1(s.bb[2]);
   T o0(occ, occ);
   T o1  = o0 | r1;
   o0    = o0 | r0;
   pt[0] = o0 ^ ((o0 ^ r0) - r0);
   pt[1] = o1 ^ ((o1 ^ r1) - r1);
}

```

A proposal for a class skeleton:




```C++

class DBB
{
   friend class XMM;
   friend class GPR;
public:
   DBB(){}
   ... more constructors
public:
   union
   {
      __m128i x; // this intrinsice type is wrapped here
      u64 b[2];
   };
};

// intrinsic sse2 xmm wrapper
class XMM : public DBB
{
public:
   XMM(){}
   XMM(U64 b) {x = _mm_cvtsi64x_si128(b);}
   XMM(__m128i a){x = a;}
   XMM(U64 high, U64 low) ...
   ... more constructors

   XMM& operator>>=(int sh) {x = _mm_srli_epi64(x, sh); return *this;}
   XMM& operator<<=(int sh) {x = _mm_slli_epi64(x, sh); return *this;}
   XMM& operator&=(const XMM &a) {x = _mm_and_si128(x, a.x); return *this;}
   XMM& operator|=(const XMM &a) {x = _mm_or_si128 (x, a.x); return *this;}
   XMM& operator^=(const XMM &a) {x = _mm_xor_si128(x, a.x); return *this;}

   // byte- or rankwise arithmetic
   XMM& operator+=(const XMM &a) {x = _mm_add_epi8(x, a.x); return *this;}
   XMM& operator-=(const XMM &a) {x = _mm_sub_epi8(x, a.x); return *this;}

   friend XMM operator>>(const XMM &a, int sh) {return XMM(_mm_srli_epi64(a.x, sh));}
   friend XMM operator<<(const XMM &a, int sh) {return XMM(_mm_slli_epi64(a.x, sh));}
   friend XMM operator& (const XMM &a, const XMM &b) {return XMM(_mm_and_si128(a.x, b.x));}
   friend XMM operator| (const XMM &a, const XMM &b) {return XMM(_mm_or_si128(a.x, b.x));}
   friend XMM operator^ (const XMM &a, const XMM &b) {return XMM(_mm_xor_si128(a.x, b.x));}
   friend XMM operator+ (const XMM &a, const XMM &b) {return XMM(_mm_add_epi8(a.x, b.x));}
   friend XMM operator- (const XMM &a, const XMM &b) {return XMM(_mm_sub_epi8(a.x, b.x));}
   ...
};

// pure C wrapper
class GPR : public DBB
{
   ...
};

```

## See also


* [DirGolem](DirGolem "DirGolem")
* [Pigeon](Pigeon "Pigeon")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SIMD Techniques](SIMD_Techniques "SIMD Techniques") for [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [Bitboards](Bitboards "Bitboards")
* [SSE2 Conversions](Quad-Bitboards#SSE2Conversions "Quad-Bitboards") of [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")


## SIMD


* [AltiVec](AltiVec "AltiVec")
* [AVX](AVX "AVX")
* [AVX2](AVX2 "AVX2")
* [AVX-512](AVX-512 "AVX-512")
* [MMX](MMX "MMX")
* [SSE](SSE "SSE")
* [SSE3](SSE3 "SSE3")
* [SSSE3](SSSE3 "SSSE3")
* [SSE4](SSE4 "SSE4")
* [SSE5](SSE5 "SSE5")
* [XOP](XOP "XOP")


## Manuals


* [AMD64 Architecture Programmer’s Manual Volume 4: 128-Bit and 256-Bit Media Instructions](https://support.amd.com/TechDocs/26568.pdf) (pdf)
* [Intel® 64 and IA-32 Architectures Software Developer’s Manual Volume 2A: Instruction Set Reference, A-L](https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-2a-manual.html)
* [Intel® 64 and IA-32 Architectures Software Developer’s Manual Volume 2B: Instruction Set Reference, M-U](https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-2b-manual.html)


## Forum Posts


* [A SIMD idea, eg. Piece/Gain of a capture target](https://www.stmintz.com/ccc/index.php?id=343790) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 21, 2004 » [Move Ordering](Move_Ordering "Move Ordering")
* [SSE2 bit[64] \* byte[64] dot product](https://www.stmintz.com/ccc/index.php?id=377546) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 17, 2004
* [SSE2-Sort within a register](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/11095ec26e3ed536) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), January 08, 2005
* [planning a SSE-optimized chess engine](https://www.stmintz.com/ccc/index.php?id=405396) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), January 12, 2005
* [On SSE2-Intrinsics](https://www.stmintz.com/ccc/index.php?id=418648) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), March 28, 2005
* [Problem with functions not inlining](http://www.talkchess.com/forum/viewtopic.php?t=30471) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), November 04, 2009


## External Links


* [SSE from Wikipedia](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions)
* [SSE2 from Wikipedia](https://en.wikipedia.org/wiki/SSE2)
* [SSE SSE2 and SSE3 for GNU C++](http://stackoverflow.com/questions/661338/sse-sse2-and-sse3-for-gnu-c), [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow)
* [Concurrency - SSE instructions: single memory access](http://stackoverflow.com/questions/7646018/sse-instructions-single-memory-access), [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow)
* [Agner Fog's manuals](http://www.agner.org/optimize/#manuals)


 [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
* [Agner`s CPU blog](http://www.agner.org/optimize/blog/) by [Agner Fog](http://www.agner.org/)
* [SSEPlus Project](http://developer.amd.com/cpu/Libraries/sseplus/Pages/default.aspx) from [AMD Developer Central](http://developer.amd.com/pages/default.aspx)
* [SSEPlus Project Documentation](http://sseplus.sourceforge.net/index.html)
* [Intel Intrinsics Guide](http://software.intel.com/sites/landingpage/IntrinsicsGuide/)
* [The Software Vectorization HandBook](http://www.aartbik.com/simd.php) by [Aart Bik](Aart_Bik "Aart Bik")
* [Kraan](Category:Kraan "Category:Kraan") - Vollgas Ahoi <a id="cite-note-9" href="#cite-ref-9">[9]</a>, [Rätschenmühle](https://www.swp.de/suedwesten/staedte/geislingen/raetsche-geislingen-aus-der-raetschenmuehle-live-in-die-wohnzimmer-44964276.html), [Geislingen](https://en.wikipedia.org/wiki/Geislingen_an_der_Steige), April 25, 2009, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Hellmut Hattler](Category:Hellmut_Hattler "Category:Hellmut Hattler"), [Peter Wolbrandt](https://en.wikipedia.org/wiki/Peter_Wolbrandt), [Jan Fride Wolbrandt](https://www.discogs.com/artist/345783-Jan-Fride-Wolbrandt)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [AMD64 Architecture Programmer’s Manual Volume 4: 128-Bit and 256-Bit Media Instructions](https://support.amd.com/TechDocs/26568.pdf) (pdf), has detailed explanations on all SSE2 128-Bit Media Instructions
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Integer Intrinsics Using Streaming SIMD Extensions 2](http://msdn.microsoft.com/en-us/library/84t4h8ys%28v=VS.100%29.aspx) Visual C++ Developer Center - Run-Time Library Reference
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Instruction Reference](http://msdn.microsoft.com/en-us/library/x8zs5twb%28v=VS.100%29.aspx) Visual C++ Developer Center - Run-Time Library Reference
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Intel Intrinsics Guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Dot Product - from Wolfram MathWorld](http://mathworld.wolfram.com/DotProduct.html)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [SSE2 bit[64] \* byte[64] dot product](https://www.stmintz.com/ccc/index.php?id=377546) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 17, 2004
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Intel 64 and IA32 Architectures Optimization Reference Manual](http://www.intel.com/design/processor/manuals/248966.pdf) (pdf) Appendix C Instruction Latencies
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Software Optimization Guide for AMD Family 10h and 12h Processors](https://www.amd.com/system/files/TechDocs/40546.pdf) (pdf) Appendix C Instruction Latencies
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Vollgas - Wiktionary](https://en.wiktionary.org/wiki/Vollgas), [ahoi - Wiktionary](https://en.wiktionary.org/wiki/ahoi)

**[Up one Level](X86 "X86")**







 
