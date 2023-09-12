# Youtube Video Summarizer
This is a tool that utilizes the power of OpenAI's Whisper API and PyTube library to download YouTube videos, transcribe them, and generate summaries using the GPT-3.5 language model.

# Dependencies
To run this application, you need the following dependencies installed:

- [OpenAI](https://pypi.org/project/openai/): The Whisper & GPT-3.5 API from OpenAI is used for transcription and summarization.
- [OpenAI API Key](https://platform.openai.com/account/api-keys): to use OpenAI's APIs 
- [PyTube](https://pytube.io/en/latest/user/install.html): A lightweight, dependency-free library to download YouTube videos.

# How It Works
1. Video Download: The [PyTube library](https://pytube.io/en/latest/user/install.html) is used to download the YouTube video specified by the user. The video is saved locally for further processing.
2. Transcription: The downloaded video is then transcribed using [OpenAI's Whisper API](https://platform.openai.com/docs/api-reference/audio). Whisper is a state-of-the-art automatic speech recognition (ASR) system that converts spoken language into written text. It provides accurate transcriptions of the audio content.
3. Summarization: The generated transcription is passed to the [GPT-3.5 language model](https://platform.openai.com/docs/api-reference/chat/create), which is capable of understanding and generating human-like text. It analyzes the transcription and generates a concise summary of the video's content.

# Getting Started
1. Clone the repository to your local machine:
```bash
$ git clone https://github.com/ibnaleem/youtube-video-summarizer.git
```
2. Install the required dependencies. Make sure you have the [latest version of Python](https://www.python.org/downloads/) and pip installed. Run the following commands:

```bash
$ cd /cmd
$ pip install -r requirements.txt
```
3. Set up your OpenAI API credentials. You will need to create an account on OpenAI's platform and obtain an API key. Then, set the `API_KEY` variable in `config.json` with your API key.
```json
{
  "API_KEY": ""
}
```
4. Run the script and you should be prompted to provide a YouTube URL:
```cmd
Enter YouTube URL:
```
5. Check your `/cmd` directory for a `.txt` file.

# Configuration
You can modify some aspects of the summarization process by adjusting the following parameters in the script:
1. Whisper Model: Currently, only `whisper-1` model is available. If you have access to another Whisper model, you can change `transcript = openai.Audio.transcribe("whisper-1", audio_file)` in `main.py` (line 25)
2. GPT Model: If you have access to GPT-4, you can change `response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{...}]` in `main.py` (line 28)

# License
This project is licensed under the MIT License.

Feel free to contribute, open issues, and suggest improvements.
