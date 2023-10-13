import openai, os, json
import pytube
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


with open("config.json", "r") as f:
    config = json.load(f)

openai.api_key = config["API_KEY"]


def download_video(url: str) -> str:
    if url.startswith("https://www.youtube.com/"):

        try:
            global yt
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


def main(new_t: str) -> bool:
        
        with open("note.txt", "r") as f:
             format = f.read()

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                  "role":
                  "assistant",
                  "content":
                  f"Your output should use the following template given the provided transcription:\n{format}"
            }])

        with open(f'{yt.title} Summary.txt', "w", encoding="utf-8") as f:
            f.write(response['choices'][0]['message']['content'])

        return True


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")

    new_file = download_video(url)
    new_t = transcribe_video(new_file)
    main(new_t)

    if main() is True:
        os.remove(new_file)
    else:
         raise RuntimeError("Unsuccessful, aborting...")