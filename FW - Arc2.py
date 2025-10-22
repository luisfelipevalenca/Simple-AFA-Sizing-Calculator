# ==============================================================
#  AlgoSec Full Architecture Diagram (.drawio XML)
#  Author: ChatGPT (for Luís)
# ==============================================================

import datetime

xml = f"""<mxfile host="app.diagrams.net" modified="{datetime.datetime.utcnow().isoformat()}Z"
 agent="ChatGPT GPT-5" version="20.6.3">
  <diagram name="AlgoSec Architecture">
    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1"
     arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="1000" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- ServiceNow / ITSM -->
        <mxCell id="servicenow" value="ServiceNow / ITSM"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1;align=center;"
         vertex="1" parent="1">
          <mxGeometry x="500" y="40" width="200" height="50" as="geometry"/>
        </mxCell>

        <!-- SIEM / Log Server -->
        <mxCell id="siem" value="SIEM / Log Server (e.g., QRadar)"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="480" y="120" width="240" height="50" as="geometry"/>
        </mxCell>

        <!-- Active Directory -->
        <mxCell id="ad" value="Active Directory"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="520" y="200" width="160" height="50" as="geometry"/>
        </mxCell>

        <!-- AlgoSec Central Mgmt -->
        <mxCell id="central" value="AlgoSec Central Mgmt"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="480" y="280" width="240" height="60" as="geometry"/>
        </mxCell>

        <!-- Firewall Analyzer -->
        <mxCell id="fa" value="FirewallAnalyzer"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;"
         vertex="1" parent="1">
          <mxGeometry x="180" y="380" width="160" height="60" as="geometry"/>
        </mxCell>

        <!-- FireFlow -->
        <mxCell id="ff" value="FireFlow"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;"
         vertex="1" parent="1">
          <mxGeometry x="480" y="380" width="160" height="60" as="geometry"/>
        </mxCell>

        <!-- BusinessFlow -->
        <mxCell id="bf" value="BusinessFlow"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;"
         vertex="1" parent="1">
          <mxGeometry x="780" y="380" width="160" height="60" as="geometry"/>
        </mxCell>

        <!-- AlgoSec Collector -->
        <mxCell id="collector" value="AlgoSec Collector(s)"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="470" y="520" width="260" height="60" as="geometry"/>
        </mxCell>

        <!-- Firewalls / Routers / Cloud APIs -->
        <mxCell id="fw" value="Firewalls / Routers / Cloud APIs"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="450" y="620" width="300" height="60" as="geometry"/>
        </mxCell>

        <!-- App Servers / DC -->
        <mxCell id="app" value="App Servers / DC"
         style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=13;"
         vertex="1" parent="1">
          <mxGeometry x="500" y="720" width="200" height="50" as="geometry"/>
        </mxCell>

        <!-- Connections (Vertical flow) -->
        <mxCell id="edge1" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="servicenow" target="siem"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="edge2" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="siem" target="ad"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="edge3" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="ad" target="central"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Central Mgmt to modules -->
        <mxCell id="edge4" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="central" target="fa"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="edge5" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="central" target="ff"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="edge6" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="central" target="bf"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Merged edges from FA / FF / BF to Collector -->
        <mxCell id="edge7" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="fa" target="collector"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="edge8" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="ff" target="collector"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="edge9" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="bf" target="collector"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Downward flow -->
        <mxCell id="edge10" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="collector" target="fw"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="edge11" style="edgeStyle=elbowEdgeStyle;endArrow=block;html=1;strokeColor=#000000;"
         edge="1" parent="1" source="fw" target="app"><mxGeometry relative="1" as="geometry"/></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

# Write the .drawio file
with open("AlgoSec_Full_Architecture.drawio", "w", encoding="utf-8") as f:
    f.write(xml)

print("✅ Draw.io file created: AlgoSec_Full_Architecture.drawio")
