from context_manager_exp import myopenfunc

with myopenfunc("data.txt", "r") as myfile:
  data = myfile.read()
  print(data)