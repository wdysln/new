metadata = """
summary @ Perl HTML parser class
homepage @ http://search.cpan.org/dist/HTML-Parser
license @ LGPL
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/perl-HTML-Parser/HTML-Parser-3.68.tar.gz/5550b2da7aa94341f1e8a17a4ac20c68/HTML-Parser-3.68.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl dev-perl/HTML-Tagset
"""

def configure():
	pass

def build():
	system("perl Makefile.PL INSTALLDIRS=vendor")
	make()

def install():
	raw_install("DESTDIR=%s" % install_dir)

