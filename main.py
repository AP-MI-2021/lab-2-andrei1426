def factorial(n: int) -> int:
    """Calculeaza si returneaza factorialul unui numar """
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


def get_n_choose_k(n: int, k: int):
    """Calculeaza combinari de n luate cate k """
    return factorial(n) / (factorial(k) * factorial(n - k))


def test_get_n_choose_k():
    """Testeaza functia get_n_choose_k
    """
    assert get_n_choose_k(10, 0) == 1.0
    assert get_n_choose_k(5, 1) == 5.0
    assert get_n_choose_k(5, 4) == 5.0
    assert get_n_choose_k(5, 4) == get_n_choose_k(5, 1)
    assert get_n_choose_k(7, 2) == get_n_choose_k(7, 5)


def input_get_n_choose_k():
    print("Functia calculeaza combinari de n luate cate k.")
    n = int(input("n="))
    k = int(input("k="))
    print(f"Exista {get_n_choose_k(n, k)} combinari de {n} luate cate {k}.")


def is_palindrome(n: int) -> bool:
    """Verifica daca numarul dat este un palindrom"""
    ogl = 0
    lungime = len(str(n))
    for i in range(lungime //2):
        ogl *= 10
        ogl += n % 10
        n //= 10

    if lungime % 2 == 1:
        n //= 10

    return n == ogl


def test_is_palidnrome():
    """Testeaza is_palindrome
    """
    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True


def print_menu():
    print("1. Test nr palindrom")
    print("2. Combinari de n luate cate k")
    print("3. Iesire")


def main():
    test_get_n_choose_k()
    test_is_palidnrome()

    while True:
        print_menu()
        optiune = input("Alegeti optiunea")
        if optiune == "1":
            n = int(input("Ce numar doriti sa testati?"))
            print(is_palindrome(n))
        elif optiune == "2":
            n = int(input("Dati n="))
            k = int(input("Dati k="))
            print(get_n_choose_k(n, k))
        elif optiune == "3":
            break
        else:
            print("optiune greita!")


main()
