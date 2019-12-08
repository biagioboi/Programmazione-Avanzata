#Scrivere la funzione procTesto all’interno del file esercizio4.py.
# Se la funzione ha bisogno di invocare altre procedure, fornire anche quest’ultime.
# La funzione procTesto prende in input una lista di nomi di file, una lista di stringhe,
# e il parametro concorrenza. La funzione procTesto deve cecare nel testo dell’i-esimo file
# della prima lista l’i-esima stringa della seconda lista e deve fare cio` con un processo
# separato per ogni coppia file-stringa. Attenzione, il callable utilizzato da procTesto
# deve riceve in input il testo del file e non il file. La funzione procTesto deve inoltre
# stampare per ciascuna coppia file-stringa se la stringa e` presente o meno nel file.
# Le stampe devono avvenire nell’ordine in cui terminano i processi e al termine degli stessi.

import concurrent.futures
from functools import wraps
from datetime import datetime


#########################DECORATORI########################################

def time_of_exec(func): 
    """decoratore che pemette di misuare il tempo di esecuzione"""
    @wraps(func)
    def wrapper(*args,**kargs):
        start = datetime.now()
        result = func(*args,**kargs)
        finish = datetime.now()
        print(f'{func.__name__} finished in {finish-start} second(s)')
        return result
    return wrapper

def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper  
##############################################################################

def find(contex,to_find):
   return to_find in contex.split()
    
def get_jobs(source, target):
    for name,to_find in zip(source,target):
        yield open(name,"r").read(), to_find,name

def wait_futures(futures):
    results = []
    
    for future in concurrent.futures.as_completed(futures.keys()):
        if future.exception() is None:
            source,to_find = futures.get(future)
            if future.result():
                results.append(f"La stringa {to_find} e` presente nel file {source}")
            else:
                results.append(f"La stringa {to_find} non e' presente nel file {source}")
                

            
    return results

#scrivere qui la funzione
@time_of_exec
def procTesto(files,stringhe,concurrency):

    futures = dict()

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        for name,to_find,source in get_jobs(files,stringhe):
            future = executor.submit(find,name,to_find)
            futures[future] = source,to_find
            
    summary = wait_futures(futures)
    for result in summary:
        print(result)

@time_of_exec
def procTestoProcess(files,stringhe,concurrency):

    futures = dict()

    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
        for name,to_find,source in get_jobs(files,stringhe):
            future = executor.submit(find,name,to_find)
            futures[future] = source,to_find
            
    summary = wait_futures(futures)
    for result in summary:
        print(result)


@time_of_exec
def no_futures(files,stringhe):
     for name,to_find,source in get_jobs(files,stringhe):
         if(find(name,to_find)):
            print(f"La stringa {to_find} e` presente nel file {source}")
         else:
            print(f"La stringa {to_find} non e' presente nel file {source}")

@time_of_exec
def pipeline_processing(files,stringhe,concurrency):
    pipeline = create_pipeline(concurrency)
    i=0
    for data,to_find,source in get_jobs(files,stringhe):
        pipeline.send((data,to_find,source,i))
        i += 1

def create_pipeline(concurrency):
    pipeline = None
    sink = results()
    for who in range(concurrency):
        pipeline = find_coroutine(pipeline, sink,who) #pipeline avra' sempre il valore della coroutine della precedente iterazione, tranne la prima volta che vale none.
    return pipeline

@coroutine
def find_coroutine(recever,sink,me):
    while True:
        data,to_find,source,who = (yield)
        if who == me:
            result = find(data,to_find)
            sink.send((result,source,to_find))
        elif recever is not None:
            recever.send((data,to_find,source,who))
        
            
@coroutine
def results():
    while True:
        result,source,to_find = (yield)
        results.todo += 1
        if result is not None:
            results.ok += 1
            if(result):
                print(f"La stringa {to_find} e` presente nel file {source}")
            else:
                print(f"La stringa {to_find} non e' presente nel file {source}")

results.todo = results.ok = 0




    





  
def main():
   

    files=["file2","file5","file8","file2","file5","file8"]
    stringhe=["panca","Trento","entrarono","a","di","capra"]
            
    print("//*******THREAD POOL*********//")
    procTesto(files,stringhe,6)
    print("//*******NO FUTURES*********//")
    no_futures(files,stringhe)
    print("//*******PROCESS POOL*********//")
    procTestoProcess(files,stringhe,6)
    print("//********COUROUTINE*********//")
    pipeline_processing(files,stringhe,6)
    print("//********PROCESS WITH QUEUE *******//")

    
    


 

if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato:
La stringa panca e` presente nel file file2:
La stringa Trento e` presente nel file file5:
La stringa entrarono e` presente nel file file8:
La stringa a non e` presente nel file file2:
La stringa di non e` presente nel file file5:
La stringa capra non e` presente nel file file8:
"""