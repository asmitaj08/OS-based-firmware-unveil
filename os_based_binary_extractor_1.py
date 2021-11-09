import os 
import sys
import subprocess           # Execute shell commands 
from subprocess import PIPE                 
#import binwalk              # Binwalk is used in the backened for firmware binary extraction
import re                   # regex for pattern matching


# Function to take the binary file path input from user
def take_binary_input():
    file_path_input = input("Enter the path of the binary file: ")
    #Check if the file exists in the path
    assert os.path.isfile(file_path_input), "File %s not found. Please enter the correct path of binary" %file_path_input
    return file_path_input

# Function to extract the firmware binary
def extract_binary_basic_info():
    file_path = take_binary_input()
    print("Extracting the binary %s" %file_path)
    try:
        # Using binwalk APIs - https://github.com/ReFirmLabs/binwalk/blob/master/API.md
        binwalk.scan(file_path,signature=True, quiet=True, extract=True, entropy=True)   
        print("The extracted files are in file 'filestructure.txt' ")
    # list_d = subprocess.run(["tree","_tp-link-archer-gx90-router.bin*"])
        os.system("tree _* > filestructure.txt") #replace os.system with subprocess
    except binwalk.ModuleException as e:
        print ("Binwalk critical failure:", e)


# Function to look CVE database to report vulnerabilities w.r.t identified version number of the binary
def cve_bin_tool():
    file_path = take_binary_input()
    with open('cve_check_results.txt', 'w') as f:
        f.write('cve-bin-tool %s \n' %file_path)
        cve_check = subprocess.Popen(['cve-bin-tool', file_path], stdout=f)


# Testing cve-bin-tool
cve_bin_tool()
