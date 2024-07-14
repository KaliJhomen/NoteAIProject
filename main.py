from ui import create_ui
from database import crear_base_de_datos

def main():
    crear_base_de_datos()
    create_ui()

if __name__ == '__main__':
    main()
