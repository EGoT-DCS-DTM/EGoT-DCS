import sys
import csv
import time
import argparse
import random
from random import randrange

#take in user arguments
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, metavar='', help = 'name of the file that will be generated')
ap.add_argument('-p', '--profile', required=True, metavar='', help = 'the profile deciding the type data is generated')
ap.add_argument('-n', '--number', required=True, metavar='', type=int, help = 'the number of data sets generated')
ap.add_argument('-i', '--increment', required=True, metavar='', type =float, help = 'time increment')
args = ap.parse_args()

profiles = ['ideal', 'random', 'flawed', 'almost_good', 'almost_bad']
if args.profile not in profiles:
    print(f"please specify a valid profile. '{args.profile}' is not a valid option")
    print("here are the options: ")
    print(profiles)
    quit()

#this ideal profile only generates expected data
def ideal_profile():
    fileWriter = csv.writer(csvFile)
    for x in range(args.number):
        fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return

#this radom profile generates ex, Ux, ind, or n data
def random_profile():
    messageList = ['Ex','Ux','Ind','N', 'Dis']
    actorList = ['DER','DCM','DERAS','DTM']
    fileWriter = csv.writer(csvFile)
    for x in range(args.number):
        randomIndexM = randrange(len(messageList))
        message = messageList[randomIndexM]

        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        
        fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x) , random.randint(15, 45)/100, 'No Attack'])
    return 

#this flawed profile  
def flawed_profile():
    messageList = ['Ux','Ind','N', 'Dis']
    actorList = ['DER','DCM','DERAS','DTM']
    fileWriter = csv.writer(csvFile)
    for x in range(args.number):
        randomIndex = randrange(len(messageList))
        message = messageList[randomIndex]

        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100/100, 'No Attack'])
    return 

def almost_ideal():
    fileWriter = csv.writer(csvFile)
    numrange = args.number 
    for x in range(numrange - 1):
        fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    
    for x in range(1):
        fileWriter.writerow(['DER' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DCM' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DERAS' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DTM' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return

def almost_flawed():
    messageList = ['Ux','Ind','N', 'Dis']
    actorList = ['DER','DCM','DERAS','DTM']
    fileWriter = csv.writer(csvFile)
    numrange = args.number
    for x in range(numrange - 1):
        randomIndex = randrange(len(messageList))
        message = messageList[randomIndex]

        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        #TODO: look into what the float values are for time
        fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    
    for x in range(1):
        fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return 
#create and write to csv file
#TODO: check if the file name aleady exists to avoid overwrite 
with open(args.file, 'w') as csvFile:
    fileWriter = csv.writer(csvFile)
    fileWriter.writerow(['Actor', 'Message Eval Catagory', 'Current Time', 'Transit Time', 'Attack Status'])
    #get information from data generator 
    if (args.profile == "ideal"):
        ideal_profile()
    elif (args.profile == "random"):
        random_profile()
    elif(args.profile == "flawed"):
        flawed_profile()
    elif(args.profile == "almost_good"):
        almost_ideal()
    elif(args.profile == "almost_bad"):
        almost_flawed()

#TODO: use xml file comparison against the xsd to determine EX, Ux, Ind, N instead of these 
# values being hardcoded in 

#TODO: look at python library xmlschema 

#TODO: create a profile where everything goes right until the end