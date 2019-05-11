from QuackBehavior import QuackBehavior

class Squeak(QuackBehavior):
    def quack(self):
        print("SQUEAK!")

if __name__ == '__main__':
    s = Squeak()
    s.quack()
