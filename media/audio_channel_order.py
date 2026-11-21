import math

def map_channel(index, layout):
    """显式声道映射。"""
    raise NotImplementedError("TODO: map_channel")

def gain(kind):
    """标准下混系数。"""
    raise NotImplementedError("TODO: gain")

def lfe(freq):
    """LFE 低通。"""
    raise NotImplementedError("TODO: lfe")

def phase(left, right):
    """相位检测。"""
    raise NotImplementedError("TODO: phase")

def mono(value):
    """单声道复制。"""
    raise NotImplementedError("TODO: mono")

def count(header, actual):
    """按实际声道数。"""
    raise NotImplementedError("TODO: count")

def ridx(frame, channels):
    """按帧重采样。"""
    raise NotImplementedError("TODO: ridx")

def negotiate(device, source):
    """设备布局协商。"""
    raise NotImplementedError("TODO: negotiate")

def upmix(left, right):
    """上混。"""
    raise NotImplementedError("TODO: upmix")

def meta(value):
    """保留元数据。"""
    raise NotImplementedError("TODO: meta")

def layout_of(metadata):
    """布局读取。"""
    raise NotImplementedError("TODO: layout_of")

def swap(left, right):
    """声道交换。"""
    raise NotImplementedError("TODO: swap")

def channels_for(layout):
    """布局通道数。"""
    raise NotImplementedError("TODO: channels_for")

def clamp_gain(value):
    """增益钳制。"""
    raise NotImplementedError("TODO: clamp_gain")

def frame_size(channels):
    """帧大小。"""
    raise NotImplementedError("TODO: frame_size")
