"""
This module runs a celery task Synchronously(Just to monitor memory/CPU usage,
although we can run it Asynchronously). This module divides the list of input parameters
into chunks and run task for each chunk repeatedly without building a separate task for each integer
in Message Queue instead it builds task for each chunk in Message Queue(Redis Queue).
"""
# App Specific Imports
from celery_chunks_and_groups_with_chords.constants import TOTAL_TASKS, CHUNK_SIZE
from celery_chunks_and_groups_with_chords.tasks import group_task, callback
# 3rd Party Imports
from memory_profiler import profile as mp
from celery import chord


@mp  # Decorator for memory_profiler
# @profile  # Decorator for line_profiler (CPU Usage)
def run():
    """
    This module runs a group of Celery tasks for chunks of input parameters
    """
    """
    Celery.task.chunks function makes chunks of input parameters.
    Here I am making chunks of 45000 integers,
    each chunk would contain 1000 integers (a chunk is an array)
    """
    # for tasks in xrange(1, TOTAL_TASKS, 1000):
    chunk = group_task.chunks(zip(range(TOTAL_TASKS)), CHUNK_SIZE)
    # Using Celery chord to receive a callback with results, when all tasks has finished
    # Converting chunk to groups because chord doesn't seem to work ideally with chunk.
    chord(chunk.group())(callback.s())
    # Running task
    # celery_chord.get()


if __name__ == '__main__':
    run()
