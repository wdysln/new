metadata = """
summary @ Expat-based XML parser module for perl
homepage @ http://search.cpan.org/dist/XML-Parser
license @ GPL PerlArtistic
src_url @ http://cpan.org/CPAN/authors/id/C/CH/CHORNY/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl dev-libs/expat
"""

def configure():
    export("PERL_MM_USE_DEFAULT", "1")
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def build():
    make()
    make("test")
    
install = lambda: (linstall())

