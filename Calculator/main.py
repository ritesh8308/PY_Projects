# import keyboard
# def main_loop():
#     while True:
try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))

            print("""What kind of operation do you want to perform:\n
                Press + for addition \n
                Press - for substraction\n 
                Press / for division \n
                Press * for multiplication\n""")
                
            o = input("Enter Operation: ")
            match o:
                case "+":
                    print(f"The result is: {a+b}")
                case "-":
                    print(f"The result is: {a-b}")
                case "/":
                    print(f"The result is: {a/b}")
                case "*":
                    print(f"The result is: {a*b}")
                
                

except Exception as e:
            print("Enter a valid value of a & b")
        
        # # PRESS 'q' TO EXIT
        # if keyboard.is_pressed(''):
        #    print("Loop_Terminated: Thank You")
        
        
        

# main_loop()