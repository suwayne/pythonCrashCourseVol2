class Rocket:
    """A simple attempt to model a low power model rocket."""
    def __init__(self, name, weight, diameter, enginetype):
        """initialize name, weight, and diameter, enginetype)"""
        self.name = "Astrobean" 
        self.weight = 27
        self.diameter = 89
        self.enginetype = "c65"

    def launch(self):
        """Simulate the rocket launching."""    
        print(self.name.title() + "is now launching.")

    def trajectory(self):
        """Simulate the rocket ascending"""
        print(self.name.title() + "is on a nominal traiectorv.")




mrFresh = Rocket("Astrobeam", 25, 89, "c65")
mrFresh.launch()
mrFresh.trajectory()