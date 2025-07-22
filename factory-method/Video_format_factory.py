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


# ============================
#     Abstract Factory
# ============================
class ExporterFactory(ABC):
    """
    Factory that represents a combination of videao and audio codecs.
    Thr factory doesnt maintain any of the instances it creates.
    The factory simply creates them.
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""


# ===========================
# Concrete factories
# ===========================


class FastExporter(ExporterFactory):
    """Factory Aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a lower speed, higher quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }

    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unkown output quality option: {export_quality}.")


def main() -> None:
    # Get the exporter type
    fac = read_exporter()

    # retrieve video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_type")
    audio_exporter.prepare_export("placeholder_for_type")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
