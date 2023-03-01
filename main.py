# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:07:10 2023

@author: RENEE
"""
# imports
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import math

class ImageHandler:
    def __init__(self) :
        
        self.homeDir = os.getcwd()
        
        # get full path of all image files
        self.allFiles = [os.path.join(dirpath,f) 
                         for (dirpath, dirnames, filenames) 
                         in os.walk(self.homeDir) 
                         for f in filenames 
                         if os.path.splitext(f)[1] == '.tif']

    
    def open_single_image(self):
        image = cv2.imread(self.allFiles[38])
        
        # Fix coloring of image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return(image)
    
    def threshold_calculator(self):
        image = self.open_single_image()
        ret, thresh = cv2.threshold(image,20,255,cv2.THRESH_BINARY)
        return(thresh)
        
openImages = ImageHandler()
img = openImages.threshold_calculator()
plt.imshow(img)
