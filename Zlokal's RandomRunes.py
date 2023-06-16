import random

keystones_precision = ["Press the attack", "Lethal tempo", "Fleet footwork", "conqueror"]
other_precision = ["overheal", "Triumph", "Presence of mind"]
other_precision2 = ["Legend: bloodline", "Legend: tenacity", "Legend: Alacrity"]
other_precision3 = ["Coup de grace", "Cut Down", "Last stand"]
main_rune2_if_precision = ["Domination", "Sorcery", "Resolve", "Inspiration"]

keystones_domination = ["electrocute", "predator", "dark harvest", "hail of blades"]
other_domination = ["cheap shot", "taste of blood", "sudden impact"]
other_domination2 = ["Zombie ward", "ghost poro", "eyeball collection"]
other_domination3 = ["treasure hunter", "Ingenious hunter", "relentless hunter", "Ultimate hunter"]
main_rune2_if_domination = ["Precision", "Sorcery", "Resolve", "Inspiration"]

keystones_sorcery = ["summon aery", "arcane comet", "phase rush"]
other_sorcery = ["nullifying orb", "manaflow band", "nimbus cloak"]
other_sorcery2 = ["transcendence", "celerity", "absolute focus"]
other_sorcery3 = ["scorch", "waterwalking", "gathering storm"]
main_rune2_if_sorcery = ["Precision", "Domination", "Resolve", "Inspiration"]

keystones_resolve = ["grasp of the undying", "aftershock", "guardian"]
other_resolve = ["demolish", "font of life", "shield bash"]
other_resolve2 = ["conditioning", "second wind", "bone plating"]
other_resolve3 = ["overgrowth", "revitalize", "unflinching"]
main_rune2_if_resolve = ["Precision", "Domination", "Sorcery", "Inspiration"]

keystones_inspiration = ["glacial augment", "unsealed spellbook", "first strike"]
other_inspiration = ["hextech flashtraption", "magical footwear", "perfect timing"]
other_inspiration2 = ["future's market", "minion dematerializer", "biscuit delivery"]
other_inspiration3 = ["cosmic insight", "approach velocity", "time warp tonic"]
main_rune2_if_inspiration = ["Precision", "Domination", "Sorcery", "Resolve"]

main_rune2_domination = ["cheap shot", "taste of blood", "sudden impact", "Zombie ward", "ghost poro", "eyeball collection", "treasure hunter", "Ingenious hunter", "relentless hunter", "Ultimate hunter"]
main_rune2_sorcery = ["nullifying orb", "manaflow band", "nimbus cloak", "transcendence", "celerity", "absolute focus", "scorch", "waterwalking", "gathering storm"]
main_rune2_resolve = ["demolish", "font of life", "shield bash", "conditioning", "second wind", "bone plating", "overgrowth", "revitalize", "unflinching"]
main_rune2_inspiration = ["hextech flashtraption", "magical footwear", "perfect timing", "future's market", "minion dematerializer", "biscuit delivery", "cosmic insight", "approach velocity", "time warp tonic"]
choice_of_boost = ["adaptive force", "attack speed", "ability haste"]
choice_of_boost2 = ["adaptive force", "attack speed", "ability haste"]
choice_of_boost3 = ["adaptive force", "attack speed", "ability haste"]

main_rune = input("Chose main rune(Precision, Domination, Sorcery, Resolve or Inspiration): ").lower()
if main_rune == ("precision"):
        print("Precision")
        print(random.choice(keystones_precision))
        print(random.choice(other_precision))
        print(random.choice(other_precision2))
        print(random.choice(other_precision3))
        if_precision = random.choice(main_rune2_if_precision)
        print(if_precision)
        if if_precision == ("Domination"):
                print(random.choice(main_rune2_domination))
        if if_precision == ("Sorcery"):
                print(random.choice(main_rune2_sorcery))
        if if_precision == ("Resolve"):
                print(random.choice(main_rune2_resolve))
        if if_precision == ("Inspiration"):
                print(random.choice(main_rune2_sorcery))
        print(random.choice(choice_of_boost))
        print(random.choice(choice_of_boost2))
        print(random.choice(choice_of_boost3))

if main_rune == ("domination"):
        print("Domination")
        print(random.choice(keystones_domination))
        print(random.choice(other_domination))
        print(random.choice(other_domination2))
        print(random.choice(other_domination3))
        if_domination = random.choice(main_rune2_if_domination)
        print(if_domination)
        if if_domination == ("Precision"):
                print(random.choice(main_rune2_if_precision))
        if if_domination == ("Sorcery"):
                print(random.choice(main_rune2_sorcery))
        if if_domination == ("Resolve"):
                print(random.choice(main_rune2_resolve))
        if if_domination == ("Inspiration"):
                print(random.choice(main_rune2_inspiration))
        print(random.choice(choice_of_boost))
        print(random.choice(choice_of_boost2))
        print(random.choice(choice_of_boost3))
        print("CREATED BY ZLOKAL")

if main_rune == ("sorcery"):
        print("Sorcery")
        print(random.choice(keystones_sorcery))
        print(random.choice(other_sorcery))
        print(random.choice(other_sorcery2))
        print(random.choice(other_sorcery3))
        if_sorcery = random.choice(main_rune2_if_sorcery)
        print(if_sorcery)
        if if_sorcery == ("Precision"):
                print(random.choice(main_rune2_if_precision))
        if if_sorcery == ("Sorcery"):
                print(random.choice(main_rune2_sorcery))
        if if_sorcery == ("Resolve"):
                print(random.choice(main_rune2_resolve))
        if if_sorcery == ("Inspiration"):
                print(random.choice(main_rune2_inspiration))
        print(random.choice(choice_of_boost))
        print(random.choice(choice_of_boost2))
        print(random.choice(choice_of_boost3))
        print("CREATED BY ZLOKAL")

if main_rune == ("resolve"):
        print("Resolve")
        print(random.choice(keystones_resolve))
        print(random.choice(other_resolve))
        print(random.choice(other_resolve2))
        print(random.choice(other_resolve3))
        if_resolve = random.choice(main_rune2_if_resolve)
        print(if_resolve)
        if if_resolve == ("Precision"):
                print(random.choice(main_rune2_if_precision))
        if if_resolve == ("Domination"):
                print(random.choice(main_rune2_domination))
        if if_resolve == ("Sorcery"):
                print(random.choice(main_rune2_sorcery))
        if if_resolve == ("Inspiration"):
                print(random.choice(main_rune2_inspiration))
        print(random.choice(choice_of_boost))
        print(random.choice(choice_of_boost2))
        print(random.choice(choice_of_boost3))
        print("CREATED BY ZLOKAL")

if main_rune == ("inspiration"):
        print("Inspiration")
        print(random.choice(keystones_inspiration))
        print(random.choice(other_inspiration))
        print(random.choice(other_inspiration2))
        print(random.choice(other_inspiration3))
        if_inspiration = random.choice(main_rune2_if_inspiration)
        print(if_inspiration)
        if if_inspiration == ("Precision"):
                print(random.choice(main_rune2_if_precision))
        if if_inspiration == ("Domination"):
                print(random.choice(main_rune2_domination))
        if if_inspiration == ("Sorcery"):
                print(random.choice(main_rune2_sorcery))
        if if_inspiration == ("Resolve"):
                print(random.choice(main_rune2_resolve))
        print(random.choice(choice_of_boost))
        print(random.choice(choice_of_boost2))
        print(random.choice(choice_of_boost3))
        print("CREATED BY ZLOKAL")

        




