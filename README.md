# DTM http Server and DCM http Client 

Developed by Whitman Spitzer for the DTM and DCM Raspberry Pi prototypes, written in Python 3, using standard library objects


### Some Instructions! 

First, clone this repo to a wifi enable raspberry pi.

Next, find the IP address of that Raspberry Pi. You can use the command `hostname -I`

In the server/testing folder, theres a python file, called `DTMServer3.py`

Open it from the raspi and edit `host_name` to be the raspi's IP address

Now you can run it from the command line by typing `python3 DTMServer3.py`, which will start the DTM Server. 
This should not require you to add any dependencies (unless your python version isn't up to date).

If you want to run the server or client on a non-raspberry pi machine of some kind, 
delete the line ```import RPi.GPIO as GPIO``` from the top of the file (it's for GPIO pins)
and then go through and find the ```os.popen()``` calls to check GPU temp and replace them with other variables 
to keep the code working.

Now do the same thing from your other wifi enabled raspi, except this time
in the client/testing folder, edit the `httpClient1.py` file,
change the  `host_name` to the DTM hostname. NOT the DCM (second raspi).
You're editing the `httpClient1.py` file to include the IP address of the other raspi, not itself. 
Now if you run it (while the DTM server is running), with `python3 httpClient1.py` 
(the default python version on raspi's isn't 3)
The DCM should connect to the DTM server and start sending XML POST requests every 5 seconds, 
which the DTM server will be parsing, adding some information, and storing in the `TrustLogv2.xml file`.

The DTM server will also update a webpage, visible from any browser on the network by pasting
`[IP address XX.XX.XX.etc]:8889`, where `8889` is the port number in the code (but it can be changed).

I mentioned you can delete the ```import RPi.GPIO as GPIO``` line and ditch the `os.popen()` and then run either the 
server or client on a non-raspi computer, you can also run them both on the same computer! 
if you put the keyword `localhost` anywhere `host_name` goes, it should create a loopback (maybe, I didn't try it)
for you to then put ```localhost:8889``` in the browser to view the page. 
