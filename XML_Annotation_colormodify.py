#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:51:57 2023

@author: Jaidip Jagtap
"""
import os
import re
from tqdm import *


xml_path= 'xml_folder'
mask_output =r"xml_newoutput"

if not os.path.exists(mask_output):
    os.makedirs(mask_output)


subdir, dirs, files = os.walk(xml_path).__next__()
files = [k for k in files if ".xml" in k]

for filename in tqdm(files):
    if 'png' not in filename:
        pre,ext=filename.rsplit('.xml', 1)
        fname= os.path.join(xml_path,filename) #os.rename(renamee, pre + new_extension)
        
        newfname_class = os.path.join(mask_output,filename)# 
        if os.path.exists(newfname_class):
            print(f"Skipping as output file exists: \t {filename}")
            continue        
        print(f"working on file: \t {filename}")

        fiIn = open(fname).readlines()
        
        for i in range(len(fiIn)):
            line=fiIn[i]
            line = line.rstrip("\n") # strip newline
            # line = line.rstrip("\n") # strip newline       
            print(line)
            
            if re.findall(r'Name=\"NSG_area2s\".*LineColor=\"(\d+)\"', line): 
                line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="255"', line) 
                fiIn[i]=line
                print(line)
                
            if re.findall(r'Name=\"IntimalArea\".*LineColor=\"(\d+)\"', line): #"\d+.NSG_area2s\"
                line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="0"', line) 
                fiIn[i]=line
                print(line)
                
            if re.findall(r'Name=\"LuminalArea\".*LineColor=\"(\d+)\"', line): 
                line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="4227327"', line) 
                fiIn[i]=line
                print(line)
                
            if re.findall(r'Name=\"NSG_area1d\".*LineColor=\"(\d+)\"', line): 
                line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="65535"', line) 
                fiIn[i]=line
                print(line)
                
            if re.findall(r'Name=\"NSG_area2d\".*LineColor=\"(\d+)\"', line): 
                line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="0"', line) 
                print(line)
                fiIn[i]=line
                
                #255 and 8388863 for red; 0 for black. 0 for black; 65535 used for yellow; 
                #green=65280; Brown:4227327
                
        
        
        with open(newfname_class, "w") as f:
            f.write("\n".join(fiIn))
        

        
