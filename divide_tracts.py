"""
food access datathon 2020
"""

# import the excel file of tracts in Houston and surrounding areas
import xlrd 
tract_nums = []

wb = xlrd.open_workbook("Houston_tracts.xlsx")
sheet = wb.sheet_by_index(0)
# get the tract numbers for all of the Houston tracts
for i in range(1, 1109):
    tract_nums.append(sheet.row_values(i, 0, 1)[0])
print(len(tract_nums))

# import the correct tracts from the KML file and write it into the new file
# open the KML file
kml = open(r"all_tracts.txt","r") #all_tracts
# create a new file to store the info for the Houston tracks 
wanted_tracts = open("HOU_tracts2.txt","w+")

lines = kml.readlines()
num_lines = len(lines)

# for each line, check if the AFFGEOID is in the Houston tracts
for index in range(num_lines): 
    line = lines[index]
    # if the AFFGEOID is in the Houston tracks
    if "<SimpleData name=\"AFFGEOID\">1400000US" in line and line[37:48] in tract_nums:
        # start from the name 
        while line[0:6] != '<name>':
            index -= 1
            line = lines[index]
        # grab everything until and including the Placemark id and write it into the new file
        while line[0:14] != '<Placemark id=' and index < num_lines-1:
            wanted_tracts.write(line)
            index+=1
            line = lines[index]
        wanted_tracts.write(line)    


        