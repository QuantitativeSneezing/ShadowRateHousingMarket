import csv
def Index_change (Number_of_months):
    Index_list = []
    with open ("HousePriceData.csv") as csvfile:
        Index_reader = csv.reader(csvfile,delimiter=',')
        for row in Index_reader: 
            Index_list.append(row[1])
            #Will replace with pandas later
        Data_length= len(Index_list)
        # Take the difference in price between the current month and the initial month being measured from
        Total_relative_change = float(Index_list[Data_length-1])/float(Index_list[Data_length-Number_of_months-1])
        Average_rate_of_return = (Total_relative_change**(1/Number_of_months))
        Displayed_average_rate = float((int(1000*Average_rate_of_return))/1000)
    print ('The average house price increased by approximately {}% per month, compounding annually'.format(Displayed_average_rate))
    return  (Average_rate_of_return)
