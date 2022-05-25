'''
Project python 2022
Jef van der Avoirt - ITSOF1
'''


from app import VeloApp


def main():
    app = VeloApp()
    app.initialize()

    app.save_data()

if __name__ == "__main__":
    main()