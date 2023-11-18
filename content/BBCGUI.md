---
title: BBCGUI
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BBC**

**BBC**, (Bit Board Chess)

a didactic bitboard chess engine by [Maksim Korzh](Maksim_Korzh "Maksim Korzh") alias Code Monkey King, written in [C](C "C"). BBC is subject of a [YouTube](https://en.wikipedia.org/wiki/YouTube) [video tutorial](https://en.wikipedia.org/wiki/Tutorial) started in summer 2020 <a id="cite-note-1" href="#cite-ref-1">[1]</a>, actually work in progress.
The [open source engine](Category:Open_Source "Category:Open Source") is further published on [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and will be compliant to the [UCI](UCI "UCI") protocol.
While the series offers a nice introduction in chess engine programming and [bitboard](Bitboards "Bitboards") techniques,
the advanced approach of [Magic Bitboards](Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with all its lengthy initialization topics might be hard to understand and deterrent for the intended novice target group.
The linewise approaches of [First Rank Attacks](First_Rank_Attacks "First Rank Attacks") to introduce occupancy lookups, followed by [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") - as intermediate step towards magics bitboards - seem didactically more appropriate. Anyway, a valuable video series covering various aspects of computer chess programming. **BBC 1.0** was released on September 24, 2020 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, **BBC 1.3** on October 21, 2020, utilizing [Stockfish's NNUE](Stockfish_NNUE "Stockfish NNUE") evaluation via [Daniel Shawul's](Daniel_Shawul "Daniel Shawul") [Scorpio NNUE](Scorpio#ScorpioNNUE "Scorpio") [egbbdll](Scorpio#Bitbases "Scorpio") probing library <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## See also

- [BMCP](BMCP "BMCP")
- [PeSTO](PeSTO "PeSTO")
- [Vice](Vice "Vice")

## Forum Posts

- [Comparing 4 move generators: 0x88 vs 10x12 vs 10x12 + bitboards HYBRID vs Pure MAGIC BITBOARDS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74917) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), August 28, 2020
- [Bitboard CHESS ENGINE in C: YouTube series by Code Monkey King](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75017) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 06, 2020
- [Zobrist hashing tutorials on YouTube](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75155) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 19, 2020
- [BBC 1.0 release - UCI chess engine by CMK](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75199) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 24, 2020
- [How to rate my engine in CCRL?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75204) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 25, 2020 » [CCRL](CCRL "CCRL")
- [BBC GUI release - PLAY IT ONLINE!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75380) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 12, 2020 » [Web GUI Tutorial](#gui)
- [How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), [Scorpio NNUE](Scorpio#NNUE "Scorpio")

[Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 17, 2020

- [Embedding Stockfish NNUE to ANY CHESS ENGINE: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75418) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020 » [NNUE](NNUE "NNUE")
- [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 21, 2020
- [BBC 1.4 + Stockfish NNUE + Online GUI + Opening book - FINAL RELEASE!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75541) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 25, 2020
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")

## External Links

## GitHub

- [GitHub - maksimKorzh/bbc: Bit Board Chess (BBC) - The easiest to understand bitboard chess engine by Code Monkey King](https://github.com/maksimKorzh/bbc)
- [GitHub - maksimKorzh/uci-gui: Web based GUI for UCI chess engine](https://github.com/maksimKorzh/uci-gui)

## YouTube

### BBC

**Bitboard CHESS ENGINE in C**

1. [Intro](https://youtu.be/QUNP-UjujBM) » [Bitboards](Bitboards "Bitboards")
1. [Creating comfortable conditions for development](https://youtu.be/o-ySJ2EBarY)
1. [Generating pre-calculated PAWN ATTACK tables](https://youtu.be/OTWG4dERdSc) » [Pawn Attacks (Bitboards)](</Pawn_Attacks_(Bitboards)> "Pawn Attacks (Bitboards)")
1. [Generating pre-calculated KNIGHT ATTACK table](https://youtu.be/nZLuLn9JW0E) » [Knight Attacks](Knight_Pattern#KnightAttacks "Knight Pattern")
1. [Generating pre-calculated KING ATTACK tables](https://youtu.be/dWfwcfWg4XY) » [King Attacks](King_Pattern#KingAttacks "King Pattern")
1. [Masking relevant bishop occupancy bits to form a key for MAGIC BITBOARDS](https://youtu.be/Obe1-u3S0Y4) » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
1. [Masking relevant ROOK OCCUPANCY BITS to form a key for MAGIC BITBOARDS](https://youtu.be/bL7LW3jntw0)
1. [Generating SLIDER PIECES ATTACKS on the fly for MAGIC BITBOARD purposes](https://youtu.be/XFiZ3tjt7K4) » [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks")
1. [Implementing BIT COUNT routine (Brian Kernighan's way)](https://youtu.be/0F_aeUik91A) » [Population Count - Brian Kernighan's way](Population_Count#BrianKernighansway "Population Count")
1. [Getting least significant 1st BIT INDEX](https://youtu.be/JhLgV2P9sBg) » [Index of LS1B by Popcount](BitScan#Index_of_LS1B_by_Popcount "BitScan")
1. [Populating OCCUPANCY sets to multiply them later by MAGIC NUMBERS](https://youtu.be/nyk3usU95IY)
1. [Generating relevant OCCUPANCY BIT COUNT lookup tables for sliding pieces](https://youtu.be/gaXLyW-yMvg)
1. [Implementing pseudo RANDOM NUMBER generator using XORSHIFT32 algorithm](https://youtu.be/JjFYmkUhLN4) » [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")
1. [Generating MAGIC NUMBER candidates](https://youtu.be/KqWeOVyOoyU) » [Looking for Magics](Looking_for_Magics "Looking for Magics")
1. [Generating MAGIC NUMBERS via brute force trial and error method](https://youtu.be/UnEu5GOiSEs)
1. [Initializing SLIDER PIECES attack tables using PLAIN MAGIC BITBOARDS](https://youtu.be/1lAM8ffBg0A) » [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")
1. [Defining BITBOARDS, OCCUPANCIES and helper variables](https://youtu.be/ZBBju42pKvw) » [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
1. [Printing CHESS BOARD position and game state variables](https://youtu.be/iJ0VpXq90zY) » [Chess Position](Chess_Position "Chess Position")
1. [Parsing FEN string to initialize BITBOARDS, OCUUPANCIES & board state](https://youtu.be/IdFHFRiQtj8) » [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
1. [Getting QUEEN ATTACKS by looking up bishop & rook attack tables](https://youtu.be/KSs4KRQPOKE)
1. [Implementing routine to find out whether SQUARE IS ATTACKED](https://youtu.be/v9CEqjliv3E) » [Square Attacked By](Square_Attacked_By "Square Attacked By")
1. [Writing GENERATE MOVES function skeleton](https://youtu.be/eRvCLaa-3Rk) »[Move Generation](Move_Generation "Move Generation")
1. [Generating QUIET PAWN moves](https://youtu.be/62Hy1JEehqI) » [Pawn Pushes (Bitboards)](</Pawn_Pushes_(Bitboards)> "Pawn Pushes (Bitboards)")
1. [Generating PAWN CAPTURE moves](https://youtu.be/cezEoX8WpWs) » [Pawn Captures](</Pawn_Attacks_(Bitboards)#PawnCaptures> "Pawn Attacks (Bitboards)")
1. [Generating CASTLING MOVES](https://youtu.be/TXvV2jVl7co) » [Castling](Castling "Castling")
1. [Generating SLIDER & LEAPER piece MOVES by attack tables lookup](https://youtu.be/clNvT1W93o4)
1. [Binary formatting of MOVE ITEMS](https://youtu.be/ubX5lyIQoSs) » [Encoding Moves](Encoding_Moves "Encoding Moves")
1. [Encoding & decoding MOVE ITEMS](https://youtu.be/gyf3mr1LI7A)
1. [Implementing MOVE LIST + ADD MOVE, PRINT MOVE, PRINT MOVE LIST functions](https://youtu.be/AINYYiV-83I) » [Move List](Move_List "Move List")
1. [Populating MOVE LIST with newly GENERATED MOVES](https://youtu.be/944aTQQnWAA)
1. [Preserving & restoring BOARD STATE aka COPY/MAKE approach](https://youtu.be/CsUelozl0a8) » [Copy-Make](Copy-Make "Copy-Make")
1. [Implementing MAKE MOVE function (moving pieces)](https://youtu.be/coVPpTJN9iU) » [Make Move](Make_Move "Make Move")
1. [Implementing MAKE MOVE function (handling captures)](https://youtu.be/nkRrQnhRo80) » [Captures](Captures "Captures")
1. [Implementing MAKE MOVE function (handling pawn promotions)](https://youtu.be/gnDyJImkfVo) » [Promotions](Promotions "Promotions")
1. [Implementing MAKE MOVE function (handling enpassant moves)](https://youtu.be/5h5Z3bx0EKc) » [En passant](En_passant "En passant")
1. [Implementing MAKE MOVE function (handling double pawn pushes)](https://youtu.be/J-k2p1g6VTQ) » [Double Pawn Push](Pawn_Push#DoublePush "Pawn Push")
1. [Implementing MAKE MOVE function (handling castling moves)](https://youtu.be/pHohRpH30a0) » [Castling](Castling "Castling")
1. [Implementing MAKE MOVE function (updating castling rights)](https://youtu.be/zOWPZ4fuLGg) » [Castling Rights](Castling_Rights "Castling Rights")
1. [Implementing MAKE MOVE function (updating occupancy bitboards)](https://youtu.be/ZBotXGrgbdg) » [Occupancy](Occupancy "Occupancy")
1. [Implementing MAKE MOVE function (checking whether the king is in check)](https://youtu.be/sg4AMsXYuk4) » [Check](Check "Check")
1. [Writing a cross-platform function for GETTING TIME IN MILLISECONDS](https://youtu.be/bK_dg_gMW6s)
1. [Writing PERFT DRIVER function](https://youtu.be/o0xCJDhbSUM) » [Perft](Perft "Perft")
1. [Writing PERFT TEST function](https://youtu.be/p2VuC0xTPoc)
1. [Connecting to the GUI (parse move string)](https://youtu.be/1gOYB9HelXk) » [GUI](GUI "GUI"), [UCI](UCI "UCI")
1. [Connecting to the GUI (parse "position" command)](https://youtu.be/giSqiH6aa_o)
1. [Connecting to the GUI (parse "go" command)](https://youtu.be/lb46nX6gSBw)
1. [Connecting to the GUI (main loop) + BONUS (TSCP vs BBC blitz game)](https://youtu.be/rW2jzTA4kW4) » [TSCP](TSCP "TSCP")
1. [Implementing RUDIMENTARY EVALUATION (material score)](https://youtu.be/CMshozGbBdw) » [Evaluation](Evaluation "Evaluation"), [Material](Material "Material")
1. [Implementing RUDIMENTARY EVALUATION (positional piece scores)](https://youtu.be/E2JzRNI1ODI)
1. [Writing NEGAMAX ALPHA BETA skeleton](https://youtu.be/b8OcJM3VeaU) » [Negamax](Negamax "Negamax"), [Alpha-Beta](Alpha-Beta "Alpha-Beta")
1. [Detecting CHECKMATE and STALEMATE](https://youtu.be/lAAdjCkWd9s) » [Checkmate](Checkmate "Checkmate"), [Stalemate](Stalemate "Stalemate")
1. [Implementing QUIESCENCE SEARCH](https://youtu.be/WzEhVjdNByg) » [Quiescence Search](Quiescence_Search "Quiescence Search")
1. [Defining MVV LVA (Most Valuable Victim - Least Valuable Attacker) table](https://youtu.be/NMNBWxinpPY) » [MVV/LVA](MVV-LVA "MVV-LVA")
1. [Writing SCORE MOVE function](https://youtu.be/VeJnLN7jFm4) » [Move Ordering](Move_Ordering "Move Ordering")
1. [Writing SORT MOVES function](https://youtu.be/3-9tzzmtQQ0)
1. [Applying MOVE ORDERING to sort captures](https://youtu.be/DVSp_31iTBU) » [Captures](Captures "Captures")
1. [Sorting KILLER & HISTORY moves](https://youtu.be/MA6d1hZ1YBE) » [Killer Heuristic](Killer_Heuristic "Killer Heuristic"), [History Heuristic](History_Heuristic "History Heuristic")
1. [Collecting PV (Principle Variation) from the search](https://youtu.be/LOR-dkAkUyM) » [Principal Variation](Principal_Variation "Principal Variation")
1. [Implementing ITERATIVE DEEPENING](https://youtu.be/yVyQSUYts0A) » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
1. [Sorting PV moves + some BONUS TALK at the end](https://youtu.be/heJUljl_zNE)
1. [Implementing PVS (Principle Variation Search)](https://youtu.be/Gs4Zk6aihyQ) » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
1. [Applying LMR (Late Move Reduction)](https://youtu.be/OLT0bU0SIeg) » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
1. [Applying NULL MOVE PRUNING](https://youtu.be/n6xAzopULxU) » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
1. [Adjusting ASPIRATION WINDOW during iterative deepening](https://youtu.be/1LmdOHshYkI) » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
1. [BUG ALERT!!! Fixing PVS duplication bug](https://youtu.be/azEmgbdiecc)
1. [Handling TIME CONTROLS (forked from VICE by BluefeverSoftware)](https://youtu.be/t48NYINOekw) » [Vice](Vice "Vice")
1. [Zobrist HASHING (initialize random keys)](https://youtu.be/W7dah-dat8Q) » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
1. [Zobrist HASHING (generate hash key)](https://youtu.be/sV2C7hx-gOE)
1. [Zobrist HASHING (hash keys incremental updates)](https://youtu.be/5EMLgIFv5Qg) » [Incremental Updates](Incremental_Updates "Incremental Updates")
1. [Implementing HASH TABLE aka transposition table (define & initialize)](https://youtu.be/fEHjpzrcRxk) » [Transposition Table](Transposition_Table "Transposition Table") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
1. [Implementing HASH TABLE aka transposition table (read/write hash entry)](https://youtu.be/NcboP08y_JQ)
1. [Implementing HASH TABLE aka transposition table (connecting to search)](https://youtu.be/HNtAt9RMJVs)
1. [BUG ALERT! Fixing lack of enpassant & side hashing on null move](https://youtu.be/4SXKBTGUkjk)
1. [More search BUG FIXES &CLEANUPS](https://youtu.be/g1b_rT9VqAw)
1. [Handling MATING SCORES in HASH TABLE aka transposition table](https://youtu.be/XfeuxubYlT0) » [Mate Scores](Score#MateScores "Score")
1. [Sending MATING SCORES to GUI + some cleanups & adjustments](https://youtu.be/WcoOTg7Aq4E)
1. [Detecting THREE FOLD REPETITIONS](https://youtu.be/QhFtquEeffA) » [Repetitions](Repetitions "Repetitions")
1. [Final (hopefully!) SEARCH BUG FIXES](https://youtu.be/F8ueIueVsHI)
1. [Improving EVALUATION (setting file & rank masks)](https://youtu.be/Yqpm6Ad4scI) » [Evaluation](Evaluation "Evaluation"), [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")
1. [Improving EVALUATION (initializing isolated & passed pawn masks)](https://youtu.be/iwBkAEC4KSs) » [Isolated Pawns (Bitboards)](</Isolated_Pawns_(Bitboards)> "Isolated Pawns (Bitboards)"), [Passed Pawns (Bitboards)](</Passed_Pawns_(Bitboards)> "Passed Pawns (Bitboards)")
1. [Improving EVALUATION (double & isolated penalties, passed pawns bonus)](https://youtu.be/CgvZMsJImJg)
1. [Improving EVALUATION (open & semi open file scoring)](https://youtu.be/Bp4F_321j4I) » [Pawns and Files (Bitboards)](</Pawns_and_Files_(Bitboards)> "Pawns and Files (Bitboards)"), [Open File](Open_File "Open File")
1. [Improving EVALUATION (mobility and king safety)](https://youtu.be/iq2lxyjWZvA) » [Mobility](Mobility "Mobility"), [King Safety](King_Safety "King Safety")
1. [BBC 1.0 - RELEASE](https://youtu.be/1SgnTKzWuss)
1. [Improving BBC chess engine: TAPERED EVALUATION (getting game phase scores)](https://youtu.be/JYF6A0xvvtY) » [Tapered Eval](Tapered_Eval "Tapered Eval"), [PeSTO](PeSTO "PeSTO")
1. [Improving BBC chess engine: TAPERED EVALUATION (interpolating scores) + BONUS: BBC vs VICE match!](https://youtu.be/bOmXClI6Xpw) » [Vice](Vice "Vice")

### [GUI](GUI "GUI")

**Web based GUI for UCI CHESS ENGINE**

1. [INTRO & DEMO](https://youtu.be/_0uKZbHWVKM)
1. [Install dependencies, CREATE WEB APP & render the CHESS BOARD](https://youtu.be/OjZy52Tt6mY)
1. [Connecting engine back-end & MAKING IT PLAY!](https://youtu.be/9Hn1gnTYNS4)
1. [Printing game status, FEN & PGN](https://youtu.be/ZIyDWQN2buk)
1. [Adding GAME CONTROL buttons](https://youtu.be/ihHHW_CA72M)
1. [Adding MOVE STATS](https://youtu.be/TlxgZRd8VWk)
1. [Fixing layout & setting position from FEN string on button click](https://youtu.be/PWnypt2k56I)
1. [Adding MOVE TIME & FIXED DEPTH controls](https://youtu.be/DCWtkpEF8KY)
1. [Implementing DOWNLOAD PGN feature](https://youtu.be/tqR4tRyfTIg)
1. [Encapsulating CHESS ENGINE for SIMULTANEOUS PLAY](https://youtu.be/w67CEEjqIjw)
1. [final adjustments and DEPLOY at pythonanywhere.com](https://youtu.be/_u-VAFwY95U)

### [NNUE](NNUE "NNUE")

**Embedding Stockfish NNUE to ANY CHESS ENGINE**

1. [Intro & demo](https://youtu.be/zieTAE2zN9w) » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), [Scorpio NNUE](Scorpio#NNUE "Scorpio")
1. [Compiling existing ENGINE with NNUE library](https://youtu.be/59Fp4JVNob0)
1. [Extracting PIECES & SQUARES for direct NNUE probing](https://youtu.be/puLvzQnUoH8)
1. [Incorporating NNUE SCORES into EVALUATION function](https://youtu.be/cOdPe1JvVU8)
1. [bug fixes & experiments](https://youtu.be/30L9hx6hsmg)
1. [WINDOWS compatibility added](https://youtu.be/xFeJ9PBWpco)
1. [Switching to pure NNUE evaluation + important BUG FIX](https://youtu.be/Olnk9aa1zMI)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Bitboard CHESS ENGINE in C: intro](https://youtu.be/QUNP-UjujBM)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [GitHub - maksimKorzh/bbc: Bit Board Chess (BBC) - The easiest to understand bitboard chess engine by Code Monkey King](https://github.com/maksimKorzh/bbc)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [BBC 1.0 release - UCI chess engine by CMK](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75199) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 24, 2020
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 21, 2020
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [The Main Transposition Table](http://web.archive.org/web/20070809015843/www.seanet.com/%7Ebrucemo/topics/hashing.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)

**[Up one Level](Engines "Engines")**

