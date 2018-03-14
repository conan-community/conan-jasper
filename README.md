# conan-jasper

![jasper image](/images/conan-jasper.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/jasper%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/jasper%3Aconan/_latestVersion)
[![Build Status](https://travis-ci.org/conan-community/conan-jasper.svg?branch=stable%2F2.0.14)](https://travis-ci.org/conan-community/conan-jasper)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/2.0.14?svg=true)](https://ci.appveyor.com/project/memsharded/conan-jasper/branch/stable/2.0.14)

[Conan.io](https://conan.io) package recipe for [JasPer](https://github.com/mdadams/jasper) project.

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/jasper%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install jasper/2.0.14@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    jasper/2.0.14@conan/stable

    [generators]
    cmake

## License

[MIT License](LICENSE)