# Math Library
## Number types
There are two types of numbers - integers and floats. Integers' underlying C++ type is int64_t/uint64_t, whereas floats' type is double. Both on 64bit systems are 8B.

## Math Library
### incr
Increment the value stored in `NUMBER`. `NUMBER` - container containing a number.
```pil
incr NUMBER
```

### decr
Decrement the value stored in `NUMBER`. `NUMBER` - container containing a number.
```pil
decr NUMBER
```

### sum
Add all numbers together and store in `RESULT`. Returns float if at least a single value is a float. `N1...` - number, `RESULT` - container.
```pil
sum N1, N2, ..., RESULT
```

### add
Add `N1` and `N2` together and store in `RESULT`. Returns float if either number is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
add N1, N2, RESULT
```

### sub
Subtract `N1` by `N2` and store in `RESULT`. Returns float if either number is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
sub N1, N2, RESULT
```

### mul
Multiply `N1` and `N2` together and store in `RESULT`. Returns float if either number is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
mul N1, N2, RESULT
```

### div
Divide `N1` by `N2` and store in `RESULT`. Returns float if either number is a float. Returns 0 on division by zero. `N1` - number, `N2` - number, `RESULT` - container.
```pil
div N1, N2, RESULT
```

### mod
Get the remainder of dividing `N1` by `N2` and store in `RESULT`. Supports floats and negative numbers. Returns float if either number is a float. Returns 0 on division by zero. `N1` - number, `N2` - number, `RESULT` - container.
```pil
mod N1, N2, RESULT
```

### floor-mod
Get the remainder of dividing `N1` by `N2`, using the formula `((N1 % N2) + N2) % N2`, and store in `RESULT`. Supports floats and negative numbers. Returns float if either number is a float. Returns 0 on division by zero. `N1` - number, `N2` - number, `RESULT` - container.

### pow
Exponentiate `N1` to the exponent `N2`. Returns float if either number is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
pow N1, N2, RESULT
```

### neg
Negate `N` and store in `RESULT`. `N` - number, `RESULT` - container.
```pil
neg N, RESULT
```

### sqrt
Get the square root of `N` and store in `RESULT`. Returns float. Returns NAN if `N` is negative. `N` - number, `RESULT` - container.
```pil
sqrt N, RESULT
```

### cbrt
Get the cube root of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
cbrt N, RESULT
```

### sin
Get the sine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
sin N, RESULT
```

### cos
Get the cosine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
cos N, RESULT
```

### tan
Get the tangent of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
tan N, RESULT
```

### asin
Get the arcsine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
asin N, RESULT
```

### acos
Get the arccosine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
acos N, RESULT
```

### atan
Get the arctangent of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
atan N, RESULT
```

### atan2
Get the arctangent of `Y / X` using the signs of arguments to determine the correct quadrant and store in `RESULT`. Returns float. `Y` - number, `X` - number, `RESULT` - container.
```pil
atan2 Y, X, RESULT
```

### asinh
Get the inverse hyperbolic sine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
asinh N, RESULT
```

### acosh
Get the inverse hyperbolic cosine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
acosh N, RESULT
```

### atanh
Get the inverse hyperbolic tangent of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
atanh N, RESULT
```

### sinh
Get the hyperbolic sine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
sinh N, RESULT
```

### cosh
Get the hyperbolic cosine of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
cosh N, RESULT
```

### tanh
Get the hyperbolic tangent of `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
tanh N, RESULT
```

### abs
Get the absolute value of `N` and store in `RESULT`. `N` - number, `RESULT` - container.
```pil
abs N, RESULT
```

