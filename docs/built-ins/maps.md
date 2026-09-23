# Map library
## Maps
Maps are hashed containers where keys map to values. Keys cannot consist of other maps or arrays. In PIL they are passed around as references and only copied when explicitly told to. Unlike strings, there is no parse-time alternative.

## Map marking system
Each map has an integer tied to it - its mark. By default it is 0. The marking system is made for easily deallocating and retrieving a bulk of values. There are built-ins in place to achieve this.

## Map library
### map-new
Allocate a new map with all key-value pairs after `MAP` set. Throws if passed argument count is even. `MAP` - container, `KEY1` - any value except for arrays and map, `VALUE1` - any value.
```pil
map-new MAP, KEY1, VALUE1, ...
```

### map-erase
Erase a key-value pair from the map based on the `KEY`. Does nothing if it does not exist. `MAP` - map, `KEY` - any value except for arrays and map.
```pil
map-erase MAP, KEY
```

### map-set
Set or insert a `VALUE` with the key `KEY`. `MAP` - map, `KEY` - any value except for arrays and maps, `VALUE` - any value.
```pil
map-set MAP, KEY, VALUE
```

### map-at
Get the value at key `KEY` and store it in `DESTINATION`. If there is no value at `KEY`, store null. `MAP` - map, `KEY` - any value except for arrays and maps, `DESTINATION` - container.
```pil
map-at MAP, KEY, DESTINATION
```

### map-contains
Stores 1 in `DESTINATION` if a key-value pair with key `KEY` exists, otherwise 0. `MAP` - map, `KEY` - any value except for arrays and maps, `DESTINATION` - container.
```pil
map-contains MAP, KEY, DESTINATION
```

### map-size
Stores the size of the map in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-size MAP, DESTINATION
```

### map-empty
Stores 1 in `DESTINATION` if the map is empty, otherwise 0. `MAP` - map, `DESTINATION` - container.
```pil
map-empty MAP, DESTINATION
```

### map-clear
Clears all key-value pairs. `MAP` - map.
```pil
map-clear MAP
```

### map-keys
Gets all map's keys, allocates an array of them and stores in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-keys MAP, DESTINATION
```

### map-values
Gets all map's values, allocates an array of them and stores in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-values MAP, DESTINATION
```

### map-merge
Merge `MAP1` and `MAP2` and store the result in `DESTINATION`. `MAP2`'s values have higher priority. `MAP1` - map, `MAP2` - map, `DESTINATION` - container.
```pil
map-merge MAP1, MAP2, DESTINATION
```

### map-free
Frees all maps and sets them to null. Does not free maps' key-value pairs. Using a free map will result in an use-after-free error. `MAP1...` - maps.
```pil
map-free MAP1, ...
```

### map-deep-free
Frees all maps and their key-value pairs recursively and sets them to null. Using a freed map will result in an use-after-free error. `MAP1...` - maps.
```pil
map-deep-free MAP1, ...
```

### map-mark
Mark a map with integer `MARK`. A mark does nothing by itself. By default, maps are marked with 0. `MAP` - map, `MARK` - integer.
```pil
map-mark MAP, MARK
```

### map-get-mark
Get the mark of a map and store it in `DESTINATION`. `MAP` - map, `DESTINATION` - container.
```pil
map-get-mark MAP, DESTINATION
```

### map-free-marked
Free all maps marked with `MARK`. Unlike `map-free`, none of them will be set to null. Operation is O(N), where N is the number of allocated maps. `MARK` - integer.
```pil
map-free-marked MARK
```

### map-get-marked-count
Get the count of all maps marked with `MARK`. Operation is O(N), where N is the number of allocated maps. `MARK` - integer, `DESTINATION` - container.
```pil
map-get-marked-count MARK, DESTINATION
```

### map-get-marked
Get all maps marked with `MARK`, allocate an array with references to them and store in `DESTINATION`. Operation is O(N), where N is the number of allocated maps. `MARK` - integer, `DESTINATION` - container.
```pil
map-get-marked MARK, DESTINATION
```

### map-any-marked
Check if any map is marked with `MARK` and store 1 in `DESTINATION` if there is, otherwise 0. Operation is O(N), where N is the number of allocated maps. `MARK` - integer, `DESTINATION` - container.
```pil
map-any-marked MARK, DESTINATION
```

### map-shallow-copy
Shallow copies a map into `DESTINATION`. Only copies references for complex runtime values like dynamic strings, arrays and maps. `MAP` - map, `DESTINATION` - container.
```pil
map-shallow-copy MAP, DESTINATION
```

### map-deep-copy
Deep copies a map into `DESTINATION`. Copies all dynamic strings, arrays and maps recursively. If the map contains multiple identical references to the same object, it is only copied once. `MAP` - map, `DESTINATION` - container.
```pil
map-deep-copy MAP, DESTINATION
```
