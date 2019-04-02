for i in range(5):  # Vnější cyklus
    for j in range(50):  # Vnitřní cyklus
        print(j * i, end=' ')
        if i <= j:
            break
    print()