# Use

- for a while I was looking for a way to calculate maxes and weights for working sets when trying to plan lifts but couldn't find the right medium
- a web interface was too heavy, a mobile app was nice but I like to use my computer for real planning
- finally I realized a CLI was the best way and my end goal is to have a program that can perform simple calculations based on weights and reps to determine intensities and can take a spreadsheet as a value and make graphs based on the values presented

# Configuration

- create a `~/.config/pylift.ini` where you can set the directory to save you lift csv's in
- if there is no config files will be generated / searched for in the Documents directory

```ini
[dir]
lift_path = /home/cade/Desktop/lifts
```

# CSV format

- the format is a little particular but when creating a 'new lift' it gives a simple template.
- DO NOT write anything in the first 3 lines of any csv file, ie give one line of space after the two template lines
- **example**

```
/* Date */ 
/* Weight, Reps, Sets */

2-12-23
225, 6, 2
200, 10, 1

2-15-23
225, 7, 1
205, 10, 2
```
