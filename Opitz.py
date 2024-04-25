"""
Import modules
"""
from tkinter import *
from Utils import *


#setup the window
root = Tk()
root.title("Opitz Coding")
screenWidth = 800
screenHeight = 600
root.geometry(str(screenWidth)+'x'+str(screenHeight))
root.iconbitmap("icon.ico")

"""
functions
"""
CODE = ["X","X","X","X","X"]
outputParts = []
totalOutputParts = []

def Digit1st():
    clear_widgets(root)
    global CODE
    global totalOutputParts
    global outputParts
    outputParts = []
    outputParts.append('')
    print(totalOutputParts)
    def show_fields():
        a_label.pack_forget()
        a_entry.pack_forget()
        b_label.pack_forget()
        b_entry.pack_forget()
        c_label.pack_forget()
        c_entry.pack_forget()
        length_label.pack_forget()
        length_entry.pack_forget()
        diameter_label.pack_forget()
        diameter_entry.pack_forget()

        if var.get() == 2:  # NON-Rotational selected
            a_label.pack()
            a_entry.pack()
            b_label.pack()
            b_entry.pack()
            c_label.pack()
            c_entry.pack()
        else:  #rotational selected
            length_label.pack()
            length_entry.pack()
            diameter_label.pack()
            diameter_entry.pack()

    def calculate_code():
        if var.get() == 1:  # Rotational selected
            length = float(length_entry.get())
            diameter = float(diameter_entry.get())
            Ld_ratio = length / diameter
            if Ld_ratio <= 0.5:
                CODE[0] = "0"
            elif 0.5 < Ld_ratio < 3:
                CODE[0] = "1"
            else:
                CODE[0] = "2"
            my_string = ''.join(CODE)
            my_string = ''.join(CODE)
            code_label.config(text=f"Code: {my_string}")
            partSpecs = str(int(length)) +' '+ str(int(diameter))
            outputParts[0] = partSpecs

            
            
        else:  # Non-rotational selected
            A = float(a_entry.get())
            B = float(b_entry.get())
            C = float(c_entry.get())
            # Calculate code based on A, B, C values
            # code for non rotetional parts will be on future versions


        Digit2Button = Button(root, text='Next',command=Digit2st,width=25,height=3, bg='green')
        Digit2Button.place(x=screenWidth*0.75,y=screenHeight*0.88)



    var = IntVar()

    rotational_radio = Radiobutton(root, text="Rotational", variable=var, value=1, command=show_fields)
    rotational_radio.pack()

    non_rotational_radio = Radiobutton(root, text="Non-Rotational", variable=var, value=2, command=show_fields)
    non_rotational_radio.pack()

    a_label = Label(root, text="A:")
    a_label.pack_forget()
    a_entry = Entry(root)
    a_entry.pack_forget()

    b_label = Label(root, text="B:")
    b_label.pack_forget()
    b_entry = Entry(root)
    b_entry.pack_forget()

    c_label = Label(root, text="C:")
    c_label.pack_forget()
    c_entry = Entry(root)
    c_entry.pack_forget()

    length_label = Label(root, text="Length:")
    length_label.pack_forget()
    length_entry = Entry(root)
    length_entry.pack_forget()

    diameter_label = Label(root, text="Diameter:")
    diameter_label.pack_forget()
    diameter_entry = Entry(root)
    diameter_entry.pack_forget()

    code_label = Label(root, text="Opitz Code:")
    code_label.place(x=370,y=380)

    calculate_button = Button(root, text="Calculate", command=calculate_code,width=25,height=3, bg='light sky Blue')
    calculate_button.place(x=320,y=400)


