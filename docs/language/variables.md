# Variables
Variables are containers that can store a value. A variable doesn't have a type tied to it and can store any value, that can dynamically change during runtime.

## Locals
Locals are variables that are purely local to a function. There are two types of locals - function parameters and locals defined by `local` keyword. Locals cannot be used outside of the function they are defined in.

Local define is a parse-time construct and so a local define is available by any path after the point it is defined. This means same local defines in a switch statement are not permitted, since local does not care about the control flow of the function.
```pil
func(a, b)
   local c, d;
   goto skip;
   local e;
skip:
   # e is valid here, even though local was never touched.
```

## Globals
Globals are variables that can be accessed by any part of the program after the point it is defined. A global defined inside a function is still accessible to all functions and commands after it, although it is not recommended to do so.

Globals can be defined using `global` keyword. Just like locals, globals are parse-time constructs, but unlike locals, can be assigned an initial value. Unlike constants, their value can change during runtime. Global constructs can be chained using commas, with the last one ending with a semicolon.
```pil
global my-global = 1337;
global other-global;

main()
   set 42, other-global;
   println my-global, ' ', other-global;
```

## Constants
Constants are values that cannot change during runtime. They are also parse-time constructs that are completely erased before runtime begins. They can be defined using `const` keyword similarly to globals, but must have a value.
```pil
const my-const = 1337, pi = 3.141592;

main()
   println my-const, ' ', pi;
```

## Registers/return registers
By default there are 16 registers and 4 return registers for a program. But that can be changed using [Directives](directives.md). Registers are global containers that do not need to be defined. They should be used for temporary, unimportant values such as conditions. They can be accessed using `$N` and `r$N` syntax respectively and are 0-indexed.

Registers cannot be accessed using runtime values but can be using parse-time constructs such as constants and enumerations. This can be used to create named registers, which is equal to globals. The only reason for this could be the register built-ins.

Return registers are set by the [return](../built-ins/builtins.md#return) built-in, which is added at the end of every function if it is not already present. Return registers are set in the same order they are returned and can be read and modified just like regular registers. Return registers are not cleared if a function returns less than previously, instead a flag is set to the return count of the function, which can be retrieved with the [return-count](../built-ins/builtins.md#return-count) built-in. If more values are returned than there are return registers, parse-time error is thrown and they must be bumped up using [@return-reg-size](directives.md#return-reg-size) directive.
```pil
const cond = 0;

my-min(a, b)
   le a, b, $cond;
   jmp $cond, my-min-a-less;
   return b;
my-min-a-less:
   return a;

main()
   my-min 10, 20;
   println r$0;
```
