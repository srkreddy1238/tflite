# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class BidirectionalSequenceRNNOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBidirectionalSequenceRNNOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BidirectionalSequenceRNNOptions()
        x.Init(buf, n + offset)
        return x

    # BidirectionalSequenceRNNOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BidirectionalSequenceRNNOptions
    def TimeMajor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # BidirectionalSequenceRNNOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def BidirectionalSequenceRNNOptionsStart(builder): builder.StartObject(2)
def BidirectionalSequenceRNNOptionsAddTimeMajor(builder, timeMajor): builder.PrependBoolSlot(0, timeMajor, 0)
def BidirectionalSequenceRNNOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(1, fusedActivationFunction, 0)
def BidirectionalSequenceRNNOptionsEnd(builder): return builder.EndObject()
