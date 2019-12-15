import multiprocessing
import time

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
    result = multiprocessing.Queue()
    create_processes(jobs, result, concurrency)
    add_jobs(strs, n, jobs)
    jobs.join()
    while not result.empty():
        print(result.get_nowait())

def worker(jobs, result):
    while True:
        s, m = jobs.get()
        print("Questa è la lista prodotta per {}: {}".format(s, stampa(s, m)))
        result.put(stampa(s, m))
        jobs.task_done()

def create_processes(jobs, result, concurrency):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args = (jobs,result,))
        process.daemon = True
        process.start()


def main():
    scrivi_tutti(["Maria", "Marco"], 10, 1)


if __name__ == "__main__":
    main()