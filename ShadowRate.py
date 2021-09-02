import csv
from typing import List
def Shadow_rate_mean (Number_of_months, Housing_lag):
    Rate_sum = 0.00
    List_of_shadow_rates = []
    with open("ShadowRate.csv") as csvfile:
        Shadow_reader= csv.reader(csvfile,delimiter=',')
        for row in Shadow_reader:
            List_of_shadow_rates.append(row[2])
            #TODO convert to pandas
        Data_length= len(List_of_shadow_rates)
        #Most house price data will lag behind up to date fed data- for instance, the Case-Schiller is two months behind our shadow rate data
        for i in range(Data_length-Housing_lag-1, Data_length-Number_of_months-Housing_lag-1,-1):
            #Counts back from the most recent month to the desired number of months
            Rate_sum += float(List_of_shadow_rates[i])
            Rate_average = Rate_sum/Number_of_months
            # Will display the first three digits of the average rate, but preserve all of the data behind the scenes
            Displayed_rate_average = float((int(100*Rate_average))/100)
        print('The average Shadow Rate over the most recently available {} months was approximately {}%'.format(Number_of_months,Displayed_rate_average))
        return Rate_average
