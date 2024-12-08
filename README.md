## TubeFetcher
TubeFetcher is a python-based application that allows users to archive/download YouTube videos.

![Screenshot 2024-12-01 112349](https://github.com/user-attachments/assets/a95628be-025c-48f4-9192-f15815c9862f)


## Usage
TubeFetcher allows you to download both videos and audio. To get started, input the video url, press the "plus" icon and then hit download. 
All downloads will appear at your specified folder path. If no folder is provided, then a new one will appear at the programs directory.

## Features
- Settings menu: Allows you to specify the default resoultion and download type.
- Video queue: All the videos you want to download will appear in a list and downloaded in order
- Supports both video and audio format: Content can either be in the form of videos or audio
- Multiple resoultions: Supports 1080p, 780p, 360p. If the specified resoultion isnt available, then it will fallback to the next available resoultion

## Requirements
Make sure you have Python installed on your system. The required libraries can be installed using the requirements.txt file.

1. download the repo
```bash
  git clone https://github.com/AtomicExpresso/TubeFetcher.git
  cd script
```
2. Install the required libraries (if you havent already):
```bash
  pip install -r requirements.txt
```
3. run the app
```bash
  python script.py
```

## Libraries used
- CustomTkinter
- Pytube
- Pillow
- Requests

## License
This repository is for educational purposes only. TubeFetcher and it's contributers are not responsible for any misuse of this software. TubeFetcher, does not condone the use of this application in practices that violate local laws such as but not limited to the DMCA. TubeFetcher and its maintainers call upon the personal responsibility of its users to use this application in a fair way, as it is intended to be used.

This app is licencsed under the MIT [license](https://github.com/AtomicExpresso/TubeFetcher?tab=MIT-1-ov-file)
