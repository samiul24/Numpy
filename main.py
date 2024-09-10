import numpy as np
from operationclass import IntArray


file_path = "D:/Project/numpy/company.txt"

def file_handle():
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',') #return as list value
            #print(values)
            #print(type(values))

            int_value = [int(value) for value in values] # convert int value that is return as list value
            #print(int_value)
            #print(type(int_value))
            lines.append(int_value) #ceating list within list
        #print(lines)

        #data_frame = [np.array(row) for row in lines] #creating array within list
        #print(type(data_frame))

        data_frame = np.array([np.array(row) for row in lines], dtype='object')
        #print(type(data_frame)) #returing nd array
        print(data_frame.shape)
        return data_frame


    
def productivity_of_company(order, data_frame):
               
        """num_product = 0
        for element in data_frame[order]:
            num_product = num_product+element
        return num_product"""
        return np.sum(data_frame[order])
    
    
def max_productivity(data_frame):
    #i = 0
    best_company = 1
    num_of_total_products = 0
    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        print(i, result, num_of_total_products)
        if result> num_of_total_products:
            num_of_total_products = result
            best_company = i+1

    print(f"The best company is {str(best_company)} and total number of product is {str(num_of_total_products)}")


    
def min_productivity(data_frame):
    i = 0
    #worst_company = 0
    num_of_total_products = productivity_of_company(i, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        print(i, result, num_of_total_products)
        if result <= num_of_total_products:
            num_of_total_products = result
            worst_company = i+1

    print(f"The worst company is {str(worst_company)} and total number of product is {str(num_of_total_products)}")

        
def main():
    data_frame = file_handle()
    print(data_frame)

    first_barnch = IntArray(data_frame[0])
    first_barnch.display()
    first_barnch.salary()
    first_barnch.show_data()
    max_productivity(data_frame)
    min_productivity(data_frame)

if __name__=="__main__":
    main()
