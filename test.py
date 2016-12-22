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

import os

users = []

def visualize():
  nodes = []
  for u in User._all:
    t = u.teacher.id if u.teacher != None else u.id
    s = len(User.find(t).students)
    node = {
      "name": u.name,
      "infected": u.site_version == 1
    }
    nodes.append(node)
    os.system("cd html; python -m SimpleHTTPServer & open http://localhost:8000")

  edges = []
  with open("data/relations.csv") as f:
    for line in f:
      userId1, userId2 = line.strip().split(",")
      edges.append((int(userId1) -1, int(userId2) -1))

  gexf = generate_GEXF(nodes, edges)
  with open("html/data/main.gexf", "w") as f:
    f.write(gexf)

def main():
  # creates dummy users and student-teacher connections
  with open("data/users.csv") as f:
    for name in f:
      users.append(User(name.strip()))

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

  # configure starting point for infection and validate input
  print "\nEnter ID of first User to infect: ",
  starting_point = raw_input()
  while(True):
    if starting_point.isdigit():
      starting_point = int(starting_point)
      if starting_point >= 0 and starting_point < len(User._all):
        break
    print "Invalid input. Please enter a number between {} and {}: ".format(0, len(User._all) - 1),
    starting_point = raw_input()
  starting_point = users[starting_point]


  print "Infection Limit (leave blank for total infection): ",
  infection_limit = raw_input()
  while(True):
    # configure for total infection
    if infection_limit == "":
      infection_limit = len(User._all)
      break

    # configure for limited infection
    if infection_limit.isdigit():
      infection_limit = int(infection_limit)
      if infection_limit >= 0 and infection_limit <= len(User._all):
        break

    # retry if invalid input
    print "Invalid input. Please enter nothing or a number between {} and {}: ".format(0, len(User._all)),
    infection_limit = raw_input()

  print "\n--- INFECTION BEGINS ---"
  if infection_limit == len(User._all):
    total_infection(starting_point)
  else:
    limited_infection(starting_point, infection_limit, 5)

  print "\n--- REPORT ---"
  print "Out of {} total users, {} of them were infected.".format(
    len(User._all),
    sum([p.site_version for p in User._all])
  )

  visualize()

if __name__ == '__main__':
  main()