def get_current_user() -> tuple[str, int, str] | None:
    pass


if __name__ == "__main__":
    assert get_current_user() == ("Ilya Lebedev", 33, "melevir@gmail.com")
