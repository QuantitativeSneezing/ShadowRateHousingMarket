from ShadowRate import Shadow_rate_mean 
from Houseprices import Index_change  
# Will eventually allow for user changes to these variables
Average_Shadow_Rate = Shadow_rate_mean(6,2)
Average_house_return = Index_change (6)
# Even though all the displayed numbers will be truncated, the data will be preserved so it can be called if needed
Cost_of_credit_adjusted_housing_return = Average_house_return-Average_Shadow_Rate
Displayed_adjusted_return =  float((int(1000*Cost_of_credit_adjusted_housing_return))/1000)
print ('''Due to the current monetary conditions, the real return on housing should be closer to {}% per month, 
when accounting for both the increase in property value and the real cost of carrying debt'''.format(Displayed_adjusted_return))