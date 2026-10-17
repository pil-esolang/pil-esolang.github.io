# Structures
Structures are user-defined data types with multiple named fields. They can be used to nicely organize data and are a must in larger projects.

## Declaration
Structures can be defined using the `struct` keyword:
```pil
struct array? STRUCTURE ( FIELD1, FIELD2... )
```
In practice it looks like this:
```pil
struct Vec2 ( x, y )
struct Rectangle ( x, y, width, height )
struct Level (
   player,
   obstacles,
   enemies,
   collectedCoins,
   coinCount,
   boundaries,
)
```

Structures are arrays under the hood. By default array functionality is disabled and none of the array built-ins work with objects. To enable this functionality, add `array` keyword after `struct`. This will enable all array built-ins. Be careful with this, as using an invalid field will result in undefined behavior.
```pil
struct array MyArray ( a, b, c, d, e )
```

## Creation
Objects can be created using the [make](../built-ins/builtins.md#make) built-in. You must pass the same number of arguments as the amount of fields the structure has. No field can be left uninitialized (unless using structure arrays and then initializing them yourself). This allocates the object.
```pil
global null;

main()
   local v, r, l;
   make Vec2, v, 2.5, 6.2;
   make Rectangle, r, 0.2, 6.4, 10.0, 20.0;
   make Level, l, null, null, null, 0, 0, null;
   println v;
   println r;
   println l;
   free v, r, l;
```

## Freeing
Since objects are allocated, they must also be deallocated manually using [free](../built-ins/builtins.md#free) or [deep-free](../built-ins/builtins.md#deep-free) built-ins. This can be seen in the previous example.

## Field access
To access and modify fields, suffix the variable with a dot and the name of the field. Using field access, you can also directly write to the object.
```pil
struct Vec2 ( x, y )
struct Pair ( first, second )

main()
   local v1, v2, pair;
   make Vec2, v1, 1.0, 2.0;
   printfln "({}, {})", v1.x, v1.y;
   make Vec2, v2, 4.0, 3.0;
   printfln "({}, {})", v2.x, v2.y;

   make Pair, pair, v1, v2;
   printfln "({}, {})", pair.first, pair.second;
   free v1, v2;

   set 13, pair.first;
   set 37, pair.second;
   printfln "({}, {})", pair.first, pair.second;
   free pair;
```
