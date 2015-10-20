metadata = """
summary @ Perl Archive::Zip module
homepage @ http://search.cpan.org/dist/${_realname}/
license @ PerlArtistic GPL2
src_url @ http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/Archive-Zip-$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/perl
"""

srcdir = "Archive-Zip-%s" % version

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)
