from easygit import Easygit

def test_app():
    git = Easygit()
    assert git.query('h') == "Try another query"