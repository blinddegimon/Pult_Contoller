import numpy as np

BUFFER_SIZE = 2000



def convert_degrees(val, degree_flag = False, scale = 91):

    return val / scale if degree_flag else val

def description(s):
    return (f"Connected to {s.name} : {s.string_baud_rate}, "
            f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
            f"{s.string_flow_control}")

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'little',signed=True)
    return r

def add_shift_buffer(buffer, element):
    buffer = np.roll(buffer, shift=-1)
    buffer[len(buffer)-1] = element

    return buffer