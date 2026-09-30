# Built-ins
## Introduction
These are basic operation/miscellaneous built-ins present in PIL. On top of these, there are some more common math operation built-ins in the [Math Library](#math.md). Unlike other built-in documentation pages, these will contain sub-groups.
## Input/output
### printch
Output a single character to the terminal. `CHAR` - character.
```pil
printch CHAR
```

### print
Output all `ARGS` to the terminal. Does not output a separator or a newline. `ARGS...` - any value.
```pil
print ARGS...
```

### println
Output all `ARGS` to the terminal including a newline. Does not output a separator. `ARGS...` - any value.
```pil
println ARGS...
```

### printf
Formats the `FORMAT-STRING` string with all arguments after it and outputs it to the terminal. Works by replacing all `{}` with the arguments in left-to-right direction. Does not validate format argument count. `FORMAT-STRING` - constant or dynamic string, `ARG1...` - any value except for maps.
```pil
printf FORMAT-STRING, ARG1, ...
```

### printfln
Formats the `FORMAT-STRING` string with all arguments after it and outputs it and a newline to the terminal. Works by replacing all `{}` with the arguments in left-to-right direction. Does not validate format argument count. `FORMAT-STRING` - constant or dynamic string, `ARG1...` - any value except for maps.
```pil
printfln FORMAT-STRING, ARG1, ...
```

### read
Read a single word (until a whitespace is hit) from the user, allocate it as a string and store it in `DESTINATION`. `DESTINATION` - container.
```pil
read DESTINATION
```

### readln
Read a whole line (until a newline is hit) from the user, allocate it as a string and store it in `DESTINATION`. `DESTINATION` - container.
```pil
readln DESTINATION
```

### readch
Read a single character from the user and store it in `DESTINATION`. Does not output the character to the console nor wait for a newline. `DESTINATION` - container.
```pil
readch DESTINATION
```

### setecho
Set terminal echo based on `VALUE`s truthiness. 0 - off, otherwise on. When echo is off, nothing is output to the terminal. Does not change behavior of `readch`. `VALUE` - any value.
```pil
setecho VALUE
```

## Control flow
### le
Checks if `A` is less than `B` and if it is, stores 1 in `DESTINATION`, otherwise 0. Types of `A` and `B` must match, although integers can be compared to floats. `A` - number, character or any string, `B` - number, character or any string, `DESTINATION` - container.
```pil
le A, B, DESTINATION
```

### gr
Checks if `A` is greater than `B` and if it is, stores 1 in `DESTINATION`, otherwise 0. Types of `A` and `B` must match, although integers can be compared to floats. `A` - number, character or any string, `B` - number, character or any string, `DESTINATION` - container.
```pil
gr A, B, DESTINATION
```

### leeq
Checks if `A` is less than or equal to `B` and if it is, stores 1 in `DESTINATION`, otherwise 0. Types of `A` and `B` must match, although integers can be compared to floats. `A` - number, character or any string, `B` - number, character or any string, `DESTINATION` - container.
```pil
leeq A, B, DESTINATION
```

### greq
Checks if `A` is greater than or equal to `B` and if it is, stores 1 in `DESTINATION`, otherwise 0. Types of `A` and `B` must match, although integers can be compared to floats. `A` - number, character or any string, `B` - number, character or any string, `DESTINATION` - container.
```pil
greq A, B, DESTINATION
```

### eq
Checks if `A` is equal to `B` and if it is, stores 1 in `DESTINATION`, otherwise 0. If `A` and `B` don't share the same type 0 is stored, comparing integers to floats is an exception. `A` - number, character, any string or array, `B` - number, character, any string or array, `DESTINATION` - container.
```pil
eq A, B, DESTINATION
```

### neq
Checks if `A` is not equal to `B` and if it's not, stores 1 in `DESTINATION`, otherwise 0. If `A` and `B` don't share the same type 1 is stored, comparing integers to floats is an exception. `A` - number, character, any string or array, `B` - number, character, any string or array, `DESTINATION` - container.
```pil
neq A, B, DESTINATION
```

### or
Checks if either `A` or `B` is true and if so, stores 1 in `DESTINATION`, otherwise 0. `A` - any value, `B` - any value, `DESTINATION` - container.
```pil
or A, B, DESTINATION
```

### and
Checks if both `A` and `B` are true and if so, stores 1 in `DESTINATION`, otherwise 0. `A` - any value, `B` - any value, `DESTINATION` - container.
```pil
and A, B, DESTINATION
```

### not
Stores the opposite of `VALUE`s truthiness in `DESTINATION` - if it is 0, then 1, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
not VALUE, DESTINATION
```

### goto
Unconditionally jumps to `LABEL`. `LABEL` - label.
```pil
goto LABEL
```

### jmp
Jumps to `LABEL` if `CONDITION` is truthy, otherwise does nothing. `CONDITION` - any value, `LABEL` - label.
```pil
jmp CONDITION, LABEL
```

### jmpn
Jumps to `LABEL` if `CONDITION` is not truthy, otherwise does nothing. `CONDITION` - any value, `LABEL` - label.
```pil
jmpn CONDITION, LABEL
```

### jmptable
Checks `VALUE` against all `TARGET`s and if there is a match, then jump to the label after it. If the passed argument count is even and there are no matches, jump to `DEFAULT-LABEL`, otherwise do nothing. Each `TARGET` must have a corresponding `LABEL` after it. `VALUE` - number, character, any string or array, `TARGET...` - number, character, any string or array, `LABEL...` - label, `DEFAULT-LABEL?` - optional label.
```pil
jmptable VALUE, TARGET, LABEL..., DEFAULT-LABEL?
```

### call
Calls `FUNCTION` with given arguments `ARGS...` (if any) and stores all of the returns in `RETURNS...` (if any). Throws if `ARGS...` count does not match `FUNCTION`s arity or if `FUNCTION` is not parse-time. For runtime function calls use [func-call](#func-call). Throws a warning if `RETURNS...` count does not match actual returned value count. `RETURNS...` - containers, `FUNCTION` - function, `ARGS...` - any value.
```pil
call RETURNS..., FUNCTION, ARGS...
```

### func-call
Calls `FUNCTION` with given arguments `ARGS...` (if any). Throws if `ARGS...` count does not match `FUNCTION`'s arity. `FUNCTION` - function, `ARGS...` - any value.
```pil
func-call FUNCTION, ARGS...
```

### return
Returns from the function and stores all `VALUES...` (if any) in return registers. Exits the program if called from main function. `VALUES...` - any value.
```pil
return VALUES...
```

## Error handling
### catch
Calls `FUNCTION` with given arguments `ARGS...` (if any) and allocates and stores all errors as an array of strings in `DESTINATION` if any were thrown, otherwise stores null. Throws if `ARGS...` count does not match `FUNCTION`'s arity. `DESTINATION` - container, `FUNCTION` - function, `ARGS...` - any value.
```pil
catch DESTINATION, FUNCTION, ARGS...
```

### assert
Exits the program and formats the `FORMAT-STRING` in the same manner as [printf](#printf) if `CONDITION` is not truthy. Does not precompute the message if the `CONDITION` is truthy. `CONDITION` - any value, `FORMAT-STRING` - constant or dynamic string, `ARGS...` - any value except for maps.
```pil
assert CONDITION, FORMAT-STRING, ARGS...
```

### warn
Formats the `FORMAT-STRING` in the same manner as [printf](#printf) and outputs it as a warning. `FORMAT-STRING` - constant or dynamic string, `ARGS...` - any value except for maps.
```pil
warn FORMAT-STRING, ARGS...
```

### error
Formats the `FORMAT-STRING` in the same manner as [printf](#printf), outputs it as an error and as long as the error isn't caught using [catch](#catch), exits the program. `FORMAT-STRING` - constant or dynamic string, `ARGS...` - any value except for maps.
```pil
error FORMAT-STRING, ARGS...
```

### exit
Unconditionally exits the program with exit code `CODE`. An erroneous code is any code except for 0. `CODE` - number.
```pil
exit CODE
```

### stack-depth
Stores the depth of the stack in `DESTINATION`. `DESTINATION` - container.
```pil
stack-depth DESTINATION
```

### stack-name
Allocates and stores the name of the calee's function in `DESTINATION`. `DESTINATION` - container.
```pil
stack-name DESTINATION
```

### stack-line
Stores the line of calee's function in `DESTINATION`. `DESTINATION` - container.
```pil
stack-line DESTINATION
```

### stack-file
Allocates and stores the name of the file of the calee's function in `DESTINATION`. `DESTINATION` - container.
```pil
stack-file DESTINATION
```

### stack-trace
Dumps the stack trace and exits the program.
```pil
stack-trace
```

## Type utility
### typeof
Allocates and stores the name of the type of `VALUE` in `DESTINATION`. Integer - `int`, float - `float`, character - `char`, constant and dynamic strings - `string`, array - `array`, map - `map`, function - `function`, label - `label`, null - `null`. `VALUE` - any value. `DESTINATION` - container.
```pil
typeof VALUE, DESTINATION
```

### is-num
Stores 1 in `DESTINATION` if `VALUE` is a number, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-num VALUE, DESTINATION
```

### is-float
Stores 1 in `DESTINATION` if `VALUE` is a float, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-float VALUE, DESTINATION
```

### is-int
Stores 1 in `DESTINATION` if `VALUE` is an integer, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-int VALUE, DESTINATION
```

### is-char
Stores 1 in `DESTINATION` if `VALUE` is a character, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-char VALUE, DESTINATION
```

### is-string
Stores 1 in `DESTINATION` if `VALUE` is a constant or dynamic string, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-string VALUE, DESTINATION
```

### is-array
Stores 1 in `DESTINATION` if `VALUE` is an array, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-array VALUE, DESTINATION
```

### is-reg
Stores 1 in `DESTINATION` if `VALUE` is a container, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-reg VALUE, DESTINATION
```

### is-function
Stores 1 in `DESTINATION` if `VALUE` is a function, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-function VALUE, DESTINATION
```

### is-label
Stores 1 in `DESTINATION` if `VALUE` is a label, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-label VALUE, DESTINATION
```

### is-null
Stores 1 in `DESTINATION` if `VALUE` is null, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-null VALUE, DESTINATION
```

### is-inf
Stores 1 in `DESTINATION` if `VALUE` is a float and infinite, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-inf VALUE, DESTINATION
```

### is-nan
Stores 1 in `DESTINATION` if `VALUE` is a float and NaN, otherwise 0. `VALUE` - any value, `DESTINATION` - container.
```pil
is-nan VALUE, DESTINATION
```

### to-int
Converts `VALUE` to an integer and stores it in `DESTINATION`. If `VALUE` is a string and it isn't a valid number or is out of bounds, store null instead. `VALUE` - number, character or constant or dynamic string, `DESTINATION` - container.
```pil
to-int VALUE, DESTINATION
```

### to-float
Converts `VALUE` to a float and stores it in `DESTINATION`. If `VALUE` is a string and it isn't a valid number or is out of bounds, store null instead. `VALUE` - number, character or constant or dynamic string, `DESTINATION` - container.
```pil
to-float VALUE, DESTINATION
```

### to-char
Converts `VALUE` to a character and stores it in `DESTINATION`. `VALUE` - number or character. `DESTINATION` - container.
```pil
to-char VALUE, DESTINATION
```

## Time
### time
Stores the elapsed time in milliseconds since the first [time](#time) call in `DESTINATION`. `DESTINATION` - container.
```pil
time DESTINATION
```

### unix-time
Stores seconds since epoch in `DESTINATION`. `DESTINATION` - container.
```pil
unix-time DESTINATION
```

### date
Formats and allocates a date based on `FORMAT-STRING`. All format options are available [here](https://en.cppreference.com/cpp/io/manip/put_time). All of them are available and are prefixed with `%`. `FORMAT-STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
date FORMAT-STRING, DESTINATION
```

### sleep
Sleep for `SECONDS` seconds. `SECONDS` - number.
```pil
sleep SECONDS
```

## Common utility
### swap
Swap both values in the given containers. `A` - container, `B` - container.
```pil
swap A, B
```

### set
Store `VALUE` in `DESTINATION`. `VALUE` - any value, `DESTINATION` - container.
```pil
set VALUE, DESTINATION
```

### val-table
Checks `VALUE` against all `TARGET`s and if there is a match, store the value after the `TARGET` in `DESTINATION`. Otherwise if there is an odd number of arguments, store `DEFAULT?`, else null. Each `TARGET` must have a `RESULT` after it. `VALUE` - any value except for map, `DESTINATION` - container, `TARGET...` - any value except for map, `RESULT...` - any value, `DEFAULT?` - optional value.
```pil
val-table VALUE, DESTINATION, TARGET, RESULT, ..., DEFAULT?
```

### table-contains
Checks whether `VALUE` matches any of the values and stores 1 in `DESTINATION` if it does, otherwise 0. `VALUE` - any value except for map, `DESTINATION` - container, `TARGET...` - any value except for map.
```pil
table-contains VALUE, DESTINATION, TARGET...
```

### variadic-size
Stores the current function's variadic argument count in `DESTINATION`. `DESTINATION` - container.
```pil
variadic-size DESTINATION
```

### variadic-at
Get the variadic argument at position `ID` and store it in `DESTINATION`. Throws if `ID` is out of bounds (`ID` < 0 || `ID` >= variadic count). `ID` - unsigned integer, `DESTINATION` - container.
```pil
variadic-at ID, DESTINATION
```

### reg-size
Stores the total number of registers in `DESTINATION`. `DESTINATION` - container.
```pil
reg-size DESTINATION
```

### reg-at
Get the value of the register at position `ID` and store it in `DESTINATION`. Throws if `ID` is out of bounds. `ID` - unsigned integer, `DESTINATION` - container.
```pil
reg-at ID, DESTINATION
```

### reg-set
Set the register at position `ID` to `VALUE`. Throws if `ID` is out of bounds. `ID` - unsigned integer, `VALUE` - any value.
```pil
reg-set ID, VALUE
```

### return-reg-size
Stores the total number of return registers in `DESTINATION`. `DESTINATION` - container.
```pil
return-reg-size DESTINATION
```

### return-reg-at
Get the value of the return register at position `ID` and store it in `DESTINATION`. Throws if `ID` is out of bounds. `ID` - unsigned integer, `DESTINATION` - container.
```pil
return-reg-at ID, DESTINATION
```

### return-reg-set
Set the return register at position `ID` to `VALUE`. Throws if `ID` is out of bounds. `ID` - unsigned integer, `VALUE` - any value.
```pil
return-reg-set ID, VALUE
```

### return-count
Stores the number of values returned by the last function call in `DESTINATION`. `DESTINATION` - container.
```pil
return-count DESTINATION
```

### func-arity
Stores the parameter count of `FUNCTION` in `DESTINATION`. `FUNCTION` - function, `DESTINATION` - container.
```pil
func-arity FUNCTION, DESTINATION
```

### func-variadic
Stores 1 in `DESTINATION` if `FUNCTION` is variadic, otherwise 0. `FUNCTION` - function, `DESTINATION` - container.
```pil
func-variadic FUNCTION, DESTINATION
```

### func-arg-match
Checks whether `ARGS` would be a valid argument count for `FUNCTION` and stores 1 in `DESTINATION` if so, otherwise 0. `FUNCTION` - function, `ARGS` - unsigned integer, `DESTINATION` - container.
```pil
func-arg-match FUNCTION, ARGS, DESTINATION
```
