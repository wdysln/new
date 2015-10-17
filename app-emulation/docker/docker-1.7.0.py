metadata = """
summary @  Compiler and tools for the Go programming language from Google
homepage @ http://golang.org/
license @ BSD
src_url @ https://github.com/docker/docker/archive/v1.7.0.tar.gz
arch @ ~x86_64
options @ debug threads
"""

#srcdir = "%s-%s%s" % (name ,name, version)

depends = """
runtime @ sys-libs/glibc net-misc/bridge-utils 
build @ sys-fs/btrfs-progs dev-lang/go sys-fs/lvm 
        dev-vcs/git sys-apps/iproute2
"""

standard_procedure = False

def prepare():
    export("AUTO_GOPATH", "1")
    export("DOCKER_GITCOMMIT", "786b29d") 
    export("GOPATH", "%s/" % build_dir)
    export("CGO_CFLAGS", "-I/usr/include")
    export("CGO_LDFLAGS", "-L/usr/lib")
    export("DOCKER_BUILDTAGS","exclude_graphdriver_aufs")
    export("DOCKER_INITPATH", "/usr/lib/docker/dockerinit")

def build():
    system("./hack/make.sh dynbinary")


def install():  
    
    insexe("bundles/1.7.0/dynbinary/docker","/usr/bin/")
    insexe("bundles/1.7.0/dynbinary/docker-1.7.1","/usr/bin/")
    insexe("bundles/1.7.0/dynbinary/dockerinit", "/usr/libexec/dockerinit")
    insexe("bundles/1.7.0/dynbinary/dockerinit-1.7.1", "/usr/libexec/dockerinit-1.7.0")

    insinto("contrib/init/systemd/docker.service", "/usr/lib/systemd/system")
    insinto("contrib/init/systemd/docker.socket", "/usr/lib/systemd/system")
    insinto("%s/docker.conf" % filesdir ,"/usr/lib/sysusers.d")

def post_install():
    system("systemd-sysusers docker.conf")


    #dodoc("VERSION", "LICENSE", "README.md", "AUTHORS", "CONTRIBUTING.md", "CHANGELOG.md", "NOTICE")
    

