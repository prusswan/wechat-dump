#!/usr/bin/env python2
import javaobj

m = javaobj.JavaObjectUnmarshaller(open("CompatibleInfo.cfg"))
o = m.readObject()
print o.annotations[2]
