import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QTextEdit, QHBoxLayout, QFileDialog, QMessageBox


class InfoFileCreator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(700, 400)
        self.setWindowTitle('Info File Creator')

        self.labels = []
        self.fields = []

        self.setup_form()

        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.save_file)

        cancel_all_button = QPushButton('Cancel All', self)
        cancel_all_button.clicked.connect(self.cancel_all_inputs)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)

        layout = QVBoxLayout(self)
        for label, field in zip(self.labels, self.fields):
            entry_layout = QHBoxLayout()
            entry_layout.addWidget(label)
            entry_layout.addWidget(field)
            layout.addLayout(entry_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_all_button)
        button_layout.addWidget(exit_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def setup_form(self):
        field_names = [
            'Video or Playlist Name',
            'Link to Video or Playlist',
            'Link to YouTube Channel',
            'Name of YouTube Channel',
            'Project Directory',
            'Name of the Database',
            'Link to GitHub',
            'Source code',
        ]

        for field_name in field_names:
            label = QLabel(field_name, self)
            field = QLineEdit(self)

            self.labels.append(label)
            self.fields.append(field)

    def save_file(self):
        video_name = self.fields[0].text() or 'None'
        video_link = self.fields[1].text() or 'None'
        youtube_channel_link = self.fields[2].text() or 'None'
        youtube_channel_name = self.fields[3].text() or 'None'
        project_directory = self.fields[4].text() or 'None'
        database_name = self.fields[5].text() or 'None'
        github_link = self.fields[6].text() or 'None'
        source_code = self.fields[7].text() or 'None'

        default_file_name = video_name.replace(' ', '_')  # Use the video name as the default file name

        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", default_file_name, "Text Files (*.txt);;All Files (*)")

        if file_name:
            with open(file_name, 'w') as file:
                content = f"[{video_name}]({video_link})\n\n"
                content += f"[YouTube - {youtube_channel_name}]({youtube_channel_link})\n\n"
                content += f"PROJECT FOLDER: {project_directory}\n\n"
                content += f"DATABASE: {database_name}\n\n"
                content += f"GITHUB: {github_link}\n\n"
                content += f"SOURCE CODE: {source_code}\n\n"
                file.write(content)

            self.show_success_message(file_name, content)

    def cancel_all_inputs(self):
        for field in self.fields:
            field.clear()

    def show_success_message(self, file_name, content):
        success_message = f"File saved successfully!\n\nFile Name: {file_name}\n\nContent:\n{content}"

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setText(success_message)
        msg_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InfoFileCreator()
    window.show()
    sys.exit(app.exec())
