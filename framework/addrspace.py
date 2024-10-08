import os
import struct


class FileAddressSpace:
    def __init__(self, fname, mode='rb', fast=False):
        self.fname = fname
        self.name = fname
        self.fhandle = open(fname, mode)
        self.fsize = os.path.getsize(fname)

        if fast:
            self.fast_fhandle = open(fname, mode)

    def fread(self, len):
        return self.fast_fhandle.read(len)

    def read(self, addr, len):
        self.fhandle.seek(addr)
        return self.fhandle.read(len)

    def read_long(self, addr):
        string = self.read(addr, 4)
        (longval,) = struct.unpack('L', string)
        return longval

    def get_address_range(self):
        return [0, self.fsize - 1]

    def get_available_addresses(self):
        return [self.get_address_range()]

    def is_valid_address(self, addr):
        return addr < self.fsize - 1

    def close(self):
        self.fhandle.close()


# Code below written by Brendan Dolan-Gavitt

BLOCK_SIZE = 0x1000


class HiveFileAddressSpace:
    def __init__(self, fname):
        self.fname = fname
        self.base = FileAddressSpace(fname)

    def vtop(self, vaddr):
        return vaddr + BLOCK_SIZE + 4

    def read(self, vaddr, length, zero=False):
        first_block = BLOCK_SIZE - vaddr % BLOCK_SIZE
        full_blocks = ((length + (vaddr % BLOCK_SIZE)) // BLOCK_SIZE) - 1
        left_over = (length + vaddr) % BLOCK_SIZE

        paddr = self.vtop(vaddr)
        if paddr is None and zero:
            if length < first_block:
                return "\0" * length
            else:
                stuff_read = "\0" * first_block
        elif paddr is None:
            return None
        else:
            if length < first_block:
                stuff_read = self.base.read(paddr, length)
                if not stuff_read and zero:
                    return "\0" * length
                else:
                    return stuff_read

            stuff_read = self.base.read(paddr, first_block)
            if not stuff_read and zero:
                stuff_read = "\0" * first_block

        new_vaddr = vaddr + first_block
        for __ in range(0, full_blocks):
            paddr = self.vtop(new_vaddr)
            if paddr is None and zero:
                stuff_read = stuff_read + "\0" * BLOCK_SIZE
            elif paddr is None:
                return None
            else:
                new_stuff = self.base.read(paddr, BLOCK_SIZE)
                if not new_stuff and zero:
                    new_stuff = "\0" * BLOCK_SIZE
                elif not new_stuff:
                    return None
                else:
                    stuff_read = stuff_read + new_stuff
            new_vaddr = new_vaddr + BLOCK_SIZE

        if left_over > 0:
            paddr = self.vtop(new_vaddr)
            if paddr is None and zero:
                stuff_read = stuff_read + "\0" * left_over
            elif paddr is None:
                return None
            else:
                stuff_read = stuff_read + self.base.read(paddr, left_over)
        return stuff_read

    def read_long_phys(self, addr):
        string = self.base.read(addr, 4)
        (longval,) = struct.unpack('L', string)
        return longval

    def is_valid_address(self, vaddr):
        paddr = self.vtop(vaddr)
        if not paddr:
            return False
        return self.base.is_valid_address(paddr)
