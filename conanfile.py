from conan import ConanFile
from conan.tools.files import copy

import os

class QtConan(ConanFile):
    name = "qt"
    settings = "os"

    def package_info(self):
        root_path = os.path.join(os.getenv("QT_BINARY_ROOT"), self.version)
        if self.settings.os == "Macos":
            root_path = os.path.join(root_path, "macos")
        elif self.settings.os == "Windows":
            root_path = os.path.join(root_path, "msvc2019_64")
        else:
            raise Exception(f"Not supported OS: {self.settings.os}")

        if not os.path.exists(root_path):
            raise Exception(f"QT_BINARY_ROOT not found: {root_path}")

        self.env_info.path.append(os.path.join(root_path, "bin"))
        self.cpp_info.includedirs = [os.path.join(root_path, "include")]
        self.cpp_info.bindirs = [os.path.join(root_path, "bin")]
        self.cpp_info.builddirs = [root_path]
