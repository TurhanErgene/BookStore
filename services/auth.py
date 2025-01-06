from models.member import register_member, login_member

def handle_registration():
    print("\nWelcome to the Online Book Store\nNew Member Registration\n")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter street address: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip: ")
    phone = input("Enter phone: ")
    email = input("Enter email address: ")
    password = input("Password: ")

    data = (first_name, last_name, address, city, zip_code, phone, email, password)
    try:
        register_member(data)
        print("\nYou have registered successfully!")
    except Exception as e:
        print(f"Error during registration: {e}")
    input("\nPress Enter to go back to Menu")

def handle_login():
    print("\nWelcome to the Online Book Store\nMember Login\n")
    email = input("Enter email: ")
    password = input("Enter password: ")
    member = login_member(email, password)
    if member:
        print("\nLogin successful!")
        return member
    else:
        print("\nInvalid email or password.")
        return None