def Digit2st():
    clear_widgets(root)
    global CODE
    global totalOutputParts
    global outputParts
    def show_sub_options():
        if var.get() == 2:  # Stepped on one side
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()
            sub_option1.pack()
            sub_option2.pack()
            sub_option3.pack()
        elif var.get() == 3:  # Stepped on both sides
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()
            sub_option4.pack()
            sub_option5.pack()
            sub_option6.pack()
        else:
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()

    def calculate_outdigit():
        outdigit = 0
        if var.get() == 1:  # Smooth
            outdigit = 0
            outputParts.append('turning')
        elif var.get() == 2:  # Stepped on one side
            outdigit = sub_var.get() + 1
				
        elif var.get() == 3:  # Stepped on both sides
            outdigit = sub_var.get() + 1

        CODE[1]= str(outdigit)
        my_string = ''.join(CODE)
        output_label.config(text=f"Code: {my_string}")
        Digit2Button = Button(root, text='Next',command=Digit3rd,width=25,height=3, bg='green')
        Digit2Button.place(x=screenWidth*0.75,y=screenHeight*0.88)
        if outdigit == 1:
            outputParts.append('turning')
        elif outdigit == 2:
            outputParts.append('turningThreading')
        elif outdigit == 3:
            outputParts.append('turningGrooving')
        elif outdigit == 4:
            outputParts.append('turning')
            outputParts.append('turning')
        elif outdigit == 5:
            outputParts.append('turningThreading')
            outputParts.append('turningThreading')
        elif outdigit == 6:
            outputParts.append('turningGrooving')
            outputParts.append('turningGrooving')


    feature_label = Label(root, text="External Features")
    feature_label.pack()

    var = IntVar()
    smooth_radio = Radiobutton(root, text="Smooth", variable=var, value=1, command=show_sub_options)
    smooth_radio.pack()

    stepped_one_radio = Radiobutton(root, text="Stepped on one side", variable=var, value=2, command=show_sub_options)
    stepped_one_radio.pack()

    stepped_both_radio = Radiobutton(root, text="Stepped on both sides", variable=var, value=3, command=show_sub_options)
    stepped_both_radio.pack()
    sub_var = IntVar()

    sub_option1 = Radiobutton(root, text="Smooth", variable=sub_var, value=0)
    sub_option2 = Radiobutton(root, text="Thread", variable=sub_var, value=1)
    sub_option3 = Radiobutton(root, text="Groove", variable=sub_var, value=2)

    sub_option4 = Radiobutton(root, text="Smooth", variable=sub_var, value=3)
    sub_option5 = Radiobutton(root, text="Thread", variable=sub_var, value=4)
    sub_option6 = Radiobutton(root, text="Groove", variable=sub_var, value=5)


    output_label = Label(root, text="Opitz Code: ")
    output_label.place(x=370,y=380)

    calculate_button = Button(root, text="Calculate", command=calculate_outdigit,width=25,height=3, bg='light sky Blue')
    calculate_button.place(x=320,y=400)

   


def Digit3rd():
    clear_widgets(root)
    global CODE
    global totalOutputParts
    global outputParts
    def show_sub_options():
        if var.get() == 2:  # Smooth or stepped on one side
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()           
            sub_option1.pack()
            sub_option2.pack()
            sub_option3.pack()
        elif var.get() == 3:  # Stepped on both sides
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()            
            sub_option4.pack()
            sub_option5.pack()
            sub_option6.pack()
        else:
            sub_option1.pack_forget()
            sub_option2.pack_forget()
            sub_option3.pack_forget()
            sub_option4.pack_forget()
            sub_option5.pack_forget()
            sub_option6.pack_forget()

    def calculate_outdigit():
        outdigit = 0
        if var.get() == 1:  # No hole
            outdigit = 0
        elif var.get() == 2:  # Smooth or stepped on one side
            outdigit = sub_var.get() + 1
        elif var.get() == 3:  # Stepped on both sides
            outdigit = sub_var.get() + 1
        CODE[2]= str(outdigit)
        my_string = ''.join(CODE)
        output_label.config(text=f"Code: {my_string}")
        Digit3Button = Button(root, text='Next',command=Digit4th,width=25,height=3, bg='green')
        Digit3Button.place(x=screenWidth*0.75,y=screenHeight*0.88)
        if outdigit == 1:
            outputParts.append('turning')
        elif outdigit == 2:
            outputParts.append('turningThreading')
        elif outdigit == 3:
            outputParts.append('turningGrooving')
        elif outdigit == 4:
            outputParts.append('turning')
            outputParts.append('turning')
        elif outdigit == 5:
            outputParts.append('turningThreading')
            outputParts.append('turningThreading')
        elif outdigit == 6:
            outputParts.append('turningGrooving')
            outputParts.append('turningGrooving')
		
        
        
    feature_label = Label(root, text="Internal Features")
    feature_label.pack()

    var = IntVar()
    no_hole_radio = Radiobutton(root, text="No hole", variable=var, value=1, command=show_sub_options)
    no_hole_radio.pack()

    smooth_or_stepped_radio = Radiobutton(root, text="Smooth or stepped on one side", variable=var, value=2, command=show_sub_options)
    smooth_or_stepped_radio.pack()

    stepped_both_radio = Radiobutton(root, text="Stepped on both sides", variable=var, value=3, command=show_sub_options)
    stepped_both_radio.pack()
    sub_var = IntVar()

    sub_option1 = Radiobutton(root, text="No shape", variable=sub_var, value=0)
    sub_option2 = Radiobutton(root, text="Thread", variable=sub_var, value=1)
    sub_option3 = Radiobutton(root, text="Groove", variable=sub_var, value=2)

    sub_option4 = Radiobutton(root, text="No shape", variable=sub_var, value=3)
    sub_option5 = Radiobutton(root, text="Thread", variable=sub_var, value=4)
    sub_option6 = Radiobutton(root, text="Groove", variable=sub_var, value=5)


    output_label = Label(root, text="Opitz Code: ")
    output_label.place(x=370,y=380)

    calculate_button = Button(root, text="Calculate", command=calculate_outdigit,width=25,height=3, bg='light sky Blue')
    calculate_button.place(x=320,y=400)

    

