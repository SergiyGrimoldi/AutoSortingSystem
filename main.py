 # os
import os

import easygui

 # rich -console
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich import print
from rich.panel import Panel
from time import sleep
from rich.console import Console

 # easygui
from easygui import *

 # colorama
import colorama
from colorama import Fore, init, Back, Style
init(autoreset=True)

 # shutil
import shutil

console = Console()

def clear():

    try:
        os.system("cls" if os.name=="nt"else "clear")
    except:
        os.system("cls")
    finally:
        None

    title = ("Folder sorting By Sergiy Grimoldi")
    console.print(Panel(f"[green]{title}"), style="red", justify="center")

def back():
    
    backButton = console.input(Panel(f"[red]Press X to back"))
    
    if backButton == "x" or back == "X":
        menu()
    else:
        back()

def exit_program():
    
    try:
        os.system("cls" if os.name=="nt"else "clear")
        exit()
    
    except:
        exit()
    
    finally:
        exit()

def sort():


    title  =(Style.BRIGHT + Back.WHITE + Fore.RED + "Automatic Sorting System - By Sergiy Grimoldi ")+"\n"
    footer = "\n"+(Style.BRIGHT + Back.WHITE + Fore.RED + 'Goodbye from Automatic Sorting System by Sergiy Grimoldi')+"\n"


    print (title) # Print title of the program set at line 8
    ## Start of  program

    path =  easygui.diropenbox()
     # path = "/Users/sergiy/Downloads"
    directory_to_scan = path
    print(f"\nDirectory scelta - Choosen directory: \n -  {directory_to_scan}\n") # stampo la direcotry scelta da scansionare (questa è quella da riordinare)


    print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f" ----------- Cerco Files - Serching for files ----------- \n") # stampo sottotitolo di controllo
    count_done = 0 # inizializzo count dei file smistati correttamente
    count_undone = 0 # inizializzo count dei file non smistati correttamente
    count_file = 0 # inizializzo count dei file trovati nella direcotry scelta da scansionare
    files = [] # apro una lista contentente tutti i file trovati (solo nome ed estensione )
    try:
        for file in os.scandir(directory_to_scan): # ciclo i file contenuti nella scansione eseguita con os.scandir
            if file.is_file(): # se il file è un file continuo
                file=(file.name) # attribuisco al nome del file la variabile file
                print(f" - {file}") # stampo il risultato
                files.append(file) # aggiungo il nome del file con estensione all alista precedentemnte creata per poterci lavorare succesivamente
                count_file+=1 # aggiorno il count dei file trovati
        print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f"\n ----------- Fine Files trovati - Files found {count_file} ----------- \n") # stampo footer di controllo
    except:
        print(Style.BRIGHT + Back.WHITE + Fore.RED + f" - Nessuna cartella trovata con il nome {directory_to_scan}")
    
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

    print(Style.BRIGHT + Back.WHITE + Fore.BLACK + f"\n --------------- Eseguiti - Done: {count_done} - Gia esistenti - Already exists: {count_undone} ---------------\n") # sottotilo di log

    


    ## And of  program
    print(footer) # Print footer of the program set at line 9

    print()

    print("Sorting folder by type...")

     # path = easygui.diropenbox()
    

    folders_list = os.listdir(path)
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan", width=12)
    table.add_column("Type")

    print()


     # clear()

    audio_extensions = [".MP3",".WAV",".FLAC", ".AAC", ".WMA"]
    video_extensions = [".MP4", ".WEBM", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".AVI", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".AVCHD"]
    os_extension = [".ISO", ".DMG", ".PKG"]
    compressed_extensions = [".ZIP", ".RAR", ".TAR"]
    doc_extensions = [".DOCX", ".TXT", ".DOC", ".HTML", ".CSV", "TTF", "PDF"]
    image_extensions = [".PNG", ".JPG", ".JPEG"]
    apple_extensions = [".NUMBERS", ".PAGES", ".KEY"]
    app_extensions = [".APP"]

    for item in folders_list:
        
        
        if item.upper() in audio_extensions:
            item_type = "Audio"

        elif f".{item.upper()}" in audio_extensions:
            item_type = "Audio"
        
        elif item.upper() in video_extensions:
            item_type = "Video"
        
        elif f".{item.upper()}" in video_extensions:
            item_type = "Video"

        elif item.upper() in os_extension:
            item_type = "Os"
        
        elif f".{item.upper()}" in os_extension:
            item_type = "Os"

        elif item.upper() in compressed_extensions:
            item_type = "Compressed"

        elif f".{item.upper()}" in compressed_extensions:
            item_type = "Compressed"

        elif item.upper() in doc_extensions:
            item_type = "Document"

        elif f".{item.upper()}" in doc_extensions:
            item_type = "Document"
        
        elif item.upper() in image_extensions:
            item_type = "Image"
        
        elif f".{item.upper()}" in image_extensions:
            item_type = "Image"

        elif item.upper() in apple_extensions:
            item_type = "Apple"
        
        elif f".{item.upper()}" in apple_extensions:
            item_type = "Apple"

        elif item.upper() in app_extensions:
            item_type = "App"
        
        elif f".{item.upper()}" in app_extensions:
            item_type = "App"

        elif item.startswith("."):
            item_type = "System"
        
        
        else:
            item_type = "Unknown"


        if item_type == "System":
             None
        
        elif item_type == "Unknown":
           
            print(f"from {original} to {target}")

        else:
            table.add_row(f"{item}",f"[green]{item_type}")

            original = f"{path}/{item}"
            target = f"{path}/{item_type}/{item}"
     
            print(f"from {original} to {target}")

            shutil.move(original,target)

    clear()

    console.print(table, justify="center")

    print()

    back()

def menu():
   
    clear()

    console.print(Panel("[green]Menu[center]"),style="yellow", justify="center")
    console.print(Panel("[yellow]Choose what to do:"))

    selected = console.input("\n [cyan]1 - [yellow] Sort folders by type\n [bold red]X - [red]exit_program\n\n[white]\n --> ")
    
    if selected == "1":
        sort()
    
    if selected == "x" or selected == "X":
        clear()
        exit_program()
    
    else:
        menu()
    
 # initialize

if __name__ == "__main__":

    try:
        if os.geteuid() != 0:
            clear()
            
            print()
            console.print(Panel("[yellow]You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. exit_programing."), style="red", justify="center")
            print()
        
        else:
             menu()
    
    except Exception as e:
        print(e)