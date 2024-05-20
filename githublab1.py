minute = eval(input("Please input minutes: "))

print(f'{minute} minutes is aproximately {(years := minute//525600)} years and {(days := minute%(525600)//1440)} days')



