import psutil

def get_process_data():
    processes = []
    cpu_count = psutil.cpu_count()

    for proc in psutil.process_iter():
        try:
            with proc.oneshot():
                processes.append({
                    "pid": proc.pid,
                    "name": proc.name(),
                    # We get the 'total' percentage used by the process, 
                    # divide by the number of cores to scale it to 100%, 
                    # and then round it so it looks neat.
                    "cpu_percent": round(proc.cpu_percent() / cpu_count, 2),
                    "memory_percent": round(proc.memory_percent(), 2)
                })
        except:
            continue

    return processes