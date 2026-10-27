# Interpreter
Interpreter usage:
```bash
pil [FLAGS...] [COMMAND] [ARGS...]
```

## Commands
### run
```bash
pil [FLAGS...] run [FILE/EXECUTABLE]
```
Run the file/executable. Supported files are `.pil` and `.pilo`.

### compile
```bash
pil [FLAGS...] compile [FILE] [OUTPUT]
```
Compile the file into cached bytecode. The file's extension must be `.pil` and the output's extension must be `.pilo`. The cached bytecode doesn't serve as a portable executable, rather it can save time if rerunning the same program multiple times.

## Flags
Flags must be passed before the command. Here's the full list of them.

### --debug-code
Output all bytecode after parsing. Output for this program:
```pil
my-add(x, y)
   add x, y, $0;
   return $0;

main()
   println "Hello, World!";
```
Should look something like this:
```bash
Bytecode:
test.pil:2     add: Local Variable, Local Variable, Register, 
test.pil:3     return: Register, 
test.pil:6     println: Constant String, 
test.pil:6     return: 
```
Since functions and labels are translated to positions, they won't show up here.

### --debug-tokens
Output all tokens after lexing. Output for this program:
```pil
my-add(x, y)
   add x, y, $0;
   return $0;

main()
   println "Hello, World!";
```
Should look something like this:
```bash
Tokens:
test.pil:1     Identifier: 'my-add'.
test.pil:1     Left Parentheses: ''.
test.pil:1     Identifier: 'x'.
test.pil:1     Comma: ''.
test.pil:1     Identifier: 'y'.
test.pil:1     Right Parentheses: ''.
test.pil:2     Identifier: 'add'.
test.pil:2     Identifier: 'x'.
test.pil:2     Comma: ''.
test.pil:2     Identifier: 'y'.
test.pil:2     Comma: ''.
test.pil:2     Register: ''.
test.pil:2     Integer: '0'.
test.pil:2     Semicolon: ''.
test.pil:3     Identifier: 'return'.
test.pil:3     Register: ''.
test.pil:3     Integer: '0'.
test.pil:3     Semicolon: ''.
test.pil:5     Identifier: 'main'.
test.pil:5     Left Parentheses: ''.
test.pil:5     Right Parentheses: ''.
test.pil:6     Identifier: 'println'.
test.pil:6     String: 'Hello, World!'.
test.pil:6     Semicolon: ''.
test.pil:6     EOF: 'EOF'.
```

### --time
Show time of each compiler's operation and the runtime (if present). Example:
```bash
$ pil --time compile test.pil test.pilo
Writing to 'test.pilo'...
Wrote 882B to 'test.pilo'.

Compilation time:
File Read: 0.076ms.
Lexer: 0.014ms.
Parser: 0.046ms.
Writing: 0.228ms.
```
```bash
$ pil --time run test.pilo
Hello, World!

Execution time:
File Read: 0.094ms.
Runtime: 0.051ms.
```

### --allow-fileio
Allow file I/O built-ins that modify, access or view the disk in any capacity. Doing so can put your computer at risk, review the code before executing.

### --allow-env
Allow OS environment variable built-ins. Doing so can reveal any API keys and secrets, review the code before executing.

### --allow-exec
Allow [os-exec](../built-ins/fileos.md#os-exec) built-in. Doing so puts your computer at a massive risk - the program can execute any command. Refrain from giving it elevated privileges. Review the code before executing.

### --silence-leaks
Silence all memory leaks.
