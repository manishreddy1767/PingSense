from src.data.manager import DataManager
from src.data.repository import Repository


def main():

    data = DataManager.load()

    repo = Repository(data)

    message_id = data.messages.iloc[0]["message_id"]

    message = repo.get_message(message_id)

    print(type(message))
    print(message)

    user = repo.get_user(message.user_id)

    print()
    print(type(user))
    print(user)

    business = repo.get_business(message.business_id)

    print()
    print(type(business))
    print(business)


if __name__ == "__main__":
    main()