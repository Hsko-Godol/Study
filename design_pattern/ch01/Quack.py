from QuackBehavior import QuackBehavior

class Quack(QuackBehavior):
    def quack(self):
        print("QUACK!")

if __name__ == '__main__':
    q = Quack()
    q.quack()
