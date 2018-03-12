from conans import ConanFile, CMake, tools
import os


class JasperConan(ConanFile):
    name = "jasper"
    version = "2.0.14"
    license = "JasPer License Version 2.0"
    homepage = "https://github.com/mdadams/jasper"
    url = "https://github.com/conan-community/conan-jasper"
    description = "JasPer Image Processing/Coding Tool Kit"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = "libjpeg/9b@bincrafters/stable"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        tools.download("https://github.com/mdadams/jasper/archive/version-%s.zip" % self.version,
                       "jasper.zip")
        tools.unzip("jasper.zip")
        os.remove("jasper.zip")
        tools.replace_in_file("jasper-version-%s/CMakeLists.txt" % self.version,
                              "project(JasPer LANGUAGES C)",
                              """project(JasPer LANGUAGES C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["JAS_ENABLE_DOC"] = "False"
        cmake.definitions["JAS_ENABLE_PROGRAMS"] = "False"
        cmake.definitions["JAS_ENABLE_SHARED"] = "True" if self.options.shared else "False"
        cmake.definitions["JAS_LIBJPEG_REQUIRED"] = "REQUIRED"
        cmake.definitions["JAS_ENABLE_OPENGL"] = "False"
        cmake.configure(source_folder="jasper-version-%s" % self.version)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="jasper-version-%s/src/libjasper/include" % self.version)
        self.copy("*.h", dst="include", src="src/libjasper/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False, symlinks=True)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE", src="jasper-version-%s" % self.version)

    def package_info(self):
        self.cpp_info.libs = ["jasper"]
