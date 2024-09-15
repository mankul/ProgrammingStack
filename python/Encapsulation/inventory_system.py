# dunder variables in python are private variables.

class Product:
    def __init__(self):
        print("PRODUCT TYPE")
        self.__maxPrice=900
        self.discount=10

    def sellingPrice(self):
        print("Selling price is {}".format(self.__maxPrice))

    def setSellingPrice(self, price):
        self.__maxPrice = price
    
    def getDiscount(self):
        print("Discount is {}".format(self.discount))

    def setDiscount(self, discount):
        self.discount=discount

class SportsProduct(Product):
    def __init__(self):
        print("SPORTS PRODUCT TYPE")
        super().__init__()


def main():
    spr = SportsProduct()
    pr = Product()
    spr.getDiscount()
    spr.__maxPrice=1200
    spr.discount=15
    spr.getDiscount()
    spr.sellingPrice()
    spr.setDiscount(25)
    spr.setSellingPrice(1500)
    spr.sellingPrice()
    pr.getDiscount()

if __name__ == "__main__":
	main()
	
