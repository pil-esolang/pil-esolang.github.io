# Array library
It is recommended to read [Language/Values](../language/values.md) first for a better understanding of allowed parameter types, value semantics and behavior.

## array-new
Allocate a new array with all values after `ARRAY` as values. `ARRAY` - container, `ARG1...` - any value.
```pil
array-new ARRAY, ARG1, ...
```

## array-fill
Fill an array with `N` `VALUE`s, allocate it and store it in `ARRAY`. `ARRAY` - container, `N` - unsigned integer, `VALUE` - any value.
```pil
array-fill ARRAY, N, VALUE
```

## array-iota
Fill an array with `N` incrementing integers starting from `START`, allocate it and store in `ARRAY`. `ARRAY` - container, `N` - unsigned integer, `START` - integer.
```pil
array-iota ARRAY, N, START
```

## array-clear
Clears array. Its memory will still be available. `ARRAY` - array.
```pil
array-clear ARRAY
```

## array-memfree
Clears array and frees its memory. Does not free the array itself and is not necessary to call it before freeing it. `ARRAY` - array.
```pil
array-memfree ARRAY
```

## array-empty
Stores 1 in `DESTINATION` if the array is empty, otherwise 0. `ARRAY` - array, `DESTINATION` - container.
```pil
array-empty ARRAY, DESTINATION
```

## array-size
Stores the size of the array in `DESTINATION`. `ARRAY` - array, `DESTINATION` - container.
```pil
array-size ARRAY, DESTINATION
```

## array-capacity
Stores the capacity of the array in `DESTINATION`. `ARRAY` - array, `DESTINATION` - container.
```pil
array-capacity ARRAY, DESTINATION
```

## array-reserve
Reserves `N` capacity for the array to prevent unnecessary reallocations. `ARRAY` - array, `N` - unsigned integer.
```pil
array-reserve ARRAY, N
```

## array-resize
Resizes array to `N` values. If the new size is greater than the previous then the empty slots are filled with `VALUE`. Might reallocate the array. `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-resize ARRAY, N, VALUE
```

## array-set
Set a value at position `N` to value `VALUE`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-set ARRAY, N, VALUE
```

## array-at
Get a value at position `N` and store it in `DESTINATION`. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer, `DESTINATION` - container.
```pil
array-at ARRAY, N, DESTINATION
```

## array-back
Get the back (last) value of the array and store it in `DESTINATION`. Throws if array is empty. `ARRAY` - array, `DESTINATION` - container.
```pil
array-back ARRAY, DESTINATION
```

## array-front
Get the front (first) value of the array and store it in `DESTINATION`. Throws if array is empty. `ARRAY` - array, `DESTINATION` - container.
```pil
array-front ARRAY, DESTINATION
```

## array-push
Push `VALUE` at the end of the array. Might reallocate the array. `ARRAY` - array, `VALUE` - ANY VALUE.
```pil
array-push ARRAY, VALUE
```

## array-insert
Insert `VALUE` at position `N` in the array. Throws if `N` is out of bounds (`N` < 0 || `N` > `SIZE`). Might reallocate the array. `ARRAY` - array, `N` - unsigned integer, `VALUE` - any value.
```pil
array-insert ARRAY, N, VALUE
```

## array-pop
Pop the last value of the array. Throws if array is empty. `ARRAY` - array.
```pil
array-pop ARRAY
```

## array-erase
Erase the value at position `N` in the array. Throws if `N` is out of bounds (`N` < 0 || `N` >= `SIZE`). `ARRAY` - array, `N` - unsigned integer.
```pil
array-erase ARRAY, N
```

## array-free
Frees all arrays and sets them to null. Does not free arrays' values. Using a freed array will result in an use-after-free error. `ARRAY1...` - arrays.
```pil
array-free ARRAY1, ...
```

## array-deep-free
Frees all arrays and their values recursively and sets them to null. Using a freed array will result in an use-after-free error. `ARRAY1...` - arrays.
```pil
array-deep-free ARRAY1, ...
```

## array-join
Stringify and concatenate all array's values with the `CONNECTOR` in-between, allocate the result and store it in `DESTINATION`. Throws if the array contains a map. `ARRAY` - array, `CONNECTOR` - stringifyable value, `DESTINATION` - container.
```pil
array-join ARRAY, CONNECTOR, DESTINATION
```

## array-concat
Combine `ARRAY1` and `ARRAY2` into one, allocate the result and store it in `DESTINATION`. `ARRAY1` - array, `ARRAY2` - array, `DESTINATION` - container.
```pil
array-concat ARRAY1, ARRAY2, DESTINATION
```

## array-slice
Slice the array [`START`; `END`), allocate the shallow copy and store it in `DESTINATION`. Throws if `START` < 0 || `START` >= `SIZE` || `END` < 0 || `END` > `SIZE` || `START` >= `END`. `ARRAY` - array, `START` - unsigned integer, `END` - unsigned integer, `DESTINATION` - container.
```pil
array-slice ARRAY, START, END, DESTINATION
```

## array-shuffle
Randomly shuffle the array based on global RNG. `ARRAY` - array.
```pil
array-shuffle ARRAY
```

## array-sort
Sort the array based on a callback function. The callback function must take in two arguments and must return a single value. Modifying the array or having improper sort condition can result in undefined behavior. `ARRAY` - array, `CALLBACK` - user-made function.
```pil
array-sort ARRAY, CALLBACK
```

## array-sort-asc
Sort the array in an ascending order. Throws if array contains non-comparable types (such as maps, functions, etc.). `ARRAY` - array.
```pil
array-sort-asc ARRAY
```

## array-sort-desc
Sort the array in a descending order. Throws if array contains non-comparable types (such as maps, functions, etc.). `ARRAY` - array.
```pil
array-sort-desc ARRAY
```

## array-count
Count the number of times `VALUE` occurrs in the array and store it in `DESTINATION`. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-count ARRAY, VALUE, DESTINATION
```

