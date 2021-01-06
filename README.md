# Github Stars

## Description
Just a python script that allows easy access to starred github repositories. If you find yourself frequently accessing your starred repositories (like me) you may find this handy.

## Usage
EZ Config: Change the name of the user to pull stars from by modifying the "user" variable on line 4.  
  
List repositories: `./ghstars -l`  
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
ghstars	-l		-	List stars
ghstars <number>	-	Clone repo by number
ghstars -r <number>	-	Download latest release asset
ghstars <string>	-	Search starred repos
```
