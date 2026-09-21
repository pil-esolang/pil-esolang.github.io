# Control Flow
While PIL has no control flow statements, they can be achieved with the comparison and jump built-ins. This page will contain snippets instead of ready-to-run code.

## If statement
A single if statement can be modeled as follows:
```pil
   jmp CONDITION, LABEL-IF-TRUE
   ; code if false...
   goto LABEL-IF-END
LABEL-IF-TRUE:
   ; code if true...
LABEL-IF-END:
```

## If-else statement
Multiple if statements can be chained as such:
```pil
   jmp CONDITION1, LABEL-IF-TRUE1
   jmp CONDITION2, LABEL-IF-TRUE2
   jmp CONDITION3, LABEL-IF-TRUE3
   ; and so on...
   ; code if none are true (else)...
   goto LABEL-IF-END
LABEL-IF-TRUE1:
   ; code if CONDITION1 is true...
   goto LABEL-IF-END
LABEL-IF-TRUE2:
   ; code if CONDITION2 is true...
   goto LABEL-IF-END
LABEL-IF-TRUE3:
   ; code if CONDITION3 is true...
   goto LABEL-IF-END ; for consistency
LABEL-IF-END:
```

## Switch statement
Now, you can model a switch statement just the same way as the if-else statement or use the `jmptable` built-in. The `LABEL-NONE` label is optional and is jumped to if `VALUE` does not equal any other value.
```pil
   jmptable VALUE, VALUE1, LABEL1, VALUE2, LABEL2, VALUE3, LABEL3, LABEL-NONE ; add more if needed
LABEL1:
   ; code if VALUE == VALUE1...
   goto LABEL-END
LABEL2:
   ; code if VALUE == VALUE2...
   goto LABEL-END
LABEL3:
   ; code if VALUE == VALUE3...
   goto LABEL-END
LABEL-NONE:
   ; code if value doesn't equal anything...
   goto LABEL-END
LABEL-END:
```

## While loop
While loop is the simplest loop you can model in PIL and it is done as follows:
```pil
   jmpn CONDITION, WHILE-END
WHILE-START:
   ; your code here...
   jmp CONDITION, WHILE-START
WHILE-END:
```

## For loop
For loop is written as such:
```pil
   jmpn CONDITION, FOR-END
FOR-START:
   ; your code here...
   incr I ; or decr if reversed
   ; your condition here, usually it's 'le I, N, CONDITION'. Use the same condition outside of the loop
   jmp CONDITION, FOR-START
FOR-END:
```
And written out it looks something like this:
```pil
for-loop(i, n) let condition
   le i, n, condition
   jmpn condition, for-loop-end
for-loop-start:
   println i
   incr i
   le i, n, condition
   jmp condition, for-loop-start
for-loop-end:
```

## Built-ins
That should be enough to get you started. `jmp` jumps to the label if the condition is true, `jmpn` jumps if it is false and `goto` jumps unconditionally.

There are 6 comparison built-ins: `le a, b, result` - is a lesser than b, `gr a, b, result` - is a greater than b, `leeq a, b, result` - is a lesser than or equal to b, `greq a, b, result` - is a greater than or equal to b, `eq a, b, result` - are a and b equal and `neq a, b, result` - are a and b inequal.

And there are 3 boolean built-ins: `and a, b, ..., result` - return true if all values are true, false otherwise, `or a, b, ..., result` - return true if at least a single value is true, false otherwise, and `not a, result` - flip truthiness of a.

That's everything you need to know about conditions and control flow in PIL to get you started.
