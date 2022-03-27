from components import tools
import pygame
def main():
    print("Hello world!")
    adder = tools.calculator()
    print(adder.add(1,2))
    print(tools.mult(10, 20))
    return
if __name__ == "__main__":
    main()