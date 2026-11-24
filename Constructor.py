class BankAccount:
    No = ""
    Saldo = 0

    def __init__(self, No, Saldo=0):
        # validasi saldo
        if Saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

budi = BankAccount("1234567890", 1000) # sukses
eko = BankAccount("0987654321", -1000) # error
