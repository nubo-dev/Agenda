from src import index as diary


print("""
\t\t\t\t     ___       _______  _______ .__   __.  _______       ___.
\t\t\t\t    /   \     /  _____||   ____||  \ |  | |       \     /   \.
\t\t\t\t   /  ^  \   |  |  __  |  |__   |   \|  | |  .--.  |   /  ^  \.
\t\t\t\t  /  /_\  \  |  | |_ | |   __|  |  . `  | |  |  |  |  /  /_\  \.
\t\t\t\t /  _____  \ |  |__| | |  |____ |  |\   | |  '--'  | /  _____  \.
\t\t\t\t|__/     \__\ \______| |_______||__| \__| |_______/ /__/     \__|
\t\t\t\t\t\t\t\t     ©2018 Yank Carlos R. Espinal
\n\t\t\t\t\tAplicación que se encarga de\033[1m crear una agenda\033[0m,
\t\t\t\t\tpuede\033[1m insertar\033[0m varias personas a la vez, también
\t\t\t\t\tpuede\033[1m buscar\033[0m personas y\033[1m modificar\033[0m
\t\t\t\t\tsus datos.
\n
\t\t\t\t\tIntroduzca [salir] para retroceder o [?] para
\t\t\t\t\tdesplegar el menú.
""")


def menu():
    print("""
\033[1m¿Qué desea hacer?\033[0m
1 - Introducir nuevos datos.
2 - Desplegar los datos.
3 - Buscar dentro del registro.
4 - Modificar Datos.
""")


menu()


while True:
    try:
        option = input("\n🐍 > ")
        if option not in ["1", "2", "3", "4", "salir", "?"]:
            print("\nPor favor, introduzca una opción válida. 👀")
    except KeyboardInterrupt:
        print("\nHasta la próxima... 🍂")
        exit()

    if option == "?":
        menu()
    elif option == "salir":
        print("\nHasta la próxima... 🍂")
        break
    elif option == "1":
        insertData = diary.Diary().insertData()
    elif option == "2":
        try:
            lookRegistry = diary.Diary().lookRegistry()
        except FileNotFoundError:
            print("\tDebe crear primero un registro. 😪\n")
    elif option == "3":
        try:
            searhInRegistry = diary.Diary().searhInRegistry()
        except FileNotFoundError:
            print("\tDebe crear primero un registro. 😪\n")
    elif option == "4":
        try:
            modData = diary.Diary().modData()
        except FileNotFoundError:
            print("\tDebe crear primero un registro. 😪\n")
