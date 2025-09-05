import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()
request_id_counter = 0

def generate_request():
    global request_id_counter
    request_id_counter += 1
    request = f"Заявка №{request_id_counter}"
    request_queue.put(request)
    print(f"Згенеровано та додано до черги: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Оброблено заявку: {request}")
    else:
        print("Черга пуста, немає заявок для обробки.")

def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Генеруємо нові заявки
            generate_request()
            time.sleep(random.uniform(0.5, 1.5)) # Імітуємо випадковий інтервал генерації

            # Обробляємо заявки
            process_request()
            time.sleep(random.uniform(0.3, 1.0)) # Імітуємо випадковий інтервал обробки

    except KeyboardInterrupt:
        print("\nСистема обробки заявок зупинена.")

if __name__ == "__main__":
    main()
