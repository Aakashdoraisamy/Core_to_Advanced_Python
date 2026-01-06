from errors_module import *

print("⚡ Justice League + Avengers Interactive Error Simulator ⚡\n")

while True:
    print("\nChoose a superhero error to trigger:")
    print("1 - Superman's crazy division")
    print("2 - Hulk tries to boost Iron Man suit")
    print("3 - Flash checks Avengers team")
    print("4 - Batman checks Justice League roster")
    print("5 - Doctor Strange casts a spell")
    print("6 - Aquaman tries to swim")
    print("7 - Loki tries to import magic")
    print("0 - Exit")

    choice = input("\nEnter your choice (0-7): ")

    if choice == "0":
        print("Exiting simulator... Goodbye!")
        break

    try:
        if choice == "1":
            earth_population = float(input("Enter Earth's population: "))
            super_speed_factor = float(input("Enter Superman's speed factor: "))
            print("Calculation Result:", superman_divide(earth_population, super_speed_factor))

        elif choice == "2":
            hulk_strength = int(input("Enter Hulk's strength: "))
            iron_suit_level = input("Enter Iron Man suit level: ")
            print("Combined Power:", hulk_add_strength(hulk_strength, iron_suit_level))

        elif choice == "3":
            avenger_team = ["Iron Man", "Thor", "Hulk"]
            avenger_position = int(input(f"Enter Avengers team index (0-{len(avenger_team)-1}): "))
            print("Avenger Found:", flash_team_check(avenger_team, avenger_position))

        elif choice == "4":
            justice_league_roster = {"Superman": "Man of Steel", "Wonder Woman": "Amazonian Princess"}
            hero_name = input("Enter Justice League hero name: ")
            print("Hero Info:", batman_justice_lookup(justice_league_roster, hero_name))

        elif choice == "5":
            spell_power_input = input("Enter spell power to cast: ")
            print("Spell Cast Result:", doctor_strange_spell_cast(spell_power_input))

        elif choice == "6":
            aquaman_ability = "King of Atlantis"
            print(aquaman_swim_attempt(aquaman_ability))

        elif choice == "7":
            loki_import_trick()

        else:
            print("Invalid choice! Try again.")

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except AttributeError as e:
        print(f"Caught AttributeError: {e}")
    except ImportError as e:
        print(f"Caught ImportError: {e}")
    except Exception as e:
        print(f"Some unexpected error occurred: {e}")
