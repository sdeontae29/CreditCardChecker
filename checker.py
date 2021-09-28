import math 

def validate(number):
  checker = 0
  added_product = 0
  i = 1
  j = 1
  num_list = [(number//(10**i))%10 for i in range(math.ceil(math.log(number, 10))-1, -1, -1)]
  s_t_l = len(num_list) - 2
  last_index = len(num_list) - 1

  while i < len(num_list):
    checker = num_list[s_t_l] * 2
    if checker <= 9:
      added_product += checker 
    else:
      added_product += checker % 10
      added_product += checker // 10
    s_t_l -= 2
    i += 2

  while j < len(num_list)+1:
    added_product += num_list[last_index]
    last_index -= 2
    j += 2
  
  if added_product % 10 != 0:
    return 'Invalid'
  else:
    if num_list[0] == 4 and len(num_list) in range(13,17):
      return "Visa"
    elif num_list[0] == 5 and num_list[1] in range(1,6):
      return "Mastercard"
    elif num_list[0] == 3 and (num_list[1] == 4 or num_list[1] == 7):
      return "Amex"
    else:
      return "Almost"



