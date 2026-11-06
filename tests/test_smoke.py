"""Vérifie que l'environnement est installé. Garde la CI verte avant l'agent."""


def test_psutil_is_installed():
    import psutil

    assert psutil.cpu_count() >= 1
