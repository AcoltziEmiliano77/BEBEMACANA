class JuegoDelGato:
    def _init_(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"
        self.puntaje_x = 0
        self.puntaje_o = 0

    def mostrar_tablero(self):
        print("\n  0 1 2")
        for i, fila in enumerate(self.tablero):
            print(f"{i} {'|'.join(fila)}")
            if i < 2:
                print("  -----")

    def jugar_turno(self):
        while True:
            try:
                fila = int(input(f"Turno de {self.turno}. Ingresa la fila (0-2): "))
                col = int(input(f"Turno de {self.turno}. Ingresa la columna (0-2): "))
                if self.tablero[fila][col] == " ":
                    self.tablero[fila][col] = self.turno
                    break
                else:
                    print("Esa casilla ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Entrada inválida. Asegúrate de ingresar números del 0 al 2.")

    def verificar_ganador(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or \
               all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        if all(self.tablero[i][i] == jugador for i in range(3)) or \
           all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(self.tablero[fila][col] != " " for fila in range(3) for col in range(3))

    def reiniciar_juego(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def mostrar_puntajes(self):
        print(f"\nPuntaje - X: {self.puntaje_x}    O: {self.puntaje_o}")

    def jugar(self):
        while True:
            self.mostrar_tablero()
            self.jugar_turno()

            if self.verificar_ganador(self.turno):
                self.mostrar_tablero()
                print(f"\n¡{self.turno} ha ganado!")
                if self.turno == "X":
                    self.puntaje_x += 1
                else:
                    self.puntaje_o += 1
                self.mostrar_puntajes()
                if input("¿Quieres jugar otra vez? (s/n): ").lower() != "s":
                    break
                self.reiniciar_juego()
                continue

            if self.tablero_lleno():
                self.mostrar_tablero()
                print("\n¡Empate!")
                self.mostrar_puntajes()
                if input("¿Quieres jugar otra vez? (s/n): ").lower() != "s":
                    break
                self.reiniciar_juego()
                continue

            self.turno = "O" if self.turno == "X" else "X"

class Main:
    @staticmethod
    def ejecutar():
        print("¡Bienvenido al Juego del Gato (Tic Tac Toe)!")
        juego = JuegoDelGato()
        juego.jugar()
        print("\nGracias por jugar. ¡Hasta la próxima!")

if _name_ == "_main_":
    Main.ejecutar()
