from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import variaveisControle
from popuperror import Ui_popup_aviso

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_exclusao_produto(object):
    def setupUi(self, exclusao_produto):
        exclusao_produto.setObjectName("exclusao_produto")
        exclusao_produto.resize(400, 203)

        self.search_product = QtWidgets.QLabel(exclusao_produto)
        self.search_product.setGeometry(QtCore.QRect(60, 40, 91, 20))
        self.search_product.setObjectName("search_product")

        self.search_product_line = QtWidgets.QLineEdit(exclusao_produto)
        self.search_product_line.setGeometry(QtCore.QRect(150, 40, 151, 20))
        self.search_product_line.setObjectName("search_client")

        self.excluirCatalogo_button = QtWidgets.QPushButton(exclusao_produto)
        self.excluirCatalogo_button.setGeometry(QtCore.QRect(230, 90, 101, 71))
        self.excluirCatalogo_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirCatalogo_button.setIcon(icon1)
        self.excluirCatalogo_button.setObjectName("excluirCatalogo_button")

        self.cancelar_button = QtWidgets.QPushButton(exclusao_produto)
        self.cancelar_button.setGeometry(QtCore.QRect(110, 90, 101, 71))
        self.cancelar_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.cancelar_button.setIcon(icon1)
        self.cancelar_button.setObjectName("cancelar_button")

        self.retranslateUi(exclusao_produto)
        QtCore.QMetaObject.connectSlotsByName(exclusao_produto)

    def retranslateUi(self, exclusao_produto):
        _translate = QtCore.QCoreApplication.translate
        exclusao_produto.setWindowTitle(_translate("exclusao_produto", "Form"))
        self.search_product.setText(_translate("exclusao_produto", "Nome do Produto:"))
        self.excluirCatalogo_button.setText(_translate("exclusao_produto", "Excluir do Catalogo"))
        self.cancelar_button.setText(_translate("exclusao_produto", "Cancelar"))

        ##Botão de para excluir##
        self.excluirCatalogo_button.clicked.connect(self.Excluir)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(exclusao_produto))

    def Excluir(self):
        nome = self.search_product_line.text()
        connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT DELET_PRODUCT('"+ nome + "');"
        print(consultaSql)
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except Exception as Error:
            print (Error)
            self.abrirPopUp()        
        self.search_product_line.setText("")
        mycursor.close()

    #saindo da tela
    def sairTela(self, exclusao_produto):
        exclusao_produto.close()
    def abrirPopUp(self):
        self.popup_aviso = QtWidgets.QWidget()
        self.ui = Ui_popup_aviso()
        self.ui.setupUi(self.popup_aviso)
        self.popup_aviso.show()       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exclusao_produto = QtWidgets.QWidget()
    ui = Ui_exclusao_produto()
    ui.setupUi(exclusao_produto)
    exclusao_produto.show()
    sys.exit(app.exec_())
