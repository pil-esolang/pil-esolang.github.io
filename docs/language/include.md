# Include
You can include files using the `include` keyword. Includes work in a similar fashion to C/C++, however files are automatically guarded from being included multiple times. The files are lexed and tokens inserted in the include's position.

> include.pil
```pil
my-func()
   println "Hello, World!";
```

---

> main.pil
```pil
include "include.pil"

main()
   my-func;
```

Includes assume the directory in which the PIL interpreter is run. It is a good practice to define main.pil in the source directory and assume PIL interpreter to be ran from there. From that point, you can define other files next to it or in folders next to main.pil.

```txt
project
|_include
   |_include1.pil
   |_include2.pil
   |_...
|_main.pil
```
