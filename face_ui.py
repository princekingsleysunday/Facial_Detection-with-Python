# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:24:32 2023

@author: Kingsley
"""

import streamlit as st
from face_app import  detect_faces
from face_app import detect_faces, face_cascade, cap
import cv2

def main():
    
    st.title('Face Detection App')
    
    detect_faces()



if __name__ == '__main__': 
   main()