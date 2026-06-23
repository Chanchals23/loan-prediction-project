
# salary = int(input("enter the salary :"))

# if (salary<30,000):
#     print("final tax rate is 5%")
# elif (salary>=30,000 and salary<=70000):
#     print("final tax rate is 15%")
# else :
#     print("final tax rate is 25%")


# def number(a,b):
#     result=[]
#     for i in range (a,b+1):
#         if (i%2==0):
#             result.append(i)
#     return result
   
    
# print(number(2,9))



# def count_digits(n):
#     return len(str(abs(n)))

# print(count_digits(34466768))

# or

# def count_digits(n):
#     count=0
    

#     n-abs(n)

#     if n==0:
#         return 1
    
#     while n>0:
#         n=n//10
#         count+=1

#     return count

# print(count_digits(233456))


       
# def sum_digits(n):
#     total=0
#     n=abs(n)

#     while n>0:
#         total+=n%10
#         n=n//10
#     return total

# print(sum_digits(1234))

# or

# def sum_of_digits(n):
#     return sum(int(d) for d in str(abs(n)))




# for i in range(1,101):
#     if (i%3==0 and i%5==0):
#         print(i)
         

# while True:
#     user_input = input("Enter a number (or 'Quit' to stop): ")
    
#     if user_input == "Quit":
#         break
    
#     n = int(user_input)
#     if n > 0:
#         print("Positive")
#     elif n < 0:
#         print("Negative")
#     else:
#         print("Zero")


# def cal(a,b,operation):
#     if operation=="+":
#         return a+b
#     elif operation=="-":
#         return a-b
#     elif operation=="*":
#         return a*b
#     elif operation=="/":
#         if b==0:
#             return "error"
#         return a/b
#     else:
#         return"invalid operation"
    

# print(cal(8,7,"+"))




# def is_prime(n):
#     if n<2:
#         return False

#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True

# print(is_prime(7))


# or
    
# secret_number = 42
# while True:
#     guess = int(input("Guess the number: "))
    
#     if guess > secret_number:
#         print("Too high")
#     elif guess < secret_number:
#         print("Too low")
#     else:
#         print("Correct!")
#         break
     


   

