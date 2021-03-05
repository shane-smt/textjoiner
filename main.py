import os
import time
from datetime import date


inputDirName = "./Raw_Logs"
outputDirName = "./Daily_Output"


def getListOfFiles(inputDirName):
    # create a list of file names in the given directory
    listOfFile = os.listdir(inputDirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(inputDirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    print(allFiles)
    return allFiles


def mergefiles():
    filelist = getListOfFiles(inputDirName)
    with open(f"{outputDirName}/Daily_Stats_{date.today()}.txt", "w") as outfile:
        for fname in filelist:
            # add new line between files
            with open(fname, "a") as infile:
                infile.write("\n")
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def cleanup():
    filelist = getListOfFiles(inputDirName)
    for fname in filelist:
        if fname.endswith(".txt"):
            print(fname)
            os.remove(fname)


if __name__ == "__main__":

    mergefiles()
    time.sleep(5)
    cleanup()
