print("enter price")
price = input()
print("enter dicount %")
discount = input()
discountprice = float(price) * float(discount)/100
discounttotal = float(price) - float(discountprice)
tax = 0.13 * float(discounttotal)
total = tax + float(discounttotal)
roundtotal = "{:.2f}".format(total)
roundtax = "{:.2f}".format(tax)
rounddiscounttotal = "{:.2f}".format(discounttotal)
print ("your discounted price is $" + str(rounddiscounttotal))
print ("and the tax is $" + str(roundtax))
print ("the total price of your purchace is $" + str(roundtotal))