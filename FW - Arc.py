# ==============================================================
#  AlgoSec Architecture Diagram Generator (.drawio XML)
#  Author: ChatGPT (for Luís)
# ==============================================================

import datetime

xml_template = f"""<mxfile host="app.diagrams.net" modified="{datetime.datetime.utcnow().isoformat()}Z" 
 agent="ChatGPT GPT-5" version="20.6.3">
  <diagram name="AlgoSec Flow">
    <mxGraphModel dx="1420" dy="824" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" 
     arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- User/Admin -->
        <mxCell id="UserAdmin" value="User/Admin" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1;align=center;" 
         vertex="1" parent="1">
          <mxGeometry x="280" y="40" width="150" height="60" as="geometry"/>
        </mxCell>

        <!-- Central Manager -->
        <mxCell id="CentralManager" value="Central Manager (UI + API)" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b3d9ff;strokeColor=#4b89dc;fontSize=13;" 
         vertex="1" parent="1">
          <mxGeometry x="480" y="40" width="200" height="60" as="geometry"/>
        </mxCell>

        <!-- HTTPS link -->
        <mxCell id="https" value="HTTPS" 
         style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;fontSize=12;" 
         edge="1" parent="1" source="UserAdmin" target="CentralManager">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- AFA -->
        <mxCell id="AFA" value="AFA (Analyzer)\\n- connects to firewalls\\n- parses configs" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=13;" 
         vertex="1" parent="1">
          <mxGeometry x="380" y="160" width="200" height="90" as="geometry"/>
        </mxCell>

        <!-- triggers arrow -->
        <mxCell id="triggers" value="triggers" 
         style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;fontSize=12;" 
         edge="1" parent="1" source="CentralManager" target="AFA">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- FireFlow -->
        <mxCell id="FireFlow" value="FireFlow (Ticketing)\\n- receives rule requests\\n- auto-analyzes and routes" 
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=13;" 
         vertex="1" parent="1">
          <mxGeometry x="380" y="300" width="200" height="90" as="geometry"/>
        </mxCell>

        <!-- feeds arrow -->
        <mxCell id="feeds" value="feeds" 
         style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;fontSize=12;" 
         edge="1" parent="1" source="AFA" target="FireFlow">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

# Save to file
with open("AlgoSec_Architecture.drawio", "w", encoding="utf-8") as f:
    f.write(xml_template)

print("Draw.io diagram created: AlgoSec_Architecture.drawio")
