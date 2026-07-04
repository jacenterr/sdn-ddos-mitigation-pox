# sdn-ddos-mitigation-pox

# Laboratorio de prevención de ataques DDoS (SYN Flood) automatizado usando SDN, POX y Mininet

# Mitigación Automatizada de DDoS en Redes SDN 🛡️

Este proyecto demuestra la implementación de un sistema de prevención de ataques volumétricos (DDoS SYN Flood) utilizando el paradigma de Redes Definidas por Software (SDN). 

Al detectar una anomalía de tráfico, el plano de control aísla al atacante instalando dinámicamente reglas de descarte (Drop) en el plano de datos, manteniendo la integridad del servicio para los usuarios legítimos.

## 🛠️ Tecnologías Utilizadas
* **Plano de Control:** Controlador POX (Script personalizado en Python)
* **Plano de Datos:** Open vSwitch (OVS)
* **Emulación de Red:** Mininet
* **Generación de Tráfico:** hping3, tcpdump
* **Entorno:** Ubuntu Server

## 🏗️ Topología de la Red
La red emulada consta de una topología `single,3` (Un switch central conectado a 3 hosts).
* `h1`: Atacante
* `h2`: Servidor / Víctima
* `h3`: Tráfico legítimo normal

*(Si haces un diagrama en Canva, arrastra la imagen aquí)*

## 🚀 Cómo ejecutar el laboratorio

**1. Clonar el repositorio y ubicar el controlador:**
Copia el archivo `ddos_prevent.py` dentro de la carpeta `ext` de tu instalación de POX (`~/pox/ext/`).

**2. Iniciar el Controlador POX:**
```bash
./pox.py ddos_prevent
