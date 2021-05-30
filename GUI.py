import sys
sys.setrecursionlimit(100000) #设置递归深度

from PySide2.QtWidgets import QApplication, QMessageBox,QPushButton,QFileDialog


from PySide2.QtUiTools import QUiLoader
from tools import del_file_list,run

app = QApplication([])
ui = QUiLoader().load('UI/PyQt.ui')


def click_select_json():
    global json_file
    options = QFileDialog.Options()
    json_file, _ = QFileDialog.getOpenFileName(None, options=options, )
    print(json_file)
def click_select_files():
    global files_path
    files_path = QFileDialog.getExistingDirectory()
    print(files_path)

def click_statistics_unused_files():
    global  json_file, files_path,file_not_in_Remnote
    file_not_in_Remnote = run()


def click_delete_unuseed_files():
    global  json_file, files_path,file_not_in_Remnote
    del_file_list(files_path, file_not_in_Remnote)

ui.select_json.clicked.connect(click_select_json)
ui.select_files.clicked.connect(click_select_files)
ui.statistics_unused_files.clicked.connect(click_statistics_unused_files)
ui.delete_unuseed_files.clicked.connect(click_delete_unuseed_files)
ui.show()
app.exec_()