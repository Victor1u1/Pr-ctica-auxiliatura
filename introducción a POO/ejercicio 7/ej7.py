class Celular:
    def __init__(self):
        self.apps = []
        
    def instalar(self, nombre, tamaño):
        if len(self.apps) < 20 and sum(a[1] for a in self.apps) + tamaño <= 1024:
            self.apps.append((nombre, tamaño))

    def usar(self, nombre, minutos):
        for app, tamaño in self.apps:
            if app == nombre:
                if tamaño > 250:
                    return 5 * (minutos // 10)
                elif tamaño > 100:
                    return 2 * (minutos // 10)
                return minutos // 10
        return 0  

    def __str__(self):
        return f"Aplicaciones: {', '.join(a[0] for a in self.apps)}"
        
celular = Celular()
celular.instalar("Facebook", 150)
celular.instalar("X", 100)
celular.instalar("WhatsApp", 50)

for app in celular.apps:
    print(f"{app[0]} usó {celular.usar(app[0], 30)}% de batería.")
