from FlyBehavior import FlyBehavior

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying by rocket power~")

if __name__ == '__main__':
    fww = FlyRocketPowered()
    fww.fly()
