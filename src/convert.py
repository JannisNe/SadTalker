import moviepy.editor as mp
from pathlib import Path


audio_extensions = ["mp3", "wav"]
video_extensions = ["mp4", "avi", "mov"]


class Converter:

    def __init__(self, video_path):
        self.video_path = Path(video_path)
        self.video = mp.VideoFileClip(video_path)
        self.audio = self.video.audio

    def to(self, extension, output_path=None):
        extension = extension.lower()
        if output_path is None:
            output_path = self.video_path.with_suffix(f'.{extension}')
        if extension in audio_extensions:
            obj = self.audio
        elif extension in video_extensions:
            obj = self.video
        else:
            raise ValueError(f"Unsupported extension {extension}")
        obj.write_videofile(output_path)
        return output_path

    @classmethod
    def get_type(cls, extension):
        if Path(extension).suffix.lower() in audio_extensions:
            return "audio"
        elif Path(extension).suffix.lower() in video_extensions:
            return "video"
        else:
            return None
