"""
Example of factory method being used eith different types
of video formats
"""

import pathlib
from abc import ABC, abstractmethod

# ==========================================================#
#                 Video Class and Interface
# ==========================================================#


class VideoExporter(ABC):
    """Interface definition to export video formats"""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Concrete class for Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """concrete class for H264 video format"""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """concrete class for H264 high quality video format"""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


# ===============================================================#
#              Audio Class & Interface
# ===============================================================#


class AudioExporter(ABC):
    """Interface for the audio exporter classes"""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder"""


class AACAudioExporter(AudioExporter):
    """Concrete AAC audio exporting class"""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """Concrete Wav lossless audio exporter class"""

    def prepare_export(self, audio_data):
        print("Preparing audo data for WAV export.")

    def do_export(self, folder):
        print(f"Exporting audio data in WAV format to {folder}.")


def main() -> None:

    # read the disred export quality
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unkown output quality option: {export_quality}.")

    # create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter
    else:
        # default: master quality
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_type")
    audio_exporter.prepare_export("placeholder_for_type")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

    if __name__ == "__main__":
        main()
