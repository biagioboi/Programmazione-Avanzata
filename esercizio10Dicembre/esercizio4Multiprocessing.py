# facendo uso di Futures e Multiprocessing e joinable queue
# crea un programma che prende in unput una lista L di stringhe ed un intero n e crea, in modo concorrente
# per ciascuna delle stringhe s in L una lista. La lista creata per la i-esima stringa di L dovrà contenere n//(10^i)
# occorenze della stringa. Le liste devono essere stampate non appena vengono create.
import multiprocessing


def stampa(stringa, num_volte):
    x = list()
    for y in range (0, num_volte):
        x.append(stringa)
    return x

def add_jobs(strs, n, jobs):
    d = n
    for s in strs:
        jobs.put((s, d))
        d = d // 10

def scrivi_tutti(strs, n, concurrency = 0):
    jobs = multiprocessing.JoinableQueue()
    create_processes(jobs, concurrency)
    add_jobs(strs, n, jobs)
    jobs.join()

def worker(jobs):
    while True:
        s, m = jobs.get()
        print("Questa è la lista prodotta per {}: {}".format(s, stampa(s, m)))
        jobs.task_done()

def create_processes(jobs, concurrency):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args = (jobs,))
        process.daemon = True
        process.start()


def main():
    scrivi_tutti(["Maria", "Marco"], 10, 1)


if __name__ == "__main__":
    main()