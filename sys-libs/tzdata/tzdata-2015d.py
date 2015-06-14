metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzdata2015d.tar.gz
arch @ ~x86_64
"""

standard_procedure = False


Components = ["etcetera", "southamerica", "northamerica", "europe", "africa", "antarctica", \
              "asia", "australasia", "backward", "pacificnew", "solar87", "solar88", "solar89", \
              "systemv" ]

#ExtraDist = ["zone.tab", "iso3166.tab"]
   


def install():
    copy("%s/yearistype.sh" % filesdir, "yearistype.sh")
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo %s" % (install_dir ,Components))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/posix %s"  % (install_dir ,Components))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/right -L leapseconds %s" % (install_dir ,Components))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/right -L leapseconds %s" % (install_dir ,Components))
    
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo -p America/New_York" % install_dir)
    
    
