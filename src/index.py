# Módulo
import re
import json


class Diary(object):

    def __init__(self, *args):
        self.boldStart = "\033[1m"
        self.boldEnd = "\033[0m"

    def insertData(self):
        person_amount = 0
        while person_amount <= 0:
            try:
                person_amount = int(input("¿Cuántas personas a introducir?: "))
            except ValueError:
                print("\nNo se puede introducir letras acá. 😩\n")

        person_storage = {}
        for i in range(person_amount):
            while True:
                # Nombre
                try:
                    name = input(
                        """Introducir nombre #{} 👤: """.format(i)).title()
                    match = re.search('\\d', name)
                    if (match is not None):
                        print("\n{}{}{} no es un nombre. 🙄\n".format(
                            self.boldStart,
                            name,
                            self.boldEnd
                        ))
                except KeyboardInterrupt:
                    print("\nHasta la próxima... 🍂")
                    exit()
                if(match is None):
                    # Apellido
                    while True:
                        try:
                            lastname = input(
                                """Introducir apellido #{} 👥: """.
                                format(i)).title()
                            match = re.search('\\d', lastname)
                            if(match is not None):
                                print("\n{}{}{} no es un apellido. 🙄\n".format(
                                    self.boldStart,
                                    lastname,
                                    self.boldEnd
                                ))
                        except KeyboardInterrupt:
                            print("\nHasta la próxima... 🍂")
                            exit()
                        if(match is None):
                            # Edad
                            while True:
                                try:
                                    age = int(input(
                                        """Introducir edad #{} 🐣: """.
                                        format(i)))
                                    break
                                except ValueError:
                                    print(
                                        """\nNo es una {}edad{} válida. 😒\n""".
                                        format(
                                            self.boldStart,
                                            self.boldEnd
                                        ))
                                except KeyboardInterrupt:
                                    print("\nHasta la próxima... 🍂")
                                    exit()
                            # Teléfono
                            while True:
                                try:
                                    cel = int(
                                        input(
                                            """Número teléfonico #{} 📱: """.
                                            format(i)))
                                    break
                                except ValueError:
                                    print(
                                        """\nNo es un {}número{} válido. 😒
                                        """.
                                        format(
                                            self.boldStart,
                                            self.boldEnd
                                        ))
                                except KeyboardInterrupt:
                                    print("\nHasta la próxima... 🍂")
                                    exit()
                            # Email
                            while True:
                                try:
                                    email = input(
                                        """Correo eléctronico #{} 📪: """.
                                        format(i))
                                    emailRegex = r'(^[\w]+)@([\w]+)' + '.com'
                                    match = re.search(emailRegex, email)
                                    if match:
                                        break
                                    else:
                                        print(
                                            """\n{}{}{} no es una dirección válida 🙄
                                            """.
                                            format(
                                                self.boldStart,
                                                email,
                                                self.boldEnd
                                            ))
                                except KeyboardInterrupt:
                                    print("\nHasta la próxima... 🍂")
                                    exit()
                            break
                    break
            person_storage[i] = {
                "name": name,
                "lastname": lastname,
                "age": age,
                "cellphone": cel,
                "email": email
            }

            with open("personStorage.json", "w") as f:
                json.dump(person_storage, f)
                print("\nDatos introducidos exitosamente. 😁")

    def lookRegistry(self):
        with open("personStorage.json") as f:
            data = json.load(f)
        id_ = data.keys()
        print("{}\nID NOMBRE\t\tAPELLIDO\t\tEDAD\tNUM_CELULAR\tEMAIL{}".format(
            self.boldStart,
            self.boldEnd
        ))
        for i in id_:
            name = data[i]["name"]
            lastname = data[i]["lastname"]
            age = data[i]["age"]
            cellphone = data[i]["cellphone"]
            email = data[i]["email"]
            print("{0:3}{1:21}{2:16}{3:10}{4:16}\t{5}".format(
                i,
                name,
                lastname.title(),
                age,
                cellphone,
                email.upper()
            ))
        return("\nTerminado 🙂\n")

    def searhInRegistry(self):
        with open("personStorage.json") as f:
            data = json.load(f)
            id_ = data.keys()
        try:
            options = input(
                """Buscar, Nombre[0]👤, Apellido[1]👥, Teléfono[2]📱: """)
            if options == "salir":
                return
        except KeyboardInterrupt:
            print("\nHasta la próxima... 🍂")
            exit()
        # Buscar por nombre
        if options == "0":
            print("""
            Estas son las \033[1mpersonas\033[0m disponibles. 😉
            """)
            for i in id_:
                print("{0:2}- {1}".format(i, data[i]["name"]))
            while True:
                try:
                    searh_name = input("\nIntroducir nombre de la persona 👤: ")
                except KeyboardInterrupt:
                    print("\nHasta la próxima... 🍂")
                    exit()
                listName = []
                if searh_name == "salir":
                    break
                else:
                    for i in id_:
                        names = data[i]["name"]
                        listName.append(names)

                    if searh_name not in listName:
                        print("\nEl nombre {}{}{} no existe. 🙇".format(
                            self.boldStart,
                            searh_name,
                            self.boldEnd
                        ))
                    else:
                        print(
                            "ID NOMBRE\t  APELL\t\t EDAD\tCELULAR\t\tEMAIL".
                            format(self.boldStart, self.boldEnd))
                        position = str(listName.index(searh_name))
                        name = data[position]["name"]
                        lastname = data[position]["lastname"]
                        age = data[position]["age"]
                        cellphone = data[position]["cellphone"]
                        email = data[position]["email"]
                        print("{0:3}{1:15}{2:10}{3:4}{4:15}\t{5}".format(
                            position,
                            name.title(),
                            lastname.title(),
                            age,
                            cellphone,
                            email.upper()))
        # Buscar por Apellidos
        elif options == "1":
            print(
                """\nEstos son los \033[1mapellidos\033[0m disponibles. 😉
                """)
            for i in id_:
                print("{0:2}- {1}".format(i, data[i]["lastname"]))
            while True:
                try:
                    searh_lastname = input("\nApellido a buscar 👥: ")
                except KeyboardInterrupt:
                    print("\nHasta la próxima... 🍂")
                    exit()

                listLastname = []
                if searh_lastname == "salir":
                    break
                else:
                    for i in id_:
                        lastname = data[i]["lastname"]
                        listLastname.append(lastname)
                    if searh_lastname not in listLastname:
                        print("El apellido {}{}{} no existe.".format(
                            self.boldStart,
                            searh_lastname,
                            self.boldEnd
                        ))
                    else:
                        print(
                            "ID NOMBRE\t  APELL\t\t EDAD\tCELULAR\t\tEMAIL".
                            format(self.boldStart, self.boldEnd))
                        position = str(listLastname.index(searh_lastname))
                        name = data[position]["name"]
                        lastname = data[position]["lastname"]
                        age = data[position]["age"]
                        cellphone = data[position]["cellphone"]
                        email = data[position]["email"]
                        print("{0:3}{1:15}{2:10}{3:4}{4:15}\t{5}".format(
                            position,
                            name.title(),
                            lastname.title(),
                            age,
                            cellphone,
                            email.upper()))
        # Buscar por Número Teléfonico
        elif options == "2":
            print("""\nEstos son los números teléfonicos que se encuentran actualmente
            Escriba [salir], para terminar el ciclo.
            """)
            for i in id_:
                print("{0:2}- {1}".format(i, data[i]["cellphone"]))

            while True:
                try:
                    searh_number = input("\nNúmero teléfonico 📱: ")
                except KeyboardInterrupt:
                    print("\nHasta la próxima... 🍂")
                    exit()
                listNumber = []
                if searh_number == "salir":
                    break
                else:
                    for i in id_:
                        numbers = str(data[i]["cellphone"])
                        listNumber.append(numbers)
                    if searh_number not in listNumber:
                        print("El número {}{}{} no existe 💁".format(
                            self.boldStart,
                            searh_number,
                            self.boldEnd
                        ))
                    else:
                        print(
                            "ID NOMBRE\t  APELL\t\t EDAD\tCELULAR\t\tEMAIL".
                            format(self.boldStart, self.boldEnd))
                        position = str(listNumber.index(searh_number))
                        name = data[position]["name"]
                        lastname = data[position]["lastname"]
                        age = data[position]["age"]
                        cellphone = data[position]["cellphone"]
                        email = data[position]["email"]
                        print("{0:3}{1:15}{2:10}{3:4}{4:15}\t{5}".format(
                            position,
                            name.title(),
                            lastname.title(),
                            age,
                            cellphone,
                            email.upper()
                        ))

    def modData(self):
        self.lookRegistry()
        print("\nEstos son los datos que se encuentran actualmente.")
        try:
            with open("personStorage.json") as f:
                data = json.load(f)
                id_ = data.keys()
        except FileNotFoundError:
            pass
        try:
            modID = input("\nIntroduzca el ID del campo que desea modificar: ")
            match = re.search('\\d', modID)
            for i in(id_):
                pass
            if (match is None or int(modID) > int(i)):
                print("\nEl ID {}{}{} no se ha encontrado. 😯\n".format(
                    self.boldStart,
                    str(modID),
                    self.boldEnd
                ))
                return
            else:
                print("\nModificará el siguiente campo.")
                print(
                    "ID NOMBRE\t  APELL\t\t EDAD\tCELULAR\t\tEMAIL".
                    format(self.boldStart, self.boldEnd))
                position = str(modID)
                name = data[position]["name"]
                lastname = data[position]["lastname"]
                age = data[position]["age"]
                cellphone = data[position]["cellphone"]
                email = data[position]["email"]
                print("{0:3}{1:15}{2:10}{3:4}{4:15}\t{5}".format(
                    position,
                    name.title(),
                    lastname.title(),
                    age,
                    cellphone,
                    email.upper()
                ))
        except KeyboardInterrupt:
            print("\nHasta la próxima... 🍂")
            exit()

        while True:
            try:
                mod_name = input("\nNombre: ")
            except KeyboardInterrupt:
                print("\nHasta la próxima... 🍂")
                exit()
            match = re.search('\\d', mod_name)
            if(match is not None):
                print("\n{}{}{} no es un nombre. 🙄\n".format(
                    self.boldStart,
                    name,
                    self.boldEnd
                ))
            elif(match is None):
                while True:
                    try:
                        mod_lastname = input("Apellido: ")
                    except KeyboardInterrupt:
                        print("\nHasta la próxima... 🍂")
                        exit()
                    match = re.search('\\d', mod_lastname)
                    if(match is not None):
                        print("\n{}{}{} no es un apellido. 🙄\n".format(
                            self.boldStart,
                            mod_lastname,
                            self.boldEnd))
                    elif(match is None):
                        while True:
                            try:
                                mod_age = int(input("Edad: "))
                                break
                            except ValueError:
                                print("""
                                No es una {}edad{} válida. 😒\n
                                """.format(self.boldStart, self.boldEnd))
                            except KeyboardInterrupt:
                                print("\nHasta la próxima... 🍂")
                                exit()
                        while True:
                            try:
                                mod_cellphone = int(input("Teléfono: "))
                                break
                            except ValueError:
                                print("""
                                    Eso no es un {} número {} válido. 😒\n
                                    """.format(self.boldStart, self.boldEnd))
                            except KeyboardInterrupt:
                                print("\nHasta la próxima... 🍂")
                                exit()
                        while True:
                            mod_email = input("Email: ")
                            emailRegex = r'(^[\w]+)@([\w]+)' + '.com'
                            match = re.search(emailRegex, mod_email)
                            if match:
                                break
                            else:
                                print("""
                                    {}{}{} no es una dirección válida 🙄
                                    """.format(
                                    self.boldStart,
                                    mod_email,
                                    self.boldEnd
                                ))
                        break
                break
        mod_name = data[modID]["name"] = mod_name
        mod_lastname = data[modID]["lastname"] = mod_lastname
        mod_age = data[modID]["age"] = mod_age
        mod_cellphone = data[modID]["cellphone"] = mod_cellphone
        mod_email = data[modID]["email"] = mod_email
        with open("personStorage.json", "w") as f:
            json.dump(data, f)
        print("\n¡Datos cambiados éxitosamente!\n")


if __name__ == " __main__":
    main()
