# String library
## String types
There are two types of strings: constant strings and dynamic strings. Constant strings are strings in quotes and they live for the entirety of the program and do not need to be deallocated. Dynamic strings, on the other hand, are returned by some of the built-ins, such as `string-new`, `string-format` and others. They must be deallocated manually or you'll get an error about a memory leak.

## String marking system
Each string has an integer tied to it - its mark. By default it is 0. The marking system is made for easily deallocating and retrieving a bulk of values. There are built-ins in place to achieve this.

## String library
### string-new
Stringifies and concatenates all arguments after `DESTINATION`, allocates a new string and stores it in `DESTINATION`. `DESTINATION` - container, `ARG1...` - any value except for maps.
```pil
string-new DESTINATION, ARG1, ...
```

### string-format
Formats the `FORMAT-STRING` string with all arguments after it, allocates a new string and stores it in `DESTINATION`. Works by replacing all `{}` with the arguments in left-to-right direction. Does not validate format argument count. `DESTINATION` - container, `FORMAT-STRING` - constant or dynamic string, `ARG1...` - any value except for maps.
```pil
string-format DESTINATION, FORMAT-STRING, ARG1, ...
```

### string-repeat
Stringifies `ARG`, allocates a new string that is `ARG` repeated `N` times and stores it in `DESTINATION` `DESTINATION` - container, `N` - unsigned integer, `ARG` - any value except for maps.
```pil
string-repeat DESTINATION, N, ARG
```

### string-clear
Clears string. Its memory will still be available. `STRING` - dynamic string.
```pil
string-clear STRING
```

### string-mem-free
Clears string and frees its memory. Does not free the string itself and is not necessary to call it before freeing it. `STRING` - dynamic string.
```pil
string-mem-free STRING
```

### string-empty
Stores 1 in `DESTINATION` if the string is empty, otherwise 0. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-empty STRING, DESTINATION
```

### string-size
Stores the size of the string in `DESTINATION`. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-size STRING, DESTINATION
```

### string-capacity
Stores the capacity (the maximum size before a reallocation) of the string in `DESTINATION`. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-capacity STRING, DESTINATION
```

### string-reserve
Reserves `N` capacity for the string to prevent unnecessary reallocations. `STRING` - dynamic string, `N` - unsigned integer.
```pil
string-reserve STRING, N
```

### string-resize
Resizes string to `N` characters. If the new size is greater than the previous then the empty slots are filled with `CHAR`. Might reallocate the string. `STRING` - dynamic string, `N` - unsigned integer, `CHAR` - character.
```pil
string-resize STRING, N, CHAR
```

### string-set
Set a character at position `N` to character `CHAR`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `STRING` - dynamic string, `N` - unsigned integer, `CHAR` - character.
```pil
string-set STRING, N, CHAR
```

### string-at
Get a character at position `N` and store it in `DESTINATION`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `STRING` - constant or dynamic string, `N` - unsigned integer, `DESTINATION` - container.
```pil
string-at STRING, N, DESTINATION
```

### string-back
Get the back (last) character of the string and store it in `DESTINATION`. Throws if string is empty. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-back STRING, DESTINATION
```

### string-front
Get the front (first) character of the string and store it in `DESTINATION`. Throws if string is empty. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-front STRING, DESTINATION
```

### string-push
Push `CHAR` at the end of the string. Might reallocate the string. `STRING` - dynamic string, `CHAR` - character.
```pil
string-push STRING, CHAR
```

### string-insert
Insert `CHAR` at position `N` in the string. Throws if `N` is out of bounds (`N` < 0 || `N` > `SIZE`). Might reallocate the string. `STRING` - dynamic string, `N` - unsigned integer, `CHAR` - character.
```pil
string-insert STRING, N, CHAR
```

### string-pop
Pop the last character of the string. Throws if string is empty. `STRING` - dynamic string.
```pil
string-pop STRING
```

### string-erase
Erase a character at position `N` in the string. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `STRING` - dynamic string, `N` - unsigned integer.
```pil
string-erase STRING, N
```

### string-free
Frees all strings and sets their values to null. Using a freed string will result in an use-after-free error. `ARG1...` - dynamic strings.
```pil
string-free ARG1, ...
```

### string-mark
Mark a string with integer `MARK`. A mark does nothing by itself. By default, strings are marked with 0. `STRING` - dynamic string, `MARK` - integer.
```pil
string-mark STRING, MARK
```

### string-get-mark
Get the mark of a string and store it in `DESTINATION`. `STRING` - dynamic string, `DESTINATION` - container.
```pil
string-get-mark STRING, DESTINATION
```

### string-free-marked
Free all strings marked with `MARK`. Unlike `string-free`, none of them will be set to null. Operation is O(N), where N is the number of allocated strings. `MARK` - integer.
```pil
string-free-marked MARK
```

### string-get-marked-count
Get the count of all strings marked with `MARK`. Operation is O(N), where N is the number of allocated strings. `MARK` - integer, `DESTINATION` - container.
```pil
string-get-marked-count MARK, DESTINATION
```

### string-get-marked
Get all strings marked with `MARK`, allocate an array with references to them and store in `DESTINATION`. Operation is O(N), where N is the number of allocated strings. `MARK` - integer, `DESTINATION` - container.
```pil
string-get-marked MARK, DESTINATION
```

### string-any-marked
Check if any string is marked with `MARK` and store 1 in `DESTINATION` if there is, otherwise 0. Operation is O(N), where N is the number of allocated strings. `MARK` - integer, `DESTINATION` - container.
```pil
string-any-marked MARK, DESTINATION
```

### string-split
Split the string on `DELIMITER`, allocate an array of the split pieces and store it in `DESTINATION`. Time complexity is O(N*M). Throws if `DELIMITER` is empty. `STRING` - constant or dynamic string, `DELIMITER` - constant or dynamic string or character, `DESTINATION` - container.
```pil
string-split STRING, DELIMITER, DESTINATION
```

### string-concat
Stringifies and concatenate all values after `STRING` to the string. `STRING` - dynamic string, `ARG1...` - any values except for maps.
```pil
string-concat STRING, ARG1, ...
```

### string-substr
Creates a substring [start; end) from the given string and saves it in `DESTINATION`. Throws if `START` < 0 || `START` >= `SIZE` || `END` < 0 || `END` > `SIZE` || `START` >= `END`. `STRING` - constant or dynamic string, `START` - unsigned integer, `END` - unsigned integer, `DESTINATION` - container.
```pil
string-substr STRING, START, END, DESTINATION
```

### string-count
Counts the number of occurrences of `TARGET` in the string and stores it in `DESTINATION`. Time complexity if `TARGET` is a character is O(N), whereas if `TARGET` is a string, the complexity is O(N + M), where M is the size of the target string. `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string or character, `DESTINATION` - container.
```pil
string-count STRING, TARGET, DESTINATION
```

