metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
src_url @ https://github.com/wdysln/new/raw/9cc85f724ac144d1e753f6ab0ca46fd77eb99331/sys-apps/lpms/lpms-1.0.tar.xz
license @ GPL-3
arch @ ~x86_64
"""

# TODO: lpms uses python-file to handle mime types now. So we can remove sys-apps/file dependency

depends = """
runtime @ dev-lang/python[xml,threads]:2.7 net-misc/wget sys-apps/file 
common @ dev-lang/python[xml,threads]:2.7 
"""
srcdir = "lpms-1.0"

standard_procedure = False

reserve_files = ["/etc/lpms/build.conf", "/etc/lpms/repo.conf"]


def install():
    install_path = "/usr/lib/hadron/python/lpms"

    makedirs(install_path)
    insinto("%s/lpms/*" % build_dir, install_path)
    copytree("%s/bin/" % build_dir, install_path+"/../")

    makesym("../lib/hadron/python/bin/lpms", "/usr/bin/lpms")
    makesym("../lib/hadron/python/bin/merge-conf", "/usr/bin/merge-conf")

    makedirs("/etc/lpms")
    insinto("%s/data/*" % build_dir, "/etc/lpms")
    insfile("%s/revdep-rebuild" % filesdir, "/usr/bin/revdep-rebuild")
    
    
    for directories in ('/var/db/lpms', '/var/cache/lpms/sources',
            '/var/tmp/lpms', '/var/lib/lpms', '/var/tmp/merge-conf',
            '/etc/lpms/user'):
        makedirs(directories)

    user_readme = """
    # this is the directory for fucking with options like 'app-editors/nano nls'
    # the files that you can define 
    # * lock
    # * unlock
    # * options
    # * ldflags
    # * cflags
    # * cxxflags 
    """
    
    echo(user_readme, "/etc/lpms/user/README")


    insdoc("COPYING", "AUTHORS", "README", "TODO", "VERSION") 
    
def post_install():
    system("/bin/chmod u+x /usr/bin/revdep-rebuild")