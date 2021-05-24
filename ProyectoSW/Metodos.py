from Interfaces import Esqueleto_del_mob, mob_en_bd
from Entidades import Mobs
from DB import conexion
import requests

class mob(Esqueleto_del_mob):
    
    #Este metodo nos va a dar el mob que vamos a crear
    def creacion(self, nombre: str):
        url = "https://swarfarm.com/api/v2/monsters/"
        parametros = {'name':nombre}
        response = requests.get(url, parametros).json()
        data = response['results']
        for i in data:
            Mob_nuevo = Mobs(i['name'], i['element'], False, i['skills'])      
        return Mob_nuevo
    
    #Este metodo nos va a consultar los detalles existentes en el API del mob ya dado
    def detalles(self, nombre:str) -> str:
        pass

    #Este metodo nos va a ir a buscar las runas existentes en la cuenta de swarfarm dada
    def mostrar_runas(self, mob:Mobs) -> list(str):
        response = requests.get("https://swarfarm.com/api/v2/monsters/").json()
        data = response['results']
        for i in data:
            print("name: ", i['name'], "element: ", i['element'], "runas: ", False, "skills: ", i['skills'])
        return list(str)

class db(mob_en_bd):

    #db.creacion( mob.creacion( nombre))
    def creacion(self, mob_a_guardar: Mobs):

        if(conexion == True):
            pass

    def guardado_de_mob(self):
        pass

    def cambiar_stats(self):
        pass

    def modificar_skills(self):
        pass

    def borrar_mob(self):
        pass