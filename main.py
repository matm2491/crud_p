import sys

clients = [
        {
         'name' : 'manuel',
         'company': 'facebook',
         'email' : 'matm2491@gmail.com',
        
        },
        {
        'name' : 'alejandro',
        'company': 'google',
        'email' : 'google@gmail.com' ,
        },


]

def create_client(client):
    global clients
    
    if client not in clients:
        clients.append(client)
        
    else:
        print("el cliente ya se encuentra en la lista ")


def search_clients(name_client):
    global clients

    for client in clients:
        if client != name_client:
            continue
        else:
            return True

    


def update_clients(name_client, update_clients_name):
    global clients
    if name_client in clients:
        index = clients.index(name_client)
        clients[index] = update_clients_name
    else:
        print("el nombre del cliente no esta en la lista")



def delete_client(name_client):
    global clients
    if name_client in clients:
        clients.remove(name_client)
    else:
        print("el nombre del cliente no existe")
    


def list_client():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} |{email}'.format(uid = idx, name = client['name'],
            company = client['company'], email = client['email']))


def _get_clients_field(field_name):
    field  = None
    while not field:
        field = input("cual es el cliente {}? ".format(field_name))





def _get_clients_name():
    name_client = None
    while not name_client:
        name_client = input("escribe el nombre del cliente: ")
        if name_client == "exit":
            name_client = None
            break
    if not name_client: 
        sys.exit()

        
    return name_client

def _welcome():
    print("bienvenido a alex ventas CA.")
    print("*" * 50)
    print("""Opciones
        Que te gustaria hacer
        [C]rear cliente
        [A]ctualizar cliente
        [E]eliminar cliente
        [V]er lista de clientes
        [B]uscar cliente
    """)
    print("*" * 50)



if (__name__=='__main__'):
    _welcome()
    commands = input("")
    print("*" * 10)
    commands = commands.upper()
    if commands == "C":
        client = {
            'name' : _get_clients_field('name'),
            'company' : _get_clients_field('company'),
            'email' : _get_clients_field('email'),
        }
        create_client(client)
        list_client()

    elif commands == "E":
        name_client = _get_clients_name()
        delete_client(name_client)
        list_client()

    elif commands == "A":
        name_client = _get_clients_name()
        update_clients_name = input("escribe el nuevo cliente: ")
        update_clients(name_client, update_clients_name)
        list_client()


    elif commands == "B":
        name_client = _get_clients_name()
        found = search_clients(name_client)
        if found:
            print(" {} si esta en nuestra lista".format(name_client))
        else:
            print("no se encuentra coincidencias en nuestra lista de clientes")


    elif commands == "V":
        list_client()
    
    