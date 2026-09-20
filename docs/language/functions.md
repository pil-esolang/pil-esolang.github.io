# Functions
## Preface
Before starting, there are some things that you must know about the language.

First, there are only single-line comments, which start with a semicolon:
```pil
; this is a comment
```
Second, identifiers are case-sensitive and can contain dashes and digits, but cannot start with them.

Third, commas are optional but highly recommended.

## Definition
A PIL file consists solely from functions and function calls, rest is syntax sugar and for convenience. To create a function you need an unique identifier followed by parentheses:
```pil
NAME()
   BODY...

; or
NAME(PARAM1, PARAM2, ...) let VAR1, VAR2, ...
   BODY...
```
And in practice:
```pil
print-hello-world()
   println "Hello, World!"

my-add(a, b)
   add a, b, $0
   return $0

my-complex-add(a, b, c, ...) let d, e, f, g
   variadic-size d
   add a, b, c, f
   set 0, g
   leeq d, g, e
   jmp e, loop-end
loop:
   variadic-at g, e
   add f, e, f
   incr g
   le g, d, e
   jmp e, loop
loop-end:
   return f
```

## Calling
To call a function follow its identifier by the arguments to pass to it:
```pil
main()
   print-hello-world
   my-add 10, 20
   println r$0 ; 30
   my-complex-add 1, 2, 3
   println r$0 ; 6
   my-complex-add 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   println r$0 ; 55
```
Passed argument count must match function's parameter count. If the function is variadic, the argument count must be at least the count of parameters.

`main` is a special function that must be present in all PIL scripts. It gets called at the start of the program. It must not have any parameters.

There are also a plethora of built-in functions in PIL that the user can call without including anything. They can be called the same way as user-defined functions.

## Returning
To return a value or more, the `return` function must be used. You can return as many values as you'd like (as long as you have enough return registers, more on that in [Registers](registers.md)). Some return built-ins are available such as the `return-count`, which simply returns the amount of values returned from the last function.

A function can return a variable amount of values based on different paths.
```pil
get-some(condition)
   jmp condition get-some-more
   return 1, 2
get-some-more:
   return 1, 2, 3, 4

main()
   get-some 0
   return-count $0
   println $0 ; 2

   get-some 1
   return-count $0
   println $0 ; 4
```

## Variables
Variable must be defined in the function definition. They can be set and used just like parameters can. By default they have a null value:
```pil
my-func() let a, b, result
   set 10, a
   set 20, b
   add a, b, result
   println result
```

## Variadics
To declare a function as variadic, use `...` at the end of parameter list. Later the values can be accessed via `variadic-size` and `variadic-at` functions:
```pil
sum(...) let size, i, total, condition, variadic
   variadic-size size
   set 0, i
   set 0, total
   le i, size, condition
   jmpn condition, sum-loop-end
sum-loop:
   variadic-at i, variadic
   add total, variadic, total
   incr i
   le i, size, condition
   jmp condition, sum-loop
sum-loop-end:
   return total
```
And variadic functions can be called with any parameter count:
```pil
main()
   sum
   println r$0 ; 0
   sum 1, 2, 3
   println r$0 ; 6
   sum 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   println r$0 ; 55
```
