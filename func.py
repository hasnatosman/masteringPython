# function is a block of code that performs a specific task.

def cal_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp_list = [100, 200, 300]
joe_exp_list = [200, 300, 400]
tom_total = cal_total(tom_exp_list)
joe_total = cal_total(joe_exp_list)

print("Tom's total expense ", tom_total)
print("Joe's total expense ", joe_total)
