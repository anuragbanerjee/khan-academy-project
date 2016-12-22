# Khan Academy: Infection

## Instructions

Before running, make sure you have Python 2.7. There are no dependencies for you to install. Best tested on macOS Sierra (10.12.1). To run the test case provided: run `python test.py`. This will run through an infection and generate the visualization data. To view the visualization, just run the following.

```
cd html
python -m SimpleHTTPServer
open http://localhost:8000
```

## Prompt

Requirements

- [x] **Total Infection**: given a node, infect everybody in the connected component.
- [x] **Limited Infection**: infect to a given target of users


Extras

+ [x] **Visualization**: visualize the relations between users and the infection’s spread
+ [ ] **Exact Infection**: limited infection for an EXACT number of users
+ [ ] **Custom Enhancement**: something else

## Process

First, I used pen and paper to outline a possible User model, since that's what any infection would center around. I found the words coach and student to be strange, so I renamed coach to teacher. You can identify a teacher if that user does not have a teacher but has at least 1 student. I wrote out a several test data users (users.csv)  and dummy relations between them (relations.csv). I included as many use cases I could think of: individual learners, classrooms, small groups, and circular dependencies. With these two files ready, I could develop and test my algorithms.

### Total Infection

My approach was a Depth-First Traversal. Thinking a real-world use case, most likely there wouldn't be many "levels" of coaching. More often, it'll be a teacher and a class of students. In the end, it wouldn't matter too much since the entire component would have to be infected anyways. For any given user, a total infection does the following recursively:

1. infect the user
2. infect the user's students
3. infect the user's teacher

### Limited Infection

This was the hardest to implement, simply because there were a lot of possible ways to distribute the infection. Should individual leaners be prioritized? Classroom? A balance of both? I decided that since the overall goal is to A/B test or introduce a feature, then it should make sense to increment as little as possible to make sure large swaths of people don't get a buggy version. It seems that the persona for large components would be classrooms, and so there's more on the line and that neccessitates a more refined version of the site for doing their job.

### Extra: Visualization

I made a simple visualization of the network graph. To do this, I converted my node and edge data after the infection into an GEXF file, which is an open-source standard for describing graphs. Then, I used Sigma.js to fetch and parse the GEXF files and display the graph. It was especially difficult figuring out how to algorithmically layout the nodes on the graph, but I discovered the [Force Atlas 2 layout algorithm](http://webatlas.fr/tempshare/ForceAtlas2_Paper.pdf) and used it for my node layouts, so they look much more readable. In the visualization, gray represents "uninfected" users and red represents "infected" users. You can find the code for that in the html folder.

## Gotchas

- Circular Dependencies among Student/Teacher relationships will throw an error, halt execution, and declare the data as invalid. Self-coaching relations would fall under this umbrella. Realistically, there would be some checking mechanism to make sure the data doesn't end up with one.
- Running the visualization by directly running `html/index.html` may not work. Because of security policies in certain browsers (to prevent cross-site scripting), you need to either:
    - start a server in the html folder using `python -m SimpleHTTPServer` and access it at `http://localhost:8000` (preferably with Chrome)
    - or use a browser with a more relaxed Same-Origin Policy
