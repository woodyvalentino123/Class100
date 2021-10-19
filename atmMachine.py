class Card(object):
    def __init__(self,money,company,card):
        self.money=money
        self.company=company

    def start(self):
        print("printing started")
    
    def stop(self):
        print("printing stopped")
    
black=Card("123","black","ICICI")
print(black.start())