from app.workers.operators import OPERATOR_REGISTRY


def test_builtin_operators_are_registered() -> None:
    assert set(OPERATOR_REGISTRY) == {
        "BashOperator",
        "HTTPOperator",
        "PythonOperator",
        "SQLOperator",
    }
