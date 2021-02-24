import urllib3
import http.client
import urllib.request
import urllib.parse
import RPi.GPIO as GPIO
import os
import sys
import xml.etree.ElementTree as ET
from time import sleep
import datetime

host_name = '192.168.0.178'  # DTM Rpi address
host_port = 8889
host_address = '192.168.0.178:8889'

def getTemp():
    """get temp from operating system with an os.popen call
    """
    traw = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    traw = traw.replace('temp=', '')
    traw = traw.replace('\n', '')
    traw = traw[:-2]
    temp = str(traw)
    return temp

temp = getTemp()
ct = datetime.datetime.now()
tStamp = str(ct)


data = ET.Element('TrustLog') #creating an xml element structure
el1 = ET.SubElement(data, 'DCMContact') #subelement
el1.set('timestamp', tStamp) # timestamp is an attribute, attrib
el1.set('temp', temp) #temp is an attribute
el1.text = 'CONNECTION SUCCESSFUL' #just kinda filler

obj_xml = ET.tostring(data) #converts xml object into a string

headers = {"Content-type": "text/xml", "Accept": "text/plain"} #headers for the request

while True:
    sendDTM = http.client.HTTPConnection(host_name, host_port)
    sendDTM.request('POST', host_address, obj_xml, headers) #POST type request, to server address, string created from 
                                                            #xml object, and the headers dictionary
    sleep(5) #wait 5 seconds 


