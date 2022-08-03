
import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

try:
    class Money():
        recipt = []
        def __init__(self):
            self.__totalMoney = 0
        
        def take_money(self,cost,order):
            money = int(input())
            if money == cost:
                print("Here's your ",(order.title()),"\nEnjoy")
                self.__totalMoney += cost
                logger.info(f'order {order}, cost ${cost},money ${self.__totalMoney}')
                Money.recipt.append({"order":order,"cost":cost})
                Money.recipt.append({"order":order,"cost":cost})
                return True

            elif money >= cost:
                refund = money - cost
                print("Here's your change $",refund)
                print("Here's your ",(order).title(),"\nEnjoy")
                self.__totalMoney += cost
                logger.info(f'money refunded ${refund}')
                logger.info(f'order {order}, cost ${cost},money ${self.__totalMoney}')
                Money.recipt.append({"order":order,"cost":cost})
                return True
                
            elif money <= cost:
                print("Insufficient funds!!!")
                logger.error("Insufficient Funds")
            else:
                ("enter correctly")

    class Vending(Money):
        

        def __init__(self):
            super().__init__()
            self.__sales = 0

        def snacks(self):
            print("1.Lays")
            print("2.Kurkure")
            print("3.Aloo Bhujya")
            print("4.Cookies")
            print("5.Salted Peanuts")
            choice = input()
            if choice.lower() == "lays":
                print("Plese give $1")
                if self.take_money(1,"lays"):
                    self.__sales += 1
                

            if choice.lower() == "kurkure":
                print("Plese give $1")
                if self.take_money(1,"kurkure"):
                    self.__sales += 1
            if choice.lower() == "aloo Bhujya":
                print("Plese give $2")
                if self.take_money(2,"aloo bhujya"):
                    self.__sales += 1
            if choice.lower() == "Cookies":
                print("Plese give $2")
                if self.take_money(2,"Cookies"):
                    self.__sales += 1
            if choice.lower() == "salted peanuts":
                print("Plese give $3")
                if self.take_money(3,"salted peanuts"):
                    self.__sales += 1
            
            
        def beverages(self):
            print("1.Coke")
            print("2.Pepsi")
            print("3.RedBull")
            print("4.Sting")
            print("5.Mountain Dew")
            choice = input()
            if choice.lower() == "coke":
                print("Plese give $1")
                if self.take_money(1,"coke"):
                    self.__sales += 1
            if choice.lower() == "pepsi":
                print("Plese give $1")
                if self.take_money(1,"pepsi"):
                    self.__sales += 1
            if choice.lower() == "redbull":
                print("Plese give $3")
                if self.take_money(3,"redbull"):
                    self.__sales += 1
            if choice.lower() == "sting":
                print("Plese give $4")
                if self.take_money(4,"sting"):
                    self.__sales += 1
            if choice.lower() == "mountain dew":
                print("Plese give $2")
                if self.take_money(2,"mountain dew"):
                    self.__sales += 1
           
        def ciggratte(self):
            print("1.Duke")
            print("2.Dunhill")
            print("3.Flake")
            print("4.Eclipse")
            print("5.Elita")
            choice = input()
            if choice.lower() == "duke":
                print("Plese give $1")
                if self.take_money(1,"duke"):
                    self.__sales += 1
            if choice.lower() == "dunhill":
                print("Plese give $2")
                if self.take_money(2,"dunhill"):
                    self.__sales += 1
            if choice.lower() == "flake":
                print("Plese give $3")
                if  self.take_money(3,"flake"):
                    self.__sales += 1
            if choice.lower() == "eclipse":
                print("Plese give $4")
                if self.take_money(4,"eclipse"):
                    self.__sales += 1
            if choice.lower() == "elita":
                print("Plese give $5")
                if self.take_money(5,"elita"):
                    self.__sales += 1
            
            
            
        def lottery(self):
            print("1. $5 Lottery ticket")
            print("2. $50 Lottery ticket")
            print("3. $100 Lottery ticket")
            print("4. $500 Lottery ticket")
            print("5. $1000 Lottery ticket")
            choice = input()
            if choice.lower() == "1":
                print("Plese give $5")
                if self.take_money(5,"lottery ticket"):
                    self.__sales += 1
            if choice.lower() == "2":
                print("Plese give $50")
                if self.take_money(50,"lottery ticket"):
                    self.__sales += 1
            if choice.lower() == "3":
                print("Plese give $100")
                if self.take_money(100,"lottery ticket"):
                    self.__sales += 1
            if choice.lower() == "4":
                print("Plese give $500")
                if self.take_money(500,"lottery ticket"):
                    self.__sales += 1
            if choice.lower() == "5":
                print("Plese give $1000: ")
                if self.take_money(1000,"lottery ticket"):
                    self.__sales += 1
           

            
        def sales(self):
            logger.info("Asked for sales")
            return self.__sales
except Exception as e:
    print(e)  
except Warning as e:
    print(e)                
