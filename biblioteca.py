from csv import *
def carica_da_file(file_path):
    try:
        with open (file_path, "r") as file:
            file.readline()
            biblioteca=list(DictReader(file, fieldnames=['Titolo', 'Autore', 'Anno', 'Pagine', 'Sezione']))
            for el in biblioteca:
                el['Anno']=int(el['Anno'])
                el['Pagine'] = int(el['Pagine'])
                el['Sezione'] = int(el['Sezione'])
    except FileNotFoundError:
        return None
    return biblioteca
    """Carica i libri dal file"""


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    nsezioni=1
    for el in biblioteca:
        if el['Titolo']==titolo:
            libro=None
            return libro
        nsezioni=max(nsezioni, el['Sezione'])
    if sezione not in range(nsezioni):
        libro=None
        return libro
    try:
        with open(file_path, "a") as file:
            libro=[titolo, autore, anno, pagine, sezione]
            csvWriter = writer(file, delimiter=',')
            csvWriter.writerow(libro)
        biblioteca.append({
            'Titolo': titolo, 'Autore': autore, 'Anno': anno, 'Pagine': pagine, 'Sezione': sezione
        })
        return libro
    except FileNotFoundError:
        libro=None
        return libro
    """Aggiunge un libro nella biblioteca"""


def cerca_libro(biblioteca, titolo):
    for el in biblioteca:
        if el['Titolo'] == titolo:
            risultato=(f"{el['Titolo']}, {el['Autore']}, {el['Anno']}, {el['Pagine']}, {el['Sezione']}")
    return risultato
    """Cerca un libro nella biblioteca dato il titolo"""


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    libri=[]
    for el in biblioteca:
        if el['Sezione'] == sezione:
            libri.append(el)


    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

