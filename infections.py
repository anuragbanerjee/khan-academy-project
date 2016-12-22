#!/usr/bin/env python

'''
Khan Academy Interview 1 (project)
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

There are 2 types of infection implemented here: total and limited. A
short description for exact infection is provided too.

'''

from User import User
import time

def total_infection(user, new_version = 1):
  # infect the user
  if user.site_version == new_version:
    return
  else:
    user.site_version = new_version

  # infect user's students
  for student in user.students:
    print user.name + " infects " + student.name + "."
    total_infection(student, new_version)

  # infect user's teacher, if any
  if user.teacher != None and user.teacher.site_version != new_version:
    print user.name + " infects " + user.teacher.name + "."
    total_infection(user.teacher, new_version)

def limited_infection(target, new_version = 1):
  masters = sorted(User._masters, key=lambda m: m.influence)
  total = 0
  cursor = 0
  while cursor < len(masters):
    total += masters[cursor].influence
    total_infection(masters[cursor])
    if masters[cursor].influence == 1:
      print "{} is infected.".format(masters[cursor].name)
    if (target) < total:
      break
    cursor += 1

def exact_infection(user, limit,  new_version = 1):
  # Use influence scores from User._masters in a subset-sum problem.
  pass






