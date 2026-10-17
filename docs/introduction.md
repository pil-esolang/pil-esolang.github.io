# Introduction
PIL is a loosely-typed language with no GC. It's simple - you can define functions and call them.
```pil
my-func()
   println "Hello, World!";

main()
   my-func; # Hello, World!
```

## Comments
Comments start with `#`. There are no multi-line comments in PIL.
```
# this is a comment
```

## Control flow
There are no control statements (like if-else, for, while, break...), instead you have to define labels and jump to them.
```pil
check-condition(condition)
   jmp condition, check-condition-true;
   println "The condition is false!";
   return;
check-condition-true:
   println "The condition is true!";

main()
   check-condition 1; # The condition is true!
   check-condition 0; # The condition is false!
```
It's same with loops. Here's a loop that counts from 1 to 10:
```pil
loop(i, n)
loop-start:
   greq i, n, $0;
   jmp $0, loop-end;

   println i;
   incr i;
   goto loop-start;
loop-end:

main()
   loop 1, 10;
```

## Variables
Variables can be defined inside functions using the `local` keyword.
```pil
greet()
   local name;
   print "Tell me your name: ";
   readln name;
   printfln "Hello, {}!", name;
   string-free name;

main()
   greet;
```

## Including other files
To include a file use `@include`. It works similarly to C's includes but doesn't require guards:

include.pil
```pil
my-func()
   println "Hello, World!";
```

main.pil
```pil
@include "include.pil"

main()
   my-func;
```

## Structures
PIL also contains structures that can be defined using the `struct` keyword:
```pil
struct Vec2 ( x, y )

main()
   local v1, v2, v3;
   make Vec2, v1, 1.0, 2.0;
   make Vec2, v2, 3.0, 4.0;

   local x, y;
   add v1.x, v2.x, x;
   add v1.y, v2.y, y;
   make Vec2, v3, x, y;

   printfln "Result: ({}, {})", v3.x, v3.y;
   free v1, v2, v3;
```

And structures can be used as arrays if necessary using the `array` keyword:
```pil
struct array MyArray ( _1, _2, _3, _4, _5 )

main()
   local array;
   make MyArray, array, 5, 4, 3, 2, 1;
   println array; # [5, 4, 3, 2, 1]
   array-reverse array;
   println array; # [1, 2, 3, 4, 5]
   array-shuffle array;
   println array; # [3, 5, 2, 1, 4] could be something else for you

   local x, y, z;
   array-sort array, 1;
   add array._1, array._2, x;
   add array._3, array._4, y;
   add array._5, array._1, z;
   printfln "[{},{},{}]", x, y, z; # 3, 7, 6
   free array;
```

## Enumerations
PIL also contains enumerations:
```pil
enum Day (
   Monday = 1,
   Tuesday,
   Wednesday,
   Thursday,
   Friday,
   Saturday,
   Sunday,
)

main()
   local today, day-names, name;
   array-new day-names, "", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday";
   set Day.Wednesday, today;
   array-at day-names, today, name;
   printfln "Today is {}, {} day of the week.", name, today; # Today is Wednesday, 3 day of the week.
   array-free day-names;
```

## Constants and globals
Constants are named values that cannot change. Globals are variables that can be accessed from anywhere. They are defined using `const` and `global` keywords respectively.
```pil
const pi = 3.141592;
global r = 10.0;

area()
   local result;
   mul r, r, result;
   mul result, pi, result;
   return result;

main()
   local result;
   call result, area;
   println result; # 314.159
   set 20.0, r;
   call result, area;
   println result; # 1256.637
```

## Next steps
For a better understanding of the language you can continue reading the documentation. But you learn the best by doing. Check out [Getting Started](getting_started.md) for installation steps.
