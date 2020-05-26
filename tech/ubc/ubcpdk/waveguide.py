import os

from phidl import Device
from phidl.utilities import load_lyp

lys = load_lyp(os.path.join(os.path.dirname(__file__), "..", "ubc_layers.lyp"))


def waveguide(length=10, width=0.5, layer=lys["WG"], layers_cladding=[lys["DEVREC"]]):
    c = Device()
    w = width
    c.add_polygon([(0, -w), (length, -w), (length, w), (0, w)], layer=layer)

    c.add_port(name="W0", midpoint=[0, 0], width=width, orientation=180)
    c.add_port(name="E0", midpoint=[length, 0], width=width, orientation=0)

    # labels = [
    #     f"Lumerical_INTERCONNECT_library=Design kits/EBeam",
    #     f"Lumerical_INTERCONNECT_component=ebeam_wg_integral_1550",
    #     f"Spice_param:wg_width={width:.3f}u wg_length={length:.3f}u",
    # ]
    # for i, text in enumerate(labels):
    #     c.add(pp.c.label(text=text, position=(length / 2, i * 0.1), layer=lys['DEVREC']))
    return c


if __name__ == "__main__":
    c = waveguide()
    c.write_gds("waveguide.gds")
