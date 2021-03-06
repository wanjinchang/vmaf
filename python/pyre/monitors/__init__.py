#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


# timers
def timingCenter():
    from TimingCenter import timingCenter
    return timingCenter()


def timer(name):
    return timingCenter().timer(name)


# version
__id__ = "$Id: __init__.py,v 1.1.1.1 2006-11-27 00:10:05 aivazis Exp $"

#  End of file 
