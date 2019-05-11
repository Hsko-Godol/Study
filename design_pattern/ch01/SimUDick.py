from Duck import Duck

from MallardDuck import MallardDuck
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck
from ModelDuck import ModelDuck

from FlyRocketPowered import FlyRocketPowered

def main():
    mallard:Duck = MallardDuck()
    mallard.performQuack()
    mallard.swim()
    mallard.display()
    mallard.performFly()

    print("-----------------------")

    redhead:Duck = RedheadDuck()
    redhead.performQuack()
    redhead.swim()
    redhead.display()
    redhead.performFly()

    print("-----------------------")

    rubber:Duck = RubberDuck()
    rubber.performQuack()
    rubber.swim()
    rubber.display()
    rubber.performFly()

    print("-----------------------")

    model:Duck = ModelDuck()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()

if __name__ == '__main__':
    main()
