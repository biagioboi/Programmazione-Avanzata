from concurrent import futures


def find_all(file, parola):
    cont = 0
    with open(file) as fp:
        lines = fp.read().replace("\n", " ").split(" ")
        for z in lines:
            if z == parola:
                cont+=1
    return "Nel file " + file + " sono stati trovate " + str(cont) + " occorrenze"


def conta(parola, lista_file, concorrenza):
    fut = set()
    with futures.ThreadPoolExecutor(max_workers=concorrenza) as executor:
        for x in lista_file:
            work = executor.submit(find_all, x, parola)
            fut.add(work)
    result = wait_for_futures(fut)
    for x in result:
        print(x)


def wait_for_futures(fut):
    res = list()
    for futur in futures.as_completed(fut):
        res.append(futur.result())
    return res


if __name__ == "__main__":
    conta("Biagio", ["file2", "file5", "file8"], 10)