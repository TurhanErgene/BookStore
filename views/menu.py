from services.auth import handle_registration, handle_login

def display_main_menu():
    while True:
        print("\n" + "*" * 60)
        print("*** Welcome to the Online Book Store ***")
        print("*" * 60)
        print("1. Member Login")
        print("2. New Member Registration")
        print("q. Quit")
        
        choice = input("\nType in your option: ")
        if choice == "1":
            member = handle_login()
            if member:
                display_member_menu(member)
        elif choice == "2":
            handle_registration()
        elif choice.lower() == "q":
            print("\nThank you for visiting!")
            break
        else:
            print("\nInvalid option. Please try again.")

def display_member_menu(member):
    while True:
        print("\n" + "*" * 60)
        print("*** Welcome to Online Book Store ***")
        print("*** Member Menu ***")
        print("*" * 60)
        print("1. Browse by Subject")
        print("2. Search by Author/Title")
        print("3. Check Out")
        print("4. Logout")

        choice = input("\nType in your option: ")
        if choice == "4":
            print("\nLogging out...")
            break
        else:
            print("\nThis feature is not yet implemented.")
