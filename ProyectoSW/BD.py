import mysql.connector
import requests
class conexion:

    def con(self):
        mydb = mysql.connector.connect( host="localhost", user="myusername", password="mypassword" )

class test:

    def test2(nombre: str):
        url = "https://swarfarm.com/api/v2/monsters/"
        parametros = {'name':nombre}
        response = requests.get(url, parametros).json()
        data = response['results']
        for i in data:
            print("nombre: ",i['name'], "Elemento: ",i['element'], "Runas: ",False, "skills ",i['skills'])  

        return True

if __name__ == '__main__':
    print(test.test2("Rakan"))
