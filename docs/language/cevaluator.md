# Constant evaluator
Constant evaluator is a parse-time feature that can calculate constant math, such as memory sizes, constants and very commonly negative numbers.

## Usage
Everything between brackets `[]` is evaluated in the constant evaluator and changed to the result in the code. It follows a different, more familiar syntax:
```pil
main()
   println [2 + 4 * 3], ' ', [sin(pi() / 3)], ' ', [sqrt(2)];
```
During runtime, the code looks like this:
```pil
println 14, ' ', 0.866, ' ', 1.414;
```

## Operators
Operators are roughly sorted so the operator with the least precedence is first and the operator with most is last. Unary operators cannot be chained. All operators except for exponentiation parse left-to-right.

<table>
   <thead><tr>
      <th>Operator</th>
      <th>Example</th>
      <th>Description</th>
   </tr></thead>
   <tbody>
      <tr><td>||</td><td>1 || 0</td><td>Logical or</td></tr>
      <tr><td>&&</td><td>1 && 0</td><td>Logical and</td></tr>
      <tr><td>==</td><td>1 == 0</td><td>Equals</td></tr>
      <tr><td>!=</td><td>1 != 0</td><td>Inequals</td></tr>
      <tr><td>&lt;</td><td>1 &lt; 0</td><td>Less than</td></tr>
      <tr><td>&gt;</td><td>1 &gt; 0</td><td>Greater than</td></tr>
      <tr><td>&lt;=</td><td>1 &lt;= 0</td><td>Less than or equal to</td></tr>
      <tr><td>&gt;=</td><td>1 &gt;= 0</td><td>Greater than or equal to</td></tr>
      <tr><td>|</td><td>1 | 0</td><td>Bitwise or. Operates on unsigned integers</td></tr>
      <tr><td>^</td><td>1 ^ 0</td><td>Bitwise inclusive or. Operates on unsigned integers</td></tr>
      <tr><td>&</td><td>1 & 0</td><td>Bitwise and. Operates on unsigned integers</td></tr>
      <tr><td>&lt;&lt;</td><td>1 &lt;&lt; 0</td><td>Bitwise shift left. Operates on unsigned integers</td></tr>
      <tr><td>&gt;&gt;</td><td>1 &gt;&gt; 0</td><td>Bitwise shift right. Operates on unsigned integers</td></tr>
      <tr><td>+</td><td>10 + 3</td><td>Addition</td></tr>
      <tr><td>-</td><td>10 - 3</td><td>Subtraction</td></tr>
      <tr><td>*</td><td>10 * 3</td><td>Multiplication</td></tr>
      <tr><td>/</td><td>10 / 3</td><td>Division</td></tr>
      <tr><td>%</td><td>10 % 3</td><td>Modulus</td></tr>
      <tr><td>**</td><td>10 ** 3</td><td>Exponentiation</td></tr>
      <tr><td>-</td><td>-1</td><td>Unary minus</td></tr>
      <tr><td>+</td><td>+1</td><td>Unary plus (no op)</td></tr>
      <tr><td>~</td><td>~1</td><td>Bitwise not. Operates on unsigned integers</td></tr>
      <tr><td>!</td><td>!1</td><td>Logical not</td></tr>
      <tr><td>func()</td><td>pi()</td><td>Function calls</td></tr>
      <tr><td>()</td><td>2 * (1 + 3)</td><td>Parentheses. Most precedence</td></tr>
   </tbody>
</table>

## Functions
There's a plethora of built-in functions. Here is the full table:

<table>
   <thead><tr>
      <th>Function</th>
      <th>Args</th>
      <th>Description</th>
   </tr></thead>
   <tbody>
      <tr><td>abs</td><td>1</td><td>Get the absolute value</td></tr>
      <tr><td>min</td><td>2</td><td>Get the minimum value of the two</td></tr>
      <tr><td>max</td><td>2</td><td>Get the maximum value of the two</td></tr>
      <tr><td>sqrt</td><td>1</td><td>Square root</td></tr>
      <tr><td>cbrt</td><td>1</td><td>Cube root</td></tr>
      <tr><td>sin</td><td>1</td><td>Sine</td></tr>
      <tr><td>cos</td><td>1</td><td>Cosine</td></tr>
      <tr><td>tan</td><td>1</td><td>Tangent</td></tr>
      <tr><td>asin</td><td>1</td><td>Arcsine</td></tr>
      <tr><td>acos</td><td>1</td><td>Arccosine</td></tr>
      <tr><td>atan</td><td>1</td><td>Arctangent</td></tr>
      <tr><td>atan2</td><td>1 - Y, X</td><td>Arctangent of Y / X using signs of argments to determine the correct quadrant</td></tr>
      <tr><td>asinh</td><td>1</td><td>Hyperbolic arcsine</td></tr>
      <tr><td>acosh</td><td>1</td><td>Hyperbolic arccosine</td></tr>
      <tr><td>atanh</td><td>1</td><td>Hyperbolic arctangent</td></tr>
      <tr><td>sinh</td><td>1</td><td>Hyperbolic sine</td></tr>
      <tr><td>cosh</td><td>1</td><td>Hyperbolic cosine</td></tr>
      <tr><td>tanh</td><td>1</td><td>Hyperbolic tangent</td></tr>
      <tr><td>clamp</td><td>3 - X, LO, HI</td><td>Clamp X in range [LO; HI]</td></tr>
      <tr><td>sign</td><td>1</td><td>Get the sign</td></tr>
      <tr><td>trunc</td><td>1</td><td>Truncate float</td></tr>
      <tr><td>ceil</td><td>1</td><td>Round to smallest integer not less than N</td></tr>
      <tr><td>floor</td><td>1</td><td>Round to largest integer not greater than N</td></tr>
      <tr><td>round</td><td>1</td><td>Round float to nearest integer</td></tr>
      <tr><td>exp</td><td>1</td><td>Euler's number raised to power N</td></tr>
      <tr><td>ln</td><td>1</td><td>Natural (base e) logarithm</td></tr>
      <tr><td>log</td><td>2 - N, B</td><td>Base B logarithm of N using formula ln(N) / ln(B)</td></tr>
      <tr><td>log2</td><td>1</td><td>Base 2 logarithm</td></tr>
      <tr><td>log10</td><td>1</td><td>Base 10 logarithm</td></tr>
      <tr><td>lerp</td><td>3 - A, B, T</td><td>Linearly interpolate A to B based on T [0; 1]</td></tr>
      <tr><td>if</td><td>3 - COND, YES, NO</td><td>Returns YES if COND is truthy, otherwise NO. Computes both YES and NO regardless of COND</td></tr>
      <tr><td>pi</td><td>0</td><td>3.141592653589793</td></tr>
      <tr><td>tau</td><td>0</td><td>6.283185307179586</td></tr>
      <tr><td>e</td><td>0</td><td>2.718281828459045</td></tr>
      <tr><td>hypot</td><td>2 - X, Y</td><td>Calculate &radic;<s style="text-decoration:overline">x<sup>2</sup>+y<sup>2</sup></s></td></tr>
      <tr><td>hypot3</td><td>3 - X, Y, Z</td><td>Calculate &radic;<s style="text-decoration:overline">x<sup>2</sup>+y<sup>2</sup>+z<sup>2</sup></s></td></tr>
      <tr><td>gcd</td><td>2</td><td>Greated common divisor</td></tr>
      <tr><td>lcm</td><td>2</td><td>Least common multiple</td></tr>
   </tbody>
</table>
