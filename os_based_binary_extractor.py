import os 
import sys
import subprocess           # Execute shell commands 
from subprocess import PIPE                 
import binwalk              # Binwalk is used in the backened for firmware binary extraction
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


# Function to traverse/look for different files in the extracted binary
def get_file_path(filename, directory_path):
    result = []
    # Walking top-down from the root
    for root, dir, files in os.walk(directory_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

# Function to traverse/look for a directory in the extracted binary
def get_dir_path(directory_name, directory_path):
    result = "Not found"
    # Walking top-down from the root
    for root, dir, files in os.walk(directory_path):
        if directory_name in dir:
            return os.path.join(root, directory_name)
    return result

# def get_file_paths(directory_path):
#     targeted_directory_path = ["/bin", "/usr/bin", "/sbin", "/usr/sbin" ]
#     targeted_file_paths = []
#     for root, dir, files in os.walk(directory_path):
#         for filename in files:
#             file_path = os.path.join(root, filename) # Get complete path of files
#             targeted_file_paths.append(file_path)
#     return targeted_file_paths

# Function for qemu emulation of binary for extracting version number

def extract_version_number(file_name):
    file_path = get_file_path(file_name, ".")
    root_path_part = get_dir_path("bin", ".")
    # Fetching the root path of the extracted binary
    root_path = re.sub('/bin', '', root_path_part)
    print("Emulating %s and root path is %s" %(file_path[0], root_path))
    #Provide executable permission to binary using chmod +x
    subprocess.run(["chmod", "+x", file_path[0]])
    #Emulate the targeted binary using qemu-arm
    subprocess.run(["qemu-arm", "-L", root_path,file_path[0]])
    #Direct the console output to a file (mainly planning to direct to a variabl, but failed) 
    with open('test1.txt', "wb") as outfile:
        emulation_output = subprocess.Popen(['qemu-arm', '-L', root_path, file_path[0]], stdout=PIPE)
        for c in iter(lambda: emulation_output.stdout.read(1), b''):
            # sys.stdout.buffer.write(c)
            outfile.write(c) 
    #Read the qemu output that was directed to file, in variable     
    emulated_file_dump = open('test1.txt', 'r')
    emulated_data_out = emulated_file_dump.read()
    emulated_file_dump.close()
    #Remove the file, not needed anymore
    subprocess.run(["rm", "test1.txt"])
     
    # version pattern match 
    version_pattern = re.compile(r'(\d+)\.(\d+)\.(\d+)')
    pattern_search = version_pattern.search(emulated_data_out)
    match_val = pattern_search.groups()
    version_number = '.'.join(match_val)
    print("Version number of %s is %s" %(file_name, version_number))
    print("Done")
    

# Function to look CVE database to report vulnerabilities w.r.t identified version number of the binary

# Pending


# Testing version number extraction
extract_version_number("busybox")