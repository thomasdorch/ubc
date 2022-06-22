import ubcpdk

c = ubcpdk.components.straight(length=10.0, width=0.5, layer=(1, 0), with_pins=True)
c.plot()