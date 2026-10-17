# File & OS library
It is recommended to read [Language/Values](../language/values.md) first for a better understanding of allowed parameter types, value semantics and behavior.

Most of these built-ins require special permissions that can be passed to the interpreter as flags. Without them, the program won't run. This is in place to prevent accidental malicious code execution.

## file-open
Try to open `PATH` in mode `MODE` and store the file handle in `DESTINATION` on success or null value on failure. Mode `R` - read only, `W` - write only, `A` - write only (append), `X` - read and write. Throws on unknown mode. `PATH` - string, `MODE` - character, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-open PATH, MODE, DESTINATION
```

## file-close
Close file `FILE` and set the handle to null. `FILE` - file handle.

Must have file I/O permissions.
```pil
file-close FILE
```

## file-read
Read the whole contents of `FILE`, allocate it and store in `DESTINATION`. `FILE` - file handle, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-read FILE, DESTINATION
```

## file-readln
Read a line from `FILE`, allocate it and store in `DESTINATION`. `FILE` - file handle, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-readln FILE, DESTINATION
```

## file-readch
Read a single character from `FILE` and store in `DESTINATION`. `FILE` - file handle, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-readch FILE, DESTINATION
```

## file-read-bytes
Read `N` bytes from `FILE`, allocate them and store as a dynamic string in `DESTINATION`. `FILE` - file handle, `N` - unsigned integer, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-read-bytes FILE, N, DESTINATION
```

## file-eof
Store 1 in `DESTINATION` if EOF is found, else 0. `FILE` - file handle, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-eof FILE, DESTINATION
```

## file-write
Write stringified `DATA` to `FILE`. `FILE` - file handle, `DATA` - stringifyable value.

Must have file I/O permissions.
```pil
file-write FILE, DATA
```

## file-writeln
Write stringified `DATA` to `FILE` and append a newline. `FILE` - file handle, `DATA` - stringifyable value.

Must have file I/O permissions.
```pil
file-writeln FILE, DATA
```

## file-flush
Flush the output to `FILE`. `FILE` - file handle.

Must have file I/O permissions.
```pil
file-flush FILE
```

## file-tell
Store the current position in `FILE` (in bytes from the start of the file) in `DESTINATION`. Throws if the stream is in a failed state. `FILE` - file handle, `DESTINATION` - container.

Must have file I/O permissions.
```pil
file-tell FILE, DESTINATION
```

## file-seek
Move the position in `FILE` to `POS` bytes from the start of the file. Clears any EOF or error state on the stream. `FILE` - file handle, `POS` - unsigned integer.

Must have file I/O permissions.
```pil
file-seek FILE, POS
```

## file-seek-rel
Move the position in `FILE` by `OFFSET` bytes relative to the current position. A negative `OFFSET` moves backwards. Clears any EOF or error state on the stream. `FILE` - file handle, `OFFSET` - integer.

Must have file I/O permissions.
```pil
file-seek-rel FILE, OFFSET
```

## file-seek-end
Move the position in `FILE` by `OFFSET` bytes relative to the end of the file. Clears any EOF or error state on the stream. `FILE` - file handle, `OFFSET` - integer.

Must have file I/O permissions.
```pil
file-seek-end FILE, OFFSET
```

## path-exists
Stores 1 in `DESTINATION` if `PATH` exists, otherwise 0. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
path-exists PATH, DESTINATION
```

## path-is-file
Stores 1 in `DESTINATION` if `PATH` exists and is a regular file, otherwise 0. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
path-is-file PATH, DESTINATION
```

## path-is-dir
Stores 1 in `DESTINATION` if `PATH` exists and is a directory, otherwise 0. `PATH` - string, `DESTINATION` - contaienr.

Must have file I/O permissions.
```pil
path-is-dir PATH, DESTINATION
```

## path-size
Stores the size `PATH` in `DESTINATION`. Stores null if `PATH` is a directory. Can throw. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
path-size PATH, DESTINATION
```

## path-modified-time
Stores the last modified time of `PATH` in `DESTINATION`. Can throw. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
path-modified-time PATH, DESTINATION
```

