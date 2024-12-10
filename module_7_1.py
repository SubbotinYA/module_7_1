class Product:
    def __init__(self,name:str,weight:float,category:str):
        self.name=name
        self.weight=weight
        self.category=category

    def __str__(self):
        return (f'{self.name}; {self.weight}; {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self)->str:
        """
        функция считывает состояние и возвращает информацию, записанную в файле products.txt
        """
        file= open(self.__file_name,'r')
        product=file.read()
        file.close()
        return product

    def add(self, *products)->str:
        """
       функция добавляет объекты от класса Product в файл products.txt
        """
        file = open(self.__file_name, 'a')
        for str_ in products:
            if not isinstance(str_, Product):
                print(f'добавляемый объект {str_} не принадлежит классу Product')
                continue
            elif str(str_) in self.get_products():
                print(f"Продукт {str(str_)} уже есть в магазине")
            else:
                file.write(str(str_) + '\n')
        file.close()







s1 = Shop()
p1 = Product('Meat', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())