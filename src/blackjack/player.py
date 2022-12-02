class Player:
    def __init__(self, name: str, inital_balance: float):
        self.__balance = inital_balance
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def balance(self) -> float:
        return self.__balance

    def place_inital_bet(self, param):
        pass

    def receive_card(self, param, UP):
        pass

