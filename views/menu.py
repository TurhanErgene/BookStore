from services.auth import handle_registration, handle_login
from services.browse import browse_by_subject, search_by_author, search_by_title
from services.book import get_all_subjects


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
            if not member:  ########### Remove not on production ###########
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
        if choice == "1":
            books = get_all_subjects()
            if books:
                print("\nAll book subjects: ")
                for book in books:
                    print(book)
            else:
                print("\nNo books available in the subject.")

        elif choice == "2":
            while True:
                print("1. Author Search")
                print("2. Title Search")
                print("3. Go Back to Main Menu")
                choice = input("\nType in your option: ")

                if choice == "1":
                    author = input("\nEnter the author name: ")
                    books = search_by_author(author)
                    if books:
                        print("\nBooks available by the author: ")
                        for book in books:
                            print(book)
                    else:
                        print("\nNo books available by the author.")

                elif choice == "2":
                    title = input("\nEnter the title of the book: ")
                    books = search_by_title(title)
                    if books:
                        print("\nBooks available by the title: ")
                        for book in books:
                            print(book)
                    else:
                        print("\nNo books available by the title.")

                elif choice == "3":
                    break
                else:
                    print("\nInvalid option. Please try again.")

        elif choice == "3":
            print("\nThis feature is not yet implemented.")
        elif choice == "4":
            print("\nLogging out...")
            break
        else:
            print("\nThis feature is not yet implemented.")
