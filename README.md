
# Dustbin Tracking System

The Dustbin Tracking System is an IoT based system. The device can detect when a dust bin is full and send a notification to a software application on a laptop, which is developed using Python and the Tkinter GUI framework. The software application is responsible for storing and displaying the data associated with each dust bin, including its address, longitude and latitude, and the time when it was full.


## Making the device

Assemble following components as given in the circuit diagram.

List of components:
- Arduino UNO R3
- Ultrasonic sensor
- Bluetooth Module HC-05
- Switch x 1
- LED x 2
- Jumper Wires


**Circuit diagram**

![Circuit Diagram](https://via.placeholder.com/468x300?text=Circuit+Diagram+Here)


Install Arduino IDE from [here](https://wiki-content.arduino.cc/en/software)

Upload the arduino code and the device is ready to use.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Mohitbishukarma/Dustbin-Tracking-System.git
```

Go to the project directory

```bash
  cd Dustbin-Tracking-System
```

Install required library

```bash
  pip install -r requirements.txt 
```

Go to the software directory

```bash
  cd software
```

Run the bluetooth_communication.py file in one terminal

```bash
  python bluetooth_communication.py
```
⚠️Beofre running the bluetooth_communication.py file make sure that your systems bluetooth is on and  connected to the dustbin device bluetooth

Run the main.py file in another terminal

```bash
  python main.py
```



##  Most Important Information

There are some bugs in the program that are needed to be fixed. If you can fix them then it will be good.
## Authors

- [@Mohitbishukarma](https://github.com/Mohitbishukarma/)
