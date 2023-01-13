Employee_name='Ram'
age=55
Height=150.6
# Identifying data type
print(type(Employee_name),type(age),type(Height))

# Verifying datatypes
print(type(Height) is int)

# Coerce
ht=int(Height)
print(type(ht))
Height=int(Height)
print(Height)

Salray_tier='1'
Salray_tier=int(Salray_tier)
print(type(Salray_tier))
Employee_name=float(Employee_name)
print(type(Employee_name))