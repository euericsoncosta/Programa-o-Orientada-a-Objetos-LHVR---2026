from conta_sem_protecao import Conta_Bancaria
from conta import Conta_Bancaria as Conta_Protegida

conta1 = Conta_Bancaria("234-5", "João Silva", 1000.0)

print(f"Saldo: {conta1.saldo}")

conta1.saldo = -500.0

print(f"Saldo: {conta1.saldo}")

conta2 = Conta_Protegida("678-9", "Maria Oliveira")

print("Informações da conta protegida:")
print(f"Número da conta: {conta2.numero_conta}")
print(f"Titular: {conta2.titular}")
print(f"Saldo: {conta2.saldo}")
print("____________________________________________________________")

conta2.titular = "Josefa Santos"

print("Informações da conta protegida:")
print(f"Número da conta: {conta2.numero_conta}")
print(f"Titular: {conta2.titular}")
print(f"Saldo: {conta2.saldo}")
print("____________________________________________________________")

# conta2.saldo = 10000.0
conta2.depositar(10000.0)

print("Informações da conta protegida:")
print(f"Número da conta: {conta2.numero_conta}")
print(f"Titular: {conta2.titular}")
print(f"Saldo: {conta2.saldo}")
print("____________________________________________________________")

