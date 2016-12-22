#!/usr/bin/env python

'''
Khan Academy Interview 1 (project)
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python test.py`

'''

from infections import total_infection, limited_infection
from exporter import generate_GEXF
from User import User

def visualize():
  '''
  Gathers data about nodes and edges to make a GEFX file, and launches
  a visualization of the entire graph.
  '''
  nodes = []
  for u in User._all:
    t = u.teacher.id if u.teacher != None else u.id
    s = len(User.find(t).students)
    node = {
      "name": u.name,
      "infected": u.site_version == 1
    }
    nodes.append(node)

  edges = []
  with open("data/relations.csv") as f:
    for line in f:
      userId1, userId2 = line.strip().split(",")
      edges.append((int(userId1) -1, int(userId2) -1))

  gexf = generate_GEXF(nodes, edges)
  with open("html/data/main.gexf", "w") as f:
    f.write(gexf)

def get_infection_type():
  print "\nEnter 1 for total infection or 2 for limited infection: ",
  while(True):
    infection_type = raw_input()
    if infection_type == "1":
      return "TOTAL"
    if infection_type == "2":
      return "LIMITED"
    print "Invalid input. Please enter a 1 or a 2: ",

def get_infection_limit():
  print "\nAbout many people should be infected? ",
  while(True):
    infection_limit = raw_input()
    if infection_limit.isdigit():
      infection_limit = int(infection_limit)
      if 1 <= infection_limit and infection_limit <= len(User._all):
        return infection_limit
    print "Invalid input. Please enter a number between {} and {}: ".format(
      0, len(User._all) - 1
    ),

def get_starting_point():
  print "\nEnter the ID of the user to begin infection: ",
  while(True):
    starting_point = raw_input()
    if starting_point.isdigit():
      starting_point = int(starting_point)
      if 0 < starting_point and starting_point < len(User._all):
        return User.find(starting_point)
    print "Invalid input. Please enter a number between {} and {}: ".format(
      0, len(User._all) - 1
    ),


def main():
  # creates dummy users and student-teacher connections
  with open("data/users.csv") as f:
    for name in f:
      User(name.strip())

  with open("data/relations.csv") as f:
    for line in f:
      userId1, userId2 = line.strip().split(",")
      user1 = User.find(int(userId1) - 1)
      user2 = User.find(int(userId2) - 1)
      try:
        user1.teaches(user2)
      except ValueError as e:
        print "User relations file is invalid. Circular dependency detected."
        exit(1)

  print "--- SET UP ---"

  # display all user & their IDs
  print "ID\t|\tNAME"
  print "-----------------------"
  for i in User._all:
    print "{}\t|\t{}".format(i.id, i.name)

  print "\n--- INFECTION BEGINS ---"
  infection_type = get_infection_type()
  if infection_type ==  "TOTAL":
    total_infection(get_starting_point())
  else:
    limited_infection(get_infection_limit(), 5)

  print "\n--- REPORT ---"
  print "Out of {} total users, {} of them were infected.".format(
    len(User._all),
    sum([p.site_version for p in User._all])
  )

  visualize()

if __name__ == '__main__':
  main()