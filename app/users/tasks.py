from celery import shared_task


@shared_task
def divide(x: int, y: int) -> float:
    import time
    time.sleep(5)
    return x / y


@shared_task
def divide_periodically(x: int, y: int) -> float:
    return x / y
