opcion = input("Escribe el nombre de un artista, película o serie: ").lower()

match opcion:
    case "breaking bad":
        print("Serie")
        print("2008")
        print(" Vince Gilligan")
        print("Drama y crimen")
        print("Historia: Un profesor de química se convierte en fabricante de metanfetamina.")

    case "jurassic park":
        print(" Película")
        print(" 1993")
        print(" Steven Spielberg")
        print(" Ciencia ficción y aventura")
        print(" Un parque de dinosaurios clonados provoca un desastre.")

    case "resident evil":
        print(" Videojuego/Película")
        print("1996 (videojuego) / 2002 (película)")
        print(" Capcom")
        print("Terror y acción")
        print("Una organización lucha contra experimentos biológicos peligrosos.")

    case "hollow knight":
        print("Videojuego")
        print(" 2017")
        print(" Team Cherry")
        print(" Metroidvania, acción y aventura")
        print(" Un caballero explora un antiguo reino subterráneo llamado Hallownest mientras descubre sus secretos y enfrenta enemigos peligrosos.")

    case "fifa":
        print("Videojuego deportivo")
        print(" 1993")
        print(" EA Sports")
        print(" Fútbol")
        print(" Es una de las sagas de videojuegos de fútbol más populares.")

    case _:
        print("solo hay cinco regresate wey")