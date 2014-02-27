import Image
import sys
import glob
import time


def TheRudekInHalf(coucou, form):
	pixels = Image.open(coucou);
	dim = pixels.size;
	wid = dim[0];
	hei = dim[1];
	half = wid/2;
	Plouf=0;
	Onebox=(Plouf,Plouf,Plouf+half,Plouf+hei);
	twobox=(half,Plouf,half+half,Plouf+hei);
	
	theOne = pixels.crop(Onebox);
	theTwo = pixels.crop(twobox);
	if(form!= "jpeg"):
		NameOne = coucou[:-4]+"1."+form;
		NameTwo = coucou[:-4]+"2."+form;
	else:
		NameOne = coucou[:-4]+"1.jpg";
		NameTwo = coucou[:-4]+"2.jpg";
	theOne.save(NameOne, form);
	theTwo.save(NameTwo, form);

def TheOtherHolf (choice):
	if (choice == 2):
		for x in glob.glob("*.png"):
			TheRudekInHalf(x,"png");
			print (x+" Cut");
		for x in glob.glob("*.jpg"):
			TheRudekInHalf(x,"jpeg");
			print (x+" Cut");
		for x in glob.glob("*.jpeg"):
			TheRudekInHalf(x, "jpeg");
			print (x+" Cut");
	if (choice == 1):
		path = raw_input("Give me the path to slaughter\n")
		for x in glob.glob(path+"*.png"):
			TheRudekInHalf(x,"png");
			print (x+" Cut");
		for x in glob.glob(path+"*.jpg"):
			TheRudekInHalf(x,"jpeg");
			print (x+" Cut");
		for x in glob.glob(path+"*.jpeg"):
			TheRudekInHalf(x, "jpeg");
			print (x+" Cut");


def menu ():
	Poney= raw_input("Please select what you want? \n1. Dual Monitors wallpaper split (Yay!) \n2. Nazi mode (Fuck you just do it) \nOption 1 will ask you the path of the folder, option 2 will just execute in current folder (pun intented)\nDo not answer with a different number unless you are curious")
	
	if(int(Poney) ==2 or int(Poney) == 1):
		TheOtherHolf(int(Poney));
	else:
		print("Bad answer deleting all files\nProcessing ")
		time.sleep(1);
		print(".");
		time.sleep(1);
		print(".");
		time.sleep(1);
		print(".");
		time.sleep(1);
		print(".");
		time.sleep(1);
		print(".");

menu();

print("done");

