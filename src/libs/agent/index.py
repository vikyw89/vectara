from pydantic import BaseModel, Field


class Request(BaseModel):
    id: str
    agentId: str
    userId: str
    history: list
    data: any = Field(default=None)
    type: str = Field(default="unknown")


class Step:
    def __init__(self, name, description, stepFn) -> None:
        self.name = name
        self.description = description
        self.stepFn = stepFn

    def run(self, request):
        return self.stepFn(request)

# This class is to handle any stateful data


class Memory:
    def __init__(self, name, description, saveFn, recallFn, logFn) -> None:
        self.name = name
        self.description = description
        self.saveFn = saveFn
        self.recallFn = recallFn
        self.logFn = logFn

    def log(self, request):
        return self.logFn(request)

    def save(self, request):
        self.logFn(request)
        return self.saveFn(request)

    def recall(self, request):
        self.logFn(request)
        return self.recallFn(request)

# stateless agents, designed to be customizable, 1 memory module and endless steps


class Agent:
    def __init__(self, memory, steps: list(Step)) -> None:
        self.steps = steps
        self.memory = memory

    def run(self, request):
        steps = self.steps
        self.memory.save(request)

        for step in steps:
            output = step.run(request)
            self.memory.save(output)
        return memory
