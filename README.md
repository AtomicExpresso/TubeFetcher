# TubeFetcher <br> ![version](https://img.shields.io/github/v/release/CinnamonExpresso/TubeFetcher) ![downloads](https://img.shields.io/github/downloads/cinnamonExpresso/TubeFetcher/total) ![License](https://img.shields.io/github/license/CinnamonExpresso/TubeFetcher)

TubeFetcher is a customizable Python-based GUI application that makes it easy to archive and download YouTube videos or audio.

### Preview
![image](https://github.com/user-attachments/assets/31f28fd7-f2b5-4684-894a-d45fbb4062e1)

## Features
- Video queue: Add multiple videos to a list for sequential downloading.
- Video & Audio: Download content in video or audio format.
- Multiple Resolutions: Choose from 1080p, 720p, or 360p. If a specified resolution isn't available, the best alternative will be used.
- Themes: Customize the app’s appearance with a variety of themes.
- Settings Menu: Customize default resolution, download type, file path and more.
- Save System: Automatically saves your preferences.
- Metadata Display: View video metadata in a separate window.
- Free & Open Source: Completely free and open-source software, with clean and well-documented code.

## Usage
1. Paste the video URL into the input box.
2. Press the "Plus" button to add the video to the queue.
3. Once ready, click the "Download" button.
4. Wait for the videos to finish downloading. All files will appear at the specified file path.

## Download
Only tested on Windows 11, however the application may work for different operating systems. 
You can download the latest version of the application from the [Releases page](https://github.com/cinnamonexpresso/TubeFetcher/releases).

Note: The app may take a couple of minutes to load the first time you run it.

## Building from source
If you'd like to download and compile the application yourself, follow these steps:

1. download the repo
```bash
  git clone https://github.com/cinnamonExpresso/TubeFetcher.git
  cd script
```
2. Install the required libraries:
```bash
  pip install -r requirements.txt
```
3. run the app
```bash
  python script.py
```

## Libraries used
- Customtkinter
- Pillow
- Pyperclip
- Requests
- Pytube
- Nuitka

## License
This repository is intended for educational and archival purposes only. TubeFetcher and its contributors are not responsible for any misuse of this software.
TubeFetcher does not condone practices that violate local laws, such as (but not limited to) the DMCA. Users are expected to act responsibly and ensure compliance with applicable laws.

This project is licensed under the MIT License. See the full [license](https://github.com/cinnamonExpresso/TubeFetcher?tab=MIT-1-ov-file) for details.
