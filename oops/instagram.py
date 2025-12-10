class Insta:

    def __init__(self, username, password, email):
        # These belong to the CURRENT object (self)
        self.username = username        # ex: u1.username = "aakash"
        self.password = password        # ex: u1.password = "123"
        self.email = email              # ex: u1.email = "a@gmail.com"
        self.followers = 0              # ex: u1.followers = 0
        self.following = 0              # ex: u1.following = 0

    def login(self, other_user):
        """
        self       -> the object that calls the method
        other_user -> the object that is being followed/unfollowed
        """
        # Example:
        # u1.login(u2) 
        # self.username      -> u1.username = "aakash"
        # other_user.username -> u2.username = "raj"

        if self.username == other_user.username:
            print("❌ You cannot follow yourself.")
            return False
        
        return True  # Different users → OK

    def follow(self, other_user):
        """
        Example call: u1.follow(u2)

        self       = u1  (the person who is following)
        other_user = u2  (the person being followed)
        """

        if self.login(other_user):  
            # Increase following of the current user
            self.following += 1       # u1.following = u1.following + 1

            # Increase followers of the other user
            other_user.followers += 1 # u2.followers = u2.followers + 1

            print(f"✅ {self.username} followed {other_user.username}")

        else:
            print("⚠ Operation failed")

    def unfollow(self, other_user):
        """
        Example: u1.unfollow(u2)
        
        self       = u1  (person who unfollows)
        other_user = u2  (person being unfollowed)
        """

        if self.login(other_user):

            if self.following > 0 and other_user.followers > 0:
                self.following -= 1       # u1.following = u1.following - 1
                other_user.followers -= 1 # u2.followers = u2.followers - 1

                print(f"👋 {self.username} unfollowed {other_user.username}")
            else:
                print("⚠ Cannot unfollow: counts already 0")

        else:
            print("⚠ Self-operation not allowed")

    def display(self):
        """
        Prints values stored in THIS object (self)
        """
        print("\n----- USER DETAILS -----")
        print(f"Username : {self.username}")
        print(f"Email    : {self.email}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")
        print("------------------------")


u1 = Insta("aakash", "123", "a@gmail.com")
u2 = Insta("raj", "456", "r@gmail.com")

u1.follow(u2)
u1.display()
u2.display()