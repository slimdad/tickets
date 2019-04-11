#-------------------------------------------------------------------------------
# Name:        356 Pearce
# Purpose:     Calculate ticket prices
#
# Author:      Zachary Pearce
#
# Created:     20/02/2019
# Copyright:   (c) Zach 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#begin
def main():

    #Initialize
    APRICE = 15.75
    BPRICE = 12.75
    CPRICE = 9.75
    EXPENSES = 0.07

    #Input
    numA = int(input("Enter the number of tickets for Section A"))
    numB = int(input("Enter the number of tickets for Section B"))
    numC = int(input("Enter the number of tickets for Section C"))

    #Process
    totalA = numA * APRICE
    totalB = numB * BPRICE
    totalC = numC * CPRICE
    Proceeds = (totalA + totalB + totalC)
    Tax = Proceeds * EXPENSES
    Profit = Proceeds - Tax

    #Output
    print("The income from ticket sales:")
    print("------------------------------")
    print("Section A: $ ", format(totalA, "5.2f"))
    print("Section B: $ ", format(totalB, "5.2f"))
    print("Section C: $ ", format(totalC, "5.2f"))
    print("------------------------------")
    print("Proceeds:  $ ", format(Proceeds, "5.2f"))
    print("Expenses:  $ ", format(Tax, "5.2f"))
    print("------------------------------")
    print("Profits:   $ ", format(Profit, "5.2f"))

main()
input()
#end







