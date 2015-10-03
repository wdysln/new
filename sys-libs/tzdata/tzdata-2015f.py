metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzdata2015f.tar.gz
arch @ ~x86_64
"""

standard_procedure = False


timezones = ["etcetera", "southamerica", "northamerica", "europe", "africa", "antarctica", \
              "asia", "australasia", "factory", "backward", "pacificnew", \
              "systemv" ]

def install():
    makedirs("/usr/share/zoneinfo/right")
    makedirs("/usr/share/zoneinfo/posix")
    cd("..")
    
    for tz in timezones:
        cmd = "zic -L /dev/null -d %s/usr/share/zoneinfo -y ./yearistype.sh %s" %(install_dir, tz)
        system(cmd)
        part2 = "zic -L /dev/null -d %s/usr/share/zoneinfo/posix -y ./yearistype.sh %s" %(install_dir, tz)
        system(part2)
        part3 = "zic -L leapseconds -d %s/usr/share/zoneinfo/right -y ./yearistype.sh %s"%(install_dir, tz)
        system(part3)

        # Default DST # ln -sf /usr/share/zoneinfo/Asia/Calcutta localtime
        system ("zic -d %s/usr/share/zoneinfo -p America/New_York" % install_dir)
        
        insfile("zone.tab", "/usr/share/zoneinfo/zone.tab")
        insfile("iso3166.tab", "/usr/share/zoneinfo/iso3166.tab")