# Github Stars

## Description
Just a python script that allows easy access to starred github repositories. Saves having to go to the site every time and scroll through the list when I need to find a tool.

## Usage
EZ Config: Change the name of the user to pull stars from by modifying the "user" variable on line 4.  
  
List repositories: `./ghstars`  
Clone repository: `./ghstars <star number>`  
Search repositories: `./ghstars <search string>`  
Download latest release asset: `./ghstars -r <star number>`  
Help menu: `./ghstars -h`  
  
```
==================================================
                     ghstars			             
==================================================

Tool to interact with starred github repos
Usage:
ghstars			-	List stars
ghstars <number>	-	Clone repo by number
ghstars -r <number>	-	Download latest release asset
ghstars <string>	-	Search starred repos
```
