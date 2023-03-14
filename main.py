class Client:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def get_clientlist(self):
        return f'{self.first_name} {self.second_name}. {self.city}.'

client_1 = Client('Иван','Петров','Москва',50)
client_2 = Client('Петр', 'Иванов', 'Санкт-Петербург',80)
client_3 = Client('Анастасия','Круглова','Самара',45)

client_list = [client_1, client_2, client_3]

for guest in client_list:
    print(guest.get_clientlist())