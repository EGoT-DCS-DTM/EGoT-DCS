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
ap.add_argument('-pa', '--profile_addon', required=False, metavar='', type=int, help = 'allows for random time steps for each data point')
ap.add_argument('-ma', '--mixed_args', nargs='+', required=False, metavar='', help= 'the profiles to be used in the mixed profile')

args = ap.parse_args()

profiles = ['ideal', 'random', 'flawed', 'almost_good', 'almost_bad', 'mixed']
#fileWriter = csv.writer(csvFile)
if args.profile not in profiles:
    print(f"please specify a valid profile. '{args.profile}' is not a valid option")
    print("here are the options: ")
    print(profiles)
    quit()

#this ideal profile only generates expected data
def ideal_profile(fileWriter,num_datapoints):
 #   fileWriter = csv.writer(csvFile)
    for x in range(num_datapoints):
        fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return

#this radom profile generates ex, Ux, ind, or n data
def random_profile(fileWriter,num_datapoints):
    messageList = ['Ex','Ux','Ind','N', 'Dis']
    actorList = ['DER','DCM','DERAS','DTM']
  #  fileWriter = csv.writer(csvFile)
    num_datapoints = int(num_datapoints) * 4
    rand_timestep = random.sample(range(1, 86400), num_datapoints)
    rand_timestep.sort()
    
    for x in (range(num_datapoints)):

        randomIndexM = randrange(len(messageList))
        message = messageList[randomIndexM]

        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        if(args.profile_addon == 1):
            fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + rand_timestep[x]) , random.randint(15, 45)/100, 'No Attack'])  
        else:
            fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x) , random.randint(15, 45)/100, 'No Attack'])
    return 

#this flawed profile  
def flawed_profile(fileWriter,num_datapoints):
    messageList = ['Ux','Ind','N', 'Dis']
    actorList = ['DER','DCM','DERAS','DTM']
   # fileWriter = csv.writer(csvFile)
    num_datapoints = int(num_datapoints) * 4
    for x in range(num_datapoints):
        randomIndex = randrange(len(messageList))
        message = messageList[randomIndex]

        randomIndexA = randrange(len(actorList))
        actor = actorList[randomIndexA]
        fileWriter.writerow([actor, '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100/100, 'No Attack'])
    return 

def almost_ideal(fileWriter,num_datapoints):
    #fileWriter = csv.writer(csvFile)
    #numrange = args.number 
    for x in range(num_datapoints):
        if (args.profile_addon is not None) and (x == args.profile_addon):
            fileWriter.writerow(['DER' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DCM' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DERAS' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DTM' , 'Ux', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        
        else:
            fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return

def almost_flawed(fileWriter,num_datapoints):
    messageList = ['Ux','Ind','N', 'Dis']
    #fileWriter = csv.writer(csvFile)
    for x in range(num_datapoints):
        randomIndex = randrange(len(messageList))
        message = messageList[randomIndex]
        #TODO: look into what the float values are for time
        if (args.profile_addon is not None) and (x == args.profile_addon):
            fileWriter.writerow(['DER' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DCM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DERAS' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DTM' , 'Ex', '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
        else:
            fileWriter.writerow(['DER', '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DCM', '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DERAS' , '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
            fileWriter.writerow(['DTM' , '%s' % message, '%f' % (time.time() + args.increment * x), random.randint(15, 45)/100, 'No Attack'])
    return 

def mixed(fileWriter,num_datapoints):
    x = len(args.mixed_args)
    num_datapoints_per_profile = int(num_datapoints / x)

    # check args to be valid
    for idx in args.mixed_args:
        if idx not in profiles:
            print(f"please specify a valid profile. '{idx}' is not a valid option")
            print("here are the options: ")
            print(profiles)
            quit()
        if (idx == "ideal"):
            ideal_profile(fileWriter,num_datapoints_per_profile)
        elif (idx== "random"):
            random_profile(fileWriter,num_datapoints_per_profile)
        elif(idx == "flawed"):
            flawed_profile(fileWriter,num_datapoints_per_profile)
        elif(idx == "almost_good"):
            almost_ideal(fileWriter,num_datapoints_per_profile)
        elif(idx == "almost_bad"):
            almost_flawed(fileWriter,num_datapoints_per_profile)
    
    print(x)
    print(args.mixed_args)
    return

#create and write to csv file
#TODO: check if the file name aleady exists to avoid overwrite 
with open(args.file, 'w') as csvFile:
    fileWriter = csv.writer(csvFile)
    num_datapoints = args.number
    fileWriter.writerow(['Actor', 'Message Eval Catagory', 'Current Time', 'Transit Time', 'Attack Status'])
    #get information from data generator 
    if (args.profile == "ideal"):
        ideal_profile(fileWriter,num_datapoints)
    elif (args.profile == "random"):
        random_profile(fileWriter,num_datapoints)
    elif(args.profile == "flawed"):
        flawed_profile(fileWriter,num_datapoints)
    elif(args.profile == "almost_good"):
        almost_ideal(fileWriter,num_datapoints)
    elif(args.profile == "almost_bad"):
        almost_flawed(fileWriter,num_datapoints)
    elif(args.profile == "mixed"):
        mixed(fileWriter,num_datapoints)

#TODO: use xml file comparison against the xsd to determine EX, Ux, Ind, N instead of these 
# values being hardcoded in 

#TODO: look at python library xmlschema 

#TODO: create a profile where everything goes right until the end