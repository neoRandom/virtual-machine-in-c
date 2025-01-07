import os
import sys

MEMORY_SIZE = 0x10000  # 2^16 = 65536
ROM_OFFSET = 0x200     # 2^9  = 512
STACK_SIZE = 16
NUM_REGS = 16

def read_file(file_path: str, mode: str = "rb"):
    if not os.path.exists(file_path) or not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        return None

    with open(file_path, mode) as file:
        content: bytes | None = file.read()
    
    return content

class Machine:
    def __init__(self):
        self.instruction_pointer = ROM_OFFSET
        self.stack_pointer = 0
        self.ram = [0 for _ in range(MEMORY_SIZE)]
        self.opcode = 0
        self.stack = [0 for _ in range(STACK_SIZE)]
        self.registers = [0 for _ in range(NUM_REGS)]
        self.instruction_reg = 0
        self.d_timer = 0
        self.s_timer = 0

    def start(self):
        ...

    def bootstrap(self):
        ...
    
    def reset(self):
        ...
    
    def tick(self):
        ...
    
    def tick_timer(self):
        ...
    
    def fetch(self):
        ...

    def decode(self):
        ...
    
    def execute(self):
        ...

    def load(self, *, index: int = ROM_OFFSET, file_path: str | None = None, data: bytes | None = None):
        temp_data = None

        #
        if index < ROM_OFFSET:
            raise ValueError(f"`index` ({index}) needs to be equal or greater than `ROM_OFFSET` ({ROM_OFFSET})")

        if file_path is not None:
            temp_data = read_file(file_path)

        if temp_data is not None:
            data = temp_data

        if data is None:
            raise ValueError("No data found")
        
        #
        start = index
        end = index + len(data)
        self.ram[start:end] = data
    
    def push(self):
        ...
    
    def pop(self):
        ...


def run():
    machine = Machine()

    machine.start()


if __name__ == "__main__":
    run()
