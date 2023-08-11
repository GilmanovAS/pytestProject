# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def ticket_price(age: int):
    if 0 <= age < 7:
        return "0"
    elif 7 <= age < 18:
        return "100"
    elif 18 <= age < 25:
        return "200"
    elif 25 <= age < 50:
        return "300"
    else:
        return "Error"


def double
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert ticket_price(0) == "0", "Error for 0"
    assert ticket_price(7) == "100", "Error for 7"
    assert ticket_price(45) == "300", "Error for 45"
    # assert ticket_price('PyCharm') == "Error" , "Error for  Err"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
