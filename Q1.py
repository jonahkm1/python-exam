def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15): #Create the function that calculates the net salary
	'''This functions returns the net salary by finding the gross salary and deducting the tax'''
	return (hourly_rate * hours_worked)-((hourly_rate * hours_worked)*0.15)

hourly_rate == 500
hours-worked == 40
print(f"Your net salary is ", calculate_salary)

