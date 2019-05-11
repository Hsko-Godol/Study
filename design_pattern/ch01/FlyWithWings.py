from FlyBehavior import FlyBehavior

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying~")

if __name__ == '__main__':
    fww = FlyWithWings()
    fww.fly()
