
# la classe Archive sarà il nostro Facade, che unificherà le operazioni che si effettuano sugli archivi, indipendentemente
# dal tipo di archivio che vogliamo usare
import gzip
import os
import string
import zipfile
import tarfile
import re


class Archive:

    # _names viene usata per conservare un callable che restituisce una lista di nomi nell'archivio
    # _unpack viene usata per conservare un callable che estrae tutti i file dell'archivio nella dir corrente
    # _file viene usata per conservare il file object del file aperto
    # filename è una property che mantiene il nome del file di archivio, questo per chiudere il file, prima che perdiamo il riferimento ad esso
    def __init__(self, filename):
        self._names = None
        self._unpack = None
        self._file = None
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.close()
        self.__filename = value
        # notiamo che il file non viene immediatamente aperto, ma verrà aperto solo quando necessario

    # queto metodo verrà invocato quando abbiamo finito di lavorare con un'istanza e liberiamo l'accesso al file
    # controlliamo prima che il file realmente è stato aperto (esiste un file object) e poi lo chiudiamo; quindi cancelliamo tutti i riferimenti
    def close(self):
        if self._file is not None:
            self._file.close()
        self._names = self._unpack = self._file = None

    # i metodi enter e close ci permetteranno di usare Archive come un context manager, quindi con With .. as ; così che gli utenti non dovranno preoccuparsi
    # di aprire o chiudere il file
    # in particolare il metodo enter ci restituisce un'istanza di Archive che viene assegnata alla variabile as
    # il metodo exit invece viene invocato quando usciamo dal bloccco With .. as (è terminata la lettura)
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # metodo per verificare se l'estensione del file è giusta e quindi smistare a seconda del tipo di archivio a due metodi di preparazione diversi
    def _prepare(self):
        if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
            self._prepare_tarball_or_zip()
        elif self.filename.endswith(".gz"):
            self._prepare()._gzip()
        else:
            raise ValueError("File non estraibile: {}".format(self.filename))


    # metodo per la preparazione di archivi di tipo tar o zip, con controllo su ogni file presente nell'archivio, se è sicuro o meno
    def _prepare_tarball_or_zip(self):
        def safe_extractall():
            unsafe = []
            for name in self.names():
                if not self.is_safe(name):
                    unsafe.append(name)
            if unsafe:
                raise ValueError("unsafe to unpack: {}".format(unsafe))
            self._file.extractall()
        if self.filename.endswith(".zip"):
            self._file = zipfile.ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = safe_extractall
        else: # Ends with .tar.gz, .tar.bz2, or .tar.xz
            suffix = os.path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, "r:" + suffix[1:])
            self._names = self._file.getnames
            self._unpack = safe_extractall

    # metodo per la preparazione di archivi di tipo gz, con controllo su ogni file presente nell'archivio se è sicuro o meno
    def _prepare_gzip(self):
        self._file = gzip.open(self.filename)
        filename = self.filename[:-3]
        self._names = lambda: [filename]
        def extractall():
            with open(filename, "wb") as file:
                file.write(self._file.read())
        self._unpack = extractall


    def is_safe(self, filename):
        return not (filename.startswith(("/", "\\")) or
            (len(filename) > 1 and filename[1] == ":" and
             filename[0] in string.ascii_letter) or
            re.search(r"[.][.][/\\]", filename))

    def names(self):
        if self._file is None:
            self._prepare()
        return self._names()


    def unpack(self):
        if self._file is None:
            self._prepare()
        self._unpack()
