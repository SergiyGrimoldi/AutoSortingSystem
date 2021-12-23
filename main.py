import shutil # per gestire lo spostamento e la creazione di directory
import os # per gestire il sistema operativo
import pathlib # per gestire le directory
from typing import Counter # per counter


def clear(): # ripulisce terminale
    if os.name == 'nt': # se dispositivo su cui lavora il programma è windows
        os.system('cls') # cancella scritte da cmd
    else:
        os.system('clear') # cancella scritte da terminale


def divide(): ## Qui parte la funzione di smistamento automatico
    clear() # ripulisco linea di comando
    
    if os.name == 'nt': # se dispositivo su cui lavora il programma è windows
        print("\n\n\n ------------------------- Benvenuto nel sitema automatico di smistamento file creata da Sergiy Grimoldi - Welcome to Auto Sorting System by Sergiy Grimoldi -------------------------\n\n\n") # Titolo
        print("Sistema operativo - OS:\n - Windows\n") # sistema operativo sul quel lavoro
    
    else:
        print("\n\n\n ------------------------- Benvenuto nel sitema automatico di smistamento file creata da Sergiy Grimoldi - Welcome to Auto Sorting System by Sergiy Grimoldi -------------------------\n\n\n") # Titolo
        print("Sistema operativo - OS:\n - Unix\n") # sistema operativo sul quel lavoro

    directory_to_scan = "/Your/Full/Directory/To/Scan" ## da modificare in base alla direcotry che si vuole riordinare
  
    if directory_to_scan == "/Your/Full/Directory/To/Scan": # controllo se la dirctory da analizzare è stata settata correttamente
        print("Prima configura il programma scegliendo una directory da scansionare e riordinare (Linea 25 nel codice) - Firts choose directory to scan and sort (Line 25 in code)") # stampa di info
        exit() # esco dal programma 

    print(f"\nDirectory scelta - Choosen directory: \n - {directory_to_scan}\n") # stampo la direcotry scelta da scansionare (questa è quella da riordinare)

    print(f" ----------- Cerco Files - Serching for files ----------- \n") # stampo sottotitolo di controllo
    count_done = 0 # inizializzo count dei file smistati correttamente
    count_undone = 0 # inizializzo count dei file non smistati correttamente
    count_file = 0 # inizializzo count dei file trovati nella direcotry scelta da scansionare
    files = [] # apro una lista contentente tutti i file trovati (solo nome ed estensione )
    for file in os.scandir(directory_to_scan): # ciclo i file contenuti nella scansione eseguita con os.scandir
        if file.is_file(): # se il file è un file continuo
            file=(file.name) # attribuisco al nome del file la variabile file
            print(f" - {file}") # stampo il risultato
            files.append(file) # aggiungo il nome del file con estensione all alista precedentemnte creata per poterci lavorare succesivamente
            count_file+=1 # aggiorno il count dei file trovati

    print(f"\n ----------- Fine Files trovati - Files found {count_file} ----------- \n") # stampo footer di controllo

    
    
    print(f"\n------------------------- Inizio trasferimento utomatico - Starting automated sorting -------------------------\n") # stampo sottotitlo di controllo
    
    count_file = 0 # azzero nuovaente count (ora conta i file contenuti in lista files)
    for file in files: # ciclo per ogni file contenuto nella lista

        if (file == ".DS_Store"): # escludo il file nascosto creato da macos
            continue # escludo file proprietari di sistema operativo MacOs
        file_extension = file.split(".")[-1] # ricavo estensione del file
        full_dir_file = f"{directory_to_scan}/{file}" # ricavo directory completa del file con relativa estensione

        print(f"\n --------------- {file} ---------------") # stampo sottotilo di controllo
        print(f"\n - Directory: {directory_to_scan}/{file}\n - File: {file}\n - Extension: {file_extension}") # stampo risultato di controllo contentnente drecotry del file, solo nome, solo estensione 
        
        check_if_exsist = f"{directory_to_scan}/{file_extension}" # setto la variabile di controllo (per la directory che ha come nome l'estensione del file esite o meno)
        to_check = os.path.isdir(check_if_exsist) # verifico

        if not to_check: # se non esiste
            
            os.makedirs(check_if_exsist) # creo cartella
            print(f" - Ho creato - Created: '{check_if_exsist}") # stampa di controllo
            print(f" - Copio da - Copy from: {full_dir_file} a - To:  {check_if_exsist}")# stampa di controllo
            try:
                shutil.move(full_dir_file, check_if_exsist) # sposto il file dalla direcotry scansionata a quella appena creata, solo se il file non è gia dentro
                count_done+=1 # aggiorno count dei file smistati correttamente
            except:
                print(f" - Il file - File {full_dir_file} esiste già - already exists ") # se il file esite già nella cartella
                count_undone+=1 # aggiorno count dei file non smistati correttamente

        else: # se la direcotry esiste gia
            print(f" - '{check_if_exsist}' esiste già - already exists") # stampa di controllo
            print(f" - Copio da  - Copy from:{full_dir_file} a - To: {check_if_exsist}") # stmapo di controllo
            try:
                shutil.move(full_dir_file, check_if_exsist) # sposto il file dalla direcotry scansionata a quella già esistente, solo se il file non è gia dentro
                count_done+=1 # aggiorno count dei file smistati correttamente
            except:
                print(f" - Il file - File {full_dir_file} esiste già - already exists") # se il file esite già nella cartella
                count_undone+=1 # aggiorno count dei file non smistati correttamente
        print(f"\n --------------- {file} ---------------\n\n") # stampa di controllo

    print(f"\n------------------------- Log -> Eseguiti - Done: {count_done} - Gia esistenti - Already exists: {count_undone} -------------------------\n") # sottotilo di log
    print(f"\n\n\n ------------------------- Arrivederci dal sitema automatico di smistamento file creata da Sergiy Grimoldi ({count_file}) - Goodbye form Auto Sorting System by Sergiy Grimoldi -------------------------\n\n\n") # chiusura
   

divide() # parte il programma