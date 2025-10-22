# ==============================================================
#  AlgoSec Network Diagram (.drawio XML)
# ==============================================================

import datetime

xml = f"""<mxfile host="app.diagrams.net" modified="{datetime.datetime.utcnow().isoformat()}Z" 
 agent="ChatGPT GPT-5" version="20.6.3">
  <diagram name="AlgoSec Network Architecture">
    <mxGraphModel dx="1420" dy="824" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" 
     arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- SMTP / DNS / NTP / AD/LDAP -->
        <mxCell id="infra" value="SMTP / DNS / NTP / AD/LDAP" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1;align=center;" 
         vertex="1" parent="1">
          <mxGeometry x="320" y="40" width="210" height="60" as="geometry"/>
        </mxCell>

        <!-- Mgmt Traffic label -->
        <mxCell id="mgmt" value="(Mgmt Traffic)" style="text;html=1;align=center;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="390" y="110" width="100" height="20" as="geometry"/>
        </mxCell>

        <!-- AlgoSec AFA -->
        <mxCell id="afa" value="AlgoSec AFA\\n(Mgmt Subnet: 10.1)" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=13;" 
         vertex="1" parent="1">
          <mxGeometry x="330" y="140" width="190" height="60" as="geometry"/>
        </mxCell>

        <!-- SSH/API Pull -->
        <mxCell id="ssh" value="(SSH/API Pull | Syslog/SNMP)" style="text;html=1;align=center;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="360" y="210" width="180" height="20" as="geometry"/>
        </mxCell>

        <!-- Perimeter Firewall -->
        <mxCell id="fw" value="Perimeter Firewall\\n(e.g. Palo Alto)" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=13;" 
         vertex="1" parent="1">
          <mxGeometry x="330" y="240" width="190" height="70" as="geometry"/>
        </mxCell>

        <!-- App Server 1 -->
        <mxCell id="app1" value="App Server 1\\n(Finance App)\\nSubnet: 10.10" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" 
         vertex="1" parent="1">
          <mxGeometry x="200" y="350" width="170" height="70" as="geometry"/>
        </mxCell>

        <!-- App Server 2 -->
        <mxCell id="app2" value="App Server 2\\n(HR Web Server)\\nSubnet: 10.20" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" 
         vertex="1" parent="1">
          <mxGeometry x="470" y="350" width="170" height="70" as="geometry"/>
        </mxCell>

        <!-- Connections -->
        <mxCell id="arrow1" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;" 
         edge="1" parent="1" source="infra" target="afa">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="arrow2" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;" 
         edge="1" parent="1" source="afa" target="fw">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="arrow3" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;" 
         edge="1" parent="1" source="fw" target="app1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="arrow4" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;" 
         edge="1" parent="1" source="fw" target="app2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open("AlgoSec_Network.drawio", "w", encoding="utf-8") as f:
    f.write(xml)

print("Diagram generated successfully: AlgoSec_Network.drawio")
