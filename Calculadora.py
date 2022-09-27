class Calculadora():
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0


    def sumar(self):
        self.valor1 = int(input("Digite el primer numero a sumar\n"))
        self.valor2 = int(input("Digite un numero el segundo numero a sumar\n"))
        self.resultado = self.valor1+self.valor2
        print("El resultado de la suma es: ",self.resultado)


    def resta(self):
        self.valor1 = int(input("Digite el primer numero a restar\n"))
        self.valor2 = int(input("Digite un numero el segundo numero a restar\n"))
        self.resultado = self.valor1-self.valor2
        print("El resultado de la resta es: ",self.resultado)


    def multiplicacion(self):
        self.valor1 = int(input("Digite el primer numero a multiplicar\n"))
        self.valor2 = int(input("Digite el segundo numero a multiplicar\n"))
        self.resultado = self.valor1*self.valor2
        print("El resultado de la multiplicacion es: ",self.resultado)


    def division(self):
        self.valor1 = int(input("Digite el numero dividendo\n"))
        self.valor2 = int(input("Digite un numero divisor\n"))
        self.resultado = self.valor1/self.valor2
        print("El resultado de la division es: ",self.resultado)


    def verificaNumeroPrimo(self):
        self.valor1 = int(input("Digite el numero a verificar\n"))
        contador = 0
        recorrer = 2
        if self.valor1 > 1:
            while recorrer < self.valor1 and contador == 0:
                resto=self.valor1%recorrer
                if resto==0:
                    contador+=1
                recorrer+=1
            if contador==0:
                print("El #",self.valor1," es primo") 

            else:
                print("El #",self.valor1," no es primo") 

        else:
                print("El #", self.valor1, " no es primo") 


    def verificarNumeroPalindromo(self):
        self.valor1 = input("Digite el numero a verificar\n") 
        if self.valor1 == self.valor1[::-1]: 
            print("El #",self.valor1," es palindromo ") 
        else: 
            print("El #",self.valor1," no es palindromo ")


    def menu(self):
        while True: 
            print("******************Calculadora****************")
            print("1.Sumar")
            print("2.Restar")
            print("3.Multiplicar")
            print("4.Dividir")
            print("5.Verificar si el # es primo")
            print("6.Verificar si el # es palindromo")
            print("7.Salir")
            print("*********************************************")
            opcion = input("Digite su opcion\n") 

            if opcion == "1":
                self.sumar()
            elif opcion =="2":
                self.resta()
            elif opcion =="3":
                self.multiplicacion()
            elif opcion =="4":
                self.division()
            elif opcion =="5":
                self.verificaNumeroPrimo()
            elif opcion =="6":
                self.verificarNumeroPalindromo()
            elif opcion =="7":
                 break
            seguir=input("Seguir operando (s/n): ")
            if seguir == "n": 
                break




calcular = Calculadora() #instanciar

print (calcular.menu()) #Imprimir el menuo
