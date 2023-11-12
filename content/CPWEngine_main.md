---
title: CPWEngine main
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * main**

The main routine of the engine.

## Contents

- [1 Code](#code)
  - [1.1 Header](#header)
  - [1.2 int main()](#int-main.28.29)
- [2 External Calls](#external-calls)

## Code

## Header

```C++

enum etask {
  TASK_NOTHING,
  TASK_SEARCH
} extern task;

```

## int main()

```C++

int main() {
  com_init();

  while (1) {
    if (task == TASK_NOTHING) {
      com();
    }
    else {
      root();
      task = TASK_NOTHING;
    }
  }
  return 0;
}

```

## External Calls

- [com();](CPW-Engine_com "CPW-Engine com")
- [root();](CPW-Engine_root "CPW-Engine root")

**[Up one Level](CPW-Engine "CPW-Engine")**

