from vendingMachine import Vending   
from vendingMachine import Money    
try:      
    vend = Vending()    
    while True:    
        print("1.SNACKS")
        print("2.DRINK")
        print("3.CIGGRATTE")
        print("4.LOTTERY TICKET")
        print("5.EXIT")

        choice = input()
        if choice == "1":
            vend.snacks()
        if choice == "2":
            vend.beverages()
        if choice == "3":
            vend.ciggratte()
        if choice == "4":
            vend.lottery()
        if choice == "5":
            y = input("Do You want Recipt? ")
            if y.lower() == "yes":
                x = Money.recipt
                if len(x) > 0:
                    for i in x:
                       
                        print(f'order - {i["order"]} & price - {i["cost"]}')
                    print("Hello World!")
                    break
                else:
                    print("U didnt buy anything idiot!!!")
                    print("Hello World!")
                    break
            else:
                print("Hello World!")
                break

        if choice == "sales":
            print(vend.sales())
            
       
except Exception as e:
    print(e)        