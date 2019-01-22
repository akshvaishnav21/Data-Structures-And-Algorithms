number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))



try:
  # Call the function below...
	print(linear_search(number_list, 100))
except ValueError as error_message:
  print("{0}".format(error_message))
