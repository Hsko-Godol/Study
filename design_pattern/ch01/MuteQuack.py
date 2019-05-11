from QuackBehavior import QuackBehavior

class MuteQuack(QuackBehavior):
    def quack(self):
        print("... (slient) ...")

if __name__ == '__main__':
    mq = MuteQuack()
    mq.quack()
