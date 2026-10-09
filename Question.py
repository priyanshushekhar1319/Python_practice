# Python Lab Examination Instructions 
# •Write a separate Python function for every question.
# • Call each function to demonstrate its output. 
# • Use real-life data and appropriate list, tuple, and dictionary operations.
# • Avoid writing the entire solution as a single block of code. 
# • Create VE and put all answers 
# • Submit only Github link 
# Question 1: Student Marks Analysis A college stores students' marks in a list.
# Write a function that accepts a list of marks and 
# displays the highest mark, lowest mark, average mark, and number of students who passed (marks of 40 or above). 
def student_marks_anaysis(marks):
    highest_mark=max(marks)
    lowest_mark=min(marks)
    average_marks=sum(marks)/len(marks)
    passed_students=len([marks for marks in marks if marks>=40])
    print("Highest Mark:",highest_mark)
    print("Lowest Mark:",lowest_mark)
    print("Average Mark:",average_marks)
    print("Number of student passed:",passed_students)
# marks = list(map(int, input("What are your marks? Enter marks separated by spaces: ").split()))

# student_marks_anaysis(marks)

'''
Question 2: Online Mobile Store An online store maintains a list of mobile prices. 
Write a function to display all mobiles costing more than ₹20,000, 
calculate the total inventory value, and find the most expensive mobile price. 
'''
def mobile_store_analysis(prices):
    expensive_mobiles = [price for price in prices if price > 20000]
    total_inventory_value = sum(prices)
    most_expensive_mobile = max(prices)
    print("mobiles costing more than Rs. 20000:", expensive_mobiles)
    print("Total inventory value:", total_inventory_value)
    print("Most expensive mobile price:", most_expensive_mobile)

# price = list(map(int, input("what aref the mobile prices? Enyer the prices ").split()))
# mobile_store_analysis(price)

'''
Question 3: Shopping Cart Management 
A customer adds products to a shopping cart. 
Write a function that accepts a list of product names and performs the following operations: 
• Add a new product. • Remove a purchased or unwanted product. 
• Display the final cart. • Count the total number of products. 
'''
def shopping_cart_management(cart):
    while True:
        print("\nSHopping cart management")
        print("1 Add a new product")
        print("2 Remove a purchased productt")
        print("3 Display the final cart")
        print("4 count the toatl products")
        print("5 Eixt")
        choice = int(input("enter your choice buddy: "))
        if choice == 1:
            new_product = input("enter the new product name:")
            cart.append(new_product)
        elif choice == 2:
            remove_product = input("enter the product to remove:")
            if remove_product in cart:
                cart.remove(remove_product)
            else:
                print("product is not buddy ")
        elif choice == 3:
            print("final cart:",cart)
        elif choice == 4:
            print("totaal numbet of products:",len(cart))
        elif choice == 5:
            break
shopping_cart =[]
# shopping_cart_management(shopping_cart)

'''
Question 4: Employee Salary Analysis
 A company stores employee salaries in a list.
 Write a function to calculate the average salary, 
 display salaries above the average, and increase every salary by 10%. 

'''
def employee_salary_analysis(salaries):
    average_salary = sum(salaries)/len(salaries)
    avove_average_salaries = [salary for salary in salaries if salary > average_salary]
    increased_salaries = [salary * 1.10 for salary in salaries]
    print("Aberage salary:",average_salary)
    print("salaries aboove the average:",avove_average_salaries)
    print("increased salaries by 10%",increased_salaries)

employee_salaries = list(map(int,input("enter the employee salaries:").split()))
employee_salary_analysis(employee_salaries)

        






