def main():
    db_name = input().strip()
    global_init(db_name)
    session = create_session()

    users = session.query(User).filter(
        User.address == "module_1",
        ~User.speciality.like("%engineer%"),
        ~User.position.like("%engineer%")
    ).all()

    for user in users:
        print(user.id)


if __name__ == "__main__":
    main()
