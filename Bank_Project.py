
try:
    from gtbank import Gtbank 
    from access import Access_Bank
    from polaris import Polaris_Bank

    class Bank:
        def __init__(self):
            self.nu = 'nu'
            
        def bank_menu(self):
            bank_menu_count = 1
            while bank_menu_count <= 3:
                
                print('''
                    1. GTCO
                    2. Access Bank
                    3. Polaris Bank
                ''')
                choice = int(input('Response: '))
                if choice == 1:
                    g.welcome()
                    break
                elif choice == 2:
                    a.welcome()
                    break
                elif choice == 3:
                    p.welcome()
                    break
                else:
                    print(f'Invalid input!\nSelect among options 1 to 3 only.')
                    bank_menu_count += 1
            else:
                print('Trial chances terminated. Try again later.')
                quit()
                   


    b = Bank()
    g = Gtbank()
    a = Access_Bank()
    p = Polaris_Bank()

    print(f'Welcome!\nPlease select your choice bank to transact within')
    b.bank_menu()

except ValueError:
    print('Accepts Integer Values only.\nTry Again')
    b.bank_menu()
except TypeError:
    print('User has no account record with the Bank.\nPlease register to enjoy our services.')
    b.bank_menu()
# except UnboundLocalError:
#     print('Undefined Variable')
# except AttributeError:
    # print('Missing Object Attribute.\nCheck again')

