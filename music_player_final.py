import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QListWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import Qt, QTimer, QModelIndex, QUrl
from PyQt5.QtGui import QFont

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: rgb(167, 145, 203)")

        self.media_player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.media_player.setPlaylist(self.playlist)

        self.play_button = QPushButton('Play')
        self.play_button.setFont(QFont('Montserrat', 9, QFont.Bold))
        self.pause_button = QPushButton('Pause')
        self.pause_button.setFont(QFont('Montserrat', 9, QFont.Bold))
        self.stop_button = QPushButton('Stop')
        self.stop_button.setFont(QFont('Montserrat', 9, QFont.Bold))
        self.seek_slider = QSlider(Qt.Horizontal)
        self.seek_slider.setRange(0, 0)

        self.duration_label = QLabel('00:00')
        self.current_time_label = QLabel('00:00')

        self.add_button = QPushButton('Add Song')
        self.add_button.setFont(QFont('Montserrat', 9, QFont.Bold))
        self.prev_button = QPushButton('Previous')
        self.prev_button.setFont(QFont('Montserrat', 9, QFont.Bold))
        self.next_button = QPushButton('Next')
        self.next_button.setFont(QFont('Montserrat', 9, QFont.Bold))

        self.songs_list = QListWidget()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.seek_slider)
        self.layout.addWidget(self.duration_label)
        self.layout.addWidget(self.current_time_label)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.prev_button)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.songs_list)

        self.setLayout(self.layout)

        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.add_button.clicked.connect(self.add_songs)
        self.playlist.currentMediaChanged.connect(self.update_song_title)
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)
        self.prev_button.clicked.connect(self.prev_song)
        self.next_button.clicked.connect(self.next_song)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.playlist.setCurrentIndex(0)

    def play(self):
        self.media_player.play()

    def pause(self):
        self.media_player.pause()

    def stop(self):
        self.media_player.stop()

    def add_songs(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav)")

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            for file_path in file_paths:
                file_url = QUrl.fromLocalFile(file_path)
                file_content = QMediaContent(file_url)
                self.playlist.addMedia(file_content)
                self.songs_list.addItem(file_path)

            self.media_player.setPlaylist(self.playlist)

    def update_song_title(self, media):
        if self.playlist.isEmpty():
            return
        index = self.playlist.currentIndex()
        entry = self.playlist.media(index)
        title = entry.canonicalUrl().fileName()
        items = self.songs_list.findItems(title, Qt.MatchExactly)
        if items:
            self.songs_list.setCurrentItem(items[0])

    def update_position(self, position):
        self.seek_slider.setValue(position)

    def update_duration(self, duration):
        self.seek_slider.setRange(0, duration)
        self.duration_label.setText(self.format_time(duration))

    def update_time(self):
        position = self.media_player.position()
        self.current_time_label.setText(self.format_time(position))

    def format_time(self, msec):
        h = msec // 3600000
        m = (msec % 3600000) // 60000
        s = (msec % 60000) / 1000
        return "%d:%02d:%02d" % (h, m, s)

    def prev_song(self):
        current_index = self.playlist.currentIndex()
        if current_index > 0:
            self.playlist.setCurrentIndex(current_index - 1)
        else:
            self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)

    def next_song(self):
        current_index = self.playlist.currentIndex()
        if current_index < (self.playlist.mediaCount() - 1):
            self.playlist.setCurrentIndex(current_index + 1)
        else:
            self.playlist.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())