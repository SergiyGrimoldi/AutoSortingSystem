# AutomaticFolderOrganizer

This program organizes automatically files in folders named as file's extension 

## How to use the code

Got to line ***25***
and insert your directory. (This this must be the directory contains all the files to be sorted)

> directory_to_scan = "/Your/Full/Directory/To/Scan" ## da modificare in base alla direcotry che si vuole riordinare

## How program works

This program gets all file in directory choosen, automatically gets the extension of these, check if exists a folder named as file extension;
   - If folder exists puts file in this
   - Else creates it and puts file in this
