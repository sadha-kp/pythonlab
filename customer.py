def simple_interest(p, t, senior):
    rate = 12 if senior else 10
    interest = (p * t * rate) / 100
    return interest

p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
senior_input = input("Is the customer a senior citizen (yes/no)? ").lower()

senior = senior_input == "yes"
si = simple_interest(p, t, senior)
print("Simple Interest =", si)

~                                                                                                                                                             
~      
