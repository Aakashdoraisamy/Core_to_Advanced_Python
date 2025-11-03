class Perfectnumber:

    def perfect_number(self,n):
        sum_divisors = 0
        divisors = []  
        
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
                divisors.append(i)
        
        if sum_divisors == n:
            print(f"{n} is a Perfect Number")
        else:
            print(f"{n} is NOT a Perfect Number")

class Reversenumber:  
    
    def reverse_number(self, n):
        print("Reverse of the number:", end=' ')
        while n > 0:
            rem = n % 10
            print(rem, end=' ')
            n = n // 10
    
class Number(Perfectnumber, Reversenumber):
    def __init__(self):
        self.num = int(input("Enter a number: "))

    def choose_operation(self):
        print("Choose an option:")
        print("1 - Check Perfect Number")
        print("2 - Reverse Number")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.perfect_number(self.num)
        elif choice == 2:
            self.reverse_number(self.num)
        else:
            print("Invalid choice!")

obj = Number()
obj.choose_operation()