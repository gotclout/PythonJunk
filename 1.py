#!/usr/bin/env python

MAX_TRI = 999999L

triangles = []

def next_pos(mn, pos):
  if mn > triangles[MAX_TRI - 1]:
    return -1
  else:
    maxv = MAX_TRI - 1
    minv = 0
    mid = minv + (maxv - minv) / 2
    while triangles[mid] != mn and minv < maxv:
      if triangles[mid] < mn :
        minv = mid + 1
      else :
        maxv = mid - 1
      mid = minv + (maxv - minv) / 2
  return mid

def gen_triangles(offset):
  triangles[:] = []
  i = 1L + offset * MAX_TRI
  bound = i + MAX_TRI
  print "Generating %i through %i " % (i, bound)
  while i <= bound:
    triangles.append((i * (i + 1L)) / 2L)
    i += 1L
  print "Max value = %i " % (triangles[MAX_TRI - 1])

def pe321():
  offset = 0L
  n      = 1L

  gen_triangles(offset)
  offset = total = count = mn = 0L
  n = 1L
  while count < 41:
    mn = 2L * n + n * n
    while mn % 3 != 0 and mn % 9 != 1:
      n += 1L
      mn = 2L * n + n * n
    pos = next_pos(mn, pos)
    if pos == -1 :
      offset += 2L
      gen_triangles(offset)
      pos = 0L
    if mn == triangles[pos]:
      count += 1L
      total += n
      print "M(%i) = %i is triangular" % (n, mn)
      n += 1L;
    else:
      n += 1L
  print "The sum of the first %i terms = %i" % (count, total)

pe321()
