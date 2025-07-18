"""
具体的MP4播放器实现
只能播放MP4格式文件
"""
from Adapter.media_player import MediaPlayer


class MP4Player(MediaPlayer):

    def play(self, audio_type: str, file_name: str) -> None:
        """
        实现MP4文件袋播放

        参数:
            audio_type (str): 媒体文件的类型（应为 'mp4'）
            file_name (str): 媒体文件的名称
        """
        if audio_type.lower() == 'mp4':
            print(f"Playing MP4 file: {file_name}")
        else:
            print(f"MP4Player: Unsupported audio type '{audio_type}' for file '{file_name}'")