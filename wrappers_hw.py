def test_wrap(func_to_wrap):
    def wrapper():
        print("ahaha")
        print(func_to_wrap)
        print("ohoho")

    return wrapper()


@test_wrap
def my_test():
    return "ahahah"
