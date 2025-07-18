"""
音频播放器客户端代码
使用适配器来统一不同播放器的接口
"""
from Adapter.media_adapter import MediaAdapter
from Adapter.media_player import MediaPlayer
from Adapter.mp4_player import MP4Player


class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, file_name: str) -> None:
        """
        客户端使用的统一播放方法

        参数:
            audio_type: 媒体类型
            file_name: 要播放的文件名
        """
        audio_type_lower = audio_type.lower()

        if audio_type_lower == "mp4":
            # 直接使用MP4Player，因为它已经实现了MediaPlayer接口
            player = MP4Player()
            player.play(audio_type, file_name)
        elif audio_type_lower in ["vlc", "avi"]:
            # 使用适配器来适配不同接口的播放器
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media. {audio_type} format not supported")