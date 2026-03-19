# Contributing

## Dev Setup

1. Use Python 3.11+.
2. Run scripts from project root.
3. Keep source modules in libs/, tests in tests/, examples in examples/.

## Coding Rules

1. Preserve Thai function naming style and readability.
2. Prefer small wrapper functions with clear docstrings.
3. Keep compatibility aliases only when needed.
4. Avoid breaking existing public names in libs/.

## Testing

Run core smoke tests before commit:

```bash
python tests/test_helpers.py
python tests/test_math.py
python tests/test_data_libs.py
```

Then run all tests you changed.

## Pull Request Checklist

1. Tests pass locally.
2. README updated if API behavior changed.
3. New public function added to __all__.
4. Keep root folder clean (no temp outputs).
