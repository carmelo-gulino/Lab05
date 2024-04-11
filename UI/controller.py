import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_fill(self):
        """
        prende i corsi dal modello
        :return:
        """
        return self._model.corsi

    def handle_cerca_iscr(self, e):
        """
        cerca tutti gli iscritti del corso
        :param e:
        :return: lista di studenti
        """
        try:
            corso = self._model.cercaCorso(self._view.nome_corso.value)
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(corso.studenti)} iscritti:"))
            for s in corso.studenti:
                self._view.txt_result.controls.append(ft.Text(s))
            self._view.update_page()
            #self._view.cleanPage()
        except AttributeError:
            self._view.create_alert("Selezionare un corso!")

    def handle_cerca_stud(self, e):
        """
        compila automaticamente nome e cognome a partire dalla matricola
        :param e:
        :return:
        """
        try:
            studente = self._model.cercaStudente(int(self._view.txt_matricola.value))
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"
            self._view.update_page()
            #self._view.cleanPage()
        except AttributeError:
            if self._view.txt_matricola.value=="":
                self._view.create_alert("Selezionare una matricola!")
            else:
                self._view.create_alert("Studente non presente!")

    #TODO
    #metodo che pulisce la pagina dopo ogni azione

