import ubcpdk

c = ubcpdk.components.add_fiber_array(gc_port_name='opt1', with_loopback=False, optical_routing_type=0, fanout_length=0.0)
c.plot()