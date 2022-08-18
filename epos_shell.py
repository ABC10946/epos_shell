from escpos.printer import Usb
import subprocess
import os

def main():
    p = Usb(0x416, 0x5011, in_ep=0x81, out_ep=0x03, profile="POS-5890")

    while True:
        p.text(">")
        input_line = input().split(" ")
        command = input_line[0]
        args = input_line[1:]
        p.text(command + "\n")
        if command == "exit":
            break
        elif command == "cd":
            if os.path.exists(" ".join(args)):
                print(args)
                os.chdir(" ".join(args))
                continue
            else:
                p.text("Directory not found\n\n")
                continue
            
        command_output = subprocess.getoutput(command + " ".join(args))
        p.text(command_output + "\n\n\n")


    p.cut()

if __name__ == "__main__":
    main()
