class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)
class User(Nodo):
    def __init__(self, data, SeatPref, SeatsBuyed):
        super().__init__(data)
        self.SeatPref = SeatPref
        if self.SeatsBuyed == None:
            self.SeatsBuyed = ""
        else:
            self.SeatsBuyed = SeatsBuyed    
class Seat(Nodo):
    def __init__(self, data):
        super().__init__(data)
        self.Position = ""
        self.State = False
class LinkedList:
    def __init__(self): 
        self.PTR = None
        self.ULT = None
    def __repr__(self):
        resp = ""
        P = self.PTR
        while P!= None:
            resp = resp + str(P.data) + " -> "
            P = P.next
        resp = resp + "None"
        return resp
class Movie(LinkedList):
    def __init__(self, Movie, Time, Date):
        super().__init__()
        self.MovieName = Movie
        self.Time = Time 
        self.Date = Date
    def AddSeatNode(self, data):
        P = Seat(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else: 
            self.ULT.next = P
            self.ULT.next = P
    def fillSeatList(self, QuantityRegular, QuantityVIP):
        P = self.PTR
        i = 1
        while P != None:
            if QuantityRegular != 0:
                self.AddSeatNode(i+"R")
                P.data = "Regular"
                P = P.next
                i = i + 1
                QuantityRegular = QuantityRegular - 1
                if QuantityRegular == 0:
                    i = 1
            elif QuantityVIP != 0:
                self.AddSeatNode(i+"VIP")
                P.data = "VIP"
                P = P.next
                QuantityVIP = QuantityVIP - 1
    def seatsLeft(self):
        P = self.PTR
        RegularLeft = 0
        VIPLeft = 0
        while P != None:
            if P.data == "Regular" and P.State == False:
                RegularLeft = RegularLeft + 1
            elif P.data == "VIP" and P.State == False:
                VIPLeft = VIPLeft + 1 
        return "Las sillas restantes son\n\tRegular: " + str(RegularLeft) + "\n\tVIP: " + str(VIPLeft)
    def searchSeat(self, seat):
        P = self.PTR
        Disponible = False
        while P != None or P.Position != seat:
            P = P.next
            if P.Position == seat:
                Disponible = True
        return Disponible
class User(LinkedList):
    def AddUserNode(self, data, seatPref, SeatsBuyed):
        P = User(data, seatPref, SeatsBuyed)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else: 
            self.ULT.next = P
            self.ULT.next = P
    def buySeat(self, data, Movie, User):
        if Movie.searchSeat(data) == True :
            if Movie.searchSeat(User.SeatPref) == True:
                User.SeatsBuyed.append(Movie.MovieName + "-" + User.SeatPref)
                print("Que suerte! Su silla preferida estaba disponible")
            else:
                User.SeatsBuyed.append(Movie.MovieName + "-" + data)
                print("La silla que buscaba se encuentra disponible!")
        else:
            print("La silla que desea ni su silla favorita se encuentran disponibles :(")
    def addUserToFile(self):
        f = open(r"src\Users.csv", "a")
        f.write("\n")
        f.write(self.Name +","+ self.SeatPref + "," + self.SeatsBuyed)
        f.close()
    def fillUserList(self):
        f = open(r"src\Users.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddUserNode(a[0], a[1], a[2])
        f.close()
    def searchUser(self, data):
        P = self.PTR
        Found = False
        while P != None or P.data != data:
            if P.data == data:
                Found = True
            P = P.next
        return Found
class Movies:
    def __init__(self):
        self.MovieList = []
    def addMovie(self, MovieName, Time, Date):
        self.MovieList.append[MovieName + "-" +Time+ "-" + Date]
    def searchMovie(self, name):
        if self.MovieList.count(name) == 1:
            return True
        else:
            return False
    