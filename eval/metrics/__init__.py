"""DeepEval custom metrics for rubric-based scientific-question scoring.

Import policy: the gold-rubric scoring path (``JudgeLLM`` + ``score_against_gold``)
is deepeval-free, so it is imported eagerly. The two legacy ``Rubric*Metric``
classes subclass ``deepeval.metrics.BaseMetric``; importing them eagerly would
drag the heavy ``deepeval`` dependency into every consumer — including the
headless ``eval.batch_judge`` CLI, which does not need it. They are therefore
exposed lazily via PEP 562 ``__getattr__`` so ``deepeval`` is imported only when
one of those names is actually accessed.
"""

from .judge_llm import JudgeLLM
from .gold_rubric_metric import GoldRubricResult, score_against_gold

__all__ = [
    "JudgeLLM",
    "RubricDimensionMetric",
    "RubricCompositeMetric",
    "GoldRubricResult",
    "score_against_gold",
]

# name → submodule holding it; imported on first access so deepeval stays optional.
_LAZY = {
    "RubricDimensionMetric": ".rubric_dimension_metric",
    "RubricCompositeMetric": ".rubric_composite_metric",
}


def __getattr__(name):  # PEP 562 — defer deepeval import until actually used.
    module_path = _LAZY.get(name)
    if module_path is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    from importlib import import_module

    return getattr(import_module(module_path, __name__), name)


def __dir__():
    return sorted(__all__)
