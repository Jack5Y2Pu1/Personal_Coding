import re
import os
def extract_number_with_two_decimal_places(string):
    # 使用正则表达式找到所有数字，包括小数点
    error_msg = 'your input not include number!'
    match = re.search(r'(\d+(\.\d+)?)', string)
    
    if match:
        number_str = match.group(1)
        
        # 如果没有小数点，添加小数点和两个0
        if '.' not in number_str:
            number_str += '.00'
        else:
            # 分割整数和小数部分
            integer_part, decimal_part = number_str.split('.')
            
            # 保持小数点后两位，如果有多余位数，直接截断
            decimal_part = decimal_part[:2]
            
            # 重新组合整数和小数部分
            number_str = f"{integer_part}.{decimal_part}"
            
        return number_str
    else:
        # 如果字符串中没有数字，则返回error_msg
        return error_msg

print("Tip: Please input the string to be extract, and input 'quit' to exit the program!")
# 测试函数
while True:
    input_string = input("pls input your string('quit' to end job):\n")
    if input_string == 'quit':
        break
    else:
      print('the result is:',extract_number_with_two_decimal_places(input_string))

#os.system('pause')