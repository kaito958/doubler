import subprocess

def test_doubler():
    # 10を入力して、100.0が返ってくるかテスト
    result = subprocess.run(
        ['doubler'],
        input='10\n',
        text=True,
        capture_output=True
    )
    assert '100.0' in result.stdout

