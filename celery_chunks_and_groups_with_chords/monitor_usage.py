import inspect
import os

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("===================================MEMORY AND CPU USAGE BY CELERY CHUNKS===========================")
os.system('python -m memory_profiler %s/with_chunk.py' % current_dir)
os.system('kernprof -l -v %s/with_chunks_cpu.py' % current_dir)
print("===================================MEMORY AND CPU USAGE BY CELERY GROUPS===========================")
os.system('python -m memory_profiler %s/with_group.py' % current_dir)
os.system('kernprof -l -v %s/with_group_cpu.py' % current_dir)
