from conans import ConanFile


class TestUtilitiesInterfaceConan(ConanFile):
    name = "TestUtilitiesInterface"
    description = "C++ Test Utilities interface"
    url = "https://github.com/systelab/cpp-test-utilities"
    homepage = "https://github.com/systelab/cpp-test-utilities"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "test", "utilities", "gtest")
    license = "MIT"
    generators = "cmake_find_package"
    # No settings/options are necessary, this is header only
    exports_sources = "*"


    def package(self):
        self.copy("*.h", dst="include/TestUtilitiesInterface", src="TestUtilitiesInterface")
        self.copy("*.inl", dst="include/TestUtilitiesInterface", src="TestUtilitiesInterface")

    def package_info(self):
        self.info.header_only()
