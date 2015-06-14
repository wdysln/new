metadata = """
summary @ A fast SQL database server
homepage @ https://www.mysql.com/products/community/
license @ GPL-2
src_url @ https://downloads.mariadb.com/archives/mysql-5.5/mysql-5.5.21.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-libs/openssl sys-libs/zlib
"""

get("main/cmake_utils")

def configure():
    makedirs("build")
    cd("build")
    export("CFLAGS", '-fPIC %s -fno-strict-aliasing -DBIG_JOINS=1 -fomit-frame-pointer' % get_env("CFLAGS"))
    export("CXXFLAGS", '-fPIC %s -fno-strict-aliasing -DBIG_JOINS=1 -felide-constructors -fno-rtti' % get_env("CXXFLAGS"))
    system("cmake %s -DCMAKE_BUILD_TYPE=Release" % build_dir,
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DSYSCONFDIR=/etc/mysql",
    "-DMYSQL_DATADIR=/var/lib/mysql",
    "-DMYSQL_UNIX_ADDR=/var/run/mysqld/mysqld.sock",
    "-DDEFAULT_CHARSET=utf8",
    "-DDEFAULT_COLLATION=utf8_general_ci",
    "-DENABLED_LOCAL_INFILE=ON",
    "-DINSTALL_INFODIR=share/mysql/docs",
    "-DINSTALL_MANDIR=share/man",
    "-DINSTALL_PLUGINDIR=/usr/lib/mysql/plugin",
    "-DINSTALL_SCRIPTDIR=bin",
    "-DINSTALL_INCLUDEDIR=include/mysql",
    "-DINSTALL_DOCREADMEDIR=share/mysql",
    "-DINSTALL_SUPPORTFILESDIR=share/mysql",
    "-DINSTALL_MYSQLSHAREDIR=share/mysql",
    "-DINSTALL_DOCDIR=share/mysql/docs",
    "-DINSTALL_SHAREDIR=share/mysql",
    "-DWITH_READLINE=ON",
    "-DWITH_ZLIB=system",
    "-DWITH_SSL=system",
    "-DWITH_LIBWRAP=OFF",
    "-DWITH_MYSQLD_LDFLAGS='%s'" % get_env('LDFLAGS'),
    "-DWITH_EXTRA_CHARSETS=complex",
    "-DWITH_EMBEDDED_SERVER=ON",
    "-DWITH_INNOBASE_STORAGE_ENGINE=1",
    "-DWITH_PARTITION_STORAGE_ENGINE=1",
    "-DWITHOUT_EXAMPLE_STORAGE_ENGINE=1",
    "-DWITHOUT_ARCHIVE_STORAGE_ENGINE=1",
    "-DWITHOUT_BLACKHOLE_STORAGE_ENGINE=1",
    "-DWITHOUT_FEDERATED_STORAGE_ENGINE=1")

def build():
    cd("build")
    make()

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)
    # What the fuck is that?
    insfile("%s/my.cnf" % filesdir, "/etc/my.cnf")
    insexe("%s/mysqld" % filesdir, "/etc/rc.d/mysqld")
    makedirs("/var/lib/mysql")

def post_install():
    setmod("700 /var/lib/mysql")
    system("groupadd -g 89 mysql")
    system("useradd -u 89 -g mysql -d /var/lib/mysql -s /bin/false mysql")
    system("/usr/bin/mysql_install_db --user=mysql --basedir=/usr")
    setowner("-R mysql:mysql /var/lib/mysql")
