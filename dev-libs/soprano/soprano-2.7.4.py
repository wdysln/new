metadata = """
summary @ A library which provides a highly usable object-oriented C++/Qt4 framework for RDF data
homepage @ http://soprano.sourceforge.net/
license @ GPL + LGPL
src_url @ http://downloads.sourceforge.net/project/$name/Soprano/$version/$fullname.tar.bz2
arch @ ~x86_64
options @ clucene dbus raptor redland virtuoso doc
"""

depends = """
runtime @ x11-libs/qt
"""

opt_runtime = """
doc @ app-doc/doxygen
virtuoso @ dev-db/libiodbc
raptor @ media-libs/raptor:2.0
clucene @ dev-cpp/clucene-core
redland @ dev-libs/rasqal dev-libs/redland
"""

get("main/cmake_utils")

def configure():

    plusconfig = ""
    if not opt("clucene"):
        plusconfig += " -DSOPRANO_DISABLE_CLUCENE_INDEX=ON "
    if not opt("virtuoso"):
        plusconfig += " -DSOPRANO_DISABLE_VIRTUOSO_BACKEND=ON "
    if not opt("raptor"):
        plusconfig += " -DSOPRANO_DISABLE_RAPTOR_PARSER=ON "
    if not opt("redland"):
        plusconfig += " -DSOPRANO_DISABLE_RAPTOR_SERIALIZER=ON -DSOPRANO_DISABLE_REDLAND_BACKEND=ON "

    makedirs("build")
    cd("./build")
    cmake_conf("-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SKIP_RPATH=OFF",
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DSOPRANO_BUILD_TESTS=OFF",
    "-DSOPRANO_DISABLE_SESAME2_BACKEND=ON", plusconfig, sourcedir=build_dir)

def build():
    cd("build")
    make()

def install():
    cd("build")
    installd()
