# New x in .xy


* [General](#general-info)
* [Purpose](#purpose)
* [Instalation](#installation)
* [How-to](#how-to)
* [Contact](#Contact)
* [License](#License)


## General

`New x in .xy` is a python program to be used for 
changing the x value in a .xy document.
Currently `New x in .xy` is used at the section for catalysis at
the University of Oslo.

## Purpose

Easy batch convert and change files with of the ´.xy´ format, creating a folder with the new converded data within the parent folder.

## Installation

Use the program by download to a directory accesible for you python enviornment. The enviornment need to have `python>=3.9.7`, `numpy>=1.21.2`, `pandas>=1.3.3`.


## How-to
How to use the program.


1. Import the program:
```
From New_x_in_xy import new_x_in_xy
```
2. Define the directory of the files that are to be converted and the file with the x-vlaues:
```
obj = new_x_in_xy(Directory=XXXXXX, x_value_file=XXXXXX)
```
3. Run the program. the following message will the apear:
```
New folder created



The following files have been converted witht the new x-value
```




To access the amount of files converted, use the `print(obj)`.


The program keeps track of the folder that are created. If a folder with asimilar path excists, a seperate command will appear asking to continue:
```
Folder allready exist. Make sure that the data does not overwrite and try again. 
                 Do you want to continue anyway (y/n)?       
```
If yes (y), the exsting folder will be overwritten and replaced with a new folder with the existing data. If no (n), the program will raise an error and abort.



## Contact

For developer issues, please start a ticket in Github. You can also write to the dev team directly at  **b.g.solemsli@smn.uio.no**
#### Authors: 
Bjørn Gading Solemsli (@bjorngso).

## License
This script is under the MIT license scheme. 