### min
Get the minimum value of `N1` and `N2` and store in `RESULT`. Returns float if either value is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
min N1, N2, RESULT
```

### max
Get the maximum value of `N1` and `N2` and store in `RESULT`. Returns float if either value is a float. `N1` - number, `N2` - number, `RESULT` - container.
```pil
max N1, N2, RESULT
```

### clamp
Clamp `X` to range [`LO`; `HI`] and store in `RESULT`. Returns float if any value is a float. Throws if `LO` > `HI`. `X` - number, `LO` - number, `HI` - number, `RESULT` - container.
```pil
clamp X, LO, HI, RESULT
```

### sign
Get the sign of `N` and store in `RESULT`. Returns integer. `N` - number, `RESULT` - container.
```pil
sign N, RESULT
```

### trunc
Truncate float `N` and store in `RESULT`. Returns float. `N` - number, `RESULT` - container.
```pil
trunc N, RESULT
```

### ceil
Round float `N` to the smallest integer not less than `N`. Returns float. `N` - number, `RESULT` - container.
```pil
ceil N, RESULT
```

### floor
Round float `N` to the largest integer not greater than `N`. Returns float. `N` - number, `RESULT` - container.
```pil
floor N, RESULT
```

### round
Round float `N` to the nearest integer. Returns float. `N` - number, `RESULT` - container.
```pil
round N, RESULT
```

### exp
Computes Euler's number raised to the power `N`. Returns float. `N` - number, `RESULT` - container.
```pil
exp N, RESULT
```

### ln
Computes the natural (base e) logarithm of `N`. Returns float. `N` - number, `RESULT` - container.
```pil
ln N, RESULT
```

### log
Computes the base `B` logarithm of `N`, using formula `ln(N) / ln(B)`. Returns float. `N` - number, `B` - number, `RESULT` - container.
```pil
log N, B, RESULT
```

### log2
Computes the base 2 logarithm of `N`. Returns float. `N` - number, `RESULT` - container.
```pil
log2 N, RESULT
```

### log10
Computes the base 10 logarithm of `N`. Returns float. `N` - number, `RESULT` - container.
```pil
log10 N, RESULT
```

### lerp
Linearly interpolate `A` to `B` based on `T`. Returns float. `A` - number, `B` - number, `T` - number, `RESULT` - container.
```pil
lerp A, B, T, RESULT
```

### step-towards
Step towards `TARGET` by 1 until it is reached. Returns float if either value is a float. `N` - number, `TARGET` - number, `RESULT` - container.
```pil
step-towards N, TARGET, RESULT
```

### seed-random
Seed the global RNG used in all random operations, like `random`, `randf-range`, `randi-range` and `array-shuffle`. `SEED` - unsigned integer.
```pil
seed-random SEED
```

### random
Get a random float in range [0; 1) based on global RNG and store in `RESULT`. `RESULT` - container.
```pil
random RESULT
```

### randf-range
Get a random float in range [`MIN`; `MAX`) based on global RNG and store in `RESULT`. Throws if `MIN` > `MAX`. `MIN` - number, `MAX` - number, `RESULT` - result.
```pil
randf-range MIN, MAX, RESULT
```

### randi-range
Get a random integer in range [`MIN`; `MAX`] based on global RNG and store in `RESULT`. Throws if `MIN` > `MAX`. `MIN` - number, `MAX` - number, `RESULT` - result.
```pil
randi-range MIN, MAX, RESULT
```

### gcd
Get the greatest common divisor of `N1` and `N2` and store in `RESULT`. `N1` - number, `N2` - number, `RESULT` - container.
```pil
gcd N1, N2, RESULT
```

### lcm
Get the least common multiple of `N1` and `N2` and store in `RESULT`. `N1` - number, `N2` - number, `RESULT` - container.
```pil
lcm N1, N2, RESULT
```

### hypot
Calculate &radic;<s style="text-decoration:overline">x<sup>2</sup>+y<sup>2</sup></s> and store in `RESULT`. `X` - number, `Y` - number, `RESULT` - container.
```pil
hypot X, Y, RESULT
```

### hypot3
Calculate &radic;<s style="text-decoration:overline">x<sup>2</sup>+y<sup>2</sup>+z<sup>2</sup></s> and store in `RESULT`. `X` - number, `Y` - number, `Z` - number, `RESULT` - container.
```pil
hypot X, Y, Z, RESULT
```

### bit-and
Perform bitwise and operation on `N1` and `N2` and store in `RESULT`. `N1` - unsigned integer, `N2` - unsigned integer, `RESULT` - container.
```pil
bit-and N1, N2, RESULT
```

### bit-or
Perform bitwise or operation on `N1` and `N2` and store in `RESULT`. `N1` - unsigned integer, `N2` - unsigned integer, `RESULT` - container.
```pil
bit-or N1, N2, RESULT
```

### bit-xor
Perform bitwise inclusive or operation on `N1` and `N2` and store in `RESULT`. `N1` - unsigned integer, `N2` - unsigned integer, `RESULT` - container.
```pil
bit-xor N1, N2, RESULT
```

### bit-not
Perform bitwise not operation on `N1` and store in `RESULT`. `N1` - unsigned integer, `RESULT` - container.
```pil
bit-not N1, RESULT
```

### bit-shl
Perform bitwise shift left operation on `N1` and `N2` and store in `RESULT`. Throws if `N2` >= 64. `N1` - unsigned integer, `N2` - unsigned integer, `RESULT` - container.
```pil
bit-shl N1, N2, RESULT
```

### bit-shr
Perform bitwise shift right operation on `N1` and `N2` and store in `RESULT`. Throws if `N2` >= 64. `N1` - unsigned integer, `N2` - unsigned integer, `RESULT` - container.
```pil
bit-shr N1, N2, RESULT
```

### bit-count
Return the count of set bits in `N` and store in `RESULT`. `N` - unsigned integer, `RESULT` - container.
```pil
bit-count N, RESULT
```

### bit-test
Test the bit in `A` at position `N` and store it in `RESULT`. Throws if `N` >= 64. `A` - unsigned integer, `N` - unsigned integer, `RESULT` - container.
```pil
bit-test A, N, RESULT
```

### bit-set
Set the bit in `A` at position `N` and store the result in `RESULT`. Throws if `N` >= 64. `A` - unsigned integer, `N` - unsigned integer, `RESULT` - container.
```pil
bit-set A, N, RESULT
```

### bit-clear
Clear the bit in `A` at position `N` and store the result in `RESULT`. Throws if `N` >= 64. `A` - unsigned integer, `N` - unsigned integer, `RESULT` - container.
```pil
bit-clear A, N, RESULT
```

### bit-toggle
Toggle the bit in `A` at position `N` and store the result in `RESULT`. Throws if `N` >= 64. `A` - unsigned integer, `N` - unsigned integer, `RESULT` - container.
```pil
bit-toggle A, N, RESULT
```
