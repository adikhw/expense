from cli import main_menu

def main():
    try:
        main_menu()

    except (KeyboardInterrupt, EOFError):
        print()
        print("Program interrupted. Goodbye!")

    except Exception as error:
        print()
        print("Unexpected error:", error)

if __name__ == "__main__":
    main()