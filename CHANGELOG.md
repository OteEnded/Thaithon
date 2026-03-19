# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.3.0] - 2026-03-19

### Added
- New module `เว็บ.py` — Thai wrapper for `urllib` (GET, POST, JSON, download, URL utilities)
- New module `อาร์กิวเมนต์.py` — Thai wrapper for `argparse`
- Extended `ระบบ.py` with subprocess functions: `รันกระบวนการ`, `รันและได้ผล`, `รันแบบเรียลไทม์`

## [0.2.0] - 2026-03-19

### Added
- New module `ระบบ.py` — Thai wrapper for `os` and `sys` (env vars, cwd, platform info, etc.)
- GitHub Actions CI workflow (`.github/workflows/test.yml`) — runs all tests on Python 3.10–3.13.
- Added Python 3.13 to supported classifiers in `pyproject.toml`.

### Fixed
- Renamed `มะรุ่งนี้()` in `เวลา.py` to `เวลาตอนนี้()` (old name kept as backward-compat alias).
- Removed unused imports (`timezone`, `datetime as dt_module`) from `เวลา.py`.

## [0.1.1] - 2026-03-19

### Added
- Added logo to README and PyPI project page.

### Changed
- Renamed package on PyPI from `pythai` to `thaithon`.

## [0.1.0]

### Added
- Organized project layout into libs/, tests/, examples/, tools/, and docs/.
- Added Thai wrappers for math, datetime/time, random, statistics, json, regex, file/path, and csv.
- Added repository baseline files: LICENSE, .editorconfig, .gitattributes, and CONTRIBUTING.

### Changed
- Updated examples and tests to import modules from libs/ reliably.
- Updated README with new structure and run instructions.
- Switched license from MIT to Apache-2.0 and added attribution files.
