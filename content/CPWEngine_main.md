---
title: CPWEngine main
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * main**

The main routine of the engine.

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

