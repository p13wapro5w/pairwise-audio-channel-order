import pytest
import math
from media import audio_channel_order as mod

CASES = [
    ("map", 'm.map_channel(2, ["L", "R", "C"]) == "C"'),
    ("gain", 'm.gain("C") == approx(0.707)'),
    ("lfe", 'm.lfe(200) == 120'),
    ("phase", 'm.phase(1, -1) is True'),
    ("mono", 'm.mono(5) == [5, 5]'),
    ("count", 'm.count(6, 4) == 4'),
    ("ridx", 'm.ridx(2, 2) == 4'),
    ("neg", 'm.negotiate("stereo", "5.1") == "stereo"'),
    ("upmix", 'm.upmix(1, 2) == (1, 2, 1, 2, 1, 2)'),
    ("meta", 'm.meta({"a": 1}) == {"a": 1}'),
    ("layout", 'm.layout_of({"layout": "5.1"}) == "5.1"'),
    ("swap", 'm.swap(1, 2) == (2, 1)'),
    ("channels", 'm.channels_for("5.1") == 6'),
    ("clamp", 'm.clamp_gain(2) == 1'),
    ("size", 'm.frame_size(2) == 4')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
