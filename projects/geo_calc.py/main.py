#EHCP2

from class_manage import choices, view_shapes_made, compare_shape_data, sort_shapes, select_specific_shape, save_shapes, show_shape_formulas

def main():
    print("Welcome to the Geometry Calculator!")
    while True:
        try:
            choice = int(input("What would you like to do?\n1: Create a Shape\n2: View Shapes\n3: Compare Shape Data\n4: Sort Shapes\n5: Find a shape\n6: Show shape formulas\n7: Exit\n"))
            if choice == 1:
                obj = choices()
                if obj:
                    saved = save_shapes(obj)
                    print("Saved:", saved)
            elif choice == 2:
                view_shapes_made()
            elif choice == 3:
                compare_shape_data()
            elif choice == 4:
                sort_shapes()
            elif choice == 5:
                select_specific_shape()
            elif choice == 6:
                show_shape_formulas()
            elif choice == 7:
                print("Exiting the program!")
                break
            else:
                print("That ain't something you can do!")
        except ValueError:
            print("Make sure to input a number!")
main()