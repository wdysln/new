metadata = """
summary @ SMB Fileserver and AD Domain server
homepage @ http://www.samba.org
license @ GPL3
src_url @ http://us1.samba.org/samba/ftp/stable/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ >=dev-db/sqlite-3.7 net-dns/libidn >=net-libs/gnutls-2.8.3
build @ dev-util/pkg-config net-dns/openldap dev-libs/libxslt app-arch/libarchive net-libs/gnutls dev-libs/libgpg-error
        dev-libs/popt sys-apps/dbus sys-libs/talloc sys-libs/pam app-text/docbook-xsl-stylesheets sys-apps/acl
"""
MODULES = "idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2,\
pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4,\
auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4"

def prepare():

    export("JOBS", get_env("JOBS").replace("-j", ""))

def configure():
    conf("--libdir=/usr/lib \
       --with-cachedir=/var/lib/samba \
       --with-configdir=/etc/samba \
       --with-lockdir=/var/lib/samba \
       --with-logfilebase=/var/log/samba \
       --with-modulesdir=/usr/lib/samba \
       --with-pammodulesdir=/usr/lib/security \
       --with-piddir=/run/samba \
       --with-privatedir=/var/lib/samba/private \
       --with-sockets-dir=/run/samba \
       --disable-rpath \
       --disable-rpath-install \
       --enable-fhs \
       --enable-gnutls \
       --nopyc \
       --nopyo \
       --with-acl-support \
       --with-ads \
       --with-automount \
       --with-cluster-support \
       --with-dnsupdate \
       --with-pam \
       --with-pam_smbpass \
       --with-quotas \
       --with-sendfile-support \
       --with-shared-modules=%s \
       --with-syslog \
       --with-utmp \
       --with-winbind \
      " % MODULES)
    
def build():
    make()
         
def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/*.service" % filesdir,"/usr/lib/systemd/system/")
    insfile("%s/*.socket" % filesdir,"/usr/lib/systemd/system/")
    insfile("%s/samba.conf.d" % filesdir,"/etc/conf.d/samba")
    insfile("%s/samba.conf" % filesdir,"/usr/lib/tmpfiles.d/samba.conf")
    
    insfile("%s/samba.logrotate" % filesdir,"/etc/logrotate.d/samba")
    insfile("%s/samba.pam" % filesdir,"/etc/pam.d/samba")

    
    insfile("packaging/LSB/smb.conf", "/etc/samba/smb.conf.default")
    
    makedirs("/var/spool/samba")
    makedirs("/etc/samba/private")
    setmod("1777", "%s/var/spool/samba" % install_dir)
    setmod("700", "%s/etc/samba/private" % install_dir)
    rmdir("%s/var/run" % install_dir)
     
def post_install():
    system("systemd-tmpfiles --create samba.conf")
    
