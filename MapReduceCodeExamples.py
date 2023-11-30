#!/usr/bin/python3
import sys
##########################################################################################
# MAPREDUCE EXAMPLE
# The following example seeks to average the number of sales over a company's employees.
# The dictionary, sales_data, is used to represent the retrieval of an employees sales data.
# Key is the employee ID, the value is their corresponding number of sales.
##########################################################################################
sales_data = {7:12, 5:33, 4:25, 8:26, 3:45, 1:34, 2:27, 10:36, 9:73, 6:35}

def mapper():
    for line in sys.stdin:
        employee_id = int(line.strip())
        attribute_quantity = sales_data[employee_id]
        print(attribute_quantity)

def reducer():
    total = 0
    count = 0
    for line in sys.stdin:
        attribute_quantity = int(line)
        total += attribute_quantity
        count += 1
    print(total/count)






####################################################################################################################
# MAPREDUCE EXAMPLE 2; COUNTING DIFFERENT PRODUCTS
# The following example seeks to average the number of sales over a company's employees by each individual product.
# The dictionary, sales_data2, is used to represent the retrieval of an employees sales data.
# The key is the employee ID, the value is a tuple of their sales numbers, i.e. (product1 sales, product2 sales, product3 sales)
####################################################################################################################
sales_data2 = {7:(12,15,74), 5:(33,14,36), 4:(25,22,84), 8:(26,11,35),
               3:(45,26,47), 1:(34,8,68), 2:(27,32,47), 10:(36,2,86), 9:(73,28,24), 6:(35,33,64)}

def mapper2():
    for line in sys.stdin:
        employee_id = int(line.strip())
        product_one_sales = sales_data2[employee_id][0]
        product_two_sales = sales_data2[employee_id][1]
        product_three_sales = sales_data2[employee_id][2]
        print(f"ProductOne,{product_one_sales}")
        print(f"ProductTwo,{product_two_sales}")
        print(f"ProductThree,{product_three_sales}")

def reducer2():
    key = None
    number_of_sales = 0
    count = 0
    for line in sys.stdin:
        tokens = line.strip().split(',')
        if key is None: #starting with nothing
            key = tokens[0]
            number_of_sales += int(tokens[1])
            count += 1

        elif tokens[0] == key: # continue counting current key
            number_of_sales += int(tokens[1])
            count += 1

        else: #found a new key. print and reset
            print(f"{key}, average: {number_of_sales/count}")
            key = tokens[0]
            number_of_sales = 0
            count = 0
            number_of_sales += int(tokens[1])
            count += 1
    #take care of last key
    if count > 0:
        print(f"{key}, average: {number_of_sales/count}")








####################################################################################################################
# Code entry point.
# Pass different arguments to use different functions
####################################################################################################################
def main():
    f = sys.argv[1]
    if f == 'm1':
        mapper()
    elif f == 'r1':
        reducer()
    elif f == 'm2':
        mapper2()
    elif f == 'r2':
        reducer2()



if __name__ == "__main__":
    main()




