class UnfortunateAdventurer:
  def __init__(self, name: str) -> None:
    self.name = name
  
  def smack(self, damage: int) -> None:
    print("Ow ({})".format(damage))
    
  def slow(self, amount: int) -> None:
    print("Oh noes, I am the slows ({})".format(amount))
    
  def cripple(self) -> None:
    print("Oh no, I am now robbed of the use of my legs!")
    
  def magic_smack(self, magicalness: int) -> None:
    print("This is too magical for me, my mind cannot handle the {} magical units of magicalness!".format(magicalness))
    
larry = UnfortunateAdventurer("Larry")

#Common behaviour requires a lot of copy pasting/similar code
class Sword:
  def __init__(self, name: str, damage: int, callout: str) -> None:
    self.name = name
    self.damage = damage
    self.callout = callout
  
  def get_name(self) -> str:
    return self.name
  
  def get_damage(self) -> int:
    return self.damage
    
  def use(self, target) -> str:
    target.smack(self.damage)
    return self.callout.format(self.damage)

class Bow:
  def __init__(self, name: str, damage: int, callout: str) -> None:
    self.name = name
    self.damage = damage
    self.callout = callout
  
  def get_name(self) -> str:
    return self.name
  
  def get_damage(self) -> int:
    return self.damage
  
  def use(self, target) -> str:
    target.smack(self.damage)
    target.slow(self.damage // 2)
    return self.callout.format(self.damage)

longsword = Sword("Longsword", 8, "I'm a swooooord! Take {} damage!")

print(longsword.use(larry))

shortbow = Bow("Shortbow", 6, "I'm a booow! Take {} damage!")

print(shortbow.use(larry))

########################################################################
#Inheritance allows us to keep what is the same and change whatever is different,
#meaning less copy pasting

class MagicalItem:
  def __init__(self, name: str, magicalness: int, callout: str) -> None:
    self.name = name
    self.magicalness = magicalness
    self.callout = callout

  def get_name(self) -> str:
    return self.name
    
  def get_magicalness(self) -> int:
    return self.magicalness
  
  def use(self, target) -> str:
    return self.callout.format(self.name, self.magicalness)
    

class Wand(MagicalItem):
  def use(self, target) -> str:
    target.magic_smack(self.magicalness)      
    return self.callout.format(self.name, self.magicalness)
    
class Staff(MagicalItem):
  def action_callout(self) -> str:
    target.cripple()
    target.magic_smack(self.magicalness)
    return self.callout.format(self.name, self.magicalness)
    

magic_mirror = MagicalItem("Magic Mirror", 10, "Im soooooooooooo magical look at me! I'm a {} that is {} magical units of magical if you care about the details.")

print(magic_mirror.use(larry))

fire_wand = Wand("Fire Wand", 8, "Im a waaaand! A {} that is so much lighter and better than other magical items! Im so good that I am {} magical units of magical.")

print(fire_wand.use(larry))

crystal_staff = Staff("Crystal Staff", 9, "I'm a staff, a {}. I'm strong and dependable, and I'm {} magical units.")

print(crystal_staff.use(larry))
