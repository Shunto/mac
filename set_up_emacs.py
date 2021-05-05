# import the os module
import os

path = os.path.expanduser("~")

try:
	os.chdir(path)
	#print("Current working directory: {0}".format(os.getcwd()))
	os.system("touch .emacs.el")
	os.system("echo \"(setq-default tab-width 4 indent-tabs-mode nil)\" >> .emacs.el")
	os.system("echo \"\" >> .emacs.el")
	os.system("echo \'\"\"\"(setq make-backup-files nil)\"\"\"\' >> .emacs.el")
	os.system("echo \"\" >> .emacs.el")
	os.system("echo \"(put 'upcase-region 'disabled nil)\" >> .emacs.el")
	os.system("echo \"\" >> .emacs.el")
	os.system("echo \"(put 'downcase-region 'disabled nil)\" >> .emacs.el")
	os.system("echo \"\" >> .emacs.el")
	os.system("echo \"(put 'set-goal-column 'disabled nil)\" >> .emacs.el")
	
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))
except:
	pass
