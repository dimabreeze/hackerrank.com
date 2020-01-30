from decode_huffmans import decodeHuff, buildRoot, buildEncoded


def __build_root_and_encode(inp: str):
    root = buildRoot(inp)
    encoded = buildEncoded(root, inp)
    return root, encoded


def __validate(inp: str):
    root, encoded = __build_root_and_encode(inp)
    assert decodeHuff(root, encoded) == inp


def test_build_root_and_encode():
    inp = "ABRACADABRA"
    root, encoded = __build_root_and_encode(inp)
    assert encoded == "01111001100011010111100"


def test_sample_input_00():
    __validate("ABRACADABRA")


def test_sample_input_0():
    __validate("ABACA")


def test_sample_input_1():
    __validate("Rumpelstiltskin")


def test_sample_input_2():
    __validate("howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?")
