# PIL Esolang
PIL is a primitive interpreted esolang (esoteric programming language) based off COBOL and assembly. It is a loosely-typed language with no GC.

Here's a factorial example:
```pil
# calculates the factorial of N
factorial(n)
   let result;                   # define a new variable
   leeq n, 1, $0;                # check if N is smaller or equal to 1
   jmp $0, factorial-end;        # if it is, jump to end, where we return 1

   sub n, 1, $1;                 # calculate n-1
   call result, factorial, $1;   # call factorial and store in result
   mul result, n, result;        # calculate the factorial of N
   return result;                # return the result

factorial-end:
   return 1;

main()                           # main is called on start
   factorial 5.0;                # calculate 5!
   println r$0;                  # 120
```

Think of it like interpreted assembly with functions, returns and higher-level instructions. For more examples check out the [Introduction](introduction.md). See [Getting Started](getting_started.md) for installation instructions.
