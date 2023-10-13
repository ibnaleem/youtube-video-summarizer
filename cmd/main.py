import openai, os, json
import pytube
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


with open("config.json", "r") as f:
    config = json.load(f)

openai.api_key = config["API_KEY"]

url = input("Enter YouTube URL: ")

def download_video(url:str) -> str:
    if url.startswith("https://www.youtube.com/"):

        try:
            yt = YouTube(url)
            stream = yt.streams.filter().first()
            out_file = stream.download()

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            return new_file
        
        except pytube.exceptions.VideoUnavailable:
            raise ValueError("The YouTube video has been deleted, made private, or does not exist.")

        
def transcribe_video(new_file: str) -> str:
        
        audio_file = open(new_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        new_t = transcript["text"]
        return new_t
        
        audio_file = open(new_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        new_t = transcript["text"]

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                  "role":
                  "assistant",
                  "content":
                  f"Your output should use the following template:\n**Summary**\n**Highlights**\n- [Emoji] Bulletpoint\n\nYour task is to summarise the text I have given you in up to ten concise bullet points, starting with a short highlight. Choose an appropriate emoji for each bullet point. Use the text below: {yt.title} {new_t}."
            }])

        with open(f'{yt.title} Summary.txt', "w", encoding="utf-8") as f:
            f.write(response['choices'][0]['message']['content'])

        audio_file.close()
        os.remove(new_file)


else:
    raise ValueError("Your URL is not a YouTube URL. Provide a YouTube URL or check for typos.")
