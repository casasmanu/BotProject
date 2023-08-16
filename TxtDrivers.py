#file handler te edit .txt, load and save data

def TxtReader(path: str) -> str:
    """reads the txt indicated in the input path andgives back the data."""
    counter = 0
    with open(path) as f:
        for line in f:
            salida = f.read()

    return salida

    
def main() -> None:
    text=TxtReader("C:/Users/manum/Documents/Codigo VS/sssss.txt")
    print(text)


if __name__ == '__main__':
    main()
