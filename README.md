You need to have python3, Tk, and tkinter to run.
tkinter is usually bundled with python.

if you don't have tk try:

rhel-like: sudo yum install -y tkinter tk-devel

ubuntu: sudo apt-get install python3-tk

windows/mac: http://www.activestate.com/activetcl/downloads

Task 1 is fulfilled by tk_form. GUI is staightforward and param files are written into same directory.

Task 2 is fulfilled by folder_script.py. The first argument is the path to the target folder.