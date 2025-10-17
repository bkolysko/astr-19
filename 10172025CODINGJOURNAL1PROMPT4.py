class Hedgehog:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Hedgehog Physical Characteristics:")
        print(f"  Arm length: {self.arm_length} cm")
        print(f"  Leg length: {self.leg_length} cm")
        print(f"  Number of eyes: {self.num_eyes}")
        print(f"  Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"  Is furry: {'Yes' if self.is_furry else 'No'}")
        print("\nHedgehogs are small, spiny mammals known for their round bodies and short limbs.")
        print("They use their sharp spines for protection and curl into a ball when threatened.")

# Create an instance of the Hedgehog class
my_hedgehog = Hedgehog(arm_length=3.5, leg_length=4.0, num_eyes=2, has_tail=True, is_furry=True)

# Call the describe function to print the details
my_hedgehog.describe()
