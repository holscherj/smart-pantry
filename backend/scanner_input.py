#############################################################
# scanner_input.py
# Jack Holscher
#
# A running loop to accept input from the barcode scanner
# Terminates on when user types quit
#############################################################

from pantry_class import Pantry
pantry = Pantry()

def main():
    print("Scan an item or type 'quit' to exit...")
    while True:
        user_input = input()
        if user_input.lower() == "quit":
            break

        pantry.add_item(user_input)
        
    pantry.close_pantry()
    

if __name__ == '__main__':
    main()