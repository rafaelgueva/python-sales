import sys

nombre_usuario ='rafael,antonio'

def create_nombre(nuevo):
    global nombre_usuario

    if nuevo not in nombre_usuario:
         nombre_usuario+=nuevo
         _agregar_coma()

    else:
        print('this client exist')



def _lista():
    global nombre_usuario
    print (nombre_usuario)

def _agregar_coma():
    global nombre_usuario

    nombre_usuario+=', '

def update(nombre_cliente):
    global nombre_usuario
    
    if nombre_cliente in nombre_usuario:

        update_nombre=input('indique actualizaciòn')

        nombre_usuario=nombre_usuario.replace(nombre_cliente + ',' , update_nombre)
        
    else:
        print('cliente no existe')

def delete(nombre_cliente_delete):
    global nombre_usuario

    if nombre_cliente_delete in nombre_usuario:
        nombre_usuario = nombre_usuario.replace(nombre_cliente_delete+',', '')

    else:
        print('no existe este usuario')


def busca_cliente(nombre_buscar):
    global nombre_usuario

    nombre_usuario_csg=nombre_usuario.split(',')

    for nombre_usuario in nombre_usuario_csg:
        if nombre_usuario != nombre_buscar:
            continue
        else:
            return True
        
    
def _get_client_name():
    client_name=None

    while not client_name:
        client_name=input('what is the client')

        if client_name =='exit':
            client_name =None
            break

    if not client_name:
        sys.exit()

    return client_name

def _print_menu():
    print ('BIENVENIDO AL REGISTRO DE VENTA')
    print ('*' * 50)
    print ('What would you like to do')
    print ('[C] Create client')
    print ('[D] Delete Client')
    print ('[U] Update cliente')
    print ('[S] Search client')


if __name__=='__main__':
    _print_menu()


    comando = input()
    comando = comando.upper()

    if comando =='c' or comando =='C':
        carga_nombre=_get_client_name()
        print(carga_nombre)
        create_nombre(carga_nombre)
        _lista()
    
    elif comando == 'D':
        dato_eliminar_cliente=input('cual es el nombre del cliente a eliminar)')
        delete(dato_eliminar_cliente)
        _lista
    

    elif comando =='U':

        carga_nombre=input('¿cual es el nombre que desea actualizar?')
        
        update(carga_nombre)
        _lista()

    elif comando =='S':
        nombre_buscar=input('cual es el nombre a buscar')

        found=busca_cliente(nombre_buscar)
        
        if found:
            print('true el cliente existe')
        else:
            print('fase el cliente no exite')

        

    else:
        print ('invalid command')

    cambio en codigo 1