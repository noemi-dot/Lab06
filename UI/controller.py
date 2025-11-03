import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    def mostra_auto(self, e):
        print("pulsante cliccato")
        try:
            automobili = self._model.get_automobili()
            print("automobili lette")
            self._view.lista_auto.controls.clear()
            for auto in automobili:
                self._view.lista_auto.controls.append(ft.Text(str(auto)))
            self._view.update()
        except Exception as err:
            self._view.alert.show_alert(f"Errore nel caricamento automobili: {err}")

    def cerca_auto(self, e):
        modello = self._view.input_modello_auto.value.strip()
        if modello == "":
            self._view.show_alert("Inserisci un modello da cercare.")
            return

        automobili = self._model.cerca_automobili_per_modello(modello)
        if not automobili:
            self._view.show_alert("Nessuna automobile trovata con quel modello.")
            return
        # Svuota la lista di ricerca
        self._view.lista_auto_ricerca.controls.clear()

        for auto in automobili:
            riga = ft.Text(f"{auto.id} - {auto.marca} {auto.modello} ({auto.targa}) - {auto.anno} - {auto.prezzo}€/giorno")
            self._view.lista_auto_ricerca.controls.append(riga)

        self._view.update()




