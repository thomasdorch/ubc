import ubcpdk

c = ubcpdk.components.mzi(delta_length=10.0, length_y=2.0, length_x=0.1, with_splitter=True, port_e1_splitter='opt2', port_e0_splitter='opt3', port_e1_combiner='opt2', port_e0_combiner='opt3', nbends=2)
c.plot()