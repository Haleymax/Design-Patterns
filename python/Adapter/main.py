"""
适配器模式演示的主程序
"""
from Adapter.audio_player import AudioPlayer


def main():
    print("适配器模式演示")
    print("------------")

    player = AudioPlayer()

    # 测试不同格式的播放
    player.play("mp4", "song.mp4")      # 直接使用MP4Player
    player.play("vlc", "movie.vlc")     # 通过适配器使用VLCPlayer
    player.play("avi", "video.avi")     # 通过适配器使用AviPlayer
    player.play("mp3", "music.mp3")     # 不支持的格式

if __name__ == "__main__":
    main()