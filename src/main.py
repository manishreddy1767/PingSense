from src.data.manager import DataManager
from src.data.repository import Repository

def main():
    data = DataManager.load()
    repo = Repository(data)

    first_message_id = data.messages.iloc[0]["message_id"]

    print(f"Testing message_id: {first_message_id}\n")

    message = repo.get_message(first_message_id)

    print("MESSAGE")
    print(message)

    print("\nUSER")
    print(repo.get_user(message["user_id"]))

    print("\nGROUP")
    print(repo.get_group(message["group_id"]))

    print("\nBUSINESS")
    print(repo.get_business(message["business_id"]))

if __name__ == "__main__":
    main()