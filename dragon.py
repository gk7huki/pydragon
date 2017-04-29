#!/usr/bin/env python3

################################################################################
#
# Written by Huki, file inception on 2016-11-16.
# Adapted from: 
#   https://www.reddit.com/r/dailyprogrammer/comments/3dl9wr/20150717_challenge_223_hard_the_heighway_dragon/cu2u6uo/
#
################################################################################

import sys

def heighway_sequence(degree):
  if degree == 1:
    return [1]
  else:
    left = heighway_sequence(degree-1)
    right = [-turn for turn in left[::-1]]
    return left + [1] + right

def heighway(degree):
  dirs = [(0,1), (1,0), (0,-1), (-1,0)]
  d = 0 # initial direction
  cursor = (0,1)
  yield (0,0)
  yield cursor
  for turn in heighway_sequence(degree):
    d = (d + turn) % 4
    cursor = (cursor[0]+dirs[d][0], cursor[1]+dirs[d][1])
    yield cursor

degree = 12
if len(sys.argv) > 1:
  degree = int(sys.argv[1])

for p in heighway(degree):
  print(p[0], p[1])
