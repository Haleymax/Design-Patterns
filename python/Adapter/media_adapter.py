"""
媒体适配器实现
将不同的播放器接口适配到统一的MediaPlayer接口
"""
from Adapter.avi_player import AviPlayer
from Adapter.media_player import MediaPlayer
from Adapter.mp4_player import MP4Player
from Adapter.vlc_player import VLCPlayer


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        """
        初始化适配器

        参数:
            audio_type: 要适配的媒体类型
        """
        self.audio_type = audio_type.lower()

        # 根据类型创建对应的播放器实例
        if self.audio_type == "vlc":
            self.advanced_player = VLCPlayer()
        elif self.audio_type == "avi":
            self.advanced_player = AviPlayer()
        elif self.audio_type == "mp4":
            self.advanced_player = MP4Player()
        else:
            raise ValueError(f"Unsupported media type: {audio_type}")

    def play(self, audio_type: str, file_name: str) -> None:
        """
        实现统一的播放接口

        参数:
            audio_type: 媒体类型
            file_name: 要播放的文件名
        """
        if self.audio_type == "vlc":
            self.advanced_player.play_vlc(file_name)
        elif self.audio_type == "avi":
            self.advanced_player.play_avi(file_name)
        elif self.audio_type == "mp4":
            self.advanced_player.play(audio_type, file_name)