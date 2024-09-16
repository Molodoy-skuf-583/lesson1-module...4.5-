def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()
test_function()
# inner_function() При попытке вызвать функцию inn_func за пределами ts_func мы получаем ошибку,
#т.к. функция в локальном пространстве существует только в момент выполнения тела ts_func.


        
