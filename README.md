# ProjectileMotionCalculator

Known issues:
- There is no trajectory line when initHeight is non-zero because we can't draw it properly using Tkinter's canvas
- The graphical elements are slightly off on Windows machines but the general layout is kept
- Input fields unexpectedly pass the validation and create unexpected behaviors

\
To install the packages needed to run the program type in the terminal:
```
pip3 install -r requirements.txt
```

or install the following manually:
* pygubu
* matplotlib
* termcolor
* ttkthemes

\
To uninstall the packages needed to run the program type in the terminal:
```
pip3 uninstall -r requirements.txt
```
\
To run the app type in the terminal:
```
python3 main.py
```
\
To run automatic tests type in the terminal:
```
python3 automatic_test.py
```
\
To manually test the main functions type in the terminal:
```
python3 Test.py
```
