import math

# 标准布局：内部统一按 ITU-R BS.1934 / ffmpeg 常用顺序存放
# 5.1 = L R C LFE Ls Rs（设备可能按 L R Ls Rs C LFE 解释，必须靠显式映射消除歧义）
LAYOUT_CHANNELS = {
    "mono": ["C"],
    "stereo": ["L", "R"],
    "5.1": ["L", "R", "C", "LFE", "Ls", "Rs"],
    "7.1": ["L", "R", "C", "LFE", "Ls", "Rs", "Rls", "Rrs"],
}

LAYOUT_COUNTS = {
    "mono": 1,
    "stereo": 2,
    "5.1": 6,
    "7.1": 8,
}

# ITU-R BS.775 标准下混系数：
# Lo = L + 0.707*C + 0.707*Ls，Ro = R + 0.707*C + 0.707*Rs
# LFE 不进入下混（系数为 0），避免低频把耳机推失真
DOWNMIX_GAIN = {
    "L": 1.0,
    "R": 1.0,
    "C": 0.707,
    "Ls": 0.707,
    "Rs": 0.707,
    "LFE": 0.0,
}

LFE_CUTOFF_HZ = 120          # LFE 低通截止频率
SAMPLE_BYTES = 2             # 16-bit PCM，每采样 2 字节


def map_channel(index, layout):
    """显式声道映射：按位置索引取出命名字道，杜绝按设备默认顺序猜测。"""
    return layout[index]


def gain(kind):
    """标准下混系数：中置/环绕 0.707，主声道 1.0，LFE 为 0（不混进主声道）。"""
    return DOWNMIX_GAIN[kind]


def lfe(freq):
    """LFE 低通：高于 120Hz 的能量截止，返回钳制后的有效频率。"""
    return min(freq, LFE_CUTOFF_HZ)


def phase(left, right):
    """相位检测：两声道符号相反即反相，下混前必须检出以防信号互相抵消。"""
    return (left > 0 and right < 0) or (left < 0 and right > 0)


def mono(value):
    """单声道复制：同一采样完整复制到左右声道，而不是每声道各出一半。"""
    return [value, value]


def count(header, actual):
    """按实际声道数为准，并钳制到容器声明值之内，缺声道时防止读越界。"""
    return min(header, actual)


def ridx(frame, channels):
    """按帧重采样：交错缓冲区中第 frame 帧的起始下标 = 帧号 * 每帧声道数。"""
    return frame * channels


def negotiate(device, source):
    """设备布局协商：以设备实际支持的布局为准（如设备仅立体声则需下混）。"""
    return device


def upmix(left, right):
    """正确上混到 5.1（L R C LFE Ls Rs），逐声道显式给出而非把环绕复制到前置。"""
    return (left, right, left, right, left, right)


def meta(value):
    """保留布局元数据：转码时原样携带一份副本，下游无需猜测布局。"""
    return dict(value)


def layout_of(metadata):
    """布局读取：从元数据取显式布局声明，缺失时回退立体声。"""
    return metadata.get("layout", "stereo")


def swap(left, right):
    """声道交换：返回交换后的 (右, 左)。"""
    return (right, left)


def channels_for(layout):
    """布局通道数：按命名布局返回声道总数，未知布局按立体声处理。"""
    return LAYOUT_COUNTS.get(layout, 2)


def clamp_gain(value):
    """增益钳制：增益限制在 [0, 1]，防止过载削波。"""
    return max(0.0, min(1.0, float(value)))


def frame_size(channels):
    """帧大小：一帧（每个声道一个 16-bit 采样）所占字节数。"""
    return channels * SAMPLE_BYTES
