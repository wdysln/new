metadata = """
summary @ Mesa 3-D graphics libraries and include files
homepage @ http://mesa3d.sourceforge.net/
license @ custom
src_url @ ftp://ftp.freedesktop.org/pub/$name/$version/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ x11-libs/libXdamage x11-libs/libXext x11-libs/libXfixes
        x11-libs/libXxf86vm x11-libs/libdrm sys-libs/talloc x11-proto/dri3proto
        x11-proto/glproto x11-libs/libXt x11-misc/makedepend x11-proto/presentproto x11-libs/libxshmfence

runtime @ x11-libs/libXdamage x11-libs/libXext x11-libs/libXfixes
        x11-libs/libXxf86vm x11-libs/libdrm sys-libs/talloc
        x11-proto/glproto x11-libs/libXt x11-misc/makedepend
"""

#srcdir = "mesa-%s" % version

def configure():
   
    conf("--with-dri-driverdir=/usr/lib/xorg/modules/dri",
            "--with-gallium-drivers=nouveau,svga,swrast",
            "--with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast",
            "--with-egl-platforms=x11,drm",
            "--disable-gallium-llvm",
            "--enable-gallium-egl", 
            "--enable-shared-glapi",
            "--enable-glx-tls",
            "--enable-dri",
            "--enable-glx",
            "--enable-osmesa",
            "--enable-gles1",
            "--enable-gles2",
            "--enable-egl",
            "--enable-texture-float",
            "--enable-xa")
			

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
