# Qyet

<p align="center"><img src="docs/assets/logo.png" width="200"></p>

Python package with tools for suppressing output.

> shhh... please be qyet

## Installation

```bash
pip install qyet
```

## Usage

For now, there is only one decorator, `shhh`, which suppresses the output of a function.

```python
from qyet import shhh

@shhh
def foo():
    print("Hello, world!")

foo() # No output
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Thanks to

@dunossauro for a [great content (in pt_BR) on how to create a Python package](https://www.youtube.com/playlist?list=PLOQgLBuj2-3LiHhK1upnjpHiFzcJ472QS).
