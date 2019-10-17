class Human:
    def __init__(self, name): self.name = name
    def __str__(self): return "the {} human".format(self.name)
    def speak(self): return " is speaking"

class Synthesizer:
    def __init__(self, name): self.name = name
    def __str__(self): return "the {} synthesizer".format(self.name)
    def play(self): return " is playing an electronic song"


class Computer:
    def __init__(self, name): self.name = name
    def __str__(self): return "the {} computer".format(self.name)
    def execute(self): return " exec a process"

class Adapter(Computer):
    def __init__(self, wih):
        self.wih = wih

    def execute(self):
        if isinstance(self.wih, Human):
            return self.wih.speak()
        if isinstance(self.wih, Synthesizer):
            return self.wih.play()

class WhatIUse:
    def op(self, comp):
        return comp.execute()

whatIUse = WhatIUse()
human = Human('Bob')
adapt = Adapter(human)
print(human, whatIUse.op(adapt))