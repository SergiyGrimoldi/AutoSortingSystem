from itertools import count
from locale import RADIXCHAR
import os
import shutil
from tkinter import E
from colorama import Fore, init, Back, Style
import time
init(autoreset=True)

title  =(Style.BRIGHT + Back.WHITE + Fore.RED + "Automatic Sorting System - By Sergiy Grimoldi ")

def clear():
    try:
        os.system('clear') 
    except:
        os.system('cls') 
    finally:
        None

def main():
    
    directory_to_scan = "/Users/sergiy/Downloads"
    
    files = [] 
    
    try:
        for file in os.scandir(directory_to_scan): 
            
            if file.is_file(): 
                file=(file.name) 
                 
                files.append(file)

    except: 
        None
    
    count_done = 0 

    for file in files: 

        if (file == ".DS_Store"):
            continue
       
        file_extension = file.split(".")[-1] 
        
        if file_extension == "crdownload":
            continue
        
        full_dir_file = f"{directory_to_scan}/{file}" 

        check_if_exsist = f"{directory_to_scan}/{file_extension}" 
        to_check = os.path.isdir(check_if_exsist) 

        if not to_check:
            os.makedirs(check_if_exsist) 

            try:
                shutil.move(full_dir_file, check_if_exsist) 
                count_done+=1
            
            except Exception as e:
                print(e)

        else: 
            try:
                shutil.move(full_dir_file, check_if_exsist) 
                count_done+=1 
               
                with open ("/Users/sergiy/log_sorting_download_folder.csv", "a+") as l:
                    log = f"File {full_dir_file} moved in {check_if_exsist}\n"
                    l.write(log)
                l.close()

                print(f"Log saved in '/Users/sergiy/log_sorting_download_folder.csv'\n")

            except Exception as e:
                print(e) 
                
         
    if count_done==0:
        print(f"Nothing to do")
    

while True:
    try:
        clear()

        print(title)
        print("\nScan...")

        main()

        print("\nWaiting for next scan...")
        
        time.sleep(30)
        clear()
    
    except:
        None
