#!/usr/bin/env python

'''
Khan Academy Interview 1 (project)
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

This generates GEXF-compliant XML. GEXF (Graph Exchange XML Format) is a
language for describing complex networks structures, their associated data and
dynamics. https://gephi.org/gexf/format/ This data is sent to Sigma.js to
interpret into an interactive graph.

'''

def generate_GEXF(node_data, edge_data):
    nodes_template = '''
                <node id="{}" label="{}">
                    <viz:color {}/>
                    <viz:position x="{}" y="{}" z="0.0"/>
                    <viz:size value="{}"/>
                </node>
'''
    edges_template = '''
                <edge id="{}" source="{}" target="{}" />
'''
    gefx_template = '''<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://www.gephi.org/gexf" xmlns:viz="http://www.gephi.org/gexf/viz">
    <meta lastmodifieddate="2016-12-22">
        <creator>Anurag Banerjee</creator>
        <description>Khan Academy Infection Project</description>
    </meta>
    <graph mode="static" defaultedgetype="directed">
        <nodes>
            {}
        </nodes>
        <edges>
            {}
        </edges>
    </graph>
</gexf>
'''

    nodes = ""
    edges = ""

    # node data is an array of dicts
    for index, data in enumerate(node_data):
        x = index % 10
        y = index % 3
        color = 'b="128" g="128" r="128"'
        if data["infected"]:
            color = 'b="51" g="51" r="255"'
        nodes += nodes_template.format(index, data["name"] + " (#" + str(index) + ")", color, x, y, 5)

    # edge data is an array of tuples
    for index, data in enumerate(edge_data):
        edges += edges_template.format(index, data[0], data[1])

    return gefx_template.format(nodes, edges)



