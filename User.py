#!/usr/bin/env python

'''
Khan Academy Interview 1 (project)
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.
'''

class User(object):
  _all = []
  _masters = set()

  def __init__(self, name):
      super(User, self).__init__()
      self.id = len(type(self)._all)
      self.name = name
      self.site_version = 0
      self.students = set()
      self.teacher = None
      self.influence = 1
      type(self)._all.append(self)
      type(self)._masters.add(self)

  def teaches(self, user):
    '''
    INPUT: a User object
    OUTPUT: none

    This set the properties of 2 User objects to have a teacher-student
    relationship. The input User will be the student. It triggers an update to
    the influence for the entire connected component.
    '''
    if len(user.students) > 0:
      raise ValueError()
    if user.teacher == None:
      type(self)._masters.remove(user)
    user.teacher = self
    self.students.add(user)

    master = self.get_master()
    master.influence += 1
    master.propogate_influence()

  def get_master(self):
    '''
    A master is the top-most node of the component. This method recursively
    traverses the component until it finds that user. Realistically, most users
    will not be more than a couple layers deep.
    '''
    if self.teacher == None:
      return self
    else:
      return self.teacher.get_master()

  def propogate_influence(self):
    '''
    This keeps the component's total infection count potential in sync. So, it
    is easy to predict how many people any given User can infect.
    '''
    self.influence = self.get_master().influence
    for s in self.students:
      s.propogate_influence()

  @staticmethod
  def find(id):
    '''
    INPUT: id for a User object
    OUTPUT: User object matching the id
    '''
    return User._all[id]

  def __str__(self):
    t = self.teacher
    if t == None:
      t = "none"
    else:
      t = t.name
    return "Name: {}\nTeacher:{}\nStudents:{}\nInfluence: {}\n".format(self.name, t, [x.name for x in self.students], self.influence)