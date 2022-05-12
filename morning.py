import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro(dog, day):
    if day == "Monday":
        print_pause(
            "It's Monday morning and it's a dreary, rainy day in the city.")
        print_pause(
            "Your alarm clock rings and you wake up to a dark, cold room.")
    elif day == "Wednesday":
        print_pause("Good morning. It's an average Wednesday in the city.")
        print_pause("Your alarm clock rings and you wake up.")
    else:
        print_pause("Good morning! It's a beautiful, sunny Friday "
                    "in the city.")
        print_pause("Your alarm clock rings and you wake up with the "
                    "sunshine on your face.")
    print_pause("You stare at the ceiling for a moment, thinking of "
                "all the things on the agenda for the day.")
    print_pause("Your boss will probably be deciding any day now who "
                "they will be giving that promotion to.")
    print_pause(f"Your dog {dog} is sleeping next to you.")
    print_pause("For a moment you think about staying home with him.")


def alarm(minutes, dog):
    response = valid_input("Do you snooze your alarm? (yes/no)\n", "yes", "no")
    if "yes" in response:
        print_pause("You hit snooze and stay in bed for an extra 15 minutes.")
        minutes += 15
    elif "no" in response:
        print_pause("You turn your alarm off.")
    print_pause(f"Before you get out of bed you pet {dog}.")
    return minutes


def dog_walk(minutes, dog, day):
    print_pause("You take a quick shower and throw on your "
                "clothes for the day.")
    minutes += 45
    print_pause(f"{dog} looks at you then sits down near the front door.")
    print_pause(f"You put on {dog}'s leash and head out for "
                f"your morning walk.")
    response = valid_input(f"Do you take {dog} for a short walk or a "
                           f"long walk? (short/long)\n", "short", "long")
    if "short" in response:
        print_pause(f"You spend 10 minutes outside with {dog} and promise "
                    f"to go for a long walk when you get home from work.")
        print_pause(f"When you get home, you feed {dog} breakfast.")
        minutes += 10
        return minutes
    elif "long" in response:
        print_pause(f"You decide to take an extra 20 minutes outside so "
                    f"you and {dog} can get some exercise.")
        if day == "Monday":
            print_pause("It wasn't raining hard when you left home, but "
                        "suddenly it starts to pour.")
            print_pause(f"{dog} hates the rain and you don't want to get "
                        f"drenched before work, so you take a quick walk "
                        f"and run home.")
            print_pause("By the time you get home your clothes are "
                        "cold and wet.")
            print_pause("You fix your hair and change into something dry "
                        "and more appropriate for the weather.")
            print_pause(f"You quickly feed {dog} breakfast.")
            minutes += 50
            return minutes
        elif day == "Wednesday":
            print_pause(f"You and {dog} enjoy the fresh air, then head home.")
            print_pause(f"When you get there, you feed {dog} breakfast.")
            minutes += 30
            return minutes
        elif day == "Friday":
            print_pause(f"It's such a beautiful day that you and {dog} "
                        f"lose track of time.")
            print_pause("You realize you've been outside for way too "
                        "long and head home.")
            print_pause(f"When you get there, you feed {dog} breakfast.")
            minutes += 50
            return minutes


def coffee_shop(minutes):
    print_pause("Your favorite coffee shop is coming up on your right.")
    print_pause("You look at the time.")
    response = valid_input("Do you stop to get your morning dose of caffeine, "
                           "or do you skip it today? (get/skip)\n",
                           "get", "skip")
    minutes += 15  # For walk to work.
    if "get" in response:
        people = random.randint(2, 10)
        time = people * 4
        print_pause("It usually only take 5 minutes to get your order "
                    "and leave.")
        minutes += 5
        print_pause(f"There are {people} people in line today.")
        print_pause(f"It takes {time} minutes to order.")
        minutes += time
        print_pause("They hand you your order and you continue your "
                    "walk to work.")
    elif "skip" in response:
        print_pause("You pass the coffee shop and walk straight to work.")
    return minutes


