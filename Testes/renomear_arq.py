import os

def main():
    i = 0
    path = "C:/Users/546692668/Downloads/Teste/"
    for newname in os.listdir(path):
        destino = "Teste" + str(i) + ".txt"
        source =path + newname
        dest =path + destino
        os.rename(source, dest)
        i += 1

if __name__ == "__main__":
    main()