# Piazzale Project

Il progetto "Piazzale" è un'applicazione distribuita in Python che implementa un sistema di gestione di un magazzino. Utilizza la libreria Pyro per la comunicazione tra client e server e sfrutta il concetto di oggetti distribuiti per la memorizzazione dei materiali e la gestione degli utenti abilitati.

## Descrizione

L'applicazione consente agli utenti di accedere al magazzino tramite un'interfaccia client-server. Gli utenti abilitati possono inserire nuovi materiali nel magazzino, fornendo il nome del materiale, il nome del responsabile e la data di inserimento. Il sistema tiene traccia di queste informazioni utilizzando oggetti distribuiti Pyro.

Il progetto comprende i seguenti file:

- `client.py`: Contiene l'inizializzazione dei proxy Pyro per il piazzale e il logger degli utenti, nonché il menu per l'interazione con il magazzino e il login per gli utenti.
- `person.py`: Definisce la classe `Person` e i relativi metodi che rappresentano le azioni che gli utenti possono eseguire sul magazzino. Questi metodi accedono ai metodi del piazzale attraverso i proxy Pyro.
- `material.py`: Definisce la classe `Material` e i relativi metodi per la gestione dei materiali.
- `server_piazzale.py`: Contiene l'inizializzazione del piazzale con alcuni oggetti di esempio e i metodi per interagire con essi. Questi metodi sono spesso chiamati dai metodi della classe `Person`.
- `server_logger.py`: Contiene il codice del proxy Pyro per il logger degli utenti e la funzione per il controllo delle credenziali degli utenti.

## Requisiti

Per eseguire correttamente il progetto, è necessario avere installato:

- Python 3.x
- La libreria Pyro5

## Istruzioni per l'esecuzione

1. Assicurarsi di avere Python 3.x installato nel sistema.
2. Installare le librerie utilizzando il comando `pip3 install –r requirements.txt`.
3. Avviare il name server Pyro utilizzando il comando `python3 -m Pyro5.nameserver`.
4. Eseguire il file `server_piazzale.py` per avviare il server del piazzale utilizzando il comando `python3 src/server/server_piazzale.py`.
5. Eseguire il file `server_logger.py` per avviare il server del logger degli utenti utilizzando il comando `python3 src/server/server_logger.py`.
6. Infine, eseguire il file `client.py` per avviare l'interfaccia client e iniziare a interagire con il magazzino utilizzando il comando `python src/client.py`.

## Contributi

Sono benvenuti contributi e miglioramenti a questo progetto. Se desideri contribuire, apri una pull request e descrivi le modifiche proposte.

## Licenza

Questo progetto è concesso in licenza con i termini della licenza [MIT](https://opensource.org/licenses/MIT).

