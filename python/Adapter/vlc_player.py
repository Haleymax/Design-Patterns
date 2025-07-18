"""
VLC播放器类
有不同于目标接口的方法
"""

class VLCPlayer:

    def play_vlc(self, file_name: str) -> None:
        """
        VLC播放器的专用播放方法

        参数:
            file_name: 要播放的文件名
        """
        print(f"Playing VLC file: {file_name}")