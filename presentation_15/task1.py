class MainHero:
    def __init__(self, nick, hp, power, gun):
        self.nick = nick
        self.hp = hp
        self.power = power
        self.gun = gun
    
ONE = MainHero("Gerald", 150, 100, "Sword")
TWO = MainHero("Arthur Morgan", 120, 25, "Revolver")
THREE = MainHero("Raiden", 999, 10000, "Blade")


print(f"Первый воин: {ONE.nick}\nВторой воин: {TWO.nick}\nТретий воин: {THREE.nick}")