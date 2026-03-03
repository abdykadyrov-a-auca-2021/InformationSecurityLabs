import requests

log_file = "log.txt"
SERVER_URL = "http://localhost:9000/logs"
all_logs = []

def send_to_server(logs):
    """Отправляет логи на сервер"""
    try:
        response = requests.post(SERVER_URL, json={"logs": logs})
        if response.status_code == 200:
            print("[SENT TO SERVER]")
        else:
            print("[FAILED TO SEND]")
    except Exception as e:
        print(f"[ERROR]: {e}")

print("=== Keylogger Demo ===")
print("Type text and press Enter. Type 'exit' to quit.\n")

with open(log_file, "w") as f:
    while True:
        try:
            text = input(">>> ")
            if text.lower() == "exit":
                # Отправляем все логи на сервер при выходе
                send_to_server("\n".join(all_logs))
                break
            f.write(text + "\n")
            f.flush()
            all_logs.append(text)
            print(f"[LOGGED]: {text}")
        except KeyboardInterrupt:
            send_to_server("\n".join(all_logs))
            break

print("Keylogger stopped. Logs sent to server!")
