class FellowshipJourney:

    def start_journey(self, members, food_days):
        try:
            print("The Fellowship begins its journey...")

            # Default exception: ValueError
            if members <= 0:
                raise ValueError("The Fellowship must have at least one member")

            # Default exception: ZeroDivisionError
            food_per_member = food_days / members

            print(f"Food per member: {food_per_member} days")

        except ValueError as ve:
            print("Journey Error:", ve)

        except ZeroDivisionError:
            print("Journey Error: No members to share the food")

        except Exception as e:
            print("Unexpected danger on the road:", e)

        else:
            print("The Fellowship marches forward safely 🗡️")

        finally:
            print("Journey step completed\n")

journey = FellowshipJourney()

# Case 1: Valid journey
journey.start_journey(9, 90)

# Case 2: Zero members
journey.start_journey(0, 50)

# Case 3: Invalid input
journey.start_journey(-3, 40)
