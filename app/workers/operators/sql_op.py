from app.workers.operators.base import Operator, OperatorContext, register


@register
class SQLOperator(Operator):
    operator_type = "SQLOperator"

    async def execute(self, context: OperatorContext) -> dict[str, object]:
        raise NotImplementedError("SQLOperator execution is implemented after connection handling.")
