"""
food access datathon 2020
"""

# import the excel file of tracts in Houston and surrounding areas
import xlrd 
tract_nums = {}

wb = xlrd.open_workbook("Houston_tracts.xlsx")
sheet = wb.sheet_by_index(0)
# get the tract numbers for all of the Houston tracts
for i in range(1, 1109):
    tract_nums[sheet.row_values(i, 0, 1)[0]] = sheet.row_values(i, 2, 3)[0]

# import the correct tracts from the KML file and write it into the new file
# open the KML file
kml = open(r"HOU_named2.txt","r+") #all_tracts
kml2 = open("HOU_named3.txt", "w+")

lines = kml.readlines()
num_lines = len(lines)

# for each line, check if the AFFGEOID is in the Houston tracts
for index in range(num_lines): 
    line = lines[index]
    line2 = lines[index]
    index2 = index
    if "<SimpleData name=\"COUNTYFP\">" in line:
        # find the GEOIDD in the Houston tracks
        while line2[0:25] != '<SimpleData name="GEOID">':
            index2 += 1
            line2 = lines[index2]
        GEOIDD = line2[25:36]
        # find the tracts' GEOIDD
        county_name = tract_nums[GEOIDD]
        kml2.write(line.replace(line,'<SimpleData name="COUNTY">'+county_name+'</SimpleData>\n'))
    elif "COUNTYFP" in line:
        kml2.write(line.replace("COUNTYFP",'COUNTY'))
        index += 1
        line = lines[index]
        kml2.write(line.replace(line,'<td>'+county_name+'</td>'))
    else:
        kml2.write(line)


        