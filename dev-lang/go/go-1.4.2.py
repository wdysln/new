metadata = """
summary @  Compiler and tools for the Go programming language from Google
homepage @ http://golang.org/
license @ BSD
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name$version-src.tar.gz
	https://github.com/golang/$name/archive/go$version.tar.gz
arch @ ~x86_64
options @ debug threads
"""

#srcdir = "tcl8.5.9"

export("GOROOT", "%s/go-go1.4.2" % build_dir)
export("GOBIN", "$GOROOT/bin")
export("GOPATH", "%s" % build_dir)
export("GOROOT_FINAL", "/usr/lib/go")

export("GOOS","linux")
export("GOARCH","amd64")


def build():
  
    cd("src")
    system("bash make.bash")

    cd("go-go1.4.2")

    system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/godoc")
    system("$GOROOT/bin/go build -o $GOPATH/godoc golang.org/x/tools/cmd/godoc")

    for tool in ["cover", "vet", "callgraph"]:
        system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
        system("$GOROOT/bin/go build -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():  
    cd("go-go1.4.2")
    
    #dobin("bin/*")
    
    insexe("bin/*", "/usr/bin/")
    makedirs("/usr/lib/go")
    
    insinto("doc", "/usr/lib/go")
    insinto("include", "/usr/lib/go")
    insinto("lib", "/usr/lib/go")
    insinto("pkg", "/usr/lib/go")
    insinto("src", "/usr/lib/go")

  #  dodoc("VERSION", "LICENSE", "PATENTS", "README", "AUTHORS", "CONTRIBUTORS")