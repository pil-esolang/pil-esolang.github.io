# pil-esolang.github.io
This is the website that hosts PIL's documentation. It can be found here: [https://pil-esolang.github.io/](https://pil-esolang.github.io/).

## Dependencies
- MkDocs Material
- minify plugin
- pymdown-extensions

Run `pip install -e .` in the same directory as `pyproject.toml`.
```bash
pip install mkdocs mkdocs-material mkdocs-minify-plugin pymdown-extensions
pip install -e .
```

## Local host
Local host with:
```pil
python -m mkdocs serve
```
And then open [localhost:8000](https://localhost:8000).

## Distribute
Distribute to Github with:
```pil
python -m mkdocs gh-deploy --force
```
This should push to branch `gh-pages`.

## Credits
This project was made by Daniel Vishnevsky and is licensed under MIT License.
