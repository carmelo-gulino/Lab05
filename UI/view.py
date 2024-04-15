import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.nome_corso = None
        self.btn_cerca_iscr = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_stud = None
        self.btn_cerca_corsi = None
        self.btn_cerca_iscrivi = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)
        #ROW 1
        # nome del corso
        self.nome_corso = ft.Dropdown(
            label="corso",
            width=500,
            hint_text="Selezionare un corso"
        )
        self.fillCorso()    #METODO CHE CARICA TUTTI I CORSI

        # button for the "cerca" reply
        self.btn_cerca_iscr = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_cerca_iscr)
        row1 = ft.Row([self.nome_corso, self.btn_cerca_iscr], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW 2
        self.txt_matricola = ft.TextField(
            width=166,
            hint_text="matricola"
        )
        self.txt_nome = ft.TextField(
            width=166,
            hint_text="nome",
            read_only=True
        )
        self.txt_cognome = ft.TextField(
            width=166,
            hint_text="cognome",
            read_only=True
        )
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW 3
        self.btn_cerca_stud = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cerca_stud)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cerca_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        row3 = ft.Row([self.btn_cerca_stud, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fillCorso(self):
        """
        accedo al database e popolo il menu con tutti i corsi disponibili
        """
        corsi = self._controller.handle_fill()
        for c in corsi:
            self.nome_corso.options.append(ft.dropdown.Option(key=c.codins, text=c))
        return self.nome_corso

    def cleanPage(self):
        """
        pulisce i campi della pagina
        :return:
        """
        self.nome_corso.value = None
        self.txt_matricola.value = None
        self.txt_nome.value = None
        self.txt_cognome.value = None
        self.update_page()

    def compilaCampi(self, studente):
        self.txt_nome.value = f"{studente.nome}"
        self.txt_cognome.value = f"{studente.cognome}"

    def printIscritti(self, corso):
        self.txt_result.controls.append(ft.Text(f"Ci sono {len(corso.studenti)} iscritti:"))
        for s in corso.studenti:
            self.txt_result.controls.append(ft.Text(s))
        self.update_page()

    def printCorsi(self, studente):
        self.txt_result.controls.append(ft.Text(f"Risultano {len(studente.iscrizioni)} corsi:"))
        for c in studente.iscrizioni:
            self.txt_result.controls.append(ft.Text(c))
        self.update_page()

    def cleanView(self):
        self.txt_result.controls = None