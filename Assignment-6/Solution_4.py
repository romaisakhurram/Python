
class Bank:
    bank_name = "Habib Bank"

    def __init__(self , account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls , bank_name):
        cls.bank_name = bank_name

    def dislay(self):
        print(f"Account Holder: {self.account_holder} , Bank Name: {self.bank_name}")

account_holder_1 = Bank("Ali")
account_holder_2 = Bank("Sara")

account_holder_1.dislay()
account_holder_2.dislay()

account_holder_1.change_bank_name("National Bank")

account_holder_1.dislay()
account_holder_2.dislay()

