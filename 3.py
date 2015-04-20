#!/usr/bin/env python

from math import *

def i321():
  n = 0L
  mn = 0L
  tn = 0L
  sn = 0L
  n3 = 0L
  n9 = 0L

  n = 372889431
  mn = 139046528497282623

  tn = 1L + 8L * mn

  print "M(%i) = %i\n" % (n, mn)
  print "sqrt(%d) = %i\n" % (n, sqrt(n))
  print "sqrt(%d) = %i\n" % (tn, sqrt(tn))
  print "sqrt(%i) mod 1 = %i\n" % (tn, sqrt(tn) % 1)
  print "%i mod 3 = %i\n %i mod 9 = %i\n" % (mn, mn % 3L, mn, mn % 9L) 

i321()