## array-reverse
Reverse the array. Time complexity is O(N/2). `ARRAY` - array.
```pil
array-reverse ARRAY
```

## array-find
Attempts to find the first occurrence of `VALUE` in the array. Sets `DESTINATION` to the position if it is found, else null. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-find ARRAY, VALUE, DESTINATION
```

## array-contains
Sets `DESTINATION` to 1 if `VALUE` can be found in the array, otherwise 0. Time complexity is O(N). `ARRAY` - array, `VALUE` - any value, `DESTINATION` - container.
```pil
array-contains ARRAY, VALUE, DESTINATION
```

## array-erase-if
Erases values based on a callback function. The callback function must take in a single argument and must return a single value. A value is erased if a truthy value is returned. Modifying the array while erasing can result in undefined behavior. `ARRAY` - array, `CALLBACK` - user-made function.
```pil
array-erase-if ARRAY, CALLBACK
```

## array-map
Modifies all values based on a callback function. The callback function must take in a single argument and must return a single value. The value returned will be the new value. Modifying the array while mapping values can result in undefined behavior. `ARRAY` - array, `CALLBACK` - user-made function.
```pil
array-map ARRAY, CALLBACK
```

## array-filter
Returns a span of shallow copied array based on a callback function. The callback function must take in a single argument and must return a single value. The element is included in the span if the returned value is truthy. Modifying the array while filtering can result in undefined behavior. Allocates an array. `ARRAY` - array, `CALLBACK` - user-made function, `DESTINATION` - container.
```pil
array-filter ARRAY, CALLBACK, DESTINATION
```

## array-reduce
Calculates a value based on a callback function by passing the return value from the previous calculation to the preceding element. Stores the final result in `DESTINATION`. The callback function must take in two arguments and must return a single value. Modifying the array while reducing can result in undefined behavior. `ARRAY` - array, `CALLBACK` - user-made function, `DESTINATION` - container.
```pil
array-reduce ARRAY, CALLBACK, DESTINATION
```

## array-copy
Shallow copies an array into `DESTINATION`. Only copies references for complex runtime values like dynamic strings, arrays and maps. `ARRAY` - array, `DESTINATION` - container.
```pil
array-copy ARRAY, DESTINATION
```

## array-deep-copy
Deep copies an array into `DESINATION`. Copies all dynamic strings, arrays and maps recursively. If the array contains multiple identical references to the same object, it is only copied once. `ARRAY` - array, `DESTINATION` - container.
```pil
array-deep-copy ARRAY, DESTINATION
```
