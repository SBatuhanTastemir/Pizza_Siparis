import csv
import sys
from datetime import datetime

# Menu.txt dosyası oluşturma
with open('Menu.txt', 'w') as file:
    file.write('* Pizza Seçiniz: \n1: Klasik \n2: Margherita \n3: Türk Pizza \n4: Dominos Pizza \n* Sosunuzu Seçin: \n11: Zeytin \n12: Mantar \n13: Keçi Peyniri \n14: Et \n15: Soğan \n16: Mısır \n* Teşekkür Ederiz :)')

# Log dosyası oluşturma
log_file = open('pizza_order.log', 'w')

# Başlangıç saati logu
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file.write(f"Program başlatıldı: {start_time}\n")

# Pizza superclass
class Pizza:
    def __init__(self):
        self.description = " Pizza Sınıfı oluşturuldu,"

    def get_description(self):
        return self.description

    def get_cost(self):
        return float(self.cost)
        pass


# Pizza subclasses
class Classic(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza, "
        self.cost = 50.0

    def get_cost(self):
        return self.cost


class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza, "
        self.cost = 60.0

    def get_cost(self):
        return self.cost


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza, "
        self.cost = 70.0

    def get_cost(self):
        return self.cost


class DominosPizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza, "
        self.cost = 80.0

    def get_cost(self):
        return self.cost

# Decorator superclass
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


# Sos subclasses
class Sossuz(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 0
        self.description = "Sossuz ,"

class Olives(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 10.0
        self.description = "Zeytin ile,"


class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 10.0
        self.description = "Mantar ile,"


class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 15.0
        self.description = "Keçi Peyniri ile,"


class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 20.0
        self.description = "Et ile,"


class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 10.0
        self.description = "Soğan ile"


class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 5.0
        self.description = "Mısır ile,"
        
#Boy Subclass
class Small(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 0.0
        self.description = "Küçük Boy"

class Medium(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 20.0
        self.description = "Orta Boy"

class Large(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 30.0
        self.description = "Büyük Boy"        

# Main Fonksiyon Oluşturma 
def main():
    # Print the menu
    print("Pizza Menu")
    print("==========")
    print("Pizza Seçiniz :")
    print("1: Klasik")
    print("2: Margherita")
    print("3: Türk Pizza")
    print("4: Dominos Pizza ")
    print("==========")
    print("Sos Seçiniz :")
    print("00: Sos İstemiyorum")
    print("11: Zeytin")
    print("12: Mantar")
    print("13: Keçi Peyniri")
    print("14: Et")
    print("15: Soğan")
    print("16: Mısır")
    print("==========")
    print("Boy Seçiniz")
    print("111: Küçük")
    print("222: Orta")
    print("333: Büyük")
    print("Teşekkür Ederiz :) ")
    print()

    # Kullanıcıdan pizza ve sos girdisi almak
    pizza_choice = int(input("Kaç Numaralı Pizzayı İstersiniz: "))
    sauce_choice = int(input("Kaç Numaralı Sosu İstersiniz: "))
    pizza_size = int(input("Kaç Numaralı Boyu İstersiniz: "))

    # Pizza Seçimi

    if pizza_choice == 1:
        pizza = Classic()
    elif pizza_choice == 2:
        pizza = Margherita()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = DominosPizza()
    else:
        print("Yanlış Bir Pizza Numarası Seçtiniz. ")
        
        return

    # Sos Seçimi
    
    if sauce_choice == 00:
        pizza = Sossuz(pizza)
    elif sauce_choice == 11:
        pizza = Olives(pizza)
    elif sauce_choice == 12:
        pizza = Mushrooms(pizza)
    elif sauce_choice == 13:
        pizza = GoatCheese(pizza)
    elif sauce_choice == 14:
        pizza = Meat(pizza)
    elif sauce_choice == 15:
        pizza = Onions(pizza)
    elif sauce_choice == 16:
        pizza = Corn(pizza)
    else:
        print("Yanlış Bir Sos Numarası Seçtiniz")
        return
    # Boy Seçimi
    if pizza_size == 111:
      pizza = Small(pizza)
    elif pizza_size == 222:
      pizza = Medium(pizza)
    elif pizza_size == 333:
      pizza = Large(pizza)
    else:
      print("Yanlış Bir Boy Numarası Seçtiniz")
      return
    # Toplam Hesap
    total_cost = pizza.get_cost()
    print("Toplam Fiyat: ", total_cost ,"TL")

    # Kullanıcı Bilgisi Almak
    name = input("Lütfen Ad-Soyad Giriniz: ")
    adress = input("Lütfen Adresinizi Giriniz: ")
    credit_card_number = input("Lütfen Kredi Kartı Numaranızı Giriniz: ")
    credit_card_cvc = input("Lütfen CVC2 Numaranızı Giriniz: ")

    

    # Siparişi Database de saklamak
    with open('Sipariş_Database.csv', mode='a', newline='') as database_file:
        order_writer = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        timestamp = datetime.now()
        order_writer.writerow([name, adress, credit_card_number, credit_card_cvc, pizza.get_description(),
                               total_cost, timestamp])

# Main Fonksiyonu Çalıştıma
if __name__ == '__main__':
    main()