# Introduction
PIL is a loosely-typed language with no GC. It's simple, you can define functions and call them.
```pil
my-func()
   println "Hello, World!"

main()
   my-func
```

## Comments
Comments start with a semicolon. There are no multi-line comments in PIL.
```
; this is a comment
```

## Control flow
There are no control statements (like if-else, for, while, break...), instead you can define labels and jump to them.
```pil
check-condition(condition)
   jmp condition, check-condition-true
   println "The condition is false!"
   return
check-condition-true:
   println "The condition is true!"

main()
   check-condition 1
   check-condition 0
```
It's same with loops. Here's a loop that counts from 1 to 10:
```pil
loop(i, n)
loop-start:
   println i
   incr i
   leeq i, n, $0
   jmp $0, loop-start

main()
   loop 1, 10
```

## Variables
Unlike other languages, PIL requires the variables to be defined in the function definition. It can be done using the `let` keyword.
```pil
greet() let name
   print "Tell me your name: "
   readln name
   printfln "Hello, {}!", name
   string-free name

main()
   greet
```

## Including other files
To include a file just use `@include`. It works similarly to C's includes but doesn't require guards:

include.pil
```pil
my-func()
   println "Hello, World!"
```

main.pil
```pil
@include "include.pil"

main()
   my-func
```

## Strings
PIL has a built-in string library with +40 methods. Here are some of them:
```pil
pretty-print(a, b, c, d)
   println "Strings: "
   println "1: ", a
   println "2: ", b
   println "3: ", c
   println "4: ", d

main() let a, b, c, d
   string-new a, "string1"
   string-format b, "string{}", 2
   string-copy a, c
   string-set c, 6, '3'
   string-repeat d, 10, "ab"
   pretty-print a, b, c, d

   string-reverse a
   string-free b
   string-concat c, "abcdef"
   string-erase-all d, "a"
   pretty-print a, b, c, d

   string-free a, c, d
```

## Arrays
The second complex data structure in PIL are the arrays with +30 built-in methods. Here's a small example:
```pil
main() let a, s
   array-new a, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   println a

   array-clear a
   println a

   array-push a, 2
   array-push a, 3
   array-push a, 4
   array-push a, 5
   array-insert a, 0, 1
   println a

   array-pop a
   array-pop a
   array-join a, "; ", s
   println s

   array-shuffle a
   println a

   array-free a
   string-free s
```

## Maps
And the last complex data structure are the maps. Here's an example:
```pil
main() let m, a
   map-new m
   map-set m, "john", 20
   map-set m, "jane", 30
   map-set m, "jake", 40
   map-set m, "jenny", 50
   println m

   map-at m, "john", $0
   map-contains m, "john", $1
   println $0, ' ', $1

   map-at m, "johnny", $0
   map-contains m, "johnny", $1
   println $0, ' ', $1

   map-keys m, a
   println a

   array-free a
   map-free m
```

## Constants
PIL interpreter has a few nice tools to calculate values at parse-time to make the runtime more performant. One of them are the constants:
```pil
const magic-number 42
const my-message "Hello, World!"

main()
   println magic-number
   println my-message
```
There are also the constant evaluator and the constant string formatter:
```pil
const magic-number [sqrt(20.4) * sin(tau()) - exp(pi())]
const error-message "Expected num to be ${magic-number}, got {} instead."

complex-math(num)
   ; do complex math...
   error error-message, num

main()
   complex-math 20
```

## Next steps
For a better understanding of the language you can continue reading the introduction or move on to the real documentation. Or if you'd like to try it out yourself, see [Getting Started](getting_started.md).
