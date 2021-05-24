from abc import ABC, abstractclassmethod
from Entidades import Mobs

class Esqueleto_del_mob(ABC):

    #Este metodo te pide que 
    @abstractclassmethod
    def skills(self, nombre: str) -> str:
        pass

    #Este metodo te pide que le entregues el mob para consultarlo y que te muestre sus runas
    @abstractclassmethod
    def runas(self, Mob: Mobs) -> list(str):
        pass

    @abstractclassmethod
    def detalles(self, nombre: str) -> str:
        pass
    
class mob_en_bd(ABC):

    @abstractclassmethod
    def creacion_de_mob(self, nombre: str) -> bool:
        pass

    @abstractclassmethod
    def guardado_de_mob (self, mob: Mobs) -> bool:
        pass  
    
    @abstractclassmethod
    def cambiarStats (self, mob: Mobs) -> bool:
        pass 

    @abstractclassmethod
    def modificarSkills (self, mob: Mobs) -> bool:
        pass 

    @abstractclassmethod
    def borrarMob (self, mob: Mobs) -> bool:
        pass 

class Estadisticas(ABC):

    @abstractclassmethod
    def Mostrar_estadisticas_del_Mob(self, nombre: str) -> str:
        pass

    