def Digit4th():
    clear_widgets(root)
    global CODE
    def get_digit():
        CODE[3]= str(selected_digit.get())
        my_string = ''.join(CODE)
        output_label.config(text=f"Code: {my_string}")
        Digit3Button = Button(root, text='Next',command=Digit5th,width=25,height=3, bg='green')
        Digit3Button.place(x=screenWidth*0.75,y=screenHeight*0.88)
        return selected_digit.get()

    selected_digit = IntVar()



    Radiobutton(root, text="No surface machining", variable=selected_digit, value=0).pack(anchor=CENTER)
    Radiobutton(root, text="Surface plane or curved in one direction", variable=selected_digit, value=1).pack(anchor=CENTER)
    Radiobutton(root, text="External plane circle related to graduation around a circle", variable=selected_digit, value=2).pack(anchor=CENTER)
    Radiobutton(root, text="External groove or slot", variable=selected_digit, value=3).pack(anchor=CENTER)
    Radiobutton(root, text="External spline", variable=selected_digit, value=4).pack(anchor=CENTER)
    Radiobutton(root, text="External plane surface or slot, external spline", variable=selected_digit, value=5).pack(anchor=CENTER)
    Radiobutton(root, text="Internal plane surface or slot", variable=selected_digit, value=6).pack(anchor=CENTER)
    Radiobutton(root, text="Internal spline", variable=selected_digit, value=7).pack(anchor=CENTER)
    Radiobutton(root, text="Internal and external groove or slot", variable=selected_digit, value=8).pack(anchor=CENTER)
    Radiobutton(root, text="All others", variable=selected_digit, value=9).pack(anchor=CENTER)

    output_label = Label(root, text="Opitz Code: ")
    output_label.place(x=370,y=380)


    calculate_button = Button(root, text="Calculate", command=get_digit,width=25,height=3, bg='light sky Blue')
    calculate_button.place(x=320,y=400)

    
