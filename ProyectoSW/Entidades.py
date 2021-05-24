
class Mobs:
    def __init__(self, nombre: str, elemento: str, runas: bool, skills: list(int) ):
        self.nombre = nombre
        self.elemento = elemento
        self.runas = runas #Esto esta suceptible a cambio
        self.skills = skills
        
    def __str__(self):
        return "nombre: {}, elemento: {}, runas: {}, skills: {}".format(self.nombre, self.elemento, self.runas, self.skills)
        pass
class Estadisticas:
    def __init__(self, wins: int, ban: int, ban_rate, number_of_picks: int, pick_as_first: int, pick_as_second: int, pick_as_Counter: int):
        self.wins = wins
        self.win_rate = 0
        self.ban = ban
        self.ban_rate = 0
        self.number_of_picks = number_of_picks
        self.pick_as_first = pick_as_first
        self.pick_as_second = pick_as_second
        self.pick_as_Counter = pick_as_Counter

    def mostrarWinRate(self):
        win_rate = self.wins / self.number_of_picks 
        print("El win rate es: ",win_rate)

    def mostrarBanRate(self):
        ban_rate = self.ban / self.number_of_picks
        print("El ban rate es: ", ban_rate)

    def __str__(self):
        return "Las estadisticas completas son: wins: {}, ban: {}, ban_rate: {}, number_of_picks: {}, ".format(self.wins, self.ban, self.ban_rate, self.number_of_picks)