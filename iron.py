class Iron():
    def __init__(self, fileName, websiteName) -> None:
        self.iron = open(f"{fileName}","w")
        self.vars = {}
    def inject(self, htmlCode, params):
        rep = htmlCode
        for param in params:
            try:
                rep = rep.replace(f"|%{param}%|", str(self.vars[param]))
            except:
                raise ReferenceError(f"Undefined Variable: {param}")
        self.iron.write(rep)
        self.iron.close()