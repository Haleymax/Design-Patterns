"""
定义媒体播放器的目标接口
这是客户端期望的统一接口
"""

from abc import ABC, abstractmethod

class MediaPlayer(ABC):

    @abstractmethod
    def play(self, audio_type: str, file_name: str) -> None:
        """
        播放媒体文件的抽象方法

        参数:
            audio_type (str): 媒体文件的类型（如 'mp3', 'mp4' 等）
            file_name (str): 媒体文件的名称

        返回:
            None
        """
        pass