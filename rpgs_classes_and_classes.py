#Common behaviour requires a lot of copy pasting/similar code
class Sword:
  def __init__(self, name: str, damage: int) -> None:
    self.name = name
    self.damage = damage
  
  def get_name(self) -> str:
    return self.name
  
  def get_damage(self) -> int:
    return self.damage
    
  def action_callout(self) -> str:
    return "IM A SWORD, SHWING SHWING! NOW YOU TAKE {} DAMAGE!".format(self.damage)

class Bow:
  def __init__(self, name: str, damage: int) -> None:
    self.name = name
    self.damage = damage
  
  def get_name(self) -> str:
    return self.name
  
  def get_damage(self) -> int:
    return self.damage
  
  def action_callout(self) -> str:
    return "IM A BOW, SWOOSH SWOOSH! NOW YOU TAKE {} DAMAGE!".format(self.damage)

longsword = Sword("Longsword", 8)

print(longsword.action_callout())

shortbow = Bow("Shortbow", 6)

print(shortbow.action_callout())

########################################################################
#Inheritance allows us to keep what is the same and change whatever is different,
#meaning less copy pasting

class MagicalItem:
  def __init__(self, name: str, magicalness: int):
    self.name = name
    self.magicalness = magicalness

  def get_name(self) -> str:
    return self.name
    
  def get_magicalness(self) -> int:
    return self.magicalness
  
  def action_callout(self) -> str:
    return "Im soooooooooooo magical look at me! I'm a {} that is {} magical units of magical if you care about the details.".format(self.name, self.magicalness)
    

class Wand(MagicalItem):
  def action_callout(self) -> str:
    return "Im a waaaand! A {} that is so much lighter and better than other magical items! Im so good that I am {} magical units of magical.".format(self.name, self.magicalness)
    
class Staff(MagicalItem):
  def action_callout(self) -> str:
    return "I'm a staff, a {}. I'm strong and dependable, and I'm {} magical units.".format(self.name, self.magicalness)
    

magic_mirror = MagicalItem("Magic Mirror", 10)

print(magic_mirror.action_callout())

fire_wand = Wand("Fire Wand", 8)

print(fire_wand.action_callout())

crystal_staff = Staff("Crystal Staff", 9)

print(crystal_staff.action_callout())
