def ban_users(users_ids: set[int]) -> int | None:
    pass


if __name__ == "__main__":
    assert ban_users(users_ids={167, 623, 209, 921}) == 2
