import math

class LaboratorioQuimico:
    def __init__(self):
        self.elementos = {
            "H":  {"n": "Hidrógeno", "en": 2.2,  "v": 1,  "t": "no metal"},
            "Li": {"n": "Litio",     "en": 0.98, "v": 1,  "t": "metal"},
            "Na": {"n": "Sodio",     "en": 0.93, "v": 1,  "t": "metal"},
            "K":  {"n": "Potasio",   "en": 0.82, "v": 1,  "t": "metal"},
            "Mg": {"n": "Magnesio",  "en": 1.31, "v": 2,  "t": "metal"},
            "Ca": {"n": "Calcio",    "en": 1.0,  "v": 2,  "t": "metal"},
            "Al": {"n": "Aluminio",  "en": 1.61, "v": 3,  "t": "metal"},
            "F":  {"n": "Flúor",     "en": 3.98, "v": -1, "t": "no metal"},
            "Cl": {"n": "Cloro",     "en": 3.16, "v": -1, "t": "no metal"},
            "O":  {"n": "Oxígeno",   "en": 3.44, "v": -2, "t": "no metal"},
            "S":  {"n": "Azufre",    "en": 2.58, "v": -2, "t": "no metal"},
        }

        self.nombres_aniones = {"F": "Fluoruro", "Cl": "Cloruro", "O": "Óxido", "S": "Sulfuro", "H": "Hidruro"}

    def mostrar_opciones(self, simbolo_base):
        el = self.elementos[simbolo_base]
        print(f"\nAnalizando {el['n']} (EN: {el['en']})...")
        print("Elementos con los que PUEDE reaccionar:")
        
        for s, datos in self.elementos.items():

            if el['t'] == 'metal' and datos['t'] == 'no metal':
                print(f" -> {s} ({datos['n']})")
            elif el['t'] == 'no metal' and s != simbolo_base:
                print(f" -> {s} ({datos['n']})")

    def combinar(self, s1, s2):
        e1, e2 = self.elementos[s1], self.elementos[s2]
        

        if e1['t'] == 'metal' and e2['t'] == 'metal':
            return None, "ERROR: No es posible. Dos metales no suelen formar compuestos iónicos."


        if e1['en'] < e2['en']:
            izq, der = s1, s2
        else:
            izq, der = s2, s1
            
        v_izq, v_der = abs(self.elementos[izq]['v']), abs(self.elementos[der]['v'])
        

        mcd = math.gcd(v_izq, v_der)
        sub_izq, sub_der = v_der // mcd, v_izq // mcd
        
        formula = f"{izq}{sub_izq if sub_izq > 1 else ''}{der}{sub_der if sub_der > 1 else ''}"
        nombre = f"{self.nombres_aniones.get(der, der)} de {self.elementos[izq]['n']}"
        
        explicacion = (f"Se necesitan {sub_izq} átomos de {izq} (carga +{v_izq}) y "
                      f"{sub_der} átomos de {der} (carga -{v_der}) "
                      f"para que la carga total sea 0.")
        
        return formula, nombre, explicacion

    def iniciar(self):
        print("--- SISTEMA DE COMBINACIÓN QUÍMICA ---")
        print("Disponibles:", ", ".join(self.elementos.keys()))
        sel = input("¿Qué elemento quieres elegir?: ").capitalize()
        
        if sel in self.elementos:
            self.mostrar_opciones(sel)
            reacciona = input("\n¿Con cuál quieres que reaccione?: ").capitalize()
            
            if reacciona in self.elementos:
                form, nom, expl = self.combinar(sel, reacciona)
                if form:
                    print(f"\n✅ COMBINACIÓN CORRECTA")
                    print(f"Nombre: {nom}")
                    print(f"Fórmula: {form}")
                    print(f"Proceso: {expl}")
                else:
                    print(f"\n❌ {nom}")
            else: print("Ese elemento no está en la base de datos.")
        else: print("Elemento no reconocido.")

# Ejecución
lab = LaboratorioQuimico()
lab.iniciar()