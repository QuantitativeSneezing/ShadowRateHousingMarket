import csv
def ShadowRateMean ():
    with open("ShadowRate.csv") as csvfile:
        Shadow_reader= csv.reader(csvfile,delimiter=',')
        Table_length= sum(1 for row in Shadow_reader) 
        return Table_length
