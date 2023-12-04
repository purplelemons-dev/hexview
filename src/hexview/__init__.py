from typing import Literal


def main(
    filename: str,
    data_type: Literal["hex", "dec", "oct", "bin"] = "hex",
    line_len: int = 16,
):
    with open(filename, "rb") as f:
        file_bytes = f.read()
    main_area, char_area = "", ""
    for i, byte in enumerate(file_bytes):
        if i % line_len == 0:
            if data_type == "hex":
                main_area += f"{i:08x} | "
            elif data_type == "dec":
                main_area += f"{i:08d} | "
            elif data_type == "oct":
                main_area += f"{i:08o} | "
            elif data_type == "bin":
                main_area += f"{i:08b} | "
            else:
                raise ValueError("data_type must be one of: hex, dec, oct, bin")
        if data_type=="hex":
            main_area += f"{byte:02x} "
        elif data_type=="dec":
            main_area += f"{byte:03d} "
        elif data_type=="oct":
            main_area += f"{byte:03o} "
        elif data_type=="bin":
            main_area += f"{byte:08b} "
        char_area += chr(byte) if byte in range(32, 127) else "."
        if i % line_len == line_len - 1:
            main_area += f"| {char_area}\n"
            char_area = ""
    if char_area:
        main_area += "   " * (line_len - len(char_area)) + f"| {char_area}\n"
    return main_area

