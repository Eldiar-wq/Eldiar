soma = float(input("Бастапқы салымды енгізіңіз: "))
years = int(input("Жыл санын енгізіңіз: "))
percent = float(input("Жылдық пайыздық мөлшерлеме (%): "))

for year in range(1, years + 1):
    soma += soma * (percent / 100)
    print(f"{year}-жылдағы депозит сомасы: {soma:.2f} теңге")
