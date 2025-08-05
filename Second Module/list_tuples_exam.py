fruits = ['abacaxi', 'maçã', 'limão', 'maracujá', 'morango', 'laranja']
fruits_tuple = tuple(fruits)
for fruit in fruits_tuple:
    print(f"Fruta {fruits_tuple.index(fruit)+1} = {fruit}")
