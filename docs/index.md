# PIL Esolang
PIL is a primitive interpreted esolang (esoteric programming language) based off COBOL and assembly. It is a loosely-typed language with no GC.

Here's a factorial example:
```pil
# calculates the factorial of N
factorial(n)
   local result, cond, minus1;      # define new variables
   leeq n, 1, cond;                 # check if N is smaller or equal to 1
   jmp cond, factorial-end;         # if it is, jump to end, where we return 1

   sub n, 1, minus1;                # calculate n-1
   call result, factorial, minus1;  # call factorial and store in result
   mul result, n, result;           # calculate the factorial of N
   return result;                   # return the result

factorial-end:
   return 1;

main()                              # main is called on start
   local result;                    # define a new variable
   call result, factorial, 5.0;     # calculate 5!
   println result;                  # 120
```

Think of it like interpreted assembly with functions, returns and higher-level instructions. For more examples check out the [Introduction](introduction.md). See [Getting Started](getting_started.md) for installation instructions.
