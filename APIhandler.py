import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from chatgpt import GPT


class APIhandler:
        def check_mony(mark , count):
            if "INR" in mark:
                if count >= 12500:
                    return True
                else:
                    return False
            elif "GBP" in mark:
                if count >= 20:
                    return True
                else:
                    return False
            elif "TRL" in mark:
                if count >= 5000:
                    return True
                else:
                    return False
            elif "USD" in mark:
                if count >= 30:
                    return True
                else:
                    return False
            elif "EUR" in mark:
                if count >= 30:
                    return True
                else:
                    return False
            else:
                if count >= 30:
                    return True
                else:
                    return False





        def gnaration_price(ave , many):
            a = many.find('-')
            b = many.find(" ")
            many = [int(many[1:a]) , int(many[a+1:b])]
            if ave != None:
                try:
                    ave = int(ave[2:])
                    result = ave * (21 / 100)
                    ave = result + ave
                    return int(ave)
                except:
                    ave = (many[0] + many[1]) / 2
                    return int(ave)
            else:
                ave2 = (many[0] + many[1]) / 2
                return int(ave2)
        


        def tag_check(tags):
            tag_list = ['Graphic Design', 'Logo Design', 'Photoshop', 'Illustrator', '3D Design', 'Illustration', 'T-Shirts', 'Website Design', 'Arts & Crafts', 'Caricature & Cartoons', 'Photoshop Design', 'Video Production', 'PHP', 'C Programming', 'Java', 'JavaScript', 'Python', 'Script Install', 'Translation', 'Banner Design', 'Audio Services', 'Windows Desktop', 'Linux', 'Web Security', 'Data Processing', 'Project Management', 'Industrial Design', 'CAD/CAM', 'CSS', 'Building Architecture', '3D Rendering', 'Typography', 'Animation', 'Fashion Design', 'Business Plans', 'Print', 'Home Design', 'After Effects', 'Civil Engineering', 'Photo Editing', 'Concept Design', 'PSD to HTML', 'Covers & Packaging', 'Format and Layout', 'Templates', 'AutoCAD', 'Interior Design', 'Business Cards', 'Machine Learning (ML)', 'Brochure Design', 'C++ Programming', 'HTML', 'Windows Server', 'SketchUp', 'Icon Design', 'Advertisement Design', '3ds Max', 'Pattern Making', '3D Modelling', '3D Animation', 'Poster Design', 'Sticker Design', 'Invitation Design', 'Flyer Design', 'Visual Arts', 'Fashion Modeling', 'CGI', 'Furniture Design', 'Motion Graphics', 'German Translator', 'Autodesk Revit', 'Chef Configuration Management', 'Digital Design', 'Creative Writing', 'Creative Design', 'Painting', 'Social Media Marketing', 'Business Writing', 'Network Administration', 'Video Editing', 'UX / User Experience', 'Internet Security', 'Label Design', 'Package Design', 'Instagram', 'Data Science', 'Building Design', 'Interiors', 'Tattoo Design', 'Concept Art', 'Mural Painting', 'Adobe Premiere Pro', 'App Developer', 'Book Artist', 'UI / User Interface', 'Design', 'Sign Design', 'Storyboard', '3D Model Maker', 'Neural Networks', 'Penetration Testing', 'Adobe Illustrator', 'Digital Marketing', 'Web Development', 'Web Crawling', 'Corel Painter', 'Photo Restoration', '2D Animation', 'Kinetic Typography', 'Photo Retouching', 'BeautifulSoup', 'Vue.js', 'Product Photography', 'Infrastructure Architecture', 'AutoCAD Architecture', 'Revit', 'Revit Architecture', 'PCB Design and Layout', 'Front-end Design', 'Blender', 'Urban Design', 'Architectural Rendering', 'Packaging Design', 'Selenium', 'Network Security', 'Album Design', 'Graphic Art', 'Costume Design', 'Comics', 'Building Information Modeling', 'Building Regulations', 'Art Consulting', 'Certified Ethical Hacking', 'Non-fungible Tokens (NFT)', 'Digital Art', 'Chatbot', 'Book Cover Design', 'Instructional Design', '2D Game Art', 'Childrens Book Illustration', 'Business Plan Writing', 'Fashion Writing', 'Vectorworks', '2D Drawing', '3D Architecture', '3D CAD', 'Architectural Visualization', '3D Logo', '3D Rigging', 'Angular', 'Canva', 'Lighting Design', 'Animoto', 'SmartDraw', 'Bartending', 'WordPress Design', 'Visual Design', 'Motion Design', 'YouTube Video Editing', 'TailWind', 'Logo Animation', 'Game Trailer', 'Telegram API', 'Menu Design', 'Oil Painting', 'Adobe Photoshop', 'Manga', 'Architecture', 'Vector Tracing', 'Affinity Designer', 'Digital Product Design', 'Social Media Post Design', 'Color Grading', 'Catalog Design', 'Card Design', 'Character Illustration', 'Level Design', 'Matte Painting', 'Magazine Design', 'Handy Sketch Pad', 'Print Design', 'Collage Making', 'Game Art', 'Facade Design', 'Pattern Design', 'Product Cover', 'Interaction Design', 'Sports Design', 'Digital Painting', 'Vector Design', 'Drawing Artist', 'Watercolor Painting', 'Krita', 'CorelDRAW']
            for i in tag_list:
                if i in tags:
                    return True
                else:
                    None
            return False



