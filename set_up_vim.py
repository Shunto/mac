# import the os module
import os

path = os.path.expanduser("~")

try:
	os.chdir(path)
	#print("Current working directory: {0}".format(os.getcwd()))
	os.system("touch .vimrc")
	os.system("echo set tabstop=4 >> .vimrc")
	os.system("echo syntax on >> .vimrc")
	
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))
except:
	pass
