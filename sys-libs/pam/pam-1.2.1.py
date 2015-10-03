metadata = """
summary @ Pluggable Authentication Modules
homepage @ http://www.kernel.org/pub/linux/libs/pam/
license @ GPL-2
src_url @ http://linux-pam.org/library/Linux-PAM-$version.tar.bz2
arch @ ~x86_64
options @ berkdb cracklib debug nls nis
"""

depends = """
runtime @ sys-libs/glibc sys-devel/flex
"""

opt_runtime = """
cracklib @ sys-libs/cracklib
berkdb @ sys-libs/db
"""

def configure():
    cd("../Linux-PAM-%s" % raw_version)
    patch(level=1)
    conf("--enable-dependency-tracking",
            "--enable-shared",
            config_enable("nls"),
            config_enable("nis"),
            config_enable("debug"),
            config_enable("berkdb", "db"),
            config_enable("cracklib"),
            "--disable-prelude")
    

build = lambda: (cd("../Linux-PAM-%s" % raw_version), make())

def install():
    cd("../Linux-PAM-%s" % raw_version)
    raw_install("DESTDIR=%s SCONFIGDIR=/etc/security" % install_dir)
    insfile("%s/other" % filesdir, "/etc/pam.d/other")

    insdoc("CHANGELOG", "ChangeLog", "README", "AUTHORS", "Copyright", "NEWS")

    setmod("4755", "%s/sbin/unix_chkpwd" % install_dir)
    
    for i in ('other', 'system-auth', 'system-local-login', 'system-login', 'system-services', 'system-remote-login'):
        insfile("%s/%s" % (filesdir, i), "/etc/pam.d/%s" % i)
    
    cd("/usr/lib/security")
    makesym("pam_unix.so", "/usr/lib/security/pam_unix_acct.so")
    makesym("pam_unix.so", "/usr/lib/security/pam_unix_auth.so")
    makesym("pam_unix.so", "/usr/lib/security/pam_unix_passwd.so")
    makesym("pam_unix.so", "/usr/lib/security/pam_unix_session.so")