import mylib

sun = mylib.MyClass("Sunil")
aks = mylib.MyClass("Akshatha", 100)
sun.printname()
sun.printage()
aks.printname()
aks.printage()

obj = sun + aks
obj.printname()
obj.printage()
