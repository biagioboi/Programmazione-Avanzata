# facendo uso di Futures e Multiprocessing e joinable queue
# crea un programma che prende in unput una lista L di stringhe ed un intero n e crea, in modo concorrente
# per ciascuna delle stringhe s in L una lista. La lista creata per la i-esima stringa di L dovrà contenere n//(10^i)
# occorenze della stringa. Le liste devono essere stampate non appena vengono create.
import concurrent.futures


def stampa(stringa, num_volte):
    x = list()
    for y in range (0, num_volte):
        x.append(stringa)
    return x


def scrivi_tutti(stringhe, n, concurrency = 0):
    futures = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
        for i, stringa in enumerate(stringhe):
            num_volte = n // 10**i
            exec = executor.submit(stampa, stringa, num_volte)
            futures.add(exec)
    process(futures)


def process(futures):
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)


def main():
    scrivi_tutti(["Maria", "Marco"], 10, 1)


if __name__ == "__main__":
    main()