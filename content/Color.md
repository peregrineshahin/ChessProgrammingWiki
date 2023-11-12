---
title: Color
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Color**

\[ [Viktor Vasnetsov](Category:Viktor_Vasnetsov "Category:Viktor Vasnetsov") - [Last Judgment](https://en.wikipedia.org/wiki/Last_Judgment) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
In Chess, **Color** refers to the color of the two [piece sets](Pieces "Pieces"), the color each player is assigned to, the [side to move](Side_to_move "Side to move"), and the [color of a square](Color_of_a_Square "Color of a Square").
The [pieces](Pieces "Pieces") are divided, into white and black sets, but their colors should not taken literally. The players are referred to as "White" and "Black", they control their associated pieces. The colors of the sixty-four [squares](Squares "Squares") alternate and are referred to "light squares" and "dark squares", sometimes also referred to "White" and "Black" squares.

## Contents

- [1 Color Definition](#color-definition)
- [2 Toggle Color](#toggle-color)
- [3 See also](#see-also)
- [4 External Links](#external-links)
- [5 References](#references)

## Color Definition

Since there are only two colors, one bit is sufficient to encode them. This is how one may define colors in [C++](Cpp "Cpp"):

```C++

enum enumColor {
   ecWhite = 0,
   ecBlack = 1
};

```

## Toggle Color

Since the players alternately move, one need to toggle the [side to move](Side_to_move "Side to move") color after each [move](Moves "Moves") made inside the [Chess Position](Chess_Position "Chess Position") object. This can be done by subtracting color from one (ecBlack), ...

```C++

inline enumColor toggleColor(enumColor color) {
   return ecBlack - color;
}

```

... or a little bit cheaper, by xoring the color as left operand inside a register or memory cell with an immediate constant (ecBlack).

```C++

inline enumColor toggleColor(enumColor color) {
   return color ^ ecBlack;
}

```

## See also

- [Color Flipping](Color_Flipping "Color Flipping")
- [Color of a Square](Color_of_a_Square "Color of a Square")
- [Color Weakness](Color_Weakness "Color Weakness")
- [Side to move](Side_to_move "Side to move")

## External Links

- [Color from Wikipedia](https://en.wikipedia.org/wiki/Color)
- [Black and whitefrom Wikipedia](https://en.wikipedia.org/wiki/Black_and_white)
- [Black-and-white dualism from Wikipedia](https://en.wikipedia.org/wiki/Black-and-white_dualism)
- [Black & White (video game) from Wikipedia](https://en.wikipedia.org/wiki/Black_%26_White_%28video_game%29)
- [Black from Wikipedia](https://en.wikipedia.org/wiki/Black)
- [White from Wikipedia](https://en.wikipedia.org/wiki/White)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Last Judgment](https://en.wikipedia.org/wiki/Last_Judgment) fresco by [Viktor Vasnetsov](Category:Viktor_Vasnetsov "Category:Viktor Vasnetsov"), between 1885 and 1896, [St. Vladimir's Cathedral](https://en.wikipedia.org/wiki/St_Volodymyr%27s_Cathedral), [Kiev](https://en.wikipedia.org/wiki/Kiev), [Ukraine](https://en.wikipedia.org/wiki/Ukraine), [Black-and-white dualism from Wikipedia](https://en.wikipedia.org/wiki/Black-and-white_dualism), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)

**[Up one Level](Chess "Chess")**

