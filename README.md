# **Auto Sorting System by Sergiy Grimoldi**

This program organizes automatically files in folders named as file's extension 

## How to use the code

 1. Open file  `main.py`
 2. Got to line ***25***
      and insert your directory. (This must be the directory contains all the files to be sorted). Remember keeps quotation marks

      > directory_to_scan = "/Your/Full/Directory/To/Scan"


 3. Open `terminal` 
 
            cd ./directory
      or `cmd` 
      
            dir ./directory
           

      and goto directory where you've saved folder downloaded containing this program

 3. Run python file with command-line or with your code editor digiting: 
      
         python3 main.py

 4. If program doesn't works well probably you don't have modules installed so check if:
    - `shutil` is installed
    - `os` is installed
    - `pathlib` is installed
 5. And if are not installed:

        pip3 install `module's name`
 6. If program continues not working [Contact Me](mailto:grimo.sergiy@icloud.com)
    
## How program works

This program gets all file in directory choosen, automatically gets the extension of these, check if exists a folder named as file extension;
   - If folder exists puts file in this
   - Else creates it and puts file in this

## Note

This program does not replace files if these already exists in subdirectory named as extension of files found.

If you want this feature or other [Contact Me](mailto:grimo.sergiy@icloud.com)

If you want other programs [Contact Me](mailto:grimo.sergiy@icloud.com) or check on my profile if it does'not already exsist.
