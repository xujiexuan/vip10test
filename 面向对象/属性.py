class Washer():

    def wash(self):
        print(f'我会洗衣服{self.height},{self.width}')

haier1 = Washer()

haier1.width = 500
haier1.height = 800
haier1.wash()
print(f'{haier1.height},{haier1.width}')

