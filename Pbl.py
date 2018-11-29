#Jamie Cooper - x00155152
LOWER = 10000
MIDDLE = 20000
UPPER = 50000
ALLOWANCE = 15000


list_pps = []
list_net = []
a_counter = 0
b_counter = 0
c_counter = 0
d_counter = 0
b_tax = 0
c_tax = 0
d_tax = 0

employees = int(input("Enter number of employees:"))
for iteration in range(employees):
    print("Employee", iteration + 1)
    pps = str(input("PPS Number:"))
    list_pps.append(pps)
    gross_pay = int(input("Gross Pay:"))
    print(pps, "has gross pay of €", gross_pay)
    if gross_pay <= LOWER:
        tax = 0
        a_counter +=1
    elif gross_pay <= MIDDLE:
        tax = (gross_pay - LOWER) * 0.3
        b_counter +=1
        b_tax += tax
    elif gross_pay <= UPPER:
        tax =(gross_pay - LOWER) * 0.35
        c_counter += 1
        c_tax += tax
    else:
        tax = (gross_pay - ALLOWANCE) * 0.4
        d_counter += 1
        d_tax += tax
    net_pay = (gross_pay - tax)
    list_net.append(net_pay)
    print("Paid tax of €", tax, "and has net pay of €", net_pay)
print("--------------------")
print("PPS Number         Net Pay")
for i in range(employees):
    print(list_pps[i], "           ", list_net[i])
print("--------------------")
print("Tax paid in each bracket")
print("Bracket B    €", b_tax)
print("Bracket C    €", c_tax)
print("Bracket D    €", d_tax)
print("--------------------")
print("Number in each bracket")
print("Bracket A     ", a_counter)
print("Bracket B     ", b_counter)
print("Bracket C     ", c_counter)
print("Bracket D     ", d_counter)
