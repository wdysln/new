metadata = """
summary @ An attempt at creating a safer, faster, and more stable browser (Stable Channel)
homepage @ https://build.chromium.org
license @ BSD
src_url @ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/dbus-glib x11-libs/libXrender x11-libs/libXt x11-libs/libXmu x11-libs/gtk+:2 
    media-libs/alsa-lib
build @ app-arch/unzip
"""

standard_procedure = False

#srcdir = "firefox"

get("fdo_mime", "gnome2_utils")

def install():
    makedirs("/usr/share/pixmaps")
    makedirs("/usr/share/applications")
    makedirs("/opt")
    
    insfile("%s/chrome/icons/default/default48.png" % build_dir, "/usr/share/pixmaps/%s.png" % name)
    insfile("%s/%s.desktop" % (filesdir, name), "/usr/share/applications/%s.desktop" % name)
    copytree(build_dir, "/opt/firefox")
    insexe("%s/google-chrome-bin" % filesdir, "/usr/bin/google-chrome-bin")

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()
