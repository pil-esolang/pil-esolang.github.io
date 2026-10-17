# Map library
It is recommended to read [Language/Values](../language/values.md) first for a better understanding of allowed parameter types, value semantics and behavior.

## map-new
Allocate a new map with all key-value pairs after `MAP` set. Throws if passed argument count is even. `MAP` - container, `KEY1` - key value, `VALUE1` - any value.
```pil
map-new MAP, KEY1, VALUE1, ...
```

## map-erase
Erase a key-value pair from the map based on the `KEY`. Does nothing if it does not exist. `MAP` - map, `KEY` - key value.
```pil
map-erase MAP, KEY
```

## map-set
Set or insert a `VALUE` with the key `KEY`. `MAP` - map, `KEY` - key value, `VALUE` - any value.
```pil
map-set MAP, KEY, VALUE
```

## map-at
Get the value at key `KEY` and store it in `DESTINATION`. If there is no value at `KEY`, store null. `MAP` - map, `KEY` - key value, `DESTINATION` - container.
```pil
map-at MAP, KEY, DESTINATION
```

## map-contains
Stores 1 in `DESTINATION` if a key-value pair with key `KEY` exists, otherwise 0. `MAP` - map, `KEY` - key value, `DESTINATION` - container.
```pil
map-contains MAP, KEY, DESTINATION
```

## map-size
Stores the size of the map in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-size MAP, DESTINATION
```

## map-empty
Stores 1 in `DESTINATION` if the map is empty, otherwise 0. `MAP` - map, `DESTINATION` - container.
```pil
map-empty MAP, DESTINATION
```

## map-clear
Clears all key-value pairs. `MAP` - map.
```pil
map-clear MAP
```

## map-keys
Gets all map's keys, allocates an array of them and stores in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-keys MAP, DESTINATION
```

## map-values
Gets all map's values, allocates an array of them and stores in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-values MAP, DESTINATION
```

## map-merge
Merge `MAP1` and `MAP2` and store the result in `DESTINATION`. `MAP2`'s values have higher priority. `MAP1` - map, `MAP2` - map, `DESTINATION` - container.
```pil
map-merge MAP1, MAP2, DESTINATION
```

## map-free
Frees all maps and sets them to null. Does not free maps' key-value pairs. Using a free map will result in an use-after-free error. `MAP1...` - maps.
```pil
map-free MAP1, ...
```

## map-deep-free
Frees all maps and their key-value pairs recursively and sets them to null. Using a freed map will result in an use-after-free error. `MAP1...` - maps.
```pil
map-deep-free MAP1, ...
```

## map-copy
Shallow copies a map into `DESTINATION`. Only copies references for complex runtime values like dynamic strings, arrays and maps. `MAP` - map, `DESTINATION` - container.
```pil
map-copy MAP, DESTINATION
```

## map-deep-copy
Deep copies a map into `DESTINATION`. Copies all dynamic strings, arrays and maps recursively. If the map contains multiple identical references to the same object, it is only copied once. `MAP` - map, `DESTINATION` - container.
```pil
map-deep-copy MAP, DESTINATION
```
