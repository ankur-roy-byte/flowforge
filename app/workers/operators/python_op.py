from app.workers.operators.base import Operator, OperatorContext, register


@register
class PythonOperator(Operator):
    operator_type = "PythonOperator"

    async def execute(self, context: OperatorContext) -> dict[str, object]:
        raise NotImplementedError("PythonOperator execution is implemented after sandboxing is designed.")

