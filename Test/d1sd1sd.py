from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def mask_image(imgdata, imgtype='jpg', size=85):
    image = QImage.fromData(imgdata, imgtype)

    image.convertToFormat(QImage.Format_ARGB32)

    imgsize = min(image.width(), image.height())
    rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
    )

    image = image.copy(rect)

    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    brush = QBrush(image)

    painter = QPainter(out_img)
    painter.setBrush(brush)

    painter.setPen(Qt.NoPen)

    painter.drawEllipse(0, 0, imgsize, imgsize)

    painter.end()

    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size *= pr
    pm = pm.scaled(size, size, Qt.KeepAspectRatio,
                   Qt.SmoothTransformation)

    return pm


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        imgpath = "../Images/Profile/nirs.jpg"
        imgdata = open(imgpath, 'rb').read()
        pixmap = mask_image(imgdata)
        self.ilabel = QLabel(self)
        self.ilabel.setPixmap(pixmap)
        self.ilabel.move(240, 180)
        self.tlabel = QLabel('This is circular image', self)
        self.tlabel.move(200, 250)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = Window()
    w.show()

    sys.exit(app.exec_())