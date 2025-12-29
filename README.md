# Remote-Procedure-Call-RPC-Implementation-Deployment-on-AWS-EC2
# RPC Lab — Distributed Computing (Trimester 8)

## Описание проекта
Минимальная реализация **Remote Procedure Call (RPC)** с использованием Python и TCP-сокетов.  
Состоит из двух компонентов:
- **Server** — предоставляет удалённую функцию `add(a, b)`.
- **Client** — вызывает функцию сервера, обрабатывает таймауты и повторные попытки.

Проект развернут на **AWS EC2** (две машины).

---

## Требования
- Python 3
- Библиотека `uuid` (встроена в Python)
- Доступ к AWS EC2

---

Настройка EC2:

Две EC2 машины (Ubuntu 22.04):

rpc-server-node

rpc-client-node

Security Group:

SSH (22) — My IP

Custom TCP (5000) — 0.0.0.0/0 (для RPC)

Проверить соединение:

ping <SERVER_PUBLIC_IP>
nc -vz <SERVER_PUBLIC_IP> 5000



