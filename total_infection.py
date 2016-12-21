#!/usr/bin/env python

'''
Khan Academy Interview 1 (project)
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python total_infection.py`

'''
class User(object):
  population = 0

  def __init__(self, name):
      super(User, self).__init__()
      self.name = name
      self.site_version = 0
      self.students = set()
      self.teacher = None
      User.population += 1

  def teaches(self, user):
    user.teacher = self
    self.students.add(user)

  def learn_from(self, user):
    self.teacher = user
    user.students.add(self)

  def drop_out(self):
    self.teacher = None

  def pivot_career(self):
    for s in self.students:
      drop_out(s)

  def is_teacher(self):
    return self.students > 0

  def infect(self, new_version):
    if self.site_version == new_version:
      return
    self.site_version = new_version
    for s in self.students:
      print self.name + " infected " + s.name
      s.infect(new_version)
    if self.teacher != None and self.teacher.site_version != new_version:
      print self.name + " infected " + self.teacher.name
      self.teacher.infect(new_version)

def main():
  rick = User("rick")
  morty = User("morty")
  jim = User("jim")
  pam = User("pam")
  dwight = User("dwight")
  angela = User("angela")
  kevin = User("kevin")
  oscar = User("oscar")
  eddie = User("eddie")
  michael = User("michael")
  kelly = User("kelly")
  hodor = User("hodor")

  people = [rick, morty, jim, pam, dwight, angela, kevin, oscar, eddie, michael, kelly, hodor,]

  jim.teaches(dwight)
  dwight.teaches(angela)
  angela.teaches(kelly)
  dwight.teaches(kevin)
  dwight.teaches(oscar)
  oscar.teaches(morty)
  jim.teaches(eddie)
  jim.teaches(michael)

  pam.teaches(rick)

  starting_point = jim
  site_version = 1

  b = 0
  for p in people:
    b += p.site_version

  starting_point.infect(site_version)

  a = 0
  for p in people:
    a += p.site_version
  print "---\nbefore: {} infections\nafter: {} infections\ntotal possible: {}".format(b, a, User.population * site_version)

if __name__ == '__main__':
  main()