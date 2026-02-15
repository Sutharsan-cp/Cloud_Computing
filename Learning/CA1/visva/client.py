import requests

BASE_URL = "http://localhost:5000"


def menu():
    print("\n1. Create User")
    print("2. Get Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        response = requests.post(f"{BASE_URL}/users", json={"name": name})
        print(response.json())

    elif choice == "2":
        response = requests.get(f"{BASE_URL}/users")
        print(response.json())

    elif choice == "3":
        user_id = input("Enter user id: ")
        name = input("Enter new name: ")
        response = requests.put(
            f"{BASE_URL}/users/{user_id}",
            json={"name": name}
        )
        print(response.json())

    elif choice == "4":
        user_id = input("Enter user id: ")
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        print(response.json())

    elif choice == "5":
        break
