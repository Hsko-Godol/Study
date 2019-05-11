from Duck import Duck

class ReadheadDuck(Duck):
    def display(self):
        print("I'm a readhead duck!")

if __name__ == '__main__':
    md = ReadheadDuck()

    md.quack()
    md.swim()
    md.display()
    md.fly()
