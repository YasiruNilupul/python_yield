num = int(input())
def show_decimal(num):
    decimal_list = []
    for i in range(1,num + 1):
        decimal_list.append(i)
        yield i
    #return decimal_list

def show_octal(num):
    octal_list = []
    octal_num = []
    while True:
        if num % 2 == 0:
            octal_num.insert(0,1)
        elif num % 2 == 1:
            octal_num.insert(0,1)
        elif num ==0:
            break
        num = num // 2
    return octal_num
number = show_decimal(num)
for i in number:
    binary = show_octal(i)
    print(binary)
        
    
  

