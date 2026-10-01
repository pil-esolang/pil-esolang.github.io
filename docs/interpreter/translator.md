# Translator
Translator is ran right after the lexer and is responsible for modifying the token stream in various ways. This can be done solely through directives. Throws on unknown directives. Constants cannot be used in this phase as they are handled at the parser phase.

## First pass
In the first pass the translator parses the following directives. Throws on invalid directive syntax and all directives must end with a newline.

### @include
```pil
@include "FILE.pil"
```
Lexes and directly includes the file in the token stream. Guards against including the same file multiple times.

### @reg-size
```pil
@reg-size N
```
Change the register count to `N` for the program. Only the last statement is applied so it is recommended to define it after all includes. Does not matter where it's placed. Default is 16.

### @return-reg-size
```pil
@return-reg-size N
```
Change the return register count to `N` for the program. Only the last statement is applied so it is recommended to define it after all includes. Does not matter where it's placed. Default is 4.

## Second pass
The second pass runs after the first pass, meaning registers are sized and all files have been combined into a single token stream. In the second pass more intensive directives are handled, specifically syntax sugar turning easily readable code into PIL's control-flow structures.

### @loop
```pil
@loop CONDITION
   ...
@end
```
The body runs as long as `CONDITION` is true. It is checked before each iteration. Each `@loop` must be terminated with a matching `@end`. Loops can nest.

The conditions are made in the same way as in modern languages: `&&` - and, `||` - or, `!` - not, `<` - lesser, `<=` - lesser or equal, `>` - greater, `>=` - greater or equal, `==` - equal, `!=` - inequal. Parentheses are supported as well for changing operator precedence. Math operations are not supported, however math evaluator can be used.

It works by compiling the condition into a start label with the condition being a chain of PIL control-flow commands. At the `@end` directive a goto is placed back to the start as well as the end label.

Every comparison and logical operation uses a fresh register that is counted down from the top. Condition with more operators than there are registers throws.
