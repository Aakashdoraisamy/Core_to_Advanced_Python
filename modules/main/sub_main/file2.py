from .file1 import Payment # Relative import
# from main.file1 import Payment # absolute path

class UPI(Payment):
    def pay1(self):
        print('Welcome to UPI Payment....')

    def pay2(self):
        print('option 2 .....')
        
class NetBanking(Payment):
    def pay1(self):
        print('Welcome to UPI Payment....')
        
# upi = UPI()
# upi.pay1()