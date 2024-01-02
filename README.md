# Jarvis Voice Assistant

Jarvis is a voice controlled virtual assistant that can understand voice commands and complete tasks like opening apps, searching the web, getting the news, and more.

## Installation

Jarvis requires the following Python modules:

```bash
pip install speechRecognition 
pip install pyaudio
pip install pyttsx3
pip install pygame
pip install requests
pip install beautifulsoup4 
pip install pyautogui
pip install pynput
pip install plyer
pip install speedtest-cli
```
There is also an Installer.py file included to install all required modules. Simply run:
```
python Installer.py
```
## Usage
To start Jarvis, run the Jarvis_main.py script:

```python
python Jarvis_main.py
```
You will be prompted to enter a password. The default password is in password.txt.

Once running, say "Wake up" to activate Jarvis. You can now issue voice commands like:

* "Open Chrome" - Launches Google Chrome
* "What's the weather today?" - Reports current weather
* "Search YouTube for cute cats" - Searches YouTube
* "Set an alarm for 7 AM" - Sets an alarm
* "Take a screenshot" - Takes a screenshot

And more! Try asking Jarvis for help or say "What can you do?" to get a full list of supported commands.

## Key Features

* Voice assistant capable of conversation, question-answering, launching apps and websites, 
* controlling the PC, and more
* Customizable commands and personalization like playing your playlists
* Daily agenda/schedule manager
* Alarm clock functionality
* News and weather updates
* Web searches powered by Google, YouTube and Wikipedia APIs
* Password protected access

## Credits
Jarvis was created by Anupam Thackar. The voice and speech recognition functionality uses the SpeechRecognition and PyAudio Python modules. Web scraping code snippets were reused from public GitHub gists.

## License

Jarvis is open source and released under the [MIT] (https://choosealicense.com/licenses/mit/) License. Feel free to reuse the code! 
