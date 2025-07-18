"""
AVI播放器类
有不同于目标接口的方法
"""

class AviPlayer:
    
    def play_avi(self, file_name: str) -> None:
        """
        AVI播放器的专用播放方法

        参数:
            file_name: 媒体文件的名称
        """
        print(f"Playing AVI file: {file_name}")
