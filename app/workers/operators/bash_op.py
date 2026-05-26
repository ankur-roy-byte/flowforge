from app.workers.operators.base import Operator, OperatorContext, register


@register
class BashOperator(Operator):
    operator_type = "BashOperator"

    async def execute(self, context: OperatorContext) -> dict[str, object]:
        raise NotImplementedError("BashOperator execution is implemented in Phase 3.")

