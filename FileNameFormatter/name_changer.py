import os

workingdir = os.getcwd() + "\\test" # change this to desired directory w/ downloads
moviedir = workingdir + "\\Movies"

files = [f for f in os.listdir(workingdir) if os.path.isfile(os.path.join(workingdir, f))]

for file in files:
    fullpath = os.path.join(workingdir, file)
    filename, fileext = os.path.splitext(file) # split filename and extension name
    filename = filename.split(".") 
    filename_new = filename[:-8] # remove extra file details

    filename_new[-1] = "(" + filename_new[-1] + ")" # add parentheses around year
    filename_new = " ".join(filename_new) # recombine filename

    # print(os.path.join(moviedir, filename_new + fileext)) 

    # rename and move to Movies folder
    os.rename(fullpath, os.path.join(moviedir, filename_new + fileext))

        