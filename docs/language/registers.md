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

These built-ins are runtime, whereas the `$N` syntax is lex-time. Whether a register is out of bounds will be checked at parse-time, and such the following syntax is not okay:
```pil
const my-constant 12

main()
   println $my-constant ; Error: Invalid register: $ at ...
   println $[20 / 2] ; Error: Invalid register: $ at ...
   println $ 0 ; Error: Invalid register: $ at ... note the space
```
