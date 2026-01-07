from jl_errors import HeroNotFoundError, PowerLevelError, MissionClearanceError

hero = "Joker"
power_level = 60
mission_clearance = False

try:
    print("Justice League Mission Started 🦸")

    try:
        if hero not in ["Batman", "Superman", "Wonder Woman", "Flash", "Aquaman"]:
            raise HeroNotFoundError("Hero is not part of Justice League ❌")

        if power_level < 80:
            raise PowerLevelError("Hero power level is too low ⚡")

        if not mission_clearance:
            raise MissionClearanceError("Hero has no mission clearance 🚫")

        print("Hero joined the mission ✅")

    except HeroNotFoundError as e:
        print("Inner Except: Hero Error 🚨")
        print(e)

    except PowerLevelError as e:
        print("Inner Except: Power Error 🚨")
        print(e)

    except MissionClearanceError as e:
        print("Inner Except: Clearance Error 🚨")
        print(e)

    finally:
        print("Inner Finally: Validation completed 🔍")

except Exception as e:
    print("Outer Except: Unknown Error ⚠️")
    print(e)

finally:
    print("Outer Finally: Mission Ended 🦇")
