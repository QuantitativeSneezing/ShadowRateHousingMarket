#Returns the geometric mean of the most recent 6 months of Shadow Rate data
import csv
def ShadowRateMean ():
    with open('ShadowRate.csv', newline=' ') as csvfile:
        Shadow_reader= csv.reader(ShadowCSV,delimiter=',')
        Months_Logged= sum(1 for row in Shadow_reader) -1
        #The first row in the shadow rate describes the variables
        