# ♻ ReciclAI 

## 📖 Visão Geral
- [Sobre o Projeto](#-sobre-o-projeto)
- [O que foi utilizado](#-o-que-foi-utilizado)
- [Recomendações](#-recomendações)
- [Requisitos do projeto](#Requisitos-do-projeto)
- [Instalação dos Requisitos](#-instalacao-dos-requisitos)
- [Como executar o projeto](#-como-executar-o-projeto)


## 📚 Sobre o Projeto

O ReciclAI tem como objetivo utilizar um modelo de IA desenvolvido com o YOLOv8 para a detecção de garrafas de plástico, contribuindo para a preservação do meio ambiente. O foco principal é criar uma solução eficaz para identificar e categorizar garrafas de plástico em diversos ambientes, facilitando o processo de reciclagem e promovendo práticas sustentáveis.
> **O projeto é estritamente acadêmico e visa promover o conhecimento na área de inteligência artificial aplicada à sustentabilidade.**


## 🛠 O que foi utilizado
- [Python](https://www.python.org/downloads/) - Código desenvolvido em Python🐍.

- [Arduino](https://www.arduino.cc/en/software) - O código é responsável por acionar o motor para abrir uma lixeira ao detectar um objeto.

- [Roboflow](https://roboflow.com) - Responsável por criar a demarcação das imagens para o treinamento do modelo.

## ❗ Recomendações 

>Recomenda-se utilizar uma GPU da NVIDIA para reduzir o atraso na transmissão de vídeos em tempo real.

> Recomenda-se o uso de uma máquina virtual.

```bash
pip install virtualenv
```


## Requisitos do projeto


### Instalacao dos Requisitos

```bash
pip install -r requirements.txt
```


### Instalação do Torch para funcionamento da CUDA (Compute Unified Device Architecture) - **Somente para GPU Nvidia**

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

<h4 align="center"> 
	🚨 Em caso de erro ao detectar o objeto, utilize:
</h4>

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 🚀 Como executar o projeto

```bash
# Clonando o repositório
$ git clone 

# Entrando no diretório  
$ cd ReciclAI
```

```python
# Criando a máquina virtual dentro da pasta do projeto
python -m venv .venv 

# Ativando a máquina virtual
.venv\Scripts\activate

# Instalando os requisitos necessários 
pip install -r requirements.txt

# Instalando o PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Em caso de erro ao detectar o objeto
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
```python
# Rodando o código 
python Reciclai.py
```

> Algumas alterações no código podem ser necessárias, dependendo da câmera utilizada e da porta em que o Arduino (se aplicável) está instalado.
