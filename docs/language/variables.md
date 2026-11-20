# Variables
Variables are containers that can store a value. A variable doesn't have a type tied to it and can store any value, that can dynamically change during runtime.

## Locals
Locals are variables that are purely local to a function. There are two types of locals - function parameters and locals defined by `local` keyword. Locals cannot be used outside of the function they are defined in. By default locals are set to null value.

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

Globals can be defined using `global` keyword. Just like locals, globals are parse-time constructs, but unlike locals, can be assigned an initial value. By default globals are set to null value. Unlike constants, their value can change during runtime. Global constructs can be chained using commas, with the last one ending with a semicolon.
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
