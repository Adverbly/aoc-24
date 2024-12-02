# Advent of code 2024

This year the trend towards easier/slower languages continues! With a newborn and a side project with a friend on the go, I think my only hope of finishing this year is to go full on "easy mode"(with the exception of using any LLM - we don't want to spoil the fun after all 😀). We went from rust to typescript/bun, and now we're at python! 

Rules: 

- lang: python 3.12 (latest supported by pytorch(torchaudio). jits allowed)
- allowed dependencies: numpy/pytorch, GPU-related libs(TBD)
- no LLMs
- preference for learning neovim, but falling back to vscode/pycharm with vim plugins if in a hurry

### Setup

```bash
curl https://pyenv.run | bash
pyenv install 3.12
pyenv use local 3.12
pip install --upgrade pip

##### CUDA GPU(my desktop. Will have access to this the first few days)

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu11

##### CPU (my laptop. AMD GPU. :cries in Nvdia monopoly)

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

python ./torch_test.py # validate install
```

#### Contributing

vi solutions/day-1/part-1/solve.py

#### Running

python solutions/day-1/part-1/solve.py

#### Running all solutions

TODO

#### Starting a new year
mkdir -p solutions/day_{1..25}/part_{1..2}
mkdir -p lib
touch solutions/day_{1..25}/part_{1..2}/question.md
touch solutions/day_{1..25}/part_{1..2}/solve.py
touch solutions/day_{1..25}/input.txt
touch solutions/day_{1..25}/part_{1..2}/example.txt


