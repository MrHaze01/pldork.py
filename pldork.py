try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
print("""                                                                       
    

╔═══╗──╔╗────╔═══╗────╔╗
║╔═╗║─╔╝╚╗───╚╗╔╗║────║║
║║─║╠╗╠╗╔╬══╗─║║║╠══╦═╣║╔╦══╦═╗
║╚═╝║║║║║║╔╗║─║║║║╔╗║╔╣╚╝╣║═╣╔╝
║╔═╗║╚╝║╚╣╚╝║╔╝╚╝║╚╝║║║╔╗╣║═╣║
╚╝─╚╩══╩═╩══╝╚═══╩══╩╝╚╝╚╩══╩╝                         
               Coded by: Mr.Planter                                                                       """)
print("\033[1;31;36m__________________________________________________________")
print("")
query = input("Enter your dork: ")
print('')
for j in search(query, tld="co.in", num=100, stop=100, pause=2):
    print(j)