## path-create-dir
Recursively creates directories based on `PATH`. Can throw. `PATH` - string.

Must have file I/O permissions.
```pil
path-create-dir PATH
```

## path-remove
Remove a file or an empty directory based on `PATH`. Can throw. `PATH` - string.

Must have file I/O permissions.
```pil
path-remove PATH
```

## path-remove-all
Remove files and directories recursively based on `PATH`. Can throw. `PATH` - string.

Must have file I/O permissions.
```pil
path-remove-all PATH
```

## path-copy
Copy `PATH` to `DESTINATION`. Can throw. `PATH` - string, `DESTINATION` - string.

Must have file I/O permissions.
```pil
path-copy PATH, DESTINATION
```

## path-move
Move `PATH` to `DESTINATION`. Can throw. `PATH` - string, `DESTINATION` - string.

Must have file I/O permissions.
```pil
path-move PATH, DESTINATION
```

## path-join
Join both paths together, allocate it and store in `DESTINATION`. `PATH1` - string, `PATH2` - string, `DESTINATION` - container.
```pil
path-join PATH1, PATH2, DESTINATION
```

## path-filename
Allocate the filename of the path (dir/file.ext -> file.ext) and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.
```pil
path-filename PATH, DESTINATION
```

## path-stem
Allocate the stem of the path (dir/file.ext -> file) and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.
```pil
path-stem PATH, DESTINATION
```

## path-extension
Allocate the extension of the path (dir/file.ext -> .ext) and store it in `DESTINATION`. Files with extensions return their extension starting with a dot, whereas files with no extension will return an empty string. `PATH` - string, `DESTINATION` - container.
```pil
path-extension PATH, DESTINATION
```

## path-parent
Allocate the parent of the path (dir/file.ext -> dir/) and store it in `DESTINATION`. Returns a copy of `PATH` if no parent is present. `PATH` - string, `DESTINATION` - container.
```pil
path-parent PATH, DESTINATION
```

## path-absolute
Allocate the absolute path of `PATH` and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.
```pil
path-absolute PATH, DESTINATION
```

## path-normalize
Allocate the lexically normal path of `PATH` and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.
```pil
path-normalize PATH, DESTINATION
```

## dir-list
Allocate an array of all paths of files and directories found in `PATH` and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
dir-list PATH, DESTINATION
```

## dir-list-recursive
Allocate an array of all paths of files and directories recursively found in `PATH` and store it in `DESTINATION`. `PATH` - string, `DESTINATION` - container.

Must have file I/O permissions.
```pil
dir-list-recursive PATH, DESTINATION
```

## os-name
Allocate and return the name of the user's OS. Windows - `windows`, MacOS - `macos`, Linux - `linux`, any other OS - `unknown`. `DESTINATION` - container.
```pil
os-name DESTINATION
```

## os-cwd
Allocate the current working directory and store in `DESTINATION`. Can throw. `DESTINATION` - container.

Must have file I/O permissions.
```pil
os-cwd DESTINATION
```

## os-set-cwd
Set the current working directory to `PATH`. Can throw. `PATH` - string.

Must have file I/O permissions.
```pil
os-set-cwd PATH
```

## os-env-get
Get environment variable `VAR` and store it in `DESTINATION`. Stores null if it doesn't exist. `VAR` - string, `DESTINATION` - container.

Must have environment permissions.
```pil
os-env-get VAR, DESTINATION
```

## os-env-set
Set environment variable `VAR` to stringified value `VALUE`. `VAR` - string, `VALUE` - stringifyable value.

Must have environment permissions.
```pil
os-env-set VAR, VALUE
```

## os-exec
Execute command `COMMAND` and store any output up until 4KiB in `DESTINATION`. Throws if cannot open pipe. `COMMAND` - string, `DESTINATION` - container.

Must have command execution permissions.
```pil
os-exec COMMAND, DESTINATION
```

## os-exit-code
Stores the last exit code from `os-exec` in `DESTINATION`. By default it is 0. `DESTINATION` - container.
```pil
os-exit-code DESTINATION
```
