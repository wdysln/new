metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzdata2015d.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

ZoneDir = "/usr/share/zoneinfo"
TargetDir = "%s/%s" % (install_dir, ZoneDir)

RightDir = "%s/right" % TargetDir
PosixDir = "%s/posix" % TargetDir


Components = ["etcetera", "southamerica", "northamerica", "europe", "africa", "antarctica", \
              "asia", "australasia", "backward", "pacificnew", "solar87", "solar88", "solar89", \
              "systemv" ]

ExtraDist = ["zone.tab", "iso3166.tab"]

def build():
    copy("%s/yearistype.sh" % filesdir, "yearistype.sh")
    makedirs("ZoneDir")
    makedirs("RightDir")
    makedirs("PosixDir")


def install():
    for extra in ExtraDist:
       insinto(ZoneDir, extra)

    for tz in Components:
        cmd = "zic -L /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (TargetDir, get.workDIR(), tz)
        system (cmd)
        part2 = "zic -L /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (PosixDir, get.workDIR(), tz)
        system (part2)
        part3 = "zic -L leapseconds -d %s -y \"%s/yearistype.sh\" %s" % (RightDir, get.workDIR(), tz)
        system (part3)

    system ("zic -d %s -p Europe/Istanbul" % TargetDir)
    
    
