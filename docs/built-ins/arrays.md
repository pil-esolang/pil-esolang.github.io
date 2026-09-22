# Array library
## Arrays
Arrays are data structures consisting of a collection of values. In PIL they are passed around as references and only copied when explicitly told to. All arrays are dynamic, meaning their size can be changed. Unlike strings, there is no parse-time alternative.

## Array marking system
Each array has an integer tied to it - its mark. By default it is 0. The marking system is made for easily deallocating and retrieving a bulk of values. There are built-ins in place to achieve this.

## Array library
### array-new
Allocate a new array with all values after `ARRAY` as values. `ARRAY` - container, `ARG1...` - any value.
```pil
array-new ARRAY, ARG1, ...
```

### array-fill
Fill an array with `N` `VALUE`s, allocate it and store it in `ARRAY`. `ARRAY` - container, `N` - unsigned integer, `VALUE` - any value.
```pil
array-fill ARRAY, N, VALUE
```

### array-iota
Fill an array with `N` incrementing integers starting from `START`, allocate it and store in `ARRAY`. `ARRAY` - container, `N` - unsigned integer, `START` - integer.
```pil
array-iota ARRAY, N, START
```

### array-clear
Clears array. Its memory will still be available. `ARRAY` - array.
```pil
array-clear ARRAY
```

### array-memfree
Clears array and frees its memory. Does not free the array itself and is not necessary to call it before freeing it. `ARRAY` - array.
```pil
array-memfree ARRAY
```

### array-empty
Stores 1 in `DESTINATION` if the array is empty, otherwise 0. `ARRAY` - array, `DESTINATION` - container.
```pil
array-empty ARRAY, DESTINATION
```

### array-size
Stores the size of the array in `DESTINATION`. `ARRAY` - array, `DESTINATION` - container.
```pil
array-size ARRAY, DESTINATION
```

### array-capacity
Stores the capacity of the array in `DESTINATION`. `ARRAY` - array, `DESTINATION` - container.
```pil
array-capacity ARRAY, DESTINATION
```

### array-reserve
Reserves `N` capacity for the array to prevent unnecessary reallocations. `ARRAY` - array, `N` - unsigned integer.
```pil
array-reserve ARRAY, N
```

### array-resize
Resizes array to `N` values. If the new size is greater than the previous then the empty slots are filled with `VALUE`. Might reallocate the array. `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-resize ARRAY, N, VALUE
```

