metadata = """
summary @ Meta package for XFCE desktop
homepage @ http://www.xfce.org/
license @ GPL-2
arch @ ~x86_64
"""

depends = """
build @ dev-perl/XML-Parser x11-base/xorg-server
runtime @ >=xfce-base/xfwm4-4.9 >=xfce-extra/xfce4-appfinder-4.9 >=xfce-base/xfdesktop-4.9 >=xfce-base/xfce4-session-4.9  
		  xfce-base/thunar xfce-base/xfce4-settings 
postmerge @ x11-terms/xfce4-terminal xfce-extra/xfce4-mixer dev-util/geany sys-fs/ntfs_3g 
			sys-fs/udisks sys-power/upower sys-auth/polkit-gnome gnome-base/gvfs lxde-base/lxdm
			x11-themes/faenza-icon-theme x11-themes/xfce-theme-greybird	lxde-base/lxdm xfce-extra/thunar-volman
"""

standard_procedure = False
