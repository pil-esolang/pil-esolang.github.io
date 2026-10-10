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

## Next steps
That's a quick introduction of everything PIL has to offer. For built-ins check out [Built-ins](../built-ins/strings.md).
