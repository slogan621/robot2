from adafruit_motorkit import MotorKit
import sys

def right(kit):
    kit.motor2.throttle = 0.0
    kit.motor4.throttle = 0.5

def left(kit):
    kit.motor2.throttle = 0.0
    kit.motor4.throttle = 0.5

def forward(kit): 
    kit.motor2.throttle = 0.5
    kit.motor4.throttle = 0.5

def forwardr(kit): 
    kit.motor2.throttle = 0.5
    kit.motor4.throttle = 0.6

def forwardl(kit): 
    kit.motor2.throttle = 0.6
    kit.motor4.throttle = 0.5

def back(kit):
    kit.motor2.throttle = -0.5
    kit.motor4.throttle = -0.5

def backr(kit):
    kit.motor2.throttle = -0.5
    kit.motor4.throttle = -0.6

def backl(kit):
    kit.motor2.throttle = -0.6
    kit.motor4.throttle = -0.5

def stop(kit):
    kit.motor2.throttle = 0.0
    kit.motor4.throttle = 0.0

def main():
    kit = MotorKit()
    command = sys.argv[1]
    if command == "left":
        left(kit)
    elif command == "right":
        right(kit)
    elif command == "forward":
        forward(kit)
    elif command == "forwardr":
        forwardr(kit)
    elif command == "forwardl":
        forwardl(kit)
    elif command == "back":
        back(kit)
    elif command == "backr":
        backr(kit)
    elif command == "backl":
        backl(kit)
    elif command == "stop":
        stop(kit)

if __name__ == "__main__":
    main()
