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
   local result;
   add a, b, result;
   return result;
```

## Calling
To call a function follow its identifier by the arguments to pass to it. Function calls must be terminated by a semicolon.
```pil
main()
   my-hello-world;
   local result;
   call result, my-add, 523, 814;
   println result;
```

Arguments pass copies to trivial objects (integer, floats, characters) and copies of references to allocated objects (arrays, maps, file handles) and such containers cannot be passed, only the underlying value.

Functions can also be called using some built-ins, such as [call](../built-ins/builtins.md#call), [func-call](../built-ins/builtins.md#func-call) and [catch](../built-ins/builtins.md#catch). Call supports named returns and all support argument passing. Each is used for their own case.

## Returning
To return values from a function, use the [return](../built-ins/builtins.md#return) bulit-in. You can return as many values as you'd like. Some return built-ins are available such as the [return-count](../built-ins/builtins.md#return-count), which returns the returned value count.

A function can return a variable amount of values based on different paths. Returned variables can be retrieved using [return-count](../built-ins/builtins.md#return-count) and [return-at](../built-ins/builtins.md#return-at).
```pil
get-some(condition)
   jmp condition, get-some-more;
   return 1, 2;
get-some-more:
   return 1, 2, 3, 4;

main()
   local count;
   get-some 0;
   return-count count;
   println count;

   get-some 1;
   return-count count;
   println count;
```
