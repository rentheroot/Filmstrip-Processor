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

class ConstructGui:
    def __init__(self, windowName):
        self.windowName = windowName
        self.openImages = ImageHandler()
    
    def img_window(self):
        
        # select image
        self.img = self.openImages.open_single_image()
        
        # gui window
        cv2.namedWindow(self.windowName, cv2.WINDOW_GUI_NORMAL)
        cv2.imshow(self.windowName, self.img)
        
        # threshold trackbar
        cv2.createTrackbar("Threshold Min", self.windowName , 0, 255, self.update_threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def update_threshold(self, val):
        threshold_min = cv2.getTrackbarPos("Threshold Min", self.windowName)
        _, dst = cv2.threshold(self.img, threshold_min, 255, cv2.THRESH_BINARY)
        cv2.imshow(self.windowName, dst)
    
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
        image = cv2.imread(self.allFiles[39])
        
        # Fix coloring of image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return(image)
        
Gui = ConstructGui("Test")
Gui.img_window()