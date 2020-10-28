import Logic.Logic as logic
import time

if __name__ == "__main__":
    try:
        while(True):
            print("This is Main")
            logic.one_input_one_output(1, 4)

    except KeyboardInterupt:
        print("program stopped")



