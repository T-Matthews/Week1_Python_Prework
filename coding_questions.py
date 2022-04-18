#Question 1
def hello_name(username):
    print('hello_'+username.upper()+'!')

hello_name('username')

#Question 2
def first_odds():
    i=0
    while i<100:
        i+=1
        if i%2 == 1:
            print(i)
        else:
            continue

#Test question 2
first_odds()

#Question 3
def max_num_in_list(a_list):
    high_num= int(a_list.pop())
    while a_list:
        new_num = int(a_list.pop())
        if new_num > high_num:
            high_num = new_num
    print('The high number in this list is '+
        str(high_num)+'.')

#test code in question 3
test = [1,5,9,7,5,8]
max_num_in_list(test)

#Question 4
def is_leap_year(a_year):
    #If divisible by 400, is a leap year
    if int(a_year)%400 ==0:
        leap_year = True
    #If divisible by 4 but not 100, is leap year
    elif int(a_year)%4 == 0 and int(a_year)%100!=0:
        leap_year = True
    #any other condition is not leap year
    else:
        leap_year = False
    print(leap_year)

#test code for question 4
is_leap_year(2008)
   
#Question 5
def is_consecutive(a_list):
    val = int(a_list.pop())
    is_true = True
    while a_list:
        new_val = int(a_list.pop())
        if val - new_val != 1:
            is_true = False
            break
        else:
            val = new_val
    print(is_true)

#test code for question 5
test = [1,2,3,4,5,5]   
is_consecutive(test)

