#thorvaldur and Erlandas Verkefni 5 code

#imports
from colormath.color_objects import sRGBColor, LabColor
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from array import array
import os
from PIL import Image
import sys
import time
import numpy as np
import sys

#converts hex to rgb
def closest(colors,color):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 
#return colors[index_of_smallest]
def hextorgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
  
    return rgb
#finds the color
def findcolor(lol):
    if lol.tolist() == [[202, 1, 2]]:
        return "R"
    elif lol.tolist() == [[255, 255, 0]]:
        return "Y"
    elif lol.tolist() == [[0, 128, 0]]:
        return "G"
    elif lol.tolist() == [[45, 88, 250]]:
        return "B"

def identifycard(imglink):
    subscription_key = "f101eb2dc5434e0ba374938409ee4bef"
    endpoint = "https://computervisionapi12123.cognitiveservices.azure.com/"
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    #list for card
    numbercard = []
    #OCR: Read File using the Read API, extract text - remote
    read_response = computervision_client.read(imglink,  raw=True)
    read_operation_location = read_response.headers["Operation-Location"]           #put all in fucntion so it can be called
    operation_id = read_operation_location.split("/")[-1]
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break #breaks loop if not started or running
        time.sleep(1)
    #gets results
    if read_result.status == OperationStatusCodes.succeeded: #if status is succeeded
        color_results = computervision_client.analyze_image(imglink, visual_features=[VisualFeatureTypes.color]) #gets color
        for text_result in read_result.analyze_result.read_results: #gets text
            for line in text_result.lines:
                if line.text not in numbercard and line.text.isdigit():
                    numbercard.append(line.text) #adds text to card list
    return numbercard, color_results


def main(img, list_of_colors):
    print(img, list_of_colors)
    numbercard, color_results = identifycard(img)
    color1 = hextorgb((color_results.color.accent_color)) #gets color
    closestcolor = closest(list_of_colors,color1) #finds closest color
    colortrue = findcolor(closestcolor)
    #adds color to card list
    firstcard1 = numbercard[0] + colortrue
    return firstcard1
#list of colors
list_of_colors = [[202,1,2],[255,255,0],[0,128,0],[45,88,250]]