def mind_change(minutes):
    response = valid_input("Do you get out of the cab and walk or do you "
                           "stay put? (walk/stay)\n", "walk", "stay")
    minutes += 20
    if "walk" in response:
        print_pause("You get out of the cab and walk to work.")
    elif "stay" in response:
        print_pause("You stay and it takes 30 minutes to get to the office.")
        minutes += 15
    return minutes


def cab(minutes, dog):
    print_pause(f"It took you {minutes} minutes to get ready for work today.")
    print_pause(f"When you see what time it is, you say goodbye to {dog} "
                f"and head out the door.")
    response = valid_input("Do you take the 15 minute walk to work or take "
                           "a cab? (walk/cab)\n", "walk", "cab")
    if "walk" in response:
        print_pause("You walk down the crowded city streets towards the "
                    "office.")
        minutes = coffee_shop(minutes)
        return minutes
    elif "cab" in response:
        print_pause("You get lucky and catch a cab immediately!")
        if minutes <= 55:
            print_pause("Traffic isn't too bad and you get to work in 10 "
                        "minutes.")
            minutes += 10
            return minutes
        elif minutes > 55 and minutes < 85:
            print_pause("It's rush hour. Traffic is terrible.")
            minutes = mind_change(minutes)
            return minutes
        elif minutes >= 85:
            print_pause("You're running so late that rush hour is "
                        "basically over.")
            print_pause("Traffic is light. You get to the office in "
                        "5 minutes.")
            minutes += 5
            return minutes


def do_over():
    response = valid_input("Would you like a do-over? "
                           "(yes/no)\n", "yes", "no")
    if "yes" in response:
        morning()
    if "no" in response:
        print_pause("Okay, have a nice day!")


def end(minutes, dog, day):
    print_pause(f"It took you {minutes} minutes to get through your "
                f"morning routine.")
    if minutes <= 70:
        print_pause("You walk into the office and notice that the "
                    "receptionist has not arrived yet.")
        print_pause("You sit down at your desk and look around to see "
                    "only two of your coworkers.")
        print_pause(f'As your boss is arriving, he sees you at your desk '
                    f'and says, "Happy {day}!"')
        print_pause('"I wanted to let you know that we have noticed all '
                    'of your hard work."')
        print_pause('"We have decided to give you that promotion. You '
                    'have earned it!"')
        print_pause('"Take some vacation days before you move into your '
                    'new office."')
        print_pause('"Everyone needs a break once in a while."')
        print_pause("Congratulations! Your hard work has paid off!")
        print_pause(f"Don't forget to tell {dog} the good news when you "
                    f"get home today!")
    if minutes > 70 and minutes < 110:
        print_pause("You walk into the office and greet the receptionist.")
        print_pause("She tells you that your boss wants to see you.")
        print_pause("You walk into the boss's office and they inform you "
                    "that they are happy with your performance!")
        print_pause("You've earned a decent raise. Congrats!")
        print_pause("When you get to your desk your coworker says the "
                    "promotion was finally given to someone earlier "
                    "this morning.")
        print_pause("Bummer. You really wanted that position.")
        do_over()
    if minutes >= 110:
        print_pause("You run into the office and head straight for your desk.")
        print_pause('Your coworker says, “Hey, rough morning?”')
        print_pause("Just as you sit down they tell you that your boss has "
                    "been looking for you all morning.")
        print_pause("Apparently they didn't look happy.")
        print_pause("You head to the boss's office and they tell you that "
                    "your attendance and poor work product has not gone "
                    "unnoticed.")
        print_pause("Showing up late today was the last straw.")
        print_pause("They give you a look of disappointment.")
        print_pause('“Please clean out your desk and give your ID badge to '
                    'the receptionist on your way out.”')
        print_pause("You've been fired... Yikes.")
        do_over()


def morning():
    minutes = 0
    dog = random.choice(["Tesla", "Einstein", "Hawking"])
    day = random.choice(["Monday", "Wednesday", "Friday"])
    intro(dog, day)
    minutes = alarm(minutes, dog)
    minutes = dog_walk(minutes, dog, day)
    minutes = cab(minutes, dog)
    end(minutes, dog, day)


morning()
