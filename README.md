# multiversion-lib

One repository shipping **two incompatible runtime lines of the same language**
as separate packages:

| Target | Source | Published package | Runtime line |
| --- | --- | --- | --- |
| `python2` | [`py2/`](py2/) | `zedtest/multiversion-lib-python2` | CPython 2.7 (`setup.py`, `python_requires=">=2.7, <3"`) |
| `python3` | [`py3/`](py3/) | `zedtest/multiversion-lib-python3` | CPython ≥3.9 (`pyproject.toml`, `requires-python`) |
| `node18` | [`node18/`](node18/) | `zedtest/multiversion-lib-node18` | Node ≥18 <22 (CommonJS) |
| `node22` | [`node22/`](node22/) | `zedtest/multiversion-lib-node22` | Node ≥22 (ESM + `node:` builtins) |

These genuinely cannot be one artifact: f-strings and type hints are a
`SyntaxError` on 2.7, and `import { sep } from "node:path"` in an ESM module does
not load on the pre-22 line.

## Why it is modelled this way

**zed has no version-constraint field.** There is no `engines`,
`requires_python`, `min_version`, or language-version key anywhere in the
manifest schema. So the only way to express "two runtime lines" today is one
target per line, which is what this fixture pins down — and the constraint that
actually gets enforced lives in each subtree's *native* manifest
(`python_requires`, `engines.node`), not in `.zpkg.toml`.

## The gap this fixture exists to catch

Verified against a real `zed publish` + `zed install`:

- A target named `nodejs` installs with `language: "nodejs"`, `ecosystem: "npm"`
  in the consumer's `.zed/paths.json`.
- A target named `node22` or `python2` installs with
  **`language: "universal"`, `ecosystem: "universal"`** — the tag is derived by
  matching the *target name* against a known language-token table, and
  `node22`/`python2` are not in it.

The consequence is not cosmetic. `polyglot-lib` demonstrates that zed refuses to
drop a `gomod` package into an npm project. That refusal is driven by exactly
those tags — so it **does not fire here**:

```console
$ # in a Node project, having asked for the python2 package
$ zed install
installed zedtest/multiversion-lib-python2@0.1.0
1 package(s) in .vendor/.zed/ (copied for container-safe layers)
```

A Python 2 source tree (`setup.py`, `mvlib/`) lands in a Node project and
nothing objects. Any fix — inferring the language from the subtree's marker
files, or a `language = "..."` key per target — should make this fixture's
negative case start failing.

## Shell / version managers

Deliberately out of scope for the manifest, and worth stating because it is the
obvious next question: zed does not shell out to `nvm`, `pyenv`, `gvm`, `asdf`,
or a virtualenv, and does not read or write `PATH`. It places source trees and
writes wiring files; selecting *which* interpreter then consumes them is the
caller's job — a CI matrix, an `.nvmrc`, or an activated venv. The four targets
here are what lets that caller ask for the right artifact once it has chosen.

## License

MIT
