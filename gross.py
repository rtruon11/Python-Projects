gross_pay = float(input('How much $$$$$'))


if (gross_pay <= 20000):
    print ('taxed at 15%')
    tax = (gross_pay * 0.15)

elif (20000 < gross_pay <= 40000):
    print ('taxed at 20%')
    tax = ((20000 * 0.15 ) * (gross_pay - 20000) * 0.20)

else:
    tax = ((20000 * 0.15 ) * (20000 * 0.20) * (gross_pay - 40000 * 0.25))

net_pay = gross_pay - tax

print ('Net Pay = ', net_pay)
print ('IRS sucker = ', tax)
