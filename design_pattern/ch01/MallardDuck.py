from Duck import Duck

class MallardDuck(Duck):
    def display(self):
        print("I'm a mallard duck!")

if __name__ == '__main__':
    md = MallardDuck()

    md.quack()
    md.swim()
    md.display()
    md.fly()
