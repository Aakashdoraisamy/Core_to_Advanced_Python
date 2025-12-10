class Insta:

    def __init__(self, username, password, email):
        """Initialize user details"""
        self.username = username
        self.password = password
        self.email = email
        self.followers = 0
        self.following = 0

    def login(self, other_user):
        """Check if a user is trying to follow himself"""
        if self.username == other_user.username:
            print("❌ You cannot follow yourself.")
            return False
        return True

    def follow(self, other_user):
        """Follow another user"""
        if self.login(other_user):
            self.following += 1
            other_user.followers += 1
            print(f"✅ {self.username} followed {other_user.username}")
        else:
            print("⚠ Operation failed: both usernames are same")

    def unfollow(self, other_user):
        """Unfollow another user"""
        if self.login(other_user):
            if self.following > 0 and other_user.followers > 0:
                self.following -= 1
                other_user.followers -= 1
                print(f"👋 {self.username} unfollowed {other_user.username}")
            else:
                print("⚠ Cannot unfollow: follower/following count already zero")
        else:
            print("⚠ Not possible to perform this operation")

    def display(self):
        """Display user details"""
        print("\n----- USER DETAILS -----")
        print(f"Username : {self.username}")
        print(f"Email    : {self.email}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")
        print("------------------------")
