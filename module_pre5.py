def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")


    inner_function()
#inner_function() ------ Будет ошибка, находится в не зоны досягаемости
test_function()
