---
title: General Setwise OperationsBitbySquare
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * General Setwise Operations**

\[ [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Upward, 1929 [[1]](#cite_note-1)
**General Setwise Operations**,

[binary](https://en.wikipedia.org/wiki/Binary_operation) and [unary operations](https://en.wikipedia.org/wiki/Unary_operation), essential in testing and manipulating bitboards within a chess program. [Relational operators](General_Setwise_Operations#Relational "General Setwise Operations") on bitboards test for equality, [bitwise boolean operators](General_Setwise_Operations#Bitwisebooleanoperations "General Setwise Operations") perform the intrinsic setwise operations [[2]](#cite_note-2) [[3]](#cite_note-3), such as [intersection](General_Setwise_Operations#Intersection "General Setwise Operations"), [union](General_Setwise_Operations#Union "General Setwise Operations") and [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations"). [Shifting bitboards](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations") simulates piece movement, while finally [arithmetical operations](General_Setwise_Operations#ArithmeticalOperations "General Setwise Operations") are used in [bit-twiddling](Bit-Twiddling "Bit-Twiddling") applications and to calculate various hash-indicies.

[Operators](https://en.wikipedia.org/wiki/Operator_%28mathematics%29) are denoted with focus on the [C](C "C"), [C++](Cpp "Cpp"), [Java](Java "Java") and [Pascal](Pascal "Pascal") programming languages, as well as the [mnemonics](https://en.wikipedia.org/wiki/Mnemonic#Assembly_mnemonics) of [x86](X86 "X86") or [x86-64](X86-64 "X86-64") [Assembly](Assembly "Assembly") language instructions including [bit-manipulation](Bit-Twiddling#BitManipulation "Bit-Twiddling") ([BMI1](BMI1 "BMI1"), [BMI2](BMI2 "BMI2"), [TBM](TBM "TBM")) and [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") expansions ([MMX](MMX "MMX"), [SSE2](SSE2 "SSE2"), [AVX](AVX "AVX"), [AVX2](AVX2 "AVX2"), [AVX-512](AVX-512 "AVX-512"), [XOP](XOP "XOP")), [Mathematical symbols](https://en.wikipedia.org/wiki/List_of_mathematical_symbols), some [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram) [[4]](#cite_note-4), [Truth tables](https://en.wikipedia.org/wiki/Truth_table), and bitboard diagrams where appropriate.

## Relational

[Relational operators](https://en.wikipedia.org/wiki/Relational_operator) on bitboards are the test for [equality](https://en.wikipedia.org/wiki/Relational_operator#Equality) whether they are the same or not. Greater or less in the arithmetical sense is usually not relevant with bitboards [[5]](#cite_note-5) - instead we often compare [bit](Bit "Bit") for bit of two bitboards by certain [bitwise boolean operations](General_Setwise_Operations#Bitwisebooleanoperations "General Setwise Operations") to retrieve bitwise greater, less or equal results.

## Equality

In [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java") "==" is used, to test for equality, "!=" for not equal. [Pascal](Pascal "Pascal") uses "=", "\<>" and has ":=" to distinguish relational equal operators from assignment.

```C++

if (a == b) -> both sets are equal
if (a != b) -> both sets are not equal

```

**x86-mnemonics**

[x86](X86 "X86") has a cmp-instruction, which internally performs a subtraction to set its internal processor flags (carry, zero, overflow) accordantly, for instance the zero-flag if both sets are equal. Those flags are then used by conditional jump or move instructions.

```C++

cmp  rax, rbx ; rax == rbx
je   equal    ; (jz) conditional jump if equal (jne, jnz for not equal)

```

## Empty and Universe

Two important sets are:

- The [empty set](https://en.wikipedia.org/wiki/Empty_set) is represented by all bits zero.
- The [universal set](https://en.wikipedia.org/wiki/Universal_set) contains all elements by setting all bits to binary one.

The numerical values and setwise representations of those sets:

```C++

empty set E       = 0
 set-wise         = {}

universal set U   = 2^64 - 1
 signed decimal   = -1
 hexadecimal      = 0xffffffffffffffff
 unsigned decimal = 18,446,744,073,709,551,615
 set-wise         = {a1, b1, c1, d1, ....., e8, f8, g8, h8}

```

as bitboard diagrams and [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram)

\[ Empty

```C++
                
      Empty                 Universe
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1
 . . . . . . . .        1 1 1 1 1 1 1 1

```

\[ Universe
Programmers often wonder to use -1 in [C](C "C"), [C++](Cpp "Cpp") as unsigned constant. See [The Two's Complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") - alternately one may use ~0 to define the universal set. Since in [C](C "C") or [C++](Cpp "Cpp"), decimal numbers without ULL suffix are treated as 32-bit integers, constants outside the integer range need some care concerning sign or zero extension. Const declarations or using the [C64 Macro](Bitboards#DefiningBitboards "Bitboards") is recommended:

```C++

const U64 universe = 0xffffffffffffffffULL;

```

To test whether a set is empty or not, one may compare with zero or use the logical not operator '!' in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java"):

```C++

if (a == 0) -> empty set
if (!a)     -> empty set
if (a != 0) -> set is not empty
if (a)      -> set is not empty

```

To test for the universal set is less likely:

```C++

if (a == universe) -> universal set
if (a + 1 == 0)    -> universal set

```

## Bitwise Boolean

[Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra) is an algebraic structure [[6]](#cite_note-6) [[7]](#cite_note-7) that captures essential properties of both [set operations](https://en.wikipedia.org/wiki/Set_theory#Basic_concepts) and [logical operations](https://en.wikipedia.org/wiki/Logical_connective). The properties of [associativity](https://en.wikipedia.org/wiki/Associativity), [commutativity](https://en.wikipedia.org/wiki/Commutativity), and [absorption](https://en.wikipedia.org/wiki/Absorption_laws), which define an [ordered lattice](https://en.wikipedia.org/wiki/Lattice_%28order%29), in conjunction with [distributive](https://en.wikipedia.org/wiki/Distributivity) and [complement laws](https://en.wikipedia.org/wiki/Complement_%28set_theory%29) define the [Algebra of sets](https://en.wikipedia.org/wiki/Algebra_of_sets) is in fact a [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28structure%29).

Specifically, Boolean algebra deals with the set operations of [intersection](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29), [union](https://en.wikipedia.org/wiki/Union_%28set_theory%29) and [complement](https://en.wikipedia.org/wiki/Complement_%28set_theory%29), their equivalents of [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction), [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) and [negation](https://en.wikipedia.org/wiki/Negation) and their bitwise boolean operations of [AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND), [OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and [NOT](https://en.wikipedia.org/wiki/Bitwise_operation#NOT) to implement [combinatorial logic](Combinatorial_Logic "Combinatorial Logic") in [software](Software "Software"). Bitwise boolean operations on 64-bit words are in fact 64 parallel operations on each [bit](Bit "Bit") performing one setwise operation without any "side-effects". Square mapping don't cares as long all sets use the same.

## Intersection

\[ Intersection
In [set theory](https://en.wikipedia.org/wiki/Set_theory) [intersection](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29) is denoted as:

```C++
A ∩ B

```

In [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29) [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction) is denoted as:

```C++
a ∧ b

```

Bitboard intersection or conjunction is performed by [bitwise and](https://en.wikipedia.org/wiki/Bitwise_operation#AND) (binary operator & in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java"), and the keyword "AND" in [Pascal](Pascal "Pascal")).

```C++
intersection = a & b

```

**Truth Table**

Truth table of [and](https://en.wikipedia.org/wiki/AND_gate) for one bit, for a '1' result both inputs need to be '1':

|  a
|  b
|  a and b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  0
|
|  1
|  0
|  0
|
|  1
|  1
|  1
|

Conjunction acts like a bitwise minimum, min(a, b) or as bitwise multiplication (a * b).

**x86-mnemonics**

[x86](X86 "X86") has general purpose instruction as well as [SIMD-instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") for bitwise and:

```C++

and   rax,  rbx        ; rax &= rbx
test  rax,  rbx        ; to determine whether the intersection is empty
pand  mm0,  mm1        ; MMX   mm0 &= mm1
pand  xmm0, xmm1       ; SSE2 xmm0 &= xmm1
vpand xmm0, xmm1, xmm2 ; AVX  xmm0 = xmm1 & xmm2
vpand ymm0, ymm1, ymm2 ; AVX2 ymm0 = ymm1 & ymm2

```

[SSE2](SSE2 "SSE2")-intrinsic [\_mm_and_si128](SSE2#_mm_and_si128 "SSE2")

[AVX2](AVX2 "AVX2")-intrinsic [\_mm256_and_si256](AVX2#_mm256_and_si256 "AVX2")

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

**Idempotent**

Conjunction is [idempotent](https://en.wikipedia.org/wiki/Idempotence).

```C++
a & a == a

```

**Commutative**

Conjunction is [commutative](https://en.wikipedia.org/wiki/Commutative)

```C++
a & b == b & a

```

**Associative**

Conjunction is [associative](https://en.wikipedia.org/wiki/Associative).

```C++
(a & b) & c == a & (b & c)

```

**Subset**

The intersection of two sets is [subset](https://en.wikipedia.org/wiki/Subset) of both.

Assume we have a attack set of a [queen](Queen "Queen"), and like to know whether the queen attacks opponent [pieces](Pieces "Pieces") it may [capture](Captures "Captures"), we need to 'and' the queen-attacks with the set of opponent pieces.

```C++

queen attacks    &  opponent pieces  =  attacked pieces
. . . . . . . .     1 . . 1 1 . . 1     . . . . . . . .
. . . 1 . . 1 .     1 . 1 1 1 1 1 .     . . . 1 . . 1 .
. 1 . 1 . 1 . .     . 1 . . . . . 1     . 1 . . . . . .
. . 1 1 1 . . .     . . . . . . . .     . . . . . . . .
1 1 1 * 1 1 1 .  &  . . . * . . 1 .  =  . . . * . . 1 .
. . 1 1 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . 1 . .     . . . . . . . .     . . . . . . . .
. . . 1 . . . .     . . . . . . . .     . . . . . . . .

```

To prove whether set 'a' is [subset](https://en.wikipedia.org/wiki/Subset) of another set 'b', we compare whether the intersection equals the subset:

```C++

bool isASubsetOfB(U64 a, U64 b) {return (a & b) == a;}

```

**Disjoint Sets**

To test whether two sets are [disjoint](https://en.wikipedia.org/wiki/Disjoint) - that is their intersection is empty - compiler emit the [x86](X86 "X86") test-instruction instead of and. That saves the content of a register, if the intersection is not otherwise needed:

```C++

if ( (a & b) == 0 ) -> a and b are disjoint sets

```

In chess the bitboards of white and black pieces are obviously always disjoint, same for sets of different piece-types, such as knights or pawns. Of course this is because one square is occupied by one piece only.

## Union

\[ Union
In [set theory](https://en.wikipedia.org/wiki/Set_theory) [union](https://en.wikipedia.org/wiki/Union_%28set_theory%29) is denoted as:

```C++
A ∪ B

```

In [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29) [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) is denoted as:

```C++
a ∨ b

```

The union or disjunction of two bitboards is applied by [bitwise or](https://en.wikipedia.org/wiki/Bitwise_operation#OR) (binary operator | in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java"), or the keyword "OR" in [Pascal](Pascal "Pascal")). The union is superset of the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations"), while the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") is [subset](https://en.wikipedia.org/wiki/Subset) of the union.

```C++
union = a | b

```

**Truth Table**

Truth table of [or](https://en.wikipedia.org/wiki/OR_gate) for one bit, one set input bits is sufficient to set the output:

|  a
|  b
|  a or b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  1
|
|  1
|  0
|  1
|
|  1
|  1
|  1
|

Disjunction acts like bitwise maximum, max(a, b) or as addition with saturation, min(a + b, 1). It can also be interpreted as sum minus product, a + b - a\*b, with possible temporary overflow of one binary digit to two - or with modulo 2 arithmetic.

**x86-mnemonics**

[x86](X86 "X86") has general purpose instruction as well as [SIMD-instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") for bitwise or:

```C++

or   rax,  rbx        ;       rax |= rbx
por  mm0,  mm1        ; MMX   mm0 |= mm1
por  xmm0, xmm1       ; SSE2 xmm0 |= xmm1
vpor xmm0, xmm1, xmm2 ; AVX  xmm0  = xmm1 | xmm2
vpor ymm0, ymm1, ymm2 ; AVX2 ymm0  = ymm1 | ymm2

```

[SSE2](SSE2 "SSE2")-intrinsic [\_mm_or_si128](SSE2#_mm_or_si128 "SSE2")

[AVX2](AVX2 "AVX2")-intrinsic [\_mm256_or_si256](AVX2#_mm256_or_si256 "AVX2")

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

**Idempotent**

Disjunction is [idempotent](https://en.wikipedia.org/wiki/Idempotence).

```C++
a | a == a

```

**Commutative**

Disjunction is [commutative](https://en.wikipedia.org/wiki/Commutative)

```C++
a | b == b | a

```

**Associative**

Disjunction is [associative](https://en.wikipedia.org/wiki/Associative).

```C++
(a | b) | c == a | (b | c)

```

**Distributive**

Disjunction is [distributive](https://en.wikipedia.org/wiki/Distributivity) over [conjunction](General_Setwise_Operations#Intersection "General Setwise Operations") and vice versa:

```C++
x | (y & z) == (x | y) & (x | z)
x & (y | z) == (x & y) | (x & z)

```

**Superset**

The union of two sets is superset of both. For instance the union of all white and black pieces are the set of all occupied squares:

```C++

white pieces     |  black pieces     =  occupied squares
. . . . . . . .     1 . 1 1 1 1 1 1     1 . 1 1 1 1 1 1
. . . . . . . .     1 1 1 1 . 1 1 1     1 1 1 1 . 1 1 1
. . . . . . . .     . . 1 . . . . .     . . 1 . . . . .
. . . . . . . .     . . . . 1 . . .     . . . . 1 . . .
. . . . 1 . . .  |  . . . . . . . .  =  . . . . 1 . . .
. . . . . 1 . .     . . . . . . . .     . . . . . 1 . .
1 1 1 1 . 1 1 1     . . . . . . . .     1 1 1 1 . 1 1 1
1 1 1 1 1 1 . 1     . . . . . . . .     1 1 1 1 1 1 . 1

```

Since white and black pieces are always disjoint, one may use addition here as well. That fails for union of attack sets, since squares may be attacked or defended by multiple pieces of course.

## Complement Set

\[ Complement
In [set theory](https://en.wikipedia.org/wiki/Set_theory) [complement set](https://en.wikipedia.org/wiki/Complement_%28set_theory%29) is denoted as:

```C++
A∁

```

In [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29) [negation](https://en.wikipedia.org/wiki/Negation) is denoted as:

```C++
¬a

```

The complement set (absolute complement set), negation or [ones' complement](https://en.wikipedia.org/wiki/Ones%27_complement#Ones.27_complement) has it's equivalent in [bitwise not](https://en.wikipedia.org/wiki/Bitwise_operation#NOT) (unary operator '~' in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java"), or the keyword "NOT" in [Pascal](Pascal "Pascal")).

**Truth Table**

Truth table of [not](https://en.wikipedia.org/wiki/NOT_gate) for one bit:

|  a
|  not a
|
| --- | --- |
|  0
|  1
|
|  1
|  0
|

The complement can be interpreted as bitwise subtraction (1 - a).

**x86-mnemonics**

Available as general purpose instruction.

```C++
not  rax ; rax = ~rax

```

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

**Empty Squares**

The set of empty squares for instance is the complement-set of all occupied squares and vice versa:

```C++

~occupied squares  =   empty squares
  1 . 1 1 1 1 1 1      . 1 . . . . . .
  1 1 1 1 . 1 1 1      . . . . 1 . . .
  . . 1 . . . . .      1 1 . 1 1 1 1 1
  . . . . 1 . . .      1 1 1 1 . 1 1 1
~ . . . . 1 . . .  =   1 1 1 1 . 1 1 1
  . . . . . 1 . .      1 1 1 1 1 . 1 1
  1 1 1 1 . 1 1 1      . . . . 1 . . .
  1 1 1 1 1 1 . 1      . . . . . . 1 .

```

*Don't confuse bitwise not with logical not-operator '!' in* [C](C "C"):

```C++
!0 == 1
!(anything != 0) == 0
!1  == 0
!-1 == 0

```

**Complement laws**

- The [union](General_Setwise_Operations#Union "General Setwise Operations") of a set with it's complement is the universal set -1.
- The [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of a set with it's complement is the empty set 0 - both are [disjoint](https://en.wikipedia.org/wiki/Disjoint).
- Empty set and universal set are complement sets.

```C++
a  | ~a == -1
a  & ~a ==  0
~0      == -1
~(-1)   ==  0

```

**De Morgan's laws**

- Complement of [union](General_Setwise_Operations#Union "General Setwise Operations") ([NOR](https://en.wikipedia.org/wiki/NOR_gate) ) is the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of the complements [[8]](#cite_note-8).
- Complement of [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") ([NAND](https://en.wikipedia.org/wiki/NAND_logic) or [Sheffer stroke](https://en.wikipedia.org/wiki/Sheffer_stroke) ) is the [union](General_Setwise_Operations#Union "General Setwise Operations") of the complements.

```C++
~(a | b) == ~a & ~b
~(a & b) == ~a | ~b

```

For instance to get the set of empty squares, we can complement the [union](General_Setwise_Operations#Union "General Setwise Operations") of white and black pieces. Or we can intersect the complements of white and black pieces.

## Relative Complement

\[ Relative Complement
In [set theory](https://en.wikipedia.org/wiki/Set_theory) [relative complement](https://en.wikipedia.org/wiki/Complement_%28set_theory%29#Relative_complement) is denoted as:

```C++
A∁ ∩ B = B \ A

```

The relative complement is the [absolute complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") restricted to some other set. The relative complement of 'a' inside 'b' is also known as the **set theoretic difference** of 'b' minus 'a'. It is the set of all elements that belong to 'b' but **not** to 'a'. Also called 'b' without 'a'. It is the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of 'b' with the absolute complement of 'a'.

```C++
not_a_in_b  = ~a &  b
b_without_a =  b & ~a

```

**Truth Table**

Truth table of relative complement for one bit:

|  a
|  b
|  b andnot a
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  1
|
|  1
|  0
|  0
|
|  1
|  1
|  0
|

The relative complement of 'a' in 'b' may be interpreted as a bitwise (a \< b) relation.

**x86-mnemonics**

[x86](X86 "X86") don't has an own general purpose instruction for relative complement, but [x86-64](X86-64 "X86-64") expansion [BMI1](BMI1 "BMI1"), and [SIMD-instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques"):

```C++

andn   rax,  rbx,  rcx  ; BMI1  rax = ~rbx & rcx
pandn  mm0,  mm1        ; MMX   mm0 = ~mm0 & mm1
pandn  xmm0, xmm1       ; SSE2 xmm0 = ~xmm0 & xmm1
vpandn xmm0, xmm1, xmm2 ; AVX  xmm0 = ~xmm1 & xmm2
vpandn ymm0, ymm1, ymm2 ; AVX  xmm0 = ~xmm1 & xmm2

```

[SSE2](SSE2 "SSE2")-intrinsic [\_mm_andnot_si128](SSE2#_mm_andnot_si128 "SSE2")

[AVX2](AVX2 "AVX2")-intrinsic [\_mm256_andnot_si256](AVX2#_mm256_andnot_si256 "AVX2")

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

**Super minus Sub**

In presumption of [subtraction or exclusive or](General_Setwise_Operations#XorWithout "General Setwise Operations") there are alternatives to calculate the relative complement - superset minus subset. We can take either the union without the complementing set - or the other set without the intersection

```C++
~a & b == ( a | b ) - a
~a & b == b - ( a & b )

```

## Implication

\[ Implication
Logical Implication or [Entailment](https://en.wikipedia.org/wiki/Entailment) is denoted as:

```C++
A ⇒ B

```

The boolean [Material conditional](https://en.wikipedia.org/wiki/Material_conditional) is denoted as:

```C++
a → b

```

Logical Implication or the boolean Material conditional 'a' implies 'b' (if 'a' then 'b') is an derived boolean operation, implemented as [union](General_Setwise_Operations#Union "General Setwise Operations") of the [absolute complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") of 'a' with 'b':

```C++
a_implies_b ==  ~a | b

```

**Truth Table**
Truth table of logical implication for one bit:

|  a
|  b
|  a implies b
|
| --- | --- | --- |
|  0
|  0
|  1
|
|  0
|  1
|  1
|
|  1
|  0
|  0
|
|  1
|  1
|  1
|

Implication may be interpreted as a bitwise (a \<= b) relation.

**x86-mnemonics**

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

## Exclusive Or

\[ Exclusive Or
In [set theory](https://en.wikipedia.org/wiki/Set_theory) [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) is denoted as:

```C++
A ∆ B

```

In [boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29) [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or) is denoted as:

```C++
a ⊕ b

```

Exclusive or, also exclusive disjunction (xor, binary operator '^' in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java"), or the keyword "XOR" in [Pascal](Pascal "Pascal")),

```C++
xor = a ^ b

```

also called symmetric difference, leaves all elements which are exclusively set in one of the two sets. Xor is really a multi purpose operation with a lot of applications not only bitboards of course.

```C++

1 . . . . . . 1     . . . . . . . .     1 . . . . . . 1
. 1 . . . . 1 .     . . . . . . . .     . 1 . . . . 1 .
. . 1 . . 1 . .     . . 1 1 1 1 . .     . . . 1 1 . . .
. . . 1 1 . . .     . . 1 1 1 1 . .     . . 1 . . 1 . .
. . . 1 1 . . .  ^  . . 1 1 1 1 . .  =  . . 1 . . 1 . .
. . 1 . . 1 . .     . . 1 1 1 1 . .     . . . 1 1 . . .
. 1 . . . . 1 .     . . . . . . . .     . 1 . . . . 1 .
1 . . . . . . 1     . . . . . . . .     1 . . . . . . 1

```

**Truth Table**

Truth table of [exclusive or](https://en.wikipedia.org/wiki/XOR_gate) for one bit:

|  a
|  b
|  a xor b
|
| --- | --- | --- |
|  0
|  0
|  0
|
|  0
|  1
|  1
|
|  1
|  0
|  1
|
|  1
|  1
|  0
|

Xor implements a bitwise (a != b) relation.
It acts like a bitwise addition (modulo 2), since (1 + 1) mod 2 = 0.
It also acts like a bitwise subtraction (modulo 2).

**x86-mnemonics**

[x86](X86 "X86") has general purpose instruction as well as [SIMD-instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") for bitwise exclusive or:

```C++

xor   rax,  rbx        ;       rax ^= rbx
pxor  mm0,  mm1        ; MMX   mm0 ^= mm1
pxor  xmm0, xmm1       ; SSE2 xmm0 ^= xmm1
vpxor xmm0, xmm1, xmm2 ; AVX  xmm0  = xmm1 ^ xmm2
vpxor ymm0, ymm1, ymm2 ; AVX2 ymm0  = ymm1 ^ ymm2

```

[SSE2](SSE2 "SSE2")-intrinsic [\_mm_xor_si128](SSE2#_mm_xor_si128 "SSE2")

[AVX2](AVX2 "AVX2")-intrinsic [\_mm256_xor_si256](AVX2#_mm256_xor_si256 "AVX2")

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

**Commutative**

Exclusive disjunction is [commutative](https://en.wikipedia.org/wiki/Commutative)

```C++
a ^ b == b ^ a

```

**Associative**

Xor is [associative](https://en.wikipedia.org/wiki/Associative) as well.

```C++
(a ^ b) ^ c == a ^ (b ^ c)

```

**Distributive**

[Conjunction](General_Setwise_Operations#Intersection "General Setwise Operations") is [distributive](https://en.wikipedia.org/wiki/Distributivity) over exclusive disjunction - but **not** vice versa, since conjunction acts like multiplication, while xor acts as addition in the [Galois field](https://en.wikipedia.org/wiki/Finite_field) [GF(2)](https://en.wikipedia.org/wiki/GF%282%29) :

```C++
x & (y ^ z) == (x & y) ^ (x & z)

```

**Own Inverse**

If applied two (even) times with the same operand, xor restores the original result. It is own inverse or an [involution](https://en.wikipedia.org/wiki/Involution) .

**Subset**

If one operand is subset of the other, xor (or subtraction) implements the [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations").

```C++

super               sub                 super &~ sub
. . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 1 1 1 1 1 .     . . . . . . . .     . 1 1 1 1 1 1 .
. 1 1 1 1 1 1 .     . . 1 1 1 1 . .     . 1 . . . . 1 .
. 1 1 1 1 1 1 .  ^  . . 1 1 1 1 . .     . 1 . . . . 1 .
. 1 1 1 1 1 1 .     . . 1 1 1 1 . .  =  . 1 . . . . 1 .
. 1 1 1 1 1 1 .  -  . . 1 1 1 1 . .     . 1 . . . . 1 .
. 1 1 1 1 1 1 .     . . . . . . . .     . 1 1 1 1 1 1 .
. . . . . . . .     . . . . . . . .     . . . . . . . .

```

**Subtraction**

While commutative, xor is a better replacement for subtracting from power of two minus one values, such as 63.

```C++
(2n - 1) - a == a ^ (2n - 1) with a subset of 2n - 1

```

This is because it usually safes one [x86](X86 "X86") load instruction and an additional register, but uses opcodes with immediate operands - for instance:

```C++

 1 - a == a ^  1
 3 - a == a ^  3
 7 - a == a ^  7
15 - a == a ^ 15
31 - a == a ^ 31
63 - a == a ^ 63
...
-1 - a == a ^ -1

```

**Or without And**

Xor is the same as a [union](General_Setwise_Operations#Union "General Setwise Operations") without the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") - all the bits different, 0,1 or 1,0. Since the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") is subset of the [union](General_Setwise_Operations#Union "General Setwise Operations"), xor or subtraction can replace the "without" operation & ~:

```C++
a ^ b == (a | b) &~(a & b)
a ^ b == (a | b) ^ (a & b)
a ^ b == (a | b) - (a & b)

```

**Disjoint Sets**

The symmetric difference of disjoint sets is equal to the [union](General_Setwise_Operations#Union "General Setwise Operations") or arithmetical addition. Since [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") and symmetric difference are disjoint, the union might defined that way:

```C++
a | b = ( a & b ) ^ ( a ^ b )
a | b = ( a & b ) ^   a ^ b
a | b = ( a & b ) | ( a ^ b )
a | b = ( a & b ) + ( a ^ b )

```

Assume we have distinct attack sets of pawns in left or right [direction](Direction "Direction"). The set of all squares attacked by two pawns is the intersection, the set exclusively attacked by one pawn (either right or left) is the xor-sum, while all squares attacked by any pawn is the union, see [pawn attacks](</Pawn_Attacks_(Bitboards)#PawnAttacks> "Pawn Attacks (Bitboards)").

**Union of Complements**

The symmetric difference is equivalent to the [union](General_Setwise_Operations#Union "General Setwise Operations") of both [relative complements](General_Setwise_Operations#RelativeComplement "General Setwise Operations"). Since both [relative complements](General_Setwise_Operations#RelativeComplement "General Setwise Operations") are [disjoint](https://en.wikipedia.org/wiki/Disjoint), bitwise or or add can replaced by xor itself:

```C++
a ^ b == (a & ~b) | (b & ~a)
a ^ b == (a & ~b) ^ (b & ~a)
a ^ b == (a & ~b) + (b & ~a)

```

**Toggle**

Xor can be used to toggle or flip bits by a mask.

```C++
x ^= mask;

```

**Complement**

xor with the universal set -1 flips each bit and results in the ones' complement.

```C++
a ^ -1 == ~a

```

**Without**

Due to distributive law and since symmetric difference of set and subset is the relative complement of subset in set, there are some equivalent ways to calculate the [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations") by xor. Based on surrounding expressions or whether subexpressions such as union, intersection or symmetric difference may be reused one may prefer the one or other alternative.

```C++
a & ~b == a & (-1 ^ b )
a & ~b == a & ( a ^ b )
a & ~b == a ^ ( a & b ) == a - ( a & b )
a & ~b == b ^ ( a | b ) == ( a | b ) - b

```

Also note that

```C++
a & a == a & -1

```

**Clear**

Since 'a' xor 'a' is zero, it is the shorter opcode to clear a register, since it takes no immediate operand. Applied by optimizing compilers. Same is true for subtraction by the way.

```C++

xor  rax, rax   ; same as mov rax, 0
pxor mm0, mm0   ; MMX 64-bit register
pxor xmm0, xmm0 ; SSE2 - 128-bit xmm-register

```

**Xor Swap**

Three xors on the same registers swap their content: (Note: this only works when a and b are stored on distinct memory adresses!)

```C++

a ^= b
b ^= a
a ^= b

```

If we provide an [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") by a mask, ...

```C++

a = (a ^ b) & mask
b ^= a
a ^= b

```

... 'a' becomes 'b', but only a part of 'b', where mask is one, becomes 'a'.

**Bits from two Sources**

Getting arbitrary, [disjoint](https://en.wikipedia.org/wiki/Disjoint) bits from two sources by a mask:

```C++

// if mask-bit is zero, bit from a, otherwise from b - since a^(a^b) == b
U64 mask = C64(0xFFFF0000FFFF0000);
U64 result = a ^ ((a ^ b) & mask);

```

This takes one instruction less, than the [union](General_Setwise_Operations#Union "General Setwise Operations") of [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations") of the mask in 'a' with [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of mask with 'b'.

```C++

    a ^    ((a ^ b) & mask)
== (a & ~mask) | (b & mask)
== (a & ~mask) ^ (b & mask) because both sets of the union are disjoint
== (a & ~mask) + (b & mask) because both sets of the union are disjoint

```

**XOR-applications and affairs**

- Calculation of hash-keys based on [Zobrist-keys](Zobrist_Hashing "Zobrist Hashing").
- [Cyclic redundancy check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check), [Parity words](Parallel_Prefix_Algorithms#ParityWords "Parallel Prefix Algorithms") or [Gray Code](Parallel_Prefix_Algorithms#GrayCode "Parallel Prefix Algorithms")
- [Fredkin gate](https://en.wikipedia.org/wiki/Fredkin_gate) by [Edward Fredkin](Edward_Fredkin "Edward Fredkin")
- [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence").
- [o^(o-2r)](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece").
- [Robert Hyatt's](Robert_Hyatt "Robert Hyatt") approach of a [lockless transposition table](Shared_Hash_Table#Lockless "Shared Hash Table")
- [Swapping Bits](General_Setwise_Operations#SwappingBits "General Setwise Operations").
- [The XOR affair](https://en.wikipedia.org/wiki/Perceptrons_%28book%29#The_XOR_affair) from [Perceptrons](https://en.wikipedia.org/wiki/Perceptrons_%28book%29) by [Marvin Minsky](Marvin_Minsky "Marvin Minsky") and [Seymour Papert](Mathematician#SPapert "Mathematician") [[9]](#cite_note-9)

## Equivalence

\[ Equivalence
[If and only if](https://en.wikipedia.org/wiki/If_and_only_if) (Iff) is denoted as:

```C++
A ⇔ B

```

[Logical equivalence](https://en.wikipedia.org/wiki/Logical_equivalence) is denoted as:

```C++
a ↔ b

```

[Logical equality](https://en.wikipedia.org/wiki/Logical_equality), [logical equivalence](https://en.wikipedia.org/wiki/Logical_equivalence) or [biconditional](https://en.wikipedia.org/wiki/Logical_biconditional) ([if and only if](https://en.wikipedia.org/wiki/If_and_only_if), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate) ) is the complement of xor.

```C++
a_equal_b == ~(a ^ b)
a_equal_b ==  (a & b) | (~a & ~b)
a_equal_b ==  (a & b) | ~(a | b)

```

**Truth Table**

Truth table of equivalence or for one bit:

|  a
|  b
|  a ↔ b
|
| --- | --- | --- |
|  0
|  0
|  1
|
|  0
|  1
|  0
|
|  1
|  0
|  0
|
|  1
|  1
|  1
|

Equivalence implements a bitwise (a == b) relation.

**x86-mnemonics**

[AVX-512](AVX-512 "AVX-512") has [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512")

## Majority

The [majority function](https://en.wikipedia.org/wiki/Majority_function) or **median operator** is a function from n inputs to one output. The value of the operation is false when n/2 or fewer arguments are false, and true otherwise. For two inputs it is the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations"). Three inputs require some more computation:

**Truth Table**

Truth table of majority for three inputs:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  a
|  b
|  c
|  maj(a,b,c)
|  0
|  0
|  0
|  0
|
|  0
|  0
|  1
|  0
|
|  0
|  1
|  0
|  0
|
|  0
|  1
|  1
|  1
|
|  1
|  0
|  0
|  0
|
|  1
|  0
|  1
|  1
|
|  1
|  1
|  0
|  1
|
|  1
|  1
|  1
|  1
|

```C++
major(a,b,c) = (a & b) |  (a & c) | (b & c);
major(a,b,c) = (a & b) | ((a ^ b ) & c);

```

See the application of [cardinality of multiple sets](Population_Count#CardinalityofMultipleSets "Population Count") for more than three inputs.

**x86-mnemonics**

[AVX-512](AVX-512 "AVX-512") [VPTERNLOG](AVX-512#VPTERNLOG "AVX-512") imm8 = 0xe8 implements the majority function.

## Greater One Sets

**Greater One** is a function from n inputs to one output. The value of the operation is true if more than one argument is true, false otherwise. Obviously, for two inputs it is the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations"), for three inputs it is the [majority function](General_Setwise_Operations#Majority "General Setwise Operations"). For more inputs it is the union of all distinct pairwise intersections, which can be expressed with setwise operators that way:

```C++
∪i>j∈I(Ai ∩ Aj)

```

With four bitboards this is equivalent to:

```C++

  (a1 & a0)

| (a2 & a1)
| (a2 & a0)

| (a3 & a2)
| (a3 & a1)
| (a3 & a0)

```

with

```C++
n * (n - 1) - 1

```

operations - that is 11 for n == 4.

**O(n^2) to O(n)**

Due to [distibutive law](General_Setwise_Operations#DistributiveAndOr "General Setwise Operations") one can factor out common sets ...

```C++

  (a1 & (      a0))
| (a2 & (   a1|a0))
| (a3 & (a2|a1|a0))

```

... with further reductions of the number of operations, also due to aggregation of the inner or-terms. Three additional operations for an increment of n, thus the former quadratic increase becomes linear.

In general, as mentioned,

```C++
∪i>j∈I(Ai ∩ Aj)

```

requires

```C++
n * (n - 1) - 1

```

operations, which can be reduced to

```C++
3 * (n - 1) - 2

```

operations.

This [O(n^2) to O(n)](https://en.wikipedia.org/wiki/Big_O_notation) simplification is helpful to determine for instance [knight fork target squares](Knight_Pattern#KnightForks "Knight Pattern") from eight distinct knight-wise [direction](Direction "Direction") attack sets of potential targets, like [king](King "King"), [queen](Queen "Queen"), [rooks](Rook "Rook") and hanging [bishops](Bishop "Bishop") or even [pawns](Pawn "Pawn") - or any other form of at least double attacks from n attack bitboards:

```C++

U64 attack[n]; // 0..n-1
U64 atLeastDouble = 0;
U64 atLeastSingle = a[0];
for (i=1; i < n; i++) {
  atLeastDouble |= attack[i] & atLeastSingle;
  atLeastSingle |= attack[i];
}

```

Well, if you need additionally at least triple attacks, you'll get the idea how this would work as well, see also [Odd and Major Digit Counts](Population_Count#OddMajorDigitCounts "Population Count") from the [Population Count](Population_Count "Population Count") page.

## Shifting Bitboards

In the 8\*8 board centric world with one scalar square-coordinate 0..63, each of the max eight neighboring squares can be determined by adding an offset for each [direction](Direction "Direction"). For border squares one has to care about overflows and wraps from a-file to h-file or vice versa. Some conditional code is needed to avoid that. Such code is usually part of move generation for particular pieces.

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

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
|

In the setwise world of bitboards, where a square as member of a set is determined by an appropriate one-bit 2^square, the operation to apply such movements is [shifting](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts) . Unfortunately most architectures don't support a "generalized" shift by signed values but only shift left or shift right. That makes bitboard code less general as one has usually separate code for each direction or at least for the positive and negative directions.

- Shift left (\<\<) is arithmetically a multiplication by power of two.
- Shift right (>> or >>> in [Java](Java "Java") [[10]](#cite_note-10)) is arithmetically a division by power of two.

Since the square-index is encoded as power of two exponent inside a bitboard, the power of two multiplication or division is adding or subtracting the square-index.

The reason the bitboard type-definintion is unsigned in [C](C "C"), [C++](Cpp "Cpp") is to avoid so called [arithmetical shift right](https://en.wikipedia.org/wiki/Arithmetic_shift) in opposition to [logical shift right](https://en.wikipedia.org/wiki/Logical_shift) . Arithmetical shift right implies filling one-bits in from MSB-direction if the operand is negative and has MSB bit 63 set. Logical shift right always shifts in zeros - that is what we need. [Java](Java "Java") has no unsigned types, but a special unsigned shift right operator >>>.

**x86-mnemonics**

[x86](X86 "X86") has general purpose instructions, [BMI2](BMI2 "BMI2") general purpose instructions not affecting processor flags, as well as [SIMD-instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") for various shifts:

```C++

shr      rax,  cl         ;       rax >>= cl
shl      rax,  cl         ;       rax <<= cl
shrx     r64a, r/m64, r64b; BMI2  r64a = r/m64 >> r64b
shlx     r64a, r/m64, r64b; BMI2  r64a = r/m64 << r64b 
psrlq    mm0,  mm1        ; MMX   mm0 >>= mm1
psllq    mm0,  mm1        ; MMX   mm0 <<= mm1
psrlq    xmm0, xmm1       ; SSE2 xmm0 >>= xmm1
psllq    xmm0, xmm1       ; SSE2 xmm0 <<= xmm1
vpsrlvq  ymm0, ymm1, ymm2 ; AVX2 ymm0   = ymm1 >> ymm2 ; Individual shifts
vpsllvq  ymm0, ymm1, ymm2 ; AVX2 ymm0   = ymm1 << ymm2 ; Individual shifts

```

[SSE2](SSE2 "SSE2")-intrinsics with variable register or constant immediate shift amounts, working on vectors of two bitboards:

- [\_mm_srl_epi64](SSE2#_mm_srl_epi64 "SSE2")
- [\_mm_srli_epi64](SSE2#_mm_srli_epi64 "SSE2")
- [\_mm_sll_epi64](SSE2#_mm_sll_epi64 "SSE2")
- [\_mm_slli_epi64](SSE2#_mm_slli_epi64 "SSE2")

[AVX2](AVX2 "AVX2") has [individual shifts](AVX2#IndividualShifts "AVX2") for each of four bitboards:

- [\_mm256_sllv_epi64](AVX2#_mm256_sllv_epi64 "AVX2")
- [\_mm256_srlv_epi64](AVX2#_mm256_srlv_epi64 "AVX2")

## One Step Only

The advantage with bitboards is, that the shift applies to all set bits in parallel, e.g. with all pawns. Vertical shifts by +-8 don't need any under- or overflow conditions since bits simply fall out and disappear.

```C++

U64 soutOne (U64 b) {return  b >> 8;}
U64 nortOne (U64 b) {return  b << 8;}

```

Wraps from a-file to h-file or vice versa may be considered by only shifting subsets which may not wrap.
Thus we can mask off the a- or h-file before or after a +-1,7,9 shift:

```C++

const U64 notAFile = 0xfefefefefefefefe; // ~0x0101010101010101
const U64 notHFile = 0x7f7f7f7f7f7f7f7f; // ~0x8080808080808080

```

Post-shift masks, ...

```C++

U64 eastOne (U64 b) {return (b << 1) & notAFile;}
U64 noEaOne (U64 b) {return (b << 9) & notAFile;}
U64 soEaOne (U64 b) {return (b >> 7) & notAFile;}
U64 westOne (U64 b) {return (b >> 1) & notHFile;}
U64 soWeOne (U64 b) {return (b >> 9) & notHFile;}
U64 noWeOne (U64 b) {return (b << 7) & notHFile;}

```

... and pre-shift, with the mirrored file masks.

```C++

U64 eastOne (U64 b) {return (b & notHFile) << 1;}
U64 noEaOne (U64 b) {return (b & notHFile) << 9;}
U64 soEaOne (U64 b) {return (b & notHFile) >> 7;}
U64 westOne (U64 b) {return (b & notAFile) >> 1;}
U64 soWeOne (U64 b) {return (b & notAFile) >> 9;}
U64 noWeOne (U64 b) {return (b & notAFile) << 7;}

```

[SSE2 one step only](SSE2#OneStepOnlySSE2 "SSE2") provides some optimizations according to the wraps on vectors of two bitboards.

Main application of shifts is to get attack sets or move-target sets of appropriate [pieces](Pieces "Pieces"), eg. **one step** for [pawns](Pawn "Pawn") and [king](King "King"). Applying one step **multiple** times may used to generate attack sets and moves of pieces like [knights](Knight_Pattern "Knight Pattern") and [sliding pieces](Dumb7Fill "Dumb7Fill").

For instance all push-targets of white pawns can be determined with one shift left plus [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with empty squares.

```C++

whiteSinglePawnPushTargets = nortOne(whitePawns) & emptySquares;

```

[Square-Mapping](Square_Mapping_Considerations "Square Mapping Considerations") is crucial while shifting bitboards. Shifting left inside a computer word may mean shifting right on the board with little-endian file-mapping as used in most sample code here.

## Rotate

For the sake of completeness - Rotate is similar to shift but wraps bits around. Rotate does not alter the number of set bits. With [x86-64](X86-64 "X86-64") like shift operand s modulo 64, each bit index i, in the 0 to 63 range, is transposed by

```C++

rotateLeft ::=  i := (i + s) mod 64
rotateRight::=  i := (i - s) mod 64

```

Additionally, following relations hold:

```C++

rotateLeft (s) == rotateRight(64-s)
rotateRight(s) == rotateLeft (64-s)

```

Most processors have rotate instructions, but are not supported by standard programming languages like [C](C "C") or [Java](Java "Java"). Some compilers provide intrinsic, processor specific functions.

```C++

U64 rotateLeft (U64 x, int s) {return _rotl64(x, s);}
U64 rotateRight(U64 x, int s) {return _rotr64(x, s);}

```

**x86-mnemonics**

```C++

rol  rax, cl
ror  rax, cl

```

**Rotate by Shift**

Otherwise rotate has to be emulated by shifts, with some chance optimizing compiler will emit exactly one rotate instruction.

```C++

U64 rotateLeft (U64 x, int s) {return (x << s) | (x >> (64-s));}
U64 rotateRight(U64 x, int s) {return (x >> s) | (x << (64-s));}

```

Since [x86-64](X86-64 "X86-64") 64-bit shifts are implicitly modulo 64 (and 63), one may replace (64-s) by -s.

## Generalized Shift

shifts left for positive amounts, but right for negative amounts.

```C++

U64 genShift(U64 x, int s) {
   return (s > 0) ? (x << s) : (x >> -s);
}

```

If compiler are not able to produce speculative execution of both shifts with a conditional move instruction, one may try an explicit branch-less solution:

```C++

/**
 * generalized shift
 * @author Gerd Isenberg
 * @param x any bitboard
 * @param s shift amount -64 < s < +64
 *          left if positive
 *          right if negative
 * @return shifted bitboard
 */
U64 genShift(U64 x, int s) {
   char left  =   (char) s;
   char right = -((char)(s >> 8) & left);
   return (x >> right) << (right + left);
}

```

Due to the value range of the shift, one may save the arithmetical shift right in assembly:

```C++

 ; input
 ;     ecx - shift amount,
 ;           left if positive
 ;           right if negative
 ;     rax - bitboard to shift
 mov   dl,  cl
 and   cl,  ch
 neg   cl
 shr   rax, cl
 add   cl,  dl
 shl   rax, cl

```

**One Step**

[x86-64](X86-64 "X86-64") rot64 works like a generalized shift with positive or negative shift amount - since it internally applies an unsigned modulo 64 ( & 63) and makes -i = 64-i. We need to clear either the lower or upper bits by intersection with a mask, which might be combined with the wrap-ands for [one step](General_Setwise_Operations#OneStepOnly "General Setwise Operations"). It might be applied to get attacks for both sides with a [direction](Direction "Direction") parameter and small lookups for shift amount and wrap-ands - instead of multiple code for eight directions. Of course generalized shift will be a bit slower due to lookups and using cl as the shift amount register.

```C++

// positve left, negative right shifts
int shift[8] = {9, 1,-7,-8,-9,-1, 7, 8};

U64 avoidWrap[8] =
{
   0xfefefefefefefe00,
   0xfefefefefefefefe,
   0x00fefefefefefefe,
   0x00ffffffffffffff,
   0x007f7f7f7f7f7f7f,
   0x7f7f7f7f7f7f7f7f,
   0x7f7f7f7f7f7f7f00,
   0xffffffffffffff00,
};

U64 shiftOne (U64 b, int dir8) {
   return _rotl64(b, shift[dir8]) & avoidWrap[dir8];
}

```

The avoidWrap masks by some arbitrary dir8 enumeration and shift amount:

```C++

6 == noWe -> +7     7 == nort -> +8     0 == noEa -> +9
0x7F7F7F7F7F7F7F00  0xFFFFFFFFFFFFFF00  0xFEFEFEFEFEFEFE00
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .     . . . . . . . .

5 == west -> -1                         1 == east -> +1
0x7F7F7F7F7F7F7F7F                      0xFEFEFEFEFEFEFEFE
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .                         . 1 1 1 1 1 1 1

4 == soWe -> -9     3 == sout -> -8     2 == soEa -> -7
0x007F7F7F7F7F7F7F  0x00FFFFFFFFFFFFFF  0x00FEFEFEFEFEFEFE
. . . . . . . .     . . . . . . . .     . . . . . . . .
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1

```

## See also

- [Generalized Pawn Push](</Pawn_Pushes_(Bitboards)#GeneralizedPush> "Pawn Pushes (Bitboards)")
- [Generalized Ray Attacks](Dumb7Fill#GeneralizedRays "Dumb7Fill")

## Bit by Square

Since single populated bitboards are always power of two values, shifting 2^0 left implements pow2(square) to convert square-indices to a member of a bitboard.

```C++

U64 singleBitset = C64(1) << square; // or lookup[square]

```

*The inverse function square = log2(x), is topic of [bitscan](BitScan "BitScan") and [bitboard serialization](Bitboard_Serialization "Bitboard Serialization").*

**Shift versus Lookup**

While 1 \<\< square sounds cheap, it is rather expensive in 32-bit mode - and therefor often precalculated in a small lookup-table of 64-single bit bitboards. Also, on [x86-64](X86-64 "X86-64")-processors a variable shift is restricted to the byte-register cl. Thus, two or more variable shifts are constrained by sequential execution [[11]](#cite_note-11).

**Test**

Test a bit of a square-index by [intersection](General_Setwise_Operations#Intersection "General Setwise Operations")-operator 'and'.

```C++

if (x & singleBitset) -> bit is set;

```

**Set**

Set a bit of a square-index by [union](General_Setwise_Operations#Union "General Setwise Operations")-operator 'or'.

```C++

x |=  singleBitset; // set bit

```

**Toggle**

Toggle a bit of square-index by [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations").

```C++

x ^=  singleBitset; // toggle bit

```

**Reset**

Reset a bit of square-index by [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations") of the single bit,

```C++

x &= ~singleBitset; // reset bit

```

or conditional toggle by single bit intersection

```C++

x ^=  singleBitset & x; // reset bit

```

Set and toggle (or, xor) might the faster way to reset a bit inside a register (not, and).

```C++

x |=  singleBitset; // set bit
x ^=  singleBitset; // resets set bit

```

If singleBitset needs to preserved, an extra register is needed for the complement.

**x86-Instructions**

[x86](X86 "X86") processor provides a bit-test instruction family (bt, bts, btr, btc) with 32- and 64-bit operands. They may be used implicitly by compiler optimization or explicitly by inline assembler or compiler intrinsics. Take care that they are applied on local variables likely registers rather than memory references [[12]](#cite_note-12):

- [\_bittest64](X86-64#gpinstructions "X86-64")
- [\_bittestandset64](X86-64#gpinstructions "X86-64")
- [\_bittestandcomplement64](X86-64#gpinstructions "X86-64")
- [\_bittestandreset64](X86-64#gpinstructions "X86-64")

## Update by Move

This technique to toggle [bits](Bit "Bit") by [square](Squares "Squares") is likely used to initialize or [update](Incremental_Updates "Incremental Updates") the [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition"). While [making](Make_Move "Make Move") or [unmaking moves](Unmake_Move "Unmake Move"), the single bit either correspondents with the [from](Origin_Square "Origin Square")- or [to-square](Target_Square "Target Square") of the [move](Moves "Moves"). Which particular bitboard has to be updated depends on the moving [piece](Pieces "Pieces") or captured piece.

*For simplicity we assume piece plus color and captured piece are member or method of a move-structure/class.*

[Quiet moves](Quiet_Moves "Quiet Moves") toggle both from- and to-squares of the piece-bitboard, as well for the redundant union-sets:

```C++

U64 fromBB   = C64(1) << move->from;
U64 toBB     = C64(1) << move->to;
U64 fromToBB = fromBB ^ toBB; // |+
pieceBB[move->piece]  ^=  fromToBB;   // update piece bitboard
pieceBB[move->color]  ^=  fromToBB;   // update white or black color bitboard
occupiedBB            ^=  fromToBB;   // update occupied ...
emptyBB               ^=  fromToBB;   // ... and empty bitboard

```

[Captures](Captures "Captures") need to consider the captured piece of course:

```C++

U64 fromBB   = C64(1) << move->from;
U64 toBB     = C64(1) << move->to;
U64 fromToBB = fromBB ^ toBB; // |+
pieceBB[move->piece]  ^=  fromToBB;   // update piece bitboard
pieceBB[move->color]  ^=  fromToBB;   // update white or black color bitboard
pieceBB[move->cPiece] ^=  toBB;       // reset the captured piece
pieceBB[move->cColor] ^=  toBB;       // update color bitboard by captured piece
occupiedBB            ^=  fromBB;     // update occupied, only from becomes empty
emptyBB               ^=  fromBB;     // update empty bitboard

```

Similar for special moves like [castling](Castling "Castling"), [promotions](Promotions "Promotions") and [en passant captures](En_passant "En passant").

**Upper Squares**

To get a set of all upper squares or bits, either shift ~1 or -2 left by square:

```C++

U64 upperBits =  C64(~1) << sq;

```

for instance d4 (27)

```C++

high = ~1 << d4
 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1
 . . . . 1 1 1 1
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .

```

**Lower Squares**

Lower squares are simply Bit by Square minus one.

```C++

U64 lowerBits = (C64(1 ) << sq) - 1);

```

for instance d4 (27)

```C++

low = (1<<d4)-1
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 1 1 1 . . . . .
 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1

```

## Swapping Bits

[Swapping](http://graphics.stanford.edu/%7Eseander/bithacks.html#SwappingBitsXOR) none overlapping bit-sequences in a bitboard is the base of a lot of [permutation](https://en.wikipedia.org/wiki/Permutation) tricks.

**by Position**

Suppose we like to swap n [bits](Bit "Bit") from two none overlapping bit locations of a bitboard. The trick is to set all n least significant bits by subtracting one from n power of 2. Both substrings are shifted to bit zero, exclusive ored and masked by the n ones. This sequence is then twice shifted back to their original places, while the [union](General_Setwise_Operations#Union "General Setwise Operations") (xor-union due to [disjoint](https://en.wikipedia.org/wiki/Disjoint) bits) is finally exclusive ored with the original bitboard to swap both sequences.

```C++

/**
 * swap n none overlapping bits of bit-index i with j
 * @param b any bitboard
 * @param i,j positions of bit sequences to swap
 * @param n number of consecutive bits to swap
 * @return bitboard b with swapped bit-sequences
 */
U64 swapNBits(U64 b, int i, int j, int n) {
   U64     m = ( 1 << n) - 1;
   U64     x = ((b >> i) ^ (b >> j)) & m;
   return  b ^  (x << i) ^ (x << j);
}

```

For instance swap 6 bits each, from bit-index 9 (bits named ABCDEF, either 0,1) with bit-index 41 (abcdef):

```C++

b                                       m = (1<<6) - 1
. . . . . . . .                         . . . . . . . .
* . . . . . . .                         . . . . . . . .
*|a b c d e f|*                         . . . . . . . .
. . . . . . . .                         . . . . . . . .
. . . . . . . .                         . . . . . . . .
. . . . . . . .                         . . . . . . . .
*|A B C D E F|*                         . . . . . . . .
. . . . . . . .                         1 1 1 1 1 1 . .

b >> j           ^  b >> i          =>  x = .xor & m       with
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .    r = a ^ A
. . . . . . . .     a b c d e f * *     . . . . . . . .    s = b ^ B
. . . . . . . .  ^  . . . . . . . * =>  . . . . . . . .    t = c ^ C
. . . . . . . .     . . . . . . . .     . . . . . . . .    u = d ^ D
. . . . . . . .     . . . . . . . .     . . . . . . . .    v = e ^ E
a b c d e f * *     A B C D E F * .     r s t u v w . .    w = f ^ F

b               ^  x << i | x << j  => swapNBits(9,41,6)
. . . . . . . .    . . . . . . . .     . . . . . . . .
* . . . . . . .    . . . . . . . .     * . . . . . . .
*|a b c d e f|*    . r s t u v w .     *|A B C D E F|*
. . . . . . . .    . . . . . . . .     . . . . . . . .
. . . . . . . . ^  . . . . . . . .  => . . . . . . . .
. . . . . . . .    . . . . . . . .     . . . . . . . .
*|A B C D E F|*    . r s t u v w .     *|a b c d e f|*
. . . . . . . .    . . . . . . . .     . . . . . . . .

```

**Delta Swap**

To swap any none overlapping pairs we can shift by the difference (j-i, with j>i) and supply an explicit mask with a '1' on the least significant position for each pair supposed to be swapped.

```C++

/**
 * swap any none overlapping pairs of bits
 *   that are delta places apart
 * @param b any bitboard
 * @param mask has a 1 on the least significant position
 *             for each pair supposed to be swapped
 * @param delta of pairwise swapped bits
 * @return bitboard b with bits swapped
 */
U64 deltaSwap(U64 b, U64 mask, int delta) {
   U64 x = (b ^ (b >> delta)) & mask;
   return   x ^ (x << delta)  ^ b;
}

```

To apply the swapping of the swapNBits sample above, we call deltaSwap with delta of 32 and 0x7E00 as mask. But we may apply any arbitrary and often periodic mask pattern, as long as no overlapping occurs. The [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of mask with (mask \<\< delta) must therefor be empty. But we can also swap odd or even files of a bitboard by calling deltaSwap with delta of one, and mask of 0x5555555555555555:

```C++

1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 .

```

Applications of delta swaps are [flipping, mirroring and rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating"). In [Knuth's](Donald_Knuth "Donald Knuth") *[The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming), Vol 4, page 13, bit permutation in general* [[13]](#cite_note-13), he mentions 2^k delta swaps with k = {0,1,2,3,4,5,4,3,2,1,0} to obtain any arbitrary permutation. Special cases might be cheaper.

## Arithmetic Operations

At the first glance, [arithmetic operations](https://en.wikipedia.org/wiki/Arithmetic#Arithmetic_operations), that is [addition](https://en.wikipedia.org/wiki/Addition), [subtraction](https://en.wikipedia.org/wiki/Subtraction), [multiplication](https://en.wikipedia.org/wiki/Multiplication) and [division](https://en.wikipedia.org/wiki/Division_%28mathematics%29), doesn't make much sense with bitboards. Still, there are some [bit-twiddling](Bit-Twiddling "Bit-Twiddling") applications related to least significant one bit (LS1B), to [enumerate all subsets of a set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set") or [sliding attack generation](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece"). Multiplication of certain pattern has some applications as well, most likely to calculate hash-indicies of [masked occupancies](Occupancy_of_any_Line#Multiplication "Occupancy of any Line").

## Derived from Bitwise

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Half_Adder.svg/300px-Half_Adder.svg.png)](https://en.wikipedia.org/wiki/Half_adder#Half_adder) Half Adder
Unlike bitwise boolean operations on 64-bit words, which are in fact 64 parallel operations on each bit without any interaction between them, arithmetic operations like addition need to propagate possible [carries](https://en.wikipedia.org/wiki/Carry_%28arithmetic%29) from lower to higher bits. Despite, Add and Sub are usually as fast their bitwise boolean counterparts, because they are implemented in Hardware within the [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") of the CPU. A so called [half-adder](Combinatorial_Logic#Adder "Combinatorial Logic") to add two bits (A, B), requires an [And-Gate](Combinatorial_Logic#AND "Combinatorial Logic") for the carry (C) and a [Xor-Gate](Combinatorial_Logic#XOR "Combinatorial Logic") for the sum (S):

```C++

two_bitsum = (bitA ^ bitB) | ((bitA & bitB) << 1);

```

To get an idea of the "complexity" of a simple addition, and how to implement an [carry-lookahead adder](https://en.wikipedia.org/wiki/Carry-lookahead_adder) in software with bitwise boolean and shift instructions only, and presumption on [parallel prefix algorithms](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms"), this is how a 64-bit [Kogge-Stone](Parallel_Prefix_Algorithms#FurtherElaborationsOnKoggeStone "Parallel Prefix Algorithms") adder would look like in C:

```C++

U64 koggeStoneAdd(U64 a, U64 b) {
   U64 gen = a&b;  // carries
   U64 pro = a^b;  // sum
   gen |= pro & (gen << 1);
   pro  = pro & (pro << 1);
   gen |= pro & (gen << 2);
   pro  = pro & (pro << 2);
   gen |= pro & (gen << 4);
   pro  = pro & (pro << 4);
   gen |= pro & (gen << 8);
   pro  = pro & (pro << 8);
   gen |= pro & (gen <<16);
   pro  = pro & (pro <<16);
   gen |= pro & (gen <<32);
   return a^b ^ (gen << 1);
}

```

## Addition

[Addition](https://en.wikipedia.org/wiki/Addition) might be used instead of bitwise 'xor' or 'or' for a [union](General_Setwise_Operations#Union "General Setwise Operations") of [disjoint](https://en.wikipedia.org/wiki/Disjoint) (intersection zero) sets, which may yield to simplification of the surrounding expression or may take advantage of certain address calculation instruction such as [x86](X86 "X86") load effective address (lea).

The enriched algebra with arithmetical and bitwise-boolean operations becomes aware with following relation - the bitwise overflows are the intersection, otherwise the sum modulo two is the symmetric difference - thus the arithmetical sum is the xor-sum plus the carries shifted left one:

```C++

x + y = (x ^ y) + 2*(x & y)
x ^ y =  x + y  - 2*(x & y)

```

This is particular interesting in [SWAR-arithmetic](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques"), or if we like to compute the average without possible temporary overflows:

```C++

(x + y) / 2 = ((x ^ y)>>1) + (x & y)

```

**x86-mnemonics**

```C++

add  rax, rbx ; rax += rbx
lea  rax, [rcx + rdx + const ] ; rax = rcx + rdx + const

```

## Subtraction

[Subtraction](https://en.wikipedia.org/wiki/Subtraction) (like xor) might be used to implement the [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations"), of a [subset](https://en.wikipedia.org/wiki/Subset) inside it's superset. As mentioned, subtraction may be useful in calculating [sliding attacks](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece").

**x86-mnemonics**

```C++

sub  rax, rbx ; rax -= rbx

```

## The Two's Complement

A lot of [bit-twiddling](Bit-Twiddling "Bit-Twiddling") tricks on bitboards to traverse or isolate subsets, rely on [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement) arithmetic. Most recent processors (and compiler or interpreter for these processors) use the two's complement to implement the unary minus operator for signed as well for unsigned integer types. In [C](C "C") it is guaranteed for unsigned integer types. [Java](Java "Java") guarantees two's complement for all implicit signed integral types char, short, int, long.

**x86-mnemonics**

```C++

neg  rax;  rax = -rax; rax *= -1

```

*2^N is used as power operator in this paragraph not xor* !

**Increment of Complement**

The two's complement is defined as a value, we need to add to the original value to get 264 which is an "overflowed" zero - since all 64-bit values are implicitly modulo 264. Thus, the two's complement is defined as *ones' complement plus one*:

```C++
-x == ~x + 1

```

That fulfills the condition that x + (-x) == 2bitsize (264) which overflows to zero:

```C++

x + (-x)     == 0
x +  ~x + 1  == 0
==>   x + ~x == -1 the universal set

```

**Complement of Decrement**

Replacing x by x - 1 in the increment of complement formula, leaves another definition - two's complement or Negation is also the ones' complement of the ones' decrement:

```C++
-x == ~(x - 1)

```

Thus, we can reduce subtraction by addition and ones' complement:

```C++

~(x - y) ==   ~x + y
  x - y  == ~(~x + y)

```

**Bitwise Copy/Invert**

The two's complement may also defined by a bitwise copy-loop from right (LSB) to left (MSB):

```C++

Copy bits from source to destination from right to left
- until the first binary "one" is copied.
Then invert each of the remaining higher bits.

```

**Signed-Unsigned**

This works independently whether we interpret 'x' as signed or unsigned. While 0 is is the synonym for all bits clear, -1 is the synonym for all bits set in a computer word of any arbitrary bit-size, also for 64-bit words such as bitboards.

The signed-unsigned "independence" of the two's complement is the reason that processors don't need different add or sub instructions for signed or unsigned integers. The binary pattern of the result is the same, only the interpretation differs and processors flag different overflow- or underflow conditions simultaneously.

Unsigned 64-bit values as used for bitboards have this value range:

```C++

       hexadecimal                      decimal    pow2
0x0000000000000000                            0           0
0x0000000000000001                            1           1
..
0x7fffffffffffffff    9,223,372,036,854,775,807    2^63 - 1
0x8000000000000000    9,223,372,036,854,775,808    2^63
..
0xffffffffffffffff   18,446,744,073,709,551,615    2^64 - 1


```

With signed interpretation, the positive numbers are subset of the unsigned with MSB clear:

```C++

       hexadecimal                      decimal    pow2
0x0000000000000000                            0           0
0x0000000000000001                            1           1
..
0x7fffffffffffffff    9,223,372,036,854,775,807    2^63 - 1


```

Negative numbers have MSB set to one, thus the sign bit interpretation

```C++

       hexadecimal                      decimal    pow2
0x8000000000000000   -9,223,372,036,854,775,808  -(2^63)
0x8000000000000001   -9,223,372,036,854,775,807  -(2^63) +1
..
0xfffffffffffffffe                           -2          -2
0xffffffffffffffff                           -1          -1


```

There is no "negative" zero. What makes the value range of negative values one greater than the positive numbers - and implies that

```C++

 -0x8000000000000000 == 0x8000000000000000

```

## Least Significant One

At some point bitboards require [serialization](Bitboard_Serialization "Bitboard Serialization"), thus isolation of single populated sub-sets which are power of two values if interpreted as number. Dependent on the bitboard-api those values need a further [log2(powOfTwo)](BitScan "BitScan") to convert them into the square index range from 0 to 63. Bitwise boolean operations (and, xor, or) with two's complement or ones' decrement can compute relatives of a set x in several useful ways.

### Isolation

The [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of a none empty bitboard with it's two's complement isolates the LS1B:

```C++

LS1B_of_x = x & -x;

```

With some arbitrary sample set:

```C++

      x          &        -x         =     LS1B_of_x
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. . 1 . 1 . . .     1 1 . 1 . 1 1 1     . . . . . . . .
. 1 . . . 1 . .     1 . 1 1 1 . 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. 1 . . . 1 . .  &  1 . 1 1 1 . 1 1  =  . . . . . . . .
. . 1 . 1 . . .     . . 1 1 . 1 1 1     . . 1 . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

```

Some C++ compiler warn -x still unsigned - (0-x) may used to avoid that with no overhead.

**x86-mnemonics**

[x86-64](X86-64 "X86-64") expansion [BMI1](BMI1 "BMI1") has LS1B bit isolation:

```C++

blsi  rax, rbx ; BMI1  rax = rbx & -rbx 

```

[BMI1](BMI1 "BMI1")-intrinsic [\_blsi_u32/64](BMI1#_blsi_u3264 "BMI1")

[AMD's](AMD "AMD") [x86-64](X86-64 "X86-64") expansion [TBM](TBM "TBM") further has a [Isolate Lowest Set Bit and Complement](TBM#BLSIC "TBM") instruction, which applies [De Morgan's law](General_Setwise_Operations#DeMorganslaws "General Setwise Operations") to get the complement of the LS1B:

```C++

blsic rax, rbx ; TBM:  rax = ~rbx | (rbx - 1);

```

### Reset

The [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of a none empty bitboard with it's ones' decrement resets the LS1B [[14]](#cite_note-14):

```C++

x_with_reset_LS1B = x & (x-1);

```

With some arbitrary sample set:

```C++

      x          &      (x-1)        =  x_with_reset_LS1B
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . 1 . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. 1 . . . 1 . .     . 1 . . . 1 . .     . 1 . . . 1 . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 . . . 1 . .  &  . 1 . . . 1 . .  =  . 1 . . . 1 . .
. . 1 . 1 . . .     1 1 . . 1 . . .     . . . . 1 . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .

```

... since we already know two's complement (-x) and ones' decrement (x-1) are complement sets.

**x86-mnemonics**

[x86-64](X86-64 "X86-64") expansion [BMI1](BMI1 "BMI1") has LS1B bit reset:

```C++

blsr  rax, rbx ; BMI1  rax = rbx & (rbx - 1)

```

[BMI1](BMI1 "BMI1")-intrinsic [\_blsr_u32/64](BMI1#_blsr_u3264 "BMI1")

### Separation

Masks separated by LS1B by xor with two's complement or ones' decrement. Intersection of one's complement with decrement leaves the below mask excluding LS1B:

```C++

above_LS1B_mask           =  x ^  -x;
below_LSB1_mask_including =  x ^ (x-1);
below_LSB1_mask           = ~x & (x-1);

```

With some arbitrary sample set:

```C++

      x          ^        -x         =   above_LS1B_mask
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. . 1 . 1 . . .     1 1 . 1 . 1 1 1     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     1 . 1 1 1 . 1 1     1 1 1 1 1 1 1 1
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. 1 . . . 1 . .  ^  1 . 1 1 1 . 1 1  =  1 1 1 1 1 1 1 1
. . 1 . 1 . . .     . . 1 1 . 1 1 1     . . . 1 1 1 1 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

      x          ^      (x-1)        =  below_LSB1_mask_including
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . 1 . . .     . . 1 . 1 . . .     . . . . . . . .
. 1 . . . 1 . .     . 1 . . . 1 . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 . . . 1 . .  ^  . 1 . . . 1 . .  =  . . . . . . . .
. . 1 . 1 . . .     1 1 . . 1 . . .     1 1 1 . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

     ~x          &      (x-1)        =  below_LSB1_mask
1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .
1 1 . 1 . 1 1 1     . . 1 . 1 . . .     . . . . . . . .
1 . 1 1 1 . 1 1     . 1 . . . 1 . .     . . . . . . . .
1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .
1 . 1 1 1 . 1 1  &  . 1 . . . 1 . .  =  . . . . . . . .
1 1 . 1 . 1 1 1     1 1 . . 1 . . .     1 1 . . . . . .
1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

```

**x86-mnemonics**

[x86-64](X86-64 "X86-64") expansion [BMI1](BMI1 "BMI1") has [BLSMSK](BMI1#BLSMSK "BMI1") (Mask Up to Lowest Set Bit = below_LSB1_mask_including), [AMD's](AMD "AMD") [x86-64](X86-64 "X86-64") expansion [TBM](TBM "TBM") has [TZMSK](TBM#TZMSK "TBM") (Mask From Trailing Zeros = below_LSB1_mask):

```C++

blsmsk rax, rbx ; BMI1:  rax =  rbx ^ (rbx - 1)
tzmsk  rax, rbx ; TBM:   rax = ~rbx & (rbx - 1)

```

[BMI1](BMI1 "BMI1")-intrinsic [\_blsmsk_u32/64](BMI1#_blsmsk_u3264 "BMI1")

### Smearing

To smear the LS1B up and down, we use the [union](General_Setwise_Operations#Union "General Setwise Operations") with two's complement or ones' decrement:

```C++

smearsLS1BUp   = x |  -x;
smearsLS1BDown = x | (x-1);

```

With some arbitrary sample set:

```C++

      x          |        -x         =  smearsLS1BUp
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. . 1 . 1 . . .     1 1 . 1 . 1 1 1     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     1 . 1 1 1 . 1 1     1 1 1 1 1 1 1 1
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. 1 . . . 1 . .  |  1 . 1 1 1 . 1 1  =  1 1 1 1 1 1 1 1
. . 1 . 1 . . .     . . 1 1 . 1 1 1     . . 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

      x          |      (x-1)        =  smearsLS1BDown
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . 1 . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. 1 . . . 1 . .     . 1 . . . 1 . .     . 1 . . . 1 . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 . . . 1 . .  |  . 1 . . . 1 . .  =  . 1 . . . 1 . .
. . 1 . 1 . . .     1 1 . . 1 . . .     1 1 1 . 1 . . .
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

```

**x86-mnemonics**

[AMD's](AMD "AMD") [x86-64](X86-64 "X86-64") expansion [TBM](TBM "TBM") has a [Fill From Lowest Set Bit](TBM#BLSFILL "TBM") instruction:

```C++

blsfill  rax, rbx ; TBM:  rax = rbx | (rbx - 1)

```

## Least Significant Zero

Dealing with the least significant zero bit (LS0B) or clear bit can be derived from the complement of the LS1B. [AMD's](AMD "AMD") [x86-64](X86-64 "X86-64") expansion [TBM](TBM "TBM") has six instructions based on boolean operations with the one's increment:

- [Isolate Lowest Clear Bit](TBM#BLCI "TBM"), [union](General_Setwise_Operations#Union "General Setwise Operations") with the [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") of the increment
- [Isolate Lowest Clear Bit and Complement](TBM#BLCIC "TBM"), [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of the [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") with the increment
- [Fill From Lowest Clear Bit](TBM#BLCFILL "TBM"), [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with the increment
- [Mask From Lowest Clear Bit](TBM#BLCMSK "TBM"), [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with the increment
- [Set Lowest Clear Bit](TBM#BLCS "TBM"), [union](General_Setwise_Operations#Union "General Setwise Operations") with the increment
- [Inverse Mask From Trailing Ones](TBM#T1MSKC "TBM"), [union](General_Setwise_Operations#Union "General Setwise Operations") of [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") and increment

## Most Significant One

The MS1B is not that simple to isolate as long we have no reverse arithmetic with carries propagating from left to right. To isolate MS1B, one needs to set all lower bits below MS1B, shift the resulting mask right by one and finally add one.

Setting all lower bits in the general case requires 63 times x |= x >> 1 which might be done in [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") manner in log2(64) = 6 steps:

```C++

x |= x >> 32;
x |= x >> 16;
x |= x >>  8;
x |= x >>  4;
x |= x >>  2;
x |= x >>  1;
MS1B = (x >> 1) + 1;

```

Still quite expensive - better to traverse sets the other way around or rely on intrinsic functions to use special processor instructions like [BitScanReverse](BitScan#Bitscanreverse "BitScan") or LeadingZeroCount, which implicitly performs not only the isolation but also the [log2](https://en.wikipedia.org/wiki/Binary_logarithm).

**Common MS1B**

Two sets have a common MS1B, if the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") is greater than the xor sum:

```C++

if ((a & b) > (a ^ b)) -> a and b have common MS1B

```

This is because a common MS1B is set in the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") but cleared in the xor sum. Otherwise, with no common MS1B, the xor-sum is greater except equal for two zero operands.

## Multiplication

64-bit [Multiplication](https://en.wikipedia.org/wiki/Multiplication) has become awfully fast on recent processors. Shift left is of course still faster than multiplication by power of two, but if we have more than one bit set in a factor, it already makes sense to replace for instance

```C++

y  = (x << 8) + (x << 16);

```

by

```C++

y  = x * 0x00010100;

```

**Fill-Multiplication**

In fact, we can replace [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") left shifts like,

```C++

x |= x << 32;
x |= x << 16;
x |= x <<  8;

```

where x has max one bit per file, and we can therefor safely replace 'or' by 'add'

```C++

x += x << 32;
x += x << 16;
x += x <<  8;

```

by multiplication with 0x0101010101010101 (which is the A-File in little endian mapping):

```C++

. . . . . . . .     1 . . . . . . .     . 1 1 . 1 1 . .
. . . . . . . .     1 . . . . . . .     . 1 1 . 1 1 . .
. . . . . . . .     1 . . . . . . .     . 1 1 . 1 1 . .
. . . . . . . .     1 . . . . . . .     . 1 1 . 1 1 . .
. 1 . . . 1 . .  *  1 . . . . . . .  =  . 1 1 . 1 1 . .
. . 1 . 1 . . .     1 . . . . . . .     . . 1 . 1 . . .
. . . . . . . .     1 . . . . . . .     . . . . . . . .
. . . . . . . .     1 . . . . . . .     . . . . . . . .

```

See [Kindergarten-Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")- or [Magic-Bitboards](Magic_Bitboards "Magic Bitboards") as applications of fill-multiplication.

**De Bruijn Multiplication**

Another bitboard related application of multiplication is to determine the bit-index of the least significant one bit. A isolated, single bit is multiplied with a [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence") to implement a [bitscan](BitScan#DeBruijnMultiplation "BitScan").

## Division

64-bit [Division](https://en.wikipedia.org/wiki/Division_%28mathematics%29) is still a slow instruction which takes a lot of cycles - it should be avoided at runtime. Division by a power of two is done by right shift.

An interesting application to calculate various masks for [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"), e.g. swapping [bits](Bit "Bit"), bit-duos, [nibbles](Nibble "Nibble"), [bytes](Byte "Byte"), [words](Word "Word") and [double words](Double_Word "Double Word"), is the 2-[adic](https://en.wikipedia.org/wiki/P-adic_number) division of the universal set (-1) by 2^(2^i) plus one, which may be done at compile time:

```C++

-1 / ( 2^(2^0) + 1) == -1 / (         2 + 1) == 0x5555555555555555
-1 / ( 2^(2^1) + 1) == -1 / (         4 + 1) == 0x3333333333333333
-1 / ( 2^(2^2) + 1) == -1 / (        16 + 1) == 0x0f0f0f0f0f0f0f0f
-1 / ( 2^(2^3) + 1) == -1 / (       256 + 1) == 0x00ff00ff00ff00ff
-1 / ( 2^(2^4) + 1) == -1 / (     65536 + 1) == 0x0000ffff0000ffff
-1 / ( 2^(2^5) + 1) == -1 / (4294967296 + 1) == 0x00000000ffffffff

```

See [generalized flipping, mirroring and reversion](Flipping_Mirroring_and_Rotating#Generalized "Flipping Mirroring and Rotating"). Often used masks and factors are the 2-adic division of the universal set (-1) by 2^(2^i) minus one, which results in the lowest bit of [SWAR-wise](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") bits set, bit-duos, nibbles, bytes, words and double words:

```C++

-1 / ( 2^(2^0) - 1) == -1 / (         2 - 1) == 0xffffffffffffffff
-1 / ( 2^(2^1) - 1) == -1 / (         4 - 1) == 0x5555555555555555
-1 / ( 2^(2^2) - 1) == -1 / (        16 - 1) == 0x1111111111111111
-1 / ( 2^(2^3) - 1) == -1 / (       256 - 1) == 0x0101010101010101
-1 / ( 2^(2^4) - 1) == -1 / (     65536 - 1) == 0x0001000100010001
-1 / ( 2^(2^5) - 1) == -1 / (4294967296 - 1) == 0x0000000100000001

```

## Modulo

[Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic) with 64-bit [modulo](https://en.wikipedia.org/wiki/Modulo_operation) by a constant, has applications in [Cryptography](https://en.wikipedia.org/wiki/Cryptography) [[15]](#cite_note-15), [Hashing](Hash_Table "Hash Table"), and with Bitboards in [Bit Scanning](BitScan#BitscanByModulo "BitScan"), [Population Count](Population_Count#Castingout "Population Count") and [Congruent Modulo Bitboards](Congruent_Modulo_Bitboards "Congruent Modulo Bitboards") for [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks").

### Casting out 255

Similar to [Casting out nines](https://en.wikipedia.org/wiki/Casting_out_nines) with decimals and due to the [congruence relation](https://en.wikipedia.org/wiki/Congruence_relation)

```C++
Basen ≡ 1 (mod Base-1)

```

casting out 255 can be used to add all the eight bytes within a [SWAR-wise](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") 64-bit [quad word](Quad_Word "Quad Word") if the sum is less than 255, as mentioned, applicable in [Population Count](Population_Count#Castingout "Population Count") and [Congruent Modulo Bitboards - Casting out 255](Congruent_Modulo_Bitboards#Castingout255 "Congruent Modulo Bitboards").

### Reciprocal Multiplication

Likely 64-bit compiler will optimize modulo (and division) by reciprocal, 2^64 div constant, to perform a 64\*64 = 128bit fixed point multiplication to get the quotient in the upper 64-bit, and a second multiplication and subtraction to finally get the remainder. Here some sample [x86-64](X86-64 "X86-64") assembly:

```C++

r11d := r10 % 257
 mov    r11d, r10 ; masked diagonal
 mov    rax, ff00ff00ff00ff01H ; 2^(64+8) / 257
 mul    r10
 shr    rdx, 8
 imul   edx, 257 ; 00000101H
 sub    r11d, edx

```

### Power of Two

As a remainder, and to close the cycle to [bitwise boolean operations](General_Setwise_Operations#Bitwisebooleanoperations "General Setwise Operations"), the well known trick is mentioned, to replace modulo by power of two by [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with power of two minus one:

```C++
a % 2n == a & (2n - 1)

```

## Selected Publications

## 1847 ...

- [George Boole](Mathematician#Boole "Mathematician") (**1847**). *[The Mathematical Analysis of Logic, Being an Essay towards a Calculus of Deductive Reasoning](https://archive.org/stream/mathematicalanal00booluoft/mathematicalanal00booluoft_djvu.txt)*. Macmillan, Barclay & Macmillan
- [George Boole](Mathematician#Boole "Mathematician") (**1848**). *[The Calculus of Logic](http://www.maths.tcd.ie/pub/HistMath/People/Boole/CalcLogic/)*. [Cambridge and Dublin Mathematical Journal](https://en.wikipedia.org/wiki/The_Quarterly_Journal_of_Pure_and_Applied_Mathematics), Vol. III
- [Augustus De Morgan](Mathematician#ADeMorgan "Mathematician") (**1860**). *[Syllabus of a Proposed System of Logic](http://books.google.com/books?id=Od3jgF5rZtgC)*. Walton & Malbery
- [Charles S. Peirce](Mathematician#CSPeirce "Mathematician") (**1867**). *On an Improvement in Boole's Calculus of Logic*. Proceedings of the American Academy of Arts and Sciences, Series Vol. 7
- [Georg Cantor](Mathematician#Cantor "Mathematician") (**1874**). *[Ueber eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen](<https://glossar.hs-augsburg.de/Cantor,_G._(1874):_Ueber_eine_Eigenschaft_des_Inbegriffs_aller_reellen_algebraischen_Zahlen>)*. [Journal für die reine und angewandte Mathematik](https://en.wikipedia.org/wiki/Crelle%27s_Journal), No. 77
- [Charles S. Peirce](Mathematician#CSPeirce "Mathematician") (**1880**). *[On the Algebra of Logic](https://archive.org/details/jstor-2369442)*. [American Journal of Mathematics](https://en.wikipedia.org/wiki/American_Journal_of_Mathematics), Vol. 3
- [John Venn](Mathematician#Venn "Mathematician") (**1880**). *[On the Diagrammatic and Mechanical Representation of Propositions and Reasonings](http://www.tandfonline.com/doi/abs/10.1080/14786448008626877#.U3kRnHYfwgI)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Vol. 9, No. 5
- [John Venn](Mathematician#Venn "Mathematician") (**1881**). *[Symbolic Logic](https://archive.org/details/symboliclogic00venniala)*. MacMillan & Co.

## 1900 ...

- [Claude Shannon](Claude_Shannon "Claude Shannon") (**1938**). *[A Symbolic Analysis of Relay and Switching Circuits](https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits)*. [Transactions of the AIEE](https://en.wikipedia.org/wiki/American_Institute_of_Electrical_Engineers), Vol. 57, No 12, Master's thesis 1940, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [Victor I. Shestakov](Mathematician#VIShestakov "Mathematician") (**1941**). *Algebra of Two Poles Schemata*. [Automatics and Telemechanics](https://en.wikipedia.org/wiki/Automation_and_Remote_Control), Vol. 5, No 2

## 1950 ...

- [Lazar A. Lyusternik](Mathematician#LLyusternik "Mathematician"), [Aleksandr Abramov](Mathematician#AAbramov "Mathematician"), [Victor I. Shestakov](Mathematician#VIShestakov "Mathematician"), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1952**). *Programming for High-Speed Electronic Computers*. (Программирование для электронных счетных машин)
- [Christopher Strachey](Christopher_Strachey "Christopher Strachey") (**1961**). *Bitwise operations*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 4, No. 3

## 2000 ...

- [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2002, 2012**). *[Hacker's Delight](Henry_S._Warren,_Jr.#HackersDelight "Henry S. Warren, Jr.")*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley)
- [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz)
- [Ronald L. Rivest](Ronald_L._Rivest "Ronald L. Rivest") (**2011**). *The invertibility of the XOR of rotations of a binary word*. [International Journal of Computer Mathematics, Vol. 88](https://dblp1.uni-trier.de/db/journals/ijcm/ijcm88.html), [2009 pdf preprint](https://pdfs.semanticscholar.org/8177/7b0bb30aa7ca12f9a1aea57691a6fb1e1249.pdf)

## Forum Posts

## 2000 ...

- [curiosity killed the cat... hi/lo bit C verses Assembly](https://www.stmintz.com/ccc/index.php?id=306882) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 17, 2003
- [mask of highest bit](https://www.stmintz.com/ccc/index.php?id=450730) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), September 21, 2005

## 2010 ...

- [How to Shift Left (by) a Negative Number??](http://www.talkchess.com/forum/viewtopic.php?t=47710) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), April 05, 2013
- [To shift or not to shift](http://www.open-chess.org/viewtopic.php?f=5&t=2878) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 09, 2015 » [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff")
- [Question about resetting a bit in a bitboard corresponding to a given square](https://groups.google.com/d/msg/fishcooking/r_7TSUtNXls/PUM5JgcSFQAJ) by guenther, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 09, 2016 » [Reset Bit](#ResetBit)
- [On the speed of SquareBB array](https://groups.google.com/forum/#!topic/fishcooking/TplkvO62I9U) by protonspring, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 22, 2019

## 2020 ...

- [C++20 standard bit operations](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75818) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 15, 2020 » [Population Count](Population_Count "Population Count"), [BitScan](BitScan "BitScan"), [C++](Cpp "Cpp")

## External Links

## Sets

- [Set (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Set_%28mathematics%29)
- [Portal:Set theory from Wikipedia](https://en.wikipedia.org/wiki/Portal:Set_theory)
- [Finite set from Wikipedia](https://en.wikipedia.org/wiki/Finite_set)
- [Fuzzy set from Wikipedia](https://en.wikipedia.org/wiki/Fuzzy_set)
- [Set theory from Wikipedia](https://en.wikipedia.org/wiki/Set_theory)

[Naive set theory from Wikipedia](https://en.wikipedia.org/wiki/Naive_set_theory)
[Zermelo–Fraenkel set theory from Wikipedia](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) » [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo"), [Abraham Fraenkel](Mathematician#AbrahamFraenkel "Mathematician")

- [Set Theory (Stanford Encyclopedia of Philosophy)](http://plato.stanford.edu/entries/set-theory/)
- [Venn diagram from Wikipedia](https://en.wikipedia.org/wiki/Venn_diagram)

## Algebra

- [Algebra from Wikipedia](https://en.wikipedia.org/wiki/Algebra)
- [Elementary algebra from Wikipedia](https://en.wikipedia.org/wiki/Elementary_algebra)
- [Abstract algebra from Wikipedia](https://en.wikipedia.org/wiki/Abstract_algebra)
- [Algebraic structure from Wikipedia](https://en.wikipedia.org/wiki/Algebraic_structure) ([Model theory](https://en.wikipedia.org/wiki/Model_theory))
- [Algebra of sets from Wikipedia](https://en.wikipedia.org/wiki/Algebra_of_sets)
- [Boolean algebra from Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra)
- [Boolean algebra (logic) from Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra_%28logic%29)
- [Boolean algebra (structure) from Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra_%28structure%29)
- [Boolean algebras canonically defined from Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebras_canonically_defined)
- [Boolean ring from Wikipedia](https://en.wikipedia.org/wiki/Boolean_ring)
- [Finite field from Wikipedia](https://en.wikipedia.org/wiki/Finite_field)
- [GF(2) from Wikipedia](https://en.wikipedia.org/wiki/GF%282%29)
- [The Mathematics of Boolean Algebra (Stanford Encyclopedia of Philosophy)](http://plato.stanford.edu/entries/boolalg-math/)

## Logic

- [Logic from Wikipedia](https://en.wikipedia.org/wiki/Logic)
- [Portal:Logic from Wikipedia](https://en.wikipedia.org/wiki/Portal:Logic)
- [Mathematical logic from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_logic)
- [Algebraic logic from Wikipedia](https://en.wikipedia.org/wiki/Algebraic_logic)
- [Propositional calculus from Wikipedia](https://en.wikipedia.org/wiki/Propositional_calculus)
- [Predicate logic from Wikipedia](https://en.wikipedia.org/wiki/Predicate_logic)
- [Entailment from Wikipedia](https://en.wikipedia.org/wiki/Entailment)
- [Syllogism from Wikipedia](https://en.wikipedia.org/wiki/Syllogism)
- [Logical connective from Wikipedia](https://en.wikipedia.org/wiki/Logical_connective)

## Operations

### Setwise

- [Set (mathematics) - Basic operations from Wikipedia](https://en.wikipedia.org/wiki/Set_%28mathematics%29#Basic_operations)

[Intersection (set theory) from Wikipedia](https://en.wikipedia.org/wiki/Intersection_%28set_theory%29)
[Union (set theory) from Wikipedia](https://en.wikipedia.org/wiki/Union_%28set_theory%29)
[Complement (set theory) from Wikipedia](https://en.wikipedia.org/wiki/Complement_%28set_theory%29)

### Bitwise

- [Bitwise operation from Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

[Logical conjunction from Wikipedia](https://en.wikipedia.org/wiki/Logical_conjunction)
[Logical disjunction from Wikipedia](https://en.wikipedia.org/wiki/Logical_disjunction)
[Exclusive or from Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or)
[Negation from Wikipedia](https://en.wikipedia.org/wiki/Negation)
[Bit Shifts from Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts)
[Circular shift from Wikipedia](https://en.wikipedia.org/wiki/Circular_shift)

### Arithmetic

- [Arithmetic operations from Wikipedia](https://en.wikipedia.org/wiki/Arithmetic#Arithmetic_operations)

[Addition from Wikipedia](https://en.wikipedia.org/wiki/Addition)
[Subtraction from Wikipedia](https://en.wikipedia.org/wiki/Subtraction)
[Two's complement from Wikipedia](https://en.wikipedia.org/wiki/Two%27s_complement)
[Multiplication from Wikipedia](https://en.wikipedia.org/wiki/Multiplication)
[Division from Wikipedia](https://en.wikipedia.org/wiki/Division_%28mathematics%29)
[Modulo operation from Wikipedia](https://en.wikipedia.org/wiki/Modulo_operation)

### Modular arithmetic

- [Congruence relation from Wikipedia](https://en.wikipedia.org/wiki/Congruence_relation)
- [Modular arithmetic from Wikipedia](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Linear congruence theorem from Wikipedia](https://en.wikipedia.org/wiki/Linear_congruence_theorem)

## Misc

- [Casiopea](Category:Casiopea "Category:Casiopea") - Conjunction, [Perfect Live](https://en.wikipedia.org/wiki/Casiopea_Perfect_Live_II) (1986), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [Hux Flux](Category:Hux_Flux "Category:Hux Flux") - Bitshifter, [Division by Zero](https://en.wikipedia.org/wiki/Division_by_Zero_%28album%29), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. [↑](#cite_ref-1) [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Upward, 1929, [Peggy Guggenheim Collection](https://en.wikipedia.org/wiki/Peggy_Guggenheim_Collection), [Wikimedia COmmons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. [↑](#cite_ref-2) [Andrey Ershov](Mathematician#Ershov "Mathematician"), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1980**). *[The Early Development of Programming in the USSR](http://ershov.iis.nsk.su/archive/eaindex.asp?lang=2&gid=910)*. in [Nicholas C. Metropolis](https://en.wikipedia.org/wiki/Nicholas_C._Metropolis) (ed.) *[A History of Computing in the Twentieth Century](http://dl.acm.org/citation.cfm?id=578384)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), [preprint pp. 43](http://ershov.iis.nsk.su/archive/eaimage.asp?did=28792&fileid=173670)
1. [↑](#cite_ref-3) [Lazar A. Lyusternik](https://en.wikipedia.org/wiki/Lazar_Lyusternik), [Aleksandr A. Abramov](http://www.mathnet.ru/php/person.phtml?personid=30351&option_lang=eng), [Victor I. Shestakov](https://en.wikipedia.org/wiki/Victor_Shestakov), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1952**). *Programming for High-Speed Electronic Computers*. (Программирование для электронных счетных машин)
1. [↑](#cite_ref-4) [John Venn](Mathematician#Venn "Mathematician") (**1880**). *[On the Diagrammatic and Mechanical Representation of Propositions and Reasonings](http://www.tandfonline.com/doi/abs/10.1080/14786448008626877#.U3kRnHYfwgI)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Vol. 9, No. 59
1. [↑](#cite_ref-5) Greater or less in the arithmetical sense is usually not relevant with bitboards, but see greater condition in [Thor's Hammer's move generation](Thor%27s_Hammer#MoveGeneration "Thor's Hammer")
1. [↑](#cite_ref-6) [George Boole](Mathematician#Boole "Mathematician") (**1847**). *[The Mathematical Analysis of Logic, Being an Essay towards a Calculus of Deductive Reasoning](https://archive.org/stream/mathematicalanal00booluoft/mathematicalanal00booluoft_djvu.txt)*. Macmillan, Barclay & Macmillan
1. [↑](#cite_ref-7) [Charles S. Peirce](Mathematician#CSPeirce "Mathematician") (**1880**). *[On the Algebra of Logic](https://archive.org/details/jstor-2369442)*. [American Journal of Mathematics](https://en.wikipedia.org/wiki/American_Journal_of_Mathematics), Vol. 3
1. [↑](#cite_ref-8) [Augustus De Morgan](Mathematician#ADeMorgan "Mathematician") (**1860**). *[Syllabus of a Proposed System of Logic](http://books.google.com/books?id=Od3jgF5rZtgC)*. Walton & Malbery
1. [↑](#cite_ref-9) [Marvin Minsky](Marvin_Minsky "Marvin Minsky"), [Seymour Papert](Mathematician#SPapert "Mathematician") (1969, **1972**). *[Perceptrons: An Introduction to Computational Geometry](https://en.wikipedia.org/wiki/Perceptrons_%28book%29)*. [The MIT Press](https://en.wikipedia.org/wiki/MIT_Press), ISBN 0-262-63022-2
1. [↑](#cite_ref-10) [Re: Java chess program?](https://groups.google.com/d/msg/rec.games.chess.computer/o3AMPvhmY3o/1yZhMk3_VlIJ) by [Moritz Berger](Moritz_Berger "Moritz Berger"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 29, 1997 » [Shifting Bitboards](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), [Java](Java "Java")
1. [↑](#cite_ref-11) [To shift or not to shift](http://www.open-chess.org/viewtopic.php?f=5&t=2878) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 09, 2015
1. [↑](#cite_ref-12) [On the speed of SquareBB array](https://groups.google.com/forum/#!topic/fishcooking/TplkvO62I9U) by protonspring, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 22, 2019
1. [↑](#cite_ref-13) [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz)
1. [↑](#cite_ref-14)  [Peter Wegner](Mathematician#PWegner "Mathematician") (**1960**). *A technique for counting ones in a binary computer*. [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM), [Volume 3, 1960](http://www.informatik.uni-trier.de/~ley/db/journals/cacm/cacm3.html#Wegner60)
1. [↑](#cite_ref-15) [Modular exponentiation from Wikipedia](https://en.wikipedia.org/wiki/Modular_exponentiation)

**[Up one Level](Bitboards "Bitboards")**

