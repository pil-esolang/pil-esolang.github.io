# Constants
## Constant definitions
Constants are parse-time constructs. At runtime they do not exist and are wholly replaced. To define a constant use the `const` keyword:
```pil
const my-lucky-number 846.542
const the-answer 42
const my-string "Hello, World!"

main()
   println my-lucky-number
   println the-answer
   println my-string
```
After parsing the code would turn into:
```pil
main()
   println 846.542
   println 42
   println "Hello, World!"
```

## Constant evaluator
There's also a way to do math at parse-time. To do it, wrap the expression in square brackets. The constant evaluator also supports a plethora of math functions, although with a more familiar syntax.
```pil
const a [20.0 / 3.0 + 2.0]
const b [sin(pi() / 2.0)]
const c [gcd(6, 15)]

main()
   printfln "{} {} {} {}", a, b, c, [a * b * c]
```

## Constant formatting
And finally, there's a way to format strings at parse-time using `${}` and `$[]` syntax. If there's a necessity to print it, escape with `\$`. `${}` is for values, you can put as many parse-time values (non-register, non-local-variable) as you'd like and they all will get concatenated. `$[]` is for the constant evaluator, the result will be inserted as a string.
```pil
const a [20.0 / 3.0 + 2.0]
const b [sin(pi() / 2.0)]
const c [gcd(6, 15)]

main()
   println "${a} ${b} ${c} $[a * b * c]" ; this is better than the previous
                                         ; example as this moves the work to
                                         ; the parser instead of the runtime
```
After parsing, the code is simply this:
```pil
main()
   println "8.666667 1.000000 3 26.000000"
```
