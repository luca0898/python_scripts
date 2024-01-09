import requests

def log_github_status():
    response = requests.get("https://api.github.com/status")

    if response.status_code == 200:
        dados = response.json()

        message = dados.get('message', 'N/A')

        with open('status_github.txt', 'w') as arquivo:
            arquivo.write(f"Status: {message}")

        print("Consulta concluída. As informações foram salvas em 'status_github.txt'.")
    else:
        print(f"Falha na solicitação. Código de status: {response.status_code}")

if __name__ == "__main__":
    log_github_status()
