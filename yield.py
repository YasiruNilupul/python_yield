num = int(input())

def show_decimal(num):
    decimal_list = []
    for i in range(1,num + 1):
        decimal_list.append(i)
        yield i
    #return decimal_list

def show_octal(num):
    #octal_list = []
    octal_num = []
    while True:
        if num ==0:
            break
        elif num % 2 == 0:
            octal_num.insert(0,0)
        elif num % 2 == 1:
            octal_num.insert(0,1)
        
        num = num // 2
    return [str(x) for x in octal_num]
# print("".join(show_octal(num)))

number = show_decimal(num)

for i in number:
    binary = show_octal(i)
    print("".join(binary))
