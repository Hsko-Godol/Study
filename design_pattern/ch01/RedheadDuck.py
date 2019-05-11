from Duck import Duck

class RedheadDuck(Duck):
    def display(self):
        print("I'm a red head duck!")

if __name__ == '__main__':
    rd = RedheadDuck()

    rd.quack()
    rd.swim()
    rd.display()
    rd.fly()
