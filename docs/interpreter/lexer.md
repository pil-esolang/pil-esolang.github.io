# Lexer
## Introduction
The lexer is responsible for turning code into tokens. You can also view it as turning sentences into words for easier parsing. It is also responsible for checking if the tokens are correctly formed.

## Tokens
In PIL there are 41 different tokens, each having its own meaning. They all have the file and the line tied to them for better error handling:

<table>
   <thead><tr>
      <th>Name</th>
      <th>Example</th>
      <th>Description</th>
   </tr></thead>
   <tbody>
      <tr><td>Return Register</td><td>r$ or R$</td><td>Return register access syntax for parse-time</td></tr>
      <tr><td>Register</td><td>$</td><td>Register access syntax for parse-time</td></tr>
      <tr><td>Left Parentheses</td><td>(</td><td>Used in function declarations and math evaluator and some directives for operator precedence</td></tr>
      <tr><td>Right Parentheses</td><td>)</td><td>Used to close left parentheses</td></tr>
      <tr><td>Three Dots</td><td>...</td><td>Used to denote variadic parameters in function declaration</td></tr>
      <tr><td>Colon</td><td>:</td><td>Used to define a label</td></tr>
      <tr><td>Left Bracket</td><td>[</td><td>Used to denote math evaluator start</td></tr>
      <tr><td>Right Bracket</td><td>]</td><td>Used to terminate math evaluator</td></tr>
      <tr><td>Add</td><td>+</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Subtract</td><td>-</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Multiply</td><td>*</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Divide</td><td>/</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Modulus</td><td>%</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Logical Or</td><td>||</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Logical And</td><td>&&</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Logical Not</td><td>!</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Binary Or</td><td>|</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Binary Xor</td><td>^</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Binary And</td><td>&</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Binary Not</td><td>~</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Equal</td><td>==</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Inequal</td><td>!=</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Lesser</td><td>&lt;</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Lesser Equal</td><td>&gt;=</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Greater</td><td>&gt;</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Greater Equal</td><td>&gt;=</td><td>Used as an operator in the math evaluator and some directives</td></tr>
      <tr><td>Bit Shift Left</td><td>&lt;&lt;</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Bit Shift Right</td><td>&gt;&gt;</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Exponentiate</td><td>**</td><td>Used as an operator in the math evaluator</td></tr>
      <tr><td>Directive</td><td>@[a-zA-Z0-9_-]* or @MY-IDENTIFIER123</td><td>Used to denote a directive for the translator phase</td></tr>
      <tr><td>Identifier</td><td>[a-zA-Z_][a-zA-Z0-9_-]* or MY-IDENTIFIER123</td><td>Used to name a variable or a function</td></tr>
      <tr><td>Integer</td><td>[0-9]+ or 123</td><td>Used to create an integer</td></tr>
      <tr><td>Floating</td><td>[0-9]+\.[0-9] or 123.456</td><td>Used to create a float</td></tr>
      <tr><td>String</td><td>"*"</td><td>Used to create a string. See [String rules](#string-rules)</td></tr>
      <tr><td>Character</td><td>'.'</td><td>Used to create a character. See [String rules](#string-rules)</td></tr>
      <tr><td>Format Start</td><td>${</td><td>Used in constant formatting. See [String rules](#string-rules)</td></tr>
      <tr><td>Format End</td><td>}</td><td>Used to end constant formatting. See [String rules](#string-rules)</td></tr>
      <tr><td>Eval Start</td><td>$[</td><td>Used in constant formatting. See [String rules](#string-rules)</td></tr>
      <tr><td>Eval End</td><td>]</td><td>Used to end constant formatting. See [String rules](#string-rules)</td></tr>
      <tr><td>Newline</td><td></td><td>Used to separate function calls</td></tr>
      <tr><td>EOF</td><td></td><td>Used to denote the end of tokens</td></tr>
   </tbody>
</table>

## String rules
Strings and characters support the following escape codes: `\a`, `\b`, `\t`, `\n`, `\v`, `\f`, `\r`, `\e`, `\\`, `\'`, `\"`, `\{`, `\}`, `\$`.

Strings and characters terminate on a newline, so multi-line strings are not possible.

Strings support constant formatting. Lexer emits formatting and evaluation tokens on found `${` and `$[`, that get later handled in the parser.
