import ubcpdk

c = ubcpdk.components.ring_with_crossing(gap=0.2, length_x=4, length_y=0, radius=5.0, with_component=True, port_name='opt4')
c.plot()