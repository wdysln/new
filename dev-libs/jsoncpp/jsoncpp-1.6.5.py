metadata = """
summary @ A C++ library for interacting with JSON
homepage @ https://github.com/open-source-parsers/jsoncpp
license @ MIT
src_url @ https://github.com/open-source-parsers/jsoncpp/archive/1.6.5.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake
"""

get("main/cmake_utils")


def configure():
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
				-DCMAKE_INSTALL_PREFIX=/usr \
				-DBUILD_SHARED_LIBS=ON \
				-DBUILD_STATIC_LIBS=OFF")
