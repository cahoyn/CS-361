# Author: Nathan Cahoy
# CS361 Term Project
# Description: A unit converter that will be added to over time,
# beginning with a temperature converter between C and F

def C_to_F(c_val):
    og_val = int(c_val)
    f_val = (og_val)*(9/5) + 32
    return f_val

def F_to_C(f_val):
    og_val = int(f_val)
    c_val = (og_val - 32)*(5/9)
    return c_val

def kg_to_lb(kg_val):
    og_val = int(kg_val)
    lb_val = (og_val)*(2.205)
    return lb_val

def lb_to_kg(lb_val):
    og_val = int(lb_val)
    kg_val = (og_val)/(2.205)
    return kg_val

if __name__ == '__main__':
    while True:
        print("Welcome to Cahoy's Conversions, where your unit conversions are just a few clicks away! Here's what's new:")
        print("Users now have the option to convert weight between pounds and kilograms!")
        print("Users can also convert temperatures between Fahrenheit and Celsius.")
        cont = True
        while cont is True:
            print("Would you like to make a weight or temperature conversion? Type W for weight or T for temperature: ")
            inp = input()
            if inp == "T":
                print("Type C to convert from Fahrenheit to Celsius or type F to convert from Celsius to Fahrenheit: ")
                typ = input()
                if typ == "C":
                    print("Enter the value you'd like to convert from F to C (number only): ")
                    f_val = input()
                    c_val = F_to_C(f_val)
                    f_val_str = str(f_val)
                    c_val_str = str(c_val)
                    print(f_val_str + " degrees Fahrenheit is " + c_val_str + " degrees Celsius!")
                    # end or ask for another conversion
                    print("Would you like to make another conversion? Type Y or N: ")
                    inp2 = input()
                    if inp2 == "Y":
                        # cont is still True
                        cont = True
                    else:
                        print("Thank you for using Cahoy's Conversions!")
                        cont = False
                        break
                elif typ == "F":
                    print("Enter the value you'd like to convert from C to F (number only): ")
                    c_val = input()
                    f_val = C_to_F(c_val)
                    f_val_str = str(f_val)
                    c_val_str = str(c_val)
                    print(c_val_str + " degrees Celsius is " + f_val_str + " degrees Fahrenheit!")
                    # end or ask for another conversion
                    print("Would you like to make another conversion? Type Y or N: ")
                    inp2 = input()
                    if inp2 == "Y":
                        # cont is still True
                        cont = True
                    else:
                        print("Thank you for using Cahoy's Conversions!")
                        cont = False
                        break
                else:
                    print("Invalid entry, please try again.")
            elif inp == "W":
                print("Type P to convert from kilograms to pounds or type K to convert from pounds to kilograms: ")
                typ = input()
                if typ == "P":
                    print("Enter the value you'd like to convert from kg to lbs (number only): ")
                    kg_val = input()
                    lb_val = kg_to_lb(kg_val)
                    lb_val_str = str(lb_val)
                    kg_val_str = str(kg_val)
                    print(kg_val_str + " kilograms is " + lb_val_str + " pounds!")
                    # end or ask for another conversion
                    print("Would you like to make another conversion? Type Y or N: ")
                    inp2 = input()
                    if inp2 == "Y":
                        # cont is still True
                        cont = True
                    else:
                        print("Thank you for using Cahoy's Conversions!")
                        cont = False
                        break
                elif typ == "K":
                    print("Enter the value you'd like to convert from lbs to kg (number only): ")
                    lb_val = input()
                    kg_val = lb_to_kg(lb_val)
                    lb_val_str = str(lb_val)
                    kg_val_str = str(kg_val)
                    print(lb_val_str + " pounds is " + kg_val_str + " kilograms!")
                    # end or ask for another conversion
                    print("Would you like to make another conversion? Type Y or N: ")
                    inp2 = input()
                    if inp2 == "Y":
                        # cont is still True
                        cont = True
                    else:
                        print("Thank you for using Cahoy's Conversions!")
                        cont = False
                        break
                else:
                    print("Invalid entry, please try again.")
            else:
                print("Invalid input.")
        break

        # Future implementations: add ounces to weight options
        # Length: feet to meters
        # Time: seconds, minutes, hours, days
