from pytest import fixture

@fixture()
def Ansible_var(Ansible):
    """
    Returns value for Ansible Variable:
    - **variable** - The variable
    **returns** - Variable String
    """
    def f(variable):
        return Ansible("debug", "msg={{ %s }}" % variable)["msg"]
    return f

def test_httpd_is_installed(Package, Ansible_var):
    httpd = Package("httpd")
    assert httpd.is_installed
    assert httpd.version == Ansible_var("httpd_version")

def test_httpd_running_and_enabled(Service):
    httpd = Service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
