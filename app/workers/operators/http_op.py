from app.workers.operators.base import Operator, OperatorContext, register


@register
class HTTPOperator(Operator):
    operator_type = "HTTPOperator"

    async def execute(self, context: OperatorContext) -> dict[str, object]:
        raise NotImplementedError("HTTPOperator execution is implemented in Phase 3.")

