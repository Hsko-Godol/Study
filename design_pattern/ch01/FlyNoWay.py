from FlyBehavior import FlyBehavior

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly..")

if __name__ == '__main__':
    fnw = FlyNoWay()
    fnw.fly()
