# Todd Bartoszkiewicz
# CSC507: Foundations of Operating Systems
# Module 4: Critical Thinking Assignment
#
# First Fit memory allocation algorithm
class MemoryBlock:
    def __init__(self, block_size, block_sizes):
        self.block_size = block_size
        self.blocks = []
        start = 0
        for i in range(len(block_sizes)):
            self.blocks.append([start, block_sizes[i]])
            start += block_sizes[i]
        # Initially all blocks are free
        self.free_block_list = self.blocks[:]

    def allocate(self, process_block_size):
        for i, (start, block_size) in enumerate(self.free_block_list):
            if block_size >= process_block_size:
                # Allocate the block
                allocated_start = start
                allocated_block_size = process_block_size

                self.free_block_list[i] = (start, block_size - allocated_block_size)
                return i, allocated_start
        # Couldn't find a block size big enough to allocate
        return None

    def print_memory_map(self):
        print("Memory Map:")
        i = 1
        for start, block_size in self.free_block_list:
            print(f"  Block#{i}: {start}, Remaining Block Size: {block_size}")
            i += 1


if __name__ == "__main__":
    memory_size = 1000
    memory_block_sizes = [100, 200, 300, 400, 500, 600]
    process_sizes = [212, 417, 112, 426]

    memory_block = MemoryBlock(memory_size, memory_block_sizes)

    print("Initial Memory Block Map")
    memory_block.print_memory_map()

    print("-"*30)

    k = 1
    for process_size in process_sizes:
        j, allocation_address = memory_block.allocate(process_size)
        if allocation_address is not None:
            print(f"[ALLOC] Process #{k} (size: {process_size}) -> Block {j}")
        else:
            print(f"Could not allocate memory for block size: {process_size}")
        k += 1

    print("-"*30)

    print("Final Memory Block Map")
    memory_block.print_memory_map()
