from easygit.easygit import Easygit

def test_app():
    git = Easygit()
    assert git.query('h') == "Try another query or visit https://git-scm.com/docs"
