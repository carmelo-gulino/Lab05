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
        self._view.cleanView()
        try:
            corso = self._model.cercaCorso(self._view.nome_corso.value)
            self._view.printIscritti(corso)
        except AttributeError:
            self._view.create_alert("Selezionare un corso!")
        self._view.cleanPage()

    def handle_cerca_stud(self, e):
        """
        compila automaticamente nome e cognome a partire dalla matricola
        :param e:
        :return:
        """
        self._view.cleanView()
        try:
            studente = self._model.cercaStudente(int(self._view.txt_matricola.value))
            self._view.compilaCampi(studente)
            self._view.update_page()
        except AttributeError:
            self._view.create_alert("Studente non presente!")
            self._view.cleanPage()
        except ValueError:
            self._view.create_alert("Selezionare una matricola!")
            self._view.cleanPage()

    def handle_cerca_corsi(self, e):
        """
        restituisce una lista dei corsi a cui è iscritto lo studente
        :param e:
        :return:
        """
        self._view.cleanView()
        try:
            studente = self._model.cercaStudente(int(self._view.txt_matricola.value))
            self._view.printCorsi(studente)
        except AttributeError:
            self._view.create_alert("Studente non presente!")
        except ValueError:
            self._view.create_alert("Selezionare una matricola!")
        self._view.cleanPage()

    def handle_iscrivi(self, e):
        """
        chiama i metodi per aggiungere un'istanza ad 'iscrizione' ed aggiungere
        il corso allo studente e lo studente al corso
        :param e:
        :return:
        """
        self._view.cleanView()
        try:
            studente = self._model.cercaStudente(int(self._view.txt_matricola.value))
            corso = self._model.cercaCorso(self._view.nome_corso.value)
            self._model.addIscrizione(studente, corso)
        except AttributeError:
            self._view.create_alert("Studente non presente!")
            return
        except ValueError:
            self._view.create_alert("Selezionare matricola e corso!")
            return
        except KeyError:
            self._view.create_alert("Studente già iscritto!")
        self._view.cleanPage()