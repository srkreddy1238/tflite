# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class ZerosLikeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsZerosLikeOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ZerosLikeOptions()
        x.Init(buf, n + offset)
        return x

    # ZerosLikeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ZerosLikeOptionsStart(builder): builder.StartObject(0)
def ZerosLikeOptionsEnd(builder): return builder.EndObject()