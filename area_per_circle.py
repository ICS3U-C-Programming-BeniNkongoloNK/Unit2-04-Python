#imports math and constants *holds value of radius)
import math
import constants


def main():
    # calculates circumferene and area
    circ = math.pi*2*constants.RAD
    area = math.pi*constants.RAD**2
    print(circ, area)

if __name__ == "__main__":
    main()
