# Registers
## Introduction
Think of registers like global un-named variables. There are two types of registers: registers and return registers. Registers can be accessed via `$N` and `R$N` syntax:
```pil
my-func()
   return 1, 2

main()
   set 20, $0
   set 50, $1
   println $0 ; acess register 0 - 20
   println $1 ; acess register 1 - 50

   my-func
   println r$0 ; access return register 0 - 1
   println r$1 ; access return register 1 - 2
```

## Return registers
Registers are never edited by the interpreter unless specifically requested by the user. Whereas return registers are overwritten anytime a user-defined function returns a value or more.

It's completely valid to access a return register that hasn't been written to (e.g. you return 2 values but access R$3). By default you'll get a null value or some old return. Values will be written in the order they are returned.
```pil
get-three()
   return 1, 2, 3

main()
   get-three
   println r$0, r$1, r$2 ; 123
```

## Directives
There's a limit on how many registers you can have. By default it is 16 for registers and 4 for return registers. However, you can set your own limit by using the `@reg-size` and `@return-reg-size` directives (more on those in [Directives](directives.md)).
```pil
@reg-size 20

main()
   set 42, $19
   println $19
```

## Built-ins
There are also built-ins for dynamically accessing and writing to registers. For this, `reg-size`, `reg-at`, `reg-set` and the return counterparts, including `return-count`, exist.

These built-ins are runtime, whereas the `$N` syntax is parse-time. Whether a register is out of bounds will be checked at parse-time:
```pil
const my-lucky-reg 12

; func(a, b, reg)
;    add a, b, $reg ; Error: Expected an Integer/Floating after register...

main()
   set 20, $12
   println $my-lucky-reg ; 20
   println $[20 / 2 + 2] ; 20
   println $ 12 ; 20
   ; func 20, 30, $[10 + 2]
```
