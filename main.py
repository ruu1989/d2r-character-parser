import struct
from bitstring import BitArray


class BinaryReader:
    parsed_bytes = []

    def __init__(self, all_bytes):
        for byte in all_bytes:
            self.parsed_bytes.append(list(bin(byte)[2:].zfill(8)))
        print(self.parsed_bytes)

    def get_byte_as_int(self, offset):
        return int(self._get_bin_str_for_offset(offset), 2)

    def get_byte_as_string(self, offset):
        return chr(self.get_byte_as_int(offset))

    def get_string_for_length_without_pad(self, offset, max_length):
        chars = [
            self.get_byte_as_string(offset + a)
            for a
            in range(0, max_length)
            if not self._is_pad_at_offset(offset + a)
        ]

        return ''.join(chars)

    def _get_bin_str_for_offset(self, offset):
        return ''.join(self.parsed_bytes[offset])

    def _is_pad_at_offset(self, offset):
        return self._get_bin_str_for_offset(offset) == '00000000'


if __name__ == '__main__':
    with open("Tester.d2s", "rb") as f:
        br = BinaryReader(f.read())

    print(br.get_string_for_length_without_pad(20, 16))  # Name
    print(br.get_byte_as_int(43))  # Level

# class D2SParser:
#     def __init__(self, filename):
#         with open(filename, "rb") as f:
#             self.raw_data = f.read()
#
#             self.item_offset = self.raw_data.find(b'JM') + 2
#             self.corpse_offset = self.raw_data.find(b'JM', self.item_offset) + 2
#             # for jm in self._find_all_occurrences_in_raw(b'JM'):
#             #     print(self.read_from_position(jm + 2, 16))
#
#             inventory_offset = self._find_all_occurrences_in_raw(b'JM')[0] + 2
#             item_data = self.read_from_position(inventory_offset, 640)
#             print(item_data)
#             print(int.from_bytes(item_data, byteorder='big'))
#             # 11100000000000100000000000010100010000000000001010100000000000000001100111101001111
#             # \x07
#             # \x00\x10\x00\xa2\x00\x15\x00\x00\xcfO
#             # \x00\x10\x00\xa2\x00\x15\x04\x00\xcfO
#             # \x00\x10\x00\xa2\x00\x15\x08\x00\xcfO
#             # \x00\x10\x00\xa2\x00\x15\x0c\x00\xcfO
#             # \x00\x10\x00\xa2\x00\x05\xe4\xc4\x90=\x08\x10\x00\xa2\x00\x05\xa4\xe4G"\x10\x00\x82\x00
#             # print(self._bin_to_string((int.from_bytes(item_data, byteorder='big') >> 64 & 0b111111111111111111111111).to_bytes(3, byteorder='big')))
#             # print(self._bin_to_uint16(self.read_from_position(inventory_offset, 2)))
#
#
#             merc_offset = self._find_all_occurrences_in_raw(b'jf')[0] + 2
#             if self.read_from_position(merc_offset, 2) == b'kf':
#                 self.has_merc = False
#
#
#             # print(self.read_from_position(merc_offset, 2) == b'kf')
#             # self.has_corpse = self.read_from_position(self.corpse_offset, 2) != b'\x00\x00'
#
#             # print(self.item_offset)
#             # print(self.corpse_offset)
#             # position = self.read_from_position(self.item_offset, 16)
#             # print(position)
#
#             # print(self._bin_to_string(position))
#
#
#
#     def read_from_position(self, start, length_bytes):
#         return self.raw_data[start:start + length_bytes]
#
#     @property
#     def character_class(self):
#         return [
#             'Amazon',
#             'Sorceress',
#             'Necromancer',
#             'Paladin',
#             'Barbarian',
#             'Druid',
#             'Assassin'
#         ][self._bin_to_int(self.read_from_position(40, 1))]
#
#     @property
#     def character_name(self):
#         return self._bin_to_string(self.read_from_position(20, 16))
#
#     @property
#     def character_level(self):
#         return self._bin_to_int(self.read_from_position(43, 1))
#
#     @property
#     def is_dead(self):
#         pass
#
#     @staticmethod
#     def _bin_to_string(binary_value):
#         stripped = binary_value.rstrip(b'\x00')  # Remove trailing zeroes
#         length = len(stripped)
#         values = struct.unpack('{l}s'.format(l=length), stripped)
#         return values[0].decode('cp1252')
#
#     @staticmethod
#     def _bin_to_int(binary_value):
#         values = struct.unpack('b', binary_value)
#         return values[0]
#
#     @staticmethod
#     def _bin_to_uint16(binary_value):
#         values = struct.unpack('H', binary_value)
#         return values[0]
#
#     def _find_all_occurrences_in_raw(self, search_bytes):
#         start = 0
#         occurrences = []
#         while True:
#             start = self.raw_data.find(search_bytes, start)
#             if start == -1:
#                 return occurrences
#             occurrences.append(start)
#             start += len(search_bytes)  # use start += 1 to find overlapping matches
#

# if __name__ == '__main__':
#     tester = D2SParser("C:\\Users\\Ruu\\Saved Games\\Diablo II Resurrected\\Tester.d2s")
#     # print(tester.character_name)
#     # print(tester.character_level)
#     # print(tester.character_class)
#     # print('Dead: {d}'.format(d=tester.is_dead))
