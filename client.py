import json
from socket import *
from constCS import *

# Cria a requisição em lote (Batch Request) chamando múltiplas funcionalidades
batch_request = {
    "batch": [
        {
            "operation": "analyze_text",
            "payload": "Sistemas distribuidos exigem arquiteturas bem definidas."
        },
        {
            "operation": "calculate_stats",
            "payload": [12.5, 45.2, 8.0, 99.9, 21.4]
        },
        {
            "operation": "generate_fibonacci",
            "payload": 10
        }
    ]
}

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Enviando requisição em lote para o servidor...")

# Serializa o dicionário Python para uma string JSON e envia
payload_bytes = str.encode(json.dumps(batch_request))
s.send(payload_bytes)

# Recebe a resposta
data = s.recv(4096)

# Desserializa a resposta JSON de volta para dicionário Python
response_dto = json.loads(bytes.decode(data))

print("\n--- Resultados do Processamento ---")
for res in response_dto.get("results", []):
    print(f"\nOperação: {res['operation']} | Status: {res['status']}")
    print(f"Resultado: {json.dumps(res.get('result'), indent=2)}")

s.close()
