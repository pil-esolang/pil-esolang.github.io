# Directives
Directives are translator-time constructs that modify the token stream or set some interpreter configuration.

## @include
```pil
@include "FILE.pil"
```
Lexes and directly includes the file in the token stream. Guards against including the same file multiple times.

## @reg-size
```pil
@reg-size N
```
Change the register count to `N` for the program. Only the last statement is applied so it is recommended to define it after all includes. Does not matter where it's placed. Default is 16.

## @return-reg-size
```pil
@return-reg-size N
```
Change the return register count to `N` for the program. Only the last statement is applied so it is recommended to define it after all includes. Does not matter where it's placed. Default is 4.
