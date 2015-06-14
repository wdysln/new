metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzdata2015d.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

timezones=('africa' 'antarctica' 'asia' 'australasia'
           'europe' 'northamerica' 'southamerica'
           'pacificnew' 'etcetera' 'backward'
           'systemv' 'factory')


   
    
def install():
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo %s" % (install_dir ,timezones))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/posix %s"  % (install_dir ,timezones))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/right -L leapseconds %s" % (install_dir ,timezones))
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo/right -L leapseconds %s" % (install_dir ,timezones))
    
    system("zic -y ./yearistype -d %s/usr/share/zoneinfo -p America/New_York" % install_dir)
    #  install -m444 -t ${pkgdir}/usr/share/zoneinfo iso3166.tab zone1970.tab zone.tab 
   
