import names
import xlsxwriter     

import random 
 


          

workbook  = xlsxwriter.Workbook('filename.xlsx')
worksheet = workbook.add_worksheet() 
def name():  
# Rows and columns are zero indexed.     
        row = 1
        column = 0    

        for i in range(1000):
        #content = ["Parker", "Smith", "John"]     
            
        # iterating through the content list     
        #for item in content :     
            
            # write operation perform     
            worksheet.write(row, column, names.get_full_name())     
            
            # incrementing the value of row by one with each iterations.     
            row += 1    


def test():
    row = 1
    column = 1 
    for i in range(3):
        for i in range(1000): 
                n=random.randint(20,100)  
                worksheet.write(row, column,n) 
                row += 1   
        row=1  
        column +=1

def hours():
    row = 1
    column = 4
    for i in range(1000): 
                n=random.randint(1,10)  
                worksheet.write(row, column,n) 
                row += 1   

hours()
name()
test()
workbook.close()   