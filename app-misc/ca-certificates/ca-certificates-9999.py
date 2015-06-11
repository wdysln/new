metadata = """
summary @ Common ca-certificates
homepage @ http://packages.qa.debian.org/c/ca-certificates.html
license @ MPL
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash dev-libs/openssl sys-apps/debianutils
          sys-apps/findutils sys-apps/coreutils sys-apps/sed
"""
standard_procedure = False



def prepare():
	for i in ("make-ca.sh","build_certs.sh","make-cert.pl","remove-expired-certs.sh"):
		system("cp %s/%s" % (filesdir, i), "%s" % i)
		system("chmod u+x %s"% i)
		 


def build():
    system ("./build_certs.sh")
    
def install():
    insinto("certs/*.pem", "/etc/ssl/certs")
	 
	#insinto ("BLFS-ca-bundle*.crt", "ca-certificates.crt", "/etc/ssl/certs") 
    insfile("BLFS-ca-bundle*.crt", "/etc/ssl/certs/ca-certificates.crt")
    
def post_install():
    system("c_rehash")




