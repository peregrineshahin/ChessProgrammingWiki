---
title: Oxidation
---

Oxidation is a [UCI](UCI) compliant variant engine written in [Rust](Rust) and licensed under the [GPL](GPL). The variants are configured through optional parameters added to the end of the FEN. The engine and a GUI for playing the variants can be found in the [Liberty Chess](https://github.com/Mathmagician8191/Liberty-Chess) repository, although the GUI currently only supports an embedded Oxidation engine.

## Variant features supported:
 - Arbitrary board sizes
 - 12 new types of pieces (Archbishop, Chancellor, Camel, Zebra, Mann, Nightrider, Champion, Centaur, Amazon, Elephant, Obstacle, Wall)
 - Friendly fire mode (optional setting that lets you capture your own pieces)
 - Support for arbitrary numbers of kings (losing if any of them are checkmated, or by losing all your pieces if you have no king)
 - Options to configure the number of moves a pawn can go on its first move and other miscellaneous settings

## Search features:
 - [Alpha-beta search](AlphaBeta)
 - [Quiescence Search](Quiescence_Search) with a limited depth to prevent potential search explosions in variants
 - [Transposition Table](Transposition_Table)
 - [Check Extensions](Check_Extensions)
 - [Null Move Pruning](Null_Move_Pruning)

## Evaluation features:
 - [Material](Material)
 - A penalty for being on the edge of the board
 - Parameter values tuned with [Texel tuning](Texel27s_Tuning_method)
