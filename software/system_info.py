from tkinter import Canvas
def make_system_info_view(parent_frame:str)-> None:
    canvas = Canvas(
    parent_frame,
    bg = "#FFFFFF",
    height = 600,
    width = (1000-277),
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    # DESCRIPTION SECTION
    canvas.create_text(
        (1000-277)/2 -30,
        5.0+20,
        anchor="nw",
        text="System Info",
        fill="#2F3061",
        font=("Lato Bold", 20 * -1)
    )
    canvas.create_rectangle(
        19.0,
        71.0,
        623.0+75,
        178.0,
        fill="#F0F2FF",
        outline="")
    canvas.create_text(
        33.0,
        77.0,
        anchor="nw",
        text="Desciption",
        fill="#2F3061",
        font=("Lato Medium", 18 * -1)
    )

    canvas.create_rectangle(
        33.0,
        99.0,
        82.01063537597656,
        101.0,
        fill="#2F3061",
        outline="")


    canvas.create_text(
        35.0,
        115.0,
        anchor="nw",
        text="The waste management system is a software tool that helps track the status of dust bins in a\ngiven area. It is designed to detect when dust bins are full and provide this information to the\nuser through the software interface.",
        fill="#000000",
        font=("Lato Regular", 16 * -1)
    )
    # SYSTEM COMPONENTS SECTION
    canvas.create_rectangle(
        19.0,
        192.0,
        623.0+75,
        565.0+20,
        fill="#F0F2FF",
        outline="")
    canvas.create_text(
        33.0,
        208.0,
        anchor="nw",
        text="System Components",
        fill="#2F3061",
        font=("Lato Medium", 18 * -1)
    )
    canvas.create_rectangle(
        33.0,
        230.0,
        127.010009765625,
        232.0,
        fill="#2F3061",
        outline="")
    canvas.create_text(
        35.0,
        246.0,
        anchor="nw",
        text="The system consists of an Arduino board, which is responsible for collecting data from sensors\nattached to the dust bins, and a software interface developed using Python and Tkinter.The\nArduino board is connected to the 9V battery which is connected to the sensor box.",
        fill="#000000",
        font=("Lato Regular", 16 * -1)
    )
    canvas.create_text(
        35.0,
        308.0,
        anchor="nw",
        text="Hardware",
        fill="#2F3061",
        font=("Lato SemiBold", 16 * -1)
    )
    canvas.create_text(
        59.0,
        328.0,
        anchor="nw",
        text="1. Arduino UNO R3\n2. Ultarsonic Sensor HC-SR04\n3. Bluetooth Module HC-05\n4. Jumper Wires\n5. LEDs\n6. Resistors",
        fill="#000000",
        font=("Lato Regular", 16 * -1)
    )
    canvas.create_text(
        35.0,
        438.0,
        anchor="nw",
        text="Software",
        fill="#2F3061",
        font=("Lato SemiBold", 16 * -1)
    )

    canvas.create_text(
        60.0,
        458.0,
        anchor="nw",
        text="1.Python Programming Language\n2. C/C++ Programming Language\n3. Tkinter Library \n4. Visual Studio Code\n5. Figma\n6. Arduino IDE",
        fill="#000000",
        font=("Lato Regular", 16 * -1)
    )

