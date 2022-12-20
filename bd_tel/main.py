import UI
import print_bd
import bd_add
import import_bd
import export_bd
num_menu = ''
while True:
    num_menu = UI.menu()
    if num_menu == '5':
        exit()
    if num_menu == '1':
        print_bd.print_bd()
    if num_menu == '2':
        bd_add.bd_add()
    if num_menu == '3':
        x, y = import_bd.import_bd()
        if y == '1':
            import_bd.import_bd_1(x)
        if y == '2':
            import_bd.import_bd_2(x)
    if num_menu == '4':
        export_bd.export_bd()
