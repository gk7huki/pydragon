#!/usr/bin/env python3

################################################################################
#
# Written by Huki, file inception on 2016-11-16.
# Adapted to python from: 
#   http://blog.cyclopsgroup.org/2009/11/project-euler-problem-220.html
#
################################################################################

import sys

degree = 12
if len(sys.argv) > 1:
  degree = int(sys.argv[1])

max_steps = 10**12
if len(sys.argv) > 2:
  max_steps = int(sys.argv[2])

substitute = {'F': 0, 'L': -1, 'R': 1}
expand = {'a': 'aRbFR', 'b': 'LFaLb'}
cache = {}

directions = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0 # initial direction
cursor = [0,0]
steps = 0

rotate = (
  lambda pos: [pos[0], pos[1]],
  lambda pos: [pos[1], -pos[0]],
  lambda pos: [-pos[0], -pos[1]],
  lambda pos: [-pos[1], pos[0]]
)

def save_path(start):
  end = [cursor, d, steps]
  up = (-start[1]) % 4
  start[0] = rotate[up](start[0])
  end[0] = rotate[up](end[0])
  for i in range(2):
    end[0][i] -= start[0][i]
  end[1] = (end[1] - start[1]) % 4
  end[2] -= start[2]
  return end

def apply_path(end):
  end[0] = rotate[d](end[0])
  for i in range(2):
    end[0][i] += cursor[i]
  end[1] = (d + end[1]) % 4
  end[2] += steps
  return end

def traverse(string, level):
  global cursor, d, steps
  for c in string:
    if c in substitute:
      turn = substitute[c]
      if turn == 0:
        for i in range(2):
          cursor[i] += directions[d][i]
        steps += 1
        print(cursor[0], cursor[1])
      else:
        d = (d + turn) % 4
    else:
      if level < degree:
        key = c + str(level)
        if key in cache:
          if (steps + cache[key][2]) <= max_steps:
            cursor, d, steps = apply_path(cache[key][:])
            print(cursor[0], cursor[1])
          else:
            traverse(expand[c], level+1)
        else:
          start = [cursor[:], d, steps]
          traverse(expand[c], level+1)
          cache[key] = save_path(start)
    if steps == max_steps:
      return

print(cursor[0], cursor[1])
traverse('Fa', 0)
