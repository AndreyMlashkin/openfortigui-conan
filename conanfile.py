from conans import ConanFile, CMake, tools
from conan.tools.scm import Version, Git

class OpenfortiguiConan(ConanFile):
    name = "openfortigui"
    license = "GPLv3"
    author = "rene@hadler.me"
    url = "https://github.com/theinvisible/openfortigui"
    description = "VPN-GUI to connect to Fortigate-Hardware, based on openfortivpn"
    topics = ("VPN")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake", "cmake_find_package_multi"

    def set_version(self):
        git = Git(self, folder=self.recipe_folder)
        self.version = git.run("describe --always --tags --abbrev=9")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def export_sources(self):
        self.copy("*")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def requirements(self):
        self.requires('qt/5.15.10')
        self.options["qt"].with_dbus = True

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

