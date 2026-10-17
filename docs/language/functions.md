# Functions
Functions are reusable pieces of code that can be called from anywhere in the program. A PIL file consists solely from functions and function calls. Each program starts with the main function. Code outside of functions is not permitted and not ran.

## Declaration
To declare a function, you need an unique identifier followed by parentheses with an optional parameter list:
```pil
NAME(PARAM1?, PARAM2?...)
   BODY...
```
In practice it looks like this:
```pil
my-hello-world()
   println "Hello, World!";

my-add(a, b)
   add a, b, $0;
   return $0;
```

## Calling
To call a function follow its identifier by the arguments to pass to it. Function calls must be terminated by a semicolon.
```pil
main()
   my-hello-world;
   my-add 523, 814;
   println r$0;
```

Arguments pass copies to trivial objects (integer, floats, characters) and copies of references to allocated objects (arrays, maps, file handles) and such containers cannot be passed, only the underlying value. If a function has to return a value without a return, a solution could be to pass an integer and then set the register at the integer with [reg-set](../built-ins/builtins.md#reg-set) built-in.
```pil
add-copy(a, b, r)
   add a, b, $0;
   reg-set r, $0;
```

Functions can also be called using some built-ins, such as [call](../built-ins/builtins.md#call), [func-call](../built-ins/builtins.md#func-call) and [catch](../built-ins/builtins.md#catch). Call supports named returns and all support argument passing. Each is used for their own case.

## Returning
To return values from a function, use the [return](../built-ins/builtins.md#return) bulit-in. You can return as many values as you'd like (as long as you have enough [return registers](variables.md#registersreturn-registers)). Some return built-ins are available such as the [return-count](../built-ins/builtins.md#return-count), which returns the returned value count.

A function can return a variable amount of values based on different paths. Returned variables can either be accessed via [return registers](variables.md#registersreturn-registers) or [return built-ins](../built-ins/builtins.md#return-reg-size).
```pil
get-some(condition)
   jmp condition, get-some-more;
   return 1, 2;
get-some-more:
   return 1, 2, 3, 4;

main()
   get-some 0;
   return-count $0;
   printfln "{}: {},{}", $0, r$0, r$1; # 2: 1,2

   get-some 1;
   return-count $0;
   printfln "{}: {},{},{},{}", $0, r$0, r$1, r$2, r$3; # 4: 1,2,3,4
```
