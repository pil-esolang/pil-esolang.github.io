# Getting Started
If you'd like an introduction first, [click here](introduction/introduction.md).

## Installation
To run PIL you need the PIL interpreter. There are two options:

1. download a pre-built executable from [Github Releases](https://github.com/pil-esolang/PIL/releases)
2. build the [source code](https://github.com/pil-esolang/PIL) yourself

## Building
You'll first need to clone the repository or download it as a ZIP. If cloning:
```bash
git clone https://github.com/pil-esolang/PIL.git
cd PIL
```

The project uses C++20 and can be built using CMake. To build in release:
```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```
After, the executable will be located in `build/pil`.

You can also simply build using your favorite compiler:
```bash
g++ -std=c++20 -Iinclude source/*.cpp -o pil
```

## Installing globally
To be able to use the interpreter from anywhere on Unix you can move it to `/usr/bin`:
```bash
sudo mv pil /usr/bin/pil
```
Then relaunch your terminal and run `pil -h` to verify.

On Windows you can move the executable to a safe spot (e.g. `C:/pil_interpreter/pil.exe`) and then add that folder to your path.

## Hello, World!
To run the famous hello world program paste this into a `main.pil` file:
```pil
main()
   println "Hello, World!"
```
And then run using this command:
```bash
pil run main.pil
```
This should be enough to get you going, good luck!
