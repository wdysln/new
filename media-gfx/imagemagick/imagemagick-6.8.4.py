metadata = """
summary @ A collection of tools and libraries for many image formats
homepage @ http://www.imagemagick.org/
license @ custom
src_url @ http://ftp.sunet.se/pub/multimedia/graphics/ImageMagick/ImageMagick-6.8.4-6.tar.xz
arch @ ~x86_64
options @ bzip2 fontconfig jpeg lcms perl png svg tiff truetype X xml lzma zlib static-libs
"""

depends = """
runtime @ media-libs/fontconfig media-libs/freetype media-libs/jpeg media-libs/libpng dev-libs/libxml2 gnome-base/librsvg
"""


srcdir = "ImageMagick-%s-6" % raw_version

def configure():
    conf("--with-modules",
            config_enable("static-libs", "static"),
            "--enable-openmp",
            "--with-wmf",
            "--with-gslib",
            "--with-gs-font-dir=/usr/share/fonts/Type1",
            '--with-perl-options="INSTALLDIRS=vendor"',
            "--without-gvc",
            "--without-djvu",
            "--without-autotrace",
            "--with-jp2",
            "--without-jbig",
            "--without-x",
            "--without-fpx",
            "--without-dps",
            "--without-fftw",
            "--with-magick-plus-plus",
            "--without-lcms")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE", "NOTICE", "AUTHORS.txt", "ChangeLog", "NEWS.txt")