### array-set
Set a value at position `N` to value `VALUE`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-set ARRAY, N, VALUE
```

### array-at
Get a value at position `N` and store it in `DESTINATION`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer, `DESTINATION` - container.
```pil
array-at ARRAY, N, DESTINATION
```

### array-back
Get the back (last) value of the array and store it in `DESTINATION`. Throws if array is empty. `ARRAY` - array, `DESTINATION` - container.
```pil
array-back ARRAY, DESTINATION
```

### array-front
Get the front (first) value of the array and store it in `DESTINATION`. Throws if array is empty. `ARRAY` - array, `DESTINATION` - container.
```pil
array-front ARRAY, DESTINATION
```

### array-push
Push `VALUE` at the end of the array. Might reallocate the array. `ARRAY` - array, `VALUE` - ANY VALUE.
```pil
array-push ARRAY, VALUE
```

### array-insert
Insert `VALUE` at position `N` in the array. Throws if `N` is out of bounds (`N` < 0 || `N` > `SIZE`). Might reallocate the array. `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-insert ARRAY, N, VALUE
```

### array-pop
Pop the last value of the array. Throws if array is empty. `ARRAY` - array.
```pil
array-pop ARRAY
```

### array-erase
Erase the value at position `N` in the array. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer.
```pil
array-erase ARRAY, N
```

### array-free
Frees all arrays and sets them to null. Does not free arrays' values. Using a freed array will result in an use-after-free error. `ARG1...` - arrays.
```pil
array-free ARG1, ...
```

### array-deep-free
Frees all arrays and their values recursively and sets them to null. Using a freed array will result in an use-after-free error. `ARG1...` - arrays.
```pil
array-deep-free ARG1, ...
```

### array-mark
Mark an array with integer `MARK`. A mark does nothing by itself. By default, arrays are marked with 0. `ARRAY` - array, `MARK` - integer.
```pil
array-mark ARRAY, MARK
```

### array-get-mark
Get the mark of an array and store it in `DESTINATION`. `ARRAY` - array, `DESTINATION` - container.
```pil
array-get-mark ARRAY, DESTINATION
```

### array-free-marked
Free all arrays marked with `MARK`. Unlike `array-free`, none of them will be set to null. Operation is O(N), where N is the number of allocated arrays. `MARK` - integer.
```pil
array-free-marked MARK
```

### array-get-marked-count
Get the count of all arrays marked with `MARK`. Operation is O(N), where N is the number of allocated arrays. `MARK` - integer, `DESTINATION` - container.
```pil
array-get-marked-count MARK, DESTINATION
```

### array-get-marked
Get all arrays marked with `MARK`, allocate an array with references to them and store in `DESTINATION`. Operation is O(N), where N is the number of allocated arrays. `MARK` - integer, `DESTINATION` - container.
```pil
array-get-marked MARK, DESTINATION
```

### array-any-marked
Check if any array is marked with `MARK` and store 1 in `DESTINATION` if there is, otherwise 0. Operation is O(N), where N is the number of allocated arrays. `MARK` - integer, `DESTINATION` - container.
```pil
array-any-marked MARK, DESTINATION
```

### array-join
Stringify and concatenate all array's values with the `CONNECTOR` in-between, allocate the result and store it in `DESTINATION`. Throws if the array contains a map. `ARRAY` - array, `CONNECTOR` - any value except for maps, `DESTINATION` - container.
```pil
array-join ARRAY, CONNECTOR, DESTINATION
```

### array-concat
Combine `ARRAY1` and `ARRAY2` into one, allocate the result and store it in `DESTINATION`. `ARRAY1` - array, `ARRAY2` - array, `DESTINATION` - container.
```pil
array-concat ARRAY1, ARRAY2, DESTINATION
```

### array-slice
Slice the array [`START`; `END`), allocate the shallow copy and store it in `DESTINATION`. Throws if `START` < 0 || `START` >= `SIZE` || `END` < 0 || `END` > `SIZE` || `START` >= `END`. `ARRAY` - array, `START` - unsigned integer, `END` - unsigned integer, `DESTINATION` - container.
```pil
array-slice ARRAY, START, END, DESTINATION
```

### array-shuffle
Randomly shuffle the array based on global RNG. `ARRAY` - array.
```pil
array-shuffle ARRAY
```

### array-sort
Sort the array. Sorts ascendingly if `ASCENDING` is thruthy, descendingly otherwise. Throws if array contains functions, labels, arrays or maps. `ARRAY` - array, `ASCENDING` - integer.
```pil
array-sort ARRAY, ASCENDING
```

### array-count
Count the number of times `VALUE` occurrs in the array and store it in `DESTINATION`. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-count ARRAY, VALUE, DESTINATION
```

### array-reverse
Reverse the array. Time complexity is O(N/2). `ARRAY` - array.
```pil
array-reverse ARRAY
```

### array-find
Attempts to find the first occurrence of `VALUE` in the array. Sets `DESTINATION` to the position if it is found, else null. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-find ARRAY, VALUE, DESTINATION
```

### array-contains
Sets `DESTINATION` to 1 if `VALUE` can be found in the array, otherwise 0. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-contains ARRAY, VALUE, DESTINATION
```

### array-erase-all
Erases all `VALUE`s from array. Time complexity is O(N). `ARRAY` - array, `VALUE` - value.
```pil
array-erase-all ARRAY, VALUE
```

### array-shallow-copy
Shallow copies an array into `DESTINATION`. Only copies references for complex runtime values like dynamic strings, arrays and maps. `ARRAY` - array, `DESTINATION` - container.
```pil
array-shallow-copy ARRAY, DESTINATION
```

### array-deep-copy
Deep copies an array into `DESINATION`. Copies all dynamic strings, arrays and maps recursively. If the array contains multiple identical references to the same object, it is only copied once. `ARRAY` - array, `DESTINATION` - container.
```pil
array-deep-copy ARRAY, DESTINATION
```
