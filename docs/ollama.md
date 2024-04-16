## Ollama

### Installation

Ollama allows you to run open-source large language models, such as Llama 2, locally. Ollama bundles model weights, configuration, and data into a single package, defined by a Modelfile. It optimizes setup and configuration details, including GPU usage.

    https://ollama.com/

    OR 

    curl https://ollama.ai/install.sh | sh


Ollama supports a variety of LLMs including LLaMA-2, uncensored LLaMA, CodeLLaMA, Falcon, Mistral, Vicuna model, WizardCoder, and Wizard uncensored.

    https://ollama.com/library
    
    see also:
    https://klu.ai/glossary/ollama

### Usage

Console 

    ollama -h
    ollama pull llama2
    ollama list
    ollama run llama2

    Stop command: /bye

API

    curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{
        "model": "llama2",
        "prompt": "Why is the sky blue?"
    }'

WebUI 

    git clone https://github.com/ollama-webui/ollama-webui.git

    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v ollama-webui:/app/backend/data --name ollama-webui --restart always ghcr.io/ollama-webui/ollama-webui:main

![](../media/demo.gif)

WebUI lite

    git clone https://github.com/ollama-webui/ollama-webui-lite.git

    cd ollama-webui-lite
    pnpm i && pnpm run dev






