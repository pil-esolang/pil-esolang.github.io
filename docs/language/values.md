# Values
A value holds a specific type of data. A container can hold any type of value and can dynamically change during runtime.

## Values
<table>
   <thead><tr>
      <th>Name</th>
      <th>Example</th>
      <th>Description</th>
   </tr></thead>
   <tbody>
      <tr><td>Integer</td><td>123</td><td>64-bit signed integer</td></tr>
      <tr><td>Floating</td><td>123.456</td><td>Double, most likely 64 bits</td></tr>
      <tr><td>Character</td><td>'a'</td><td>A single character</td></tr>
      <tr><td>Constant string</td><td>"Hello, World!"</td><td>Parse-time constant string</td></tr>
      <tr><td>Dynamic string</td><td>string-new "Hello, World!", $0</td><td>Allocated runtime string</td></tr>
      <tr><td>Function pointer</td><td>main</td><td>Pointer to a function</td></tr>
      <tr><td>Label</td><td>label</td><td>Pointer to a label</td></tr>
      <tr><td>Local variable</td><td>local</td><td>Named container that holds a value</td></tr>
      <tr><td>Register</td><td>$0</td><td>Index of a register that holds a value</td></tr>
      <tr><td>Return register</td><td>r$0</td><td>Index of a return register that holds a value</td></tr>
      <tr><td>Array</td><td>array-new $0, 1, 2, 3</td><td>Dynamically allocated array of dynamic size</td></tr>
      <tr><td>Map</td><td>map-new $0, 1, 2</td><td>Allocated hash map</td></tr>
      <tr><td>File handle</td><td>file-open "my.file", 'r', $0</td><td>A file handle</td></tr>
      <tr><td>Structure</td><td>struct Struct (...)</td><td>A user-defined structure</td></tr>
      <tr><td>Structure Access</td><td>Struct.Field</td><td>Access into a structure</td></tr>
      <tr><td>Global Variable</td><td>global</td><td>Named container that holds a value</td></tr>
      <tr><td>Null</td><td>to-int "", $0</td><td>Invalid/error value</td></tr>
   </tbody>
</table>

## Value classification
Values program-wise are split in 3 types: parse-time, runtime and container values. Container values simultaneously go under runtime values.

#### Parse-time values
Parse-time values are basic values that are able to be created at parse-time. These include integers, floating-point numbers, characters and constant strings.

#### Runtime values
Runtime values are values that must be allocated to use or require references usable after parsing. These include dynamic strings, arrays, maps, file handles, function pointers, labels and null. All except null are simply references to internal values and have to be copied explicitly (if allowed by the data type).

#### Containers
Containers are runtime values that store other values. These include registers, return registers, locals, globals and structure accesses. Constants do not fall under this category as they do not exist after parsing.

## Built-in value terminology
Built-in documentation uses the following terminology to name a group of types.

#### Stringifyable values
Stringifyable values refer to values whose underlying data can be converted to a string. These include any type except for maps and file handles.

#### Key value
Key values are any value that can be used as a key for a hash map. These are any value except for arrays, maps and file handles.

#### String value
String value refers to any string value - constant or dynamic string, unless specifically noted as only a constant or dynamic string.

#### Unsigned integer
Unsigned integer is an integer that cannot be negative. It still is signed under the hood but when passed to a built-in it must not be negative.

## String types
There are two types of strings - constant strings and dynamic strings. Constant strings are strings defined in quotes and they live for the entirety of the program and do not need to be deallocated. Dynamic strings, on the other hand, are returned by some of the built-ins and they must be deallocated manually.
