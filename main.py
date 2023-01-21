import gui
import database
import training
import testing

def main():
    user = gui.get_user()
    while True:
        mode = gui.get_mode()
        if mode == "training":
            training.run_training(user)
        elif mode == "testing":
            testing.run_test(user)

if __name__ == "__main__":
    main()
