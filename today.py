from datetime import date, timedelta
y, m, d = map(int, input("Enter date (YYYY MM DD): ").split())
t = date(y, m, d)

print("Yesterday:", t - timedelta(1))
print("Today:", t)
print("Tomorrow:", t + timedelta(1))

~                                                                             
~                                                                             
~                                                                             
~                                                                             
~                                                                             
~         
