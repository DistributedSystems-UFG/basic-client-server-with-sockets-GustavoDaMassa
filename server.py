
import json
from socket import *
from constCS import *



def analyze_text(payload):
    """Analisa uma string e extrai métricas estruturadas."""
    text = str(payload)
    vowels = "aeiouAEIOU"
    return {
        "word_count": len(text.split()),
        "char_count": len(text),
        "vowel_count": sum(1 for char in text if char in vowels)
    }

def calculate_stats(payload):
    """Calcula estatísticas sobre uma lista de números."""
    if not isinstance(payload, list) or len(payload) == 0:
        return {"error": "Payload deve ser uma lista não vazia de números."}
    
    numbers = sorted(payload)
    n = len(numbers)
    mean = sum(numbers) / n
    median = numbers[n//2] if n % 2 != 0 else (numbers[n//2 - 1] + numbers[n//2]) / 2
    
    return {
        "mean": mean,
        "median": median,
        "max": numbers[-1],
        "min": numbers[0]
    }

def generate_fibonacci(payload):
    """Gera sequência de Fibonacci até a n-ésima posição."""
    try:
        n = int(payload)
        if n <= 0: return []
        if n == 1: return [0]
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib
    except ValueError:
        return {"error": "Payload deve ser um inteiro válido."}


OPERATIONS = {
    "analyze_text": analyze_text,
    "calculate_stats": calculate_stats,
    "generate_fibonacci": generate_fibonacci
}

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print(f"Servidor de Processamento em Lote rodando em {HOST}:{PORT}...")

while True:
    conn, addr = s.accept()
    print(f"Conectado a {addr}")
    
    while True:
        data = conn.recv(4096)
        if not data: 
            break
            
        try:
          e
            request_dto = json.loads(data.decode('utf-8'))
            responses = []
            
            
            for req in request_dto.get("batch", []):
                op_name = req.get("operation")
                payload = req.get("payload")
                
                if op_name in OPERATIONS:
                    result = OPERATIONS[op_name](payload)
                    responses.append({"operation": op_name, "status": "SUCCESS", "result": result})
                else:
                    responses.append({"operation": op_name, "status": "ERROR", "message": "Operação não suportada."})
            
        
            conn.send(str.encode(json.dumps({"results": responses})))
            
        except json.JSONDecodeError:
            error_msg = json.dumps({"error": "Formato JSON inválido."})
            conn.send(str.encode(error_msg))
            
    conn.close()
