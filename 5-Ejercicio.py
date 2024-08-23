class Control_estudiante:
    def __init__(self, codigo = 0, nombre = "", apellido  = "", edad = 0, nota = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota

    def entrada_datos(self):
        self.codigo = int(input("Ingrese su codigo: "))
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = int(input("Ingrese su edad: "))
        self.nota = float(input("Ingrese su nota obtenida: "))
        print("--------------------------------------")

    def muestreo_datos(self):
        print("Código del alumno:", self.codigo)
        print("Nombre del alumno:", self.nombre)
        print("Apellido del alumno:", self.apellido)
        print("Edad del alumno:", self.edad)
        print("Nota del alumno:", self.nota)
        print("--------------------------------------")

    def resultado_datos(self):
        if self.nota <=5:
            print(f"Lo sentimos, {self.nombre}, usted a reprobado")
        else:
            print(f"Felicidades, {self.nombre}, usted aprobo con exito")
        print("--------------------------------------")

estudiante = Control_estudiante() #Creamos nuestra instancia
estudiante.entrada_datos() #Entrada de datos
estudiante.muestreo_datos() #Muestreo de datos obtenidos
estudiante.resultado_datos() #Estado del alumno dependiendo de su nota
