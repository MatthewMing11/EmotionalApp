# EmotionalApp
This app was made by Shayan Chowdhury, Henry He, Matthew Ming, and Larry Wong with the help of our Google mentor, Alex Liu.

# Roles
* Matthew Ming provided the background interface made in Kivy.
* Larry Wong assisted Shayan Chowdhury in coding the main program
* Henry He assembled the test data with Larry.

# Instructions(Linux only)
1. Install the necessary packages using the command
```python
python3 -m pip install --upgrade --user pip setuptools virtualenv
```
2. Make the virtual environment if you don't have one.
```python
 python3 -m virtualenv ~/kivy_venv
 source ~/kivy_venv/bin/activate
```
3. Install kivy inside the virtual environment.
```python
python3 -m pip install kivy
```
4. Install requirements with the following command.
```python
pip install SpeechRecognition numpy nltk keras tensorflow sklearn
```
5. Run the following commands to install remaining modules.
```python
python3
import nltk
nltk.download('punkt')
Ctrl+D
```
6. Run main.py
```python
python3 main.py
```
# Pitfalls
Due to the scarcity of data on emotional connotation in language, we were unable to fully interpret emotion based on data.
