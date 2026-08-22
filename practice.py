# num = int(input("enter a number: "))
# check = True
# for i in range(2, int(num**0.5) + 1):
#     if(num % i == 0):
#         check = False
#         break

 if(check == True):
     print(f"{num} is a prime number")
 else:
     print(f"{num} is not a prime number")

#question 2
# m = int(input("enter a number: "))
# n = int(input("enter a power: "))
# print(m**n)

#question 3
# def check_even(num):
#     if(num % 2 == 0):
#         return True
#     else:
#         return False
    
# num = int(input("enter a number: "))
# check = check_even(num)
# print(check)

#question 4
# num = int(input("enter a number of series required: "))
# print("1 ", end="")
# for i in range(2, num+1):
#     if(i % 2 == 0):
#         print(f"- {i} ", end="")
#     else:
#         print(f"+ {i} ", end="")

#question 5
# string = input("enter : ")
# while True:
#     print("1. find the frequency of a character in a string ")
#     print("2. replace a character by another in a string ")
#     print("3. remove the first occurrence of a character from string ")
#     print("4. remove all occurrence of a character from a string ")
#     print("5. Exit ")

#     option = int(input("enter a option: "))

#     if(option == 1):
#         print(len(string))
#     elif(option == 2):
#         char1 = input("enter a old character for replace: ")
#         char2 = input("enter a new character for replace: ")
#         print(string.replace(char1, char2))

#     elif(option == 3):
#         char = input("enter a character for remove: ")
#         index = string.find(char)
#         string2 = string[:index] + string[index+1:]
#         print(string2)

#     elif(option == 4):
#         char3 = input("enter a character for remove all occurrence: ")
#         print(string.replace(char3, ""))

#     elif(option == 5):
#         break

#     else:
#         print("Invalid input")


#question 6 
# str1 = input("enter a string 1 : ")
# str2 = input("enter a string 2 : ")
# print(str1.find(str2))

#question 7 
# import numpy as np
# arr1 = np.array([0, 0, 0, 0])
# arr2 = np.array([5,6,7,8])
# print(arr1*arr2)
# print(np.max(arr_1d))
# print(np.min(arr_1d))
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix)

# for i in range(4):
#     a = int(input("enter a number: "))
#     arr1[i] = a
# print(arr1)

#question 8 
# def check_sentence(sentence):
#     sentence = sentence.lower()
#     check_list = set(sentence.split(" "))
#     dict_list = {}
#     for word in check_list:
#         dict_list.update({word: sentence.count(word)})
#     return dict_list

# name = input("enter a sentence: ")
# sen = check_sentence(name)
# print(sen)
        
#question 9 
# t1 =(1,2,5,7,9,2,4,6,8,10)
# while True:
#     print("\n1. Divide the tuple in half")
#     print("2. Print all even number")
#     print("3. concatenate two tuples")
#     print("4. find maximum and minimum value")
#     print("5. Exit ")

#     option = int(input("enter a option: "))

#     if(option == 1):
#         mid = len(t1) // 2
#         for i in range(len(t1)):
#             print(t1[i], end = " ")
#             if i == mid-1:
#                 print()
#     elif(option == 2):
#         t3 = ()
#         for i in t1:
#             if(i % 2 == 0):
#                 t3 += (i,)
#         print(t3)
#     elif(option == 3):
#         t2 = (11,13,15)
#         print(t1+t2)
#     elif(option == 4):
#         print(f"max value: {max(t1)}")
#         print(f"min value: {min(t1)}")
#     elif(option == 5):
#         break
#     else:
#         print("Invalid input")

#question 10 
def read_line():
    pass

#questionn 11
# try:
#     num = int(input("enter a number: "))
#     print(num / 0)
# except:
#     print("division by zero is not possible")

#question 12
# def check_num(number: list[int]):
#     seen = set()
#     for num in number:
#         if num in seen:
#             raise ValueError(f"Duplicate number found: {num}")
#         seen.add(num)

# try :
#     check_num([1,2,3,4,5,6,5,7,8])
# except ValueError as e:
#     print(f"Error caught: {e}")

#question 13
# import numpy as np
# import matplotlib.pyplot as plt

# # Function to plot sine curve
# def plot_sine():
#     x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
#     y = np.sin(x)
#     plt.plot(x, y, label="sin(x)")

# # Function to plot cosine curve
# def plot_cosine():
#     x = np.linspace(-2 * np.pi, 2 * np.pi, 400)     
#     y = np.cos(x)
#     plt.plot(x, y, label="cos(x)")

# # Function to plot polynomial curve
# def plot_polynomial():
#     x = np.linspace(-5, 5, 400)
#     y = x**3 - 4*x**2 + x + 6
#     plt.plot(x, y, label="x³ - 4x² + x + 6")

# # Function to plot exponential curve
# def plot_exponential():
#     x = np.linspace(-2, 2, 400)
#     y = np.exp(x)
#     plt.plot(x, y, label="e^x")

# # Main function
# def main():
#     plt.figure(figsize=(10, 10))

#     plot_sine()
#     plot_cosine()
#     plot_polynomial()
#     plot_exponential()

#     plt.title("Sine, Cosine, Polynomial and Exponential Curves")
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")
#     plt.grid(True)
#     plt.legend()
#     plt.show()

# # Run the program
# if __name__ == "__main__":
#     main()



#-------------------------------------------------------------
#practice
# x= [1,2,3,4,5]
# y1 = [10,20,30,40,50]
# y2 = [20,30,45,50,55]

# plt.plot(x, y1, label="sales 2024")
# plt.plot(x, y2, label="sales 2025")

# plt.title("Sales Graph")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()
#--------------------------------------------------------------

#question 14
# import matplotlib.pyplot as plt
# num = int(input("enter the number of month: "))
# profit = []
# months = []
# for i in range(num):
#     pro1 = input("enter a profit of the month: ")
#     mon1 = input("enter the month of profit: ")
#     profit.append(float(pro1))
#     months.append(mon1)

# plt.plot(months, profit,marker='o', label="Company Profit")
# plt.title("company ABC")
# plt.xlabel("Month Number")
# plt.ylabel("Total Profit")
# plt.grid(True)
# plt.legend()
# plt.show()
