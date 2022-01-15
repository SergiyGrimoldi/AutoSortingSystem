import os
import shutil
from traceback import print_tb
import colorama
from colorama import Fore, init, Back, Style
import time
init(autoreset=True)


title  =(Style.BRIGHT + Back.WHITE + Fore.RED + "Automatic Sorting System - By Sergiy Grimoldi ")



def clear():
    try:
        os.system('clear') # Clear the screen of unix system
    except:
        os.system('cls') # Clear the screen of windows system
    finally:
        None

def main():
     # print (title) # Print title of the program set at line 8
    ## Start of  program

     # directory_to_scan =  easygui.diropenbox()
    directory_to_scan = "/Users/sergiy/Downloads"
     # print(f"\nDirectory scelta - Choosen directory: \n -  {directory_to_scan}\n") # stampo la direcotry scelta da scansionare (questa è quella da riordinare)


     # print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f" ----------- Cerco Files - Serching for files ----------- \n") # stampo sottotitolo di controllo
    count_done = 0 # inizializzo count dei file smistati correttamente
    count_undone = 0 # inizializzo count dei file non smistati correttamente
    count_file = 0 # inizializzo count dei file trovati nella direcotry scelta da scansionare
    files = [] # apro una lista contentente tutti i file trovati (solo nome ed estensione )
    try:
        for file in os.scandir(directory_to_scan): # ciclo i file contenuti nella scansione eseguita con os.scandir
            if file.is_file(): # se il file è un file continuo
                file=(file.name) # attribuisco al nome del file la variabile file
                 # print(f" - {file}") # stampo il risultato
                files.append(file) # aggiungo il nome del file con estensione all alista precedentemnte creata per poterci lavorare succesivamente
                count_file+=1 # aggiorno il count dei file trovati
         # print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f"\n ----------- Fine Files trovati - Files found {count_file} ----------- \n") # stampo footer di controllo
    except:
         # print(Style.BRIGHT + Back.WHITE + Fore.RED + f" - Nessuna cartella trovata con il nome {directory_to_scan}")
        None
    
    count_file = 0 # azzero nuovaente count (ora conta i file contenuti in lista files)

    for file in files: # ciclo per ogni file contenuto nella lista

        if (file == ".DS_Store"): # escludo il file nascosto creato da macos
            continue # escludo file proprietari di sistema operativo MacOs
        file_extension = file.split(".")[-1] # ricavo estensione del file
        full_dir_file = f"{directory_to_scan}/{file}" # ricavo directory completa del file con relativa estensione

         # print(f"\n --------------- {file} ---------------") # stampo sottotilo di controllo
         # print(f"\n - Directory: {directory_to_scan}/{file}\n - File: {file}\n - Extension: {file_extension}") # stampo risultato di controllo contentnente drecotry del file, solo nome, solo estensione 
        
        check_if_exsist = f"{directory_to_scan}/{file_extension}" # setto la variabile di controllo (per la directory che ha come nome l'estensione del file esite o meno)
        to_check = os.path.isdir(check_if_exsist) # verifico

        if not to_check: # se non esiste
            
            os.makedirs(check_if_exsist) # creo cartella
             # print(f" - Ho creato - Created: '{check_if_exsist}") # stampa di controllo
             # print(f" - Copio da - Copy from: {full_dir_file} a - To:  {check_if_exsist}")# stampa di controllo
            try:
                shutil.move(full_dir_file, check_if_exsist) # sposto il file dalla direcotry scansionata a quella appena creata, solo se il file non è gia dentro
                count_done+=1 # aggiorno count dei file smistati correttamente
            
            except:
                 # print(f" - Il file - File {full_dir_file} esiste già - already exists ") # se il file esite già nella cartella
                count_undone+=1 # aggiorno count dei file non smistati correttamente

        else: # se la direcotry esiste gia
             # print(f" - '{check_if_exsist}' esiste già - already exists") # stampa di controllo
             # print(f" - Copio da  - Copy from:{full_dir_file} a - To: {check_if_exsist}") # stmapo di controllo

            try:
                shutil.move(full_dir_file, check_if_exsist) # sposto il file dalla direcotry scansionata a quella già esistente, solo se il file non è gia dentro
                count_done+=1 # aggiorno count dei file smistati correttamente
                with open ("/Users/sergiy/log_sorting_download_folder.csv", "a+") as l:
                    log = f"File {full_dir_file} moved in {check_if_exsist}\n"
                    l.write(log)
                l.close()

                print(f"Log saved in '/Users/sergiy/log_sorting_download_folder.csv'\n")

            except:
                print(f"File {full_dir_file} already exists\n") # se il file esite già nella cartella
                count_undone+=1 # aggiorno count dei file non smistati correttamente
         # print(f"\n --------------- {file} ---------------\n\n") # stampa di controllo

     # print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f"\n --------------- Eseguiti - Done: {count_done} - Gia esistenti - Already exists: {count_undone} ---------------\n") # sottotilo di log

    if count_done==0:
        print(f"Nothing to do")
        
    ## And of  program
     # print(footer) # Print footer of the program set at line 9


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


 # This file automatically start with boot of computer (strartup.sh in Userss/sergiy)