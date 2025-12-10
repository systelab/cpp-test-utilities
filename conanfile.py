from conan import ConanFile
from conan.tools.files import copy
import os

class TestUtilitiesInterfaceConan(ConanFile):
    name = "test-utilities-interface"
    description = "C++ Test Utilities interface"
    url = "https://github.com/systelab/cpp-test-utilities"
    homepage = "https://github.com/systelab/cpp-test-utilities"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "test", "utilities", "gtest")
    license = "MIT"

    package_type = "header-library"
    exports_sources = "*.h", "*.inl"

    def package(self):
        include_src = os.path.join(self.source_folder, "TestUtilitiesInterface")
        include_dst = os.path.join(self.package_folder, "include", "TestUtilitiesInterface")
        
        copy(self, "*.h", dst=include_dst, src=include_src)
        copy(self, "*.inl", dst=include_dst, src=include_src)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]