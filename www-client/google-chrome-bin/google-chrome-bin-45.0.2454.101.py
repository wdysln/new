metadata = """
summary @ An attempt at creating a safer, faster, and more stable browser (Stable Channel)
homepage @ https://build.chromium.org
license @ BSD
src_url @ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/dbus-glib x11-libs/libXrender x11-libs/libXt x11-libs/libXmu x11-libs/gtk+:2 
          media-libs/alsa-lib net-print/cups
"""

standard_procedure = False


get("fdo_mime", "gnome2_utils")

def install():
    system("ar x %s/google-chrome-stable_current_amd64.deb" % src_cache)
    system("tar -xJf data.tar.xz -C %s/ --exclude=etc" % install_dir)

    
    copy("%s/opt/google/chrome/product_logo_48.png" % install_dir, "/usr/share/pixmaps/google-chrome.png")
    insfile("%s/eula_text.html" % filesdir, "/usr/share/licenses/google-chrome/eula_text.html")

    
def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()
