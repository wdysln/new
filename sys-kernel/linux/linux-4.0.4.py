metadata = """
summary @ Linux Kernel
homepage @ http://www.kernel.org/
license @ GPL2
src_url @ ftp://ftp.kernel.org/pub/linux/kernel/v4.x/$fullname.tar.xz       
arch @ ~x86_64
options @ sources headers
"""

depends = """
build @ sys-devel/bc app-arch/cpio app-text/docbook-xsl-stylesheets app-text/xmlto
"""


standard_procedure = False


def configure():
    copy("%s/config" % filesdir, ".config")

def build():
 #   make("mrproper")
   # make("headers_check")
   # copy("%s/config" % filesdir, ".config")
    make()

def install():
    notify("Installing modules...")
    make("INSTALL_MOD_PATH=%s/ DEPMOD=/bin/true modules_install mod-fw=" % install_dir)
    
    notify("Installing Libc headers...")
    make("INSTALL_HDR_PATH=%s/usr headers_install" % install_dir)
    
    notify("installing kernel as /boot/%s" % version)
    insfile("arch/x86/boot/bzImage", "/boot/kernel-%s" % version)
    
    
   # insfile("System.map", "/boot/System.map-%s" % version)
    insfile("System.map",  "/lib/modules/%s/System.map" % version)
    insfile("System.map",  "/usr/src/linux-headers-%s/System.map" % version)
    
    insfile("Module.symvers",  "/lib/modules/%s/Module.symvers" % version)
    insfile("Module.symvers",  "/usr/src/linux-headers-%s/Module.symvers" % version)
    

    

    pruned = ["include", "scripts", "Documentation"]
    wanted = ["Makefile*", "Kconfig*", "Kbuild*", "*.sh", "*.pl", "*.lds"]

    headersDirectoryName = "usr/src/linux-headers-%s" % version

    # Get the destination directory for header installation
    destination = os.path.join(install_dir, headersDirectoryName)
    makedirs(destination)

    # First create the skel
    find_cmd = "find . -path %s -prune -o -type f \( -name %s \) -print" % \
                (
                    " -prune -o -path ".join(["'./%s/*'" % l for l in pruned]),
                    " -o -name ".join(["'%s'" % k for k in wanted])
                ) + " | cpio -pVd --preserve-modification-time %s" % destination

    system(find_cmd)


    # Install remaining headers
    system("cp -a %s %s" % (" ".join(pruned), destination))

    # Cleanup directories
    system("rm -rf %s/scripts/*.o" % destination)
    system("rm -rf %s/scripts/*/*.o" % destination)
    system("rm -rf %s/Documentation/DocBook" % destination)
    
    system("rm -rf %s/var" % install_dir)
    
    system("rm -rf %s/lib/modules/%s/source" % (install_dir ,version))
    system("rm -rf %s/lib/modules/%s/build" % (install_dir ,version))
    
    

    # Finally copy the include directories found in arch/
 #   system("'(find arch -name include -type d -print | \
  #                      xargs -n1 -i: find : -type f)' | \
   #                     cpio -pd --preserve-modification-time %s" % destination)
  

    # Settle the correct build symlink to this headers
    makesym("/%s" % headersDirectoryName, "/lib/modules/%s/build" % version)
    makesym("build", "/lib/modules/%s/source" % version)

