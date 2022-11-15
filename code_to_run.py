import src.LinkedList as LL
Movies = LL.Movies()
Usuarios = LL.User()
while __name__ == '__main__':
    resp = 0
    while resp != 5:
        resp = input("1.Ver peliculas disponibles\n2.Agregar pelicula\n3.Comprar entrada\n4.Registrarse\nElija una opcion: \n")
        if resp == "1":
            pass
        elif resp == "2":
            MovieName = input("Nombre de la pelicula: ")
            Date = input("Fecha de la pelicula: ")
            Time = input("Hora de la pelicula")
            Movies.addMovie(MovieName, Time, Date)
            print("La pelicula se agrego")
        elif resp == "3":
            tempUser = input("Digite su usuario: ")
            if Usuarios.searchUser(tempUser):
                silla = input("Que silla desea: ")
                pelicula = input("Que pelicula desea: ")
                hora = input("Que hora desea: ")
                Usuarios.buySeat(silla, pelicula, tempUser)
                print("Gracias por comprar en cine Toro!")
        elif resp == "4":
            Name = input("Digite su nombre: ")
            seatPref = input("Digite su silla favorita: ")
            Usuarios.AddUserNode(Name, seatPref, None)
            print("Gracias por registrarse!")