# Values
## Overview
A container can hold any value and are not type-checked. There are 3 types of values - parse-time, runtime and containers. Parse-time is before starting the program.

## Parse-time values
Parse-time values are basic values that can be constructed at parse-time. These include integers, floating-point numbers, characters and constant strings.
```pil
20 ; integer
3.141592 ; floating
'a', '\n' ; characters
"String" ; constant string
```

## Runtime values
Runtime values are values that must be allocated to use or require post-parsing references, therefore not being able to be used at parse-time. These include dynamic strings, arrays, maps, function pointers, labels and null.
```pil
string-new s, "String" ; allocate a new dynamic string
array-new a, 1, 2, 3 ; allocate a new array
map-new m, "John", 1, "Jake", 2, "Jane", 3 ; allocate a new map
to-int "" ; null
println main ; function pointer
MY-LABEL:
println MY-LABEL ; label
```

## Containers
Containers are runtime values that store other values. These include registers, return registers and locals. Locals are function parameters and `let` defined variables:
```pil
main() let a, b, c
   println $0
   println r$0
   println a
```
