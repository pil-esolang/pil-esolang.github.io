# Enumerations
Enumerations are a group of similar constant named integers. They are used to define a plethora of integral constants. By default enumerations start with 0 and increment by one after each constant. Enumerations can also be set to specific integral values.

Just like constants, enumerations don't exist during the runtime and are completely replaced with their corresponding values at parse-time.

## Declaration
They can be defined using the `enum` keyword in a similar fashion to structures:
```pil
enum ENUMERATION ( ENTRY1, ENTRY2 = INTEGER, ENTRY3... )
```
And in practice they look like this:
```pil
enum Day (
   Monday = 1,
   Tuesday,
   Wednesday,
   Thursday,
   Friday,
   Saturday,
   Sunday,
)

enum Direction (
   East,
   West,
   North,
   South,
)

enum PermissionFlags (
   File        = [1 << 0], # 1
   Environment = [1 << 1], # 2
   OsExec      = [1 << 2], # 4
   Network     = [1 << 3], # 8
)
```

There are also array enumerations that work more closely to constants. They don't require the dot syntax to access but in turn polute the global namespace with a lot of symbols. It's recommended to either not use them or use them with MACRO_CASE. Everything else functions just the same as for regular enumerations. They can be defined by using `array` keyword after `enum` keyword:
```pil
enum array Thing (
   x = 20,
   y = 30,
   z = 40,
   w = 50,
)

main()
   println Thing.x; # 20
   println Thing.y; # 30
   println z;       # 40
   println w;       # 50
```

## Access
Enumeration values can be accessed using `ENUM.ENTRY` syntax. Enumeration types cannot be passed just like structures can and are purely parse-time for this reason. Enumerations cannot be converted to strings without an external array for the same reason. To access array enumerations, you can use the aforementioned syntax or simply the entry's name.
```pil
enum Direction ( East, West, North, South )

main()
   local direction, map, name;
   array-new map, "east", "west", "north", "south";

   set Direction.East, direction;
   array-at map, direction, name;
   println "Wind is blowing from ", name;

   set Direction.North, direction;
   array-at map, direction, name;
   println "Now wind is blowing from ", name;
   free map;
```
