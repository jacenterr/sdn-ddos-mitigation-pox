from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

packet_counts = {}
THRESHOLD = 100
blocked_macs = set()

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    src_mac = str(packet.src)
    
    if src_mac.startswith("33:33") or src_mac == "ff:ff:ff:ff:ff:ff":
        return

    current_time = time.time()
    
    if src_mac not in packet_counts:
        packet_counts[src_mac] = []
    
    packet_counts[src_mac].append(current_time)
    
    packet_counts[src_mac] = [t for t in packet_counts[src_mac] if current_time - t < 2]
    
    if len(packet_counts[src_mac]) > THRESHOLD and src_mac not in blocked_macs:
        log.warning("ALERTA DDoS: Trafico anomalo detectado desde MAC: %s", src_mac)
        blocked_macs.add(src_mac)
        
        msg = of.ofp_flow_mod()
        msg.match.dl_src = packet.src  
        msg.idle_timeout = 30          
        msg.hard_timeout = 60          
        event.connection.send(msg)
        log.info("Regla Drop instalada en el Switch para MAC: %s", src_mac)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Modulo de prevencion DDoS cargado con exito.")