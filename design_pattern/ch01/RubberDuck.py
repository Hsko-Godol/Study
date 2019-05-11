from Duck import Duck

class RubberDuck(Duck):
    def quack(self):
        print("RubberDuck's QUACK!")

    def display(self):
        print("I'm a rubber duck")

if __name__ == '__main__':
    md = RubberDuck()

    md.quack()
    md.swim()
    md.display()
    md.fly()
