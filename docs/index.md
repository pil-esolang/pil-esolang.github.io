# PIL Esolang
PIL is a primitive interpreted esolang (esoteric programming language) based off COBOL and assembly. It is a loosely-typed language with no GC.

Here's a full working factorial example:
```pil
factorial(n) let minus1, result     ; define a new function and two variables - minus1, result
   leeq n, 1, $0                    ; check if N is smaller or equal to 1 and store the result in register 0
   jmp $0, factorial-end            ; if it is, jump to end, where we return 1

   sub n, 1, minus1                 ; subtract one from N and store it in minus1
   call result, factorial, minus1   ; call factorial and store in result
   mul result, n, result            ; multiply N by result
   return result                    ; return it
factorial-end:
   return 1

main()                              ; main program entry point
   factorial 5.0                    ; calculate factorial of 5
   printn R$0                       ; 120
```

Think of it like interpreted assembly with functions, returns and higher-level instructions. For more examples check out the [Introduction](introduction.md). To try it yourself check out [Getting Started](getting_started.md).
