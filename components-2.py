import ubcpdk

c = ubcpdk.components.bend_euler(angle=90.0, p=0.5, with_arc_floorplan=True, npoints=720, direction='ccw', with_cladding_box=True)
c.plot()