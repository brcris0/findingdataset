#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:47:56 2021

@author: wlr
"""

import os, re
import Levenshtein as lev


pub_authors_path = "../pq1a/authors.tsv"
datasets_path = "../pq1a/dataset2.tsv"
output_path = "../pq1a/authored_datasets2.tsv"


if not os.path.isfile(output_path):
    file = open(output_path, "w")
    file.close()


file0 = open(pub_authors_path, "r", encoding="utf8")
file1 = open(datasets_path, "r", encoding="utf8")

lines0 = file0.readlines()
lines1 = file1.readlines()

json0 = {}


def bag_of_names (name):
    
    name = name.replace(" ", "**")
        
    name = re.sub('[^A-Za-z0-9*]+', '_', name).lower().strip()
        
    name = name.replace("**", " ")
        
    name = name.split(" ")
        
    for term in name:
            
        if len(term) <= 3:
                
            name.remove(term)
            
            
    return(name)



for line0 in lines0:
    
    line = line0.strip().split("\t")
    
    names0 = line[2].split("||")
    
    names = []
    
    for name in names0:
        
        names.append(bag_of_names(name))
        
        
    idlattes = line[1].split("||")
    
    json0[line[0]] = {"idlattes": idlattes, "names": names}
    

    
    
    
for line1 in lines1:

    line = line1.strip().split("\t")
    
    names = line[2].replace("\'", "").replace("||", " ").replace(",", "").replace("-", "")
    
    names = bag_of_names(names)
    
    id = line[0]
    
    dataset_id = line[1]
    
    authors_id = []
    authors = []
    
    try:
        authors_id = json0[id]["idlattes"]
        authors = json0[id]["names"]
    except:
        pass
    
    
    is_author = False
    
    authors_match = ""
    
    i = 0
    
    for author in authors:
        
        for term0 in author:
            
            for term1 in names:
                
                distance = lev.distance(term0, term1)
                
                if distance <= 3:
                    
                    is_author = True
        
                    
        if is_author:
                    
            authors_match = authors_match + authors_id[i] + "||"
        
        i += 1
        
    if authors_match != "":
        authors_match = authors_match[:-2] 
                
    if is_author:  
        
        print(id, dataset_id,  authors_match)
        
        output_file = open(output_path, "a")
        output_file.write(id + "\t" + dataset_id + "\t" + authors_match + "\n")
        output_file.close()



    