def Digit5th():
    clear_widgets(root)
    global CODE
    global totalOutputParts
    global outputParts
    totalOutputParts.append(outputParts)
    
    def show_buttons(case):
        if case == 1:
            case_1_buttons.pack()
            case_2_buttons.pack_forget()
            case_3_buttons.pack_forget()
        elif case == 2:
            case_1_buttons.pack_forget()
            case_2_buttons.pack()
            case_3_buttons.pack_forget()
        elif case == 3:
            case_1_buttons.pack_forget()
            case_2_buttons.pack_forget()
            case_3_buttons.pack()
        

    def get_digit():
        DigitCode =0
        if case.get() == 1:
            DigitCode = selected_digit_case_1.get()
        elif case.get() == 2:
            DigitCode = selected_digit_case_2.get()
        elif case.get() == 3:
            DigitCode = selected_digit_case_3.get()
        CODE[4] = str(DigitCode)
        my_string = ''.join(CODE)
        output_label.config(text=f"Code: {my_string}")
        Digit4Button = Button(root, text='Finish',command=finish,width=25,height=3, bg='green')
        Digit4Button.place(x=screenWidth*0.75,y=screenHeight*0.88)
        

    case = IntVar()
    selected_digit_case_1 = IntVar()
    selected_digit_case_2 = IntVar()
    selected_digit_case_3 = IntVar()

    Radiobutton(root, text="Case 1: No Gear", variable=case, value=1, command=lambda: show_buttons(1)).pack(anchor=CENTER)
    Radiobutton(root, text="Case 2: With Gear", variable=case, value=2, command=lambda: show_buttons(2)).pack(anchor=CENTER)
    Radiobutton(root, text="Case 3: Other", variable=case, value=3, command=lambda: show_buttons(3)).pack(anchor=CENTER)

    case_1_buttons = Frame(root)
    Radiobutton(case_1_buttons, text="No Auxillary hole", variable=selected_digit_case_1, value=0).pack(anchor=CENTER)
    Radiobutton(case_1_buttons, text="Axial, not on pitch circle diameter", variable=selected_digit_case_1, value=1).pack(anchor=CENTER)
    Radiobutton(case_1_buttons, text="Axial on pitch circle diameter", variable=selected_digit_case_1, value=2).pack(anchor=CENTER)
    Radiobutton(case_1_buttons, text="Radial, not on pitch circle diameter", variable=selected_digit_case_1, value=3).pack(anchor=CENTER)
    Radiobutton(case_1_buttons, text="Axial or/and radial or/and other direction", variable=selected_digit_case_1, value=4).pack(anchor=CENTER)
    Radiobutton(case_1_buttons, text="Axial or/and radial on PCD or/and other direction", variable=selected_digit_case_1, value=5).pack(anchor=CENTER)

    case_2_buttons = Frame(root)
    Radiobutton(case_2_buttons, text="Spur Gear", variable=selected_digit_case_2, value=6).pack(anchor=CENTER)
    Radiobutton(case_2_buttons, text="Bevel Gear", variable=selected_digit_case_2, value=7).pack(anchor=CENTER)
    Radiobutton(case_2_buttons, text="Other Gear Slot", variable=selected_digit_case_2, value=8).pack(anchor=CENTER)

    case_3_buttons = Frame(root)
    Radiobutton(case_3_buttons, text="All Others", variable=selected_digit_case_3, value=9).pack(anchor=CENTER)

    output_label = Label(root, text="Opitz Code: ")
    output_label.place(x=370,y=380)


    calculate_button = Button(root, text="Calculate", command=get_digit,width=25,height=3, bg='light sky Blue')
    calculate_button.place(x=320,y=400)


def writePartsFile():
    global totalOutputParts
    
    # Open a file for reading
    file_path = 'Operations.txt'

    with open(file_path, 'w') as file:
        for part in totalOutputParts:
            # Convert the list to a string
            line = ' '.join(map(str, part)) + '\n'
            # Write the string to the file
            file.write(line)

            
            

            
    
def finish():
    clear_widgets(root)
    global CODE

    output_label = Label(root, text=f"Opitz Code: {''.join(CODE)}",font=('Helvatical bold',20), bg='green')
    output_label.place(x=280,y=250)
    RepeatButton = Button(root, text='Repeat',command=Digit1st,width=25,height=3, bg='yellow')
    RepeatButton.place(x=screenWidth*0.75,y=screenHeight*0.78)
    FinishButton = Button(root, text='Finish',command=writePartsFile ,width=25,height=3, bg='red')
    FinishButton.place(x=screenWidth*0.75,y=screenHeight*0.88)
    CODE = ["X","X","X","X","X"]


"""
LOAD the credits screen
"""
# Load the image
tk_image = ImageTk.PhotoImage(Image.open("Background.png"))
# Create a Label widget with the image
label = Label(root, text="Opitz",image=tk_image)
label.pack()

StartButton = Button(root, text='Start',command=Digit1st,width=25,height=3, bg='green')
StartButton.place(x=screenWidth*0.75,y=screenHeight*0.88)






root.mainloop()