"""Contrat de agent.collector.collect().

Squelette : les tests sont ignorés tant que agent/collector.py n'existe pas,
pour que la CI reste verte sur la PR de mise en place.
"""
import json

import pytest

collector = pytest.importorskip("agent.collector")

EXPECTED_KEYS = {"ts", "cpu_pct", "ram_pct", "disk_free_pct"}
# Conformité : ce qui ne doit JAMAIS sortir de l'agent (voir docs/DATA_POLICY.md)
FORBIDDEN_KEYS = {"hostname", "username", "user", "window_title", "url", "keystrokes"}


def test_sample_has_expected_keys():
    sample = collector.collect()
    assert EXPECTED_KEYS <= sample.keys()


def test_sample_has_no_forbidden_keys():
    sample = collector.collect()
    assert not (FORBIDDEN_KEYS & sample.keys())


@pytest.mark.parametrize("key", ["cpu_pct", "ram_pct", "disk_free_pct"])
def test_percentages_are_in_range(key):
    sample = collector.collect()
    assert 0.0 <= sample[key] <= 100.0


def test_sample_is_json_serializable():
    json.dumps(collector.collect())


def test_ts_is_utc():
    # TODO: décider le format de ts (epoch ? ISO 8601 ?) puis écrire l'assertion
    pytest.skip("format de ts à décider")


def test_agent_overhead_is_below_one_percent_cpu():
    # TODO (semaine 1 ou 4) : mesurer avec psutil.Process().cpu_percent()
    pytest.skip("mesure à écrire")
