from abc import ABC, abstractmethod
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class OperatorContext(BaseModel):
    dag_run_id: str
    task_run_id: str
    task_key: str
    config: dict[str, object] = Field(default_factory=dict)
    input_payload: dict[str, object] = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")


class Operator(ABC):
    operator_type: ClassVar[str]

    @abstractmethod
    async def execute(self, context: OperatorContext) -> dict[str, object]:
        raise NotImplementedError


OPERATOR_REGISTRY: dict[str, type[Operator]] = {}


def register(cls: type[Operator]) -> type[Operator]:
    OPERATOR_REGISTRY[cls.operator_type] = cls
    return cls
