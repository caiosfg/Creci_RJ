import unicodedata
#transformar de Unicode para UTF-8

    def load_mockup(mockup_name="utf-8"):
    #  abre ao passar o nome do arquivo html, abrindo e fechando automatico
        with open(f"tests/mockup/{mockup_name}", encoding=encoding, mode="r") as f:
            return f.read()

    def normalize_text(text: str) -> str:
        # texto escrito em Unicode ignorado, parserado para utf8
        return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf8")