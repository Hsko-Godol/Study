from MallardDuck import MallardDuck
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck

def main():
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.swim()
    mallard.display()
    mallard.performFly()

    print("-----------------------")

    redhead = RedheadDuck()
    redhead.performQuack()
    redhead.swim()
    redhead.display()
    redhead.performFly()

    print("-----------------------")

    rubber = RubberDuck()
    rubber.performQuack()
    rubber.swim()
    rubber.display()
    rubber.performFly()

if __name__ == '__main__':
    main()
