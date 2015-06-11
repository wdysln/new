metadata = """
summary @ Check for POD errors in files
homepage @ http://search.cpan.org/dist/Test-Pod
license @ GPL + PerlArtistic
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/perl-Test-Pod/Test-Pod-1.44.tar.gz/02380af5539521524d5df17273a57ae7/Test-Pod-1.44.tar.gz
arch @ ~x86_64
"""

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def install():
    raw_install("DESTDIR=%s" % install_dir)
