# Directives
## Overview
Directives are translator-time constructs that change the tokens before parsing. In simple terms, they change the code.

## Includes
The most useful directive is the `@include` directive. It includes a file directly in the calee's file. It expects a string as the next value followed by a mandatory newline. Files will automatically be guarded from being included twice.

util.pil
```pil
my-util-func(a)
   add a, a, a
   return a
```

main.pil
```pil
@include "util.pil"
@include "util.pil" ; valid, does nothing

main()
   my-util-func 4
   println r$0
```
This turns the code into:
```pil
my-util-func(a)
   add a, a, a
   return a

main()
   my-util-func 4
   println r$0
```

## Register size
To change the number of registers/return registers used by a file use `@reg-size` and `@return-reg-size` directives respectively. By default the program uses 16 registers and 4 return registers. Both expect a number followed by a mandatory newline. Only the last duplicated directive will take action.
```pil
@reg-size 20
@return-reg-size 8

get-eight()
   return 1, 2, 3, 4, 5, 6, 7, 8

main()
   get-eight      ; now up to 8 values can be returned
   println $19    ; and registers $0-$19 be used
```
