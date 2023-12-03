# Changelog

## 0.1.0 (2023-11-04)


### Features

* add bug report and feature request templates ([9627692](https://github.com/vikyw89/vectara/commit/962769217179ac5ae34a0fef4c147444d3bd44b7))
* add compose.alpha.yml file to define a Docker Compose configuration for the alpha environment ([b220359](https://github.com/vikyw89/vectara/commit/b2203594e9d4794d5dc8fdb21c6914a9356497de))
* add Dockerfile.alpha to build a Docker image for the alpha environment ([b220359](https://github.com/vikyw89/vectara/commit/b2203594e9d4794d5dc8fdb21c6914a9356497de))
* Add initial server implementation ([1a406ad](https://github.com/vikyw89/vectara/commit/1a406ad1872d19c4c0923412d48c2cb67c3b4c68))
* **agent/index.py:** add Agent class ([562b95f](https://github.com/vikyw89/vectara/commit/562b95f0e164fd76eee916344ed18719d45185d2))
* **main.py:** add support for OPENAI_TOKEN environment variable to be able to use OpenAI API in the application ([17ac2c2](https://github.com/vikyw89/vectara/commit/17ac2c2cd65415053e21719d3a27501763f3c990))
* **openai.py:** import openai and make a chat completion request using GPT-3.5-turbo model ([562b95f](https://github.com/vikyw89/vectara/commit/562b95f0e164fd76eee916344ed18719d45185d2))
* **prisma:** add Prisma schema file to define data models and relationships ([5e2aa5b](https://github.com/vikyw89/vectara/commit/5e2aa5b492c867ea826a5fb6c6545c5414eb1e16))
* **pyproject.toml:** add httpx, python-dotenv, and uvicorn dependencies to support additional functionality ([0471cc8](https://github.com/vikyw89/vectara/commit/0471cc8314edaea71fee0ee2c3bbc4e641b22fe1))
* **pyproject.toml:** add openai dependency with version 0.28.1 ([562b95f](https://github.com/vikyw89/vectara/commit/562b95f0e164fd76eee916344ed18719d45185d2))
* **pyproject.toml:** add Prisma as a dependency to the project ([5e2aa5b](https://github.com/vikyw89/vectara/commit/5e2aa5b492c867ea826a5fb6c6545c5414eb1e16))
* **src/libs/agent/index.py:** add classes for Request, Step, Memory, and Agent to handle stateful and stateless agents ([5e2aa5b](https://github.com/vikyw89/vectara/commit/5e2aa5b492c867ea826a5fb6c6545c5414eb1e16))


### Bug Fixes

* **main.py:** remove trailing slash from "/webhook" route to improve consistency with other routes ([17ac2c2](https://github.com/vikyw89/vectara/commit/17ac2c2cd65415053e21719d3a27501763f3c990))
