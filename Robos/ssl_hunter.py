"""
Docstring-------------------------------------------------
ROBÔ: SSL HUNTER
FUNÇÃO: Faz auditoria de segurança em sites específicos.
        Ou seja, Auditor de Segurança: Checa certificados SSL de sites externos.
STATUS: Ativo e funcional - Nível 2
"""
# --- SSL Hunter: Auditoria de Segurança ---
import ssl
import socket
import datetime
import requests

# Lista de alvos (No futuro, o robô pode pegar isso do Google Maps)
# Coloquei sites aleatórios apenas como exemplo, e um que costuma dar erro pra testar
dominios = [
    "google.com",
    "python.org",
    "siteinexistente12345.com.br",
    "expired.badssl.com",  # Site feito para testar erro de SSL
]

def verificar_site(hostname):
    print(f"\n[...] Analisando: {hostname}")
    
    # 1. Teste de Conexão Básica (O site existe?)
    try:
        requests.get(f"http://{hostname}", timeout=5)
    except:
        print(f"[ALVO ABATIDO] O site {hostname} nem abre! (Oportunidade de oferecer resgate)")
        return

    # 2. Teste de SSL (Segurança)
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                # Pega a data de validade
                notAfter = cert['notAfter']
                # Formato de data do SSL é chato, vamos converter
                expiry_date = datetime.datetime.strptime(notAfter, r'%b %d %H:%M:%S %Y %Z')
                days_left = (expiry_date - datetime.datetime.utcnow()).days
                
                if days_left < 0:
                    print(f"[ALVO CRÍTICO] {hostname} -> CERTIFICADO VENCIDO! (Aviso de 'Não Seguro')")
                elif days_left < 15:
                    print(f"[ALERTA] {hostname} -> Vence em {days_left} dias. (Hora de renovar)")
                else:
                    print(f"[OK] {hostname} -> Seguro ({days_left} dias restantes).")
                    
    except ssl.SSLError:
        print(f"[ALVO CRÍTICO] {hostname} -> Erro de SSL/Segurança detectado!")
    except Exception as e:
        print(f"[ERRO] Não consegui checar o SSL de {hostname}: {e}")

print("--- INICIANDO VARREDURA DE SEGURANÇA ---")
for site in dominios:
    verificar_site(site)
print("\n--- FIM DA CAÇADA ---")
