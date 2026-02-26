import os
import json
from samplecode.sample import save_dict

def test_save_dict(tmpdir, capsys):
    filepath=os.path.join(tmpdir, "test.json") #joins temporary directory path with name of file
    _dict= {"a": 1, "b" : 2}
    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    #How to read statements from functions
    assert capsys.readouterr().out == "saved\n"