### string-reverse
Reverses the string. Time complexity is O(N/2). `STRING` - dynamic string.
```pil
string-reverse STRING
```

### string-find
Attempts to find `TARGET` in the string starting from position `START` (0 to search everything). Returns position if target can be found, otherwise null. Time complexity is O(N*M). Throws if `START` < 0 || `START` > `SIZE`. `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string or character, `START` - unsigned integer, `DESTINATION` - container.
```pil
string-find STRING, TARGET, START, DESTINATION
```

### string-rfind
Attempts to find `TARGET` in the string starting from position `START` (>=`SIZE` or -1 to search everything) in a reverse order. Returns position if target can be found, otherwise null. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string or character, `START` - unsigned integer, `DESTINATION` - container.
```pil
string-rfind STRING, TARGET, START, DESTINATION
```

### string-find-first-of
Attempts to find the first character found in `TARGET` in the string. Returns position if target can be found, otherwise null. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string, `DESTINATION` - container.
```pil
string-find-first-of STRING, TARGET, DESTINATION
```

### string-find-first-not-of
Attempts to find the first character not found in `TARGET` in the string. Returns position if target can be found, otherwise null. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string, `DESTINATION` - container.
```pil
string-find-first-not-of STRING, TARGET, DESTINATION
```

### string-find-last-of
Attempts to find the first character found in `TARGET` in the string in a reverse order. Returns position if target can be found, otherwise null. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string, `DESTINATION` - container.
```pil
string-find-last-of STRING, TARGET, DESTINATION
```

### string-find-last-not-of
Attempts to find the first character not found in `TARGET` in the string in a reverse order. Returns position if target can be found, otherwise null. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string, `DESTINATION` - container.
```pil
string-find-last-not-of STRING, TARGET, DESTINATION
```

### string-replace
Attempts to find `TARGET` in the string and if it does, replaces it with `REPLACEMENT`. Time complexity is O(N*M). Throws if `START` < 0 || `START` > `SIZE`. `STRING` - dynamic string, `TARGET` - constant or dynamic string or character, `REPLACEMENT` - constant or dynamic string or character, `START` - unsigned integer.
```pil
string-replace STRING, TARGET, REPLACEMENT, START
```

### string-replace-all
Finds all `TARGET`s in the string and replaces them with `REPLACEMENT`. Time complexity is O(N*M) to O(N\*M\*K) depending on how `TARGET`'s size differs from `REPLACEMENT`'s and on match count. Throws if `REPLACEMENT` is empty. `STRING` - dynamic string, `TARGET` - constant or dynamic string or character, `REPLACEMENT` - constant or dynamic string or character.
```pil
string-replace-all STRING, TARGET, REPLACEMENT
```

### string-contains
Stores 1 in `DESTINATION` if `TARGET` is found in the string, else 0. Time complexity is O(N*M). `STRING` - constant or dynamic string, `TARGET` - constant or dynamic string or character, `DESTINATION` - container.
```pil
string-contains STRING, TARGET, DESTINATION
```

### string-erase-all
Erases all characters found in `CHARS` from the string. Time complexity is O(N*M). `STRING` - dynamic string, `CHARS` - constant or dynamic string or character.
```pil
string-erase-all STRING, CHARS
```

### string-starts-with
Stores 1 in `DESTINATION` if string starts with `START`, else 0. `STRING` - constant or dynamic string, `START` - constant or dynamic string or character, `DESTINATION` - container.
```pil
string-starts-with STRING, START, DESTINATION
```

### string-ends-with
Stores 1 in `DESTINATION` if string ends with `END`, else 0. `STRING` - constant or dynamic string, `END` - constant or dynamic string or character, `DESTINATION` - container.
```pil
string-ends-with STRING, END, DESTINATION
```

### string-trim
Trims all whitespace from both sides of the string. `STRING` - dynamic string.
```pil
string-trim STRING
```

### string-to-lower
Converts string to lowercase. `STRING` - dynamic string.
```pil
string-to-lower STRING
```

### string-to-upper
Converts string to uppercase. `STRING` - dynamic string.
```pil
string-to-upper STRING
```

### string-copy
Copies and allocates a new string into `DESTINATION`. `STRING` - constant or dynamic string, `DESTINATION` - container.
```pil
string-copy STRING, DESTINATION
```
